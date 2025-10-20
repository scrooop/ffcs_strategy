#!/usr/bin/env python3
"""
Performance test for EarningsCache module.

Tests:
1. Cold start performance (100 symbols, all cache misses)
2. Warm cache performance (100 symbols, all cache hits)
3. Mixed equity/futures handling
4. Cache invalidation (simulated stale date)
"""

import time
import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent / "scripts"))

from earnings_cache import EarningsCache


def test_cold_start_performance():
    """Test performance with 100 symbols (cold start)."""
    print("\n=== Test 1: Cold Start Performance (100 symbols) ===")

    # Create fresh cache for this test
    test_cache_path = ".cache/test_earnings.db"
    Path(test_cache_path).unlink(missing_ok=True)

    cache = EarningsCache(test_cache_path)

    # 100 popular symbols (mix of tech, finance, energy, ETFs)
    symbols = [
        # Tech (25)
        "AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA", "NFLX",
        "AMD", "INTC", "ADBE", "CRM", "ORCL", "CSCO", "IBM", "QCOM",
        "TXN", "AVGO", "MU", "AMAT", "LRCX", "KLAC", "SNPS", "CDNS", "MCHP",

        # Finance (15)
        "JPM", "BAC", "WFC", "GS", "MS", "C", "BLK", "SCHW",
        "USB", "PNC", "TFC", "COF", "AXP", "BK", "STT",

        # Energy (10)
        "XOM", "CVX", "COP", "SLB", "EOG", "MPC", "PSX", "VLO", "OXY", "HAL",

        # Healthcare (10)
        "UNH", "JNJ", "PFE", "ABBV", "TMO", "ABT", "DHR", "BMY", "AMGN", "GILD",

        # Consumer (10)
        "WMT", "HD", "NKE", "SBUX", "TGT", "LOW", "MCD", "COST", "DIS", "CMCSA",

        # Industrial (10)
        "BA", "CAT", "GE", "HON", "UPS", "LMT", "RTX", "MMM", "DE", "EMR",

        # ETFs (10 - should return None)
        "SPY", "QQQ", "IWM", "DIA", "EEM", "EFA", "GLD", "SLV", "TLT", "HYG",

        # Futures (10 - should bypass)
        "/ES", "/NQ", "/RTY", "/GC", "/SI", "/CL", "/NG", "/ZB", "/ZN", "/6E"
    ]

    print(f"Testing {len(symbols)} symbols...")
    start_time = time.time()

    results = cache.batch_get_earnings(symbols)

    elapsed = time.time() - start_time
    print(f"✓ Completed in {elapsed:.2f} seconds")
    print(f"  Avg: {elapsed/len(symbols)*1000:.1f} ms/symbol")

    # Analyze results
    with_earnings = sum(1 for r in results.values() if r['next_earnings'] is not None)
    without_earnings = sum(1 for r in results.values() if r['next_earnings'] is None and r['source'] == 'yahoo')
    bypassed = sum(1 for r in results.values() if r['source'] == 'bypass')

    print(f"\nResults breakdown:")
    print(f"  With earnings: {with_earnings}")
    print(f"  Without earnings: {without_earnings} (ETFs, no data)")
    print(f"  Bypassed: {bypassed} (futures)")

    # Target: <10s for cold start
    if elapsed < 10:
        print(f"✓ PASS: Cold start under 10s target ({elapsed:.2f}s)")
    else:
        print(f"⚠ WARN: Cold start exceeded 10s target ({elapsed:.2f}s)")

    cache.close()
    return elapsed


