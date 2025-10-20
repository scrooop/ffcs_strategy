---
name: core-calc-corrections
description: Align FFCS scanner calculations with strategy transcript - fix ATM anchor, FF gating, wing-exact doubles, IV sources, and liquidity filters
status: backlog
created: 2025-10-20T03:42:50Z
---

# PRD: Core Calculation Corrections for FFCS Scanner

## Executive Summary

The Forward Factor Calendar Spread (FFCS) scanner has several calculation and filtering misalignments with the original strategy methodology from the transcript. These misalignments affect trade selection accuracy, particularly near threshold boundaries and for double calendar structures. This PRD defines the corrections needed to bring the scanner into full compliance with the strategy's deterministic rules for ATM anchoring, FF computation, wing-exact double calendars, IV source handling, and liquidity filtering.

**Impact:** High-priority corrections that affect entry signal accuracy and cannot be fixed via threshold adjustments alone.

## Problem Statement

### What problem are we solving?

The current scanner implementation deviates from the strategy's calculation methodology in five critical areas:

1. **ATM anchor selection:** Uses "strike closest to spot" instead of "≈50Δ call strike"
2. **ATM FF gating:** Computes two FFs (call + put) and filters on their average instead of using a single ATM measure
3. **Double calendar gating:** Uses average(FF_call, FF_put) instead of min(FF_call, FF_put)
4. **IV source handling:** Uses expiration-level ex-earn IV for doubles (collapses wing skew) instead of strike-level IV with proper fallback
5. **Liquidity filtering:** Uses tastytrade liquidity_rating instead of the strategy's "≥10k avg options volume/day" rule

### Why is this important now?

- **Threshold sensitivity:** Averaging FFs can flip marginal pass/fail decisions near thresholds (FF ≥ 0.20-0.23)
- **Wing skew masking:** Expiration-level IV substitutions remove critical wing skew information for double calendars
- **Strategy fidelity:** Current implementation can generate trade signals that don't match the strategy's selection criteria
- **Threshold calibration:** Cannot reliably adjust thresholds when the underlying calculation and gating logic differs from the strategy

## User Stories

### Primary User Persona: Options Trader (Strategy Implementer)

**User Story 1: ATM Calendar Selection**
- **As a** trader running daily ATM calendar scans
- **I want** the scanner to use the 50Δ call strike as the ATM anchor
- **So that** my FF calculations match the strategy's intended ATM reference point
- **Acceptance Criteria:**
  - [ ] ATM strike selection finds the strike with delta closest to 0.50 (call delta)
  - [ ] If no strike within ±0.10Δ of 0.50, use fallback to strike nearest spot
  - [ ] Single FF computed from chosen ATM IV (not averaged from call + put FFs)
  - [ ] CSV output includes `atm_delta` column showing actual delta of selected strike

**User Story 2: Double Calendar Min-Gate**
- **As a** trader scanning double calendar opportunities
- **I want** the scanner to require BOTH wings to meet the FF threshold independently
- **So that** I don't enter trades where one wing is below threshold (hidden in averaging)
- **Acceptance Criteria:**
  - [ ] Compute FF_call at +35Δ call strike (same strike T1/T2)
  - [ ] Compute FF_put at -35Δ put strike (same strike T1/T2)
  - [ ] Trade passes only if `min(FF_call, FF_put) >= threshold`
  - [ ] CSV output shows `min_ff` column = min(FF_call, FF_put) for sorting/filtering
  - [ ] `combined_ff` retained for reference but NOT used for gating

**User Story 3: Strike-Level IV with Fallback**
- **As a** trader scanning symbols during earnings season
- **I want** the scanner to use strike-level ex-earn IV when available, with graceful fallback to strike-level regular IV
- **So that** I get accurate wing-specific FF calculations and clear visibility into IV data sources
- **Acceptance Criteria:**
  - [ ] For doubles, attempt to fetch strike-level ex-earn IV for each wing
  - [ ] If ex-earn unavailable, fallback to strike-level Greeks IV (do NOT skip the symbol)
  - [ ] CSV output includes `iv_source_call_front`, `iv_source_call_back`, `iv_source_put_front`, `iv_source_put_back` columns
  - [ ] Values: `exearn_strike`, `fallback_regular` (not `xearn` or `greeks`)
  - [ ] No expiration-level IV substitutions that collapse wing skew

