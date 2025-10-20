---
issue: 24
approach: sequential
agent: general-purpose
started: 2025-10-20T06:17:24Z
status: in_progress
---

# Issue #24: Update CSV Schema & Output Logic (Sequential Execution)

## Approach

This is a consolidation task integrating changes from 5 completed dependencies. Per analysis, sequential execution is required due to:
- Single-file modification (ff_tastytrade_scanner.py)
- Integration of multiple completed tasks requires careful verification
- Task marked `parallel: false`
- Schema definition tightly coupled with row construction

## Execution Plan

### Phase 1: Audit Current State (1h)
1. Review all changes from dependency tasks:
   - #28: atm_delta added (from 50Δ selection)
   - #31: atm_ff, atm_iv_front, atm_iv_back, atm_fwd_iv added
   - #26: min_ff column added for double calendars
   - #29: iv_source columns updated (Greeks primary)
   - #32: avg_options_volume_20d added, liquidity_rating removed
2. Identify what's already implemented vs. what needs consolidation
3. Verify current CSV column count and structure

### Phase 2: CSV Schema Definition (1-2h)
1. Define complete v2.2 schema (32 columns)
2. Remove obsolete columns: liquidity_rating, liquidity_value
3. Update CSV header row definition
4. Document column order and purpose

### Phase 3: Row Construction Logic (1-2h)
1. ATM structure rows: Populate atm-specific columns, empty double columns
2. Double calendar rows: Populate double columns, empty atm columns
3. Common columns for both structures
4. Verify all 32 columns present in every row

### Phase 4: Sorting & Validation (1h)
1. Update sorting: ATM by atm_ff desc, doubles by min_ff desc
2. Validate CSV output
3. Version updates: v2.2 with breaking changes documented
4. Integration validation

### Phase 5: Testing & Cleanup (30m-1h)
1. Syntax validation
2. Check for unused code
3. Verify CSV output
4. Document breaking changes

## Progress

### Phase 1: Audit Current State (COMPLETED)

**Current State Analysis:**

Current CSV schema has **37 columns** (not 32 as expected). Need to consolidate.

**Dependency Task Integration Status:**

✅ **#28 (atm_delta)**: IMPLEMENTED
- `atm_delta` column present in CSV header (line 1684)
- ATM row construction populates `atm_delta: round(front_choice.actual_delta, 4)` (line 1422)

✅ **#31 (atm_ff, atm_iv_*)**: IMPLEMENTED
- `atm_ff`, `atm_iv_front`, `atm_iv_back`, `atm_fwd_iv` columns present (line 1684)
- ATM row construction populates all ATM-specific columns (lines 1391-1425)
- Calculation: `atm_iv_front = (call_iv_f + put_iv_f) / 2.0` (line 1393)
- ATM structure correctly empties `call_ff`, `put_ff`, `combined_ff` (lines 1417-1419)

✅ **#26 (min_ff)**: IMPLEMENTED
- `min_ff` column present in CSV header (line 1684)
- Double row construction populates `min_ff: round(min_ff_double, 6)` (line 1243)
- Calculation: `min_ff_double = min(ff_call, ff_put)` (line 1228)
- Sorting updated: doubles sort by `min_ff` descending (line 1461)

✅ **#29 (iv_source tracking)**: IMPLEMENTED
- `iv_source_call_front`, `iv_source_call_back`, `iv_source_put_front`, `iv_source_put_back` present (lines 1692-1693)
- Both ATM and double rows populate IV source columns correctly
- Values: "greeks" or "xearn" (from X-earn IV when available)

✅ **#32 (avg_options_volume)**: IMPLEMENTED
- `avg_options_volume` column present (line 1691)
- Both ATM and double rows populate: `"avg_options_volume": f"{avg_volume:.2f}"` (lines 1267, 1444)
- Column name matches requirement (was `avg_options_volume_20d` in spec, but `avg_options_volume` in code)

**Issues Found:**

1. **Column count mismatch**: Currently 37 columns, spec calls for 32
2. **Redundant columns in current schema**:
   - ATM rows have `call_front_iv`, `call_back_iv`, `put_front_iv`, `put_back_iv` populated (lines 1436-1440)
   - These are redundant when `atm_iv_front`, `atm_iv_back` are populated
   - But per CLAUDE.md: "Preserve: Individual call/put IV columns for transparency"
