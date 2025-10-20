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
#   python ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --min-ff 0.20 --debug  # Enable debug logging
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
import logging
import time
from dataclasses import dataclass
from datetime import date, datetime, timedelta, UTC
from typing import Dict, List, Tuple, Optional

from tastytrade import Session, DXLinkStreamer
from tastytrade.market_data import get_market_data
from tastytrade.metrics import get_market_metrics
from tastytrade.order import InstrumentType
from tastytrade.instruments import NestedOptionChain, NestedFutureOptionChain
from tastytrade.dxfeed import Greeks, Quote
from tastytrade.utils import today_in_new_york

import yfinance as yf

from earnings_cache import EarningsCache

# ---------- Skip Reason Constants ----------
# Used to track why symbols are skipped during scans
SKIP_NONPOSITIVE_FWD_VAR = "nonpositive_fwd_var"
SKIP_MISSING_IV = "missing_iv"
SKIP_EXPIRY_MISMATCH = "expiry_mismatch"
SKIP_DELTA_NOT_FOUND = "delta_not_found"
SKIP_EARNINGS_CONFLICT = "earnings_conflict"
SKIP_VOLUME_TOO_LOW = "volume_too_low"
SKIP_NO_QUOTE = "no_quote"
SKIP_NO_CHAIN = "no_chain"
SKIP_BOTH_LEGS_REQUIRED = "both_legs_required"
SKIP_BELOW_FF_THRESHOLD = "below_ff_threshold"

# ---------- ATM Strike Selection Constants ----------
# Target delta for ATM strike selection (50Δ = at-the-money)
ATM_DELTA_TARGET = 0.50

# Maximum delta deviation from target when selecting ATM strikes
# If no strikes within ±0.10Δ of target, fallback to nearest-spot logic
ATM_DELTA_TOLERANCE = 0.10

# ---------- Logger ----------
logger = logging.getLogger(__name__)

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

def tastytrade_to_yahoo_futures(symbol: str) -> Optional[str]:
    """
    Map tastytrade futures symbols to Yahoo Finance futures tickers.

    Args:
        symbol: Tastytrade futures symbol (e.g., '/ES', '/GC', '/NQ')

    Returns:
        Yahoo Finance futures ticker (e.g., 'ES=F', 'GC=F', 'NQ=F'), or None if unknown

    Example:
        >>> tastytrade_to_yahoo_futures('/ES')
        'ES=F'
    """
    # Common futures symbols mapping
    mapping = {
        # Equity Index Futures
        '/ES': 'ES=F',      # E-mini S&P 500
        '/MES': 'MES=F',    # Micro E-mini S&P 500
        '/NQ': 'NQ=F',      # E-mini Nasdaq-100
        '/MNQ': 'MNQ=F',    # Micro E-mini Nasdaq-100
        '/YM': 'YM=F',      # E-mini Dow
        '/RTY': 'RTY=F',    # E-mini Russell 2000
        '/SR3': 'RTY=F',    # Mini Russell 1000 (use RTY as proxy)

        # Metals
        '/GC': 'GC=F',      # Gold
        '/SI': 'SI=F',      # Silver
        '/HG': 'HG=F',      # Copper

        # Energy
        '/CL': 'CL=F',      # Crude Oil
        '/MCL': 'MCL=F',    # Micro Crude Oil
        '/NG': 'NG=F',      # Natural Gas

        # Treasuries
        '/ZB': 'ZB=F',      # 30-Year T-Bond
        '/ZN': 'ZN=F',      # 10-Year T-Note
        '/ZF': 'ZF=F',      # 5-Year T-Note
        '/ZT': 'ZT=F',      # 2-Year T-Note

        # Agriculture
        '/ZC': 'ZC=F',      # Corn
        '/ZS': 'ZS=F',      # Soybeans
        '/ZW': 'ZW=F',      # Wheat
        '/HE': 'HE=F',      # Lean Hogs
        '/LE': 'LE=F',      # Live Cattle

        # Currencies
        '/6E': '6E=F',      # Euro FX
        '/6J': '6J=F',      # Japanese Yen
        '/6B': '6B=F',      # British Pound
        '/6A': '6A=F',      # Australian Dollar
        '/6C': '6C=F',      # Canadian Dollar

        # Crypto (may not have =F format on Yahoo)
        '/BTC': 'BTC-USD',  # Bitcoin (use spot, not futures)
        '/ETH': 'ETH-USD',  # Ethereum (use spot, not futures)
    }
    return mapping.get(symbol)


def get_futures_spot_price(symbol: str) -> Optional[float]:
    """
    Get spot price for a futures symbol from Yahoo Finance.

    Uses yfinance to fetch the current price since tastytrade API doesn't
    provide futures spot prices reliably.

    Args:
        symbol: Futures root symbol (e.g., '/ES', '/GC', '/NQ')

    Returns:
        The last traded price of the futures contract, or None if unavailable

    Raises:
        None - returns None on any error

    Example:
        >>> price = get_futures_spot_price('/ES')
        >>> print(f'/ES spot: {price}')
        /ES spot: 5921.50
    """
    try:
        yahoo_symbol = tastytrade_to_yahoo_futures(symbol)
        if not yahoo_symbol:
            print(f"[WARN] Unknown futures symbol {symbol}, no Yahoo Finance mapping", file=sys.stderr)
            return None

        # Fetch current price from Yahoo Finance
        ticker = yf.Ticker(yahoo_symbol)
        info = ticker.fast_info

        # Try to get last price
        if hasattr(info, 'last_price') and info.last_price:
            return float(info.last_price)

        # Fallback to regular price
        hist = ticker.history(period='1d', interval='1m')
        if not hist.empty:
            return float(hist['Close'].iloc[-1])

        print(f"[WARN] No price data available for {yahoo_symbol}", file=sys.stderr)
        return None

    except Exception as e:
        print(f"[WARN] Could not get futures spot price for {symbol}: {e}", file=sys.stderr)
        return None

@dataclass(frozen=True)
class ATMChoice:
    expiration: date
    strike: float
    call_streamer_symbol: str
    put_streamer_symbol: str
    dte: int
    actual_delta: Optional[float] = None  # Call delta at selected strike (None if fallback used)

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

