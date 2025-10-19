# Issue #4: Double Calendar Strike Selection - Implementation Guide

**Status:** ✅ Completed
**Date:** October 19, 2025
**Epic:** ff-scanner-v2
**Dependencies:** Issue #3 (Enhanced Greeks collection with delta values)

## Overview

Issue #4 implements delta-based strike selection for **double calendar spreads**. The implementation adds three new functions to `ff_tastytrade_scanner.py` that enable selecting strikes at **±35Δ** (with ±5Δ tolerance) using the delta values returned by `snapshot_greeks()`.

### What are Double Calendars?

From the strategy SOP:
- **Double-Calendar**: Higher win rate, more complex structure
  - +35Δ call calendar (sell front call, buy back call)
  - -35Δ put calendar (sell front put, buy back put)
  - ±5Δ tolerance acceptable

## Implementation Details

### New Data Structure

```python
@dataclass(frozen=True)
class DeltaStrikeChoice:
    """Represents a strike selected by delta for double calendars."""
    strike: float
    streamer_symbol: str
    actual_delta: float
    iv: float
```

### Function 1: `pick_delta_strike()`

**Purpose:** Core helper to find a strike matching a target delta.

**Signature:**
```python
def pick_delta_strike(
    expiration_obj,
    greek_map: Dict[str, Greeks],
    target_delta: float,
    delta_tolerance: float = 0.05,
    option_type: str = "call"
) -> Optional[DeltaStrikeChoice]
```

**Parameters:**
- `expiration_obj`: NestedOptionChain expiration object with strikes
- `greek_map`: Dict mapping streamer_symbol → Greeks (with delta values)
- `target_delta`: Target delta (e.g., 0.35 for +35Δ call, -0.35 for -35Δ put)
- `delta_tolerance`: Maximum deviation from target delta (default 0.05 = ±5Δ)
- `option_type`: "call" or "put"

**Returns:**
- `DeltaStrikeChoice` with the strike closest to target delta (within tolerance)
- `None` if no strike found within tolerance

**Algorithm:**
1. Iterate through all strikes in the expiration
2. For each strike, get the Greeks from `greek_map`
3. Calculate delta error: `|actual_delta - target_delta|`
4. Keep track of the strike with minimum error
5. Return only if error ≤ `delta_tolerance`

**Example Usage:**
```python
# Find +35Δ call strike
call_strike = pick_delta_strike(
    expiration_obj=exp_obj,
    greek_map=greeks,
    target_delta=0.35,
    delta_tolerance=0.05,
    option_type="call"
)

if call_strike:
    print(f"Strike: ${call_strike.strike:.2f}")
    print(f"Delta: {call_strike.actual_delta:.4f}")
    print(f"IV: {call_strike.iv:.4f}")
```

### Function 2: `snapshot_greeks_for_range()`

**Purpose:** Efficiently fetch Greeks for multiple strikes around the spot price.

**Signature:**
```python
async def snapshot_greeks_for_range(
    session: Session,
    expiration_obj,
    spot: float,
    range_pct: float = 0.25,
    timeout_s: float = 5.0
) -> Dict[str, Greeks]
```

**Parameters:**
- `session`: tastytrade Session
- `expiration_obj`: NestedOptionChain expiration object
- `spot`: Current underlying spot price
- `range_pct`: Percentage range around spot (default 0.25 = ±25%)
- `timeout_s`: Timeout for Greeks snapshot (default 5s)

**Returns:**
- Dict mapping streamer_symbol → Greeks for all strikes in range

**Algorithm:**
1. Calculate strike range: `[spot × (1 - range_pct), spot × (1 + range_pct)]`
2. Collect streamer symbols for all calls and puts in range
3. Use existing `snapshot_greeks()` to fetch Greeks for all symbols
4. Return the Greeks map

