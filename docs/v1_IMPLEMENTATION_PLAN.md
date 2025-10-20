# Forward Factor Scanner - Feature Implementation Plan

## Overview
This document outlines the detailed implementation plan for adding four critical features to the FF scanner, based on the YouTube video transcript requirements.

---

## Feature 1: Earnings Date Filtering ✅ CRITICAL

### Objective
Filter out positions with earnings events between entry (today) and back expiration, as the transcript explicitly states:
> "For simplicity and consistency, it's easiest for most traders to avoid trading this strategy through earnings, meaning no earnings events should occur between your entry and the second expiration."

### API Resources Available

**Option A: Market Metrics API (PREFERRED)**
- Endpoint: `get_market_metrics(session, symbols)`
- Returns: `MarketMetricInfo` with embedded `EarningsReport`
- Fields:
  - `earnings.expected_report_date: date | None` - Next earnings date
  - `earnings.estimated: bool` - Whether date is estimated
  - `earnings.time_of_day: str | None` - "Before Market", "After Market", etc.

**Option B: Historical Earnings API**
- Endpoint: `get_earnings(session, symbol, start_date)`
- Returns: List of `EarningsInfo` with `occurred_date: date`
- Use for historical data only

### Implementation Steps

1. **Fetch Earnings Data**
   ```python
   from tastytrade.metrics import get_market_metrics

   async def get_earnings_dates(session, symbols):
       metrics = get_market_metrics(session, symbols)
       earnings_map = {}
       for m in metrics:
           if m.earnings and m.earnings.expected_report_date:
               earnings_map[m.symbol] = m.earnings.expected_report_date
       return earnings_map
   ```

2. **Check Earnings Window**
   ```python
   def has_earnings_in_window(earnings_date, today, back_expiration):
       """
       Returns True if earnings falls between today and back_expiration (inclusive).
       """
       if earnings_date is None:
           return False
       return today <= earnings_date <= back_expiration
   ```

3. **Integration Points**
   - Call `get_earnings_dates()` **once per scan** (before main loop)
   - Check earnings for each symbol **before** processing DTE pairs
   - Add `--skip-earnings` flag (default: True)
   - Add `--show-earnings-conflicts` flag to display filtered positions

4. **Output Changes**
   - Add `earnings_date` column to CSV/JSON output
   - Add `earnings_conflict` boolean column
   - Print warning: `"[WARN] Skipping {symbol}: earnings on {date} conflicts with {back_exp}"`

5. **CLI Flags**
   ```bash
   --skip-earnings          # Skip positions with earnings conflicts (default: True)
   --allow-earnings         # Allow trading through earnings
   --show-earnings-conflicts # Show positions that were filtered due to earnings
   ```

### Testing
- Test with AAPL (frequent earnings)
- Test with SPY (no earnings)
- Verify filtering works for 30-60, 30-90, 60-90 DTE pairs

---

## Feature 2: Liquidity Filters 🔍 IMPORTANT

### Objective
Implement 20-day average option volume filter as stated in transcript:
> "We only traded names with a twenty day average option volume above ten thousand contracts per day."

### API Resources Available

**MarketMetricInfo Fields:**
- `liquidity_value: Decimal | None` - Numerical liquidity score
- `liquidity_rank: Decimal | None` - Percentile rank (0-100)
- `liquidity_rating: int | None` - Rating scale (0-5)
- `liquidity_running_state: Liquidity | None` - Real-time liquidity tracking
  - `sum: Decimal` - Total liquidity value
  - `count: int` - Number of data points
  - `started_at: datetime`
  - `updated_at: datetime | None`

**Problem:** The API does **not** directly provide "20-day avg option volume". We have two approaches:

### Implementation Approach

**Approach A: Use Liquidity Rating as Proxy (RECOMMENDED)**
```python
def meets_liquidity_threshold(market_metric):
    """
    Use tastytrade's liquidity_rating (0-5 scale).
    Rating >= 3 generally indicates >10k contracts/day.
    """
    if market_metric.liquidity_rating is None:
        return False
    return market_metric.liquidity_rating >= 3  # Adjust threshold as needed
```

**Approach B: Fetch Historical Option Volume** (More Accurate, More Complex)
- Would require historical data fetching per symbol
- Not currently available in tastytrade SDK
- **NOT RECOMMENDED** for v1 implementation

### Implementation Steps

1. **Fetch Liquidity Data**
   - Already fetched via `get_market_metrics()` (same call as earnings)
   - No additional API calls needed