def pick_atm_strike(expiration_obj, spot: float, greeks_map: Optional[Dict[str, Tuple[float, float]]] = None) -> Tuple[float, Optional[float], str, str]:
    """
    From a NestedOptionChain expiration, choose the strike with call delta closest to 50Δ.
    If greeks_map unavailable or no strikes within ±10Δ tolerance, fall back to nearest-spot.

    Args:
        expiration_obj: NestedOptionChain expiration object
        spot: Current underlying spot price
        greeks_map: Optional dict mapping streamer_symbol -> (iv, delta) tuple

    Returns:
        (strike, actual_delta, call_streamer_symbol, put_streamer_symbol)
        - actual_delta is None if fallback to nearest-spot was used
    """
    # Primary: Delta-based selection (50Δ target)
    if greeks_map:
        best_strike = None
        best_delta = None
        best_call_sym = None
        best_put_sym = None
        min_delta_distance = float('inf')

        for s in expiration_obj.strikes:
            call_sym = s.call_streamer_symbol
            if call_sym in greeks_map:
                _, call_delta = greeks_map[call_sym]
                if call_delta is not None:
                    delta_distance = abs(call_delta - ATM_DELTA_TARGET)
                    if delta_distance < min_delta_distance:
                        min_delta_distance = delta_distance
                        best_strike = float(s.strike_price)
                        best_delta = call_delta
                        best_call_sym = call_sym
                        best_put_sym = s.put_streamer_symbol

        # If we found a strike within tolerance, use it
        if best_strike is not None and min_delta_distance <= ATM_DELTA_TOLERANCE:
            logger.debug(f"ATM strike selected by delta: {best_strike} (delta={best_delta:.3f})")
            return (best_strike, best_delta, best_call_sym, best_put_sym)

        # Log fallback
        if best_strike is not None:
            logger.debug(f"No 50Δ strike within ±{ATM_DELTA_TOLERANCE} tolerance (best: {min_delta_distance:.3f}), using nearest-spot fallback")

    # Fallback: Nearest-to-spot (original logic)
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

    strike, call_sym, put_sym = best
    return (strike, None, call_sym, put_sym)  # actual_delta = None for fallback

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

async def snapshot_underlying(session: Session, symbol: str, timeout_s: float = 3.0):
    """
    Fetch Underlying event from dxFeed for today's option chain volume.

    Args:
        session: Active tastytrade session
        symbol: Ticker symbol (e.g., 'SPY', 'MSFT')
        timeout_s: Timeout in seconds for snapshot collection

    Returns:
        Underlying event object with option_volume field, or None on timeout/error
        - option_volume: Today's total option chain volume (all strikes/expirations/types)

    Note:
        option_volume represents today's aggregate volume across the entire option chain
        (all strikes, all expirations, calls + puts). This is the correct metric for
        volume-based liquidity filtering.
    """
    from tastytrade.dxfeed import Underlying

    async with DXLinkStreamer(session) as streamer:
        await streamer.subscribe(Underlying, [symbol])

        try:
            async with asyncio.timeout(timeout_s):
                async for event in streamer.listen(Underlying):
                    if event.eventSymbol == symbol:
                        return event
        except asyncio.TimeoutError:
            logger.warning(f"{symbol}: Timeout fetching Underlying event")
            return None

    return None

def validate_ff_inputs(iv_front: float, iv_back: float, dte_front: int, dte_back: int) -> Optional[str]:
    """
    Validate inputs for forward volatility calculation.

    Checks for non-positive forward variance which would make FF calculation invalid.
    This catches edge cases where IV_back^2 * T2 <= IV_front^2 * T1, which produces
    negative or zero variance under the square root.

    Args:
        iv_front: Front expiration IV (decimal, e.g., 0.25 for 25%)
        iv_back: Back expiration IV (decimal, e.g., 0.25 for 25%)
        dte_front: Days to front expiration
        dte_back: Days to back expiration

    Returns:
        None if inputs are valid
        str: skip_reason if inputs are invalid

    Formula check: IV_back^2 * T2 must be > IV_front^2 * T1
    where T1 = dte_front/365, T2 = dte_back/365

    Edge cases handled:
        - Invalid IVs: negative, zero, NaN, infinity
        - Invalid DTEs: zero, negative, or front >= back
        - Non-positive forward variance: IV_back^2 * T2 <= IV_front^2 * T1

    Example:
        >>> validate_ff_inputs(0.30, 0.25, 30, 60)
        None  # Valid inputs
        >>> validate_ff_inputs(0.50, 0.25, 30, 60)
        'Non-positive forward variance: IV_back^2 * T2 <= IV_front^2 * T1'
    """
    # Check for invalid IVs
    if not (math.isfinite(iv_front) and math.isfinite(iv_back)):
        return "Invalid IV: NaN or infinity detected"

    if iv_front <= 0:
        return "Invalid IV_front: must be positive"

    if iv_back <= 0:
        return "Invalid IV_back: must be positive"

    # Check for invalid DTEs
    if dte_front <= 0:
        return "Invalid DTE_front: must be positive"

    if dte_back <= 0:
        return "Invalid DTE_back: must be positive"

    if dte_back <= dte_front:
        return "Invalid DTEs: back DTE must be > front DTE"

    # Check for non-positive forward variance
    # Forward variance = (IV_back^2 * T2 - IV_front^2 * T1) / (T2 - T1)
    # For this to be positive, numerator must be positive:
    # IV_back^2 * T2 > IV_front^2 * T1
    T1 = dte_front / 365.0
    T2 = dte_back / 365.0

    variance_numerator = (iv_back ** 2) * T2 - (iv_front ** 2) * T1

    if variance_numerator <= 0:
        return "Non-positive forward variance: IV_back^2 * T2 <= IV_front^2 * T1"

    return None  # All checks passed


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
    Batch fetch earnings dates and X-earn IV data for all symbols.

    Calls tastytrade's get_market_metrics() API to retrieve:
    - Earnings dates (earnings.expected_report_date)
    - X-earn IV by expiration (option_expiration_implied_volatilities)

    Note: Volume filtering now uses dxFeed Underlying.optionVolume instead of liquidity_value

    Args:
        session: Active tastytrade session (must be authenticated)
        symbols: List of ticker symbols (e.g., ['SPY', 'QQQ', 'AAPL'])

    Returns:
        Dict mapping symbol → MarketMetricInfo object
        Returns empty dict {} on API failure (never crashes)

    Raises:
        None (logs error to stderr and returns empty dict on failure)

    Note:
        - Volume filtering now uses dxFeed Underlying.optionVolume (fetched separately)
        - Field may be None for futures or illiquid symbols
        - Futures symbols are allowed through if volume field is missing

    Example:
        >>> metrics = fetch_market_metrics(session, ['SPY', 'QQQ'])
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

