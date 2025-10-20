# Issue #28 Analysis: Refactor ATM Strike Selection (50Δ Anchor)

## Overview
Modify ATM strike selection to use 50Δ call strike (delta-based) instead of strike nearest to spot price. Add fallback to nearest-spot if no strikes within ±0.10Δ tolerance.

## Work Streams

### Stream A: Refactor pick_atm_strike() Function
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Update function signature: `pick_atm_strike(expiration, spot, chain, greeks_map)`
- Add greeks_map parameter (passed from snapshot_greeks() result)
- Primary logic: Find strike with call delta closest to 0.50
- Calculate delta distance: `abs(greeks_map[call_symbol].delta - 0.50)`
- Select strike with minimum delta distance
- Tolerance check: If min distance > 0.10, trigger fallback
- Fallback: Use existing nearest-to-spot logic
- Return tuple: `(strike, actual_delta, call_symbol, put_symbol)`
- Add logging when fallback used

**Estimated Time:** 2 hours

### Stream B: Update Call Sites
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Identify all calls to `pick_atm_strike()` (scan loop, ~2-3 locations)
- Update to pass greeks_map parameter
- Handle new return value with delta
- Store actual_delta for CSV output or logging
- Verify greeks_map availability at call sites
- Add skip logic if greeks_map empty

**Estimated Time:** 1 hour

### Stream C: Constants and Configuration
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Define constant: `ATM_DELTA_TARGET = 0.50`
- Define constant: `ATM_DELTA_TOLERANCE = 0.10`
- Document rationale in comments
- Consider CLI flag for tolerance (optional, low priority)

**Estimated Time:** 15 minutes

### Stream D: Unit Tests
**File Pattern:** `tests/test_ff_calculations.py`
**Work:**
- Test delta selection within tolerance (delta=0.48, 0.52)
- Test exact 50Δ match
- Test fallback when no strikes within ±0.10Δ
- Test empty greeks_map (should skip symbol)
- Mock greeks data with various delta values
- Verify correct strike selected

**Estimated Time:** 1.5 hours

### Stream E: Integration Testing
**File Pattern:** Manual testing
**Work:**
- Run scanner with ATM structure on test symbols
- Verify 50Δ strikes selected (check CSV output)
- Test symbols with wide strike spacing (triggers fallback)
- Check logging output for fallback cases
- Compare old vs new strike selection

**Estimated Time:** 30 minutes

## Execution Strategy

**Sequential execution within single agent** - Function refactoring first, then call sites:
1. Refactor pick_atm_strike() with delta logic (Stream A)
2. Update all call sites (Stream B)
3. Add constants (Stream C)
4. Add unit tests (Stream D)
5. Integration testing (Stream E)

## File Locations

- **Main file:** `scripts/ff_tastytrade_scanner.py`
  - Function location: ~line 242
  - Call sites: scan loop (~lines 700-1000)
- **Test file:** `tests/test_ff_calculations.py`

## Success Criteria

- pick_atm_strike() uses delta-based selection
- Fallback to nearest-spot works when needed
- All call sites updated and working
- Unit tests passing
- Logging added for fallback cases
- No breaking changes (graceful degradation)

## Dependencies

- Depends on #23 (validate_ff_inputs) ✅ COMPLETE
- Depends on #25 (skip tracking) ✅ COMPLETE
- **Conflicts with:** #31 (ATM FF simplification) - must complete before #31
- **Parallel with:** #26, #29, #32

## Coordination Notes

- **MUST complete before #31:** Task #31 depends on this refactored function
- Safe to parallelize with #26, #29, #32
- Greeks map already available from snapshot_greeks()

## Key Implementation Details

**Function Signature Change:**
```python
# Old:
def pick_atm_strike(expiration, spot, chain):
    # Find strike closest to spot
    return strike, call_symbol, put_symbol

# New:
def pick_atm_strike(expiration, spot, chain, greeks_map):
    # Find strike with delta closest to 0.50
    # Fallback to nearest-spot if no strikes within ±0.10Δ
    return strike, actual_delta, call_symbol, put_symbol
```

**Delta Selection Logic:**
```python
ATM_DELTA_TARGET = 0.50
ATM_DELTA_TOLERANCE = 0.10

best_strike = None
min_delta_distance = float('inf')

for strike, symbols in strikes_map.items():
    call_symbol = symbols['call']
    if call_symbol not in greeks_map:
        continue

    call_delta = greeks_map[call_symbol].delta
    delta_distance = abs(call_delta - ATM_DELTA_TARGET)

    if delta_distance < min_delta_distance:
        min_delta_distance = delta_distance
        best_strike = strike
        best_delta = call_delta

if min_delta_distance > ATM_DELTA_TOLERANCE:
    # Fallback to nearest-spot
    logger.debug(f"No 50Δ strike within tolerance, using nearest-spot fallback")
    best_strike = nearest_to_spot(strikes, spot)
    best_delta = None  # or fetch from greeks_map

return best_strike, best_delta, call_symbol, put_symbol
```

**Logging:**
```python
if fallback_used:
    logger.debug(f"{symbol}: ATM fallback to nearest-spot (no 50Δ within ±{ATM_DELTA_TOLERANCE})")
```

## Testing

- Unit tests: Mock greeks_map with test delta values
- Integration: Run scanner and verify strike selection
- Edge cases: Empty greeks_map, wide strike spacing, exact 50Δ match
- Verify CSV output shows correct strikes
