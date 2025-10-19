---
name: ff-scanner-v2
description: Enhanced FF scanner with earnings filtering, liquidity screening, X-earn IV support, and double calendar structure scanning
status: backlog
created: 2025-10-19T08:09:47Z
---

# PRD: FF Scanner v2.0

## Executive Summary

FF Scanner v2.0 enhances the existing Forward Factor calendar spread scanner with four critical features that align with the research methodology from the original YouTube transcript: earnings date filtering, liquidity screening, X-earn IV support, and double calendar structure scanning (±35Δ). The primary goal is to increase trade quality by reducing false positives, discovering higher-probability opportunities, and automating manual verification steps currently performed on the tastytrade platform.

**Key Value Proposition**: Transform the scanner from a broad opportunity finder into a precision instrument that outputs only high-quality, tradable calendar spread opportunities that match the exact research criteria used in the original backtest.

## Problem Statement

### Current Pain Points

1. **False Positives from Earnings Risk**: The current scanner identifies opportunities that span earnings events, which violates the strategy's core assumption of stable forward volatility. Traders must manually check earnings calendars on tastytrade, wasting time and risking oversight.

2. **Illiquid Positions**: Scanner returns results for thinly-traded options that cannot be executed at reasonable bid-ask spreads. The original research required "20-day average option volume above 10,000 contracts per day," but current scanner has no liquidity filters.

3. **IV Data Mismatch**: The research used "X-earn IV" (earnings-removed implied volatility), but the current scanner uses raw dxFeed Greeks IV which includes earnings premium. This creates systematic bias in Forward Factor calculations around earnings cycles.

4. **Missing Double Calendar Opportunities**: The research showed double calendars (±35Δ call + put calendars) have higher win rates than ATM call calendars, but current scanner only detects ATM structures. Traders are blind to potentially superior setups.

5. **Manual Workflow Overhead**: After running scanner, trader must:
   - Check each symbol for earnings dates
   - Verify liquidity ratings on tastytrade platform
   - Manually scan for double calendar strikes
   - Filter results in spreadsheet

### Why This Matters Now

- **Strategy Fidelity**: Current scanner doesn't match the research methodology, creating uncertainty about whether backtested edge will translate to live trading
- **Time Efficiency**: Pre-market scanning window is limited; manual verification steps consume valuable decision-making time
- **Opportunity Cost**: Missing double calendar setups means leaving profitable trades on the table
- **Risk Management**: Earnings surprises during position hold period can destroy calendar spreads; automated filtering is critical for capital preservation

## User Stories

### Primary Persona: Active Options Trader (You)

**Background**: Experienced trader implementing Forward Factor calendar spread strategy based on quantitative research. Trades 10-20 positions per month across liquid underlyings (SPY, QQQ, major tech stocks). Scans daily before market open and opportunistically intraday.

#### User Journey 1: Daily Pre-Market Scan

**Current State (v1.0)**:
1. Run scanner: `python ff_tastytrade_scanner.py --tickers SPY QQQ AAPL TSLA NVDA META AMZN --pairs 30-60 30-90 60-90 --min-ff 0.20`
2. Get 15-20 raw opportunities
3. Open tastytrade platform → check each symbol's earnings calendar
4. Check liquidity rating for each symbol
5. Manually calculate if double calendar applies
6. Filter results in spreadsheet → down to 3-5 tradable opportunities
7. **Time spent: 20-30 minutes**

**Desired State (v2.0)**:
1. Run scanner: `python ff_tastytrade_scanner.py --tickers SPY QQQ AAPL TSLA NVDA META AMZN --pairs 30-60 30-90 60-90 --min-ff 0.23 --skip-earnings --min-liquidity-rating 3 --structure both --csv-out scan.csv`
2. Get 3-5 pre-filtered, high-quality opportunities (both ATM and double calendar)
3. Review CSV → assess FF rankings → select top 2-3 for execution
4. **Time spent: 5-10 minutes**