2. **Filter by Liquidity**
   ```python
   def check_liquidity(symbol, market_metrics, min_rating=3):
       metric = market_metrics.get(symbol)
       if not metric or metric.liquidity_rating is None:
           return False, "No liquidity data"

       if metric.liquidity_rating < min_rating:
           return False, f"Liquidity rating {metric.liquidity_rating} < {min_rating}"

       return True, None
   ```

3. **CLI Flags**
   ```bash
   --min-liquidity-rating 3  # Minimum liquidity rating (0-5, default: 3)
   --skip-liquidity-check    # Disable liquidity filtering
   ```

4. **Output Changes**
   - Add `liquidity_rating` column
   - Add `liquidity_value` column
   - Print: `"[INFO] {symbol}: liquidity_rating={rating}"`

### Testing
- Test with SPY (highly liquid, rating=5)
- Test with low-liquidity stocks
- Verify threshold works correctly

---

## Feature 3: X-earn IV Support 📊 ADVANCED

### Objective
Use earnings-removed implied volatility as stated:
> "For all our calculations and all the research we'll discuss here, we use earn implied volatility. That's implied volatility with the earnings implied volatility removed."

### API Resources Available

**OptionExpirationImpliedVolatility** (nested in MarketMetricInfo):
```python
option_expiration_implied_volatilities: list[OptionExpirationImpliedVolatility] | None
```

Each `OptionExpirationImpliedVolatility` contains:
- `expiration_date: date`
- `implied_volatility: Decimal | None`
- `settlement_type: str`
- `option_chain_type: str`

**Key Question:** Does `implied_volatility` represent X-earn IV or regular IV?
- **Unknown from docs** - needs testing/validation
- **Alternative:** Continue using dxFeed Greeks IV (current approach)

### Implementation Approach

**Option A: Use MarketMetricInfo.option_expiration_implied_volatilities (INVESTIGATE FIRST)**
```python
def get_xearn_iv_from_market_metrics(market_metric, expiration_date):
    """
    Try to extract X-earn IV for a specific expiration from market metrics.
    """
    if not market_metric.option_expiration_implied_volatilities:
        return None

    for exp_iv in market_metric.option_expiration_implied_volatilities:
        if exp_iv.expiration_date == expiration_date:
            return float(exp_iv.implied_volatility) if exp_iv.implied_volatility else None

    return None
```

**Option B: Continue with Current Approach + Earnings Filter (SIMPLER)**
- Keep using dxFeed Greeks IV (current implementation)
- Rely on earnings filtering to avoid earnings-juiced IV
- **This is effectively "X-earn" by avoiding earnings entirely**

### Implementation Steps (Option A - if API supports it)

1. **Test OptionExpirationImpliedVolatility**
   - Fetch for a symbol with upcoming earnings
   - Compare IV values before/after earnings
   - Determine if it's X-earn or regular IV

