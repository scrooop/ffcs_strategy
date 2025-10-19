---
id: 10
name: Error Handling & Edge Cases
status: todo
priority: high
estimated_hours: 2
dependencies: [01, 02, 03, 04, 05, 06]
phase: 4
created: 2025-10-19T08:35:09Z
---

# Task 10: Error Handling & Edge Cases

## Objective

Implement robust error handling for partial data scenarios, ensuring scanner never crashes mid-scan and degrades gracefully when data is unavailable.

## Scope

Add comprehensive error handling, logging, and graceful degradation for all identified edge cases.

## Technical Details

### Edge Cases to Handle

#### EC1: Missing Earnings Data

**Scenario**: Symbol has no earnings in market metrics

**Current Behavior**: Crash or incorrect filtering

**Desired Behavior**:
```python
def check_earnings_conflict(...):
    metric = metrics.get(symbol)
    if not metric or not metric.earnings:
        # No earnings data - proceed without filtering
        print(f"[INFO] {symbol}: No earnings data available, skipping earnings filter")
        return True, None

    earnings_date = metric.earnings.expected_report_date
    if not earnings_date:
        print(f"[INFO] {symbol}: Earnings date not available, skipping earnings filter")
        return True, None

    # ... rest of logic
```

#### EC2: Missing Liquidity Rating

**Scenario**: Symbol has no liquidity_rating in market metrics

**Current Behavior**: Crash or incorrect filtering

**Desired Behavior**:
```python
def check_liquidity(...):
    metric = metrics.get(symbol)
    if not metric:
        print(f"[WARN] {symbol}: No market metrics available, skipping liquidity filter")
        return True, None

    if metric.liquidity_rating is None:
        print(f"[WARN] {symbol}: No liquidity rating available, skipping liquidity filter")
        return True, None

    # ... rest of logic
```

#### EC3: Greeks Timeout

**Scenario**: Greeks don't arrive within timeout for some strikes

**Current Behavior**: Partial Greeks map returned

**Desired Behavior**:
```python
async def scan_atm_calendar(...):
    greeks_map = await snapshot_greeks(session, [front_call_symbol, back_call_symbol])

    if front_call_symbol not in greeks_map:
        print(f"[WARN] {symbol}: Greeks timeout for front leg, skipping")
        return None

    if back_call_symbol not in greeks_map:
        print(f"[WARN] {symbol}: Greeks timeout for back leg, skipping")
        return None

    # ... rest of logic
```

#### EC4: No Strikes Within Delta Tolerance

**Scenario**: Double calendar can't find ±35Δ strikes within tolerance

**Current Behavior**: Return (None, None)

**Desired Behavior**:
```python
async def scan_double_calendar(...):
    call_info, put_info = await find_delta_strikes(...)

    if not call_info or not put_info:
        print(f"[WARN] {symbol} {front_dte}-{back_dte}: No strikes within {delta_tolerance}Δ, skipping double calendar")
        return None

    # ... rest of logic
```

#### EC5: Negative Forward Variance

**Scenario**: IV backwardation so extreme that fwd_var < 0

**Current Behavior**: math.sqrt() raises ValueError

**Desired Behavior**:
```python
def calculate_forward_iv(iv_front, iv_back, T1, T2):
    """Calculate forward IV with error handling."""
    fwd_var = (iv_back**2 * T2 - iv_front**2 * T1) / (T2 - T1)

    if fwd_var <= 0:
        print(f"[WARN] Negative forward variance: fwd_var={fwd_var:.6f}, skipping")
        return None

    return math.sqrt(fwd_var)
```

#### EC6: API Call Failures

**Scenario**: tastytrade API call fails (network error, rate limit, etc.)

**Current Behavior**: Exception crashes entire scan

**Desired Behavior**:
```python
async def fetch_market_metrics(session, symbols):
    """Fetch market metrics with error handling."""
    try:
        from tastytrade.metrics import get_market_metrics
        metrics_list = get_market_metrics(session, symbols)
        # ... build dict
    except Exception as e:
        print(f"[ERROR] Failed to fetch market metrics: {e}")
        print(f"[INFO] Proceeding without earnings/liquidity filtering")
        return {}  # Empty dict - all symbols will skip filtering
```

#### EC7: Invalid Expiration Dates

**Scenario**: No expirations within tolerance of target DTE

**Current Behavior**: `nearest_expiration()` returns None

