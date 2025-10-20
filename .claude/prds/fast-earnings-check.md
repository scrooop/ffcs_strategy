---
name: fast-earnings-check
description: High-performance earnings date filtering with caching to eliminate 80%+ of scan runtime
status: backlog
created: 2025-10-19T23:23:15Z
---

# PRD: Fast Earnings Check

## Executive Summary

The FF scanner currently processes 100-1000 symbols per scan, but **every symbol incurs a 500ms TastyTrade API call** to fetch earnings dates—even symbols that will immediately be filtered out. During heavy earnings weeks (e.g., Q4), 80-90% of symbols are eliminated by the earnings filter, meaning the scanner wastes 8+ minutes processing symbols that never should have entered the pipeline.

**Solution:** Implement fast earnings pre-filtering using Yahoo Finance API (or similar fast source), file-based persistent caching, and pipeline reordering to eliminate non-qualifying symbols within seconds instead of minutes.

**Expected Impact:**
- **80-95% runtime reduction** during heavy earnings periods
- 1000-symbol scan: **8+ minutes → under 30 seconds**
- Improved user experience for daily pre-market scans
- Reduced API load on TastyTrade infrastructure

---

## Problem Statement

### Current State Pain Points

**1. Inefficient Pipeline Order:**
- Earnings filtering happens AFTER expensive TastyTrade API calls
- Symbols are fully processed (market data, Greeks, IV extraction) before being filtered out
- No early-exit mechanism for earnings conflicts

**2. Repetitive API Overhead:**
- Every scan re-fetches earnings dates for the same symbols
- No caching between runs (even for same-day rescans)
- TastyTrade API throttles requests (~500ms per symbol)

**3. Scale Impact:**
```
Current worst case (heavy earnings week):
- 1000 symbols × 500ms/symbol = 8.3 minutes
- 800 symbols filtered by earnings (80% rejection rate)
- Wasted time: 800 × 500ms = 6.6 minutes on symbols that never qualified
```

**4. User Friction:**
- Long wait times discourage frequent scanning
- No visibility into why scans are slow (earnings check vs other steps)
- Diminishing returns when scaling to larger watchlists

### Why This Matters Now

- **Earnings season approaching:** Next week has concentrated earnings (80-90% filter rate observed)
- **Strategy expansion:** Users want to scan 100-1000 symbols, not 5-10
- **Automation goals:** Slow scans prevent cron job / scheduled automation
- **Competitive edge:** Fast scans enable more frequent market monitoring

### Root Cause Analysis

1. **TastyTrade API is the bottleneck** for earnings data (500ms throttle)
2. **No caching layer** for earnings dates (re-fetch same data repeatedly)
3. **Pipeline ordering is backwards** (filter AFTER expensive operations instead of BEFORE)

---

## User Stories

### Primary Persona: Active Options Trader

**Background:**
- Scans 100-500 symbols daily pre-market
- Runs scanner 2-3 times per day to catch new opportunities
- During earnings season, 80%+ of symbols get filtered out

**User Journey (Current State):**

1. **9:00 AM:** Start pre-market scan with 300 symbols
2. **Wait 2.5 minutes** watching progress messages scroll by
3. **Frustration:** "Why is this taking so long?"
4. **9:02:30:** Results show only 40 symbols passed (260 were earnings-filtered)
5. **Insight:** "I just wasted 2+ minutes on symbols I knew had earnings"

**Pain Points:**
- Long wait times reduce scanning frequency
- Can't scan large watchlists (1000+ symbols) in reasonable time
- No way to know which symbols will be filtered before processing them
- Same earnings checks repeated for same-day rescans

**User Journey (Desired State):**

1. **9:00 AM:** Start pre-market scan with 300 symbols
2. **9:00:05 (5 seconds later):** Earnings pre-filter completes
   - Console: "260 symbols filtered by earnings conflicts (cache hit: 285, fresh fetch: 15)"
   - 40 symbols proceed to TastyTrade pipeline
