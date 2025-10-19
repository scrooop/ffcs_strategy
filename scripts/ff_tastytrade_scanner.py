#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ff_tastytrade_scanner.py
# A forward-volatility (FF) scanner that uses the official tastytrade API + dxFeed streamer.
# It fetches ATM IV for two expirations (closest to target DTEs), computes forward IV,
# and reports FF = (FrontATMIV - FwdIV) / FwdIV for each requested ticker.
#
# Requirements:
#   pip install tastytrade
#
# Auth:
#   Provide credentials via env vars: TT_USERNAME, TT_PASSWORD
#   (Production is used by default; pass --sandbox to use the sandbox environment.)
#
# Usage examples:
#   python ff_tastytrade_scanner.py --tickers SPY QQQ --pairs 30-60 30-90 60-90 --min-ff 0.20
#
# Notes:
#   * Greeks.volatility from dxFeed is Black-Scholes IV per contract.
#   * NestedOptionChain is used to find expirations & strikes; we pick the strike nearest to spot.
#   * If Greeks for a leg fail to arrive within the timeout, the row is skipped or marked partial.
#
# DISCLAIMER: For educational use. Trading involves risk.

import os
import sys
import math
import json
import asyncio
import argparse
from dataclasses import dataclass
from datetime import date
from typing import Dict, List, Tuple, Optional

from tastytrade import Session, DXLinkStreamer
from tastytrade.market_data import get_market_data
from tastytrade.order import InstrumentType
from tastytrade.instruments import NestedOptionChain
from tastytrade.dxfeed import Greeks
from tastytrade.utils import today_in_new_york

# ---------- Helpers ----------

def ny_today() -> date:
    """Return today's date in America/New_York (broker convention)."""
    return today_in_new_york()

def dte(exp: date, ref: Optional[date] = None) -> int:
    """Days to expiration from ref (New York date)."""
    if ref is None:
        ref = ny_today()
    return (exp - ref).days

def parse_pairs(pairs: List[str]) -> List[Tuple[int, int]]:
    out: List[Tuple[int, int]] = []
    for p in pairs:
        a, b = p.split("-")
        a, b = int(a), int(b)
        if a >= b:
            raise ValueError(f"Pair must be ascending DTEs like 30-60, got {p}")
        out.append((a, b))
    return out

@dataclass(frozen=True)
class ATMChoice:
    expiration: date
    strike: float
    call_streamer_symbol: str
    put_streamer_symbol: str
    dte: int

def nearest_expiration(chain, target_dte: int, dte_tolerance: int) -> Optional[date]:
    """
    Pick the expiration date whose DTE is closest to target_dte within tolerance.
    `chain` is a NestedOptionChain. We access `chain.expirations`, each with .expiration_date.
    """
    today = ny_today()
    best_exp = None
    best_err = None
    for exp in chain.expirations:
        err = abs((exp.expiration_date - today).days - target_dte)
        if best_err is None or err < best_err:
            best_err, best_exp = err, exp.expiration_date
    if best_err is not None and best_err <= dte_tolerance:
        return best_exp
    return None

def pick_atm_strike(expiration_obj, spot: float) -> Tuple[float, str, str]:
    """
    From a NestedOptionChain expiration, choose the strike closest to spot.
    Return (strike, call_streamer_symbol, put_streamer_symbol).
    """
    best = None
    best_err = None
    for s in expiration_obj.strikes:
        strike = float(s.strike_price)
        err = abs(strike - spot)
        if best_err is None or err < best_err:
            best_err = err
            best = (strike, s.call_streamer_symbol, s.put_streamer_symbol)
    if best is None:
        raise RuntimeError("No strikes found in expiration.")
    return best

