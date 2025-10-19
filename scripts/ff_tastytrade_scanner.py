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

# ---------- Double Calendar Strike Selection (Issue #4) ----------

@dataclass(frozen=True)
class DeltaStrikeChoice:
    """Represents a strike selected by delta for double calendars."""
    strike: float
    streamer_symbol: str
    actual_delta: float
    iv: float

def pick_delta_strike(
    expiration_obj,
    greek_map: Dict[str, Greeks],
    target_delta: float,
    delta_tolerance: float = 0.05,
    option_type: str = "call"
) -> Optional[DeltaStrikeChoice]:
    """
    From a NestedOptionChain expiration, choose the strike closest to target delta.

    Args:
        expiration_obj: NestedOptionChain expiration object with strikes
        greek_map: Dict mapping streamer_symbol -> Greeks (with delta values)
        target_delta: Target delta (e.g., 0.35 for +35Δ call, -0.35 for -35Δ put)
        delta_tolerance: Maximum deviation from target delta (default 0.05 = ±5Δ)
        option_type: "call" or "put"

    Returns:
        DeltaStrikeChoice or None if no strike within tolerance
    """
    best = None
    best_err = None

    for s in expiration_obj.strikes:
        strike = float(s.strike_price)
        symbol = s.call_streamer_symbol if option_type == "call" else s.put_streamer_symbol

        if symbol not in greek_map:
            continue

        greeks = greek_map[symbol]
        if greeks.delta is None or greeks.volatility is None:
            continue

        actual_delta = float(greeks.delta)
        iv = float(greeks.volatility)
        err = abs(actual_delta - target_delta)

        if err <= delta_tolerance and (best_err is None or err < best_err):
            best_err = err
            best = DeltaStrikeChoice(
                strike=strike,
                streamer_symbol=symbol,
                actual_delta=actual_delta,
                iv=iv
            )

    return best

async def snapshot_greeks_for_range(
    session: Session,
    expiration_obj,
    spot: float,
    range_pct: float = 0.25,
    timeout_s: float = 5.0
) -> Dict[str, Greeks]:
    """
    Fetch Greeks for a range of strikes around spot price.

    Args:
        session: tastytrade Session
        expiration_obj: NestedOptionChain expiration object
        spot: Current underlying spot price
        range_pct: Percentage range around spot (default 0.25 = ±25%)
        timeout_s: Timeout for Greeks snapshot

    Returns:
        Dict mapping streamer_symbol -> Greeks for all strikes in range
    """
    lower_bound = spot * (1 - range_pct)
    upper_bound = spot * (1 + range_pct)

    streamer_symbols: List[str] = []
    for s in expiration_obj.strikes:
        strike = float(s.strike_price)
        if lower_bound <= strike <= upper_bound:
            streamer_symbols.extend([s.call_streamer_symbol, s.put_streamer_symbol])

    if not streamer_symbols:
        return {}

    return await snapshot_greeks(session, streamer_symbols, timeout_s=timeout_s)

async def get_double_calendar_strikes(
    session: Session,
    expiration_obj,
    spot: float,
    call_target_delta: float = 0.35,
    put_target_delta: float = -0.35,
    delta_tolerance: float = 0.05,
    timeout_s: float = 5.0
) -> Dict[str, Optional[DeltaStrikeChoice]]:
    """
    Get both ±35Δ strikes for a double calendar spread.

    Args:
        session: tastytrade Session
        expiration_obj: NestedOptionChain expiration object
        spot: Current underlying spot price
        call_target_delta: Target delta for call leg (default 0.35 = +35Δ)
        put_target_delta: Target delta for put leg (default -0.35 = -35Δ)
        delta_tolerance: Maximum deviation from target delta (default 0.05 = ±5Δ)
        timeout_s: Timeout for Greeks snapshot

    Returns:
        Dict with keys "call_35delta" and "put_35delta", values are DeltaStrikeChoice or None
    """
    # Fetch Greeks for a wide range of strikes
    greek_map = await snapshot_greeks_for_range(session, expiration_obj, spot, timeout_s=timeout_s)

    # Find strikes matching target deltas
    call_strike = pick_delta_strike(
        expiration_obj, greek_map, call_target_delta, delta_tolerance, "call"
    )
    put_strike = pick_delta_strike(
        expiration_obj, greek_map, put_target_delta, delta_tolerance, "put"
    )

    return {
        "call_35delta": call_strike,
        "put_35delta": put_strike
    }

# ---------- Main scan ----------