**Acceptance Criteria**:
- Scanner automatically excludes earnings conflicts
- Only liquid underlyings shown (liquidity rating ≥ 3)
- Both ATM and double calendar opportunities displayed
- CSV output ready for further analysis

#### User Journey 2: Intraday Opportunity Monitoring

**Current State (v1.0)**:
1. Market moves → re-run scanner manually
2. Get mix of old + new opportunities
3. No way to filter "what changed since morning"

**Desired State (v2.0)**:
1. Market moves → re-run scanner
2. Compare new CSV to morning CSV (external diff tool)
3. Identify new opportunities that crossed FF threshold
4. Act on intraday volatility spikes

**Acceptance Criteria**:
- Scanner produces consistent CSV format for time-series analysis
- Timestamps in output allow "delta" comparison

#### User Journey 3: Structure-Specific Scanning

**As a trader, I want to scan only ATM call calendars OR only double calendars, so that I can focus on specific trade structures based on market conditions.**

**Scenario A: High IV Environment → ATM Focus**
```bash
python ff_tastytrade_scanner.py --tickers SPY QQQ --pairs 30-60 --structure atm-call --min-ff 0.23
```

**Scenario B: Low IV Environment → Double Calendar Focus**
```bash
python ff_tastytrade_scanner.py --tickers SPY QQQ --pairs 60-90 --structure double --min-ff 0.20
```

**Acceptance Criteria**:
- `--structure` flag supports: `atm-call`, `double`, `both` (default: `both`)
- Output clearly indicates which structure each row represents

#### User Journey 4: Investigating Filtered Opportunities (Learning Mode)

**As a trader, I want to see WHY opportunities were filtered out, so that I can validate the scanner logic and learn about market conditions.**

**Example**: "Why didn't AAPL show up today?"

```bash
python ff_tastytrade_scanner.py --tickers AAPL --pairs 30-60 --show-earnings-conflicts
```

**Output**:
```
[FILTERED] AAPL 30-60: Earnings on 2025-11-01 conflicts with back expiry 2025-11-05
           FF would have been: 0.28 (Strong opportunity, but earnings risk)
           Liquidity Rating: 5 (Excellent)
```

**Acceptance Criteria**:
- `--show-earnings-conflicts` flag reveals filtered positions
- Output shows what the FF would have been + reason for filtering
- Helps trader learn when to potentially override filters (e.g., trading ex-earnings IV)

## Requirements

### Functional Requirements

#### FR1: Earnings Date Filtering

**FR1.1**: Scanner SHALL fetch next earnings date for each symbol via `tastytrade.metrics.get_market_metrics()` API before processing option chains.

**FR1.2**: Scanner SHALL skip any symbol where earnings date falls between today and back expiration (inclusive), unless `--allow-earnings` flag is set.

**FR1.3**: Scanner SHALL add `earnings_date` and `earnings_conflict` columns to CSV output.

**FR1.4**: Scanner SHALL print warning when skipping symbol due to earnings: `[WARN] Skipping {symbol}: earnings on {date} conflicts with {back_exp}`.

**FR1.5**: Scanner SHALL support `--show-earnings-conflicts` flag to display filtered positions with their hypothetical FF values.

**FR1.6**: Default behavior: `--skip-earnings` (filter out earnings conflicts). User can override with `--allow-earnings`.

#### FR2: Liquidity Screening

**FR2.1**: Scanner SHALL fetch liquidity metrics for each symbol via `tastytrade.metrics.get_market_metrics()` API (same call as earnings data, no additional API overhead).

**FR2.2**: Scanner SHALL filter out symbols with `liquidity_rating < min_threshold` (default threshold: 3 on 0-5 scale).

**FR2.3**: Scanner SHALL support `--min-liquidity-rating N` flag (0-5, default: 3).

**FR2.4**: Scanner SHALL support `--skip-liquidity-check` flag to disable liquidity filtering.

**FR2.5**: Scanner SHALL add `liquidity_rating` and `liquidity_value` columns to CSV output.

**FR2.6**: Scanner SHALL print info when filtering: `[INFO] {symbol}: liquidity_rating={rating} < {min_threshold}, skipping`.

