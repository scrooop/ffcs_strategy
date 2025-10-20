---
issue: 15
created: 2025-10-19T19:30:00Z
status: ready
---

# Analysis: Create earnings_cache.py module

## Overview
Create a standalone Python module that provides persistent SQLite caching for earnings dates with Yahoo Finance as the primary data source. This is the foundational component that all other tasks depend on.

## Work Streams

### Stream A: Core Cache Infrastructure (6-8 hours)
**Scope:** SQLite database setup, schema creation, CRUD operations
**Owner:** general-purpose agent

**Implementation details:**
- Create `scripts/earnings_cache.py` with `EarningsCache` class
- SQLite schema: `earnings(symbol, next_earnings_date, last_updated, data_source)`
- Auto-create `.cache/` directory if doesn't exist
- `__init__()` method initializes database connection
- `_get_from_cache()` - retrieve cached earnings date
- `_save_to_cache()` - insert/update earnings record
- `_is_cache_fresh()` - check if date is in future (invalidation logic)

**Files to create:**
- `scripts/earnings_cache.py` (NEW)

**Key considerations:**
- Use `sqlite3` stdlib module (no new dependencies)
- Database location: `.cache/earnings.db` (relative to project root)
- Handle SQLite exceptions gracefully (database locked, corruption)
- Thread-safe: Use `check_same_thread=False` if needed

**Testing approach:**
- Manual: Create cache, insert records, verify persistence
- Manual: Test cache invalidation by setting old dates
- Edge cases: Database doesn't exist, corrupted database

### Stream B: Yahoo Finance Integration (4-6 hours)
**Scope:** Fetch earnings dates from Yahoo Finance via yfinance
**Owner:** general-purpose agent

**Implementation details:**
- `_fetch_from_yahoo(symbol)` - primary data source method
- Use `yfinance` library (already installed)
- Try `ticker.calendar` first, fallback to `ticker.get_earnings_dates()`
- Extract next upcoming earnings date from response
- Handle API timeouts (5s timeout)
- Handle missing data gracefully (return None)
- Futures symbols (starting with '/') return None immediately

**Key considerations:**
- yfinance is unofficial API (may break)
- Need timeout to prevent hanging
- Some symbols may not have earnings data available
- Date format: YYYY-MM-DD (ISO 8601)

**Testing approach:**
- Manual: Test with 10 known symbols (AAPL, SPY, QQQ, etc.)
- Manual: Test with futures symbols (/ES, /GC) - should skip API call
- Manual: Test with invalid symbol - should handle gracefully
- Performance: Measure response time (~100ms target)

### Stream C: Batch Processing & Public API (2-3 hours)
**Scope:** Efficient batch processing for multiple symbols
**Owner:** general-purpose agent

**Implementation details:**
- `get_next_earnings(symbol)` - single symbol lookup
- `batch_get_earnings(symbols)` - batch processing
- Return format: `{"symbol": str, "next_earnings": str|None, "source": str, "cached_at": str}`
- Cache-first strategy: Check cache before fetching
- Invalidation: Re-fetch if cached date in past

**Key considerations:**
- Batch processing should be efficient (avoid N+1 queries)
- Return consistent dict format for all symbols
- Track data source ("cache" vs "yahoo" for debugging)

**Testing approach:**
- Manual: Process 100 symbols, verify performance (<10s)
- Manual: Run twice, verify cache hits on second run
- Manual: Verify futures bypass (instant return)

## Dependencies Between Streams
- **Stream A → Stream B:** Cache infrastructure must exist before Yahoo fetching
- **Stream B → Stream C:** Yahoo fetching must work before batch processing
- **Sequential execution recommended:** A → B → C

## Success Criteria
- [ ] `scripts/earnings_cache.py` file exists with complete implementation
- [ ] Manual testing: 100 symbols in <10s (cold start)
- [ ] Manual testing: 100 symbols in <1s (warm cache)
- [ ] Manual testing: Futures symbols instant bypass
- [ ] Code review: All edge cases handled
- [ ] Ready for Task #16 integration

## Risks & Mitigations
**Risk:** Yahoo Finance API changes
- Mitigation: TastyTrade fallback in Task #17
- Current approach: Use yfinance library (maintains compatibility)

**Risk:** SQLite database corruption
- Mitigation: Auto-rebuild on corruption detection
- User can manually delete `.cache/earnings.db`

**Risk:** Performance doesn't meet targets
- Mitigation: Optimize batch queries, consider connection pooling
- Target is generous (10s for 1000 symbols)

## Notes
- No TastyTrade integration yet (Task #17)
- No CSV output changes yet (Task #18)
- Module should be standalone and testable independently