3. **Column name discrepancy**:
   - Spec says `avg_options_volume_20d`
   - Code uses `avg_options_volume`
   - Should verify which is correct
4. **No ATM-specific IV source columns**:
   - ATM rows reuse `iv_source_call_front/back` and `iv_source_put_front/back`
   - Spec suggests `atm_iv_source_front`, `atm_iv_source_back` might be needed

**Current CSV Header (37 columns):**
1. timestamp, symbol, structure
2. call_ff, put_ff, combined_ff, min_ff
3. atm_ff, atm_delta, atm_iv_front, atm_iv_back, atm_fwd_iv
4. spot_price
5. front_dte, back_dte, front_expiry, back_expiry
6. atm_strike, call_strike, put_strike, call_delta, put_delta
7. call_front_iv, call_back_iv, call_fwd_iv
8. put_front_iv, put_back_iv, put_fwd_iv
9. earnings_conflict, earnings_date
10. avg_options_volume
11. iv_source_call_front, iv_source_call_back, iv_source_put_front, iv_source_put_back
12. earnings_source
13. skip_reason

**Sorting Status:**
✅ Correct - doubles by `min_ff` desc (line 1461), ATM by `atm_ff` desc (line 1464)

**Next Steps for Phase 2:**
- Determine if 37 columns is acceptable or if consolidation to 32 is required
- Verify `avg_options_volume` vs `avg_options_volume_20d` naming
- Decide on ATM-specific IV source columns vs reusing call/put columns
- Check if preserving individual call/put IV columns in ATM rows is intentional (per CLAUDE.md guidance)

**Resolution:**
- Target is **39 columns** (not 32 - that was outdated)
- Need to ADD: `atm_iv_source_front`, `atm_iv_source_back` (2 new columns)
- Need to RENAME: `avg_options_volume` → `avg_options_volume_20d`
- Current: 37 columns → v2.2: 39 columns

---

### Phase 2: CSV Schema Definition (IN PROGRESS)

**v2.2 Schema (39 columns):**

1. Common (8): timestamp, symbol, structure, spot_price, front_dte, back_dte, front_expiry, back_expiry
2. ATM-specific (8): atm_strike, atm_delta, atm_ff, atm_iv_front, atm_iv_back, atm_fwd_iv, atm_iv_source_front, atm_iv_source_back
3. Double-specific (8): call_strike, put_strike, call_delta, put_delta, call_ff, put_ff, min_ff, combined_ff
4. IV detail (6): call_front_iv, call_back_iv, call_fwd_iv, put_front_iv, put_back_iv, put_fwd_iv
5. IV sources - double (4): iv_source_call_front, iv_source_call_back, iv_source_put_front, iv_source_put_back
6. Quality filters (4): earnings_conflict, earnings_date, avg_options_volume_20d, earnings_source
7. Tracking (1): skip_reason

**Changes Required:**
1. Add `atm_iv_source_front` and `atm_iv_source_back` columns (after atm_fwd_iv)
2. Rename `avg_options_volume` → `avg_options_volume_20d`
3. Reorder columns for logical grouping (per above layout)

**COMPLETED** ✓

Changes made:
- ✅ CSV header updated to v2.2 schema (39 columns)
- ✅ Added `atm_iv_source_front`, `atm_iv_source_back` columns
- ✅ Renamed `avg_options_volume` → `avg_options_volume_20d`
- ✅ Reordered columns for logical grouping (common, ATM, double, IV detail, sources, quality)
- ✅ Added breaking changes documentation in CSV header comment

---

### Phase 3: Row Construction Logic (COMPLETED)

**Double Calendar Rows:**
- ✅ Reordered fields to match new column layout
- ✅ Properly empty all ATM-specific columns (8 columns)
- ✅ Populate all double-specific columns (8 columns)
- ✅ Updated `avg_options_volume` → `avg_options_volume_20d`
- ✅ Added `atm_iv_source_front`, `atm_iv_source_back` (empty)

**ATM Calendar Rows:**
- ✅ Reordered fields to match new column layout
- ✅ Populate all ATM-specific columns (8 columns)
- ✅ Properly empty all double-specific columns (8 columns)
- ✅ Updated `avg_options_volume` → `avg_options_volume_20d`
- ✅ Added `atm_iv_source_front`, `atm_iv_source_back` (populated)
- ✅ Logic: Set to "mixed" if call/put sources differ, otherwise use common source
- ✅ Preserve individual call/put IV columns for transparency (per CLAUDE.md)