#### FR3: X-earn IV Support

**FR3.1**: Scanner SHALL attempt to fetch X-earn IV from `MarketMetricInfo.option_expiration_implied_volatilities` for target expirations.

**FR3.2**: If X-earn IV is available for an expiration, scanner SHALL use it in Forward Factor calculation instead of dxFeed Greeks IV.

**FR3.3**: If X-earn IV is unavailable, scanner SHALL fall back to dxFeed Greeks IV (current behavior).

**FR3.4**: Scanner SHALL support `--use-xearn-iv` flag to enable X-earn IV mode (default: enabled).

**FR3.5**: Scanner SHALL support `--force-greeks-iv` flag to always use dxFeed Greeks IV (current behavior).

**FR3.6**: Scanner SHALL add `iv_source` column to CSV output indicating "xearn" or "greeks" for each leg.

**FR3.7**: Scanner SHALL log warning if X-earn IV is not available: `[WARN] {symbol}: X-earn IV unavailable for {exp_date}, using Greeks IV`.

**Uncertainty Caveat**: FR3 assumes `OptionExpirationImpliedVolatility.implied_volatility` represents X-earn IV. If testing reveals this is regular IV, FR3 will be deferred to v2.1 pending API clarification.

#### FR4: Double Calendar Structure Scanning

**FR4.1**: Scanner SHALL support scanning for double calendar structures (±35Δ call and put calendars).

**FR4.2**: Scanner SHALL find strikes with delta closest to +0.35 (calls) and -0.35 (puts) within ±0.05 tolerance.

**FR4.3**: Scanner SHALL fetch dxFeed Greeks (including delta) for all strikes to enable delta-based strike selection.

**FR4.4**: Scanner SHALL compute separate Forward Factors for:
- Call calendar: front +35Δ call / back +35Δ call
- Put calendar: front -35Δ put / back -35Δ put

**FR4.5**: Scanner SHALL support `--structure` flag with values:
- `atm-call`: ATM call calendar only (current behavior)
- `double`: Double calendar only (±35Δ)
- `both`: Scan both structures (default)

**FR4.6**: Scanner SHALL support `--delta-tolerance` flag (default: 0.05) for acceptable delta deviation.

**FR4.7**: Scanner output SHALL include columns:
- `structure`: "atm-call" or "double"
- For double calendars: `call_strike`, `put_strike`, `call_delta`, `put_delta`, `call_ff`, `put_ff`, `combined_ff`

**FR4.8**: For double calendars, `combined_ff` SHALL be arithmetic mean of `call_ff` and `put_ff`.

**FR4.9**: Scanner SHALL apply `--min-ff` threshold to `combined_ff` for double calendars.

#### FR5: Enhanced CSV Output

**FR5.1**: Scanner SHALL produce CSV output with ALL columns:
```
timestamp, symbol, structure, front_dte, back_dte, front_expiry, back_expiry,
atm_strike, call_strike, put_strike, call_delta, put_delta,
front_iv, back_iv, fwd_iv, ff, call_ff, put_ff, combined_ff,
earnings_date, earnings_conflict, liquidity_rating, liquidity_value,
iv_source_front, iv_source_back
```

**FR5.2**: Columns not applicable to structure SHALL be empty (e.g., `call_strike` for ATM calendars).