async def snapshot_greeks(session: Session, streamer_symbols: List[str], timeout_s: float = 3.0) -> Dict[str, Greeks]:
    """
    Subscribe to Greeks for `streamer_symbols` once and collect a single snapshot.
    Returns a dict mapping event_symbol -> Greeks.
    """
    results: Dict[str, Greeks] = {}
    async with DXLinkStreamer(session) as streamer:
        if streamer_symbols:
            await streamer.subscribe(Greeks, streamer_symbols)

            async def collector():
                async for g in streamer.listen(Greeks):
                    results[g.event_symbol] = g
                    if len(results) >= len(streamer_symbols):
                        break

            try:
                await asyncio.wait_for(collector(), timeout=timeout_s)
            except asyncio.TimeoutError:
                # partial results are okay; caller will decide how to handle
                pass
    return results

def forward_iv(iv_front: float, iv_back: float, dte_front: int, dte_back: int) -> Optional[float]:
    """
    Compute forward IV between two expirations using annualized vols.
    T = DTE/365.  IVs are decimals (e.g., 0.25 for 25%).
    """
    if iv_front <= 0 or iv_back <= 0 or dte_back <= dte_front:
        return None
    T1 = dte_front / 365.0
    T2 = dte_back / 365.0
    try:
        num = (T2 * (iv_back ** 2)) - (T1 * (iv_front ** 2))
        den = (T2 - T1)
        if num <= 0 or den <= 0:
            return None
        return math.sqrt(num / den)
    except Exception:
        return None

# ---------- Main scan ----------

async def scan(session: Session, tickers: List[str], pairs: List[Tuple[int, int]],
               min_ff: float, dte_tolerance: int, timeout_s: float) -> List[dict]:
    rows: List[dict] = []
    today = ny_today()

    for sym in tickers:
        # 1) Underlying spot
        md = get_market_data(session, sym, InstrumentType.EQUITY)
        if md is None or md.last is None:
            print(f"[WARN] No quote for {sym}, skipping.", file=sys.stderr)
            continue
        spot = float(md.last) if md.last is not None else float(md.mark)
        # 2) Chain (nested)
        chain_list = NestedOptionChain.get(session, sym)
        if not chain_list:
            print(f"[WARN] No option chain for {sym}, skipping.", file=sys.stderr)
            continue
        chain = chain_list[0]  # API returns a list; take first element

        # Pre-index expirations by date for fast lookup
        exp_by_date = {exp.expiration_date: exp for exp in chain.expirations}

        # 3) For each unique DTE in pairs, pick an expiration within tolerance and its ATM strike
        required_targets = sorted(set([t for pair in pairs for t in pair]))
        choices: Dict[int, ATMChoice] = {}
        streamer_syms: List[str] = []

        for target in required_targets:
            exp_date = nearest_expiration(chain, target, dte_tolerance)
            if exp_date is None:
                continue
            exp_obj = exp_by_date[exp_date]
            strike, call_sym, put_sym = pick_atm_strike(exp_obj, spot)
            choices[target] = ATMChoice(
                expiration=exp_date,
                strike=strike,
                call_streamer_symbol=call_sym,
                put_streamer_symbol=put_sym,
                dte=dte(exp_date, today),
            )
            streamer_syms.extend([call_sym, put_sym])

        if not choices:
            print(f"[WARN] No expirations matched tolerance for {sym}", file=sys.stderr)
            continue

        # 4) Snapshot Greeks (to get IV) for all needed ATM contracts
        greek_map = await snapshot_greeks(session, streamer_syms, timeout_s=timeout_s)

        # 5) Compute ATM IV per target DTE and then compute forward IV + FF for each pair
        atm_iv_by_target: Dict[int, float] = {}

        for target, ch in choices.items():
            call_iv = None
            put_iv = None
            if ch.call_streamer_symbol in greek_map:
                call_iv = float(greek_map[ch.call_streamer_symbol].volatility or 0.0)
            if ch.put_streamer_symbol in greek_map:
                put_iv = float(greek_map[ch.put_streamer_symbol].volatility or 0.0)

            # If both present, average; if one present, use it.
            ivs = [v for v in [call_iv, put_iv] if v and v > 0]
            if not ivs:
                continue
            atm_iv_by_target[target] = sum(ivs) / len(ivs)

        # 6) Build rows for pairs
        for front, back in pairs:
            if front not in choices or back not in choices:
                continue
            if front not in atm_iv_by_target or back not in atm_iv_by_target:
                continue

            front_choice = choices[front]
            back_choice = choices[back]
            iv_f = atm_iv_by_target[front]
            iv_b = atm_iv_by_target[back]

            fwd = forward_iv(iv_f, iv_b, front_choice.dte, back_choice.dte)
            if fwd is None:
                continue
            ff = (iv_f - fwd) / fwd if fwd > 0 else None
            if ff is None:
                continue
            if ff >= min_ff:
                rows.append({
                    "symbol": sym,
                    "front_target_dte": front,
                    "front_exp": front_choice.expiration.isoformat(),
                    "front_dte": front_choice.dte,
                    "front_atm_strike": f"{front_choice.strike:.2f}",
                    "front_atm_iv": round(iv_f, 6),
                    "back_target_dte": back,
                    "back_exp": back_choice.expiration.isoformat(),
                    "back_dte": back_choice.dte,
                    "back_atm_strike": f"{back_choice.strike:.2f}",
                    "back_atm_iv": round(iv_b, 6),
                    "fwd_iv": round(fwd, 6),
                    "ff_ratio": round(ff, 6),
                })

    # Sort by highest FF
    rows.sort(key=lambda r: r["ff_ratio"], reverse=True)
    return rows