**User Story 4: Volume-Based Liquidity Filter**
- **As a** trader filtering for liquid names
- **I want** the scanner to enforce the strategy's "≥10k avg options volume/day" rule
- **So that** my filtered results match the strategy's liquidity criteria
- **Acceptance Criteria:**
  - [ ] Fetch 20-day average options volume for each symbol
  - [ ] Skip symbols with `avg_options_volume_20d < 10000`
  - [ ] Remove dependency on tastytrade `liquidity_rating`
  - [ ] CSV output includes `avg_options_volume_20d` column
  - [ ] CLI flag: `--min-avg-volume` (default: 10000)

**User Story 5: Edge Case Handling**
- **As a** trader running scans on diverse symbols
- **I want** the scanner to gracefully handle missing data and invalid calculations
- **So that** I get clean results without crashes or incorrect FF values
- **Acceptance Criteria:**
  - [ ] Skip calculation if `IV_back^2 * T2 <= IV_front^2 * T1` (non-positive forward variance)
  - [ ] Skip symbol if any required IV/Greeks data missing after timeout
  - [ ] Skip if expiration mismatch (requested DTE vs actual expiration beyond tolerance)
  - [ ] Log warning with reason for each skip (debug mode)
  - [ ] CSV output includes `skip_reason` column when applicable

## Requirements

### Functional Requirements

#### FR1: ATM Strike Selection (50Δ Anchor)
- **Primary method:** Find strike with call delta closest to 0.50
- **Fallback:** If no strike within ±0.10Δ of 0.50, use strike nearest to spot
- **Implementation:**
  ```python
  def pick_atm_strike(exp_obj, spot, greeks_data, tolerance=0.10):
      # Find strike with delta closest to 0.50
      # Fallback to strike nearest spot if no deltas within tolerance
      # Return (strike, delta, call_greeks_symbol, put_greeks_symbol)
  ```
- **Output:** Add `atm_delta` column to CSV showing actual delta of selected ATM strike

#### FR2: ATM Single-FF Computation
- **Remove:** Separate call_ff and put_ff for ATM calendars
- **Add:** Single `atm_ff` computed from chosen ATM IV
- **ATM IV source priority:**
  1. Strike-level ex-earn IV (if available)
  2. Strike-level Greeks IV (fallback)
- **Gating:** Filter on `atm_ff >= threshold` (not combined_ff)
- **CSV columns (ATM):**
  - `atm_ff` (primary FF for filtering)
  - `atm_iv_front`, `atm_iv_back`, `atm_fwd_iv`
  - `atm_iv_source_front`, `atm_iv_source_back` (`exearn_strike` or `fallback_regular`)

#### FR3: Wing-Exact FF for Double Calendars
- **Call wing:**
  - Find strike with delta closest to +0.35 (within `--delta-tolerance`, default ±0.05)
  - Use SAME strike for front and back expirations
  - Compute `FF_call` from call wing IVs
- **Put wing:**
  - Find strike with delta closest to -0.35 (within `--delta-tolerance`, default ±0.05)
  - Use SAME strike for front and back expirations
  - Compute `FF_put` from put wing IVs
- **Gating rule:**
  - Trade passes only if `min(FF_call, FF_put) >= threshold`
  - Both wings must independently meet threshold
- **CSV columns (doubles):**
  - `call_ff`, `put_ff` (individual wing FFs)
  - `min_ff` = min(call_ff, put_ff) (primary sorting/filtering metric)
  - `combined_ff` = avg(call_ff, put_ff) (retained for reference, NOT for gating)

#### FR4: Strike-Level IV with Fallback (Doubles)
- **Primary:** Attempt strike-level ex-earn IV for each wing (call_front, call_back, put_front, put_back)
- **Fallback:** If ex-earn unavailable, use strike-level Greeks IV
- **Prohibited:** No expiration-level IV substitutions
- **Source tracking:**
  - `iv_source_call_front`: `exearn_strike` or `fallback_regular`
  - `iv_source_call_back`: `exearn_strike` or `fallback_regular`
  - `iv_source_put_front`: `exearn_strike` or `fallback_regular`
  - `iv_source_put_back`: `exearn_strike` or `fallback_regular`
