---
name: fast-earnings-check
status: completed
created: 2025-10-19T23:52:40Z
updated: 2025-10-20T01:32:35Z
completed: 2025-10-20T01:32:35Z
progress: 100%
prd: .claude/prds/fast-earnings-check.md
github: https://github.com/scrooop/ffcs_strategy/issues/14
---

# Epic: Fast Earnings Check

## Overview

Replace slow TastyTrade earnings API calls with fast Yahoo Finance lookups + SQLite caching to achieve **80-95% runtime reduction** during heavy earnings weeks. The core optimization is **pipeline reordering**: filter symbols by earnings conflicts BEFORE expensive TastyTrade API processing, eliminating 80%+ of symbols in under 10 seconds.

**Current bottleneck:** Every symbol makes a ~500ms TastyTrade API call for earnings data, even symbols immediately filtered out.
**Solution:** Yahoo Finance (~100ms) + SQLite cache (instant) + move earnings filter to FRONT of pipeline.

**Impact:** 1000-symbol scan: 8+ minutes → <30 seconds

## Architecture Decisions

### AD1: Yahoo Finance as Primary Source
**Decision:** Use Yahoo Finance (via existing yfinance dependency) as primary earnings data source, with TastyTrade as fallback.

**Rationale:**
- yfinance already installed (used for futures spot prices)
- No API key required, no rate limiting
- Fast response (~100ms vs 500ms TastyTrade)
- Ticker.calendar or get_earnings_dates() methods provide next earnings date

**Tradeoffs:**
- Unofficial API (may break if Yahoo changes)
- Mitigation: TastyTrade fallback + cache fallback ensures reliability

### AD2: SQLite for Persistent Cache
**Decision:** Use Python stdlib sqlite3 for earnings date cache (`.cache/earnings.db`).

**Rationale:**
- No new dependencies (stdlib)
- Simple file-based persistence (survives restarts)
- Fast lookups (<10ms per symbol)
- Sufficient for single-user local scans

**Alternatives rejected:**
- In-memory only: Loses cache between runs (defeats purpose for same-day rescans)
- Redis: Overkill, requires external service, adds complexity
- JSON file: Slower than SQLite, no ACID guarantees

### AD3: Simple Cache Invalidation
**Decision:** Re-fetch earnings date only when cached date has passed (date < today).

**Rationale:**
- Earnings dates rarely change once announced
- Simple logic: if `next_earnings_date` in past → fetch new upcoming date
- No TTL needed (eliminates configuration complexity)

**Risks accepted:**
- If earnings rescheduled, cache may be stale until manual clear
- Mitigation: Document limitation, recommend users verify before trade entry

### AD4: Leverage Existing Functions
**Decision:** Reuse existing `check_earnings_conflict()` and `fetch_market_metrics()` functions with minimal changes.

**Rationale:**
- Scanner already has earnings conflict logic (just needs earlier execution)
- `check_earnings_conflict()` interface unchanged (accepts metrics dict)
- Only `fetch_market_metrics()` needs TastyTrade fallback integration

**Simplification:**
- Don't rebuild earnings logic from scratch
- Cache layer sits BEFORE existing functions, minimal invasive changes

## Technical Approach

### Backend Components

#### 1. Earnings Cache Module (`scripts/earnings_cache.py`)
**New standalone module** with clean API:

```python
class EarningsCache:
    """Persistent earnings date cache with multi-source fetching."""

    def __init__(self, cache_path: str = ".cache/earnings.db")
    def get_next_earnings(self, symbol: str) -> dict
    def batch_get_earnings(self, symbols: list[str]) -> dict[str, dict]
    def _fetch_from_yahoo(self, symbol: str) -> Optional[date]
    def _fetch_from_tastytrade(self, session: Session, symbol: str) -> Optional[date]
```

**Key methods:**
- `batch_get_earnings()`: Main entry point, returns earnings for all symbols
- `_fetch_from_yahoo()`: Yahoo Finance via yfinance (ticker.calendar)
- `_fetch_from_tastytrade()`: Fallback to existing fetch_market_metrics()
- Cache invalidation: Check if `next_earnings_date < today()` → re-fetch

**Database schema:**
```sql
CREATE TABLE earnings (
    symbol TEXT PRIMARY KEY,
    next_earnings_date TEXT,  -- YYYY-MM-DD format
    last_updated TEXT,         -- ISO timestamp
    data_source TEXT           -- 'yahoo' | 'tastytrade'
)
```

