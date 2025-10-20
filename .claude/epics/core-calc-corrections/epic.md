---
name: core-calc-corrections
status: completed
created: 2025-10-20T04:32:53Z
updated: 2025-10-20T07:01:58Z
progress: 100%
prd: .claude/prds/core-calc-corrections.md
github: https://github.com/scrooop/ffcs_strategy/issues/22
---

# Epic: Core Calculation Corrections for FFCS Scanner

## Overview

This epic implements five critical calculation corrections to align the FFCS scanner with the strategy transcript methodology. The corrections focus on strike selection (50Δ anchoring), FF computation (single ATM FF, min-gate for doubles), IV source handling (strike-level with fallback), liquidity filtering (volume-based), and edge case guards. These changes affect trade selection accuracy and cannot be compensated by threshold adjustments alone.

**Version bump:** v2.1 → v2.2 (breaking CSV schema changes)

## Architecture Decisions

### 1. Strike Selection Architecture
- **ATM (50Δ anchor):** Modify `pick_atm_strike()` to use delta-based selection instead of spot-based
  - Primary: Find strike with call delta closest to 0.50
  - Fallback: If no strikes within ±0.10Δ, use nearest-to-spot (existing logic)
  - **Leverage existing:** `snapshot_greeks()` already fetches deltas for all strikes
  - **No new API calls:** Delta data already available in Greeks map

- **Doubles (±35Δ wings):** Existing `pick_delta_strike()` already implements correct logic
  - No changes needed to strike selection
  - Only change: Update gating from `avg(FF_call, FF_put)` to `min(FF_call, FF_put)`

### 2. FF Computation & Gating Architecture
- **ATM structure:** Consolidate call_ff/put_ff into single `atm_ff`
  - Remove dual-FF calculation (call + put at same strike produces nearly identical FFs)
  - Use single IV from 50Δ call strike (or average of call/put IV at that strike)
  - **Simplification:** Reduces complexity, aligns with transcript methodology

- **Double structure:** Change gating rule only (formulas unchanged)
  - Keep per-wing FF calculation (call_ff, put_ff)
  - Add `min_ff = min(call_ff, put_ff)` as primary filtering metric
  - Retain `combined_ff = avg(call_ff, put_ff)` for reference only
  - **Leverage existing:** Forward variance/IV formulas already correct

### 3. IV Source Handling
- **Current state:** `extract_xearn_iv()` fetches expiration-level ex-earn IV
  - Problem: Expiration-level IV doesn't capture wing skew for doubles
  - **Solution:** Keep expiration-level ex-earn as fallback, prefer strike-level Greeks IV

- **New priority order:**
  1. Strike-level Greeks IV (primary, already available from `snapshot_greeks()`)
  2. Expiration-level ex-earn IV (fallback only if Greeks missing)
  3. Skip symbol if both unavailable

