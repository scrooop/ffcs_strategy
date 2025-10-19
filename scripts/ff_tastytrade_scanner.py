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
from datetime import date, datetime
from typing import Dict, List, Tuple, Optional

from tastytrade import Session, DXLinkStreamer
from tastytrade.market_data import get_market_data
from tastytrade.metrics import get_market_metrics
from tastytrade.order import InstrumentType
from tastytrade.instruments import NestedOptionChain, NestedFutureOptionChain
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
    """
    Parse DTE pair strings into tuples of integers.

    Args:
        pairs: List of DTE pair strings (e.g., ['30-60', '30-90', '60-90'])

    Returns:
        List of (front_dte, back_dte) tuples

    Raises:
        ValueError: If pair is not ascending (e.g., '60-30') or invalid format

    Example:
        >>> parse_pairs(['30-60', '60-90'])
        [(30, 60), (60, 90)]
    """
    out: List[Tuple[int, int]] = []
    for p in pairs:
        a, b = p.split("-")
        a, b = int(a), int(b)
        if a >= b:
            raise ValueError(f"Pair must be ascending DTEs like 30-60, got {p}")
        out.append((a, b))
    return out

def is_futures_symbol(symbol: str) -> bool:
    """
    Check if symbol is a futures symbol.

    Futures symbols start with '/' (e.g., /ES, /GC, /NQ, /CL).
    Equity symbols do not (e.g., SPY, QQQ, AAPL).

    Args:
        symbol: The symbol to check

    Returns:
        True if symbol is a futures symbol, False otherwise

    Example:
        >>> is_futures_symbol('/ES')
        True
        >>> is_futures_symbol('SPY')
        False
    """
    return symbol.startswith('/')

def get_futures_spot_price(session: Session, symbol: str) -> Optional[float]:
    """
    Get spot price for a futures symbol from the active (front-month) contract.

    Uses NestedFutureOptionChain to find the active contract, then fetches
    market data for that specific contract symbol (e.g., /ESZ5 for /ES).

    Args:
        session: tastytrade Session object
        symbol: Futures root symbol (e.g., '/ES', '/GC', '/NQ')

    Returns:
        The last traded price of the active futures contract, or None if unavailable

    Raises:
        None - returns None on any error

    Example:
        >>> session = Session('username', 'password')
        >>> price = get_futures_spot_price(session, '/ES')
        >>> print(f'/ES spot: {price}')
        /ES spot: 4521.50
    """
    try:
        # Get futures option chain to find the active contract
        chain = NestedFutureOptionChain.get(session, symbol)
        if not chain or not chain.futures:
            print(f"[WARN] No futures chain found for {symbol}", file=sys.stderr)
            return None

        # Find the active month contract
        active_contract = None
        for future in chain.futures:
            if hasattr(future, 'active_month') and future.active_month:
                active_contract = future.symbol
                break

        if not active_contract:
            print(f"[WARN] No active contract found for {symbol}", file=sys.stderr)
            return None

        # Get market data for the active contract (e.g., /ESZ5)
        md = get_market_data(session, active_contract, InstrumentType.FUTURE)

        if md is None or md.last is None:
            print(f"[WARN] No quote for active contract {active_contract}", file=sys.stderr)
            return None

        return float(md.last) if md.last is not None else float(md.mark)

    except Exception as e:
        print(f"[ERROR] Failed to get futures spot price for {symbol}: {e}", file=sys.stderr)
        return None

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

async def snapshot_greeks(session: Session, streamer_symbols: List[str], timeout_s: float = 3.0) -> Dict[str, Tuple[float, float]]:
    """
    Subscribe to Greeks for `streamer_symbols` once and collect a single snapshot.

    Args:
        session: Active tastytrade session
        streamer_symbols: List of dxFeed streamer symbols for options
        timeout_s: Timeout in seconds for snapshot collection

    Returns:
        Dict mapping event_symbol -> (iv, delta) tuple
        - iv: Implied volatility (decimal, e.g., 0.25 = 25%)
        - delta: Option delta (decimal, e.g., 0.50 = 50 delta)
        Both values may be None if unavailable.

    Note:
        Partial results are acceptable on timeout. Caller should handle missing data.
    """
    raw_results: Dict[str, Greeks] = {}
    async with DXLinkStreamer(session) as streamer:
        if streamer_symbols:
            await streamer.subscribe(Greeks, streamer_symbols)

            async def collector():
                async for g in streamer.listen(Greeks):
                    raw_results[g.event_symbol] = g
                    if len(raw_results) >= len(streamer_symbols):
                        break

            try:
                await asyncio.wait_for(collector(), timeout=timeout_s)
            except asyncio.TimeoutError:
                # partial results are okay; caller will decide how to handle
                pass

    # Extract (iv, delta) tuples from Greeks objects
    results: Dict[str, Tuple[float, float]] = {}
    for symbol, greeks in raw_results.items():
        iv = float(greeks.volatility) if greeks.volatility is not None else None
        delta = float(greeks.delta) if greeks.delta is not None else None
        results[symbol] = (iv, delta)

    return results

