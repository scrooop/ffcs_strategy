---
name: ff-scanner-v2
status: in-progress
created: 2025-10-19T08:30:29Z
updated: 2025-10-19T16:52:10Z
progress: 50%
prd: .claude/prds/ff-scanner-v2.md
github: https://github.com/scrooop/ffcs_strategy/issues/1
---

# Epic: FF Scanner v2.0 - Enhanced Quality Filtering

## Overview

Enhance the existing FF scanner (`scripts/ff_tastytrade_scanner.py`) with four integrated features that automate manual verification steps: earnings filtering, liquidity screening, X-earn IV support, and double calendar structure scanning. The implementation leverages existing scanner architecture and adds a single batched `get_market_metrics()` API call to minimize performance impact while maximizing trade quality.

**Core Strategy**: Modify the existing scanner's main loop to add pre-filtering (earnings/liquidity) and post-processing (double calendar scanning) without changing the core FF calculation logic.

## Architecture Decisions

### AD1: Single Batched Market Metrics Call

**Decision**: Fetch all market metrics (earnings + liquidity) for ALL symbols in a single batched API call before the main scanning loop.

**Rationale**:
- Minimizes API overhead (1 call vs N calls)
- Enables pre-filtering before expensive Greeks streaming
- tastytrade API supports batch requests up to 50+ symbols

**Implementation**: Add `fetch_market_metrics()` function that returns a dict mapping symbol → MarketMetricInfo.

### AD2: Reuse Existing Greeks Streaming for Delta

**Decision**: Extend current `snapshot_greeks()` function to collect delta values in addition to IV.

**Rationale**:
- dxFeed Greeks already provides delta (Greeks.delta)
- No additional API calls needed
- For double calendars, request Greeks for more strikes (±35Δ range instead of just ATM)

**Trade-off**: Slightly more Greeks subscriptions per symbol (8-12 strikes vs 2-4), but still within performance targets.

### AD3: Modular Filtering Pipeline

**Decision**: Implement filtering as composable predicate functions that can be enabled/disabled via CLI flags.

**Pattern**:
```python
def check_earnings_conflict(symbol, market_metrics, back_expiry) -> Tuple[bool, str]:
    """Returns (passes_filter, reason_if_filtered)"""

def check_liquidity(symbol, market_metrics, min_rating) -> Tuple[bool, str]:
    """Returns (passes_filter, reason_if_filtered)"""
```

**Rationale**:
- Clean separation of concerns
- Easy to test each filter independently
- Supports `--show-earnings-conflicts` by preserving filter reasons

### AD4: Structure-Based Scanning Strategy

**Decision**: Scan structures sequentially (ATM first, then double if requested) rather than in parallel.

**Rationale**:
- Simpler control flow (no concurrent state management)
- ATM scanning can inform double calendar strike range (use ATM as center reference)
- Negligible performance difference (bottleneck is Greeks streaming, not computation)

**Implementation**: Single `scan_symbol()` function with `structure` parameter that returns list of results (0-2 rows per symbol).

### AD5: X-earn IV with Graceful Degradation

**Decision**: Attempt X-earn IV from market metrics, fall back to Greeks IV, log source in CSV.

**Rationale**:
- Handles uncertainty about X-earn IV availability (40% risk per PRD)
- Maintains backward compatibility (current behavior uses Greeks IV)
- CSV `iv_source` column enables post-hoc analysis of data quality

**Fallback Strategy**: If X-earn IV unavailable for ALL symbols in Week 1 testing, disable FR3 and rely on earnings filtering (defer X-earn IV to v2.1).

### AD6: Backward-Compatible CLI Design

**Decision**: All new flags use additive defaults (e.g., `--skip-earnings` is default behavior).

**Rationale**:
- v1.0 commands continue to work unchanged
- New behavior is opt-out, not opt-in (safer for production use)
- `--help` documents all flags clearly

## Technical Approach

### Data Flow Architecture

