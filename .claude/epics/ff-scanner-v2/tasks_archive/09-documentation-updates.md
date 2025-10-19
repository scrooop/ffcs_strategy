---
id: 09
name: Documentation Updates
status: todo
priority: medium
estimated_hours: 2-3
dependencies: [01, 02, 03, 04, 05, 06, 07]
phase: 4
created: 2025-10-19T08:35:09Z
---

# Task 09: Documentation Updates

## Objective

Update all project documentation to reflect v2.0 features, new CLI flags, usage examples, and implementation details.

## Scope

Update `CLAUDE.md`, `scripts/README_TT.md`, and add comprehensive docstrings to all new functions.

## Technical Details

### Files to Update

1. **CLAUDE.md** (project instructions)
2. **scripts/README_TT.md** (scanner usage guide)
3. **docs/gpt-setup-instructions1.txt** (if needed)
4. **scripts/ff_tastytrade_scanner.py** (function docstrings)

### Documentation Changes Required

#### 1. Update CLAUDE.md

**Section to Add**: "Scanner v2.0 Features and Usage"

```markdown
## FF Scanner v2.0 Features (Enhanced Quality Filtering)

### New Features

**Earnings Date Filtering**:
- Automatically excludes positions spanning earnings events
- Uses tastytrade `get_market_metrics()` API for earnings dates
- CLI: `--skip-earnings` (default), `--allow-earnings`, `--show-earnings-conflicts`

**Liquidity Screening**:
- Filters symbols by tastytrade liquidity rating (0-5 scale)
- Default threshold: rating ≥ 3 (approx. 10k contracts/day)
- CLI: `--min-liquidity-rating N`, `--skip-liquidity-check`

**X-earn IV Support** (if available):
- Attempts to use earnings-removed IV from market metrics
- Falls back to dxFeed Greeks IV if unavailable
- CLI: `--use-xearn-iv` (default), `--force-greeks-iv`
- CSV tracks IV source: `iv_source_front`, `iv_source_back`

**Double Calendar Structure**:
- Scans for ±35Δ call and put calendars in addition to ATM
- Computes separate FFs for call and put calendars
- Combined FF = (call_ff + put_ff) / 2
- CLI: `--structure {atm-call,double,both}` (default: both)

### Usage Examples

**Daily Pre-Market Scan** (production):
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL TSLA NVDA META AMZN GOOGL MSFT AMD \
  --pairs 30-60 30-90 60-90 \
  --min-ff 0.23 \
  --structure both \
  --csv-out "$(date +%y%m%d_%H%M)_ff_scan.csv"
```

**Focus on Double Calendars** (60-90 DTE):
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ IWM \
  --pairs 60-90 \
  --structure double \
  --min-ff 0.20 \
  --csv-out double_calendars.csv
```

**Debug: Why didn't AAPL show up?**
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers AAPL \
  --pairs 30-60 \
  --show-earnings-conflicts \
  --skip-liquidity-check
```

### CSV Output Schema (v2.0)

25 columns including:
- **Structure indicators**: `structure`, `atm_strike`, `call_strike`, `put_strike`
- **Earnings data**: `earnings_date`, `earnings_conflict`
- **Liquidity metrics**: `liquidity_rating`, `liquidity_value`
- **Double calendar**: `call_delta`, `put_delta`, `call_ff`, `put_ff`, `combined_ff`
- **IV source tracking**: `iv_source_front`, `iv_source_back`

See PRD Appendix B for full schema.

### Performance

- 10-symbol scan: ~25 seconds
- 20-symbol scan: ~50 seconds
- Market metrics batch call: +2 seconds overhead (one-time per scan)
```

#### 2. Update scripts/README_TT.md

**Sections to Add/Update**:

```markdown
# FF Scanner v2.0 - Enhanced Quality Filtering

## Quick Start

### Basic Scan (All Features Enabled)
```bash
python ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL \
  --pairs 30-60 30-90 \
  --min-ff 0.23 \
  --csv-out scan.csv
```

Default behavior (v2.0):
- ✅ Earnings conflicts filtered out (`--skip-earnings`)
- ✅ Liquidity rating ≥ 3 required (`--min-liquidity-rating 3`)
- ✅ X-earn IV used if available (`--use-xearn-iv`)
- ✅ Both ATM and double calendars scanned (`--structure both`)

## CLI Flags Reference

### Core Scanning (v1.0)
- `--tickers`: Space-separated symbols (required)
- `--pairs`: DTE pairs like `30-60 30-90` (required)
- `--min-ff`: Minimum Forward Factor (default: 0.20)
- `--dte-tolerance`: Max DTE deviation (default: 5 days)
- `--timeout`: Greeks snapshot timeout (default: 3s)
- `--csv-out`: Output CSV file path
- `--sandbox`: Use sandbox environment (not recommended)

### Earnings Filtering (v2.0)
- `--skip-earnings`: Skip positions with earnings conflicts (default: True)
- `--allow-earnings`: Allow trading through earnings
- `--show-earnings-conflicts`: Show filtered positions with reasons

### Liquidity Screening (v2.0)
- `--min-liquidity-rating N`: Minimum liquidity rating 0-5 (default: 3)
- `--skip-liquidity-check`: Disable liquidity filtering

### IV Data Source (v2.0)
- `--use-xearn-iv`: Use X-earn IV from market metrics (default: True)
- `--force-greeks-iv`: Always use dxFeed Greeks IV

### Calendar Structure (v2.0)
- `--structure {atm-call,double,both}`: Structure type (default: both)
- `--delta-tolerance N`: Max delta deviation for double calendars (default: 0.05)