- **Do NOT skip symbol** if ex-earn unavailable; proceed with fallback and mark source

#### FR5: Volume-Based Liquidity Filter
- **Data source:** Fetch 20-day average options volume from tastytrade Market Metrics API
- **Threshold:** `avg_options_volume_20d >= 10000` (configurable via `--min-avg-volume`)
- **Remove:** All usage of `liquidity_rating`
- **CSV output:** Add `avg_options_volume_20d` column
- **CLI flags:**
  - `--min-avg-volume`: Minimum average options volume (default: 10000)
  - `--skip-liquidity-check`: Disable volume filtering (for testing)

#### FR6: Edge Case Guards
- **Non-positive forward variance:**
  - Skip if `IV_back^2 * T2 <= IV_front^2 * T1`
  - Log warning: "Skipping {symbol} {structure}: non-positive forward variance"
- **Missing IV/Greeks:**
  - Skip if any required IV missing after timeout
  - Log warning: "Skipping {symbol} {structure}: missing IV data for {leg}"
- **Expiration mismatch:**
  - Skip if actual DTE exceeds `--dte-tolerance` from target
  - Log warning: "Skipping {symbol} {structure}: expiration mismatch (target {target_dte}, actual {actual_dte})"
- **CSV skip tracking:**
  - Add `skip_reason` column (empty if not skipped)
  - Values: `nonpositive_fwd_var`, `missing_iv`, `expiry_mismatch`, `volume_too_low`, `delta_not_found`

### Non-Functional Requirements

#### NFR1: Calculation Precision
- **Float precision:** Use Python `float` (double-precision, 64-bit IEEE 754)
- **Display precision:** Format FF, IV values to ≥4 decimal places in CSV output
- **Comparison tolerance:** Use `abs(a - b) < 1e-8` for float equality checks
- **Formula validation:** Unit tests verify forward variance, forward IV, and FF formulas against known test cases

#### NFR2: Performance
- **No degradation:** Calculation changes should not increase runtime
- **Delta-based strike selection:** May require fetching Greeks for all strikes in chain (already done)
- **Volume data:** Batch fetch for all symbols (already done for earnings in v2.1)
- **Target:** Maintain current scan performance (<30s for 1000 symbols with warm cache)

#### NFR3: Backward Compatibility
- **CSV schema changes:**
  - **Breaking changes:** ATM columns restructured (call_ff/put_ff → atm_ff), liquidity_rating removed
  - **Version:** Bump to v2.2
  - **Migration:** Document column mapping for users with existing CSV parsers
- **CLI flags:**
  - **Deprecated:** `--min-liquidity-rating` (replaced by `--min-avg-volume`)
  - **New:** `--min-avg-volume`, `--atm-anchor-method` (for future flexibility)

#### NFR4: Error Handling & Logging
- **Graceful degradation:** Skip symbols with missing data; do not crash
- **Informative logs:** Include symbol, structure, reason for each skip
- **Debug mode:** `--debug` flag shows all skip decisions and IV source selections
- **User feedback:** Summary at end: "Scanned X symbols, Y passed filters, Z skipped (reasons: ...)"

## Success Criteria

### Measurable Outcomes

1. **ATM anchor correctness:**
   - 95%+ of ATM strikes have delta between 0.45-0.55 (±5Δ from 50Δ target)
   - Remaining 5% use fallback to nearest-spot with clear marking

2. **Double calendar gating accuracy:**
   - 100% of double calendar trades have both wings with FF ≥ threshold
   - No trades where one wing has FF < threshold (previously hidden by averaging)

3. **IV source transparency:**
   - 100% of CSV rows include `iv_source` columns with accurate values
   - Clear distinction between `exearn_strike` and `fallback_regular`

4. **Volume filter compliance:**
   - 100% of filtered symbols have `avg_options_volume_20d >= threshold`
   - `liquidity_rating` removed from all code and documentation

5. **Edge case handling:**
   - Zero crashes due to negative forward variance, missing IV, or expiration mismatches
   - All skips logged with clear reasons

### Key Metrics & KPIs