def forward_iv(iv_front: float, iv_back: float, dte_front: int, dte_back: int) -> Optional[float]:
    """
    Compute forward implied volatility between two expirations using variance decomposition.

    Uses the formula: σ_fwd = sqrt((T2·σ2² - T1·σ1²) / (T2 - T1))
    where T = DTE/365 (annualized time).

    Args:
        iv_front: Front expiration IV (decimal, e.g., 0.25 = 25%)
        iv_back: Back expiration IV (decimal, e.g., 0.25 = 25%)
        dte_front: Days to front expiration
        dte_back: Days to back expiration

    Returns:
        Forward IV as decimal (e.g., 0.25 = 25%), or None if calculation invalid

    Raises:
        None (returns None on any error)

    Example:
        >>> forward_iv(0.30, 0.25, 30, 60)
        0.2041...  # Forward IV for 30-60 DTE window
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

# ---------- Double Calendar Strike Selection ----------

@dataclass(frozen=True)
class DeltaStrikeChoice:
    """Represents a strike selected by delta for double calendars."""
    strike: float
    streamer_symbol: str
    actual_delta: float
    iv: float

def pick_delta_strike(
    expiration_obj,
    greeks_map: Dict[str, Tuple[float, float]],
    target_delta: float,
    delta_tolerance: float = 0.05,
    option_type: str = "call"
) -> Optional[DeltaStrikeChoice]:
    """
    From a NestedOptionChain expiration, choose the strike closest to target delta.

    Args:
        expiration_obj: NestedOptionChain expiration object with strikes
        greeks_map: Dict mapping streamer_symbol → (iv, delta) tuples
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

        if symbol not in greeks_map:
            continue

        iv, delta = greeks_map[symbol]
        if delta is None or iv is None:
            continue

        err = abs(delta - target_delta)

        if err <= delta_tolerance and (best_err is None or err < best_err):
            best_err = err
            best = DeltaStrikeChoice(
                strike=strike,
                streamer_symbol=symbol,
                actual_delta=delta,
                iv=iv
            )

    return best

async def snapshot_greeks_for_range(
    session: Session,
    expiration_obj,
    spot: float,
    range_pct: float = 0.25,
    timeout_s: float = 5.0
) -> Dict[str, Tuple[float, float]]:
    """
    Fetch Greeks (IV and delta) for a range of strikes around current spot price.

    Used for delta-based strike selection in double calendar spreads. Fetches
    Greeks for both calls and puts within ±range_pct of spot price.

    Args:
        session: Active tastytrade session
        expiration_obj: NestedOptionChain expiration object containing strikes
        spot: Current underlying spot price
        range_pct: Percentage range around spot (default 0.25 = ±25%)
                   Example: spot=100, range_pct=0.25 → fetch strikes 75-125
        timeout_s: Timeout for Greeks snapshot in seconds (default 5.0)

    Returns:
        Dict mapping streamer_symbol → (iv, delta) tuple
        - iv: Implied volatility (decimal, e.g., 0.25 = 25%)
        - delta: Option delta (decimal, e.g., 0.35 = +35Δ call)
        Returns empty dict {} if no strikes in range

    Raises:
        None (returns partial results on timeout, empty dict if no strikes found)

    Example:
        >>> greeks = await snapshot_greeks_for_range(session, exp_obj, spot=100.0)
        >>> len(greeks)  # Number of option contracts with Greeks data
        42
        >>> greeks['.SPY251121C100']
        (0.25, 0.50)  # (IV=25%, delta=50Δ)
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
    Find both call and put strikes matching target deltas for double calendar spreads.

    Double calendar structure: Sell front ±35Δ call/put, buy back ±35Δ call/put.
    This function finds strikes closest to the target deltas within tolerance.

    Args:
        session: Active tastytrade session
        expiration_obj: NestedOptionChain expiration object containing strikes
        spot: Current underlying spot price
        call_target_delta: Target delta for call leg (default 0.35 = +35Δ)
        put_target_delta: Target delta for put leg (default -0.35 = -35Δ)
        delta_tolerance: Max deviation from target (default 0.05 = ±5Δ)
                        Example: 0.35 target with 0.05 tolerance → accept 0.30-0.40
        timeout_s: Timeout for Greeks snapshot in seconds (default 5.0)

    Returns:
        Dict with keys:
        - "call_35delta": DeltaStrikeChoice for call leg, or None if not found
        - "put_35delta": DeltaStrikeChoice for put leg, or None if not found

    Raises:
        None (returns None values if strikes not found within tolerance)

    Example:
        >>> strikes = await get_double_calendar_strikes(session, exp_obj, spot=100.0)
        >>> strikes['call_35delta']
        DeltaStrikeChoice(strike=105.0, streamer_symbol='.SPY251121C105',
                         actual_delta=0.34, iv=0.25)
        >>> strikes['put_35delta']
        DeltaStrikeChoice(strike=95.0, streamer_symbol='.SPY251121P95',
                         actual_delta=-0.35, iv=0.24)
    """
    # Fetch Greeks for a wide range of strikes
    greeks_map = await snapshot_greeks_for_range(session, expiration_obj, spot, timeout_s=timeout_s)

    # Find strikes matching target deltas
    call_strike = pick_delta_strike(
        expiration_obj, greeks_map, call_target_delta, delta_tolerance, "call"
    )
    put_strike = pick_delta_strike(
        expiration_obj, greeks_map, put_target_delta, delta_tolerance, "put"
    )

    return {
        "call_35delta": call_strike,
        "put_35delta": put_strike
    }