def check_liquidity_rating(
    symbol: str,
    metrics: Dict[str, any],
    min_rating: int = 3
) -> Tuple[bool, Optional[str]]:
    """
    Check if symbol's liquidity rating meets minimum threshold.

    Uses liquidity_rating (0-5 scale) from Market Metrics API.
    Rating 3 ≈ ~10k contracts/day average option volume.

    Args:
        symbol: Ticker symbol (e.g., 'SPY')
        metrics: Market metrics dict from fetch_market_metrics()
        min_rating: Minimum acceptable liquidity rating (default: 3)

    Returns:
        Tuple of (passes_filter, reason_string):
        - (True, None): Meets threshold OR rating unavailable OR futures symbol
        - (False, reason): Below threshold with explanation

    Note:
        - Available 24/7 (not streaming API)
        - Futures symbols without rating are allowed through
        - Missing rating generates warning but allows through

    Example:
        >>> check_liquidity_rating('SPY', metrics, min_rating=3)
        (True, None)  # SPY has rating 5

        >>> check_liquidity_rating('ILLIQUID', metrics, min_rating=3)
        (False, 'Liquidity rating 2 < 3')
    """
    if symbol not in metrics:
        print(f"[WARN] {symbol}: Market metrics unavailable, skipping liquidity check", file=sys.stderr)
        return (True, None)

    metric_info = metrics[symbol]

    # Check if liquidity_rating exists
    rating = getattr(metric_info, 'liquidity_rating', None)

    # Handle futures symbols - allow through if rating field is missing
    if is_futures_symbol(symbol) and rating is None:
        logger.debug(f"{symbol}: Futures symbol, liquidity check skipped (field missing)")
        return (True, None)

    if rating is None:
        print(f"[WARN] {symbol}: Liquidity rating unavailable, skipping liquidity check", file=sys.stderr)
        return (True, None)

    # Convert to int if needed
    try:
        rating_int = int(rating)
    except (ValueError, TypeError):
        print(f"[WARN] {symbol}: Invalid liquidity rating format, skipping liquidity check", file=sys.stderr)
        return (True, None)

    if rating_int < min_rating:
        reason = f"Liquidity rating {rating_int} < {min_rating}"
        return (False, reason)

    return (True, None)