- **Formula validation:** Unit tests pass for all reference test cases
- **Trade count impact:** Document change in trade count before/after corrections (expected: ~5-15% change due to gating differences)
- **Threshold stability:** FF distributions consistent with strategy expectations (validated against transcript examples)
- **Performance:** Scan time ≤ current baseline (no regression)

## Constraints & Assumptions

### Technical Constraints

1. **tastytrade API limitations:**
   - Market Metrics API provides expiration-level ex-earn IV, NOT strike-level
   - May need to fallback to Greeks IV more often than ideal
   - Strike-level ex-earn IV may require different API endpoint (TBD)

2. **Greeks streaming timeout:**
   - Current 3s timeout may need adjustment if fetching deltas for all strikes
   - Balance between completeness and scan speed

3. **Volume data availability:**
   - Assume tastytrade provides 20-day avg options volume in Market Metrics
   - Fallback to daily volume * 20 if avg not available (document assumption)

### Assumptions

1. **50Δ call = ATM proxy:** Strategy transcript uses "ATM" and "50Δ call" interchangeably
2. **Ex-earn IV preference:** When available, strike-level ex-earn IV is more accurate than Greeks IV for FF calculations
3. **Min-gate for doubles:** Both wings must meet threshold for a valid trade setup (conservative risk management)
4. **Volume threshold calibration:** 10k contracts/day is the strategy's stated liquidity minimum

## Out of Scope

### Explicitly NOT building

1. **Alternative ATM definitions:** Straddle mid-IV, weighted IV across strikes (future enhancement)
2. **Wing delta targets other than ±35Δ:** Strategy specifies 35Δ; other deltas require separate research
3. **Dynamic threshold adjustment:** Thresholds remain user-configurable, not auto-adjusted based on market conditions
4. **Strike-level ex-earn IV API:** If not available via current endpoints, use fallback; separate PRD for API enhancement
5. **Historical backtest validation:** Formula corrections are based on transcript alignment; backtest validation is separate effort
6. **Greeks IV interpolation:** Use actual strike IVs; no interpolation for missing strikes

## Dependencies

### External Dependencies

1. **tastytrade API:**
   - Market Metrics API for volume data (verify endpoint availability)
   - Confirm if strike-level ex-earn IV is accessible via existing endpoints
   - Greeks streaming via dxFeed (no changes expected)

2. **Python libraries:**
   - No new dependencies required
   - Current `tastytrade` SDK should support all needed endpoints

### Internal Dependencies

1. **CLAUDE.md documentation:**
   - Update CSV schema section (30 → 31+ columns)
   - Update command examples showing new flags
   - Document v2.1 → v2.2 migration guide

2. **scripts/README_TT.md:**
   - Update usage examples
   - Document new CLI flags
   - Add troubleshooting section for volume data issues

3. **Unit tests:**
   - Add test cases for forward variance, forward IV, FF formulas
   - Test edge cases (negative variance, missing IV, expiry mismatch)
   - Validate ATM delta selection logic
   - Validate min-gate for doubles

## Implementation Plan

### Phase 1: Formula & Edge Case Guards (Core Math)
**Tasks:**
- [ ] Add unit tests for forward variance/IV/FF formulas with reference test cases
- [ ] Implement non-positive forward variance guard
- [ ] Implement missing IV/Greeks guard
- [ ] Implement expiration mismatch guard
- [ ] Add `skip_reason` column to CSV output

**Success criteria:** All edge case guards tested and functional; no crashes on malformed data

### Phase 2: ATM Corrections (50Δ Anchor + Single FF)
**Tasks:**
- [ ] Implement `pick_atm_strike_by_delta()` with 50Δ target and fallback
- [ ] Refactor ATM FF calculation to use single ATM IV source
- [ ] Update CSV schema: `atm_ff`, `atm_iv_front/back/fwd`, `atm_delta`, `atm_iv_source_front/back`
- [ ] Remove call_ff/put_ff/combined_ff columns for ATM structure
- [ ] Update ATM gating logic to filter on `atm_ff >= threshold`

**Success criteria:** ATM calendars use 50Δ strikes (or nearest-spot fallback), single FF gating works correctly

### Phase 3: Double Calendar Wing-Exact FF (Min-Gate)
**Tasks:**
- [ ] Refactor double calendar gating to use `min(FF_call, FF_put) >= threshold`
- [ ] Add `min_ff` column to CSV (primary sorting metric for doubles)
- [ ] Retain `combined_ff` for reference but remove from gating logic
- [ ] Validate both wings independently in filtering logic