**Why This Function?**
- For ATM calendars, we only need Greeks for 1-2 strikes per expiration
- For double calendars, we need Greeks for many strikes to find ±35Δ
- This function batches the Greeks fetch to minimize API calls

**Example Usage:**
```python
# Fetch Greeks for strikes within ±25% of spot
greeks = await snapshot_greeks_for_range(
    session=session,
    expiration_obj=exp_obj,
    spot=580.00,
    range_pct=0.25,  # ±25% = $435-$725
    timeout_s=5.0
)
# Returns Greeks for ~20-40 strikes (both calls and puts)
```

### Function 3: `get_double_calendar_strikes()`

**Purpose:** High-level wrapper to get both ±35Δ strikes for a double calendar.

**Signature:**
```python
async def get_double_calendar_strikes(
    session: Session,
    expiration_obj,
    spot: float,
    call_target_delta: float = 0.35,
    put_target_delta: float = -0.35,
    delta_tolerance: float = 0.05,
    timeout_s: float = 5.0
) -> Dict[str, Optional[DeltaStrikeChoice]]
```

**Parameters:**
- `session`: tastytrade Session
- `expiration_obj`: NestedOptionChain expiration object
- `spot`: Current underlying spot price
- `call_target_delta`: Target delta for call leg (default 0.35)
- `put_target_delta`: Target delta for put leg (default -0.35)
- `delta_tolerance`: Maximum deviation from target delta (default 0.05)
- `timeout_s`: Timeout for Greeks snapshot (default 5s)

**Returns:**
- Dict with keys `"call_35delta"` and `"put_35delta"`
- Values are `DeltaStrikeChoice` or `None` if no strike found

**Algorithm:**
1. Call `snapshot_greeks_for_range()` to get Greeks for many strikes
2. Call `pick_delta_strike()` for +35Δ call
3. Call `pick_delta_strike()` for -35Δ put
4. Return both results

**Example Usage:**
```python
# Get both ±35Δ strikes for a double calendar
delta_strikes = await get_double_calendar_strikes(
    session=session,
    expiration_obj=exp_obj,
    spot=580.00
)

call_strike = delta_strikes["call_35delta"]
put_strike = delta_strikes["put_35delta"]

if call_strike and put_strike:
    print(f"Call: ${call_strike.strike:.2f} (Δ={call_strike.actual_delta:.4f})")
    print(f"Put:  ${put_strike.strike:.2f} (Δ={put_strike.actual_delta:.4f})")
else:
    print("Could not find both strikes within tolerance")
```

## Testing

A test script is provided: `scripts/test_double_calendar_strikes.py`

**Prerequisites:**
```bash
# Set tastytrade credentials
export TT_USERNAME="your_username"
export TT_PASSWORD="your_password"
```

**Run Test:**
```bash
# Test with SPY at 60 DTE
python scripts/test_double_calendar_strikes.py --ticker SPY --target-dte 60

# Test with QQQ at 30 DTE
python scripts/test_double_calendar_strikes.py --ticker QQQ --target-dte 30 --dte-tolerance 5

# Test with custom ticker
python scripts/test_double_calendar_strikes.py --ticker AAPL --target-dte 45
```

**Expected Output:**
```
======================================================================
Testing Double Calendar Strike Selection
Ticker: SPY | Target DTE: 60
======================================================================

[1/4] Fetching spot price for SPY...
      Spot price: $580.43

[2/4] Fetching option chain...

[3/4] Finding expiration near 60 DTE (±7 days)...
      Selected expiration: 2025-12-19 (61 DTE)

[4/4] Selecting ±35Δ strikes...

======================================================================
RESULTS: Double Calendar Strike Selection
======================================================================

✓ +35Δ CALL:
    Strike:        $590.00
    Actual Delta:  0.3487
    IV:            0.1423 (14.23%)
    Symbol:        .SPY251219C590
    Delta Error:   0.0013

✓ -35Δ PUT:
    Strike:        $570.00
    Actual Delta:  -0.3512
    IV:            0.1389 (13.89%)
    Symbol:        .SPY251219P570
    Delta Error:   0.0012

======================================================================
SUCCESS: Both ±35Δ strikes found within tolerance
Strike Width: $20.00 (3.4% of spot)
======================================================================
```