**Desired Behavior**:
```python
async def scan_symbol(...):
    front_exp_date = nearest_expiration(chain, front_dte, dte_tolerance)
    back_exp_date = nearest_expiration(chain, back_dte, dte_tolerance)

    if not front_exp_date:
        print(f"[WARN] {symbol}: No expiration near {front_dte} DTE (tolerance {dte_tolerance}), skipping")
        return []

    if not back_exp_date:
        print(f"[WARN] {symbol}: No expiration near {back_dte} DTE (tolerance {dte_tolerance}), skipping")
        return []

    # ... rest of logic
```

#### EC8: Empty Results

**Scenario**: All symbols filtered out, no opportunities found

**Current Behavior**: Empty results list

**Desired Behavior**:
```python
async def main():
    # ... scanning logic ...

    if not results:
        print("\n[INFO] No opportunities found matching criteria")
        print("[INFO] Suggestions:")
        print("  - Lower --min-ff threshold")
        print("  - Reduce --min-liquidity-rating")
        print("  - Use --allow-earnings")
        print("  - Widen --dte-tolerance")
        return

    # ... CSV writing
```

### Logging Levels

**[ERROR]**: Fatal errors that prevent scan from continuing
- API call failures (if critical)
- Invalid arguments (caught in validation)

**[WARN]**: Non-fatal issues that skip individual symbols/legs
- Greeks timeout
- No strikes within delta tolerance
- Negative forward variance
- Missing expiration dates

**[INFO]**: Informational messages about filtering
- Missing earnings/liquidity data (proceeding anyway)
- Symbols filtered due to earnings/liquidity
- No opportunities found

**[FILTERED]**: Special prefix for `--show-earnings-conflicts`
- Filtered symbols with hypothetical FF values

### Error Recovery Strategy

**Principle**: Never crash mid-scan. Skip problematic symbols and continue.

```python
async def main():
    # ... setup ...

    results = []
    for symbol in args.tickers:
        try:
            symbol_results = await scan_symbol(session, symbol, ...)
            results.extend(symbol_results)
        except Exception as e:
            print(f"[ERROR] Failed to scan {symbol}: {e}")
            print(f"[INFO] Continuing with remaining symbols...")
            continue  # Don't let one symbol crash entire scan

    # ... output results
```

## Deliverables

- [ ] Missing earnings data handling (EC1)
- [ ] Missing liquidity rating handling (EC2)
- [ ] Greeks timeout handling (EC3)
- [ ] No delta strikes handling (EC4)
- [ ] Negative forward variance handling (EC5)
- [ ] API call failure handling (EC6)
- [ ] Invalid expiration handling (EC7)
- [ ] Empty results handling (EC8)
- [ ] Per-symbol try/except wrapper in main loop
- [ ] Consistent logging levels ([ERROR], [WARN], [INFO], [FILTERED])

## Testing Checklist

- [ ] Test with symbol that has no earnings data (e.g., ETF)
- [ ] Test with obscure symbol that may lack liquidity data
- [ ] Test with `--timeout 0.1` to force Greeks timeouts
- [ ] Test with `--delta-tolerance 0.01` to force "no strikes" scenario
- [ ] Test with extreme IV backwardation (negative fwd_var)
- [ ] Test with network disconnected (API failure simulation)
- [ ] Test with `--dte-tolerance 1` on day before expiration (no valid expirations)
- [ ] Test with all symbols filtered out (empty results)
- [ ] Verify no crashes in any scenario
- [ ] Verify scan continues after individual symbol failures

## Acceptance Criteria

- ✅ Scanner never crashes mid-scan (all exceptions caught)
- ✅ Missing earnings/liquidity data handled gracefully (proceed without filtering)
- ✅ Greeks timeout handled (skip symbol with warning)
- ✅ No delta strikes handled (skip double calendar for that symbol)
- ✅ Negative forward variance handled (skip that calendar)
- ✅ API failures handled (log error, proceed without data)
- ✅ Invalid expirations handled (skip symbol with warning)
- ✅ Empty results handled (helpful suggestions printed)
- ✅ Logging levels consistent and informative
- ✅ Per-symbol error recovery prevents full scan failure

## Notes

- **Fail Gracefully**: User expects partial results, not crashes
- **Informative Logging**: User should understand WHY symbols were skipped
- **Continue on Error**: One bad symbol shouldn't block rest of scan
- **Helpful Suggestions**: If no results, guide user on how to adjust filters
- **Consistent Prefixes**: [ERROR], [WARN], [INFO], [FILTERED] for easy parsing