# ---------- Market Metrics & Filtering ----------

def fetch_market_metrics(session: Session, symbols: List[str]) -> Dict[str, any]:
    """
    Batch fetch earnings dates, liquidity ratings, and X-earn IV data for all symbols.

    Calls tastytrade's get_market_metrics() API to retrieve:
    - Earnings dates (earnings.expected_report_date)
    - Liquidity ratings (0-5 scale)
    - X-earn IV by expiration (option_expiration_implied_volatilities)

    Args:
        session: Active tastytrade session (must be authenticated)
        symbols: List of ticker symbols (e.g., ['SPY', 'QQQ', 'AAPL'])

    Returns:
        Dict mapping symbol → MarketMetricInfo object
        Returns empty dict {} on API failure (never crashes)

    Raises:
        None (logs error to stderr and returns empty dict on failure)

    Example:
        >>> metrics = fetch_market_metrics(session, ['SPY', 'QQQ'])
        >>> metrics['SPY'].liquidity_rating
        5
        >>> metrics['SPY'].earnings.expected_report_date
        date(2025, 10, 25)
    """
    try:
        metrics = get_market_metrics(session, symbols)
        if not metrics:
            return {}
        # Convert list to dict for easy lookup
        return {m.symbol: m for m in metrics if m.symbol}
    except Exception as e:
        print(f"[ERROR] Market metrics fetch failed: {e}", file=sys.stderr)
        return {}

def check_earnings_conflict(
    symbol: str,
    metrics: Dict[str, any],
    back_expiry: date,
    today: date
) -> Tuple[bool, Optional[str]]:
    """
    Check if earnings announcement falls between today and back expiration (inclusive).

    Calendar spreads should avoid holding through earnings announcements to prevent
    unexpected IV crush and P&L volatility. This function checks if the expected
    earnings date falls within the trade window.

    Args:
        symbol: Ticker symbol (e.g., 'AAPL')
        metrics: Market metrics dict from fetch_market_metrics()
        back_expiry: Back leg expiration date (end of trade window)
        today: Current date in NY timezone (start of trade window)

    Returns:
        Tuple of (passes_filter, reason_string):
        - (True, None): No conflict detected OR earnings data unavailable
        - (False, reason): Earnings conflict detected with explanation

    Raises:
        None (gracefully handles missing data with warnings to stderr)

    Example:
        >>> # Earnings on 2025-11-01, back expiry 2025-11-15
        >>> check_earnings_conflict('AAPL', metrics, date(2025, 11, 15), date(2025, 10, 20))
        (False, 'Earnings on 2025-11-01 conflicts with back expiry 2025-11-15')

        >>> # Earnings on 2025-12-01, back expiry 2025-11-15 (no conflict)
        >>> check_earnings_conflict('AAPL', metrics, date(2025, 11, 15), date(2025, 10, 20))
        (True, None)
    """
    if symbol not in metrics:
        # No metrics data - log warning but allow through
        print(f"[WARN] {symbol}: Market metrics unavailable, skipping earnings check", file=sys.stderr)
        return (True, None)

    metric_info = metrics[symbol]

    # Check if earnings attribute exists
    earnings = getattr(metric_info, 'earnings', None)
    if earnings is None:
        print(f"[WARN] {symbol}: Earnings data unavailable, skipping earnings check", file=sys.stderr)
        return (True, None)

    # Get expected_report_date from earnings object
    earnings_date = getattr(earnings, 'expected_report_date', None)
    if earnings_date is None:
        print(f"[WARN] {symbol}: Earnings date unavailable, skipping earnings check", file=sys.stderr)
        return (True, None)

    # Check if earnings falls in the window
    if today <= earnings_date <= back_expiry:
        reason = f"Earnings on {earnings_date} conflicts with back expiry {back_expiry}"
        return (False, reason)

    return (True, None)

