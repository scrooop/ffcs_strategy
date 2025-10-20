#!/usr/bin/env python3
"""
Quick test to see if tastytrade API supports futures symbols.
"""
import os
from tastytrade import Session
from tastytrade.market_data import get_market_data
from tastytrade.order import InstrumentType
from tastytrade.instruments import NestedOptionChain, NestedFutureOptionChain, Future

# Authenticate
username = os.getenv("TT_USERNAME")
password = os.getenv("TT_PASSWORD")
session = Session(username, password=password, is_test=False)

# Test 1: Can we get market data for /ES as FUTURE?
print("=" * 60)
print("TEST 1: Get market data for /ES as FUTURE")
print("=" * 60)
try:
    md = get_market_data(session, "/ES", InstrumentType.FUTURE)
    print(f"SUCCESS: {md}")
    print(f"Last price: {md.last}")
except Exception as e:
    print(f"FAILED: {e}")

# Test 2: Can we get /ES future info?
print("\n" + "=" * 60)
print("TEST 2: Get Future instrument for /ES")
print("=" * 60)
try:
    future = Future.get(session, "/ES")
    print(f"SUCCESS: {future}")
except Exception as e:
    print(f"FAILED: {e}")

# Test 3: Can we get option chain for /ES?
print("\n" + "=" * 60)
print("TEST 3: Get option chain for /ES using NestedOptionChain")
print("=" * 60)
try:
    chain = NestedOptionChain.get(session, "/ES")
    print(f"SUCCESS: Found {len(chain[0].expirations) if chain else 0} expirations")
    if chain:
        print(f"First expiration: {chain[0].expirations[0].expiration_date}")
except Exception as e:
    print(f"FAILED: {e}")

# Test 4: Can we get futures option chain using NestedFutureOptionChain?
print("\n" + "=" * 60)
print("TEST 4: Get futures option chain using NestedFutureOptionChain")
print("=" * 60)
try:
    chain = NestedFutureOptionChain.get(session, "/ES")
    print(f"SUCCESS: {chain}")
    if chain:
        print(f"Number of chains: {len(chain)}")
        if len(chain) > 0:
            print(f"First chain expirations: {len(chain[0].expirations)}")
except Exception as e:
    print(f"FAILED: {e}")

# Test 5: Try /GC
print("\n" + "=" * 60)
print("TEST 5: Get market data for /GC as FUTURE")
print("=" * 60)
try:
    md = get_market_data(session, "/GC", InstrumentType.FUTURE)
    print(f"SUCCESS: {md}")
    print(f"Last price: {md.last}")
except Exception as e:
    print(f"FAILED: {e}")

# Test 6: Try ES without /
print("\n" + "=" * 60)
print("TEST 6: Get market data for ES (no /) as EQUITY")
print("=" * 60)
try:
    md = get_market_data(session, "ES", InstrumentType.EQUITY)
    print(f"SUCCESS: {md}")
    print(f"Last price: {md.last}")
except Exception as e:
    print(f"FAILED: {e}")

print("\n" + "=" * 60)
print("TESTS COMPLETE")
print("=" * 60)
