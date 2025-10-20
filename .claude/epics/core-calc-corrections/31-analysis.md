---
issue: 31
title: Simplify ATM FF Computation (Single FF)
analyzed: 2025-10-20T06:09:49Z
estimated_hours: 5-6
parallelization_factor: 1.3
---

# Parallel Work Analysis: Issue #31

## Overview

Simplify ATM calendar spread calculation by removing dual call_ff/put_ff computation and implementing single `atm_ff` metric. This requires modifying the scan loop logic, updating CSV schema, and adjusting gating/sorting behavior.

**Key Change**: ATM structure currently computes separate call_ff and put_ff (like double calendars), but since ATM uses a single strike, this creates redundant similar values. New approach: single atm_ff using IV from the 50Δ strike.

## Parallel Streams

### Stream A: Core ATM Calculation Logic
**Scope**: Modify ATM structure calculation in main scan loop
**Files**:
- `scripts/ff_tastytrade_scanner.py` (scan loop, ~lines 1200-1400)
**Agent Type**: general-purpose
**Can Start**: immediately (depends on #28 which is complete)
**Estimated Hours**: 3-4
**Dependencies**: Issue #28 ✅ (50Δ strike selection provides actual_delta)

**Work Items**:
1. Locate ATM structure branch in scan loop
2. Remove dual call_ff/put_ff calculation
3. Implement single atm_ff computation using call IV from 50Δ strike
   - Option 1: Use call IV only
   - Option 2: Average of call and put IV at ATM strike
4. Update gating logic: `if atm_ff >= args.min_ff` (not combined_ff)
5. Preserve actual_delta from pick_atm_strike() for CSV output

### Stream B: CSV Schema & Output Logic
**Scope**: Update CSV columns for ATM structure rows
**Files**:
- `scripts/ff_tastytrade_scanner.py` (CSV header, row construction, ~lines 500-600, 1400-1500)
**Agent Type**: general-purpose
**Can Start**: after Stream A completes (or in parallel with careful coordination)
**Estimated Hours**: 2-3
**Dependencies**: Stream A (needs atm_ff field available)

**Work Items**:
1. Add ATM-specific CSV columns:
   - `atm_ff`: Single forward factor for ATM structure
   - `atm_delta`: Actual delta from 50Δ strike selection
   - `atm_iv_front`: Front expiry IV at ATM strike
   - `atm_iv_back`: Back expiry IV at ATM strike
   - `atm_fwd_iv`: Forward IV between expirations
2. For ATM rows: Remove or leave empty call_ff, put_ff, combined_ff columns
3. Update CSV row construction to populate new ATM columns
4. Update sorting logic: ATM rows sort by atm_ff descending
5. Coordinate with Task #24 (CSV Schema) if needed

### Stream C: Testing & Validation (OPTIONAL)
**Scope**: Add/update tests for ATM FF calculation
**Files**:
- `tests/test_ff_calculations.py` (if ATM-specific tests needed)
**Agent Type**: general-purpose
**Can Start**: after Streams A & B complete
**Estimated Hours**: 1-2
**Dependencies**: Streams A & B

**Work Items**:
1. Review if existing tests cover ATM FF calculation
2. Add tests if needed for single atm_ff computation
3. Verify CSV output format for ATM rows
4. Integration test: Run scanner with ATM structure and verify output

## Coordination Points

### Shared Files
- `scripts/ff_tastytrade_scanner.py`: Both Stream A and B modify this file
  - **Stream A**: Scan loop logic (lines 1200-1400)
  - **Stream B**: CSV header/output (lines 500-600, 1400-1500)
  - **Risk**: Medium - different sections but same file

### Sequential Requirements
1. **Core logic before CSV**: Stream A must define atm_ff before Stream B can output it
2. **Calculation before testing**: Stream C depends on A & B completing

### Coordination Strategy
**Option 1 (Recommended)**: Sequential execution
- Complete Stream A (calculation logic)
- Then Stream B (CSV schema)
- Optional Stream C (testing)

**Option 2**: Hybrid parallel
- Start Stream A
- When A is 50% complete (atm_ff defined), start Stream B
- Stream B coordinates with A on variable names and structure

## Conflict Risk Assessment

**Medium Risk**: Single-file modification with two logical areas
- Streams A and B both modify `ff_tastytrade_scanner.py`
- Different sections of the file reduce direct conflicts
- CSV schema changes (Stream B) depend on calculation changes (Stream A)
- Coordination overhead may offset parallelization benefits

## Parallelization Strategy

**Recommended Approach**: Sequential with optional parallelization

**Sequential** (safest):
1. Complete Stream A (core calculation logic)
2. Complete Stream B (CSV schema updates)
3. Optional Stream C (testing/validation)

**Hybrid** (if time-critical):
1. Start Stream A
2. When Stream A defines atm_ff variable, start Stream B in parallel
3. Stream B waits/coordinates on any changes Stream A makes to data structures
4. Stream C after both complete

## Expected Timeline

**With sequential execution**:
- Stream A: 3-4 hours
- Stream B: 2-3 hours
- Stream C: 1-2 hours (optional)
- **Total wall time**: 5-6 hours (matches estimate)

**With hybrid parallel execution**:
- Streams A & B overlap by ~2 hours
- Stream C: 1-2 hours
- **Total wall time**: 4-5 hours
- **Efficiency gain**: ~15-20%

## Notes

**Important Considerations**:
1. **Task metadata shows `parallel: false`** - suggests sequential execution preferred
2. **Conflicts with Task #24** (CSV Schema) - coordinate on column changes
3. **Depends on Issue #28** ✅ - 50Δ strike selection now provides actual_delta
4. **Decision needed**: Use call IV only, or average of call/put IV at ATM strike?
5. **CSV compatibility**: Ensure new columns don't break downstream processing

**Recommendation**:
Execute sequentially (Stream A → Stream B → Stream C optional) unless time pressure requires hybrid parallelization. The tight coupling and single-file modification make coordination overhead higher than potential time savings.

**IV Source Decision**:
Per CLAUDE.md documentation: "For ATM Call Calendars: σ₁ (front IV) = IV from the ATM strike at front expiration. IV = average of (call IV, put IV) at that strike."

Use **average of call and put IV** at the 50Δ strike for consistency with existing documentation.
