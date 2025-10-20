# Issue #32 Analysis: Implement Volume-Based Liquidity Filter

## Overview
Replace `liquidity_rating` (opaque 0-5 scale) with volume-based filter using 20-day average options volume from Market Metrics API. Enforce strategy's "≥10k avg options volume/day" rule.

## Work Streams

### Stream A: Extend fetch_market_metrics() Function
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Add volume extraction to existing `fetch_market_metrics()` function
- Extract `avg_options_volume_20d` field from API response (verify field name)
- Store in market_metrics dict: `{symbol: {'earnings': ..., 'avg_volume': value}}`
- Handle missing field: Use fallback logic (daily_volume * 20) or None
- Batch fetch with existing earnings data (single API call per symbol)
- Handle futures: May not have volume field, allow through if missing

**Estimated Time:** 1.5 hours

### Stream B: Implement Volume Filter
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Add volume check in pre-filter section (before Greeks fetching)
- Filter condition: `avg_volume < args.min_avg_volume`
- Use skip_reason: "volume_too_low"
- Track in skip_stats dictionary
- Skip Greeks API call if filtered (performance optimization)
- Respect `--skip-liquidity-check` flag (disable filter)

**Estimated Time:** 1 hour

### Stream C: Add CLI Flag
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Add `--min-avg-volume` flag (default: 10000)
- Type: int, help text explaining 20-day avg volume
- Keep `--skip-liquidity-check` flag (reuse for volume filter)
- Remove `--min-liquidity-rating` flag (obsolete)
- Update help text to clarify volume-based filtering

**Estimated Time:** 30 minutes

### Stream D: Remove liquidity_rating References
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Search for all `liquidity_rating` references
- Remove from:
  - CSV header row
  - CSV row construction
  - Variable assignments
  - fetch_market_metrics() return values
- Verify no breakage from removal
- Clean up comments mentioning rating scale

**Estimated Time:** 45 minutes

### Stream E: Update CSV Schema
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Remove columns: `liquidity_rating`, `liquidity_value`
- Add column: `avg_options_volume_20d`
- Update CSV header row
- Update row construction with volume value
- Verify column order matches documentation
- Update column count in comments

**Estimated Time:** 30 minutes

### Stream F: Documentation Updates
**File Pattern:** `CLAUDE.md`, `scripts/README_TT.md`
**Work:**
- Update CLAUDE.md CSV schema section
- Remove liquidity_rating references
- Add avg_options_volume_20d column documentation
- Update column count (31 → new count)
- Update CLI examples (remove --min-liquidity-rating, add --min-avg-volume)
- Document futures handling (may not have volume field)

**Estimated Time:** 1 hour

### Stream G: Testing
**File Pattern:** Manual testing, unit tests
**Work:**
- Test volume filter with various thresholds
- Test --min-avg-volume flag
- Test --skip-liquidity-check bypass
- Test futures symbols (handle missing volume field)
- Test API field missing (fallback logic)
- Verify skip_stats tracking
- Check CSV output includes avg_options_volume_20d

**Estimated Time:** 1 hour

## Execution Strategy

**Sequential execution within single agent** - API changes first, then filter logic:
1. Extend fetch_market_metrics() (Stream A)
2. Implement volume filter (Stream B)
3. Add CLI flag (Stream C)
4. Remove liquidity_rating references (Stream D)
5. Update CSV schema (Stream E)
6. Update documentation (Stream F)
7. Testing (Stream G)

## File Locations

- **Main file:** `scripts/ff_tastytrade_scanner.py`
  - fetch_market_metrics(): ~lines 400-500
  - Pre-filter section: scan loop before Greeks fetching
  - CLI flags: argparse section
- **Docs:** `CLAUDE.md`, `scripts/README_TT.md`

## Success Criteria