def read_list_arg(values: List[str]) -> List[str]:
    # Allow comma-separated or repeated flags
    out: List[str] = []
    for v in values:
        out.extend([x for x in v.split(",") if x])
    return [x.strip().upper() for x in out if x.strip()]

def main():
    ap = argparse.ArgumentParser(description="Forward-IV (FF) scanner using tastytrade API + dxFeed greeks.")
    ap.add_argument("--tickers", nargs="+", required=True, help="List of underlyings. You can comma-separate or space-separate.")
    ap.add_argument("--pairs", nargs="+", required=True, help="DTE pairs like 30-60 30-90 (front-back).")
    ap.add_argument("--min-ff", type=float, default=0.20, help="Minimum FF ratio to include (default: 0.20).")
    ap.add_argument("--dte-tolerance", type=int, default=5, help="Max absolute deviation allowed from target DTE (default: 5 days).")
    ap.add_argument("--timeout", type=float, default=3.0, help="Streamer snapshot timeout in seconds (default: 3s).")
    ap.add_argument("--sandbox", action="store_true", help="Use sandbox instead of production.")
    ap.add_argument("--json-out", type=str, default="", help="Optional path to write JSON results.")
    ap.add_argument("--csv-out", type=str, default="", help="Optional path to write CSV results.")

    args = ap.parse_args()
    tickers = read_list_arg(args.tickers)
    pairs = parse_pairs(read_list_arg(args.pairs))

    username = os.environ.get("TT_USERNAME", "").strip()
    password = os.environ.get("TT_PASSWORD", "").strip()
    if not username or not password:
        print("ERROR: Set TT_USERNAME and TT_PASSWORD env vars.", file=sys.stderr)
        sys.exit(2)

    # Create session
    session = Session(username, password=password, is_test=bool(args.sandbox))

    # Run scan
    rows = asyncio.run(scan(session, tickers, pairs, args.min_ff, args.dte_tolerance, args.timeout))

    # Print results
    cols = [
        "symbol", "front_target_dte", "front_exp", "front_dte", "front_atm_strike", "front_atm_iv",
        "back_target_dte", "back_exp", "back_dte", "back_atm_strike", "back_atm_iv",
        "fwd_iv", "ff_ratio",
    ]

    if not rows:
        print("No results passing filters.")
    else:
        print(",".join(cols))
        for r in rows:
            print(",".join(str(r[c]) for c in cols))

    # Optional outputs
    if args.json_out and rows:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(rows, f, indent=2)
        print(f"Wrote JSON -> {args.json_out}", file=sys.stderr)

    if args.csv_out and rows:
        import csv
        with open(args.csv_out, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(rows)
        print(f"Wrote CSV -> {args.csv_out}", file=sys.stderr)

if __name__ == "__main__":
    main()
