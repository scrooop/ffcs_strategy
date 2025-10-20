#!/usr/bin/env python3
"""
Examine all fields in NestedFutureOptionChain to find price data.
"""
import os
from tastytrade import Session
from tastytrade.instruments import NestedFutureOptionChain

# Authenticate
username = os.getenv("TT_USERNAME")
password = os.getenv("TT_PASSWORD")
session = Session(username, password=password, is_test=False)

# Get futures option chain
chain = NestedFutureOptionChain.get(session, "/ES")

print("="*60)
print("NestedFutureOptionChain fields:")
print("="*60)
print(f"Type: {type(chain)}")
print(f"Dir: {dir(chain)}")
print()

if chain.futures:
    print("="*60)
    print("Active futures contract details:")
    print("="*60)
    active = None
    for future in chain.futures:
        if hasattr(future, 'active_month') and future.active_month:
            active = future
            break

    if active:
        print(f"Type: {type(active)}")
        print(f"Symbol: {active.symbol}")
        print(f"\nAll fields:")
        for attr in dir(active):
            if not attr.startswith('_'):
                val = getattr(active, attr, None)
                if not callable(val):
                    print(f"  {attr}: {val}")
    else:
        print("No active contract found")

print("\n" + "="*60)
print("Option chain fields (if available):")
print("="*60)
if chain.option_chains:
    opt_chain = chain.option_chains[0]
    print(f"Type: {type(opt_chain)}")
    print(f"\nAll fields:")
    for attr in dir(opt_chain):
        if not attr.startswith('_'):
            val = getattr(opt_chain, attr, None)
            if not callable(val):
                print(f"  {attr}: {val}")
