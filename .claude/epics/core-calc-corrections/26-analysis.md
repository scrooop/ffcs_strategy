# Issue #26 Analysis: Update Double Calendar Gating (Min-Gate)

## Overview
Change double calendar gating from average-gate to min-gate. Both wings (call and put) must independently meet FF threshold for opportunity to qualify.

## Work Streams

### Stream A: Add min_ff Calculation
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Add `min_ff = min(call_ff, put_ff)` computation for double structure
- Insert after call_ff and put_ff calculations (scan loop, ~lines 700-900)
- Store min_ff alongside call_ff, put_ff, combined_ff
- Ensure calculation only for structure="double"

**Estimated Time:** 30 minutes

### Stream B: Update Gating Logic
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Change filter condition from `combined_ff >= threshold` to `min_ff >= threshold`
- Verify both wings independently pass threshold
- Retain combined_ff calculation for reference/CSV output
- Update logging to reflect min-gate logic

**Estimated Time:** 45 minutes

### Stream C: CSV Schema Update
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Add `min_ff` column to CSV header (position TBD, likely after combined_ff)
- Update row construction to include min_ff value
- For structure="atm-call": min_ff = empty or same as combined_ff
- For structure="double": min_ff = min(call_ff, put_ff)
- Update CSV column count documentation

**Estimated Time:** 30 minutes

### Stream D: Update Sorting Logic
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Change sort key for double calendars: primary by min_ff descending
- Secondary sort by combined_ff (for tie-breaking)
- Keep ATM sorting unchanged (by combined_ff)
- Verify results list properly sorted before CSV write

**Estimated Time:** 30 minutes

### Stream E: Unit Tests
**File Pattern:** `tests/test_ff_calculations.py`
**Work:**
- Add test for min_ff calculation: `min(0.25, 0.30) = 0.25`
- Add test for min-gate filtering logic
- Test edge cases: equal FFs, one wing below threshold
- Verify ATM structure unaffected

**Estimated Time:** 1 hour

## Execution Strategy

**Sequential execution within single agent** - All streams tightly coupled:
1. Add min_ff calculation (Stream A)
2. Update gating logic (Stream B)
3. Update CSV schema (Stream C)
4. Update sorting logic (Stream D)
5. Add unit tests (Stream E)

## File Locations

- **Main file:** `scripts/ff_tastytrade_scanner.py`
- **Test file:** `tests/test_ff_calculations.py` (extend existing)

## Success Criteria

- min_ff calculation added for double structure
- Gating uses min_ff instead of combined_ff
- CSV includes min_ff column
- Sorting by min_ff (primary), combined_ff (secondary)
- Unit tests passing
- No breaking changes to ATM structure

## Dependencies

- Depends on #23 (validate_ff_inputs) ✅ COMPLETE
- Depends on #25 (skip tracking) ✅ COMPLETE
- **Parallel with:** #28, #29, #32

## Coordination Notes

- **Conflicts with:** #24 (CSV schema) - coordinate column order
- **Safe to parallelize:** Does NOT conflict with #28, #29, #32
- All changes isolated to double calendar branch of scan loop

## Key Implementation Details

**Formula:**
```python
# Current (wrong):
combined_ff = (call_ff + put_ff) / 2
if combined_ff >= threshold:
    include()

# New (correct):
min_ff = min(call_ff, put_ff)
combined_ff = (call_ff + put_ff) / 2  # keep for reference
if min_ff >= threshold:
    include()
```

**CSV Column Addition:**
- Insert `min_ff` after `combined_ff` column
- ATM rows: leave empty or set to combined_ff value
- Double rows: populate with min(call_ff, put_ff)

**Sorting:**
```python
# Doubles sort by min_ff descending (primary), combined_ff (secondary)
doubles_sorted = sorted(doubles, key=lambda x: (x['min_ff'], x['combined_ff']), reverse=True)
```

## Testing

- Manual testing: Run scanner with double structure
- Verify filtering uses min_ff threshold
- Check CSV output includes min_ff column
- Verify sorting by min_ff
- Confirm both wings must pass threshold independently
