---
id: 08
name: Integration Testing & Validation
status: todo
priority: high
estimated_hours: 2-3
dependencies: [01, 02, 03, 04, 05, 06, 07]
phase: 4
created: 2025-10-19T08:35:09Z
---

# Task 08: Integration Testing & Validation

## Objective

Perform end-to-end integration testing with real market data to validate all v2.0 features work correctly together and meet performance benchmarks.

## Scope

Execute comprehensive test suite covering earnings filtering, liquidity screening, double calendar scanning, X-earn IV, and performance validation.

## Technical Details

### Test Plan

#### Test 1: Earnings Filtering Accuracy

**Purpose**: Verify earnings conflicts are correctly identified and filtered

**Command**:
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers AAPL TSLA NVDA \
  --pairs 30-60 \
  --show-earnings-conflicts
```

**Expected Outcomes**:
- [ ] Symbols with upcoming earnings show `[FILTERED]` messages
- [ ] Filtered positions display hypothetical FF values
- [ ] Earnings dates match tastytrade platform (manual verification)
- [ ] Without `--show-earnings-conflicts`, filtered symbols are silently skipped

**Manual Verification**:
- Check 3 symbols on tastytrade platform for earnings dates
- Verify scanner correctly identifies conflicts

#### Test 2: Liquidity Threshold Validation

**Purpose**: Verify liquidity rating filtering works correctly

**Command**:
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ IWM AAPL MSFT LOW_VOLUME_STOCK \
  --pairs 30-60 \
  --min-liquidity-rating 4 \
  --csv-out liquidity_test.csv
```

**Expected Outcomes**:
- [ ] Only symbols with liquidity_rating ≥ 4 appear in CSV
- [ ] Console shows `[INFO]` messages for filtered symbols
- [ ] SPY, QQQ likely pass (high liquidity)
- [ ] Low-volume stock likely filtered out

**Manual Verification**:
- Spot-check 5 symbols: compare liquidity_rating in CSV to tastytrade platform
- Verify rating ≥ 4 for all results

#### Test 3: Double Calendar Strike Selection

**Purpose**: Verify ±35Δ strike selection and FF calculations

**Command**:
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY \
  --pairs 60-90 \
  --structure double \
  --csv-out double_test.csv
```

**Expected Outcomes**:
- [ ] CSV contains `structure=double` rows
- [ ] `call_strike` and `put_strike` populated (not null)
- [ ] `call_delta` ≈ 0.30-0.40, `put_delta` ≈ -0.30 to -0.40
- [ ] `call_ff` and `put_ff` are reasonable values
- [ ] `combined_ff` = (call_ff + put_ff) / 2

**Manual Verification**:
- Open tastytrade platform → SPY option chain for back expiration
- Find strikes near ±35Δ
- Manually calculate FF using platform's IV values
- Compare to scanner output (should match within 0.01)

#### Test 4: Structure Scanning Modes

**Purpose**: Verify `--structure` flag controls output correctly

**Commands**:
```bash
# ATM only
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --structure atm-call --csv-out atm_only.csv

# Double only
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --structure double --csv-out double_only.csv

# Both (default)
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --structure both --csv-out both.csv
```

**Expected Outcomes**:
- [ ] `atm_only.csv`: Only `structure=atm-call` rows
- [ ] `double_only.csv`: Only `structure=double` rows
- [ ] `both.csv`: Contains both structures (2 rows per symbol-pair)

#### Test 5: X-earn IV Functionality

**Purpose**: Validate X-earn IV extraction or confirm unavailability

**Command**:
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL TSLA NVDA \
  --pairs 30-60 \
  --use-xearn-iv \
  --csv-out xearn_test.csv
```

**Expected Outcomes**:
- [ ] CSV contains `iv_source_front` and `iv_source_back` columns
- [ ] Values are either "xearn" or "greeks"
- [ ] If all "greeks", X-earn IV is unavailable (defer FR3 to v2.1)
- [ ] If "xearn" appears, IV values differ from `--force-greeks-iv` run

**Decision Point**:
- If X-earn IV unavailable for ALL symbols → document limitation, rely on earnings filtering
- If X-earn IV available → validate values are reasonable (not wildly different from Greeks)

#### Test 6: Performance Benchmark

**Purpose**: Verify scanner meets performance targets