def check_liquidity(
    symbol: str,
    metrics: Dict[str, any],
    min_rating: int
) -> Tuple[bool, Optional[str]]:
    """
    Check if symbol's liquidity rating meets minimum threshold.

    Liquidity ratings from tastytrade are on a 0-5 scale:
    - 5: Extremely liquid (tight bid-ask, deep book)
    - 4: Very liquid
    - 3: Moderately liquid (typical minimum for calendar spreads)
    - 2: Low liquidity (wide spreads possible)
    - 1: Very low liquidity
    - 0: Illiquid (avoid trading)

    Args:
        symbol: Ticker symbol (e.g., 'SPY')
        metrics: Market metrics dict from fetch_market_metrics()
        min_rating: Minimum acceptable liquidity rating (0-5, default 3)

    Returns:
        Tuple of (passes_filter, reason_string):
        - (True, None): Meets threshold OR liquidity data unavailable
        - (False, reason): Below threshold with explanation

    Raises:
        None (gracefully handles missing/invalid data with warnings to stderr)

    Example:
        >>> check_liquidity('SPY', metrics, min_rating=3)
        (True, None)  # SPY has rating 5

        >>> check_liquidity('ILLIQUID', metrics, min_rating=3)
        (False, 'Liquidity rating 2 < 3')
    """
    if symbol not in metrics:
        print(f"[WARN] {symbol}: Market metrics unavailable, skipping liquidity check", file=sys.stderr)
        return (True, None)

    metric_info = metrics[symbol]

    # Check if liquidity_rating attribute exists
    liquidity_rating = getattr(metric_info, 'liquidity_rating', None)
    if liquidity_rating is None:
        print(f"[WARN] {symbol}: Liquidity rating unavailable, skipping liquidity check", file=sys.stderr)
        return (True, None)

    # Convert to int if needed
    try:
        rating = int(liquidity_rating)
    except (ValueError, TypeError):
        print(f"[WARN] {symbol}: Invalid liquidity rating format, skipping liquidity check", file=sys.stderr)
        return (True, None)

    if rating < min_rating:
        reason = f"Liquidity rating {rating} < {min_rating}"
        return (False, reason)

    return (True, None)

def extract_xearn_iv(
    metrics: Dict[str, any],
    symbol: str,
    expiration_date: date
) -> Optional[float]:
    """
    Try to extract X-earn IV (earnings-removed implied volatility) from Market Metrics API.

    Args:
        metrics: Market metrics dict from fetch_market_metrics()
        symbol: Ticker symbol (e.g., 'SPY')
        expiration_date: Option expiration date to match

    Returns:
        X-earn IV as decimal (e.g., 0.25 = 25%) or None if unavailable

    Note:
        Falls back to None if:
        - Symbol not in metrics
        - option_expiration_implied_volatilities field missing
        - Expiration date not found in the list
        - IV value is None or invalid
    """
    if symbol not in metrics:
        return None

    metric_info = metrics[symbol]

    # Try to get option_expiration_implied_volatilities field
    iv_list = getattr(metric_info, 'option_expiration_implied_volatilities', None)
    if iv_list is None or not isinstance(iv_list, list):
        return None

    # Search for matching expiration date
    for iv_entry in iv_list:
        # Expecting structure like: {'expiration_date': date(...), 'implied_volatility': 0.25}
        entry_date = getattr(iv_entry, 'expiration_date', None)
        if entry_date == expiration_date:
            iv_value = getattr(iv_entry, 'implied_volatility', None)
            if iv_value is not None:
                try:
                    return float(iv_value)
                except (ValueError, TypeError):
                    return None

    return None

# ---------- Main scan ----------