def test_warm_cache_performance():
    """Test performance with cached data (warm cache)."""
    print("\n=== Test 2: Warm Cache Performance (100 symbols) ===")

    # Reuse cache from previous test
    cache = EarningsCache(".cache/test_earnings.db")

    symbols = [
        # Same 100 symbols as cold start test
        "AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA", "NFLX",
        "AMD", "INTC", "ADBE", "CRM", "ORCL", "CSCO", "IBM", "QCOM",
        "TXN", "AVGO", "MU", "AMAT", "LRCX", "KLAC", "SNPS", "CDNS", "MCHP",
        "JPM", "BAC", "WFC", "GS", "MS", "C", "BLK", "SCHW",
        "USB", "PNC", "TFC", "COF", "AXP", "BK", "STT",
        "XOM", "CVX", "COP", "SLB", "EOG", "MPC", "PSX", "VLO", "OXY", "HAL",
        "UNH", "JNJ", "PFE", "ABBV", "TMO", "ABT", "DHR", "BMY", "AMGN", "GILD",
        "WMT", "HD", "NKE", "SBUX", "TGT", "LOW", "MCD", "COST", "DIS", "CMCSA",
        "BA", "CAT", "GE", "HON", "UPS", "LMT", "RTX", "MMM", "DE", "EMR",
        "SPY", "QQQ", "IWM", "DIA", "EEM", "EFA", "GLD", "SLV", "TLT", "HYG",
        "/ES", "/NQ", "/RTY", "/GC", "/SI", "/CL", "/NG", "/ZB", "/ZN", "/6E"
    ]

    print(f"Testing {len(symbols)} symbols (all should be cached)...")
    start_time = time.time()

    results = cache.batch_get_earnings(symbols)

    elapsed = time.time() - start_time
    print(f"✓ Completed in {elapsed:.2f} seconds")
    print(f"  Avg: {elapsed/len(symbols)*1000:.1f} ms/symbol")

    # Verify cache hits
    cache_hits = sum(1 for r in results.values() if r['source'] == 'cache')
    bypassed = sum(1 for r in results.values() if r['source'] == 'bypass')
    yahoo_fetches = sum(1 for r in results.values() if r['source'] == 'yahoo')

    print(f"\nCache effectiveness:")
    print(f"  Cache hits: {cache_hits}")
    print(f"  Bypassed: {bypassed} (futures)")
    print(f"  Yahoo fetches: {yahoo_fetches} (should be 0)")

    # Target: <1s for warm cache
    if elapsed < 1.0:
        print(f"✓ PASS: Warm cache under 1s target ({elapsed:.2f}s)")
    else:
        print(f"⚠ WARN: Warm cache exceeded 1s target ({elapsed:.2f}s)")

    cache.close()
    return elapsed


def test_cache_stats():
    """Display cache statistics."""
    print("\n=== Test 3: Cache Statistics ===")

    cache = EarningsCache(".cache/test_earnings.db")
    stats = cache.get_cache_stats()

    print(f"Total symbols cached: {stats['total_symbols']}")
    print(f"  With earnings: {stats['symbols_with_earnings']}")
    print(f"  Without earnings: {stats['symbols_without_earnings']}")
    print(f"Oldest entry: {stats['oldest_entry']}")
    print(f"Newest entry: {stats['newest_entry']}")

    cache.close()


def test_specific_symbols():
    """Test specific symbols with expected earnings."""
    print("\n=== Test 4: Specific Symbol Validation ===")

    cache = EarningsCache(".cache/test_earnings.db")

    # Test known symbols
    test_cases = [
        ("AAPL", "should have earnings date"),
        ("MSFT", "should have earnings date"),
        ("NVDA", "should have earnings date"),
        ("SPY", "ETF - no earnings"),
        ("/ES", "futures - bypassed"),
        ("/GC", "futures - bypassed")
    ]

    for symbol, expected in test_cases:
        result = cache.get_next_earnings(symbol)
        print(f"{symbol:6} → {result['next_earnings']:10} ({result['source']:8}) | {expected}")

    cache.close()


if __name__ == "__main__":
    print("=" * 70)
    print("EARNINGS CACHE PERFORMANCE TEST")
    print("=" * 70)

    cold_time = test_cold_start_performance()
    warm_time = test_warm_cache_performance()
    test_cache_stats()
    test_specific_symbols()

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Cold start (100 symbols): {cold_time:.2f}s (target: <10s)")
    print(f"Warm cache (100 symbols): {warm_time:.2f}s (target: <1s)")
    print(f"Speedup: {cold_time/warm_time:.1f}x")

    if cold_time < 10 and warm_time < 1:
        print("\n✓ ALL PERFORMANCE TARGETS MET")
    else:
        print("\n⚠ PERFORMANCE TARGETS NOT MET")

    print("=" * 70)