**Commands**:
```bash
# 10-symbol scan
time python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL TSLA NVDA META AMZN GOOGL MSFT AMD \
  --pairs 30-60 30-90 60-90 \
  --structure both

# 20-symbol scan
time python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ IWM AAPL TSLA NVDA META AMZN GOOGL MSFT AMD NFLX DIS BA GE JPM BAC XOM CVX MRK \
  --pairs 30-60 30-90 60-90 \
  --structure both
```

**Expected Outcomes**:
- [ ] 10-symbol scan: ≤30 seconds (target: 25s)
- [ ] 20-symbol scan: ≤60 seconds (target: 50s)
- [ ] Market metrics batch call adds ≤2 seconds overhead

**Performance Analysis**:
- Measure time breakdown: market metrics, option chains, Greeks streaming
- If performance issues, investigate bottlenecks

#### Test 7: Error Handling & Edge Cases

**Purpose**: Verify robust handling of partial data

**Scenarios to Test**:

**7a. Missing Earnings Data**
```bash
# Use symbol with no earnings data (e.g., ETF like SPY)
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 30-60
```
Expected: Scanner proceeds without filtering (no crash)

**7b. Missing Liquidity Rating**
```bash
# Use obscure symbol that may lack liquidity data
python scripts/ff_tastytrade_scanner.py --tickers OBSCURE_STOCK --pairs 30-60
```
Expected: Warning logged, scanner proceeds

**7c. Greeks Timeout**
```bash
# Reduce timeout to force failures
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --timeout 0.1
```
Expected: Some symbols skipped with warnings, no crash

**7d. No Strikes Within Delta Tolerance**
```bash
# Use very tight tolerance
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --structure double --delta-tolerance 0.01
```
Expected: Warning logged, fallback to ATM-only or skip symbol

#### Test 8: Backward Compatibility

**Purpose**: Verify v1.0 commands still work

**Command** (v1.0 syntax):
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 30-90 60-90 \
  --min-ff 0.20 \
  --csv-out v1_compat.csv
```

**Expected Outcomes**:
- [ ] Scanner runs without errors
- [ ] Results match v1.0 behavior (ATM-only, no earnings filtering by default)
- [ ] CSV contains new columns (superset) but v1.0 columns unchanged

## Deliverables

- [ ] Test 1 completed: Earnings filtering validated
- [ ] Test 2 completed: Liquidity filtering validated
- [ ] Test 3 completed: Double calendar validated
- [ ] Test 4 completed: Structure modes validated
- [ ] Test 5 completed: X-earn IV validated (or deferred)
- [ ] Test 6 completed: Performance benchmarks met
- [ ] Test 7 completed: Error handling validated
- [ ] Test 8 completed: Backward compatibility confirmed
- [ ] Test results documented (pass/fail for each scenario)

## Testing Checklist

### Pre-Test Setup
- [ ] tastytrade production environment accessible
- [ ] TT_USERNAME and TT_PASSWORD environment variables set
- [ ] Market hours or after-hours with live data

### Test Execution
- [ ] All 8 tests executed with real market data
- [ ] Results documented (screenshots or output logs)
- [ ] Manual verifications completed (spot-checks vs tastytrade platform)
- [ ] Performance measurements recorded

### Post-Test Analysis
- [ ] All tests passed OR issues documented with repro steps
- [ ] X-earn IV decision made (ship or defer)
- [ ] Performance targets met OR bottlenecks identified
- [ ] Edge cases handled gracefully (no crashes)

## Acceptance Criteria

- ✅ Earnings filtering: 0 false negatives (all conflicts caught)
- ✅ Liquidity filtering: ≤5% false positives (manual spot-check)
- ✅ Double calendar: strikes within tolerance ≥90% of time
- ✅ Performance: 10-symbol scan ≤30s, 20-symbol scan ≤60s
- ✅ Error handling: No crashes on partial data
- ✅ Backward compatibility: v1.0 commands work unchanged
- ✅ X-earn IV: Decision made (ship or defer to v2.1)

## Notes

- **Real Market Data Required**: Sandbox has insufficient data for testing
- **Spot-Check Validation**: Manually verify 3-5 symbols against tastytrade platform for each test
- **X-earn IV Decision**: Critical decision point - if unavailable, document and move on
- **Performance**: If targets not met, investigate market_metrics batch call overhead
- **Test Documentation**: Keep logs/screenshots for each test as evidence of validation