**FR5.3**: `timestamp` SHALL use ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ` (UTC).

**FR5.4**: CSV SHALL be sorted by `combined_ff` (or `ff` for ATM) descending (highest opportunities first).

### Non-Functional Requirements

#### NFR1: Performance

**NFR1.1**: Scanner SHALL complete 10-symbol scan in ≤ 30 seconds (current: ~20 seconds).

**NFR1.2**: Scanner SHALL complete 20-symbol scan in ≤ 60 seconds.

**NFR1.3**: API calls SHALL be batched where possible:
- `get_market_metrics()` for ALL symbols in single call (earnings + liquidity)
- `snapshot_greeks()` per symbol (unavoidable due to strike-level data)

#### NFR2: Reliability

**NFR2.1**: Scanner SHALL handle partial data gracefully:
- If earnings date unavailable → log warning, proceed without filtering
- If liquidity rating unavailable → log warning, proceed without filtering
- If Greeks data times out → skip that symbol, continue scan

**NFR2.2**: Scanner SHALL validate all API responses for None/null values before calculations.

**NFR2.3**: Scanner SHALL not crash if single symbol fails; SHALL log error and continue.

#### NFR3: Usability

**NFR3.1**: All new CLI flags SHALL have sensible defaults matching research methodology.

**NFR3.2**: Scanner help text (`--help`) SHALL document all flags with examples.

**NFR3.3**: Console output SHALL clearly indicate filtering actions with `[INFO]`, `[WARN]`, `[FILTERED]` prefixes.

**NFR3.4**: CSV column headers SHALL be self-documenting (no abbreviations requiring external docs).

#### NFR4: Maintainability

**NFR4.1**: Code SHALL separate concerns:
- Data fetching (tastytrade API calls)
- Business logic (FF calculation, filtering)
- Output formatting (CSV generation)

**NFR4.2**: All new functions SHALL include docstrings with parameter types and return values.

**NFR4.3**: Magic numbers (thresholds, tolerances) SHALL be named constants at module level.

#### NFR5: Compatibility

**NFR5.1**: Scanner SHALL remain compatible with existing v1.0 CLI flags (backward compatible).

**NFR5.2**: CSV output format SHALL be superset of v1.0 (add columns, don't remove).

**NFR5.3**: Scanner SHALL work with tastytrade SDK v10.1.0+ (current production version).

**NFR5.4**: Scanner SHALL require production tastytrade environment (sandbox has insufficient market data).

## Success Criteria

### Primary Success Metric: Trade Quality Index (TQI)

**Definition**: TQI = (Avg FF of output opportunities) × (% filtered out) × (1 / avg scan time in minutes)

**Target**: TQI ≥ 2.0

**Example Calculation**:
- v1.0: Avg FF = 0.22, 0% filtered, 25 min scan → TQI = 0.22 × 1.0 × (1/25) = 0.0088
- v2.0: Avg FF = 0.28, 70% filtered, 8 min scan → TQI = 0.28 × 1.7 × (1/8) = 0.0595 (6.7x improvement)

### Secondary Success Metrics

**Efficiency Gains**:
- ✅ Pre-market scan time reduced from 20-30 min → 5-10 min (≥50% reduction)
- ✅ Manual verification steps eliminated: 0 manual earnings checks, 0 manual liquidity checks

**Coverage Expansion**:
- ✅ Double calendar opportunities discovered: ≥30% of total opportunities
- ✅ Opportunities per scan (10 symbols): 3-5 high-quality setups (down from 15-20 raw)

**Quality Improvement**:
- ✅ False positives (earnings conflicts): 0% (down from ~20-30%)
- ✅ Illiquid underlyings: 0% (down from ~10-15%)
- ✅ Avg FF of output opportunities: ≥0.25 (up from ~0.21 with --min-ff 0.20)

**Validation Metrics (Post-Launch)**:
- ✅ Actual trade win rate matches backtest expectation (60-70% for double calendars)
- ✅ No positions entered that subsequently hit earnings during hold period
- ✅ All positions achieve fills within 2 standard deviations of mid-price

## Constraints & Assumptions

### Technical Constraints

**TC1**: tastytrade API limitations:
- No direct "20-day avg option volume" metric available → using `liquidity_rating` as proxy
- X-earn IV availability unknown → may need to defer FR3 to v2.1 pending validation

**TC2**: dxFeed Greeks streaming:
- Delta values required for double calendar strike selection
- Timeout-based snapshot collection may miss strikes in fast markets

**TC3**: API rate limits:
- Unknown hard limits on `get_market_metrics()` batch size
- Assume ≤ 50 symbols per call is safe

### Business Constraints

**BC1**: Single-user tool → no multi-user, no authentication beyond tastytrade credentials

**BC2**: Manual order placement → no auto-execution, no position tracking (out of scope for v2.0)

**BC3**: Development effort budget: 15-21 hours total (per implementation plan)

### Assumptions

**A1**: tastytrade production environment will remain accessible with current credentials

**A2**: dxFeed Greeks streaming will continue providing IV and delta data for all liquid symbols

**A3**: User will scan 10-20 symbols per session (not 100+)

**A4**: CSV output format is sufficient for further analysis (no need for JSON, database, etc.)

**A5**: Earnings dates from `get_market_metrics()` are accurate ≥95% of the time

**A6**: Liquidity rating ≥3 correlates with ≥10k contracts/day avg volume (to be validated)

**A7**: User has basic understanding of options Greeks (delta, IV) and calendar spread mechanics

## Out of Scope

### Explicitly NOT Building in v2.0

**OS1**: Automated order execution via tastytrade order API

**OS2**: Position tracking and P&L monitoring for existing calendar spreads

**OS3**: Backtesting framework using historical IV data

**OS4**: Real-time monitoring dashboard (web UI or GUI)

**OS5**: Alert notifications (email, SMS, push) when new opportunities appear

**OS6**: Integration with third-party portfolio management tools

**OS7**: Greeks-based position risk analysis (portfolio delta, vega, theta)

**OS8**: Earnings "ex-date" IV calculation (if X-earn IV from API is unavailable)

**OS9**: Bid-ask spread quality analysis (require spread < X% of mid-price)

**OS10**: Open interest thresholds (in addition to liquidity rating)

### Future Considerations (v2.1+)

- Auto-execution with position size allocation (fractional Kelly)
- Position tracking with Greeks aggregation
- Backtest framework for strategy validation
- Earnings ex-date IV calculation if API doesn't provide X-earn IV
- Enhanced liquidity filters (bid-ask spread, open interest)

## Dependencies

### External Dependencies

**ED1**: tastytrade SDK (v10.1.0+)
- Required for: session authentication, market data, option chains, Greeks streaming, market metrics

**ED2**: tastytrade production environment
- Required for: live market data (sandbox insufficient)
- Credentials: `TT_USERNAME`, `TT_PASSWORD` environment variables

**ED3**: dxFeed market data
- Required for: real-time Greeks (IV, delta)
- Accessed via: `DXLinkStreamer` in tastytrade SDK

**ED4**: tastytrade Market Metrics API
- Required for: earnings dates, liquidity ratings
- Endpoint: `tastytrade.metrics.get_market_metrics()`

### Internal Dependencies

**ID1**: Existing scanner codebase (`ff_tastytrade_scanner.py`)
- Current functionality must remain intact (backward compatibility)

**ID2**: Forward Factor calculation logic
- Formula: `FF = (σ₁ - σ_fwd) / σ_fwd` (no changes)
- Variance decomposition for forward IV (no changes)

**ID3**: ATM strike selection logic (`pick_atm_strike()`)
- Reusable for double calendar center reference

### Data Dependencies

**DD1**: Reliable earnings date data
- Risk: Earnings dates can change with <7 days notice
- Mitigation: Re-run scanner daily to catch updates

**DD2**: Greeks data availability
- Risk: Low-liquidity symbols may not stream Greeks
- Mitigation: Timeout handling + skip symbol on failure

**DD3**: Consistent expiration dates across API calls
- Risk: Option chain expirations must match market metrics expirations
- Mitigation: Use `expiration_date` as join key

## Implementation Phases

### Phase 1: Critical Filters (Week 1) - 5-7 hours

**Deliverables**:
- FR1: Earnings date filtering (complete)
- FR2: Liquidity screening (complete)
- Updated CLI with `--skip-earnings`, `--min-liquidity-rating` flags
- Enhanced CSV output with earnings + liquidity columns

**Success Gate**: Run scanner on 10 symbols → verify earnings conflicts filtered, liquidity thresholds enforced

### Phase 2: Advanced Features (Week 2) - 10-14 hours

**Deliverables**:
- FR3: X-earn IV support (with uncertainty handling)
- FR4: Double calendar structure scanning (complete)
- Updated CLI with `--structure`, `--use-xearn-iv` flags
- Full CSV output with all columns

**Success Gate**: Scan SPY/QQQ with `--structure both` → verify both ATM and double calendar results, validate delta selection

### Phase 3: Documentation & Testing (Continuous) - 2-4 hours

**Deliverables**:
- Update `CLAUDE.md` with new features
- Update `scripts/README_TT.md` with CLI examples
- Update `docs/gpt-setup-instructions1.txt` with v2.0 usage
- Unit tests for earnings filtering, liquidity filtering, delta strike selection

**Success Gate**: Documentation enables new user to run scanner with all features without external guidance

## Risks & Mitigations

### High Risk

**R1: X-earn IV Data Unavailability**
- **Risk**: `OptionExpirationImpliedVolatility` may not contain true X-earn IV
- **Impact**: FR3 completely blocked, FF calculations biased around earnings
- **Probability**: 40%
- **Mitigation**:
  - Phase 1 approach: Rely on earnings filtering to avoid earnings-juiced IV (effectively "X-earn" by exclusion)
  - Phase 2 approach: Test API data against known earnings events, validate data quality
  - Fallback: Defer FR3 to v2.1, document limitation in README
- **Decision Point**: Week 1 - validate X-earn IV data or defer feature

**R2: Liquidity Rating Doesn't Correlate with Volume**
- **Risk**: `liquidity_rating` may not map to "≥10k contracts/day avg volume" threshold
- **Impact**: Scanner filters incorrectly (too strict or too lenient)
- **Probability**: 30%
- **Mitigation**:
  - Week 1: Spot-check 10 symbols (SPY, QQQ, AAPL, etc.) → compare liquidity_rating to tastytrade platform's displayed volume
  - If correlation weak: adjust threshold or add `--min-liquidity-value` flag
  - Document mapping in README (e.g., "rating 3 ≈ 5k contracts/day, rating 4 ≈ 15k")

### Medium Risk

**R3: Double Calendar Strike Selection Instability**
- **Risk**: In low-liquidity or wide-spread markets, no strikes within ±0.05Δ tolerance
- **Impact**: Scanner returns no double calendar opportunities even when ATM opportunities exist
- **Probability**: 20%
- **Mitigation**:
  - Allow user-configurable `--delta-tolerance` (default 0.05, max 0.10)
  - Log warning when tolerance exceeded: `[WARN] {symbol}: No strikes found within {tolerance}Δ for double calendar`
  - Gracefully fall back to ATM-only output for that symbol

**R4: API Rate Limiting**
- **Risk**: Scanning 20+ symbols may hit undocumented tastytrade API rate limits
- **Impact**: Scanner fails mid-scan or returns incomplete data
- **Probability**: 15%
- **Mitigation**:
  - Batch `get_market_metrics()` calls (all symbols in one request)
  - Add retry logic with exponential backoff
  - Add `--rate-limit-delay` flag for user to throttle requests if needed

### Low Risk

**R5: Earnings Date Inaccuracy**
- **Risk**: Earnings dates in API are estimated/stale
- **Impact**: Scanner allows earnings conflicts or filters valid opportunities
- **Probability**: 10%
- **Mitigation**:
  - Check `earnings.estimated` flag, log warning if True
  - User responsibility to cross-check high-conviction trades on tastytrade platform
  - Document in README: "Earnings dates are estimates; verify before execution"

**R6: Backward Compatibility Breakage**
- **Risk**: v2.0 changes break existing scripts/workflows that call v1.0 scanner
- **Impact**: User workflows disrupted
- **Probability**: 5%
- **Mitigation**:
  - All v1.0 flags remain functional with same behavior
  - CSV output is superset (add columns, don't change column order)
  - Test v1.0 commands after v2.0 implementation to verify compatibility

## Validation Plan

### Pre-Launch Testing

**Test 1: Earnings Filtering Accuracy**
- Scan AAPL, TSLA, NVDA (known upcoming earnings)
- Verify scanner skips positions spanning earnings
- Verify `--show-earnings-conflicts` shows filtered positions
- Manual verification: Check tastytrade platform for earnings dates

**Test 2: Liquidity Threshold Validation**
- Scan 20 symbols with `--min-liquidity-rating 3`
- For each output symbol, manually check tastytrade liquidity rating
- Verify no symbols with rating <3 appear in results
- Spot-check 5 symbols: compare rating to actual 20-day avg volume

**Test 3: Double Calendar Strike Selection**
- Scan SPY with `--structure double`
- Verify call strike has delta ~0.35, put strike has delta ~-0.35
- Manually calculate FF using tastytrade platform's IV chain
- Compare to scanner output (should match within 0.01)

**Test 4: X-earn IV Functionality**
- Scan 5 symbols with `--use-xearn-iv`
- Check `iv_source` column in CSV
- If "xearn" appears, validate IV values differ from dxFeed Greeks
- If all "greeks", confirm X-earn IV unavailable, proceed with earnings filtering only

**Test 5: Performance Benchmark**
- Scan 10 symbols with all features enabled
- Measure execution time → should be ≤30 seconds
- Scan 20 symbols → should be ≤60 seconds

### Post-Launch Validation (30-Day Window)

**Validation 1: No Earnings Surprises**
- Track all positions entered from scanner results
- Verify 0 positions encounter earnings during hold period
- If >0, investigate: was earnings date missing in API? Did company reschedule?

**Validation 2: Trade Quality Analysis**
- Track all positions entered over 30 days
- Calculate: avg entry FF, avg P&L at front expiry, win rate
- Compare to backtest expectations from original research
- Goal: Win rate ≥60% (matches research for properly-filtered opportunities)

**Validation 3: Liquidity Validation**
- For all positions entered, record:
  - Bid-ask spread at entry (% of mid)
  - Fill quality (how close to mid-price)
- Goal: ≥90% of fills within 0.5 × bid-ask spread of mid-price

**Validation 4: Opportunity Coverage**
- Count: total opportunities scanned, total filtered out, total acted upon
- Verify: filtering isn't too aggressive (not missing obvious opportunities)
- Spot-check 3 filtered positions weekly: confirm filtering was correct

## Open Questions

**Q1**: Does `OptionExpirationImpliedVolatility.implied_volatility` represent X-earn IV or regular IV?
- **Owner**: Implementation team (you)
- **Decision by**: End of Week 1
- **Impact**: Determines if FR3 ships in v2.0 or defers to v2.1

**Q2**: What is the exact mapping of `liquidity_rating` (0-5) to average daily option volume?
- **Owner**: Implementation team (you)
- **Decision by**: Week 1, during FR2 implementation
- **Impact**: Determines correct default for `--min-liquidity-rating`

**Q3**: Should double calendar `combined_ff` be arithmetic mean or weighted by strike distance from ATM?
- **Owner**: Product (you)
- **Decision by**: Week 2, during FR4 implementation
- **Impact**: Minor - affects ranking of double calendar opportunities
- **Current assumption**: Arithmetic mean (simpler, matches research)

**Q4**: Should scanner support JSON output in addition to CSV?
- **Owner**: Product (you)
- **Decision by**: Before Phase 3 (documentation)
- **Impact**: Low - adds output format flexibility
- **Current decision**: CSV only (stated in requirements gathering)

**Q5**: Should scanner cache market metrics data for intraday re-scans to reduce API calls?
- **Owner**: Implementation team (you)
- **Decision by**: If performance issues arise
- **Impact**: Could reduce intraday scan time from 30s → 10s
- **Current decision**: No caching in v2.0 (not in scope)

---

## Appendix A: CLI Flag Reference

```bash
# Earnings Filtering
--skip-earnings              # Skip positions with earnings conflicts (default: True)
--allow-earnings             # Allow trading through earnings
--show-earnings-conflicts    # Show filtered positions due to earnings

