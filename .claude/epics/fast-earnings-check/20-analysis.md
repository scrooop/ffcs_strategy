---
issue: 20
created: 2025-10-20T01:14:00Z
status: ready
---

# Analysis: Update documentation (README_TT.md, CLAUDE.md)

## Overview
Update all project documentation to reflect v2.1 changes: fast earnings check, cache behavior, new CSV schema (31 columns), CLI flag removal, and performance improvements. Ensure users understand the new features and how to use them.

## Work Streams (Can be done sequentially by single agent)

### Stream A: Update README_TT.md (2 hours)
**Scope:** User-facing scanner documentation
**Owner:** general-purpose agent

**Sections to add/update:**

1. **Add "Performance Improvements (v2.1)" section:**
   - Fast earnings pre-filter with caching
   - Yahoo Finance as primary source (~100ms vs 500ms TastyTrade)
   - SQLite persistent cache
   - Performance impact: 1000 symbols 8min → <30s
   - Cache location: `.cache/earnings.db`

2. **Update "Command Line Flags" section:**
   - Remove `--skip-earnings` references (no longer exists)
   - Update `--allow-earnings` description
   - Add note about default behavior (filtering enabled)

3. **Update "CSV Output Schema" section:**
   - Change from 28 → 31 columns
   - Add `earnings_source` column description
   - Update example CSV row

4. **Add "Troubleshooting" section:**
   - Cache issues (slow, corrupted)
   - Stale earnings dates
   - Database locked errors
   - Solutions for each

### Stream B: Update CLAUDE.md (1 hour)
**Scope:** Developer/AI assistant documentation
**Owner:** general-purpose agent

**Sections to update:**

1. **Update version note:**
   - From "2.0" → "2.1 - Fast earnings check with caching"

2. **Update "Earnings Filtering" → "Fast Earnings Check (v2.1)":**
   - Multi-source pipeline: Cache → Yahoo → TastyTrade
   - Cache behavior and invalidation
   - Performance targets
   - CSV tracking (earnings_source column)

3. **Update "Running the Scanner" section:**
   - Remove all `--skip-earnings` examples
   - Update command examples

4. **Update "CSV Output Schema" section:**
   - Update from 28 → 31 columns
   - Add earnings_source column to schema table
   - Update column descriptions

### Stream C: Create .cache/README.md (1 hour)
**Scope:** Cache management guide
**Owner:** general-purpose agent

**New file content:**

1. **Overview:**
   - Purpose of cache
   - Location: `.cache/earnings.db`
   - Type: SQLite database

2. **Cache Schema:**
   - SQL table structure
   - Column descriptions

3. **Cache Behavior:**
   - Automatic invalidation (date-based)
   - Data sources (Yahoo, TastyTrade)

4. **Manual Management:**
   - Clear cache: `rm .cache/earnings.db`
   - Inspect cache: `sqlite3` commands
   - Cache statistics

5. **Troubleshooting:**
   - Slow cache
   - Database locked
   - Stale data

6. **Performance:**
   - Cache hit: <10ms
   - Cache miss: ~100ms (Yahoo) or ~500ms (TastyTrade)

## Dependencies
- ✅ Task #16 completed (know how pre-filter works)
- ✅ Task #17 completed (know fallback behavior)
- ✅ Task #18 completed (know CSV schema - 31 columns)
- ✅ Task #19 completed (know CLI flag removal)

## Success Criteria
- [ ] README_TT.md updated with v2.1 changes
- [ ] CLAUDE.md updated with cache behavior
- [ ] .cache/README.md created (new file)
- [ ] CSV schema shows 31 columns (including earnings_source)
- [ ] All CLI examples remove --skip-earnings
- [ ] Performance claims accurate (verified by testing)
- [ ] Troubleshooting sections complete
- [ ] Migration guide for v2.0 → v2.1 users

## Key Information to Document

**Performance numbers (from testing):**
- 112 symbols, warm cache: 0.0s (instant)
- 112 symbols, cold cache: ~10s
- Filter rate: 80.4% (90/112 symbols during earnings week)
- Cache hit rate: 100% on subsequent runs

**CSV Schema Changes:**
- Old: 28 columns
- New: 31 columns
- Added: earnings_source (31st column)
- Values: "cache", "yahoo", "tastytrade", "none", "skipped"

**CLI Changes:**
- Removed: --skip-earnings flag
- Kept: --allow-earnings flag
- Default: Earnings filtering enabled

**Fallback Chain:**
- 1. Cache (instant, <10ms)
- 2. Yahoo Finance (primary, ~100ms, 5s timeout)
- 3. TastyTrade (fallback, ~500ms)
- 4. Graceful degradation (return None)

## Files to Update/Create
- `scripts/README_TT.md` (UPDATE)
- `CLAUDE.md` (UPDATE)
- `.cache/README.md` (CREATE NEW)

## Testing Documentation
After updates:
- [ ] Follow cache clearing instructions → Verify works
- [ ] Run example commands → Verify all work (no --skip-earnings)
- [ ] Check CSV schema example → Verify matches actual output
- [ ] Follow troubleshooting steps → Verify solutions work

## Notes
- Coordinate with Task #21: Performance claims should match benchmarks
- Version increment: All docs reference v2.1 consistently
- Keep simple: Focus on user-facing behavior, not implementation details
- Migration guide: Help v2.0 users upgrade smoothly