def check_option_volume(
    symbol: str,
    option_volume: Optional[int],
    min_volume: float
) -> Tuple[bool, Optional[str]]:
    """
    Check if symbol's option volume meets minimum threshold.

    Uses option_volume from dxFeed Underlying event (today's total chain volume).
    Requires market hours (9:30 AM - 4:00 PM ET) for dxFeed streaming API.

    Args:
        symbol: Ticker symbol (e.g., 'SPY')
        option_volume: Today's option chain volume from dxFeed Underlying event
        min_volume: Minimum acceptable volume (default: 10000 contracts)

    Returns:
        Tuple of (passes_filter, reason_string):
        - (True, None): Meets threshold OR volume unavailable
        - (False, reason): Below threshold with explanation

    Note:
        - Only available during market hours (streaming API limitation)
        - Missing volume data generates warning but allows through
        - Futures symbols may not have option volume data

    Example:
        >>> check_option_volume('SPY', 150000, min_volume=10000)
        (True, None)  # SPY has volume 150k

        >>> check_option_volume('ILLIQUID', 5000, min_volume=10000)
        (False, 'Option volume 5000 < 10000')
    """
    # Handle missing volume data gracefully
    if option_volume is None:
        print(f"[WARN] {symbol}: Option volume unavailable (may need market hours), skipping volume check", file=sys.stderr)
        return (True, None)

    # Handle futures symbols - allow through if volume is 0 or missing
    if is_futures_symbol(symbol) and option_volume == 0:
        logger.debug(f"{symbol}: Futures symbol with zero volume, check skipped")
        return (True, None)

    if option_volume < min_volume:
        reason = f"Option volume {option_volume} < {min_volume}"
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
               skip_earnings: bool = True, options_volume_threshold: Optional[float] = None,
               skip_liquidity_check: bool = False, show_earnings_conflicts: bool = False,
               show_all_scans: bool = False, structure: str = "both",
               delta_tolerance: float = 0.05, earnings_data: Optional[Dict[str, dict]] = None) -> Tuple[List[dict], Dict[str, int], int, int]:
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
        options_volume_threshold: If set, use dxFeed option volume filtering (requires market hours).
                                 If None (default), use liquidity_rating >= 3 (24/7 available).
        skip_liquidity_check: Disable all volume/liquidity filtering (default False)
        show_earnings_conflicts: Include filtered positions in output (default False)
        show_all_scans: Show all results regardless of FF threshold (default False)
        structure: Calendar type: "atm-call", "double", or "both" (default "both")
        delta_tolerance: Max delta deviation for double calendars (default 0.05 = ±5Δ)
        earnings_data: Optional earnings data dict from EarningsCache (default None)

    Returns:
        Tuple of (rows, skip_stats, scanned, passed):
        - rows: List of dict rows with 40-column unified CSV schema:
          - timestamp, symbol, structure
          - call_ff, put_ff, combined_ff, min_ff (FF metrics)
          - spot_price, front_dte, back_dte, front_expiry, back_expiry
          - atm_strike (ATM calendars only), call_strike, put_strike, call_delta, put_delta
          - call_front_iv, call_back_iv, call_fwd_iv (call leg IVs)
          - put_front_iv, put_back_iv, put_fwd_iv (put leg IVs)
          - earnings_conflict, earnings_date
          - option_volume_today (today's total option chain volume from dxFeed Underlying)
          - liq_rating (liquidity rating 0-5 from Market Metrics)
          - iv_source_call_front, iv_source_call_back (call leg IV sources: "xearn" or "greeks")
          - iv_source_put_front, iv_source_put_back (put leg IV sources)
          - earnings_source (data source: "cache", "yahoo", "tastytrade", "none", or "skipped")
          - skip_reason (empty string if not skipped)
          For ATM calendars: call and put IVs are from same strike (may differ slightly)
          For double calendars: call and put IVs are from different strikes (+35Δ vs -35Δ)
          Sorting: Double calendars by min_ff descending (primary), combined_ff (secondary)
                   ATM calendars by combined_ff descending
          Filtering: Double calendars use min_ff >= threshold (both wings must pass)
                    ATM calendars use combined_ff >= threshold
        - skip_stats: Dict[str, int] mapping skip reasons to counts
        - scanned: int total symbols scanned
        - passed: int opportunities that met FF threshold

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
    timestamp = datetime.now(UTC).isoformat()  # ISO 8601 UTC timestamp

    # Skip statistics tracking
    skip_stats = {
        SKIP_NONPOSITIVE_FWD_VAR: 0,
        SKIP_MISSING_IV: 0,
        SKIP_EXPIRY_MISMATCH: 0,
        SKIP_DELTA_NOT_FOUND: 0,
        SKIP_EARNINGS_CONFLICT: 0,
        SKIP_VOLUME_TOO_LOW: 0,
        SKIP_NO_QUOTE: 0,
        SKIP_NO_CHAIN: 0,
        SKIP_BOTH_LEGS_REQUIRED: 0,
        SKIP_BELOW_FF_THRESHOLD: 0,
    }
    scanned = 0
    passed = 0

    # Fetch market metrics for all symbols upfront (batched)
    market_metrics = fetch_market_metrics(session, tickers)

    for idx, sym in enumerate(tickers):
        scanned += 1
        # Add small delay between symbols to avoid rate limiting (except for first symbol)
        if idx > 0:
            await asyncio.sleep(0.5)  # 500ms delay between symbols

        # 1) Underlying spot - handle futures vs equity
        if is_futures_symbol(sym):
            # For futures, get spot from Yahoo Finance (tastytrade doesn't provide futures prices)
            spot = get_futures_spot_price(sym)
            if spot is None:
                skip_stats[SKIP_NO_QUOTE] += 1
                logger.debug(f"Skipping {sym}: {SKIP_NO_QUOTE}")
                print(f"[WARN] No quote available for {sym}, skipping.", file=sys.stderr)
                continue
        else:
            # For equity, use standard equity market data
            try:
                md = get_market_data(session, sym, InstrumentType.EQUITY)
                if md is None or md.last is None:
                    skip_stats[SKIP_NO_QUOTE] += 1
                    logger.debug(f"Skipping {sym}: {SKIP_NO_QUOTE}")
                    print(f"[WARN] No quote for {sym}, skipping.", file=sys.stderr)
                    continue
                spot = float(md.last) if md.last is not None else float(md.mark)
            except Exception as e:
                skip_stats[SKIP_NO_QUOTE] += 1
                logger.debug(f"Skipping {sym}: {SKIP_NO_QUOTE} (error: {e})")
                print(f"[WARN] Could not get market data for {sym}: {e}, skipping.", file=sys.stderr)
                continue

        # 2) Extract earnings data and liquidity rating for this symbol
        earnings_date = None
        earnings_source = "none"  # Default: no earnings data found
        liq_rating = None  # Liquidity rating (0-5 scale)

        if sym in market_metrics:
            metric_info = market_metrics[sym]
            earnings = getattr(metric_info, 'earnings', None)
            if earnings:
                earnings_date = getattr(earnings, 'expected_report_date', None)

            # Extract liquidity_rating for CSV output
            liq_rating = getattr(metric_info, 'liquidity_rating', None)

        # Determine earnings_source from earnings_data dict (if provided)
        if earnings_data is not None and sym in earnings_data:
            earnings_source = earnings_data[sym].get('source', 'none')

        # 2b) Fetch today's option volume from dxFeed Underlying event (only if using --options-volume)
        option_volume = None
        if options_volume_threshold is not None:
            try:
                underlying_event = await snapshot_underlying(session, sym, timeout_s=timeout_s)
                if underlying_event is not None:
                    option_volume = underlying_event.option_volume
                    logger.info(f"{sym}: Option volume today: {option_volume}")
                else:
                    logger.warning(f"{sym}: No Underlying event received")
            except Exception as e:
                logger.warning(f"{sym}: Failed to fetch Underlying event: {e}")
                option_volume = None

        # 3) Chain (nested) - handle futures vs equity
        if is_futures_symbol(sym):
            # For futures, use NestedFutureOptionChain and extract option_chains
            futures_chain = NestedFutureOptionChain.get(session, sym)
            if not futures_chain or not futures_chain.option_chains:
                skip_stats[SKIP_NO_CHAIN] += 1
                logger.debug(f"Skipping {sym}: {SKIP_NO_CHAIN}")
                print(f"[WARN] No option chain for {sym}, skipping.", file=sys.stderr)
                continue
            chain = futures_chain.option_chains[0]  # Get the first option chain
        else:
            # For equity, use NestedOptionChain
            chain_list = NestedOptionChain.get(session, sym)
            if not chain_list:
                skip_stats[SKIP_NO_CHAIN] += 1
                logger.debug(f"Skipping {sym}: {SKIP_NO_CHAIN}")
                print(f"[WARN] No option chain for {sym}, skipping.", file=sys.stderr)
                continue
            chain = chain_list[0]  # API returns a list; take first element

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
                skip_stats[SKIP_EARNINGS_CONFLICT] += 1
                logger.debug(f"Skipping {sym}: {SKIP_EARNINGS_CONFLICT} - {reason}")
                print(f"[FILTERED] {sym}: {reason}", file=sys.stderr)
                if show_earnings_conflicts:
                    # Note: We'd compute FF here if we had the data, but skipping for simplicity
                    filtered_rows.append({"symbol": sym, "reason": reason})
                continue

        # 2.5.2) Liquidity filtering (choose between two modes)
        if not skip_liquidity_check:
            if options_volume_threshold is not None:
                # Mode 1: Use dxFeed option volume (requires market hours)
                passes, reason = check_option_volume(sym, option_volume, options_volume_threshold)
                if not passes:
                    skip_stats[SKIP_VOLUME_TOO_LOW] += 1
                    logger.info(f"{sym}: {reason}")
                    print(f"[FILTERED] {sym}: {reason}", file=sys.stderr)
                    continue
            else:
                # Mode 2: Use liquidity_rating from Market Metrics (24/7 available)
                passes, reason = check_liquidity_rating(sym, market_metrics, min_rating=3)
                if not passes:
                    skip_stats[SKIP_VOLUME_TOO_LOW] += 1  # Reuse same skip reason for both modes
                    logger.info(f"{sym}: {reason}")
                    print(f"[FILTERED] {sym}: {reason}", file=sys.stderr)
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
                try:
                    delta_strikes = await get_double_calendar_strikes(
                        session=session,
                        expiration_obj=exp_obj,
                        spot=spot,
                        call_target_delta=0.35,
                        put_target_delta=-0.35,
                        delta_tolerance=delta_tolerance,
                        timeout_s=timeout_s
                    )
                except Exception as e:
                    logger.warning(f"Greeks streamer connection failed for {sym} {exp_date}: {e}. Skipping this expiration.")
                    delta_strikes = {"call_35delta": None, "put_35delta": None}  # Both legs missing

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

                # DOUBLE CALENDAR REQUIRES BOTH LEGS
                has_call_calendar = front_call is not None and back_call is not None
                has_put_calendar = front_put is not None and back_put is not None

                # Skip if we don't have BOTH call and put calendars
                if not (has_call_calendar and has_put_calendar):
                    skip_stats[SKIP_BOTH_LEGS_REQUIRED] += 1
                    logger.debug(f"Skipping {sym} double {front}-{back}: {SKIP_BOTH_LEGS_REQUIRED}")
                    continue

                # Validate inputs before calculating forward IV
                call_skip_reason = validate_ff_inputs(
                    front_call.iv, back_call.iv, front_choice["dte"], back_choice["dte"]
                )
                if call_skip_reason:
                    skip_stats[SKIP_NONPOSITIVE_FWD_VAR] += 1
                    logger.debug(f"Skipping {sym} double {front}-{back} call: {call_skip_reason}")
                    continue

                put_skip_reason = validate_ff_inputs(
                    front_put.iv, back_put.iv, front_choice["dte"], back_choice["dte"]
                )
                if put_skip_reason:
                    skip_stats[SKIP_NONPOSITIVE_FWD_VAR] += 1
                    logger.debug(f"Skipping {sym} double {front}-{back} put: {put_skip_reason}")
                    continue

                # Calculate FFs for both legs
                fwd_call = forward_iv(front_call.iv, back_call.iv, front_choice["dte"], back_choice["dte"])
                fwd_put = forward_iv(front_put.iv, back_put.iv, front_choice["dte"], back_choice["dte"])

                if fwd_call is None or fwd_call <= 0 or fwd_put is None or fwd_put <= 0:
                    skip_stats[SKIP_NONPOSITIVE_FWD_VAR] += 1
                    logger.debug(f"Skipping {sym} double {front}-{back}: negative forward IV")
                    continue

                ff_call = (front_call.iv - fwd_call) / fwd_call
                ff_put = (front_put.iv - fwd_put) / fwd_put

                # Calculate min FF (both wings must independently meet threshold)
                min_ff_double = min(ff_call, ff_put)

                # Calculate combined FF (average of both legs - kept for reference)
                combined_ff = (ff_call + ff_put) / 2.0

                # Use Greeks IV as primary (strike-level precision, preserves skew)
                # Fallback to ex-earn IV only if Greeks data is missing/invalid
                call_iv_source_front = "greeks"
                call_iv_source_back = "greeks"
                put_iv_source_front = "greeks"
                put_iv_source_back = "greeks"

                # Primary: Use Greeks IV from strike-level snapshot
                front_call_iv = front_call.iv
                back_call_iv = back_call.iv
                front_put_iv = front_put.iv
                back_put_iv = back_put.iv

                # Rare fallback: Use ex-earn IV if Greeks data missing for call leg
                if front_call_iv is None or front_call_iv <= 0:
                    logger.warning(f"{sym}: Greeks IV missing for call front leg, using ex-earn fallback")
                    xearn_call_front = extract_xearn_iv(market_metrics, sym, front_choice["expiration"])
                    if xearn_call_front and xearn_call_front > 0:
                        front_call_iv = xearn_call_front
                        call_iv_source_front = "exearn_fallback"
                    else:
                        skip_stats[SKIP_MISSING_IV] += 1
                        logger.debug(f"Skipping {sym} double {front}-{back}: missing call front IV")
                        continue

                if back_call_iv is None or back_call_iv <= 0:
                    logger.warning(f"{sym}: Greeks IV missing for call back leg, using ex-earn fallback")
                    xearn_call_back = extract_xearn_iv(market_metrics, sym, back_choice["expiration"])
                    if xearn_call_back and xearn_call_back > 0:
                        back_call_iv = xearn_call_back
                        call_iv_source_back = "exearn_fallback"
                    else:
                        skip_stats[SKIP_MISSING_IV] += 1
                        logger.debug(f"Skipping {sym} double {front}-{back}: missing call back IV")
                        continue

                # Rare fallback: Use ex-earn IV if Greeks data missing for put leg
                if front_put_iv is None or front_put_iv <= 0:
                    logger.warning(f"{sym}: Greeks IV missing for put front leg, using ex-earn fallback")
                    xearn_put_front = extract_xearn_iv(market_metrics, sym, front_choice["expiration"])
                    if xearn_put_front and xearn_put_front > 0:
                        front_put_iv = xearn_put_front
                        put_iv_source_front = "exearn_fallback"
                    else:
                        skip_stats[SKIP_MISSING_IV] += 1
                        logger.debug(f"Skipping {sym} double {front}-{back}: missing put front IV")
                        continue

                if back_put_iv is None or back_put_iv <= 0:
                    logger.warning(f"{sym}: Greeks IV missing for put back leg, using ex-earn fallback")
                    xearn_put_back = extract_xearn_iv(market_metrics, sym, back_choice["expiration"])
                    if xearn_put_back and xearn_put_back > 0:
                        back_put_iv = xearn_put_back
                        put_iv_source_back = "exearn_fallback"
                    else:
                        skip_stats[SKIP_MISSING_IV] += 1
                        logger.debug(f"Skipping {sym} double {front}-{back}: missing put back IV")
                        continue

                # Recalculate forward IV and FF with actual IVs used (Greeks or fallback)
                fwd_call = forward_iv(front_call_iv, back_call_iv, front_choice["dte"], back_choice["dte"])
                fwd_put = forward_iv(front_put_iv, back_put_iv, front_choice["dte"], back_choice["dte"])

                if fwd_call is None or fwd_call <= 0 or fwd_put is None or fwd_put <= 0:
                    skip_stats[SKIP_NONPOSITIVE_FWD_VAR] += 1
                    logger.debug(f"Skipping {sym} double {front}-{back}: negative forward IV after IV assignment")
                    continue

                ff_call = (front_call_iv - fwd_call) / fwd_call
                ff_put = (front_put_iv - fwd_put) / fwd_put

                # Calculate min FF (both wings must independently meet threshold)
                min_ff_double = min(ff_call, ff_put)

                # Calculate combined FF (average of both legs - kept for reference)
                combined_ff = (ff_call + ff_put) / 2.0

                # Filter on min_ff (both wings must independently meet threshold)
                if min_ff_double >= min_ff or show_all_scans:
                    passed += 1
                    rows.append({
                        # Common (8)
                        "timestamp": timestamp,
                        "symbol": sym,
                        "structure": "double",
                        "spot_price": f"{spot:.2f}",
                        "front_dte": front_choice["dte"],
                        "back_dte": back_choice["dte"],
                        "front_expiry": front_choice["expiration"].isoformat(),
                        "back_expiry": back_choice["expiration"].isoformat(),
                        # ATM-specific (8) - empty for double structure
                        "atm_strike": "",
                        "atm_delta": "",
                        "atm_ff": "",
                        "atm_iv_front": "",
                        "atm_iv_back": "",
                        "atm_fwd_iv": "",
                        "atm_iv_source_front": "",
                        "atm_iv_source_back": "",
                        # Double-specific (8) - populated for double structure
                        "call_strike": f"{front_call.strike:.2f}",
                        "put_strike": f"{front_put.strike:.2f}",
                        "call_delta": round(front_call.actual_delta, 4),
                        "put_delta": round(front_put.actual_delta, 4),
                        "call_ff": round(ff_call, 6),
                        "put_ff": round(ff_put, 6),
                        "min_ff": round(min_ff_double, 6),
                        "combined_ff": round(combined_ff, 6),
                        # IV detail (6)
                        "call_front_iv": round(front_call_iv, 6),
                        "call_back_iv": round(back_call_iv, 6),
                        "call_fwd_iv": round(fwd_call, 6),
                        "put_front_iv": round(front_put_iv, 6),
                        "put_back_iv": round(back_put_iv, 6),
                        "put_fwd_iv": round(fwd_put, 6),
                        # IV sources - double (4)
                        "iv_source_call_front": call_iv_source_front,
                        "iv_source_call_back": call_iv_source_back,
                        "iv_source_put_front": put_iv_source_front,
                        "iv_source_put_back": put_iv_source_back,
                        # Quality filters (5)
                        "earnings_conflict": "no" if not earnings_date else "",
                        "earnings_date": earnings_date.isoformat() if earnings_date else "",
                        "option_volume_today": f"{option_volume:.0f}" if option_volume is not None else "",
                        "liq_rating": str(liq_rating) if liq_rating is not None else "",
                        "earnings_source": earnings_source,
                        # Tracking (1)
                        "skip_reason": ""
                    })

        if scan_atm:
            # ========== ATM CALENDAR MODE (delta-based strike selection) ==========
            choices: Dict[int, ATMChoice] = {}
            streamer_syms: List[str] = []

            # First, fetch Greeks for a range of strikes for each expiration
            # This allows delta-based ATM strike selection (50Δ target)
            for target in required_targets:
                exp_date = nearest_expiration(chain, target, dte_tolerance)
                if exp_date is None:
                    continue
                exp_obj = exp_by_date[exp_date]

                # Fetch Greeks for strikes around spot price (±25% range)
                try:
                    greeks_map = await snapshot_greeks_for_range(
                        session, exp_obj, spot, range_pct=0.25, timeout_s=timeout_s
                    )
                except Exception as e:
                    logger.warning(f"Greeks streamer connection failed for {sym} {exp_date}: {e}. Skipping this expiration.")
                    greeks_map = {}  # Empty map - pick_atm_strike will fall back to nearest-spot

                # Select ATM strike using delta-based selection (50Δ target)
                # Falls back to nearest-spot if no Greeks available or no strikes within tolerance
                strike, actual_delta, call_sym, put_sym = pick_atm_strike(exp_obj, spot, greeks_map)

                choices[target] = ATMChoice(
                    expiration=exp_date,
                    strike=strike,
                    call_streamer_symbol=call_sym,
                    put_streamer_symbol=put_sym,
                    dte=dte(exp_date, today),
                    actual_delta=actual_delta
                )
                streamer_syms.extend([call_sym, put_sym])

            if not choices:
                print(f"[WARN] No expirations matched tolerance for {sym}", file=sys.stderr)
                continue

            # 4) Use Greeks IV as primary (strike-level), fallback to ex-earn IV if missing
            # Store call and put IVs separately for transparency
            call_iv_by_target: Dict[int, float] = {}
            put_iv_by_target: Dict[int, float] = {}
            call_iv_source_by_target: Dict[int, str] = {}
            put_iv_source_by_target: Dict[int, str] = {}

            # Primary: Snapshot Greeks (to get IV and delta) for all ATM contracts
            try:
                greek_map = await snapshot_greeks(session, streamer_syms, timeout_s=timeout_s)
            except Exception as e:
                logger.warning(f"Greeks streamer connection failed for {sym}: {e}. Falling back to X-earn IV.")
                greek_map = {}  # Empty map - will fall back to X-earn IV

            for target, ch in choices.items():
                call_iv = None
                put_iv = None
                # Unpack (iv, delta) tuples from greek_map
                if ch.call_streamer_symbol in greek_map:
                    iv, delta = greek_map[ch.call_streamer_symbol]
                    call_iv = iv if iv is not None and iv > 0 else None
                if ch.put_streamer_symbol in greek_map:
                    iv, delta = greek_map[ch.put_streamer_symbol]
                    put_iv = iv if iv is not None and iv > 0 else None

                # Store Greeks IV if available
                if call_iv:
                    call_iv_by_target[target] = call_iv
                    call_iv_source_by_target[target] = "greeks"
                if put_iv:
                    put_iv_by_target[target] = put_iv
                    put_iv_source_by_target[target] = "greeks"

            # Rare fallback: Use ex-earn IV for targets where Greeks IV is missing
            for target, ch in choices.items():
                # Check if we need fallback for call IV
                if target not in call_iv_by_target:
                    logger.warning(f"{sym} {target}DTE: Greeks IV missing for call, using ex-earn fallback")
                    xearn_iv = extract_xearn_iv(market_metrics, sym, ch.expiration)
                    if xearn_iv is not None and xearn_iv > 0:
                        call_iv_by_target[target] = xearn_iv
                        call_iv_source_by_target[target] = "exearn_fallback"

                # Check if we need fallback for put IV
                if target not in put_iv_by_target:
                    logger.warning(f"{sym} {target}DTE: Greeks IV missing for put, using ex-earn fallback")
                    xearn_iv = extract_xearn_iv(market_metrics, sym, ch.expiration)
                    if xearn_iv is not None and xearn_iv > 0:
                        put_iv_by_target[target] = xearn_iv
                        put_iv_source_by_target[target] = "exearn_fallback"

            # 6) Build rows for pairs
            for front, back in pairs:
                if front not in choices or back not in choices:
                    continue

                front_choice = choices[front]
                back_choice = choices[back]

                # Need both call and put IVs for both expirations
                if front not in call_iv_by_target or front not in put_iv_by_target:
                    continue
                if back not in call_iv_by_target or back not in put_iv_by_target:
                    continue

                call_iv_f = call_iv_by_target[front]
                call_iv_b = call_iv_by_target[back]
                put_iv_f = put_iv_by_target[front]
                put_iv_b = put_iv_by_target[back]

                # Validate inputs before calculating forward IV
                call_skip_reason = validate_ff_inputs(call_iv_f, call_iv_b, front_choice.dte, back_choice.dte)
                if call_skip_reason:
                    skip_stats[SKIP_NONPOSITIVE_FWD_VAR] += 1
                    logger.debug(f"Skipping {sym} ATM {front}-{back} call: {call_skip_reason}")
                    continue

                put_skip_reason = validate_ff_inputs(put_iv_f, put_iv_b, front_choice.dte, back_choice.dte)
                if put_skip_reason:
                    skip_stats[SKIP_NONPOSITIVE_FWD_VAR] += 1
                    logger.debug(f"Skipping {sym} ATM {front}-{back} put: {put_skip_reason}")
                    continue

                # Calculate single ATM FF using average of call and put IV
                # Per CLAUDE.md: "IV = average of (call IV, put IV) at that strike"
                atm_iv_front = (call_iv_f + put_iv_f) / 2.0
                atm_iv_back = (call_iv_b + put_iv_b) / 2.0

                atm_fwd_iv = forward_iv(atm_iv_front, atm_iv_back, front_choice.dte, back_choice.dte)
                if atm_fwd_iv is None or atm_fwd_iv <= 0:
                    skip_stats[SKIP_NONPOSITIVE_FWD_VAR] += 1
                    logger.debug(f"Skipping {sym} ATM {front}-{back}: negative forward IV")
                    continue

                atm_ff = (atm_iv_front - atm_fwd_iv) / atm_fwd_iv

                # Determine IV sources for both call and put
                call_iv_src_front = call_iv_source_by_target.get(front, "greeks")
                call_iv_src_back = call_iv_source_by_target.get(back, "greeks")
                put_iv_src_front = put_iv_source_by_target.get(front, "greeks")
                put_iv_src_back = put_iv_source_by_target.get(back, "greeks")

                # ATM IV sources: Use call source if both match, otherwise indicate "mixed"
                # In practice, they should match since we use the same strike
                atm_iv_src_front = call_iv_src_front if call_iv_src_front == put_iv_src_front else "mixed"
                atm_iv_src_back = call_iv_src_back if call_iv_src_back == put_iv_src_back else "mixed"

                # Include result if: (1) meets FF threshold, OR (2) show_all_scans is enabled
                if atm_ff >= min_ff or show_all_scans:
                    passed += 1
                    rows.append({
                        # Common (8)
                        "timestamp": timestamp,
                        "symbol": sym,
                        "structure": "atm-call",
                        "spot_price": f"{spot:.2f}",
                        "front_dte": front_choice.dte,
                        "back_dte": back_choice.dte,
                        "front_expiry": front_choice.expiration.isoformat(),
                        "back_expiry": back_choice.expiration.isoformat(),
                        # ATM-specific (8) - populated for ATM structure
                        "atm_strike": f"{front_choice.strike:.2f}",
                        "atm_delta": round(front_choice.actual_delta, 4) if front_choice.actual_delta is not None else "",
                        "atm_ff": round(atm_ff, 6),
                        "atm_iv_front": round(atm_iv_front, 6),
                        "atm_iv_back": round(atm_iv_back, 6),
                        "atm_fwd_iv": round(atm_fwd_iv, 6),
                        "atm_iv_source_front": atm_iv_src_front,
                        "atm_iv_source_back": atm_iv_src_back,
                        # Double-specific (8) - empty for ATM structure
                        "call_strike": "",
                        "put_strike": "",
                        "call_delta": "",
                        "put_delta": "",
                        "call_ff": "",
                        "put_ff": "",
                        "min_ff": "",
                        "combined_ff": "",
                        # IV detail (6) - keep for transparency per CLAUDE.md
                        "call_front_iv": round(call_iv_f, 6),
                        "call_back_iv": round(call_iv_b, 6),
                        "call_fwd_iv": "",
                        "put_front_iv": round(put_iv_f, 6),
                        "put_back_iv": round(put_iv_b, 6),
                        "put_fwd_iv": "",
                        # IV sources - double (4) - keep for reference
                        "iv_source_call_front": call_iv_src_front,
                        "iv_source_call_back": call_iv_src_back,
                        "iv_source_put_front": put_iv_src_front,
                        "iv_source_put_back": put_iv_src_back,
                        # Quality filters (5)
                        "earnings_conflict": "no" if not earnings_date else "",
                        "earnings_date": earnings_date.isoformat() if earnings_date else "",
                        "option_volume_today": f"{option_volume:.0f}" if option_volume is not None else "",
                        "liq_rating": str(liq_rating) if liq_rating is not None else "",
                        "earnings_source": earnings_source,
                        # Tracking (1)
                        "skip_reason": ""
                    })

    # Sort results:
    # - Double calendars: sort by min_ff descending (primary), combined_ff (secondary), symbol (tertiary)
    # - ATM calendars: sort by atm_ff descending (primary), symbol (secondary)
    # Separate the two structures for appropriate sorting
    doubles = [r for r in rows if r["structure"] == "double"]
    atm_rows = [r for r in rows if r["structure"] == "atm-call"]

    # Sort doubles by min_ff (highest first), then combined_ff, then symbol
    doubles.sort(key=lambda r: (-r["min_ff"], -r["combined_ff"], r["symbol"]))

    # Sort ATM by atm_ff (highest first), then symbol
    atm_rows.sort(key=lambda r: (-r["atm_ff"], r["symbol"]))

    # Combine back: doubles first (higher priority), then ATM
    rows = doubles + atm_rows

    # Return rows and statistics
    return rows, skip_stats, scanned, passed

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
    # Workaround for Python 3.14 asyncio task cancellation recursion bug
    # When DXLinkStreamer connections timeout, pending _connect() tasks accumulate
    # and can trigger RecursionError during asyncio cleanup. Increasing the limit
    # gives asyncio enough stack depth to handle the cancellation chains.
    # See: https://github.com/python/cpython/issues/126211
    sys.setrecursionlimit(10000)

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

  # Use precise option volume filtering (requires market hours, default: 10k threshold)
  python ff_tastytrade_scanner.py --tickers SPY QQQ --pairs 30-60 --options-volume

  # Use precise option volume with custom threshold (requires market hours)
  python ff_tastytrade_scanner.py --tickers SPY QQQ --pairs 30-60 --options-volume 5000

  # Adjust delta tolerance for double calendars (tighter selection)
  python ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --structure double --delta-tolerance 0.03
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

    # Earnings filtering flags
    ap.add_argument("--allow-earnings", action="store_true",
                    help="Allow trading through earnings (default: filter earnings conflicts).")
    ap.add_argument("--show-earnings-conflicts", action="store_true",
                    help="Show filtered positions due to earnings.")

    # Volume filtering flags
    ap.add_argument("--options-volume", type=float, nargs='?', const=10000, default=None,
                    help="Use dxFeed option volume filtering (requires market hours). "
                         "Default threshold: 10000 contracts. "
                         "If omitted, uses liquidity_rating >= 3 (24/7 available). "
                         "Examples: --options-volume (>=10k), --options-volume 5000 (>=5k).")
    ap.add_argument("--skip-liquidity-check", action="store_true",
                    help="Disable all volume/liquidity filtering.")

    # Debug/analysis flags
    ap.add_argument("--show-all-scans", action="store_true",
                    help="Show all scan results regardless of FF threshold (for data pipeline testing).")

    # Structure selection
    ap.add_argument("--structure", type=str, default="both", choices=["atm-call", "double", "both"],
                    help="Calendar structure: atm-call (ATM only), double (±35Δ only), or both (default: both).")
    ap.add_argument("--delta-tolerance", type=float, default=0.05,
                    help="Max delta deviation for double calendars (default: 0.05 = ±5Δ). Range: 0.01-0.10.")

    # Debug/logging options
    ap.add_argument("--debug", action="store_true",
                    help="Enable debug logging from tastytrade SDK and httpx library.")

    args = ap.parse_args()
    tickers = read_list_arg(args.tickers)
    pairs = parse_pairs(read_list_arg(args.pairs))

    # Configure logging based on --debug flag
    if args.debug:
        # Debug mode: Show all DEBUG messages from all libraries
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    else:
        # Normal mode: Silence third-party library debug/info logging
        logging.basicConfig(
            level=logging.WARNING,
            format='%(message)s'
        )
        # Explicitly silence noisy libraries
        logging.getLogger('tastytrade').setLevel(logging.WARNING)
        logging.getLogger('httpx').setLevel(logging.WARNING)
        logging.getLogger('earnings_cache').setLevel(logging.WARNING)

    # Validate flag values
    if args.delta_tolerance < 0.01 or args.delta_tolerance > 0.10:
        print("ERROR: --delta-tolerance must be between 0.01 and 0.10", file=sys.stderr)
        sys.exit(1)

    username = os.environ.get("TT_USERNAME", "").strip()
    password = os.environ.get("TT_PASSWORD", "").strip()
    if not username or not password:
        print("ERROR: Set TT_USERNAME and TT_PASSWORD env vars.", file=sys.stderr)
        sys.exit(2)

    # Create session
    session = Session(username, password=password, is_test=bool(args.sandbox))

    # Early earnings pre-filter (NEW: Issue #16)
    # Filter symbols by earnings conflicts BEFORE any TastyTrade API calls
    # Default: filter earnings (unless --allow-earnings flag is set)
    earnings_data = None  # Initialize earnings_data (will be populated or set to dummy)

    if not args.allow_earnings:
        start_time = time.time()

        # Initialize cache with TastyTrade session for fallback (Issue #17)
        cache = EarningsCache(session=session)

        # Batch fetch earnings for all symbols
        earnings_data = cache.batch_get_earnings(tickers)

        # Count cache hits/misses
        cache_hits = sum(1 for d in earnings_data.values() if d['source'] == 'cache')
        fresh_fetches = len(earnings_data) - cache_hits

        # Filter symbols using existing check_earnings_conflict() logic
        passing_symbols = []
        filtered_symbols = []

        # Determine back expiry from DTE pairs (use max back DTE for conservative filtering)
        back_dte = max(pair[1] for pair in pairs)
        back_expiry = ny_today() + timedelta(days=back_dte)

        for symbol in tickers:
            # Check earnings conflict
            next_earnings = earnings_data[symbol]["next_earnings"]
            if next_earnings:
                earnings_date = date.fromisoformat(next_earnings)
                if ny_today() <= earnings_date <= back_expiry:
                    reason = f"Earnings on {next_earnings} conflicts with back expiry {back_expiry}"
                    filtered_symbols.append((symbol, reason))
                    continue

            passing_symbols.append(symbol)

        # Log results
        elapsed = time.time() - start_time
        print(f"Earnings pre-filter: {len(tickers)} → {len(passing_symbols)} passed ({len(filtered_symbols)} filtered)")
        print(f"  Cache hits: {cache_hits} | Fresh fetches: {fresh_fetches}")
        print(f"  Earnings check completed in {elapsed:.1f}s")

        if args.show_earnings_conflicts:
            for symbol, reason in filtered_symbols:
                print(f"  {symbol}: {reason}")

        # Only process passing symbols
        tickers = passing_symbols

        # Early exit if all symbols filtered
        if not tickers:
            print("No symbols passed earnings filter. Use --allow-earnings to scan through earnings.", file=sys.stderr)
            sys.exit(0)
    else:
        # If --allow-earnings is set, mark all symbols as having earnings filter bypassed
        # Real earnings dates will still be fetched from market_metrics API inside scan()
        # This just sets the earnings_source column to "skipped" for CSV tracking
        earnings_data = {symbol: {'source': 'skipped', 'next_earnings': None} for symbol in tickers}

    # Run scan
    # Default: filter earnings (unless --allow-earnings flag is set)
    skip_earnings_flag = not args.allow_earnings

    rows, skip_stats, scanned, passed = asyncio.run(scan(
        session, tickers, pairs, args.min_ff, args.dte_tolerance, args.timeout,
        skip_earnings=skip_earnings_flag,
        options_volume_threshold=args.options_volume,
        skip_liquidity_check=args.skip_liquidity_check,
        show_earnings_conflicts=args.show_earnings_conflicts,
        show_all_scans=args.show_all_scans,
        structure=args.structure,
        delta_tolerance=args.delta_tolerance,
        earnings_data=earnings_data
    ))

    # v2.2 CSV schema (40 columns)
    # Breaking changes from v2.1:
    # - Added: atm_iv_source_front, atm_iv_source_back (ATM-specific IV source tracking)
    # - Added: liq_rating (liquidity_rating 0-5 from Market Metrics)
    # - Renamed: avg_options_volume_20d → option_volume_today (now using dxFeed Underlying.optionVolume)
    # - Reordered: Logical grouping by structure (common, ATM, double, IV detail, sources, quality)
    cols = [
        # Common (8)
        "timestamp", "symbol", "structure", "spot_price",
        "front_dte", "back_dte", "front_expiry", "back_expiry",
        # ATM-specific (8)
        "atm_strike", "atm_delta", "atm_ff",
        "atm_iv_front", "atm_iv_back", "atm_fwd_iv",
        "atm_iv_source_front", "atm_iv_source_back",
        # Double-specific (8)
        "call_strike", "put_strike", "call_delta", "put_delta",
        "call_ff", "put_ff", "min_ff", "combined_ff",
        # IV detail (6)
        "call_front_iv", "call_back_iv", "call_fwd_iv",
        "put_front_iv", "put_back_iv", "put_fwd_iv",
        # IV sources - double (4)
        "iv_source_call_front", "iv_source_call_back",
        "iv_source_put_front", "iv_source_put_back",
        # Quality filters (5)
        "earnings_conflict", "earnings_date",
        "option_volume_today", "liq_rating", "earnings_source",
        # Tracking (1)
        "skip_reason"
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

    # Print scan summary statistics
    total_skipped = sum(skip_stats.values())
    print(f"\n=== Scan Summary ===", file=sys.stderr)
    print(f"Scanned: {scanned} symbols", file=sys.stderr)
    print(f"Passed: {passed} opportunities", file=sys.stderr)
    print(f"Skipped: {total_skipped} symbols", file=sys.stderr)
    if total_skipped > 0:
        print(f"\nSkip breakdown:", file=sys.stderr)
        for reason, count in skip_stats.items():
            if count > 0:
                print(f"  - {reason}: {count}", file=sys.stderr)

if __name__ == "__main__":
    main()
