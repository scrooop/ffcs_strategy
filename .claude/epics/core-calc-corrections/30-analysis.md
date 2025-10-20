---
issue: 30
title: Integration Testing & Validation
analyzed: 2025-10-20T06:51:37Z
estimated_hours: 4-6
parallelization_factor: 1.0
---

# Parallel Work Analysis: Issue #30

## Overview

Final validation task for the core-calc-corrections epic. Comprehensive end-to-end testing of v2.2 scanner including formula validation, CSV schema verification, performance regression testing, and comparison with v2.1 baseline.

**Critical Note**: Task mentions "32 columns" but actual v2.2 schema has **39 columns** (per Task #24). All validation must use 39 columns.

**Purpose**: Gate for epic completion - ensures all changes work correctly together and meet quality standards before merge.

## Work Stream Analysis

### Single Stream: Comprehensive Integration Testing (Recommended)

**Scope**: Complete end-to-end validation of v2.2 scanner
**Files**:
- `scripts/ff_tastytrade_scanner.py` (testing, no modifications)
- Test output CSVs (generated during testing)
- Test results documentation (new file in `.claude/epics/core-calc-corrections/`)
**Agent Type**: general-purpose
**Can Start**: immediately (dependencies #24, #27 complete)
**Estimated Hours**: 4-6
**Dependencies**: None (all implementation tasks complete)

**Testing Phases**:

**Phase 1: End-to-End Scan Testing (1h)**
1. Run scanner with known liquid symbols: SPY, QQQ, AAPL, TSLA, NVDA
2. Test both ATM and double structures
3. Verify scanner completes without errors
4. Generate CSV output for validation

**Phase 2: CSV Schema Validation (1h)**
1. Verify 39 columns present (NOT 32)
2. Check column order matches v2.2 spec
3. Validate column types and formats
4. Verify structure-specific columns:
   - ATM rows: atm_* columns populated, double columns empty
   - Double rows: double columns populated, atm_* columns empty
5. Check all rows have exactly 39 fields

**Phase 3: Calculation Accuracy Testing (1-1.5h)**
1. ATM structure validation:
   - Verify atm_ff used for filtering (not combined_ff)
   - Check 50Δ strike selection accuracy (atm_delta within ±0.05 of 0.50)
   - Target: 95%+ of ATM strikes within ±5Δ tolerance
2. Double structure validation:
   - Verify min_ff used for filtering (min of call_ff and put_ff)
   - Check both wings meet threshold independently
   - Verify ±35Δ strike selection (call_delta ≈ 0.35, put_delta ≈ -0.35)
3. Hand-calculate FF for 3 sample opportunities:
   - Pick 1 ATM, 2 double calendars from output
   - Manual calculation using spot, IVs, DTEs
   - Compare to scanner output (tolerance: ±0.0001)

**Phase 4: Feature Verification Testing (1h)**
1. Volume filter test:
   - Test symbols below --min-avg-volume threshold
   - Verify skip_reason = "volume_too_low"
   - Check avg_options_volume_20d populated correctly
2. IV source test:
   - Verify Greeks IV used as primary
   - Check iv_source_* columns show "greeks" predominantly
   - Log any "xearn" fallback cases (should be rare)
3. Edge case testing:
   - Symbols with missing IV data
   - Non-positive variance scenarios
   - Expiration date mismatches
   - Graceful error handling validation

**Phase 5: Performance Regression Testing (30m-1h)**
1. Baseline test: Time v2.2 scanner with different symbol counts
   - Small: 10 symbols
   - Medium: 50 symbols
   - Large: 100 symbols
2. Document scan times
3. Note: Cannot compare to v2.1 directly (would need v2.1 branch)
4. Verify no obvious performance issues (reasonable scan times)

**Phase 6: Manual Spot-Checks (30m-1h)**
1. Select 5 high-FF opportunities from scan output
2. Manual validation for each:
   - Verify strike prices reasonable (near spot for ATM, ±35Δ for double)
   - Check FF calculation makes sense (front IV > back IV)
   - Validate DTE pairs match requested pairs
   - Confirm structure field matches populated columns
3. Document findings

**Phase 7: Test Results Documentation (30m)**
1. Create test results file: `.claude/epics/core-calc-corrections/30-test-results.md`
2. Document:
   - Test environment (date, branch, commit)
   - Test execution summary (pass/fail for each phase)
   - CSV schema validation results
   - Calculation accuracy results (hand-calc comparison)
   - Performance metrics
   - Edge case handling results
   - Manual spot-check findings
   - Issues found (if any)
   - Overall assessment (ready to merge or needs fixes)

## Alternative Parallelization (NOT Recommended)

Could theoretically split into 2 streams:

### Stream A: Automated Testing
**Scope**: Automated scans, CSV validation, performance testing
**Estimated Hours**: 2-3

### Stream B: Manual Validation
**Scope**: Hand calculations, spot-checks, results documentation
**Estimated Hours**: 2-3

**Why Not Recommended:**
1. Manual validation depends on automated scan output
2. Task marked `parallel: false` (final validation gate)
3. Single sequential flow ensures thorough validation
4. Documentation is easier with complete context
5. No time savings (manual work waits for scans anyway)

## Coordination Points

### No Shared Files
- Testing only, no code modifications
- Each test phase builds on previous results
- Clear sequential dependencies

### Sequential Requirements
1. Scans must complete before CSV validation
2. CSV output needed for hand-calc verification
3. All tests done before documenting results
4. Results documented before marking epic complete

## Conflict Risk Assessment

**No Risk**: Testing task, no code changes
- Reads existing scanner code
- Generates test outputs
- Documents validation results
- No conflicts possible

## Parallelization Strategy

**Recommended Approach**: Sequential

Execute testing phases in order:
1. End-to-end scan testing
2. CSV schema validation
3. Calculation accuracy testing
4. Feature verification testing
5. Performance regression testing
6. Manual spot-checks
7. Test results documentation

**Rationale**:
- Task marked `parallel: false`
- Final validation gate for epic
- Sequential flow ensures thoroughness
- Each phase builds on previous results
- Documentation requires complete context
- Quality and accuracy more important than speed

## Expected Timeline

**Sequential execution**:
- Phase 1: 1h (end-to-end scans)
- Phase 2: 1h (CSV validation)
- Phase 3: 1-1.5h (calculation accuracy)
- Phase 4: 1h (feature verification)
- Phase 5: 30m-1h (performance testing)
- Phase 6: 30m-1h (manual spot-checks)
- Phase 7: 30m (documentation)
- **Total wall time**: 5-7 hours

**Note**: Estimate includes API wait times for scanner execution.

## Notes

**Critical Corrections Needed**:
1. **Column count**: Task says "32 columns" but actual is **39 columns** (per #24)
2. All CSV validation must check for 39 columns
3. Update task acceptance criteria after validation

**Test Environment Requirements**:
- TastyTrade API credentials (TT_USERNAME, TT_PASSWORD)
- Production environment (sandbox has limited data)
- Internet connectivity for API calls
- Sufficient API rate limits

**Validation Success Criteria**:
1. Scanner completes without errors
2. CSV has exactly 39 columns in correct order
3. ATM strikes within ±5Δ of 0.50 (95%+ accuracy)
4. Hand-calculated FF matches scanner (±0.0001 tolerance)
5. Volume filter working correctly
6. Greeks IV used as primary source
7. Edge cases handled gracefully
8. Performance acceptable (no obvious regressions)
9. Manual spot-checks confirm accuracy

**Expected Findings**:
- ATM delta accuracy should be high (50Δ target implemented in #28)
- min_ff filtering should show conservative double calendar selection (#26)
- Greeks IV should be primary source (99%+ of cases, per #29)
- Volume filtering should work cleanly (#32)
- CSV schema should match v2.2 spec exactly (#24)

**Potential Issues to Watch For**:
- API timeouts during Greeks snapshot
- Missing volume data for some symbols
- Edge cases with illiquid symbols
- Column count mismatch if documentation incorrect
- Performance issues with large symbol lists

**v2.1 vs v2.2 Comparison** (cannot perform without v2.1 baseline):
- Task mentions comparing trade counts (5-15% change expected)
- Without v2.1 branch/tag, can only document v2.2 behavior
- Focus on validating v2.2 implementation correctness
- Document known differences from requirements:
  - ATM: Single atm_ff (simpler)
  - Double: min_ff filtering (conservative)
  - Strikes: 50Δ for ATM (more accurate)

## Test Documentation Template

```markdown
# v2.2 Integration Test Results

**Test Date**: [timestamp]
**Branch**: epic/core-calc-corrections
**Commit**: [hash]
**Tester**: AI Agent (general-purpose)

## Test Environment
- TastyTrade: Production API
- Python: [version]
- OS: [platform]

## Test Execution Summary

### Phase 1: End-to-End Scan ✅/❌
- Symbols tested: SPY, QQQ, AAPL, TSLA, NVDA
- Structures: ATM + Double
- Result: [PASS/FAIL]
- Issues: [none/list]

### Phase 2: CSV Schema Validation ✅/❌
- Expected columns: 39
- Actual columns: [count]
- Column order: [correct/incorrect]
- Result: [PASS/FAIL]

### Phase 3: Calculation Accuracy ✅/❌
- ATM delta accuracy: [%] within ±5Δ
- Hand-calc comparison: [results]
- Result: [PASS/FAIL]

### Phase 4: Feature Verification ✅/❌
- Volume filter: [PASS/FAIL]
- IV source: [PASS/FAIL]
- Edge cases: [PASS/FAIL]
- Result: [PASS/FAIL]

### Phase 5: Performance Testing ✅/❌
- 10 symbols: [time]
- 50 symbols: [time]
- 100 symbols: [time]
- Result: [PASS/FAIL]

### Phase 6: Manual Spot-Checks ✅/❌
- Opportunities validated: 5
- Accuracy: [results]
- Result: [PASS/FAIL]

## Overall Assessment
- **Status**: [READY TO MERGE / NEEDS FIXES]
- **Confidence**: [HIGH/MEDIUM/LOW]
- **Issues Found**: [count]
- **Recommendation**: [merge / fix and retest]

## Detailed Findings
[Detailed results from each phase]
```

## Recommendation

**Execute sequentially** through all 7 testing phases. This is the final validation gate for the epic - thoroughness and accuracy are paramount.

Sequential testing ensures:
- Complete validation coverage
- Clear results documentation
- High confidence in v2.2 quality
- No missed integration issues
- Proper validation before merge

This task is about quality assurance, not speed. Take the time to validate properly.