## Integration into Main Scanner

The functions are now available in `ff_tastytrade_scanner.py` and can be integrated into the main scan flow in future phases.

**Future Integration (Phase 2):**
1. Add `--double-calendar` flag to scanner
2. When enabled, call `get_double_calendar_strikes()` for each expiration
3. Compute forward IV for the ±35Δ strikes (similar to ATM)
4. Report FF ratios for both call and put calendars
5. Add columns: `call_35delta_strike`, `put_35delta_strike`, `call_delta`, `put_delta`

**Example Future Usage:**
```bash
# Scan for double calendars at ±35Δ
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 60-90 \
  --min-ff 0.23 \
  --double-calendar
```

## Code Location

All new code added to: `scripts/ff_tastytrade_scanner.py` (lines 146-277)

- Lines 148-154: `DeltaStrikeChoice` dataclass
- Lines 156-203: `pick_delta_strike()` function
- Lines 205-237: `snapshot_greeks_for_range()` function
- Lines 239-277: `get_double_calendar_strikes()` function

## Design Decisions

### 1. Why ±25% strike range?
- ±35Δ strikes are typically within ±10-15% of spot for equities
- ±25% provides a comfortable buffer for high IV or skewed underlyings
- Can be adjusted via `range_pct` parameter if needed

### 2. Why 5s timeout (vs 3s for ATM)?
- Double calendars require Greeks for 20-40 strikes (vs 2-4 for ATM)
- More data to stream → longer timeout needed
- 5s is a reasonable trade-off between speed and reliability

### 3. Why return None instead of raising exceptions?
- Consistent with existing `pick_atm_strike()` behavior
- Allows scanner to gracefully handle partial results
- Caller can decide whether to skip or fall back to ATM

### 4. Why separate call/put selection?
- Allows independent tolerance checking
- Enables reporting when only one leg is found
- Matches strategy requirement: "±35Δ (±5Δ acceptable)" per leg

## Performance Considerations

### API Calls
- **ATM Calendar**: 1 Greeks snapshot with 2-4 symbols per expiration
- **Double Calendar**: 1 Greeks snapshot with 20-40 symbols per expiration
- **Recommendation**: Use double calendar mode sparingly to avoid rate limits

### Optimization Ideas (Future)
1. **Cache Greeks**: If scanning multiple DTE pairs, reuse Greeks from same expiration
2. **Adaptive Range**: Start with ±15% range, expand to ±25% only if no strikes found
3. **Parallel Fetches**: Fetch Greeks for multiple expirations concurrently

## Validation Checklist

- ✅ Functions correctly select strikes within ±5Δ tolerance
- ✅ Returns None when no strikes found (graceful failure)
- ✅ Handles edge cases (no Greeks, missing delta, etc.)
- ✅ Consistent with existing code style and patterns
- ✅ Well-documented with docstrings and type hints
- ✅ Test script provided for validation
- ✅ Compatible with Issue #3 enhancements (Greeks with delta)

## Next Steps (Future Issues)

1. **Issue #5**: Integrate double calendar mode into main scanner
2. **Issue #6**: Add earnings filtering (no earnings between front/back expiry)
3. **Issue #7**: Add liquidity filters (volume, open interest, bid-ask)
4. **Issue #8**: Backtest framework for strategy validation

## References

- Strategy SOP: `docs/forward-factor-calendar-spread-SOP.md`
- Main Scanner: `scripts/ff_tastytrade_scanner.py`
- tastytrade SDK Docs: `docs/tastytrade-sdk-docs/dxfeed.md`
- Greeks Class: `tastytrade.dxfeed.Greeks` (includes delta field)