2. **Integration** (if test confirms it's X-earn IV)
   ```python
   # Replace current dxFeed Greeks IV fetch with:
   iv = get_xearn_iv_from_market_metrics(market_metric, expiration_date)
   if iv is None:
       # Fallback to dxFeed Greeks
       iv = get_iv_from_greeks(...)
   ```

3. **CLI Flags**
   ```bash
   --use-xearn-iv          # Use X-earn IV from market metrics (if available)
   --force-greeks-iv       # Always use dxFeed Greeks IV (current behavior)
   ```

### Recommendation
**Start with Option B** (earnings filtering only) for v1.0. Add X-earn IV in v1.1 after validation.

---

## Feature 4: Double Calendar Scanner (±35Δ) 🎯 ENHANCEMENT

### Objective
Support double calendar structure as described:
> "We also explored the long 35 delta double calendar... selling richer front period SKU and owning relatively cheaper back period SKU"

Structure:
- **+35Δ call calendar** (sell front +35Δ call, buy back +35Δ call)
- **-35Δ put calendar** (sell front -35Δ put, buy back -35Δ put)
- ±5Δ tolerance acceptable

### API Resources Available

**NestedOptionChain already provides:**
- `.strikes[]` with `.call_streamer_symbol` and `.put_streamer_symbol`
- BUT: No delta information directly

**dxFeed Greeks provides:**
- `Greeks.delta: Decimal` - option delta

### Implementation Approach

**Step 1: Find ±35Δ Strikes**
```python
async def find_delta_strike(session, expiration_obj, spot, target_delta, is_call, tolerance=0.05):
    """
    Find strike with delta closest to target_delta.

    Args:
        target_delta: +0.35 for calls, -0.35 for puts
        tolerance: ±0.05 (i.e., 0.30 to 0.40 acceptable)
    """
    # Get all strikes
    strikes = expiration_obj.strikes

    # Get Greeks for all strikes
    symbols = [s.call_streamer_symbol if is_call else s.put_streamer_symbol
               for s in strikes]
    greeks_map = await snapshot_greeks(session, symbols)

    # Find strike with delta closest to target
    best_strike = None
    best_delta_error = None

    for strike in strikes:
        symbol = strike.call_streamer_symbol if is_call else strike.put_streamer_symbol
        greeks = greeks_map.get(symbol)

        if not greeks or greeks.delta is None:
            continue

        delta = float(greeks.delta)
        error = abs(delta - target_delta)

        if error <= tolerance and (best_delta_error is None or error < best_delta_error):
            best_delta_error = error
            best_strike = strike

    return best_strike
```

**Step 2: Compute Double Calendar FF**
```python
async def scan_double_calendar(session, symbol, front_dte, back_dte, spot):
    """
    Scan for double calendar opportunity.

    Returns:
        - Front +35Δ call / Back +35Δ call
        - Front -35Δ put / Back -35Δ put
        - Combined FF (average or weighted)
    """
    # Find strikes for front and back
    front_call_35d = await find_delta_strike(session, front_exp, spot, 0.35, is_call=True)
    back_call_35d = await find_delta_strike(session, back_exp, spot, 0.35, is_call=True)
    front_put_35d = await find_delta_strike(session, front_exp, spot, -0.35, is_call=False)
    back_put_35d = await find_delta_strike(session, back_exp, spot, -0.35, is_call=False)

    # Get IVs for all legs
    # Compute FF for call calendar
    # Compute FF for put calendar
    # Return combined result
```

### Implementation Steps

1. **Add `--structure` CLI flag**
   ```bash
   --structure atm-call     # ATM call calendar (current, default)
   --structure double       # Double calendar (±35Δ)
   --structure both         # Scan both structures
   ```

2. **Modify scan() function**
   - Add delta-based strike selection
   - Compute FF for both call and put calendars
   - Output separate rows or combined row

3. **Output Changes**
   ```csv
   symbol,structure,front_dte,back_dte,call_strike,put_strike,call_ff,put_ff,combined_ff
   SPY,double,30,60,580.0,560.0,0.25,0.23,0.24
   ```

4. **CLI Flags**
   ```bash
   --structure {atm-call,double,both}  # Calendar structure type
   --delta-tolerance 0.05              # Max deviation from ±35Δ (default: 0.05)
   ```

### Testing
- Test with SPY (liquid, many strikes)
- Verify delta calculations
- Compare results to ATM calendar

---

## Implementation Priority & Timeline

### Phase 1: Critical Features (Week 1)
1. ✅ Earnings Date Filtering - **3-4 hours**
2. ✅ Liquidity Filters - **2-3 hours**

### Phase 2: Advanced Features (Week 2)
3. ⏸️ X-earn IV Support - **4-6 hours** (investigate first)
4. ✅ Double Calendar Scanner - **6-8 hours**

### Total Effort: 15-21 hours

---

## Testing Strategy

### Unit Tests
- `test_earnings_filtering()` - Verify earnings date logic
- `test_liquidity_threshold()` - Verify liquidity rating filtering
- `test_delta_strike_selection()` - Verify 35Δ strike finding
- `test_double_calendar_ff()` - Verify FF calculation for double calendar

### Integration Tests
- Run full scan with earnings filtering
- Run full scan with liquidity filtering
- Run full scan with double calendar structure
- Compare results to manual validation

### Live Testing
```bash
# Test earnings filtering
python scripts/ff_tastytrade_scanner.py --tickers AAPL --pairs 30-60 --skip-earnings

# Test liquidity filtering
python scripts/ff_tastytrade_scanner.py --tickers SPY QQQ --pairs 30-60 --min-liquidity-rating 4

# Test double calendar
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 60-90 --structure double --min-ff 0.20
```

---

## API Call Optimization

**Current:**
- 1x `get_market_data()` per symbol
- 1x `NestedOptionChain.get()` per symbol
- 1x `snapshot_greeks()` per symbol (for 2-6 ATM strikes)

**After All Features:**
- 1x `get_market_metrics()` for ALL symbols (batched, adds earnings + liquidity)
- 1x `get_market_data()` per symbol (unchanged)
- 1x `NestedOptionChain.get()` per symbol (unchanged)
- 1x `snapshot_greeks()` per symbol (4-12 strikes for double calendar)

**Net impact:** +1 batched API call, +2-6 Greeks subscriptions per symbol

---

## Documentation Updates

All documentation files must be updated with:
- New CLI flags and their defaults
- Earnings filtering behavior
- Liquidity filtering criteria
- Double calendar structure explanation
- Example commands for each feature

Files to update:
- `CLAUDE.md`
- `scripts/README_TT.md`
- `docs/gpt-setup-instructions1.txt`