#### 2. Scanner Pipeline Integration (`scripts/ff_tastytrade_scanner.py`)
**Minimal changes to main():**

```python
def main():
    # ... parse args, authenticate session ...

    # NEW: Early earnings pre-filter (if earnings filtering enabled)
    if not args.allow_earnings:
        cache = EarningsCache()
        earnings_data = cache.batch_get_earnings(tickers)

        # Filter symbols using EXISTING check_earnings_conflict() function
        passing_symbols = []
        filtered_symbols = []
        for symbol in tickers:
            passes, reason = check_earnings_conflict_from_cache(
                symbol, earnings_data, back_dte
            )
            if passes:
                passing_symbols.append(symbol)
            else:
                filtered_symbols.append((symbol, reason))

        # Show results
        print(f"Earnings pre-filter: {len(tickers)} → {len(passing_symbols)} passed")

        if args.show_earnings_conflicts:
            for sym, reason in filtered_symbols:
                print(f"  {sym}: {reason}")

        tickers = passing_symbols  # Only process passing symbols

    # EXISTING: Continue with TastyTrade pipeline (unchanged)
    market_metrics = fetch_market_metrics(session, tickers)  # Now only for passing symbols
    # ... rest of pipeline unchanged ...
```

**New helper function:**
```python
def check_earnings_conflict_from_cache(
    symbol: str,
    earnings_data: dict,
    back_dte: int
) -> Tuple[bool, Optional[str]]:
    """Wrapper around existing check_earnings_conflict() for cache data."""
    # Convert cache format to metrics format, call existing function
```

#### 3. CSV Output Enhancement
**Add earnings_source column** to 28-column schema:

Current columns include `earnings_conflict`, `earnings_date` → Add `earnings_source`
- Values: "cache" | "yahoo" | "tastytrade"
- Tracks where earnings data came from (for debugging/auditing)

### Infrastructure

#### Deployment Considerations
- No infrastructure changes (local script, SQLite file)
- Cache file location: `.cache/earnings.db` in project root
- Auto-create `.cache/` directory if doesn't exist
- Cache is safe to delete manually (`rm .cache/earnings.db`)

#### Monitoring and Observability
**Console output additions:**
```
Earnings pre-filter: 300 symbols → 40 passed (260 filtered)
  Cache hits: 285 | Fresh fetches: 15 | Yahoo: 12 | TastyTrade fallback: 3
  Earnings check completed in 4.2s
```

**CSV tracking:**
- Add `earnings_source` column to track data provenance
- Existing `earnings_conflict` and `earnings_date` columns unchanged

## Implementation Strategy

### Development Phases

**Phase 1: Core Cache Implementation (Minimal Viable Product)**
- Create `earnings_cache.py` with SQLite backend
- Implement Yahoo Finance fetching only (no TastyTrade fallback yet)
- Simple cache invalidation (date in past → re-fetch)
- Unit tests for cache CRUD operations

**Phase 2: Scanner Integration**
- Add earnings pre-filter to main() BEFORE TastyTrade calls
- Integrate EarningsCache.batch_get_earnings()
- Add console logging (cache stats, timing)
- Test with 100-symbol scan (measure improvement)

**Phase 3: Fallback & Polish**
- Add TastyTrade fallback for Yahoo Finance failures
- Add `earnings_source` column to CSV output
- Error handling and graceful degradation
- Remove `--skip-earnings` flag (breaking change)

**Phase 4: Documentation & Validation**
- Update README_TT.md, CLAUDE.md
- Create `.cache/README.md` (cache management guide)
- Performance benchmark with 1000 symbols
- Integration tests for edge cases

### Risk Mitigation

**R1: Yahoo Finance API Changes**
- Risk: yfinance breaks if Yahoo changes API
- Mitigation: TastyTrade fallback ensures functionality
- Monitoring: Check yfinance GitHub issues regularly

**R2: Pipeline Refactoring Bugs**
- Risk: Moving earnings filter breaks existing logic
- Mitigation: Reuse existing `check_earnings_conflict()` function (minimal changes)
- Testing: Backward compatibility tests (verify same results as v2.0)

**R3: Cache Corruption**
- Risk: SQLite database becomes corrupted
- Mitigation: Auto-rebuild on corruption detection, document manual clearing

### Testing Approach

