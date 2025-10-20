---
issue: 24
title: Update CSV Schema & Output Logic
analyzed: 2025-10-20T06:17:24Z
estimated_hours: 4-6
parallelization_factor: 1.0
---

# Parallel Work Analysis: Issue #24

## Overview

Consolidate all CSV schema changes from completed dependency tasks (#28, #31, #26, #29, #32) into a unified v2.2 CSV schema. This is an integration task that brings together ATM column changes, double calendar min_ff, volume-based filtering, and IV source tracking into a coherent 32-column output format.

**Critical Context**: This task integrates changes from 5 completed tasks and requires careful verification that all pieces fit together correctly.

## Work Stream Analysis

### Single Stream: CSV Schema Consolidation (Recommended)
**Scope**: Complete CSV schema v2.2 implementation and validation
**Files**:
- `scripts/ff_tastytrade_scanner.py` (CSV header, row construction, sorting)
**Agent Type**: general-purpose
**Can Start**: immediately (all dependencies complete)
**Estimated Hours**: 4-6
**Dependencies**: #28 ✅, #31 ✅, #26 ✅, #29 ✅, #32 ✅

**Work Phases**:

**Phase 1: Audit Current State (1h)**
1. Review all changes from dependency tasks:
   - #28: atm_delta added (from 50Δ selection)
   - #31: atm_ff, atm_iv_front, atm_iv_back, atm_fwd_iv added
   - #26: min_ff column added for double calendars
   - #29: iv_source columns updated (Greeks primary)
   - #32: avg_options_volume_20d added, liquidity_rating removed
2. Identify what's already implemented vs. what needs consolidation
3. Verify current CSV column count and structure

**Phase 2: CSV Schema Definition (1-2h)**
1. Define complete v2.2 schema (32 columns):
   - Common: timestamp, symbol, structure, spot_price, front_dte, back_dte, front_expiry, back_expiry
   - ATM-specific: atm_strike, atm_delta, atm_ff, atm_iv_front, atm_iv_back, atm_fwd_iv
   - Double-specific: call_strike, put_strike, call_delta, put_delta, call_ff, put_ff, min_ff, combined_ff
   - IV columns: call_front_iv, call_back_iv, call_fwd_iv, put_front_iv, put_back_iv, put_fwd_iv
   - Source tracking: iv_source_call_front, iv_source_call_back, iv_source_put_front, iv_source_put_back
   - Quality filters: earnings_conflict, earnings_date, avg_options_volume_20d, earnings_source
   - Tracking: skip_reason
2. Remove obsolete columns: liquidity_rating, liquidity_value
3. Update CSV header row definition
4. Document column order and purpose

**Phase 3: Row Construction Logic (1-2h)**
1. ATM structure rows:
   - Populate: atm_strike, atm_delta, atm_ff, atm_iv_front, atm_iv_back, atm_fwd_iv
   - Empty: call_strike, put_strike, call_delta, put_delta, call_ff, put_ff, min_ff, combined_ff
   - Preserve: Individual call/put IV columns for transparency
   - Source tracking: atm_iv_source_front, atm_iv_source_back
2. Double calendar rows:
   - Populate: call_strike, put_strike, call_delta, put_delta, call_ff, put_ff, min_ff, combined_ff
   - Empty: atm_strike, atm_delta, atm_ff, atm_iv_front, atm_iv_back, atm_fwd_iv
   - Preserve: Individual call/put IV columns
   - Source tracking: iv_source_call_front, iv_source_call_back, iv_source_put_front, iv_source_put_back
3. Common columns for both structures:
   - Quality filters: earnings_conflict, earnings_date, avg_options_volume_20d, earnings_source
   - Tracking: skip_reason
4. Verify all 32 columns present in every row

**Phase 4: Sorting & Validation (1h)**
1. Update sorting logic:
   - ATM rows: Sort by atm_ff descending (highest opportunities first)
   - Double rows: Sort by min_ff descending (per #26)
   - Combined output: Maintain structure-specific sorting
2. Validate CSV output:
   - Check column count (exactly 32)
   - Verify no missing columns
   - Test with sample data
3. Version updates:
   - Update docstring: "v2.2" with breaking changes documented
   - Update comments referencing schema version
4. Integration validation:
   - Verify all dependency task changes are included
   - Check for any orphaned code from old schema

**Phase 5: Testing & Cleanup (30m-1h)**
1. Syntax validation: `python -m py_compile scripts/ff_tastytrade_scanner.py`
2. Check for unused variables or dead code
3. Verify CSV file can be written and read
4. Document breaking changes in commit message

## Alternative Parallelization (NOT Recommended)

If time-critical, could split into 2 streams:

### Stream A: Schema Definition & Header
**Scope**: Define v2.2 schema and update CSV header
**Estimated Hours**: 1-2
**Risk**: Medium - must coordinate column order with Stream B

### Stream B: Row Construction & Sorting
**Scope**: Update ATM/double row logic and sorting
**Estimated Hours**: 2-3
**Dependencies**: Coordinate with Stream A on final column list

**Why Not Recommended:**
- Single file modification creates merge conflicts
- Tight coupling between header and row construction
- Task marked `parallel: false`
- Coordination overhead likely exceeds time savings

## Coordination Points

### Shared Files
- `scripts/ff_tastytrade_scanner.py`: All work in single file
  - CSV header definition (~line 1675-1691)
  - ATM row construction (~line 1386-1464)
  - Double row construction (~line 1236-1274)
  - Sorting logic (~line 1453-1464)

### Sequential Requirements
1. Schema definition must be finalized before row construction updates
2. Row construction must be complete before sorting updates
3. All logic changes before version bump and documentation

## Conflict Risk Assessment

**Medium-High Risk** (if parallelized):
- Single-file modification with multiple logical sections
- Schema changes affect both header and row construction
- Column order must match exactly between header and rows
- High coordination overhead for marginal time savings

**Low Risk** (if sequential):
- Clear linear progression through phases
- No coordination needed
- Easy to validate at each step

## Parallelization Strategy

**Recommended Approach**: Sequential

Execute in order:
1. Phase 1: Audit current state
2. Phase 2: CSV schema definition
3. Phase 3: Row construction logic
4. Phase 4: Sorting & validation
5. Phase 5: Testing & cleanup

**Rationale**:
- Task marked `parallel: false`
- Single-file consolidation task
- Integration of 5 completed tasks requires careful verification
- Sequential execution ensures nothing is missed
- Clear phase boundaries make progress tracking easy

## Expected Timeline

**Sequential execution**:
- Phase 1: 1 hour (audit)
- Phase 2: 1-2 hours (schema definition)
- Phase 3: 1-2 hours (row construction)
- Phase 4: 1 hour (sorting & validation)
- Phase 5: 30m-1h (testing)
- **Total wall time**: 4-6 hours

**Parallel execution** (not recommended):
- Streams A & B overlap: 2-3 hours
- Merge conflicts & coordination: +1 hour
- **Total wall time**: 3-4 hours (only 1-2h savings, high risk)

## Notes

**Critical Success Factors**:
1. **Verify all dependency changes are included**:
   - ✅ #28: atm_delta from pick_atm_strike()
   - ✅ #31: atm_ff and atm_iv_* columns
   - ✅ #26: min_ff for double calendars
   - ✅ #29: IV source tracking (Greeks primary)
   - ✅ #32: avg_options_volume_20d, removed liquidity_rating

2. **Column count accuracy**: Must be exactly 32 columns
3. **Structure-specific logic**: ATM vs. double rows have different populated columns
4. **Sorting correctness**: ATM by atm_ff, doubles by min_ff
5. **Version bump**: Update to v2.2 in docstring and comments

**Integration Validation Checklist**:
- [ ] atm_delta present in ATM rows (from #28)
- [ ] atm_ff, atm_iv_front, atm_iv_back, atm_fwd_iv in ATM rows (from #31)
- [ ] min_ff present in double rows (from #26)
- [ ] iv_source_* columns tracking data sources (from #29)
- [ ] avg_options_volume_20d present, liquidity_rating removed (from #32)
- [ ] skip_reason column present
- [ ] All 32 columns in header match row construction
- [ ] Sorting by correct column per structure

**Potential Issues**:
- Some columns may already be partially implemented by dependency tasks
- Need to verify current state before making changes
- May find inconsistencies between tasks that need reconciliation
- CSV schema documentation (CLAUDE.md) will need updates in #27

**Documentation Impact**:
- Breaking changes: v2.1 → v2.2
- Column count change: 31 → 32 (or current count → 32)
- Schema changes affect downstream CSV consumers
- Task #27 will update CLAUDE.md and README_TT.md

## Recommendation

**Execute sequentially** through the 5 phases. This is a consolidation and integration task where careful verification is more important than speed. The risk of errors from parallelization outweighs the 1-2 hour potential time savings.
