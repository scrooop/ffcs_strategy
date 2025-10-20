---
issue: 16
created: 2025-10-20T00:42:00Z
status: ready
---

# Analysis: Integrate earnings pre-filter into scanner pipeline

## Overview
Integrate the `EarningsCache` module into the main scanner (`ff_tastytrade_scanner.py`) to filter symbols by earnings conflicts BEFORE any TastyTrade API calls. This is the core performance optimization that eliminates 80%+ of symbols in under 10 seconds during heavy earnings weeks.

## Work Stream (Single-threaded, Sequential)

### Integration Implementation (4-6 hours)
**Scope:** Modify main() function to add earnings pre-filter
**Owner:** general-purpose agent

**Implementation details:**

1. **Import EarningsCache:**
   ```python
   from earnings_cache import EarningsCache
   ```

2. **Add pre-filter logic in main() (BEFORE fetch_market_metrics):**
   ```python
   if not args.allow_earnings:
       import time
       start_time = time.time()

       # Initialize cache
       cache = EarningsCache()

       # Batch fetch earnings
       earnings_data = cache.batch_get_earnings(tickers)

       # Filter symbols
       passing_symbols = []
       filtered_symbols = []

       for symbol in tickers:
           # Determine back expiry from DTE pairs
           back_dte = max(pair[1] for pair in dte_pairs)
           back_expiry = ny_today() + timedelta(days=back_dte)

           # Check earnings conflict
           next_earnings = earnings_data[symbol]["next_earnings"]
           if next_earnings:
               earnings_date = date.fromisoformat(next_earnings)
               if ny_today() <= earnings_date <= back_expiry:
                   reason = f"Earnings on {next_earnings} conflicts with back expiry {back_expiry}"
                   filtered_symbols.append((symbol, reason))
                   continue

           passing_symbols.append(symbol)

       # Console logging
       elapsed = time.time() - start_time
       cache_hits = sum(1 for d in earnings_data.values() if d['source'] == 'cache')
       fresh_fetches = len(earnings_data) - cache_hits

       print(f"Earnings pre-filter: {len(tickers)} → {len(passing_symbols)} passed ({len(filtered_symbols)} filtered)")
       print(f"  Cache hits: {cache_hits} | Fresh fetches: {fresh_fetches}")
       print(f"  Earnings check completed in {elapsed:.1f}s")

       if args.show_earnings_conflicts:
           for symbol, reason in filtered_symbols:
               print(f"  {symbol}: {reason}")

       # Only process passing symbols
       tickers = passing_symbols

   # EXISTING: Continue with TastyTrade pipeline (unchanged)
   market_metrics = fetch_market_metrics(session, tickers)
   ```

3. **Key integration points:**
   - Add AFTER argparse and session authentication
   - Add BEFORE fetch_market_metrics() call
   - Reuse existing `ny_today()` function for date calculations
   - Calculate back_expiry from DTE pairs (use max back DTE)
   - Preserve existing `--allow-earnings` and `--show-earnings-conflicts` flags

**Files to modify:**
- `scripts/ff_tastytrade_scanner.py` (main() function)

**Key considerations:**
- Don't modify existing TastyTrade pipeline (only add pre-filter)
- Futures symbols automatically pass (earnings_data returns None for futures)
- Maintain backward compatibility (same filtering logic as v2.0)
- Console output should be informative (cache stats, timing, filtered symbols)

**Testing approach:**
- Manual: Run with 10 symbols, verify pre-filter works
- Manual: Run with --allow-earnings, verify pre-filter skipped
- Manual: Run with --show-earnings-conflicts, verify filtered symbols shown
- Performance: 100 symbols, verify earnings check <5s
- Backward compatibility: Same results as v2.0 (just faster)

## Dependencies
- ✅ Task #15 completed (EarningsCache module exists)
- ✅ Existing scanner functions: `ny_today()`, `fetch_market_metrics()`

## Success Criteria
- [ ] EarningsCache imported and instantiated in main()
- [ ] Earnings pre-filter runs BEFORE fetch_market_metrics()
- [ ] Console output shows cache stats and timing
- [ ] --allow-earnings flag bypasses pre-filter
- [ ] --show-earnings-conflicts flag shows filtered symbols
- [ ] Manual testing: 100 symbols in <5s (earnings check only)
- [ ] Backward compatibility: Same filtering results as v2.0

## Risks & Mitigations
**Risk:** Integration breaks existing scanner functionality
- Mitigation: Add pre-filter as isolated block, minimal changes to existing code
- Mitigation: Test with known symbol lists to verify same results

**Risk:** Performance doesn't meet targets
- Mitigation: Cache should handle 100 symbols in <5s (verified in Task #15)
- Mitigation: Add timing instrumentation to identify bottlenecks

**Risk:** Edge cases not handled (empty list, all filtered, etc.)
- Mitigation: Test edge cases explicitly
- Mitigation: Graceful degradation on errors

## Notes
- This is a small, focused change (add pre-filter block to main())
- TastyTrade pipeline remains unchanged (receives filtered ticker list)
- No CSV changes yet (Task #18)
- No CLI flag changes yet (Task #19)
- Focus on functional integration only