**Unit Tests (scripts/test_earnings_cache.py):**
- Cache invalidation (date in past → re-fetch)
- Yahoo Finance fetching (mock API responses)
- TastyTrade fallback (simulate Yahoo failure)
- Futures symbol handling (skip earnings check)

**Integration Tests:**
- Full pipeline with 100 symbols (measure runtime)
- Cache hit/miss scenarios (first run vs second run)
- Yahoo Finance failure simulation (verify fallback)

**Performance Tests:**
- 1000 symbols, 90% cache hit rate → Target: <5s earnings check
- 1000 symbols, 0% cache hit rate (cold start) → Target: <30s earnings check

**Backward Compatibility Tests:**
- Verify same filtering results as v2.0 (using TastyTrade)
- Verify CSV schema compatible with existing analysis tools

## Task Breakdown Preview

High-level task categories (aim for <10 tasks):

- [ ] **Task 1:** Create earnings_cache.py module with SQLite backend and Yahoo Finance integration
  - SQLite schema, cache CRUD operations, Yahoo Finance fetching via yfinance
  - Deliverable: Working cache module with unit tests

- [ ] **Task 2:** Integrate earnings pre-filter into scanner pipeline
  - Add EarningsCache call before TastyTrade processing in main()
  - Filter symbols early, reuse existing check_earnings_conflict() logic
  - Deliverable: Scanner filters earnings upfront, console shows cache stats

- [ ] **Task 3:** Implement TastyTrade fallback for Yahoo Finance failures
  - Add fallback chain: Cache → Yahoo → TastyTrade → graceful degradation
  - Error handling, timeout logic, logging
  - Deliverable: Robust multi-source earnings fetching

- [ ] **Task 4:** Add earnings_source column to CSV output
  - Extend CSV schema from 28 to 29 columns
  - Track data provenance ("cache" | "yahoo" | "tastytrade")
  - Deliverable: CSV includes earnings source tracking

- [ ] **Task 5:** Remove --skip-earnings flag (breaking change)
  - Clean up argparse, update default behavior
  - Add migration error message for users still using old flag
  - Deliverable: Cleaner CLI with only --allow-earnings flag

- [ ] **Task 6:** Update documentation (README_TT.md, CLAUDE.md)
  - Document new cache behavior, performance improvements
  - Add cache management guide (.cache/README.md)
  - Update usage examples, troubleshooting section
  - Deliverable: Complete documentation for v2.1 feature

- [ ] **Task 7:** Performance benchmarking and validation
  - Benchmark 1000-symbol scans (cache hit vs cold start)
  - Verify 80-95% runtime reduction target
  - Integration tests for edge cases
  - Deliverable: Performance report validating PRD targets

## Dependencies

### External Dependencies
- **yfinance:** Already installed (used for futures spot prices)
- **Yahoo Finance API:** Unofficial public API (no SLA)
- **TastyTrade API:** Already in use (fallback only)

### Internal Dependencies
- **Existing scanner functions:** Reuse `check_earnings_conflict()`, `fetch_market_metrics()`
- **CSV schema:** Extend by 1 column (backward compatible for readers)

### Prerequisite Work
- None (all dependencies already met)

## Success Criteria (Technical)

### Performance Benchmarks
**Primary KPI:**
- 1000-symbol scan runtime: 8+ minutes → <30 seconds (80-95% reduction)

**Component-level targets:**
- Earnings pre-filter: <10s for 1000 symbols (cache hits <1s)
- Yahoo Finance fetch: ~100ms per symbol
- SQLite cache lookup: <10ms per symbol

### Quality Gates
- **Unit test coverage:** >80% for earnings_cache.py
- **Integration tests:** Pass all backward compatibility tests
- **Performance tests:** Meet runtime targets (see above)
- **Documentation:** All 3 docs updated (README_TT.md, CLAUDE.md, .cache/README.md)

### Acceptance Criteria
From PRD functional requirements (FR1-FR5):
- [x] Yahoo Finance as primary earnings source
- [x] SQLite persistent cache with date-based invalidation
- [x] Earnings filtering BEFORE TastyTrade API calls
- [x] Multi-source fallback (Cache → Yahoo → TastyTrade)
- [x] Remove --skip-earnings flag

## Estimated Effort

### Overall Timeline
**2 weeks** (matches PRD rollout plan)

