# Issue #23 Analysis: Add Edge Case Validation & Unit Tests

## Overview
Foundation task that implements validation logic and comprehensive unit tests for FF formulas before any calculation changes.

## Work Streams

### Stream A: Validation Function Implementation
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Create `validate_ff_inputs(iv_front, iv_back, dte_front, dte_back)` function
- Implement non-positive forward variance check: `IV_back^2 * T2 <= IV_front^2 * T1`
- Return skip_reason string if invalid, None if valid
- Add function before existing calculation functions (around line 300)
- Use double-precision float (64-bit)
- Document with docstring including formula and edge cases

**Estimated Time:** 1-2 hours

### Stream B: Unit Test Suite Creation
**File Pattern:** `tests/test_ff_calculations.py` (new file)
**Work:**
- Create test file structure (if tests/ doesn't exist, create it)
- Implement test cases for:
  - Forward variance: `V_fwd = (IV_back^2 * T2 - IV_front^2 * T1) / (T2 - T1)`
  - Forward IV: `IV_fwd = sqrt(V_fwd)`
  - FF formula: `FF = (IV_front - IV_fwd) / IV_fwd`
- Test edge cases:
  - Non-positive variance (IV_back^2 * T2 <= IV_front^2 * T1)
  - Zero DTE
  - Invalid IVs (negative, NaN, infinity)
- Test monotonicity: FF increases as IV_front increases
- Use pytest framework with 1e-8 tolerance for float comparisons
- Document reference values and expected outputs

**Estimated Time:** 3-4 hours

## Execution Strategy

**Sequential execution preferred** - Since this is a foundation task, it's best to:
1. Implement validation function first (Stream A)
2. Then create comprehensive unit tests (Stream B)
3. Tests can validate the validation function itself

## File Locations

- **Main file:** `scripts/ff_tastytrade_scanner.py`
- **Test file:** `tests/test_ff_calculations.py` (to be created)
- **Test runner:** Use pytest (already installed based on project setup)

## Success Criteria

- `validate_ff_inputs()` function exists and works correctly
- Unit test file created with ≥95% formula coverage
- All tests pass
- Tests documented with reference values
- Code follows project style (PEP 8)

## Dependencies

None - this is the first task in the epic.

## Coordination Notes

This task does NOT conflict with any other tasks and must complete before:
- #25 (Skip tracking uses validation function)
- #26, #28, #29, #32 (all depend on #23 + #25)