async def scan(session: Session, tickers: List[str], pairs: List[Tuple[int, int]],
               min_ff: float, dte_tolerance: int, timeout_s: float,
               double_calendar: bool = False, delta_tolerance: float = 0.05) -> List[dict]:
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

        required_targets = sorted(set([t for pair in pairs for t in pair]))

        if double_calendar:
            # ---------- DOUBLE CALENDAR MODE ----------
            # 3) For each unique DTE, get delta strikes (±35Δ)
            delta_choices: Dict[int, Dict[str, Optional[DeltaStrikeChoice]]] = {}

            for target in required_targets:
                exp_date = nearest_expiration(chain, target, dte_tolerance)
                if exp_date is None:
                    continue
                exp_obj = exp_by_date[exp_date]

                # Get ±35Δ strikes
                delta_strikes = await get_double_calendar_strikes(
                    session=session,
                    expiration_obj=exp_obj,
                    spot=spot,
                    call_target_delta=0.35,
                    put_target_delta=-0.35,
                    delta_tolerance=delta_tolerance,
                    timeout_s=timeout_s
                )

                # Store with expiration info
                delta_choices[target] = {
                    "expiration": exp_date,
                    "dte": dte(exp_date, today),
                    "call_35delta": delta_strikes["call_35delta"],
                    "put_35delta": delta_strikes["put_35delta"]
                }

            if not delta_choices:
                print(f"[WARN] No expirations matched tolerance for {sym}", file=sys.stderr)
                continue

            # 4) Build rows for double calendar pairs
            for front, back in pairs:
                if front not in delta_choices or back not in delta_choices:
                    continue

                front_choice = delta_choices[front]
                back_choice = delta_choices[back]

                # Check if we have both call and put strikes for both expirations
                front_call = front_choice["call_35delta"]
                back_call = back_choice["call_35delta"]
                front_put = front_choice["put_35delta"]
                back_put = back_choice["put_35delta"]

                # We need at least one complete calendar (call or put)
                has_call_calendar = front_call is not None and back_call is not None
                has_put_calendar = front_put is not None and back_put is not None

                if not (has_call_calendar or has_put_calendar):
                    continue

                # Process call calendar
                if has_call_calendar:
                    fwd_call = forward_iv(front_call.iv, back_call.iv, front_choice["dte"], back_choice["dte"])
                    if fwd_call and fwd_call > 0:
                        ff_call = (front_call.iv - fwd_call) / fwd_call
                        if ff_call >= min_ff:
                            rows.append({
                                "symbol": sym,
                                "calendar_type": "call",
                                "front_target_dte": front,
                                "front_exp": front_choice["expiration"].isoformat(),
                                "front_dte": front_choice["dte"],
                                "front_strike": f"{front_call.strike:.2f}",
                                "front_delta": round(front_call.actual_delta, 4),
                                "front_iv": round(front_call.iv, 6),
                                "back_target_dte": back,
                                "back_exp": back_choice["expiration"].isoformat(),
                                "back_dte": back_choice["dte"],
                                "back_strike": f"{back_call.strike:.2f}",
                                "back_delta": round(back_call.actual_delta, 4),
                                "back_iv": round(back_call.iv, 6),
                                "fwd_iv": round(fwd_call, 6),
                                "ff_ratio": round(ff_call, 6),
                            })

                # Process put calendar
                if has_put_calendar:
                    fwd_put = forward_iv(front_put.iv, back_put.iv, front_choice["dte"], back_choice["dte"])
                    if fwd_put and fwd_put > 0:
                        ff_put = (front_put.iv - fwd_put) / fwd_put
                        if ff_put >= min_ff:
                            rows.append({
                                "symbol": sym,
                                "calendar_type": "put",
                                "front_target_dte": front,
                                "front_exp": front_choice["expiration"].isoformat(),
                                "front_dte": front_choice["dte"],
                                "front_strike": f"{front_put.strike:.2f}",
                                "front_delta": round(front_put.actual_delta, 4),
                                "front_iv": round(front_put.iv, 6),
                                "back_target_dte": back,
                                "back_exp": back_choice["expiration"].isoformat(),
                                "back_dte": back_choice["dte"],
                                "back_strike": f"{back_put.strike:.2f}",
                                "back_delta": round(back_put.actual_delta, 4),
                                "back_iv": round(back_put.iv, 6),
                                "fwd_iv": round(fwd_put, 6),
                                "ff_ratio": round(ff_put, 6),
                            })

        else:
            # ---------- ATM CALENDAR MODE ----------
            # 3) For each unique DTE in pairs, pick an expiration within tolerance and its ATM strike
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
    ap.add_argument("--double-calendar", action="store_true", help="Scan for double calendars at ±35Δ instead of ATM calendars.")
    ap.add_argument("--delta-tolerance", type=float, default=0.05, help="Delta tolerance for double calendars (default: 0.05 = ±5Δ).")
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
    rows = asyncio.run(scan(
        session, tickers, pairs, args.min_ff, args.dte_tolerance, args.timeout,
        double_calendar=args.double_calendar,
        delta_tolerance=args.delta_tolerance
    ))

    # Print results
    if args.double_calendar:
        cols = [
            "symbol", "calendar_type", "front_target_dte", "front_exp", "front_dte",
            "front_strike", "front_delta", "front_iv",
            "back_target_dte", "back_exp", "back_dte",
            "back_strike", "back_delta", "back_iv",
            "fwd_iv", "ff_ratio",
        ]
    else:
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