## Common Workflows

### 1. Daily Pre-Market Scan
```bash
python ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL TSLA NVDA META AMZN GOOGL MSFT AMD \
  --pairs 30-60 30-90 60-90 \
  --min-ff 0.23 \
  --structure both \
  --csv-out "$(date +%y%m%d_%H%M)_ff_scan.csv"
```

**Expected outcome**: 3-5 high-quality opportunities (filtered from 15-20 raw)

### 2. Structure-Specific Scanning

**ATM call calendars only** (simpler, cheaper):
```bash
python ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 \
  --structure atm-call \
  --min-ff 0.23
```

**Double calendars only** (higher win rate):
```bash
python ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 60-90 \
  --structure double \
  --min-ff 0.20
```

### 3. Debugging Filtered Opportunities

**Why didn't AAPL show up?**
```bash
python ff_tastytrade_scanner.py \
  --tickers AAPL \
  --pairs 30-60 \
  --show-earnings-conflicts
```

Output:
```
[FILTERED] AAPL 30-60: Earnings on 2025-11-01 conflicts with back expiry 2025-11-05
           FF would have been: 0.28 (Strong opportunity, but earnings risk)
           Liquidity Rating: 5 (Excellent)
```

## CSV Output Format

v2.0 CSV contains 25 columns. Key additions:
- `structure`: "atm-call" or "double"
- `earnings_date`, `earnings_conflict`: Earnings risk indicators
- `liquidity_rating`, `liquidity_value`: Liquidity metrics
- `call_strike`, `put_strike`, `call_delta`, `put_delta`: Double calendar details
- `call_ff`, `put_ff`, `combined_ff`: Forward Factors by structure
- `iv_source_front`, `iv_source_back`: "xearn" or "greeks"

CSV is sorted by `combined_ff` descending (highest opportunities first).

## Troubleshooting

**Problem**: No results returned
- **Cause**: Thresholds too strict (high min_ff, high liquidity rating, earnings conflicts)
- **Solution**: Lower `--min-ff` to 0.15, try `--min-liquidity-rating 2`, use `--allow-earnings`

**Problem**: "X-earn IV unavailable" warnings
- **Cause**: Market metrics API may not provide X-earn IV data
- **Solution**: This is expected - scanner falls back to Greeks IV automatically

**Problem**: "No strikes found within delta tolerance"
- **Cause**: Weekly expirations or illiquid symbols may lack ±35Δ strikes
- **Solution**: Widen `--delta-tolerance` to 0.10, or use `--structure atm-call`

**Problem**: Scan takes > 60 seconds for 20 symbols
- **Cause**: Network latency or API throttling
- **Solution**: Check internet connection, try during off-peak hours

## API Rate Limits

Scanner makes:
- 1x `get_market_metrics()` call for ALL symbols (batched)
- 1x `get_market_data()` call per symbol
- 1x `NestedOptionChain.get()` call per symbol
- 1x `snapshot_greeks()` call per symbol (4-12 strikes depending on structure)

Total: ~4 API calls per symbol + 1 batched call per scan.
```

#### 3. Update Function Docstrings

Add comprehensive docstrings to all new functions:

```python
async def fetch_market_metrics(session: Session, symbols: List[str]) -> Dict[str, MarketMetricInfo]:
    """
    Batch fetch market metrics (earnings + liquidity) for all symbols.

    Args:
        session: tastytrade Session
        symbols: List of ticker symbols

    Returns:
        Dict mapping symbol → MarketMetricInfo

    Raises:
        tastytrade.APIError: If API call fails

    Example:
        >>> metrics = await fetch_market_metrics(session, ['SPY', 'QQQ'])
        >>> spy_earnings = metrics['SPY'].earnings.expected_report_date
        >>> spy_liquidity = metrics['SPY'].liquidity_rating
    """
```

**Functions requiring docstrings**:
- `fetch_market_metrics()`
- `check_earnings_conflict()`
- `check_liquidity()`
- `find_delta_strikes()`
- `scan_symbol()`
- `scan_atm_calendar()`
- `scan_double_calendar()`
- `extract_xearn_iv()`
- `get_iv_for_expiration()`
- `write_csv()`
- `print_summary()`
- `validate_args()`

## Deliverables

- [ ] CLAUDE.md updated with v2.0 features and examples
- [ ] scripts/README_TT.md completely rewritten for v2.0
- [ ] All new functions have comprehensive docstrings
- [ ] Docstrings include type hints, examples, and exception documentation
- [ ] docs/gpt-setup-instructions1.txt updated (if needed)
- [ ] README examples match PRD Appendix C scenarios

## Testing Checklist

- [ ] CLAUDE.md examples run successfully
- [ ] README_TT.md examples run successfully
- [ ] Docstring examples are accurate (no typos in function signatures)
- [ ] All CLI flags documented match actual implementation
- [ ] Troubleshooting section covers common issues from testing

## Acceptance Criteria

- ✅ CLAUDE.md comprehensively documents v2.0 features
- ✅ README_TT.md enables new user to run scanner without external help
- ✅ All new functions have docstrings with type hints and examples
- ✅ Examples in docs match actual working commands (tested)
- ✅ CLI flags documentation matches `--help` output
- ✅ Troubleshooting section addresses common issues

## Notes

- **User-First Documentation**: Write for trader who has never seen v2.0 before
- **Working Examples**: Test all examples before committing to docs
- **Docstring Style**: Follow Google Python Style Guide
- **Keep Updated**: Update docs in parallel with code changes (don't defer to end)
