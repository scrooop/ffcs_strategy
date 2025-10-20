---
issue: 27
approach: sequential
agent: general-purpose
started: 2025-10-20T06:25:44Z
status: in_progress
---

# Issue #27: Update Documentation (Sequential Execution)

## Approach

Per analysis, sequential execution is required due to:
- Task marked `parallel: false`
- Consistency critical across both documentation files
- Shared content (CSV schema, breaking changes, migration guide)
- Accuracy more important than time savings

## Execution Plan

### Phase 1: Gather v2.2 Changes (30m)
1. Review Task #24 completion summary
2. Extract v2.2 CSV schema details (39 columns, not 32)
3. Identify all breaking changes:
   - 8 new columns added
   - 1 column renamed
   - 2 columns removed (already in #32)
   - CLI flags changed
4. Create comprehensive change list for reference

### Phase 2: Update CLAUDE.md (1.5-2h)
1. Update CSV Output Schema section (31 → 39 columns)
2. Add v2.1 → v2.2 Migration Guide with column mapping table
3. Update CLI flags documentation (remove deprecated, document new)
4. Add Troubleshooting section
5. Update Version History with v2.2 entry
6. Update usage examples (ATM and double structures)
7. Document IV source priority decision (Greeks primary)

### Phase 3: Update README_TT.md (1-1.5h)
1. Apply same changes as CLAUDE.md
2. Ensure consistency with main documentation
3. Update command examples
4. Add troubleshooting section

### Phase 4: Validation (30m)
1. Verify column counts match implementation (39 not 32)
2. Check all CLI flags are current
3. Test example command syntax
4. Ensure consistency between docs

## v2.2 Changes Summary (from #24)

**CSV Schema**: v2.1 (31 cols) → v2.2 (39 cols)

**Added Columns (8):**
- atm_delta: Delta at ATM strike (50Δ selection)
- atm_ff: Single forward factor for ATM structure
- atm_iv_front, atm_iv_back, atm_fwd_iv: ATM IV values
- atm_iv_source_front, atm_iv_source_back: ATM IV source tracking
- min_ff: Minimum FF for double calendar filtering

**Renamed Columns (1):**
- avg_options_volume → avg_options_volume_20d

**Removed Columns (2):**
- liquidity_rating (removed in #32)
- liquidity_value (removed in #32)

**Breaking Changes:**
1. CSV schema expanded from 31 to 39 columns
2. ATM structure uses new atm-specific columns, empties double columns
3. Double structure uses new min_ff column, empties atm columns
4. Column rename requires CSV parser updates
5. CLI flags removed: --use-xearn-iv, --force-greeks-iv, --min-liquidity-rating

## Progress

### Phase 1: Gather v2.2 Changes (COMPLETED)

**Verified v2.2 CSV Schema: 39 columns (not 32)**

Exact column order from scanner code (lines 1708-1729):
1. Common (8): timestamp, symbol, structure, spot_price, front_dte, back_dte, front_expiry, back_expiry
2. ATM-specific (8): atm_strike, atm_delta, atm_ff, atm_iv_front, atm_iv_back, atm_fwd_iv, atm_iv_source_front, atm_iv_source_back
3. Double-specific (8): call_strike, put_strike, call_delta, put_delta, call_ff, put_ff, min_ff, combined_ff
4. IV detail (6): call_front_iv, call_back_iv, call_fwd_iv, put_front_iv, put_back_iv, put_fwd_iv
5. IV sources - double (4): iv_source_call_front, iv_source_call_back, iv_source_put_front, iv_source_put_back
6. Quality filters (4): earnings_conflict, earnings_date, avg_options_volume_20d, earnings_source
7. Tracking (1): skip_reason

**Breaking Changes from v2.1:**
1. **Added columns (9)**:
   - atm_delta (from 50Δ strike selection, #28)
   - atm_ff (single FF for ATM, #31)
   - atm_iv_front, atm_iv_back, atm_fwd_iv (ATM IV values, #31)
   - atm_iv_source_front, atm_iv_source_back (ATM IV source tracking, #31)
   - min_ff (min of call_ff and put_ff for doubles, #26)
   - skip_reason (tracking field, #24)

2. **Renamed columns (1)**:
   - avg_options_volume → avg_options_volume_20d (#32)

3. **Removed columns (2)**:
   - liquidity_rating (removed in #32)
   - liquidity_value (removed in #32)

4. **Structure-specific changes**:
   - ATM rows: New atm_* columns populated, double columns empty
   - Double rows: Double columns populated, atm_* columns empty
   - ATM FF calculation simplified: single atm_ff replaces dual call_ff/put_ff

5. **CLI flag changes**:
   - Removed: --use-xearn-iv (X-earn is now fallback)
   - Removed: --force-greeks-iv (Greeks is now primary)
   - Removed: --min-liquidity-rating (replaced by volume filtering)
   - Current: --min-avg-volume (volume-based filtering)

6. **IV source priority**:
   - Greeks IV is PRIMARY (strike-level precision)
   - X-earn IV is RARE FALLBACK (when Greeks missing)
   - Rationale: More reliable, consistent availability, preserves skew

**Documentation Updates Required:**
- CLAUDE.md: 8 sections to update
- README_TT.md: 7 sections to update
- Add migration guide to both files
- Add troubleshooting section to both files
- Update all CLI examples to use current flags only

**Phase 2: Update CLAUDE.md (COMPLETED)**

**Changes Applied:**

1. **CSV Output Schema** (lines 299-360):
   - Updated header: "31 Columns" → "39 Columns - v2.2"
   - Updated sorting description: atm_ff (ATM) or min_ff (double)
   - Reorganized sections by column groups (8+8+8+6+4+4+1 = 39)
   - Added ATM-specific columns: atm_strike, atm_delta, atm_ff, atm_iv_*, atm_iv_source_*
   - Added double-specific: min_ff (new filtering metric)
   - Renamed: avg_options_volume → avg_options_volume_20d
   - Added tracking: skip_reason column
   - Complete column order updated (39 columns)

2. **Migration Guide** (lines 362-459):
   - NEW SECTION: v2.1 → v2.2 migration guide
   - Schema changes summary (31 → 39 columns)
   - Column mapping table (15 rows)
   - Breaking changes (5 items): ATM workflow, strike selection, column rename, removed columns, sorting
   - CLI flag changes (removed 3 flags)
   - Migration steps for CSV consumers (7 steps)
   - Example v2.2 CSV parsing code (Python/pandas)

3. **ATM Strike Selection** (lines 65, 252-255, 294, 320, 400):
   - Updated references: "closest to spot" → "delta closest to 50Δ (0.50 absolute delta)"
   - Updated FF calculation description: Single atm_ff using averaged ATM IVs
   - Updated pick_atm_strike() description

4. **Troubleshooting Section** (lines 531-637):
   - NEW SECTION: Common Issues and Solutions (9 issues)
   - Skip reason codes (8 codes)
   - Debug commands (3 subsections: cache, testing, schema verification)

5. **Version History** (lines 725-815):
   - NEW SECTION: Version History
   - v2.2 entry: Core calculation corrections (October 2025)
   - v2.1 entry: Fast earnings check with caching (September 2025)
   - v2.0 entry: Quality filtering and structure support (August 2025)
   - v1.0 entry: Initial release (July 2025)

6. **CSV Tracking Reference** (line 192):
   - Removed column position reference "(31st column)"

**Verification:**
- All v2.2 changes documented
- 39 columns confirmed in schema section
- Migration guide complete with examples
- Troubleshooting covers common issues
- Version history comprehensive

**Next: Phase 3 - Update README_TT.md**