# Liquidity Screening
--min-liquidity-rating N     # Minimum liquidity rating 0-5 (default: 3)
--skip-liquidity-check       # Disable liquidity filtering

# X-earn IV Support
--use-xearn-iv               # Use X-earn IV from market metrics (default: True)
--force-greeks-iv            # Always use dxFeed Greeks IV

# Double Calendar Structure
--structure {atm-call,double,both}  # Calendar structure type (default: both)
--delta-tolerance N                  # Max deviation from ±35Δ (default: 0.05)

# Existing Flags (v1.0, unchanged)
--tickers SYMBOL [SYMBOL ...]        # Space-separated symbols
--pairs DTE-DTE [DTE-DTE ...]        # DTE pairs (e.g., 30-60 30-90)
--min-ff N                           # Minimum Forward Factor (default: 0.20)
--dte-tolerance N                    # Max DTE deviation (default: 5)
--timeout N                          # Greeks snapshot timeout (default: 3)
--csv-out FILENAME                   # CSV output file
--json-out FILENAME                  # JSON output file (if implemented)
```

## Appendix B: CSV Output Schema

```csv
timestamp,symbol,structure,front_dte,back_dte,front_expiry,back_expiry,spot_price,
atm_strike,call_strike,put_strike,call_delta,put_delta,
front_iv,back_iv,fwd_iv,ff,call_ff,put_ff,combined_ff,
earnings_date,earnings_conflict,liquidity_rating,liquidity_value,
iv_source_front,iv_source_back
```

**Column Definitions**:
- `timestamp`: ISO 8601 UTC (e.g., "2025-10-19T12:30:00Z")
- `symbol`: Underlying ticker (e.g., "SPY")
- `structure`: "atm-call" or "double"
- `front_dte`, `back_dte`: Days to expiration for front/back legs
- `front_expiry`, `back_expiry`: Expiration dates (YYYY-MM-DD)
- `spot_price`: Underlying price at scan time
- `atm_strike`: Strike for ATM calendar (null for double)
- `call_strike`, `put_strike`: Strikes for double calendar (null for ATM)
- `call_delta`, `put_delta`: Delta values for double calendar strikes (null for ATM)
- `front_iv`, `back_iv`: Implied volatility for front/back expirations
- `fwd_iv`: Calculated forward volatility
- `ff`: Forward Factor for ATM calendar (null for double)
- `call_ff`, `put_ff`: Forward Factors for double calendar legs (null for ATM)
- `combined_ff`: Average FF for double calendar, or same as `ff` for ATM
- `earnings_date`: Next earnings date (YYYY-MM-DD or null)
- `earnings_conflict`: Boolean ("True" or "False")
- `liquidity_rating`: tastytrade liquidity rating (0-5)
- `liquidity_value`: tastytrade liquidity value (Decimal or null)
- `iv_source_front`, `iv_source_back`: "xearn" or "greeks"

## Appendix C: Example Usage Scenarios

**Scenario 1: Daily Pre-Market Scan (Production Use)**
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL TSLA NVDA META AMZN GOOGL MSFT AMD \
  --pairs 30-60 30-90 60-90 \
  --min-ff 0.23 \
  --skip-earnings \
  --min-liquidity-rating 3 \
  --structure both \
  --csv-out "$(date +%y%m%d_%H%M)_ff_scan.csv"
```

**Scenario 2: Focus on 60-90 DTE Double Calendars**
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ IWM \
  --pairs 60-90 \
  --min-ff 0.20 \
  --structure double \
  --csv-out double_calendars.csv
```

**Scenario 3: Debugging Why AAPL Didn't Appear**
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers AAPL \
  --pairs 30-60 \
  --show-earnings-conflicts \
  --skip-liquidity-check
```

**Scenario 4: Aggressive Scan (Lower Thresholds, More Opportunities)**
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 60-90 \
  --min-ff 0.15 \
  --min-liquidity-rating 2 \
  --structure both
```