```
1. Parse CLI args + validate
2. Batch fetch market metrics for ALL symbols (earnings + liquidity)
3. For each symbol:
   a. Pre-filter: Check earnings conflict → skip if conflicts
   b. Pre-filter: Check liquidity rating → skip if too low
   c. Fetch option chain (existing logic)
   d. For each DTE pair:
      i.   Find ATM strikes (existing logic)
      ii.  Fetch Greeks for ATM (existing logic, add delta)
      iii. Calculate FF for ATM (existing logic)
      iv.  If --structure=double or both:
           - Find ±35Δ strikes using delta from Greeks
           - Fetch Greeks for ±35Δ strikes
           - Calculate FF for call and put calendars
      v.   Apply --min-ff threshold
      vi.  Collect results
4. Sort results by combined_ff descending
5. Output CSV with all columns
```

### Core Components

#### Component 1: Market Metrics Integration (New)

**File**: `scripts/ff_tastytrade_scanner.py` (modify existing)

**Functions**:
```python
async def fetch_market_metrics(session: Session, symbols: List[str]) -> Dict[str, MarketMetricInfo]:
    """Batch fetch earnings and liquidity data for all symbols."""

def check_earnings_conflict(symbol: str, metrics: Dict, back_expiry: date, today: date) -> Tuple[bool, Optional[str]]:
    """Returns (passes, reason). Example: (False, "Earnings 2025-11-01 conflicts with back expiry 2025-11-05")"""

def check_liquidity(symbol: str, metrics: Dict, min_rating: int) -> Tuple[bool, Optional[str]]:
    """Returns (passes, reason). Example: (False, "Liquidity rating 2 < 3")"""
```

**Integration Point**: Call `fetch_market_metrics()` once before main loop in `async def main()`.

#### Component 2: Enhanced Greeks Collection (Modify Existing)

**File**: `scripts/ff_tastytrade_scanner.py` (modify existing `snapshot_greeks()`)

**Changes**:
- Current: Returns dict mapping streamer_symbol → Greeks.volatility (IV only)
- Enhanced: Returns dict mapping streamer_symbol → (IV, delta)

**Function Signature**:
```python
async def snapshot_greeks(session, symbols: List[str], timeout=3.0) -> Dict[str, Tuple[float, float]]:
    """Returns {symbol: (iv, delta)} for each symbol that arrives within timeout."""
```

#### Component 3: Double Calendar Strike Selection (New)

**File**: `scripts/ff_tastytrade_scanner.py` (new function)

**Functions**:
```python
async def find_delta_strikes(
    session: Session,
    expiration_obj,
    target_delta_call: float = 0.35,
    target_delta_put: float = -0.35,
    tolerance: float = 0.05
) -> Tuple[Optional[Strike], Optional[Strike]]:
    """
    Find strikes closest to ±35Δ.
    Returns (call_strike_obj, put_strike_obj) or (None, None) if not found.
    """
```

**Algorithm**:
1. Get all strikes from expiration_obj
2. Request Greeks for all strikes (or reasonable subset, e.g., ±20% from ATM)
3. Filter strikes by delta within tolerance
4. Return strike with smallest delta error

#### Component 4: X-earn IV Extraction (New)

**File**: `scripts/ff_tastytrade_scanner.py` (new function)

**Functions**:
```python
def extract_xearn_iv(metrics: Dict, symbol: str, expiration_date: date) -> Optional[float]:
    """
    Try to extract X-earn IV from MarketMetricInfo.option_expiration_implied_volatilities.
    Returns None if unavailable.
    """
```

**Integration**: Call before `snapshot_greeks()` for each expiration; use result if available, otherwise fall back to Greeks IV.

#### Component 5: Enhanced CSV Output (Modify Existing)

**File**: `scripts/ff_tastytrade_scanner.py` (modify CSV writing logic)

**Changes**:
- Add columns: timestamp, structure, call_strike, put_strike, call_delta, put_delta, call_ff, put_ff, combined_ff, earnings_date, earnings_conflict, liquidity_rating, liquidity_value, iv_source_front, iv_source_back
- Sort by combined_ff descending
- Use ISO 8601 timestamp format

**Function**:
```python
def write_csv(results: List[Dict], output_file: str):
    """Write results to CSV with all columns."""
```

### Testing Strategy

**Unit Tests** (scripts/test_ff_scanner.py - new file):
```python
def test_earnings_conflict_detection()
def test_liquidity_threshold_filtering()
def test_delta_strike_selection()
def test_xearn_iv_extraction()
def test_csv_output_schema()
```

