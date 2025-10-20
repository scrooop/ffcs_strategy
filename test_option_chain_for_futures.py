#!/usr/bin/env python3
"""
Test using NestedOptionChain for futures symbols and see if we can infer spot price.
"""
import os
from tastytrade import Session
from tastytrade.instruments import NestedOptionChain

# Authenticate
username = os.getenv("TT_USERNAME")
password = os.getenv("TT_PASSWORD")
session = Session(username, password=password, is_test=False)

# Get option chain using NestedOptionChain (not NestedFutureOptionChain)
chains = NestedOptionChain.get(session, "/ES")

print("="*60)
print("NestedOptionChain for /ES:")
print("="*60)
print(f"Type: {type(chains)}")
print(f"Number of chains: {len(chains)}")
print()

if chains:
    chain = chains[0]
    print(f"First chain type: {type(chain)}")

    # Check for underlying_price or similar fields
    for attr in dir(chain):
        if not attr.startswith('_') and not callable(getattr(chain, attr, None)):
            val = getattr(chain, attr, None)
            if not isinstance(val, list):  # Skip long lists
                print(f"{attr}: {val}")

    # Also check the first expiration if available
    if chain.expirations:
        print("\n" + "="*60)
        print("First expiration details:")
        print("="*60)
        exp = chain.expirations[0]
        for attr in dir(exp):
            if not attr.startswith('_') and not callable(getattr(exp, attr, None)):
                val = getattr(exp, attr, None)
                if not isinstance(val, list):  # Skip strikes list
                    print(f"{attr}: {val}")