- **Source tracking:** Update `iv_source` values
  - Change: `xearn` → `exearn_strike` (misleading, since it's expiration-level)
  - Change: `greeks` → `fallback_regular` → **REVERSE THIS**: `greeks` should be primary
  - **Correction:** Greeks IV is MORE accurate for wing-specific FF (preserves skew)

### 4. Liquidity Filter Architecture
- **Replace:** `liquidity_rating` with `avg_options_volume_20d`
- **Data source:** Market Metrics API (same as earnings data)
- **Batch fetch:** Add to existing `fetch_market_metrics()` function
- **Leverage existing:** Earnings fetching already batches all symbols

### 5. Edge Case Guards
- **Add validation layer:** Pre-flight checks before FF computation
  - Non-positive forward variance: `IV_back^2 * T2 <= IV_front^2 * T1`
  - Missing IV/Greeks: Timeout or incomplete data
  - Expiration mismatch: Actual DTE beyond tolerance
- **Skip tracking:** Add `skip_reason` column to CSV output

## Technical Approach

### Core Components (Single File: ff_tastytrade_scanner.py)

All changes are isolated to `scripts/ff_tastytrade_scanner.py`. No new files needed.

#### 1. Strike Selection (Refactor Existing)
**Function:** `pick_atm_strike()` (lines 242-257)
- **Change:** Add delta-based selection with fallback
- **Input:** Add `greeks_map` parameter (delta data already available)
- **Logic:**
  ```python
  # Primary: Find strike with call delta closest to 0.50
  for strike in strikes:
      call_delta = greeks_map[call_symbol][1]  # (iv, delta)
      if abs(call_delta - 0.50) < tolerance:
          # Use this strike
  # Fallback: Existing nearest-to-spot logic
  ```
- **Output:** Add `atm_delta` to return tuple

#### 2. FF Computation (Simplify ATM, Update Doubles)
**ATM structure:**
- **Remove:** Separate call_ff/put_ff calculation (lines in main scan loop)
- **Add:** Single `atm_ff` using IV from 50Δ strike
- **CSV columns:** Replace `call_ff`, `put_ff`, `combined_ff` → `atm_ff`

**Double structure:**
- **Keep:** Existing per-wing FF calculation (correct)
- **Add:** `min_ff = min(call_ff, put_ff)` computation
- **Change:** Gating logic from `combined_ff >= threshold` → `min_ff >= threshold`

#### 3. IV Source Priority (Invert Current Logic)
**Current:** Ex-earn primary, Greeks fallback
**New:** Greeks primary (strike-level), ex-earn fallback (expiration-level, less accurate)

**Rationale:** Strategy requires wing-specific IV for doubles. Expiration-level ex-earn IV collapses skew and defeats the purpose of wing-exact FF.

**Implementation:**
- Remove `--use-xearn-iv` / `--force-greeks-iv` flags (confusing)
- Always use Greeks IV from `snapshot_greeks()` (already strike-specific)
- Only use ex-earn IV if Greeks timeout/missing (rare edge case)
- Update `iv_source` tracking: `greeks` (primary) or `exearn_fallback` (rare)

#### 4. Volume Filter (Add to Batch Fetch)
**Function:** `fetch_market_metrics()` (already exists for earnings)
- **Add:** Extract `avg_options_volume_20d` from market metrics
- **Filter:** Skip symbols with volume < threshold (default 10000)
- **CSV:** Add `avg_options_volume_20d` column
- **Remove:** All `liquidity_rating` references

#### 5. Edge Case Guards (Add Validation Layer)
**New function:** `validate_ff_inputs(iv_front, iv_back, dte_front, dte_back)`
- Check non-positive forward variance before computation
- Return `skip_reason` if invalid, else None

**Integration:** Call before each FF calculation
- Skip symbol if validation fails
- Log warning with reason
- Add `skip_reason` to CSV output

### CSV Schema Changes (v2.2)

**Breaking changes:**
- ATM: `call_ff`, `put_ff`, `combined_ff` → `atm_ff`
- ATM: Add `atm_delta`, `atm_iv_front`, `atm_iv_back`, `atm_fwd_iv`
- Doubles: Add `min_ff` (primary sorting), keep `combined_ff` (reference)
- All: Remove `liquidity_rating`, `liquidity_value`
- All: Add `avg_options_volume_20d`, `skip_reason`
- All: Update `iv_source` values (greeks primary, exearn_fallback rare)

**Column count:** 31 → 32 columns (net +1 after removals)

## Implementation Strategy

### Phased Rollout (Sequential Tasks)

**Phase 1: Foundation (Tasks 1-3)**
- Validation layer, unit tests, edge case guards
- Establishes safety net before touching FF logic

**Phase 2: Core Calculations (Tasks 4-5)**
- ATM 50Δ anchor and single FF
- Double min-gate (gating logic only, formulas unchanged)

**Phase 3: Data Sources (Tasks 6-7)**
- IV source priority inversion (Greeks primary)
- Volume filter (batch fetch + filtering)

**Phase 4: Integration (Tasks 8-9)**
- CSV schema updates and migration
- Documentation updates

**Phase 5: Validation (Task 10)**
- End-to-end testing and verification

### Risk Mitigation

1. **tastytrade API constraints:**
   - Greeks IV already fetched, no new API dependencies
   - Volume data in Market Metrics (verify endpoint, fallback if needed)

2. **Breaking changes:**
   - Version bump to v2.2 (clear signal)
   - Migration guide for CSV parsers
   - Consider `--legacy-csv` flag (future enhancement)

3. **Performance:**
   - No new API calls (Greeks/volume already fetched)
   - Minimal overhead from delta-based selection

### Testing Approach

1. **Unit tests:** Formula validation, edge cases, strike selection
2. **Integration tests:** End-to-end scans with known symbols
3. **Regression tests:** Compare v2.1 vs v2.2 outputs (expected: 5-15% change in trade count)
4. **Performance tests:** Benchmark scan times (no degradation expected)

## Task Breakdown Preview

### Task 1: Add Edge Case Validation & Unit Tests
- Implement `validate_ff_inputs()` with non-positive variance check
- Add unit tests for forward variance/IV/FF formulas
- Test edge cases: negative variance, zero DTE, invalid IVs

### Task 2: Implement Skip Tracking & Logging
- Add `skip_reason` column to CSV schema
- Update logging for skip decisions (debug mode)
- Add summary statistics (scanned, passed, skipped counts)

### Task 3: Refactor ATM Strike Selection (50Δ Anchor)
- Modify `pick_atm_strike()` to use delta-based selection
- Add fallback to nearest-spot if no strikes within ±0.10Δ
- Return `atm_delta` in output tuple
- Add unit tests for delta selection logic

### Task 4: Simplify ATM FF Computation (Single FF)
- Remove separate call_ff/put_ff for ATM structure
- Implement single `atm_ff` using 50Δ strike IV
- Update CSV columns: `atm_ff`, `atm_iv_front/back/fwd`, `atm_delta`
- Update gating logic: `atm_ff >= threshold`

### Task 5: Update Double Calendar Gating (Min-Gate)
- Add `min_ff = min(call_ff, put_ff)` computation
- Change gating: `min_ff >= threshold` (was `combined_ff >= threshold`)
- Keep `combined_ff` for reference only
- Update CSV sorting: primary key = `min_ff` (doubles) or `atm_ff` (ATM)

### Task 6: Invert IV Source Priority (Greeks Primary)
- **CRITICAL DECISION:** Greeks IV is strike-specific (preserves skew), ex-earn is expiration-level (collapses skew)
- Change priority: Greeks IV (primary) → ex-earn IV (fallback only)
- Remove `--use-xearn-iv` / `--force-greeks-iv` flags (confusing, no longer needed)
- Update `iv_source` tracking: `greeks` (primary) or `exearn_fallback` (rare)
- Document: Ex-earn IV is expiration-level and less accurate for wing-specific FF

### Task 7: Implement Volume-Based Liquidity Filter
- Add volume extraction to `fetch_market_metrics()`
- Implement filter: `avg_options_volume_20d >= threshold`
- Add `--min-avg-volume` CLI flag (default: 10000)
- Remove all `liquidity_rating` references from code
- Add `avg_options_volume_20d` column to CSV

### Task 8: Update CSV Schema & Output Logic
- Implement v2.2 CSV schema (32 columns)
- Update all CSV write operations
- Add ATM-specific columns: `atm_ff`, `atm_delta`, `atm_iv_*`
- Add double-specific columns: `min_ff`
- Add common columns: `avg_options_volume_20d`, `skip_reason`
- Remove columns: `liquidity_rating`, `liquidity_value`

### Task 9: Update Documentation (CLAUDE.md, README_TT.md)
- Update CLAUDE.md CSV schema section (31 → 32 columns)
- Document breaking changes (v2.1 → v2.2)
- Create migration guide (column mapping)
- Update command examples with new flags
- Add troubleshooting section (delta not found, volume missing)
- Update version history

### Task 10: Integration Testing & Validation
- End-to-end scan with known symbols (SPY, QQQ, AAPL)
- Compare v2.1 vs v2.2 outputs (trade count, FF values)
- Validate CSV schema (all required columns present)
- Performance regression test (scan times)
- Spot-check high-FF opportunities manually

## Dependencies

### External Dependencies
1. **tastytrade API:**
   - Market Metrics API (earnings, volume data)
   - dxFeed Greeks streaming (no changes)
   - **Assumption:** 20-day avg volume available in metrics API

2. **Python libraries:**
   - No new dependencies (all changes in existing code)

### Internal Dependencies
1. **Documentation files:**
   - `CLAUDE.md` (CSV schema, usage examples)
   - `scripts/README_TT.md` (command reference)

2. **Test infrastructure:**
   - Unit test framework (add new tests)
   - Integration test suite (update with v2.2 expectations)

## Success Criteria (Technical)

### Performance Benchmarks
- **Scan time:** ≤ v2.1 baseline (<30s for 1000 symbols, warm cache)
- **Memory usage:** No significant increase (same data structures)
- **API calls:** No additional calls (reuse existing fetches)

### Quality Gates
1. **Formula correctness:**
   - Unit tests pass for forward variance/IV/FF
   - Edge cases handled (non-positive variance, missing data)

2. **Strike selection accuracy:**
   - 95%+ ATM strikes have delta 0.45-0.55 (±5Δ from 50Δ)
   - Remaining 5% use fallback with clear marking

3. **Gating correctness:**
   - ATM: Filter on single `atm_ff >= threshold`
   - Doubles: Filter on `min_ff >= threshold` (both wings pass)

4. **IV source transparency:**
   - 100% of rows include accurate `iv_source` values
   - Greeks primary, ex-earn fallback only

5. **Volume filter compliance:**
   - 100% of filtered symbols have volume >= threshold
   - `liquidity_rating` fully removed

### Acceptance Criteria
- [ ] All unit tests pass (formulas, edge cases, strike selection)
- [ ] Integration tests pass (end-to-end scans, CSV validation)
- [ ] Performance tests pass (no regression vs v2.1)
- [ ] CSV schema matches v2.2 spec (32 columns, correct values)
- [ ] Documentation updated (CLAUDE.md, README_TT.md, migration guide)
- [ ] Zero crashes on edge cases (negative variance, missing data)

## Estimated Effort

### Overall Timeline
- **Duration:** 2-3 days (full-time equivalent)
- **Task breakdown:**
  - Foundation (Tasks 1-2): 4-6 hours
  - Core calculations (Tasks 3-5): 6-8 hours
  - Data sources (Tasks 6-7): 4-6 hours
  - Integration (Tasks 8-9): 4-6 hours
  - Validation (Task 10): 2-4 hours

### Resource Requirements
- **Engineer:** 1 developer (full-stack Python)
- **Testing:** Manual validation + automated tests
- **Documentation:** Technical writing for migration guide

### Critical Path
1. **Task 1-2:** Edge case validation (blocks all FF changes)
2. **Task 3-4:** ATM 50Δ anchor + single FF (ATM structure changes)
3. **Task 5:** Double min-gate (double structure changes)
4. **Task 8:** CSV schema (integrates all changes)
5. **Task 10:** Validation (final gate before release)

**Parallelization opportunities:**
- Task 6 (IV source) can run in parallel with Tasks 3-5 (FF logic)
- Task 7 (volume filter) can run in parallel with Tasks 3-5
- Task 9 (documentation) can start during Task 8

## Risk Assessment

### High Risk
- **tastytrade API volume data:** Verify 20-day avg available
  - Mitigation: Fallback to daily volume approximation
  - Testing: Check API response structure first

### Medium Risk
- **Breaking CSV changes:** Existing parsers may break
  - Mitigation: Version bump, migration guide, `--legacy-csv` flag (future)

- **Trade count changes:** 5-15% expected due to gating differences
  - Mitigation: Document changes, provide comparison report

### Low Risk
- **Performance regression:** No new API calls expected
  - Mitigation: Benchmark before/after

## Open Questions

1. **Market Metrics API volume field:** Confirm exact field name for 20-day avg options volume
   - **Action:** Test API call with sample symbol before Task 7

2. **Ex-earn IV availability:** How often is strike-level ex-earn IV actually available?
   - **Decision:** Made in architecture - use Greeks (strike-level) as primary since ex-earn is expiration-level
   - **Implication:** Ex-earn becomes rare fallback, not primary source

3. **Legacy CSV support:** Should we offer `--legacy-csv` flag for v2.1 schema?
   - **Decision:** Defer to future enhancement (not in scope)
   - **Rationale:** Breaking changes necessary for correctness, document migration path

## Notes

### Key Simplifications (vs Original PRD Phases)
- **Consolidated tasks:** 6 PRD phases → 10 consolidated tasks
- **Removed unnecessary complexity:** Ex-earn IV research (decision: use Greeks primary)
- **Leveraged existing functionality:** Greeks fetching, batch metrics fetch, delta selection logic
- **Single-file changes:** All modifications in `ff_tastytrade_scanner.py` (no new files)

### Critical Architecture Decision: IV Source Priority
**PRD assumption:** Strike-level ex-earn IV is ideal, fallback to Greeks IV
**Reality:** tastytrade provides expiration-level ex-earn IV (not strike-level)
**Decision:** Invert priority - use Greeks IV (strike-specific) as primary
**Rationale:** Wing-exact FF requires strike-specific IV to capture skew; expiration-level ex-earn defeats this purpose

This decision is documented in Task 6 and affects success criteria (Greeks = primary source).

[38;2;131;148;150m───────┬────────────────────────────────────────────────────────────────────────[0m
       [38;2;131;148;150m│ [0m[1mSTDIN[0m
[38;2;131;148;150m───────┼────────────────────────────────────────────────────────────────────────[0m
[38;2;131;148;150m   1[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m## Tasks Created[0m
[38;2;131;148;150m   2[0m   [38;2;131;148;150m│[0m 
[38;2;131;148;150m   3[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m- [ ] #23 - Add Edge Case Validation & Unit Tests (parallel: false)[0m
[38;2;131;148;150m   4[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m- [ ] #25 - Implement Skip Tracking & Logging (parallel: false)[0m
[38;2;131;148;150m   5[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m- [ ] #28 - Refactor ATM Strike Selection (50Δ Anchor) (parallel: false)[0m
[38;2;131;148;150m   6[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m- [ ] #31 - Simplify ATM FF Computation (Single FF) (parallel: false)[0m
[38;2;131;148;150m   7[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m- [ ] #26 - Update Double Calendar Gating (Min-Gate) (parallel: true)[0m
[38;2;131;148;150m   8[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m- [ ] #29 - Invert IV Source Priority (Greeks Primary) (parallel: true)[0m
[38;2;131;148;150m   9[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m- [ ] #32 - Implement Volume-Based Liquidity Filter (parallel: true)[0m
[38;2;131;148;150m  10[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m- [ ] #24 - Update CSV Schema & Output Logic (parallel: false)[0m
[38;2;131;148;150m  11[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m- [ ] #27 - Update Documentation (CLAUDE.md, README_TT.md) (parallel: false)[0m
[38;2;131;148;150m  12[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m- [ ] #30 - Integration Testing & Validation (parallel: false)[0m
[38;2;131;148;150m  13[0m   [38;2;131;148;150m│[0m 
[38;2;131;148;150m  14[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m**Total tasks:** 10[0m
[38;2;131;148;150m  15[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m**Parallel tasks:** 3 (can be worked on simultaneously)[0m
[38;2;131;148;150m  16[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m**Sequential tasks:** 7 (have dependencies)[0m
[38;2;131;148;150m  17[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m**Estimated total effort:** 38-50 hours (approx. 2-3 days full-time)[0m
[38;2;131;148;150m───────┴────────────────────────────────────────────────────────────────────────[0m
### Task Dependency Graph

```
Foundation Phase:
001 (Validation) → 002 (Skip Tracking)
                     ↓
Core Calculations:   ├→ 003 (ATM 50Δ) → 004 (ATM Single FF)
                     ├→ 005 (Double Min-Gate) ──┐
Data Sources:        ├→ 006 (IV Priority) ──────┤
                     └→ 007 (Volume Filter) ─────┤
                                                 ↓
Integration:                            008 (CSV Schema) → 009 (Docs)
                                                            ↓
Validation:                                              010 (Testing)
```

### Parallelization Strategy

**Concurrent work streams:**
- After Task 002 completes, three parallel tracks can begin:
  1. **ATM track:** Tasks 003 → 004 (sequential)
  2. **Double track:** Task 005 (independent)
  3. **Data sources track:** Tasks 006, 007 (independent)

**Critical path:** 001 → 002 → 003 → 004 → 008 → 009 → 010 (7 tasks)
**Shortest timeline:** ~24-32 hours with optimal parallelization
