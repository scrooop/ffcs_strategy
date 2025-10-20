# Issue #29 Analysis: Invert IV Source Priority (Greeks Primary)

## Overview
Invert IV source priority to use strike-level Greeks IV as primary (preserves wing skew), with expiration-level ex-earn IV as rare fallback only. Remove confusing CLI flags.

## Work Streams

### Stream A: Invert IV Priority Logic
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Locate IV extraction code in scan loop
- Current: ex-earn IV primary, Greeks IV fallback
- New: Greeks IV primary, ex-earn IV fallback
- Update logic for both ATM and double structures
- For ATM: Use Greeks IV from 50Δ strike (after #28 merge, but code defensively)
- For doubles: Use Greeks IV from ±35Δ strikes (wing-specific)
- Fallback: Use ex-earn IV only when Greeks missing/timeout
- Update iv_source tracking: "greeks" or "exearn_fallback"

**Estimated Time:** 2 hours

### Stream B: Remove CLI Flags
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Remove `--use-xearn-iv` flag from argparse
- Remove `--force-greeks-iv` flag from argparse
- Remove associated logic branches
- Update help text to reflect new default behavior
- Simplify code paths (no more user choice)

**Estimated Time:** 30 minutes

### Stream C: Update IV Source Tracking
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Update iv_source column values:
  - "greeks" (primary, expected default)
  - "exearn_fallback" (rare fallback case)
- Ensure tracking for all 4 columns:
  - iv_source_call_front
  - iv_source_call_back
  - iv_source_put_front
  - iv_source_put_back
- CSV output already has these columns (v2.1)

**Estimated Time:** 30 minutes

### Stream D: Add Fallback Logging
**File Pattern:** `scripts/ff_tastytrade_scanner.py`
**Work:**
- Add logger.warning() when ex-earn fallback used
- Log format: `"{symbol}: Using ex-earn IV fallback (Greeks data missing for {leg})"`
- Track fallback statistics in skip_stats
- Include fallback count in summary output

**Estimated Time:** 45 minutes

### Stream E: Documentation Updates
**File Pattern:** `scripts/README_TT.md`, `CLAUDE.md`
**Work:**
- Update CLAUDE.md: Document new IV priority
- Remove references to `--use-xearn-iv` and `--force-greeks-iv` flags
- Explain rationale: strike-level vs expiration-level IV
- Update examples to remove obsolete flags
- Add note about skew preservation

**Estimated Time:** 1 hour

### Stream F: Integration Tests
**File Pattern:** Manual testing
**Work:**
- Test Greeks IV used by default (verify iv_source="greeks")
- Test fallback when Greeks timeout (set short timeout)
- Test both missing (should skip symbol)
- Verify wing-specific IV for doubles (different strikes, different IVs)
- Check CSV iv_source columns populated correctly

**Estimated Time:** 1 hour

## Execution Strategy

**Sequential execution within single agent** - Priority inversion first, then cleanup:
1. Invert IV priority logic (Stream A)
2. Remove CLI flags (Stream B)
3. Update IV source tracking (Stream C)
4. Add fallback logging (Stream D)
5. Update documentation (Stream E)
6. Integration testing (Stream F)

## File Locations

- **Main file:** `scripts/ff_tastytrade_scanner.py`
  - IV extraction: scan loop (~lines 700-1000)
  - CLI flags: argparse section (~lines 50-150)
- **Docs:** `CLAUDE.md`, `scripts/README_TT.md`

## Success Criteria

- IV priority inverted (Greeks primary, ex-earn fallback)
- CLI flags removed (--use-xearn-iv, --force-greeks-iv)
- iv_source tracking updated
- Fallback logging added
- Documentation updated
- Integration tests verify Greeks used by default
- Edge cases handled: Greeks timeout, ex-earn missing, both missing

## Dependencies

- Depends on #23 (validate_ff_inputs) ✅ COMPLETE
- Depends on #25 (skip tracking) ✅ COMPLETE
- **Independent of:** #28, #31 (different code paths)
- **Parallel with:** #26, #28, #32

## Coordination Notes

- **Conflicts with:** #24 (CSV schema) - coordinate iv_source columns
- Safe to parallelize with #26, #28, #32
- Greeks data already fetched via snapshot_greeks()
- Ex-earn data already fetched via extract_xearn_iv()

## Key Implementation Details

**Current Flow (v2.1 - WRONG):**
```python
# Primary: Try ex-earn IV (expiration-level, collapses skew)
iv = extract_xearn_iv(expiration)
if iv is None or args.force_greeks_iv:
    # Fallback: Use Greeks IV (strike-level, preserves skew)
    iv = greeks_map[strike_symbol].volatility
    iv_source = "greeks"
else:
    iv_source = "xearn"
```

**New Flow (CORRECT):**
```python
# Primary: Use Greeks IV (strike-level, preserves skew)
if strike_symbol in greeks_map and greeks_map[strike_symbol].volatility:
    iv = greeks_map[strike_symbol].volatility
    iv_source = "greeks"
else:
    # Rare fallback: Use ex-earn IV (expiration-level, collapses skew)
    logger.warning(f"{symbol}: Greeks IV missing for {leg}, using ex-earn fallback")
    iv = extract_xearn_iv(expiration)
    if iv is None:
        # Both sources failed, skip symbol
        skip_reason = "missing_iv"
        continue
    iv_source = "exearn_fallback"
```

**Why This Matters:**
- Ex-earn IV: Single value per expiration (collapses volatility smile)
- Greeks IV: Unique value per strike (preserves skew)
- For ±35Δ strikes: Greeks IV may differ by 5-10% from ATM
- Wing-exact FF requires strike-specific IV
- Greeks IV preserves pricing accuracy

**CLI Simplification:**
```python
# REMOVE these flags:
parser.add_argument('--use-xearn-iv', ...)
parser.add_argument('--force-greeks-iv', ...)

# No user choice needed - Greeks always primary
```

**Logging:**
```python
if iv_source == "exearn_fallback":
    logger.warning(f"{symbol} {leg}: Using ex-earn IV fallback (Greeks data missing)")
```

## Testing

- Verify Greeks IV used by default (check CSV iv_source columns)
- Test fallback with Greeks timeout (use --timeout 0.1)
- Test both sources missing (should skip symbol with "missing_iv")
- Verify wing-specific IV for doubles (different IV values for ±35Δ)
- Check fallback statistics in summary output
- Integration: Run full scan and verify no unexpected ex-earn usage
