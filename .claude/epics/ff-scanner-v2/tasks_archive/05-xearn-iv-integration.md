---
id: 05
name: X-earn IV Integration
status: todo
priority: medium
estimated_hours: 2-3
dependencies: []
phase: 3
created: 2025-10-19T08:35:09Z
---

# Task 05: X-earn IV Integration

## Objective

Attempt to extract X-earn IV (earnings-removed implied volatility) from tastytrade's `MarketMetricInfo.option_expiration_implied_volatilities`, with graceful fallback to dxFeed Greeks IV if unavailable.

## Scope

Add X-earn IV extraction with uncertainty handling, track IV source in CSV output, and provide CLI flags to control behavior.

## Technical Details

### Files to Modify
- `scripts/ff_tastytrade_scanner.py`

### New Function to Add

```python
def extract_xearn_iv(
    metrics: Dict[str, MarketMetricInfo],
    symbol: str,
    expiration_date: date
) -> Optional[float]:
    """
    Try to extract X-earn IV from MarketMetricInfo.

    Args:
        metrics: Market metrics dict from fetch_market_metrics()
        symbol: Ticker symbol
        expiration_date: Target expiration date

    Returns:
        X-earn IV as float (decimal, e.g., 0.25 for 25%) or None if unavailable

    Example:
        xearn_iv = extract_xearn_iv(metrics, 'SPY', date(2025,11,21))
        if xearn_iv:
            print(f"X-earn IV: {xearn_iv:.4f}")
        else:
            print("X-earn IV unavailable, using Greeks IV")
    """
    metric = metrics.get(symbol)
    if not metric or not metric.option_expiration_implied_volatilities:
        return None

    # Search for matching expiration
    for exp_iv in metric.option_expiration_implied_volatilities:
        if exp_iv.expiration_date == expiration_date:
            if exp_iv.implied_volatility is not None:
                return float(exp_iv.implied_volatility)

    return None
```

### Integration with FF Calculation

Modify IV extraction logic to try X-earn first, then fall back to Greeks:

```python
async def get_iv_for_expiration(
    session: Session,
    symbol: str,
    expiration_obj,
    spot: float,
    metrics: Dict,
    use_xearn: bool,
    force_greeks: bool
) -> Tuple[Optional[float], str]:
    """
    Get IV for an expiration, trying X-earn first if enabled.

    Returns:
        (iv, source) where source is 'xearn' or 'greeks'
    """
    iv = None
    source = 'greeks'  # Default

    # Try X-earn IV if enabled and not forced to use Greeks
    if use_xearn and not force_greeks:
        iv = extract_xearn_iv(metrics, symbol, expiration_obj.expiration_date)
        if iv is not None:
            source = 'xearn'

    # Fallback to Greeks IV
    if iv is None:
        # Use existing ATM IV extraction via snapshot_greeks()
        atm_strike, call_symbol, put_symbol = pick_atm_strike(expiration_obj, spot)
        greeks_map = await snapshot_greeks(session, [call_symbol, put_symbol])

        # Average call and put IVs (existing logic)
        call_greeks = greeks_map.get(call_symbol)
        put_greeks = greeks_map.get(put_symbol)

        if call_greeks and put_greeks:
            call_iv, _ = call_greeks
            put_iv, _ = put_greeks
            iv = (call_iv + put_iv) / 2.0
            source = 'greeks'

            if use_xearn and not force_greeks:
                # Log warning that X-earn IV was unavailable
                print(f"[WARN] {symbol}: X-earn IV unavailable for {expiration_obj.expiration_date}, using Greeks IV")

    return iv, source
```

### CLI Flags to Add

```python
parser.add_argument('--use-xearn-iv', action='store_true', default=True,
                    help='Use X-earn IV from market metrics if available (default: True)')
parser.add_argument('--force-greeks-iv', action='store_true', default=False,
                    help='Always use dxFeed Greeks IV, never X-earn IV')
```

### CSV Output Enhancement

Add IV source tracking to result dict:

```python
result = {
    # ... existing fields ...
    'iv_source_front': 'xearn' or 'greeks',
    'iv_source_back': 'xearn' or 'greeks',
}
```

## Deliverables

- [ ] `extract_xearn_iv()` function implemented
- [ ] `get_iv_for_expiration()` helper function implemented
- [ ] IV source tracking added to results
- [ ] CLI flags added: `--use-xearn-iv`, `--force-greeks-iv`
- [ ] Fallback logic: X-earn → Greeks
- [ ] Warning logging when X-earn IV unavailable
- [ ] CSV columns added: `iv_source_front`, `iv_source_back`

## Testing Checklist

### Phase 1 Validation (Critical Decision Point)
- [ ] **Test with 5 symbols** (SPY, QQQ, AAPL, TSLA, NVDA)
- [ ] Check if `option_expiration_implied_volatilities` is populated
- [ ] If populated, compare X-earn IV to Greeks IV values
- [ ] **Decision**: If X-earn IV unavailable for ALL symbols → defer FR3 to v2.1

### If X-earn IV is Available
- [ ] Test X-earn IV extraction: verify values are reasonable (0.10-0.50 range)
- [ ] Test fallback: verify Greeks IV used when X-earn unavailable
- [ ] Test `--force-greeks-iv`: verify X-earn IV never used
- [ ] Test `iv_source` tracking: verify correct source logged in CSV
- [ ] Compare FF values: X-earn vs Greeks (should differ around earnings)

## Acceptance Criteria

- ✅ Scanner attempts X-earn IV extraction when `--use-xearn-iv` enabled
- ✅ Graceful fallback to Greeks IV when X-earn unavailable
- ✅ `iv_source` column correctly tracks data source (xearn or greeks)
- ✅ Warning logged when X-earn IV unavailable but requested
- ✅ `--force-greeks-iv` overrides X-earn IV extraction completely
- ✅ **Decision made by end of Day 2**: Ship FR3 or defer to v2.1

## Notes

- **40% Risk of Unavailability**: PRD estimates 40% chance X-earn IV data is not available in API
- **Decision Point**: End of Phase 1 (Day 2) - validate data availability
- **Fallback Strategy**: If X-earn IV unavailable, earnings filtering effectively provides "X-earn" by exclusion
- **Data Quality**: If X-earn IV values seem unrealistic, consider deferring feature
- **CSV Analysis**: `iv_source` column enables post-hoc analysis of X-earn vs Greeks data quality
