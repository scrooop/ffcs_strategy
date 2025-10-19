---
id: 01
name: Market Metrics Integration
status: todo
priority: critical
estimated_hours: 3-4
dependencies: []
phase: 1
created: 2025-10-19T08:35:09Z
---

# Task 01: Market Metrics Integration

## Objective

Implement batched market metrics fetching to enable earnings and liquidity filtering before expensive Greeks streaming operations.

## Scope

Add earnings date filtering and liquidity screening using tastytrade's `get_market_metrics()` API in a single batched call.

## Technical Details

### Files to Modify
- `scripts/ff_tastytrade_scanner.py`

### New Functions to Add

#### 1. `fetch_market_metrics()`
```python
async def fetch_market_metrics(session: Session, symbols: List[str]) -> Dict[str, MarketMetricInfo]:
    """
    Batch fetch market metrics (earnings + liquidity) for all symbols.

    Args:
        session: tastytrade Session
        symbols: List of ticker symbols

    Returns:
        Dict mapping symbol → MarketMetricInfo

    Example:
        metrics = await fetch_market_metrics(session, ['SPY', 'QQQ', 'AAPL'])
        spy_metrics = metrics.get('SPY')
        if spy_metrics.earnings and spy_metrics.earnings.expected_report_date:
            print(f"SPY earnings: {spy_metrics.earnings.expected_report_date}")
    """
    from tastytrade.metrics import get_market_metrics

    # Batch fetch all symbols in one API call
    metrics_list = get_market_metrics(session, symbols)

    # Build dict mapping symbol → MarketMetricInfo
    metrics_dict = {}
    for metric in metrics_list:
        metrics_dict[metric.symbol] = metric

    return metrics_dict
```

#### 2. `check_earnings_conflict()`
```python
def check_earnings_conflict(
    symbol: str,
    metrics: Dict[str, MarketMetricInfo],
    back_expiry: date,
    today: date,
    allow_earnings: bool = False
) -> Tuple[bool, Optional[str]]:
    """
    Check if earnings date conflicts with position window.

    Args:
        symbol: Ticker symbol
        metrics: Market metrics dict from fetch_market_metrics()
        back_expiry: Back expiration date
        today: Current date (NY timezone)
        allow_earnings: If True, skip filtering

    Returns:
        (passes_filter, reason_if_filtered)

    Example:
        passes, reason = check_earnings_conflict('AAPL', metrics, date(2025,11,5), date(2025,10,19))
        if not passes:
            print(f"[WARN] Skipping AAPL: {reason}")
    """
    if allow_earnings:
        return True, None

    metric = metrics.get(symbol)
    if not metric or not metric.earnings:
        # No earnings data available - proceed without filtering
        return True, None

    earnings_date = metric.earnings.expected_report_date
    if not earnings_date:
        return True, None

    # Check if earnings falls between today and back_expiry (inclusive)
    if today <= earnings_date <= back_expiry:
        reason = f"Earnings on {earnings_date} conflicts with back expiry {back_expiry}"
        return False, reason

    return True, None
```

#### 3. `check_liquidity()`
```python
def check_liquidity(
    symbol: str,
    metrics: Dict[str, MarketMetricInfo],
    min_rating: int,
    skip_check: bool = False
) -> Tuple[bool, Optional[str]]:
    """
    Check if symbol meets minimum liquidity threshold.

    Args:
        symbol: Ticker symbol
        metrics: Market metrics dict
        min_rating: Minimum liquidity rating (0-5 scale)
        skip_check: If True, skip filtering

    Returns:
        (passes_filter, reason_if_filtered)

    Example:
        passes, reason = check_liquidity('AAPL', metrics, min_rating=3)
        if not passes:
            print(f"[INFO] {reason}")
    """
    if skip_check:
        return True, None

    metric = metrics.get(symbol)
    if not metric:
        # No metrics data - proceed without filtering
        return True, None

    if metric.liquidity_rating is None:
        # No liquidity rating - log warning but proceed
        reason = f"{symbol}: No liquidity rating available"
        return True, reason  # Still passes, but with warning

    if metric.liquidity_rating < min_rating:
        reason = f"{symbol}: liquidity_rating={metric.liquidity_rating} < {min_rating}"
        return False, reason

    return True, None
```