**Success criteria:** Double calendar trades require both wings to pass threshold; min_ff correctly computed

### Phase 4: Strike-Level IV with Fallback
**Tasks:**
- [ ] Research tastytrade API for strike-level ex-earn IV (if available)
- [ ] Implement fallback logic: strike ex-earn → strike Greeks IV
- [ ] Update `iv_source` columns: `exearn_strike`, `fallback_regular`
- [ ] Remove expiration-level IV substitutions for doubles
- [ ] Ensure no symbol skipping when ex-earn unavailable

**Success criteria:** IV source tracking accurate; wing skew preserved; no symbol skipping on ex-earn miss

### Phase 5: Volume-Based Liquidity Filter
**Tasks:**
- [ ] Fetch 20-day avg options volume from Market Metrics API
- [ ] Implement volume filter: `avg_options_volume_20d >= threshold`
- [ ] Add `--min-avg-volume` CLI flag (default: 10000)
- [ ] Remove `liquidity_rating` from code and CSV schema
- [ ] Add `avg_options_volume_20d` column to CSV output

**Success criteria:** Volume filter functional; liquidity_rating fully removed; CSV includes volume data

### Phase 6: Documentation & Migration
**Tasks:**
- [ ] Update CLAUDE.md with v2.2 schema (document breaking changes)
- [ ] Update scripts/README_TT.md with new CLI flags and examples
- [ ] Create v2.1 → v2.2 migration guide (CSV column mapping)
- [ ] Add troubleshooting section for common issues (missing volume data, delta not found, etc.)
- [ ] Update version history with calculation corrections summary

**Success criteria:** All documentation accurate and complete; users can migrate existing workflows

## Testing Strategy

### Unit Tests

1. **Formula validation:**
   - Test forward variance calculation with known IV/DTE inputs
   - Test forward IV calculation (sqrt of variance)
   - Test FF formula: `(IV_front - IV_fwd) / IV_fwd`
   - Test edge case: `IV_back^2 * T2 = IV_front^2 * T1` (should skip)

2. **ATM strike selection:**
   - Test 50Δ selection when strikes available
   - Test fallback to nearest-spot when no strikes within tolerance
   - Test delta tolerance boundary conditions

3. **Double calendar min-gate:**
   - Test `min(FF_call, FF_put) >= threshold` logic
   - Test rejection when one wing below threshold
   - Test acceptance when both wings above threshold

4. **IV source fallback:**
   - Test strike-level ex-earn IV usage
   - Test fallback to Greeks IV when ex-earn missing
   - Test `iv_source` column values

### Integration Tests

1. **End-to-end scan:**
   - Run scanner on known symbols with expected results
   - Validate CSV output schema (all required columns present)
   - Validate FF values against hand-calculated reference

2. **Volume filter:**
   - Test symbols above and below 10k volume threshold
   - Validate filtering behavior with `--min-avg-volume` flag
   - Test `--skip-liquidity-check` override

3. **Edge case handling:**
   - Test symbols with missing earnings data
   - Test symbols with missing IV/Greeks
   - Test symbols with non-positive forward variance
   - Validate skip reasons logged correctly

### Validation Tests

1. **Threshold stability:**
   - Compare trade counts before/after corrections
   - Validate FF distributions align with strategy expectations
   - Spot-check high-FF opportunities manually

2. **Performance regression:**
   - Benchmark scan time with 100, 500, 1000 symbols
   - Validate no significant performance degradation vs v2.1

## Risk Assessment

### High Risk

1. **tastytrade API limitations:**
   - **Risk:** Strike-level ex-earn IV not available via current API
   - **Mitigation:** Implement robust fallback to Greeks IV; document limitation
   - **Contingency:** Feature request to tastytrade for strike-level ex-earn endpoint

2. **Volume data availability:**
   - **Risk:** 20-day avg volume not in Market Metrics API
   - **Mitigation:** Fallback to daily volume approximation; document assumption
   - **Contingency:** Manual volume lookup for high-priority symbols

### Medium Risk