**Integration Tests** (manual, documented in README):
```bash
# Test 1: Earnings filtering
python scripts/ff_tastytrade_scanner.py --tickers AAPL --pairs 30-60 --show-earnings-conflicts

# Test 2: Liquidity filtering
python scripts/ff_tastytrade_scanner.py --tickers SPY QQQ ILLIQUID_SYMBOL --min-liquidity-rating 4

# Test 3: Double calendar
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 60-90 --structure double

# Test 4: Performance
time python scripts/ff_tastytrade_scanner.py --tickers SPY QQQ AAPL TSLA NVDA META AMZN GOOGL MSFT AMD --pairs 30-60 30-90 60-90 --structure both
```

## Implementation Strategy

### Phased Rollout

**Phase 1: Foundation + Earnings/Liquidity (Days 1-3)**
- Implement market metrics fetching
- Add earnings and liquidity filters
- Update CLI with new flags
- Test with 10-symbol scan

**Phase 2: Double Calendar (Days 4-6)**
- Implement delta-based strike selection
- Add double calendar scanning logic
- Enhance CSV output with structure columns
- Test with SPY/QQQ

**Phase 3: X-earn IV + Polish (Days 7-8)**
- Implement X-earn IV extraction (with fallback)
- Add iv_source tracking
- Final CSV schema implementation
- Performance optimization

**Phase 4: Documentation (Day 9)**
- Update CLAUDE.md with new features
- Update scripts/README_TT.md with examples
- Add inline docstrings to all new functions

### Risk Mitigation

**Risk R1 (X-earn IV unavailable)**:
- Mitigation: Test in Phase 1 with 5 symbols
- Decision point: End of Day 2
- Fallback: Skip FR3, document limitation, rely on earnings filtering

**Risk R2 (Liquidity rating correlation weak)**:
- Mitigation: Validate mapping in Phase 1 (spot-check 10 symbols)
- Adjustment: Change default threshold or add --min-liquidity-value flag

**Risk R3 (Double calendar strike selection fails)**:
- Mitigation: Add --delta-tolerance flag (default 0.05, allow up to 0.10)
- Fallback: Log warning, return ATM-only for that symbol

## Task Breakdown

**Total: 10 Tasks (21-28 hours estimated)**

All task files are located in `.claude/epics/ff-scanner-v2/tasks/`

### Phase 1: Foundation + Filters (6-8 hours)

**[Task 01: Market Metrics Integration](tasks/01-market-metrics-integration.md)** - 3-4 hours
- Priority: **CRITICAL** | Dependencies: None
- Implement batched earnings + liquidity fetching
- Add `fetch_market_metrics()`, `check_earnings_conflict()`, `check_liquidity()` functions
- CLI flags: `--skip-earnings`, `--allow-earnings`, `--show-earnings-conflicts`, `--min-liquidity-rating`, `--skip-liquidity-check`

**[Task 02: Enhanced Greeks Collection](tasks/02-enhanced-greeks-collection.md)** - 1-2 hours
- Priority: **CRITICAL** | Dependencies: None
- Modify `snapshot_greeks()` to return `(iv, delta)` tuples
- Maintain backward compatibility for ATM scanning

### Phase 2: Double Calendar (6-8 hours)

**[Task 03: Double Calendar Strike Selection](tasks/03-double-calendar-strike-selection.md)** - 3-4 hours
- Priority: **HIGH** | Dependencies: Task 02
- Implement ±35Δ strike finding algorithm
- Add `find_delta_strikes()` function
- CLI flag: `--delta-tolerance`

**[Task 04: Double Calendar Scanning Logic](tasks/04-double-calendar-scanning.md)** - 3-4 hours
- Priority: **HIGH** | Dependencies: Tasks 02, 03
- Add structure-based scanning to main loop
- Implement `scan_atm_calendar()` and `scan_double_calendar()` functions
- CLI flag: `--structure {atm-call,double,both}`
- Compute `call_ff`, `put_ff`, `combined_ff`

### Phase 3: X-earn IV + Polish (4-5 hours)

**[Task 05: X-earn IV Integration](tasks/05-xearn-iv-integration.md)** - 2-3 hours
- Priority: **MEDIUM** | Dependencies: None
- Attempt X-earn IV extraction with fallback to Greeks IV
- Add `extract_xearn_iv()` function
- CLI flags: `--use-xearn-iv`, `--force-greeks-iv`
- **Decision Point**: End of Day 2 - ship or defer to v2.1