### CLI Flags to Add

Update `argparse` setup in `main()`:

```python
# Earnings filtering
parser.add_argument('--skip-earnings', action='store_true', default=True,
                    help='Skip positions with earnings conflicts (default: True)')
parser.add_argument('--allow-earnings', action='store_true', default=False,
                    help='Allow trading through earnings (overrides --skip-earnings)')
parser.add_argument('--show-earnings-conflicts', action='store_true',
                    help='Show filtered positions due to earnings with hypothetical FF')

# Liquidity screening
parser.add_argument('--min-liquidity-rating', type=int, default=3,
                    help='Minimum liquidity rating (0-5 scale, default: 3)')
parser.add_argument('--skip-liquidity-check', action='store_true',
                    help='Disable liquidity filtering')
```

### Integration Points

Modify `async def main()`:

```python
async def main():
    args = parse_args()

    # ... existing session setup ...

    # NEW: Batch fetch market metrics before main loop
    print(f"Fetching market metrics for {len(args.tickers)} symbols...")
    market_metrics = await fetch_market_metrics(session, args.tickers)

    results = []
    for symbol in args.tickers:
        # NEW: Pre-filter for earnings conflicts
        for front_dte, back_dte in args.pairs:
            # Find back expiration date (need this for earnings check)
            chain = await NestedOptionChain.get(session, symbol)
            back_expiry = nearest_expiration(chain, back_dte, args.dte_tolerance)

            if back_expiry:
                passes, reason = check_earnings_conflict(
                    symbol, market_metrics, back_expiry, ny_today(), args.allow_earnings
                )
                if not passes:
                    if args.show_earnings_conflicts:
                        print(f"[FILTERED] {symbol} {front_dte}-{back_dte}: {reason}")
                        # TODO: Still calculate FF for learning mode
                    else:
                        print(f"[WARN] Skipping {symbol}: {reason}")
                    continue

        # NEW: Pre-filter for liquidity
        passes, reason = check_liquidity(symbol, market_metrics, args.min_liquidity_rating, args.skip_liquidity_check)
        if not passes:
            print(f"[INFO] {reason}, skipping")
            continue

        # ... existing scanning logic ...
```

## Deliverables

- [ ] `fetch_market_metrics()` function implemented
- [ ] `check_earnings_conflict()` filter function implemented
- [ ] `check_liquidity()` filter function implemented
- [ ] CLI flags added: `--skip-earnings`, `--allow-earnings`, `--show-earnings-conflicts`, `--min-liquidity-rating`, `--skip-liquidity-check`
- [ ] Integration into main loop complete
- [ ] Console logging added for filtering actions

## Testing Checklist

- [ ] Test with AAPL (known earnings): verify filtering works
- [ ] Test with `--allow-earnings`: verify filtering is disabled
- [ ] Test with `--show-earnings-conflicts`: verify filtered positions are shown
- [ ] Test with `--min-liquidity-rating 4`: verify low-liquidity symbols are filtered
- [ ] Test with `--skip-liquidity-check`: verify liquidity filtering is disabled
- [ ] Test batch API call with 10+ symbols: verify single API call made
- [ ] Test with symbol that has no earnings data: verify graceful handling

## Acceptance Criteria

- ✅ Earnings filtering prevents positions spanning earnings events
- ✅ Liquidity filtering removes symbols with rating < threshold
- ✅ `--show-earnings-conflicts` reveals filtered opportunities with reasons
- ✅ Console output clearly indicates why symbols were filtered
- ✅ No additional API calls per symbol (single batched call)
- ✅ Graceful handling when earnings/liquidity data unavailable

## Notes

- **API Call Batching**: Critical for performance - must fetch ALL symbols in one `get_market_metrics()` call
- **Earnings Date Accuracy**: If `earnings.estimated == True`, consider logging warning
- **Backward Compatibility**: `--allow-earnings` overrides default `--skip-earnings` behavior
- **Learning Mode**: `--show-earnings-conflicts` helps validate filtering logic