3. **9:00:25 (total 25 seconds):** Full scan complete with results
4. **Delight:** "This is 6x faster than before!"

---

## Requirements

### Functional Requirements

#### FR1: Fast Earnings Data Source
**Priority:** P0 (Critical)

**Description:**
Replace TastyTrade earnings API with a fast, free alternative for primary earnings date lookup.

**Acceptance Criteria:**
- [ ] Implement earnings date fetching from Yahoo Finance (via yfinance library)
  - Use `ticker.calendar` or `ticker.get_earnings_dates()` methods
  - Extract next upcoming earnings date from returned data
- [ ] Support batch/parallel fetching (where possible) to minimize latency
- [ ] Fallback to TastyTrade API if Yahoo Finance fails or returns no data
- [ ] Handle futures symbols (futures have no earnings, skip check automatically)
- [ ] Return standardized format: `{"symbol": "AAPL", "next_earnings": "2025-11-01", "source": "yahoo"}`

**Technical Notes:**
- yfinance already a project dependency (used for futures spot prices)
- Yahoo Finance typically responds in <100ms per symbol
- No known rate limiting on Yahoo Finance public API

---

#### FR2: File-Based Persistent Cache
**Priority:** P0 (Critical)

**Description:**
Implement SQLite-based earnings date cache that persists between scanner runs.

**Acceptance Criteria:**
- [ ] Store earnings dates in SQLite database (`.cache/earnings.db` or similar)
- [ ] Cache schema includes:
  - `symbol` (TEXT, PRIMARY KEY)
  - `next_earnings_date` (TEXT, ISO format YYYY-MM-DD)
  - `last_updated` (TEXT, ISO timestamp)
  - `data_source` (TEXT, "yahoo" | "tastytrade")
- [ ] Cache invalidation logic:
  - If `next_earnings_date` is in the PAST → re-fetch from API
  - If `next_earnings_date` is in the FUTURE → use cached value (no TTL)
- [ ] Graceful cache miss handling (fetch from API, then cache result)
- [ ] Thread-safe cache operations (if future parallelization needed)

**Cache Behavior Example:**
```
Jan 1:  AAPL earnings = Feb 15 → cached
Jan 15: Re-scan AAPL → cache hit (Feb 15 still in future)
Feb 16: Re-scan AAPL → cache miss (Feb 15 in past) → fetch new date (May 10) → cache
```

**Technical Notes:**
- Use Python `sqlite3` (stdlib, no new dependencies)
- Cache file location: `.cache/earnings.db` in project root
- Create `.cache/` directory if doesn't exist

---

#### FR3: Early Earnings Pre-Filter (Pipeline Reordering)
**Priority:** P0 (Critical)

**Description:**
Move earnings filtering to the FRONT of the pipeline, immediately after ticker list input.

**Current Pipeline Order:**
1. Input: ticker list
2. Fetch market data (spot price) → TastyTrade API
3. Fetch market metrics (liquidity, earnings) → TastyTrade API
4. Filter by earnings conflicts
5. Fetch option chains → TastyTrade API
6. Fetch Greeks → TastyTrade API
7. Calculate FF, output results

**New Pipeline Order:**
1. Input: ticker list
2. **Fast earnings pre-filter** (Yahoo Finance + cache) → **< 5 seconds for 1000 symbols**
3. Remove symbols with earnings conflicts (unless `--allow-earnings`)
4. Fetch market data (spot price) → TastyTrade API (only for passing symbols)
5. Fetch market metrics (liquidity) → TastyTrade API
6. Fetch option chains → TastyTrade API
7. Fetch Greeks → TastyTrade API
8. Calculate FF, output results