1. **Breaking CSV schema changes:**
   - **Risk:** Users with existing CSV parsers may break
   - **Mitigation:** Version bump to v2.2; provide migration guide
   - **Contingency:** Offer `--legacy-csv` flag for v2.1 schema (future enhancement)

2. **Trade count changes:**
   - **Risk:** Corrections may significantly change trade opportunities
   - **Mitigation:** Document expected changes; provide comparison report
   - **Contingency:** Adjust thresholds if trade count drops too low

### Low Risk

1. **Performance regression:**
   - **Risk:** Delta-based strike selection may slow scans
   - **Mitigation:** Greeks already fetched for all strikes; minimal overhead
   - **Contingency:** Optimize Greeks fetching if needed

## Formula Reference (Plain Text)

### Forward Variance
```
V_fwd = (IV_back^2 * T2 - IV_front^2 * T1) / (T2 - T1)

where:
  T1 = DTE_front / 365
  T2 = DTE_back / 365
  IV_front, IV_back in decimal format (e.g., 0.30 for 30%)
```

### Forward IV
```
IV_fwd = sqrt(V_fwd)

Skip calculation if V_fwd <= 0 (non-positive forward variance)
```

### Forward Factor (FF)
```
FF = (IV_front - IV_fwd) / IV_fwd

Properties:
  - FF > 0: front IV is "hot" (backwardation)
  - FF increases monotonically with IV_front (holding IV_back, T1, T2 fixed)
  - Typical trading threshold: FF >= 0.20 to 0.23
```

### Skip Condition (Non-Positive Forward Variance)
```
Skip if: IV_back^2 * T2 <= IV_front^2 * T1

Reason: Would result in V_fwd <= 0, which is invalid (cannot take sqrt)
```

## Appendix: CSV Schema v2.2 (32 Columns)

### Common Columns (All Structures)
1. `timestamp` - ISO 8601 UTC
2. `symbol` - Ticker
3. `structure` - "atm-call" or "double"
4. `spot_price` - Current underlying price
5. `front_dte`, `back_dte` - Days to expiration
6. `front_expiry`, `back_expiry` - YYYY-MM-DD
7. `earnings_conflict` - "yes" or "no"
8. `earnings_date` - YYYY-MM-DD (empty if none)
9. `avg_options_volume_20d` - 20-day avg options volume (NEW)
10. `earnings_source` - "cache", "yahoo", "tastytrade", "none", "skipped"
11. `skip_reason` - Empty if not skipped (NEW)

### ATM Calendar Columns (structure="atm-call")
12. `atm_strike` - Strike with delta ≈ 0.50
13. `atm_delta` - Actual delta of ATM strike (NEW)
14. `atm_ff` - Forward factor (PRIMARY SORTING METRIC, NEW)
15. `atm_iv_front`, `atm_iv_back`, `atm_fwd_iv` - IVs (NEW)
16. `atm_iv_source_front`, `atm_iv_source_back` - "exearn_strike" or "fallback_regular" (NEW)

### Double Calendar Columns (structure="double")
17. `call_strike`, `put_strike` - ±35Δ strikes
18. `call_delta`, `put_delta` - Actual deltas
19. `call_ff`, `put_ff` - Per-wing FFs
20. `min_ff` - min(call_ff, put_ff) (PRIMARY SORTING METRIC, NEW)
21. `combined_ff` - avg(call_ff, put_ff) (reference only, NOT for gating)
22. `call_front_iv`, `call_back_iv`, `call_fwd_iv` - Call wing IVs
23. `put_front_iv`, `put_back_iv`, `put_fwd_iv` - Put wing IVs
24. `iv_source_call_front`, `iv_source_call_back` - "exearn_strike" or "fallback_regular"
25. `iv_source_put_front`, `iv_source_put_back` - "exearn_strike" or "fallback_regular"

### Removed Columns (from v2.1)
- `liquidity_rating` - Replaced by `avg_options_volume_20d`
- `liquidity_value` - Removed (unused)

### Breaking Changes
- ATM structure: `call_ff`, `put_ff`, `combined_ff` → `atm_ff`
- ATM structure: Generic IV columns → `atm_iv_*` columns
- All structures: `liquidity_rating` removed
- Sorting metric changed: `combined_ff` → `atm_ff` (ATM) or `min_ff` (doubles)
