#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# test_double_calendar_strikes.py
# Test script for Issue #4: Double Calendar Strike Selection
#
# This script validates that the new pick_delta_strike() and get_double_calendar_strikes()
# functions correctly select ±35Δ strikes for double calendar spreads.
#
# Usage:
#   python test_double_calendar_strikes.py --ticker SPY --target-dte 60
#
# Requirements:
#   TT_USERNAME and TT_PASSWORD environment variables must be set

import os
import sys
import asyncio
import argparse
from datetime import date

from tastytrade import Session
from tastytrade.market_data import get_market_data
from tastytrade.order import InstrumentType
from tastytrade.instruments import NestedOptionChain
from tastytrade.utils import today_in_new_york

# Import the functions we're testing
sys.path.insert(0, os.path.dirname(__file__))
from ff_tastytrade_scanner import (
    nearest_expiration,
    get_double_calendar_strikes,
    dte
)

async def test_double_calendar_selection(
    session: Session,
    ticker: str,
    target_dte: int,
    dte_tolerance: int = 7
):
    """
    Test the double calendar strike selection for a given ticker and DTE.
    """
    print(f"\n{'='*70}")
    print(f"Testing Double Calendar Strike Selection")
    print(f"Ticker: {ticker} | Target DTE: {target_dte}")
    print(f"{'='*70}\n")

    # 1) Get underlying spot price
    print(f"[1/4] Fetching spot price for {ticker}...")
    md = get_market_data(session, ticker, InstrumentType.EQUITY)
    if md is None or md.last is None:
        print(f"ERROR: No market data for {ticker}")
        return
    spot = float(md.last) if md.last is not None else float(md.mark)
    print(f"      Spot price: ${spot:.2f}")

    # 2) Get option chain
    print(f"\n[2/4] Fetching option chain...")
    chain_list = NestedOptionChain.get(session, ticker)
    if not chain_list:
        print(f"ERROR: No option chain for {ticker}")
        return
    chain = chain_list[0]

    # 3) Find expiration closest to target DTE
    print(f"\n[3/4] Finding expiration near {target_dte} DTE (±{dte_tolerance} days)...")
    exp_date = nearest_expiration(chain, target_dte, dte_tolerance)
    if exp_date is None:
        print(f"ERROR: No expiration found within tolerance")
        return

    today = today_in_new_york()
    actual_dte = dte(exp_date, today)
    print(f"      Selected expiration: {exp_date} ({actual_dte} DTE)")

    # 4) Get double calendar strikes (±35Δ)
    print(f"\n[4/4] Selecting ±35Δ strikes...")
    exp_by_date = {exp.expiration_date: exp for exp in chain.expirations}
    exp_obj = exp_by_date[exp_date]

    delta_strikes = await get_double_calendar_strikes(
        session=session,
        expiration_obj=exp_obj,
        spot=spot,
        call_target_delta=0.35,
        put_target_delta=-0.35,
        delta_tolerance=0.05,
        timeout_s=5.0
    )

    # Display results
    print(f"\n{'='*70}")
    print(f"RESULTS: Double Calendar Strike Selection")
    print(f"{'='*70}\n")

    call_strike = delta_strikes.get("call_35delta")
    put_strike = delta_strikes.get("put_35delta")

    if call_strike:
        print(f"✓ +35Δ CALL:")
        print(f"    Strike:        ${call_strike.strike:.2f}")
        print(f"    Actual Delta:  {call_strike.actual_delta:.4f}")
        print(f"    IV:            {call_strike.iv:.4f} ({call_strike.iv*100:.2f}%)")
        print(f"    Symbol:        {call_strike.streamer_symbol}")
        print(f"    Delta Error:   {abs(call_strike.actual_delta - 0.35):.4f}")
    else:
        print(f"✗ +35Δ CALL: NOT FOUND (no strike within ±5Δ tolerance)")

    print()

    if put_strike:
        print(f"✓ -35Δ PUT:")
        print(f"    Strike:        ${put_strike.strike:.2f}")
        print(f"    Actual Delta:  {put_strike.actual_delta:.4f}")
        print(f"    IV:            {put_strike.iv:.4f} ({put_strike.iv*100:.2f}%)")
        print(f"    Symbol:        {put_strike.streamer_symbol}")
        print(f"    Delta Error:   {abs(put_strike.actual_delta - (-0.35)):.4f}")
    else:
        print(f"✗ -35Δ PUT: NOT FOUND (no strike within ±5Δ tolerance)")

    # Summary
    print(f"\n{'='*70}")
    if call_strike and put_strike:
        print(f"SUCCESS: Both ±35Δ strikes found within tolerance")
        strike_width = abs(call_strike.strike - put_strike.strike)
        print(f"Strike Width: ${strike_width:.2f} ({strike_width/spot*100:.1f}% of spot)")
    elif call_strike or put_strike:
        print(f"PARTIAL: Only one strike found (may need wider tolerance)")
    else:
        print(f"FAILURE: No strikes found (check tolerance or DTE)")
    print(f"{'='*70}\n")

def main():
    ap = argparse.ArgumentParser(
        description="Test double calendar strike selection (Issue #4)"
    )
    ap.add_argument(
        "--ticker",
        default="SPY",
        help="Ticker to test (default: SPY)"
    )
    ap.add_argument(
        "--target-dte",
        type=int,
        default=60,
        help="Target DTE for expiration (default: 60)"
    )
    ap.add_argument(
        "--dte-tolerance",
        type=int,
        default=7,
        help="DTE tolerance in days (default: 7)"
    )
    ap.add_argument(
        "--sandbox",
        action="store_true",
        help="Use sandbox environment (production required for live Greeks)"
    )

    args = ap.parse_args()

    # Get credentials
    username = os.environ.get("TT_USERNAME", "").strip()
    password = os.environ.get("TT_PASSWORD", "").strip()
    if not username or not password:
        print("ERROR: Set TT_USERNAME and TT_PASSWORD env vars.", file=sys.stderr)
        sys.exit(2)

    # Create session
    print("Authenticating with tastytrade...")
    session = Session(username, password=password, is_test=bool(args.sandbox))
    print("✓ Authentication successful\n")

    # Run test
    try:
        asyncio.run(
            test_double_calendar_selection(
                session,
                args.ticker,
                args.target_dte,
                args.dte_tolerance
            )
        )
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
