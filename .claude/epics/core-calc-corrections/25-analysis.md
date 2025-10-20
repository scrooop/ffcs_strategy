# Issue #25 Analysis: Implement Skip Tracking & Logging

## Overview
Add observability to the scanner by tracking and logging why symbols are skipped during scans. This provides transparency for filtering decisions and helps debug issues.

## Work Streams

### Stream A: CSV Schema Update
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Add `skip_reason` column to CSV output structure
- Modify CSV writer to include skip_reason field
- Ensure backward compatibility (empty string if not skipped)
- Update CSV header row
- Update any dataclasses/dicts that store scan results

**Estimated Time:** 30-45 minutes

### Stream B: Skip Reason Integration
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Integrate `validate_ff_inputs()` calls at appropriate points
- Define skip reason constants:
  - "nonpositive_fwd_var"
  - "missing_iv"
  - "expiry_mismatch"
  - "volume_too_low"
  - "delta_not_found"
- Add logging statements at each skip point
- Track skip statistics during scan loop

**Estimated Time:** 1 hour

### Stream C: Summary Statistics
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Accumulate skip statistics during scan:
  ```python
  skip_stats = {
      "nonpositive_fwd_var": 0,
      "missing_iv": 0,
      # ... etc
  }
  ```
- Print summary at end of scan:
  ```
  Scanned 100 symbols, 15 passed filters, 85 skipped
    - nonpositive_fwd_var: 23
    - missing_iv: 45
    - expiry_mismatch: 12
    - volume_too_low: 5
  ```
- Add `--debug` flag support for detailed logging

**Estimated Time:** 45 minutes

## Execution Strategy

**Sequential execution within single agent** - All three streams are tightly coupled:
1. Update CSV schema first (Stream A)
2. Integrate skip reasons and logging (Stream B)
3. Add summary statistics (Stream C)

## File Locations

- **Main file:** `scripts/ff_tastytrade_scanner.py`
- **No new files** - all changes in existing scanner

## Success Criteria

- `skip_reason` column added to CSV
- All skip points log with reason
- Summary statistics printed at end
- Debug mode works with `--debug` flag
- No breaking changes to existing CSV output (backward compatible)

## Dependencies

- Depends on #23 (validate_ff_inputs() function) ✅ COMPLETE

## Coordination Notes

This task does NOT conflict with any other tasks.

After completion, this unblocks:
- #26 (Double calendar min-gate) - PARALLEL
- #28 (ATM 50Δ anchor selection)
- #29 (IV source priority inversion) - PARALLEL
- #32 (Volume-based liquidity filter) - PARALLEL

## Integration Points

The `validate_ff_inputs()` function from #23 will be called during:
- Forward IV calculation attempts
- Before computing FF for each expiration pair
- Results captured in skip_reason field

## Testing

- Manual testing: Run scanner with various symbols
- Check CSV output includes skip_reason column
- Verify summary statistics are accurate
- Test --debug flag shows detailed skip logs