- Volume extraction working in fetch_market_metrics()
- Filter logic functioning with threshold check
- --min-avg-volume CLI flag added and tested
- liquidity_rating fully removed from codebase
- avg_options_volume_20d column in CSV
- Batch fetching verified (no performance regression)
- Fallback documented if API field missing
- Edge cases tested: field missing, zero volume, futures

## Dependencies

- Depends on #25 (skip tracking for "volume_too_low") ✅ COMPLETE
- **Independent of:** #26, #28, #29 (different filtering logic)
- **Parallel with:** #26, #28, #29

## Coordination Notes

- **Conflicts with:** #24 (CSV schema) - coordinate column removal/addition
- Safe to parallelize with #26, #28, #29
- Leverage existing batch fetch infrastructure
- Pre-filter optimization saves API calls

## Key Implementation Details

**API Field Verification:**
```python
# Market Metrics API response (verify actual field name)
# Expected fields:
# - avg_options_volume_20d (primary)
# - daily_volume (fallback: daily_volume * 20)
# - futures may not have volume field

# Reference: docs/tastytrade_official_API_docs_full_spec.json
```

**fetch_market_metrics() Extension:**
```python
def fetch_market_metrics(session, symbols):
    """Batch fetch earnings dates and avg options volume"""
    metrics = {}
    for symbol in symbols:
        data = session.get_market_metrics(symbol)

        # Extract earnings (already implemented)
        earnings_date = data.get('earnings_date')

        # Extract volume (NEW)
        avg_volume = data.get('avg_options_volume_20d')
        if avg_volume is None:
            # Fallback: daily_volume * 20 approximation
            daily = data.get('daily_volume')
            avg_volume = daily * 20 if daily else None

        metrics[symbol] = {
            'earnings': earnings_date,
            'avg_volume': avg_volume
        }
    return metrics
```

**Volume Filter Logic:**
```python
# Pre-filter section (before Greeks fetching)
market_data = fetch_market_metrics(session, symbols)

for symbol in symbols:
    avg_volume = market_data[symbol]['avg_volume']

    # Skip futures if volume field missing (not an error)
    if symbol.startswith('/') and avg_volume is None:
        logger.debug(f"{symbol}: Futures, volume filter skipped")
        continue

    # Apply volume filter (unless --skip-liquidity-check)
    if not args.skip_liquidity_check:
        if avg_volume is None or avg_volume < args.min_avg_volume:
            logger.debug(f"{symbol}: Filtered (avg volume {avg_volume} < {args.min_avg_volume})")
            skip_stats['volume_too_low'] += 1
            continue

    # Proceed to Greeks fetching (expensive API call)
    ...
```

**CLI Flag:**
```python
parser.add_argument(
    '--min-avg-volume',
    type=int,
    default=10000,
    help='Minimum 20-day average options volume (default: 10000 contracts/day)'
)

# REMOVE this flag:
# parser.add_argument('--min-liquidity-rating', ...)
```

**CSV Schema Change:**
```python
# BEFORE (v2.1):
# liquidity_rating, liquidity_value (2 columns)

# AFTER (v2.2):
# avg_options_volume_20d (1 column)

# Net change: -1 column (31 → 30)
```

**Futures Handling:**
```python
# Futures (e.g., /ES, /NQ) may not have avg_options_volume_20d
# If symbol.startswith('/') and avg_volume is None:
#     Allow through (don't filter)
#     Document this behavior
```

**Performance Optimization:**
```python
# Volume filter runs BEFORE Greeks fetching
# Saves expensive dxFeed API calls for low-volume symbols
# Batch fetch volume data (already batched with earnings)
# No per-symbol API overhead
```

## Testing

- Test volume extraction from API
- Test filter with thresholds: 5000, 10000, 20000
- Test --skip-liquidity-check bypass
- Test futures symbols (/ES, /NQ) handle missing volume
- Test API field missing (fallback logic)
- Verify skip_stats["volume_too_low"] tracking
- Check CSV output includes avg_options_volume_20d column
- Integration: Run full scan and verify filtering works