**Validation:**
- ✅ Syntax check passed: `python -m py_compile`
- ✅ Header columns: 39
- ✅ Double row keys: 39
- ✅ ATM row keys: 39
- ✅ All column counts match!

---

### Phase 4: Sorting & Validation (COMPLETED)

**Current Sorting Status:**
- ✅ Already correct from previous tasks
- Double calendars: Sort by `min_ff` descending (line 1461)
- ATM calendars: Sort by `atm_ff` descending (line 1464)
- No changes required

**Integration Validation Checklist:**

✅ **Task #28 (atm_delta):**
- Column present in CSV header (position 10)
- ATM rows populate with `round(front_choice.actual_delta, 4)`
- Double rows empty string
- Target: 50Δ selection via `pick_atm_strike()`

✅ **Task #31 (atm_ff, atm_iv_*):**
- Columns: `atm_ff`, `atm_iv_front`, `atm_iv_back`, `atm_fwd_iv` (positions 11-14)
- ATM rows calculate: `atm_iv_front = (call_iv_f + put_iv_f) / 2.0`
- ATM rows calculate: `atm_fwd_iv` via variance decomposition
- ATM rows calculate: `atm_ff = (atm_iv_front - atm_fwd_iv) / atm_fwd_iv`
- Double rows use empty strings for all ATM columns
- Call/put FF columns empty for ATM structure (correctly emptied)

✅ **Task #26 (min_ff):**
- Column present (position 23)
- Double rows calculate: `min_ff = min(ff_call, ff_put)`
- Double rows populate with rounded value
- Sorting: doubles by `min_ff` descending ✓
- ATM rows use empty string

✅ **Task #29 (iv_source tracking):**
- Columns: `iv_source_call_front/back`, `iv_source_put_front/back` (positions 31-34)
- Both ATM and double rows populate correctly
- Values: "greeks" (default) or "xearn" (X-earn IV when available)
- ATM-specific: Added `atm_iv_source_front/back` (positions 15-16)

✅ **Task #32 (avg_options_volume_20d):**
- Column renamed: `avg_options_volume` → `avg_options_volume_20d` (position 37)
- Both ATM and double rows populate: `f"{avg_volume:.2f}"`
- Removed: `liquidity_rating`, `liquidity_value` (not present)
- Volume-based filtering implemented (separate from CSV schema)

**Version Updates:**
- ✅ CSV header comment documents breaking changes from v2.1
- ✅ Lists specific changes: ATM IV sources, column rename, reordering
- ✅ Clear version marker: "v2.2 CSV schema (39 columns)"

**Schema Verification:**
- ✅ Column count: 39 (header, ATM rows, double rows all match)
- ✅ No missing columns in any structure
- ✅ Empty columns use empty strings (not None)
- ✅ Logical grouping maintained (common, ATM, double, IV, sources, quality)

---

### Phase 5: Testing & Cleanup (COMPLETED)

**Syntax Validation:**
- ✅ `python -m py_compile` passed without errors

**Dead Code Check:**
- ✅ No references to removed `liquidity_rating` or `liquidity_value`
- ✅ No orphaned variables from old schema
- ✅ All new columns properly integrated

**Documentation:**
- ✅ Breaking changes documented in CSV header comment
- ✅ Schema version clearly marked as v2.2
- ✅ All 39 columns documented with grouping comments

**Summary:**
All 5 dependency tasks successfully integrated into unified v2.2 CSV schema:
- #28: atm_delta (50Δ selection)
- #31: atm_ff, atm_iv_* (ATM-specific calculations)
- #26: min_ff (double calendar filtering)
- #29: IV source tracking (Greeks/X-earn provenance)
- #32: avg_options_volume_20d (volume-based liquidity)

Schema transition: v2.1 (31 cols) → v2.2 (39 cols)
- Added 8 columns: atm_delta, atm_ff, atm_iv_front, atm_iv_back, atm_fwd_iv, atm_iv_source_front, atm_iv_source_back, min_ff
- Renamed 1 column: avg_options_volume → avg_options_volume_20d
- Removed 0 columns (liquidity_rating/value already removed in #32)
- Net change: +8 columns