**[Task 06: Enhanced CSV Output](tasks/06-enhanced-csv-output.md)** - 2 hours
- Priority: **HIGH** | Dependencies: Tasks 01, 02, 04, 05
- Expand CSV schema to 25 columns
- ISO 8601 timestamp, sort by `combined_ff` descending
- Null handling for structure-specific columns

### Phase 4: Testing + Documentation (5-8 hours)

**[Task 07: CLI Enhancement & Help Documentation](tasks/07-cli-enhancement.md)** - 1-2 hours
- Priority: **MEDIUM** | Dependencies: Tasks 01, 03, 04, 05
- Update argument parser with all new flags
- Comprehensive `--help` output with examples
- Flag validation logic

**[Task 08: Integration Testing & Validation](tasks/08-integration-testing.md)** - 2-3 hours
- Priority: **HIGH** | Dependencies: Tasks 01-07
- End-to-end testing with real market data
- Test earnings filtering, liquidity screening, double calendar
- Performance benchmarks (10 symbols ≤30s, 20 symbols ≤60s)
- X-earn IV validation (decision point)

**[Task 09: Documentation Updates](tasks/09-documentation-updates.md)** - 2-3 hours
- Priority: **MEDIUM** | Dependencies: Tasks 01-07
- Update `CLAUDE.md` with v2.0 features
- Rewrite `scripts/README_TT.md` with new examples
- Add comprehensive docstrings to all new functions

**[Task 10: Error Handling & Edge Cases](tasks/10-error-handling.md)** - 2 hours
- Priority: **HIGH** | Dependencies: Tasks 01-06
- Robust error handling for partial data
- Graceful degradation (missing earnings, Greeks timeout, etc.)
- Per-symbol error recovery (never crash mid-scan)

## Dependencies

### External API Dependencies
- **tastytrade SDK v10.1.0+**: Required for `get_market_metrics()`, Greeks streaming
- **tastytrade production environment**: Sandbox has insufficient market data
- **dxFeed Greeks data**: Must provide IV + delta for strike selection

### Internal Code Dependencies
- **Existing scanner logic**: ATM strike selection, FF calculation, NestedOptionChain usage
- **CLI argument parsing**: Extend existing argparse setup
- **CSV output logic**: Enhance existing CSV writer

### Data Quality Dependencies
- **Earnings date accuracy**: Assumed ≥95% accurate (validated during testing)
- **Liquidity rating mapping**: Assumed rating ≥3 ≈ ≥10k contracts/day (validated in Phase 1)
- **X-earn IV availability**: Unknown (40% risk per PRD, validated in Phase 1)

## Success Criteria (Technical)

### Performance Benchmarks
- ✅ 10-symbol scan completes in ≤30 seconds (target: 25s)
- ✅ 20-symbol scan completes in ≤60 seconds (target: 50s)
- ✅ Market metrics batch call adds ≤2 seconds overhead

### Quality Gates
- ✅ All v1.0 CLI commands continue to work (backward compatibility)
- ✅ CSV schema matches specification (25 columns)
- ✅ Earnings filtering: 0 false negatives (all conflicts caught)
- ✅ Liquidity filtering: ≤5% false positives (manual spot-check)
- ✅ Double calendar delta selection: strikes within tolerance ≥90% of time
- ✅ No crashes on partial data (earnings missing, Greeks timeout, etc.)

### Acceptance Criteria
- ✅ Scanner produces ≤5 high-quality opportunities from 10-symbol scan (down from 15-20 raw)
- ✅ `--show-earnings-conflicts` reveals filtered positions with FF values
- ✅ `--structure both` returns mix of ATM and double calendar results
- ✅ CSV output sorted by combined_ff descending
- ✅ All new functions have docstrings with type hints

## Estimated Effort

### Total Implementation Time: 21-28 hours

**Breakdown by Phase**:
- Phase 1 (Foundation + Filters): 6-8 hours
- Phase 2 (Double Calendar): 6-8 hours
- Phase 3 (X-earn IV + Polish): 4-5 hours
- Phase 4 (Documentation): 2-3 hours
- Phase 5 (Testing & Validation): 3-4 hours