**Acceptance Criteria:**
- [ ] Earnings filtering happens BEFORE any TastyTrade API calls
- [ ] Console output shows: "Earnings pre-filter: 300 symbols → 40 symbols passed (260 filtered)"
- [ ] Filtered symbols do NOT proceed to market data fetch
- [ ] Cache hit/miss statistics shown: "Cache hits: 285 | Fresh fetches: 15"
- [ ] Total earnings check time logged: "Earnings check completed in 4.2s"

**Edge Cases:**
- If `--allow-earnings` flag set → skip earnings pre-filter entirely
- If `--show-earnings-conflicts` flag set → still show filtered symbols (but don't process them)
- Futures symbols automatically pass earnings filter (futures have no earnings)

---

#### FR4: Multi-Source Fallback Strategy
**Priority:** P1 (High)

**Description:**
Implement robust fallback chain for earnings data to handle API failures.

**Fallback Order:**
1. **Cache** (if fresh) → Instant
2. **Yahoo Finance** (primary) → ~100ms
3. **TastyTrade API** (fallback) → ~500ms
4. **Graceful degradation** (warn user, skip symbol or allow through)

**Acceptance Criteria:**
- [ ] If cache miss → try Yahoo Finance
- [ ] If Yahoo Finance fails (timeout, error, no data) → try TastyTrade
- [ ] If TastyTrade fails → log warning, treat as "no earnings data" (allow symbol through with warning)
- [ ] Cache results from whichever source succeeds
- [ ] Log data source for each symbol: `iv_source` column already exists, add `earnings_source` column

**Error Handling:**
- Network timeout: 5-second timeout for Yahoo Finance
- Malformed response: Log error, fall back to next source
- Rate limiting (unlikely for Yahoo): Exponential backoff, then fallback

---

#### FR5: CLI Flag Cleanup
**Priority:** P2 (Medium)

**Description:**
Remove redundant `--skip-earnings` flag, keep only `--allow-earnings` and `--show-earnings-conflicts`.

**Current Flags (Confusing):**
- `--skip-earnings` (default behavior, redundant flag)
- `--allow-earnings` (override default)

**New Flags (Clear):**
- ~~`--skip-earnings`~~ (removed, this is default behavior)
- `--allow-earnings` (disable earnings filtering)
- `--show-earnings-conflicts` (show filtered symbols for debugging)

**Acceptance Criteria:**
- [ ] Remove `--skip-earnings` flag from argparse
- [ ] Update `scripts/README_TT.md` to reflect flag removal
- [ ] Update `CLAUDE.md` to document correct usage
- [ ] Default behavior: earnings filtering enabled (no flag needed)
- [ ] `--allow-earnings`: disables earnings filtering

**Migration:**
- Scripts using `--skip-earnings` will error with "unrecognized arguments"
- Error message should suggest: "Default behavior is to skip earnings. Remove --skip-earnings flag. Use --allow-earnings to disable filtering."

---

### Non-Functional Requirements

#### NFR1: Performance
- **Earnings pre-filter:** < 10 seconds for 1000 symbols (cache hits should be <1s)
- **Overall scan improvement:** 80-95% runtime reduction during heavy earnings weeks
- **Cache operations:** < 10ms per cache lookup
- **API timeouts:** 5-second timeout for Yahoo Finance requests

#### NFR2: Reliability
- **Cache corruption handling:** Detect and rebuild corrupted cache files
- **API failure resilience:** Fallback chain ensures no single point of failure
- **Data accuracy:** Validate earnings dates are in valid format (YYYY-MM-DD)
- **Futures handling:** Correctly identify and skip earnings check for `/SYMBOL` format

#### NFR3: Observability
- **Console logging:** Show cache hit/miss stats, time spent on earnings check
- **Data source tracking:** CSV output includes `earnings_source` column
- **Debugging mode:** `--show-earnings-conflicts` shows what would be filtered
- **Performance metrics:** Log time spent in each pipeline stage

#### NFR4: Maintainability
- **Clean code separation:** Earnings cache module separate from main scanner logic
- **Testability:** Unit tests for cache invalidation, multi-source fallback
- **Documentation:** Update all docs (README_TT.md, CLAUDE.md, SOP)
- **Error messages:** Clear, actionable error messages for common failures

---

## Success Criteria

### Quantitative Metrics

**Primary KPI: Runtime Reduction**
- Baseline: 1000 symbols in ~8 minutes (heavy earnings week)
- Target: 1000 symbols in <30 seconds (80-95% reduction)
- Measurement: Time from script start to CSV output completion

**Secondary KPIs:**
- Cache hit rate: >90% for same-day rescans
- Yahoo Finance availability: >99% uptime
- Fallback usage: <1% of requests need TastyTrade fallback
- API calls to TastyTrade: Reduced by 80-90% (only passing symbols)

### Qualitative Success

**User Experience:**
- Users report "scanner is noticeably faster"
- Daily scans become practical for 1000+ symbol watchlists
- Reduced frustration waiting for results

**Developer Experience:**
- Code is clean, well-documented, testable
- Future earnings data sources can be added easily
- Cache debugging is straightforward

---

## Constraints & Assumptions

### Technical Constraints

**C1: Dependency Management**
- Prefer stdlib over new dependencies (SQLite is stdlib)
- yfinance already a dependency (no new dependency)
- No Redis/external databases (keep it simple)

**C2: Backward Compatibility**
- Must maintain compatibility with existing CSV schema
- `--allow-earnings` and `--show-earnings-conflicts` flags preserved
- Existing cron jobs should work with minimal changes

**C3: API Limitations**
- Yahoo Finance API is unofficial, may break (need fallback)
- TastyTrade API throttling remains (~500ms/request)
- No batch earnings endpoint on TastyTrade (individual lookups only)

### Assumptions

**A1: Earnings Dates Are Stable**
- Assumption: Earnings dates rarely change once announced
- Risk: If earnings get rescheduled, cached date may be stale
- Mitigation: Recommend users double-check before placing trades

**A2: Yahoo Finance Reliability**
- Assumption: Yahoo Finance API is "reliable enough" (99%+ uptime)
- Risk: Yahoo may change API, breaking yfinance
- Mitigation: TastyTrade fallback + cache fallback

**A3: Cache Invalidation is Simple**
- Assumption: "Date in past → re-fetch" is sufficient
- Risk: Edge cases (market holidays, pre-market announcements)
- Mitigation: Document known limitations

**A4: SQLite is Sufficient**
- Assumption: Single-user, local scans (no multi-user concurrency)
- Risk: SQLite may not handle multi-process writes
- Mitigation: File locking, or use journal mode for concurrency

---

## Out of Scope

The following are explicitly NOT included in this PRD:

**OS1: Parallelization of TastyTrade API Calls**
- Reason: TastyTrade likely throttles parallel requests
- Future consideration: May revisit after fast-earnings-check is proven

**OS2: Real-Time Earnings Updates**
- Reason: Cache invalidation is date-based, not real-time
- Acceptable: Users verify earnings before trade entry

**OS3: Earnings Time-of-Day**
- Reason: Scanner only cares about DATE, not time (BMO/AMC)
- Future consideration: May add for position management (exit timing)

**OS4: Alternative Cache Backends (Redis, DynamoDB)**
- Reason: SQLite sufficient for local single-user scans
- Future consideration: If multi-user/cloud deployment needed

**OS5: Earnings Estimate Data (EPS forecasts)**
- Reason: Scanner only needs DATE, not estimates
- Out of scope: Fundamental analysis features

**OS6: Historical Earnings Data**
- Reason: Scanner only needs NEXT earnings date
- Out of scope: Backtesting historical earnings impact

---

## Dependencies

### External Dependencies

**ED1: yfinance Library**
- **Type:** Python package (already installed)
- **Purpose:** Fetch earnings dates from Yahoo Finance
- **Risk:** Yahoo Finance API changes may break yfinance
- **Mitigation:** Pin yfinance version, monitor GitHub issues

**ED2: Yahoo Finance API**
- **Type:** Public web API (unofficial)
- **Purpose:** Provide earnings calendar data
- **Risk:** No SLA, may experience downtime or breaking changes
- **Mitigation:** TastyTrade fallback, cache fallback

**ED3: TastyTrade API (Fallback)**
- **Type:** Official API (already in use)
- **Purpose:** Fallback earnings data source
- **Risk:** Throttling limits (~500ms/request)
- **Mitigation:** Only used as fallback (rare usage)

### Internal Dependencies

**ID1: SQLite (Python stdlib)**
- **Type:** Embedded database
- **Purpose:** Persistent cache storage
- **Risk:** None (stdlib, mature)

**ID2: Existing Scanner Pipeline**
- **Type:** Core scanner logic (ff_tastytrade_scanner.py)
- **Purpose:** Integration point for earnings pre-filter
- **Risk:** Requires refactoring pipeline order
- **Mitigation:** Incremental refactoring, thorough testing

---

## Implementation Notes

### Proposed Architecture

**Module Structure:**
```
scripts/
├── ff_tastytrade_scanner.py          # Main scanner (modified)
├── earnings_cache.py                 # NEW: Earnings cache module
└── README_TT.md                       # Updated docs
.cache/
└── earnings.db                        # SQLite cache file (created at runtime)
```

**earnings_cache.py API:**
```python
class EarningsCache:
    """Persistent earnings date cache with multi-source fetching."""

    def __init__(self, cache_path: str = ".cache/earnings.db"):
        """Initialize cache, create DB if doesn't exist."""

    def get_next_earnings(self, symbol: str) -> dict:
        """
        Get next earnings date for symbol.

        Returns:
            {
                "symbol": "AAPL",
                "next_earnings": "2025-11-01",  # YYYY-MM-DD or None
                "source": "cache" | "yahoo" | "tastytrade",
                "cached_at": "2025-10-19T23:23:15Z"
            }
        """

    def batch_get_earnings(self, symbols: list[str]) -> dict[str, dict]:
        """Batch fetch earnings for multiple symbols (optimized)."""

    def invalidate_symbol(self, symbol: str):
        """Force re-fetch for specific symbol."""

    def clear_cache(self):
        """Clear entire cache (for debugging)."""
```

### Integration Points

**Modified Scanner Pipeline (ff_tastytrade_scanner.py):**
```python
def main():
    # ... parse args ...

    # NEW: Early earnings pre-filter
    if not args.allow_earnings:
        cache = EarningsCache()
        earnings_data = cache.batch_get_earnings(tickers)

        # Filter out symbols with earnings conflicts
        passing_symbols = []
        filtered_symbols = []
        for symbol in tickers:
            next_earnings = earnings_data[symbol]["next_earnings"]
            if next_earnings and is_earnings_conflict(next_earnings, back_dte):
                filtered_symbols.append(symbol)
            else:
                passing_symbols.append(symbol)

        print(f"Earnings pre-filter: {len(tickers)} → {len(passing_symbols)} passed ({len(filtered_symbols)} filtered)")

        if args.show_earnings_conflicts:
            # Show filtered symbols
            for symbol in filtered_symbols:
                print(f"  {symbol}: earnings on {earnings_data[symbol]['next_earnings']}")

        tickers = passing_symbols  # Only process passing symbols

    # EXISTING: Continue with TastyTrade pipeline (only for passing symbols)
    for symbol in tickers:
        # fetch market data, Greeks, calculate FF, etc.
```

### Testing Strategy

**Unit Tests:**
- Cache invalidation logic (date in past → re-fetch)
- Multi-source fallback chain (Yahoo → TastyTrade → error)
- Futures symbol detection (skip earnings check)
- SQLite corruption recovery

**Integration Tests:**
- Full pipeline with 100 symbols (measure runtime improvement)
- Cache hit/miss scenarios
- Yahoo Finance API failure simulation (test fallback)

**Performance Tests:**
- 1000 symbols with 90% cache hit rate (target: <5s)
- 1000 symbols with 0% cache hit rate (cold start, target: <30s)

---

## Documentation Updates

### Files to Update

**1. scripts/README_TT.md**
- Add "Performance" section explaining fast earnings check
- Update CLI examples to remove `--skip-earnings` flag
- Document cache location and invalidation behavior
- Add troubleshooting section for cache issues

**2. CLAUDE.md**
- Update "Earnings Filtering (v2.0)" section to "v2.1: Fast Earnings Check"
- Document cache behavior and data sources
- Update performance expectations (runtime targets)
- Note Yahoo Finance as primary source, TastyTrade as fallback

**3. docs/forward-factor-calendar-spread-SOP.md**
- Update "Quality Filtering" section with new performance characteristics
- Note that earnings verification should still happen before trade entry

### New Documentation

**4. scripts/earnings_cache.py** (docstrings)
- Module-level docstring explaining architecture
- Class/method docstrings with examples
- Inline comments for cache invalidation logic

**5. .cache/README.md** (NEW)
- Explain cache structure
- Document manual cache clearing: `rm .cache/earnings.db`
- Note: Cache is safe to delete (will rebuild automatically)

---

## Rollout Plan

### Phase 1: Core Implementation (Week 1)
- [ ] Create `earnings_cache.py` module with SQLite backend
- [ ] Implement Yahoo Finance fetching (via yfinance)
- [ ] Implement cache invalidation logic (date in past)
- [ ] Unit tests for cache module

### Phase 2: Pipeline Integration (Week 1)
- [ ] Refactor scanner to call earnings pre-filter before TastyTrade
- [ ] Remove `--skip-earnings` flag
- [ ] Add `earnings_source` column to CSV output
- [ ] Integration tests for full pipeline

### Phase 3: Fallback & Polish (Week 2)
- [ ] Implement TastyTrade fallback for Yahoo Finance failures
- [ ] Add console logging (cache stats, timing)
- [ ] Error handling and graceful degradation
- [ ] Performance testing with 1000 symbols

### Phase 4: Documentation & Release (Week 2)
- [ ] Update README_TT.md, CLAUDE.md, SOP
- [ ] Add `.cache/README.md` with cache management guide
- [ ] Create migration guide for users with existing scripts
- [ ] Release notes with performance benchmarks

---

## Risk Assessment

### High-Risk Items

**R1: Yahoo Finance API Reliability**
- **Risk:** Yahoo may change API, breaking yfinance
- **Probability:** Medium (happens ~1x per year)
- **Impact:** High (primary data source unavailable)
- **Mitigation:** TastyTrade fallback + cache fallback, monitor yfinance GitHub issues

**R2: Cache Corruption**
- **Risk:** SQLite database becomes corrupted
- **Probability:** Low (SQLite is very stable)
- **Impact:** Medium (cache rebuild required)
- **Mitigation:** Detect corruption, auto-rebuild, document manual clearing

### Medium-Risk Items

**R3: Earnings Date Rescheduling**
- **Risk:** Cached earnings date becomes stale (company reschedules)
- **Probability:** Low (rare occurrence)
- **Impact:** Medium (user trades through earnings unknowingly)
- **Mitigation:** Document limitation, recommend users verify before trade entry

**R4: Pipeline Refactoring Bugs**
- **Risk:** Reordering pipeline introduces bugs
- **Probability:** Medium (code changes are invasive)
- **Impact:** High (scanner produces incorrect results)
- **Mitigation:** Thorough testing, backward compatibility tests

### Low-Risk Items

**R5: SQLite Concurrency Issues**
- **Risk:** Multi-process writes to SQLite cache
- **Probability:** Very Low (single-user local scans)
- **Impact:** Low (cache rebuild resolves)
- **Mitigation:** SQLite journal mode, file locking

---

## Alternatives Considered

### Alternative 1: Use Only TastyTrade API (Status Quo)
**Pros:** No changes, reliable, officially supported
**Cons:** Slow (500ms/symbol), scales poorly, causes user frustration
**Verdict:** Rejected (problem persists)

### Alternative 2: In-Memory Cache Only (No Persistence)
**Pros:** Simpler implementation, no file I/O
**Cons:** Cache lost between runs, doesn't help with same-day rescans
**Verdict:** Rejected (major use case is daily rescans)

### Alternative 3: Redis/External Cache
**Pros:** Handles concurrency, shared cache across users
**Cons:** New dependency, infrastructure overhead, overkill for local scans
**Verdict:** Rejected (SQLite sufficient for single-user)

### Alternative 4: Pre-Fetch All Earnings (Daily Cron)
**Pros:** Zero runtime overhead during scans
**Cons:** Requires cron setup, doesn't help with ad-hoc symbol lists
**Verdict:** Deferred (consider as future optimization)

### Alternative 5: Use Financial Modeling Prep API
**Pros:** Official earnings API, structured data
**Cons:** Requires API key, free tier has rate limits, new dependency
**Verdict:** Considered as fallback (after Yahoo + TastyTrade)

---

## Open Questions

**Q1: Should cache have a TTL (time-to-live) even for future dates?**
- Context: Earnings dates rarely change, but it could happen
- Proposed answer: No TTL, only invalidate when date passes
- Reason: Simplicity, user can manually clear cache if needed

**Q2: Should we support manual cache warming?**
- Context: User could pre-populate cache with watchlist before scan
- Proposed answer: Defer to future enhancement
- Reason: Auto-fetching is fast enough (<10s for 1000 symbols)

**Q3: How to handle symbols with no earnings (private companies, ETFs)?**
- Context: Some symbols won't have earnings data in any API
- Proposed answer: Treat as "no earnings conflict" (allow through)
- Reason: Safer to include than exclude unknowns

**Q4: Should cache be per-user or shared?**
- Context: Multi-user setups (unlikely for current use case)
- Proposed answer: Per-user (local file in project directory)
- Reason: Simplicity, no concurrency concerns

---

## Appendix: Performance Benchmarks (Projected)

### Current State (Baseline)

| Symbols | Earnings Filter Rate | Total Runtime | Wasted Time on Filtered Symbols |
|---------|---------------------|---------------|----------------------------------|
| 100     | 80%                 | 50s           | 40s (80 symbols × 500ms)         |
| 500     | 80%                 | 4m 10s        | 3m 20s (400 symbols × 500ms)     |
| 1000    | 80%                 | 8m 20s        | 6m 40s (800 symbols × 500ms)     |

### Projected State (After Implementation)

| Symbols | Cache Hit Rate | Earnings Check Time | Total Runtime | Improvement |
|---------|----------------|---------------------|---------------|-------------|
| 100     | 90%            | 2s                  | 12s           | 76% faster  |
| 500     | 90%            | 8s                  | 58s           | 77% faster  |
| 1000    | 90%            | 15s                 | 1m 55s        | 77% faster  |

**Key Assumptions:**
- Yahoo Finance: ~100ms per symbol (fresh fetch)
- Cache lookup: ~1ms per symbol
- 80% of symbols filtered by earnings (heavy earnings week)
- Only 20% of symbols proceed to TastyTrade pipeline

---

## Version History

| Version | Date       | Author | Changes |
|---------|------------|--------|---------|
| 1.0     | 2025-10-19 | AI     | Initial PRD creation based on user requirements |

---

**Status:** Backlog (Ready for Epic Parsing)

**Next Steps:**
1. Review PRD with stakeholders
2. Validate performance assumptions with small-scale prototype
3. Run `/pm:prd-parse fast-earnings-check` to create implementation epic
