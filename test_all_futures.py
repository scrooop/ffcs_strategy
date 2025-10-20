#!/usr/bin/env python3
"""Test all futures symbols to document which have working option chains."""
import subprocess
import sys

futures = [
    '/ES', '/NQ', '/RTY', '/GC', '/SI', '/CL', '/NG',
    '/ZB', '/ZN', '/ZF', '/ZT', '/ZC', '/ZS', '/ZW',
    '/HG', '/HE', '/LE',
    '/6A', '/6B', '/6C', '/6E', '/6J',
    '/MES', '/MNQ', '/MCL', '/BTC', '/ETH', '/SR3'
]

print("Symbol,Status,Details")
print("-" * 60)

for sym in futures:
    cmd = [
        'python', 'scripts/ff_tastytrade_scanner.py',
        '--tickers', sym,
        '--pairs', '30-60',
        '--min-ff', '0.01',
        '--skip-liquidity-check',
        '--show-all-scans'
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout + result.stderr

    if output.startswith('2025') or '\n2025' in output:
        print(f"{sym},✅ WORKS,Has option chain and produces results")
    elif 'No option chain' in output:
        print(f"{sym},❌ NO CHAIN,No option chain available on tastytrade")
    elif 'No expirations matched tolerance' in output:
        print(f"{sym},⚠️  NO MATCH,Chain exists but no 30-60 DTE expirations")
    elif 'No quote available' in output:
        print(f"{sym},❌ NO PRICE,Cannot get spot price from Yahoo Finance")
    else:
        # Extract first warning
        for line in output.split('\n'):
            if '[WARN]' in line or '[INFO]' in line:
                print(f"{sym},❓ OTHER,{line[:60]}")
                break
        else:
            print(f"{sym},❓ UNKNOWN,No clear status")