async def scan(session: Session, tickers: List[str], pairs: List[Tuple[int, int]],
               min_ff: float, dte_tolerance: int, timeout_s: float,
               skip_earnings: bool = True, min_liquidity_rating: int = 3,
               skip_liquidity_check: bool = False, show_earnings_conflicts: bool = False,
               use_xearn_iv: bool = True, force_greeks_iv: bool = False,
               show_all_scans: bool = False, structure: str = "both",
               delta_tolerance: float = 0.05) -> List[dict]:
    """
    Main scanner function: Find calendar spread opportunities with high forward factors.

    Scans symbols for calendar spread setups where front-month IV is elevated relative
    to forward IV. Supports both ATM call calendars and double calendars (±35Δ).

    Workflow:
    1. Fetch market metrics (earnings, liquidity, X-earn IV) for all symbols
    2. For each symbol:
       - Get spot price and option chain
       - Apply earnings and liquidity filters
       - Find expirations matching target DTEs
       - Fetch Greeks (IV, delta) for relevant strikes
       - Calculate forward IV and FF ratio
       - Output rows for structures meeting FF threshold

    Args:
        session: Active tastytrade session (must be authenticated)
        tickers: List of ticker symbols to scan (e.g., ['SPY', 'QQQ', 'AAPL'])
        pairs: List of (front_dte, back_dte) tuples (e.g., [(30, 60), (60, 90)])
        min_ff: Minimum FF ratio threshold (e.g., 0.20 or 0.23)
        dte_tolerance: Max deviation from target DTE in days (default 5)
        timeout_s: Greeks streaming timeout in seconds (default 3.0)
        skip_earnings: Filter out positions with earnings conflicts (default True)
        min_liquidity_rating: Minimum liquidity rating 0-5 (default 3)
        skip_liquidity_check: Disable liquidity filtering (default False)
        show_earnings_conflicts: Include filtered positions in output (default False)
        use_xearn_iv: Try X-earn IV before falling back to Greeks IV (default True)
        force_greeks_iv: Always use Greeks IV, skip X-earn IV (default False)
        show_all_scans: Show all results regardless of FF threshold (default False)
        structure: Calendar type: "atm-call", "double", or "both" (default "both")
        delta_tolerance: Max delta deviation for double calendars (default 0.05 = ±5Δ)

    Returns:
        List of dict rows with 25-column unified CSV schema:
        - timestamp, symbol, structure, spot_price
        - front_dte, back_dte, front_expiry, back_expiry
        - atm_strike, call_strike, put_strike, call_delta, put_delta
        - front_iv, back_iv, fwd_iv
        - ff, call_ff, put_ff, combined_ff
        - earnings_date, earnings_conflict
        - liquidity_rating, liquidity_value
        - iv_source_front, iv_source_back

        Sorted by combined_ff descending, then symbol ascending.

    Raises:
        None (logs warnings for failures, continues processing remaining symbols)

    Example:
        >>> rows = await scan(
        ...     session, ['SPY', 'QQQ'], [(30, 60)],
        ...     min_ff=0.23, dte_tolerance=5, timeout_s=3.0
        ... )
        >>> rows[0]['symbol']
        'SPY'
        >>> rows[0]['combined_ff']
        0.285  # 28.5% FF ratio
    """
    rows: List[dict] = []
    filtered_rows: List[dict] = []  # For --show-earnings-conflicts
    today = ny_today()
    timestamp = datetime.utcnow().isoformat() + 'Z'  # ISO 8601 UTC timestamp

    # Fetch market metrics for all symbols upfront (batched)
    market_metrics = fetch_market_metrics(session, tickers)

    for idx, sym in enumerate(tickers):
        # Add small delay between symbols to avoid rate limiting (except for first symbol)
        if idx > 0:
            await asyncio.sleep(0.5)  # 500ms delay between symbols

        # 1) Underlying spot - handle futures vs equity
        if is_futures_symbol(sym):
            # For futures, get spot from active contract
            spot = get_futures_spot_price(session, sym)
            if spot is None:
                # Futures spot price not critical - we can infer from option strikes
                # Use a default that will be overridden by ATM strike selection
                print(f"[INFO] Using option chain for {sym} (futures spot not available)", file=sys.stderr)
                spot = 0.0  # Will be inferred from option chain
        else:
            # For equity, use standard equity market data
            md = get_market_data(session, sym, InstrumentType.EQUITY)
            if md is None or md.last is None:
                print(f"[WARN] No quote for {sym}, skipping.", file=sys.stderr)
                continue
            spot = float(md.last) if md.last is not None else float(md.mark)

        # 2) Extract earnings and liquidity data for this symbol
        earnings_date = None
        liquidity_rating = None
        if sym in market_metrics:
            metric_info = market_metrics[sym]
            earnings = getattr(metric_info, 'earnings', None)
            if earnings:
                earnings_date = getattr(earnings, 'expected_report_date', None)
            liquidity_rating = getattr(metric_info, 'liquidity_rating', None)

        # 3) Chain (nested)
        chain_list = NestedOptionChain.get(session, sym)
        if not chain_list:
            print(f"[WARN] No option chain for {sym}, skipping.", file=sys.stderr)
            continue
        chain = chain_list[0]  # API returns a list; take first element

        # For futures, infer spot from option chain if not available
        if is_futures_symbol(sym) and spot == 0.0:
            if chain.expirations and chain.expirations[0].strikes:
                # Use middle strike as proxy for spot price
                strikes = [s.strike_price for s in chain.expirations[0].strikes]
                spot = float(sorted(strikes)[len(strikes) // 2])
                print(f"[INFO] Inferred {sym} spot from option chain: {spot:.2f}", file=sys.stderr)

        # Pre-index expirations by date for fast lookup
        exp_by_date = {exp.expiration_date: exp for exp in chain.expirations}

        # 2.5) Pre-filtering: Check earnings conflicts and liquidity
        # Find the maximum back expiry date we'll need for this symbol
        max_back_dte = max([back for _, back in pairs])
        max_back_exp = nearest_expiration(chain, max_back_dte, dte_tolerance)

        # Skip earnings check for futures (they don't have earnings)
        if max_back_exp and skip_earnings and not is_futures_symbol(sym):
            passes, reason = check_earnings_conflict(sym, market_metrics, max_back_exp, today)
            if not passes:
                print(f"[FILTERED] {sym}: {reason}", file=sys.stderr)
                if show_earnings_conflicts:
                    # Note: We'd compute FF here if we had the data, but skipping for simplicity
                    filtered_rows.append({"symbol": sym, "reason": reason})
                continue

        if not skip_liquidity_check:
            passes, reason = check_liquidity(sym, market_metrics, min_liquidity_rating)
            if not passes:
                print(f"[INFO] {sym}: {reason}, skipping", file=sys.stderr)
                continue

        # 4) Branch based on calendar structure mode
        required_targets = sorted(set([t for pair in pairs for t in pair]))

        # Determine which structures to scan
        scan_double = structure in ("double", "both")
        scan_atm = structure in ("atm-call", "both")

        if scan_double:
            # ========== DOUBLE CALENDAR MODE ==========
            # Get ±35Δ strikes for each target DTE
            delta_choices: Dict[int, Dict] = {}

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

            # Build rows for double calendar pairs
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
                        if ff_call >= min_ff or show_all_scans:
                            rows.append({
                                "timestamp": timestamp,
                                "symbol": sym,
                                "structure": "double-call",
                                "spot_price": f"{spot:.2f}",
                                "front_dte": front_choice["dte"],
                                "back_dte": back_choice["dte"],
                                "front_expiry": front_choice["expiration"].isoformat(),
                                "back_expiry": back_choice["expiration"].isoformat(),
                                "atm_strike": "",
                                "call_strike": f"{front_call.strike:.2f}",
                                "put_strike": "",
                                "call_delta": round(front_call.actual_delta, 4),
                                "put_delta": "",
                                "front_iv": round(front_call.iv, 6),
                                "back_iv": round(back_call.iv, 6),
                                "fwd_iv": round(fwd_call, 6),
                                "ff": "",
                                "call_ff": round(ff_call, 6),
                                "put_ff": "",
                                "combined_ff": round(ff_call, 6),
                                "earnings_date": earnings_date.isoformat() if earnings_date else "",
                                "earnings_conflict": "no" if not earnings_date else "",
                                "liquidity_rating": liquidity_rating if liquidity_rating is not None else "",
                                "liquidity_value": "",
                                "iv_source_front": "greeks",
                                "iv_source_back": "greeks"
                            })

                # Process put calendar
                if has_put_calendar:
                    fwd_put = forward_iv(front_put.iv, back_put.iv, front_choice["dte"], back_choice["dte"])
                    if fwd_put and fwd_put > 0:
                        ff_put = (front_put.iv - fwd_put) / fwd_put
                        if ff_put >= min_ff or show_all_scans:
                            rows.append({
                                "timestamp": timestamp,
                                "symbol": sym,
                                "structure": "double-put",
                                "spot_price": f"{spot:.2f}",
                                "front_dte": front_choice["dte"],
                                "back_dte": back_choice["dte"],
                                "front_expiry": front_choice["expiration"].isoformat(),
                                "back_expiry": back_choice["expiration"].isoformat(),
                                "atm_strike": "",
                                "call_strike": "",
                                "put_strike": f"{front_put.strike:.2f}",
                                "call_delta": "",
                                "put_delta": round(front_put.actual_delta, 4),
                                "front_iv": round(front_put.iv, 6),
                                "back_iv": round(back_put.iv, 6),
                                "fwd_iv": round(fwd_put, 6),
                                "ff": "",
                                "call_ff": "",
                                "put_ff": round(ff_put, 6),
                                "combined_ff": round(ff_put, 6),
                                "earnings_date": earnings_date.isoformat() if earnings_date else "",
                                "earnings_conflict": "no" if not earnings_date else "",
                                "liquidity_rating": liquidity_rating if liquidity_rating is not None else "",
                                "liquidity_value": "",
                                "iv_source_front": "greeks",
                                "iv_source_back": "greeks"
                            })

        if scan_atm:
            # ========== ATM CALENDAR MODE (existing logic) ==========
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

            # 4) Try X-earn IV first (if enabled), then fall back to Greeks IV
            atm_iv_by_target: Dict[int, float] = {}
            iv_source_by_target: Dict[int, str] = {}

                # Try X-earn IV for each target DTE
            if use_xearn_iv and not force_greeks_iv:
                for target, ch in choices.items():
                    xearn_iv = extract_xearn_iv(market_metrics, sym, ch.expiration)
                    if xearn_iv is not None and xearn_iv > 0:
                        atm_iv_by_target[target] = xearn_iv
                        iv_source_by_target[target] = "xearn"

            # For targets without X-earn IV, fall back to Greeks IV
            targets_needing_greeks = [t for t in choices.keys() if t not in atm_iv_by_target]

            if targets_needing_greeks or force_greeks_iv:
                # Snapshot Greeks (to get IV and delta) for all needed ATM contracts
                greek_map = await snapshot_greeks(session, streamer_syms, timeout_s=timeout_s)

                for target, ch in choices.items():
                    # Skip if X-earn IV already available (unless force_greeks_iv)
                    if target in atm_iv_by_target and not force_greeks_iv:
                        continue

                    call_iv = None
                    put_iv = None
                    # Unpack (iv, delta) tuples from greek_map
                    if ch.call_streamer_symbol in greek_map:
                        iv, delta = greek_map[ch.call_streamer_symbol]
                        call_iv = iv if iv is not None and iv > 0 else None
                    if ch.put_streamer_symbol in greek_map:
                        iv, delta = greek_map[ch.put_streamer_symbol]
                        put_iv = iv if iv is not None and iv > 0 else None

                    # If both present, average; if one present, use it.
                    ivs = [v for v in [call_iv, put_iv] if v and v > 0]
                    if ivs:
                        atm_iv_by_target[target] = sum(ivs) / len(ivs)
                        iv_source_by_target[target] = "greeks"

            # Log X-earn IV fallback warnings
            if use_xearn_iv and not force_greeks_iv:
                for target in choices.keys():
                    if target not in iv_source_by_target or iv_source_by_target[target] == "greeks":
                        print(f"[INFO] {sym} {target}DTE: X-earn IV unavailable, using Greeks IV", file=sys.stderr)

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

                # Determine IV source for this pair (prefer front, fall back to back)
                iv_src = iv_source_by_target.get(front, iv_source_by_target.get(back, "greeks"))

                # Include result if: (1) meets FF threshold, OR (2) show_all_scans is enabled
                if ff >= min_ff or show_all_scans:
                    rows.append({
                        "timestamp": timestamp,
                        "symbol": sym,
                        "structure": "atm-call",
                        "spot_price": f"{spot:.2f}",
                        "front_dte": front_choice.dte,
                        "back_dte": back_choice.dte,
                        "front_expiry": front_choice.expiration.isoformat(),
                        "back_expiry": back_choice.expiration.isoformat(),
                        "atm_strike": f"{front_choice.strike:.2f}",
                        "call_strike": "",
                        "put_strike": "",
                        "call_delta": "",
                        "put_delta": "",
                        "front_iv": round(iv_f, 6),
                        "back_iv": round(iv_b, 6),
                        "fwd_iv": round(fwd, 6),
                        "ff": round(ff, 6),
                        "call_ff": "",
                        "put_ff": "",
                        "combined_ff": round(ff, 6),
                        "earnings_date": earnings_date.isoformat() if earnings_date else "",
                        "earnings_conflict": "no" if not earnings_date else "",
                        "liquidity_rating": liquidity_rating if liquidity_rating is not None else "",
                        "liquidity_value": "",
                        "iv_source_front": iv_src,
                        "iv_source_back": iv_src
                    })

    # Sort by combined_ff descending (highest FF first), then by symbol ascending
    rows.sort(key=lambda r: (-r["combined_ff"], r["symbol"]))
    return rows

def read_list_arg(values: List[str]) -> List[str]:
    """
    Parse command-line list arguments supporting both space and comma separation.

    Handles argparse nargs="+" arguments that can be provided as:
    - Space-separated: --tickers SPY QQQ AAPL
    - Comma-separated: --tickers SPY,QQQ,AAPL
    - Mixed: --tickers SPY,QQQ AAPL

    Args:
        values: List of strings from argparse (e.g., ['SPY,QQQ', 'AAPL'])

    Returns:
        List of uppercase, stripped strings (e.g., ['SPY', 'QQQ', 'AAPL'])

    Example:
        >>> read_list_arg(['SPY,QQQ', 'AAPL'])
        ['SPY', 'QQQ', 'AAPL']
        >>> read_list_arg(['spy', 'qqq'])
        ['SPY', 'QQQ']
    """
    out: List[str] = []
    for v in values:
        out.extend([x for x in v.split(",") if x])
    return [x.strip().upper() for x in out if x.strip()]

def main():
    ap = argparse.ArgumentParser(
        description="Forward-IV (FF) calendar spread scanner using tastytrade API + dxFeed Greeks.",
        epilog="""
Examples:
  # Daily pre-market scan with quality filtering
  python ff_tastytrade_scanner.py --tickers SPY QQQ AAPL --pairs 30-60 --min-ff 0.23 --csv-out scan.csv

  # Scan for double calendars only
  python ff_tastytrade_scanner.py --tickers SPY QQQ --pairs 60-90 --structure double --min-ff 0.20

  # Scan both ATM and double calendars
  python ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --structure both

  # Allow trading through earnings (disable earnings filter)
  python ff_tastytrade_scanner.py --tickers AAPL --pairs 30-90 --allow-earnings

  # Force use of Greeks IV instead of X-earn IV
  python ff_tastytrade_scanner.py --tickers QQQ --pairs 60-90 --force-greeks-iv
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Core scanner parameters
    ap.add_argument("--tickers", nargs="+", required=True,
                    help="List of underlyings (space or comma-separated). Example: SPY QQQ AAPL")
    ap.add_argument("--pairs", nargs="+", required=True,
                    help="DTE pairs (front-back). Example: 30-60 30-90 60-90")
    ap.add_argument("--min-ff", type=float, default=0.20,
                    help="Minimum FF ratio threshold (default: 0.20). Use 0.23 for ~20 trades/month.")
    ap.add_argument("--dte-tolerance", type=int, default=5,
                    help="Max deviation from target DTE in days (default: 5).")
    ap.add_argument("--timeout", type=float, default=3.0,
                    help="Greeks streaming timeout in seconds (default: 3.0).")

    # Output options
    ap.add_argument("--json-out", type=str, default="",
                    help="Write results to JSON file.")
    ap.add_argument("--csv-out", type=str, default="",
                    help="Write results to CSV file (recommended).")
    ap.add_argument("--sandbox", action="store_true",
                    help="Use sandbox environment (limited market data).")

    # Earnings filtering flags (mutually exclusive group)
    earnings_group = ap.add_mutually_exclusive_group()
    earnings_group.add_argument("--skip-earnings", dest="skip_earnings", action="store_true",
                                help="Skip positions with earnings conflicts (default).")
    earnings_group.add_argument("--allow-earnings", dest="skip_earnings", action="store_false",
                                help="Allow trading through earnings (disable earnings filtering).")
    ap.set_defaults(skip_earnings=True)  # Set default: skip earnings by default
    ap.add_argument("--show-earnings-conflicts", action="store_true",
                    help="Show filtered positions due to earnings.")

    # Liquidity filtering flags
    ap.add_argument("--min-liquidity-rating", type=int, default=3,
                    help="Minimum liquidity rating 0-5 (default: 3).")
    ap.add_argument("--skip-liquidity-check", action="store_true",
                    help="Disable liquidity filtering.")

    # X-earn IV flags
    ap.add_argument("--use-xearn-iv", dest="use_xearn_iv", action="store_true", default=True,
                    help="Try to use X-earn IV from market metrics (default: True).")
    ap.add_argument("--force-greeks-iv", action="store_true",
                    help="Force use of Greeks IV instead of X-earn IV.")

    # Debug/analysis flags
    ap.add_argument("--show-all-scans", action="store_true",
                    help="Show all scan results regardless of FF threshold (for data pipeline testing).")

    # Structure selection
    ap.add_argument("--structure", type=str, default="both", choices=["atm-call", "double", "both"],
                    help="Calendar structure: atm-call (ATM only), double (±35Δ only), or both (default: both).")
    ap.add_argument("--delta-tolerance", type=float, default=0.05,
                    help="Max delta deviation for double calendars (default: 0.05 = ±5Δ). Range: 0.01-0.10.")

    args = ap.parse_args()
    tickers = read_list_arg(args.tickers)
    pairs = parse_pairs(read_list_arg(args.pairs))

    # Validate flag values
    if args.min_liquidity_rating < 0 or args.min_liquidity_rating > 5:
        print("ERROR: --min-liquidity-rating must be between 0 and 5", file=sys.stderr)
        sys.exit(1)

    if args.delta_tolerance < 0.01 or args.delta_tolerance > 0.10:
        print("ERROR: --delta-tolerance must be between 0.01 and 0.10", file=sys.stderr)
        sys.exit(1)

    # Check for conflicting flags
    # Note: --skip-earnings and --allow-earnings are mutually exclusive via argparse group

    if args.use_xearn_iv and args.force_greeks_iv:
        print("ERROR: --use-xearn-iv and --force-greeks-iv are mutually exclusive", file=sys.stderr)
        sys.exit(1)

    username = os.environ.get("TT_USERNAME", "").strip()
    password = os.environ.get("TT_PASSWORD", "").strip()
    if not username or not password:
        print("ERROR: Set TT_USERNAME and TT_PASSWORD env vars.", file=sys.stderr)
        sys.exit(2)

    # Create session
    session = Session(username, password=password, is_test=bool(args.sandbox))

    # Run scan
    # Both --skip-earnings and --allow-earnings set skip_earnings via mutually exclusive group
    skip_earnings_flag = args.skip_earnings

    rows = asyncio.run(scan(
        session, tickers, pairs, args.min_ff, args.dte_tolerance, args.timeout,
        skip_earnings=skip_earnings_flag,
        min_liquidity_rating=args.min_liquidity_rating,
        skip_liquidity_check=args.skip_liquidity_check,
        show_earnings_conflicts=args.show_earnings_conflicts,
        use_xearn_iv=args.use_xearn_iv,
        force_greeks_iv=args.force_greeks_iv,
        show_all_scans=args.show_all_scans,
        structure=args.structure,
        delta_tolerance=args.delta_tolerance
    ))

    # Unified 25-column CSV schema
    cols = [
        "timestamp", "symbol", "structure", "spot_price",
        "front_dte", "back_dte", "front_expiry", "back_expiry",
        "atm_strike", "call_strike", "put_strike", "call_delta", "put_delta",
        "front_iv", "back_iv", "fwd_iv",
        "ff", "call_ff", "put_ff", "combined_ff",
        "earnings_date", "earnings_conflict",
        "liquidity_rating", "liquidity_value",
        "iv_source_front", "iv_source_back"
    ]

    if not rows:
        print("No results passing filters.")
    else:
        print(",".join(cols))
        for r in rows:
            print(",".join(str(r.get(c, "")) for c in cols))

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