**Week 1:**
- Days 1-2: Task 1 (earnings_cache.py module)
- Days 3-4: Task 2 (pipeline integration)
- Day 5: Task 3 (TastyTrade fallback)

**Week 2:**
- Day 1: Task 4 (CSV output)
- Day 2: Task 5 (CLI cleanup)
- Days 3-4: Task 6 (documentation)
- Day 5: Task 7 (benchmarking & validation)

### Resource Requirements
- **1 developer** (full-time for 2 weeks)
- **Testing infrastructure:** Existing (local Python environment)
- **No external resources needed** (SQLite, yfinance already available)

### Critical Path Items
1. **earnings_cache.py module** (Task 1) → Blocks all other tasks
2. **Pipeline integration** (Task 2) → Unblocks performance testing
3. **Performance validation** (Task 7) → Final gate before release

**Risk:** If Yahoo Finance proves unreliable in testing, may need to research alternative free APIs (adds 2-3 days).

## Simplification Opportunities

### Leverage Existing Code (Key Insight)
**Major simplification:** The scanner ALREADY has all earnings conflict logic in `check_earnings_conflict()` and `fetch_market_metrics()`. We're NOT rebuilding earnings detection from scratch.

**What changes:**
1. Add cache layer (new module: earnings_cache.py)
2. Move earnings filter earlier in main() (10 lines of code)
3. Add Yahoo Finance as primary source (reuse yfinance)

**What stays the same:**
- `check_earnings_conflict()` function (reuse as-is)
- Earnings conflict detection logic (unchanged)
- CSV output schema (just add 1 column)

### Minimal Invasive Changes
**Pipeline integration is 95% additive:**
```python
# NEW CODE (added before existing pipeline)
if not args.allow_earnings:
    cache = EarningsCache()
    earnings_data = cache.batch_get_earnings(tickers)
    tickers = [s for s in tickers if passes_filter(s, earnings_data)]

# EXISTING CODE (runs on filtered tickers, unchanged)
market_metrics = fetch_market_metrics(session, tickers)
# ... rest of pipeline ...
```

**Benefits:**
- Low risk of breaking existing functionality
- Easy to rollback (remove pre-filter block)
- Backward compatible CSV output (readers ignore new column)

### Single-File Cache Module
**Avoid over-engineering:**
- 1 Python file (earnings_cache.py), ~200 lines
- No separate config files, no complex class hierarchies
- Simple API: `batch_get_earnings(symbols) → dict`

**Contrast with PRD's complex architecture proposal:**
- PRD suggested separate fetcher classes, factory patterns
- Simplified epic: Single EarningsCache class with private methods
- Result: Same functionality, 50% less code

## Tasks Created

- [ ] #15 - Create earnings_cache.py module with SQLite backend and Yahoo Finance integration (parallel: true)
- [ ] #16 - Integrate earnings pre-filter into scanner pipeline (parallel: false)
- [ ] #17 - Implement TastyTrade fallback for Yahoo Finance failures (parallel: false)
- [ ] #18 - Add earnings_source column to CSV output (parallel: true)
- [ ] #19 - Remove --skip-earnings flag (breaking change) (parallel: true)
- [ ] #20 - Update documentation (README_TT.md, CLAUDE.md) (parallel: true)
- [ ] #21 - Performance benchmarking and validation (parallel: true)

Total tasks: 7
Parallel tasks: 4
Sequential tasks: 3
Estimated total effort: 29-43 hours

**Dependency graph:**
```
#15 (Cache module) ─┬─→ #16 (Scanner integration) ─→ #17 (TastyTrade fallback)
                    │                                  ↓
                    └──────────────────────────────→ #18 (CSV output)
                                                       ↓
                    #16,#17,#18,#19 ───────────────→ #20 (Documentation)
                    #15,#16,#17,#18,#19 ──────────→ #21 (Benchmarking)

#19 (CLI cleanup) can run in parallel with #18 (conflicts on same file)
```

## Notes

**Version increment:** This will be v2.1 of the scanner (documented in CLAUDE.md).

**Breaking changes:** Removal of `--skip-earnings` flag requires user migration (error message guides users).

**Future enhancements (out of scope):**
- Parallel Yahoo Finance fetching (if single-threaded proves too slow)
- Alternative earnings APIs (Financial Modeling Prep, Finnhub)
- Cache warming (pre-populate before scan)
- TTL-based cache invalidation (vs date-only)