**Critical Path**:
1. Market metrics integration (Task 1) → enables filtering
2. Enhanced Greeks collection (Task 2) → enables double calendar
3. Double calendar scanning (Tasks 3-4) → enables structure flexibility
4. CSV output (Task 6) → enables full feature delivery

**Parallel Work Opportunities**:
- Task 5 (X-earn IV) can be developed in parallel with Tasks 3-4 (double calendar)
- Task 7 (CLI) can be updated incrementally as features are added
- Task 9 (Documentation) can be drafted in parallel with implementation

### Resource Requirements
- **Developer**: 1 (you)
- **Environment**: tastytrade production account with live market data
- **Tools**: Python 3.12+, tastytrade SDK, existing FF scanner codebase

### Timeline
- **Week 1 (Days 1-5)**: Tasks 1-5 (core implementation)
- **Week 2 (Days 6-9)**: Tasks 6-10 (polish, testing, documentation)
- **Total Duration**: 9 working days (conservatively, 2 weeks calendar time)

## Simplification Opportunities

### Leverage Existing Code
1. **Reuse `snapshot_greeks()`**: Extend rather than replace (minimal changes)
2. **Reuse `pick_atm_strike()`**: Use as center reference for double calendar strike range
3. **Reuse FF calculation**: No changes needed to variance decomposition logic
4. **Reuse CSV writing**: Extend columns, keep existing structure

### Reduce Scope Where Possible
1. **X-earn IV**: If unavailable in Phase 1 testing, defer to v2.1 (rely on earnings filtering)
2. **Liquidity value**: If `liquidity_rating` is sufficient, skip `liquidity_value` column
3. **JSON output**: Explicitly out of scope (CSV only)
4. **Bid-ask spread analysis**: Explicitly out of scope (liquidity_rating is proxy)

### Simplify Implementation
1. **Sequential structure scanning**: ATM then double (no parallelism needed)
2. **Single batch API call**: `get_market_metrics()` for all symbols at once (no per-symbol calls)
3. **Arithmetic mean for combined_ff**: Simpler than weighted average (sufficient for ranking)

### Avoid Over-Engineering
1. **No caching layer**: Re-fetch market data on every scan (simpler, always fresh)
2. **No database**: CSV files are sufficient for analysis
3. **No retry logic**: If API call fails, log error and skip symbol (continue scan)
4. **No complex error recovery**: Graceful degradation (partial results OK)

## Tasks Created

- [ ] 001.md - Market Metrics Integration (parallel: true, 3-4 hours)
- [ ] 002.md - Enhanced Greeks Collection (parallel: true, 1-2 hours)
- [ ] 003.md - Double Calendar Strike Selection (parallel: false, depends on 002, 3-4 hours)
- [ ] 004.md - Double Calendar Scanning Logic (parallel: false, depends on 002, 003, 3-4 hours)
- [ ] 005.md - X-earn IV Integration (parallel: true, 2-3 hours)
- [ ] 006.md - Enhanced CSV Output (parallel: false, depends on 001, 002, 004, 005, 2 hours)
- [ ] 007.md - CLI Enhancement & Help Documentation (parallel: false, depends on 001, 003, 004, 005, 1-2 hours)
- [ ] 008.md - Integration Testing & Validation (parallel: false, depends on 001-007, 2-3 hours)
- [ ] 009.md - Documentation Updates (parallel: true, depends on 001-007, 2-3 hours)
- [ ] 010.md - Error Handling & Edge Cases (parallel: true, depends on 001-006, 2 hours)

**Total tasks:** 10
**Parallel tasks:** 4 (001, 002, 005, 009, 010)
**Sequential tasks:** 6 (003, 004, 006, 007, 008)
**Estimated total effort:** 21-28 hours

## Notes

- **X-earn IV Uncertainty**: Decision point at end of Phase 1. If unavailable, disable FR3 and document limitation.
- **Liquidity Rating Validation**: Spot-check mapping in Phase 1 to ensure threshold makes sense.
- **Backward Compatibility**: All v1.0 commands must continue to work. Test after each phase.
- **Performance**: Batched market metrics call is critical for keeping scan time ≤30s for 10 symbols.
- **Error Handling**: Fail gracefully on partial data (missing earnings, Greeks timeout, etc.). Never crash mid-scan.
