---
id: 03
name: Double Calendar Strike Selection
status: todo
priority: high
estimated_hours: 3-4
dependencies: [02]
phase: 2
created: 2025-10-19T08:35:09Z
---

# Task 03: Double Calendar Strike Selection

## Objective

Implement ±35Δ strike finding algorithm using delta values from enhanced Greeks collection to enable double calendar structure scanning.

## Scope

Add `find_delta_strikes()` function that identifies call and put strikes closest to target deltas (±0.35) within configurable tolerance.

## Technical Details

### Files to Modify
- `scripts/ff_tastytrade_scanner.py`

### New Function to Add

```python
async def find_delta_strikes(
    session: Session,
    expiration_obj,
    spot: float,
    target_delta_call: float = 0.35,
    target_delta_put: float = -0.35,
    tolerance: float = 0.05
) -> Tuple[Optional[Tuple[float, str, float]], Optional[Tuple[float, str, float]]]:
    """
    Find strikes closest to ±35Δ for double calendar structure.

    Args:
        session: tastytrade Session
        expiration_obj: NestedOptionChain expiration object
        spot: Current underlying price
        target_delta_call: Target delta for call (default: 0.35)
        target_delta_put: Target delta for put (default: -0.35)
        tolerance: Max deviation from target delta (default: 0.05)

    Returns:
        (call_info, put_info) where each is (strike, streamer_symbol, delta) or None
        Returns (None, None) if no strikes found within tolerance

    Example:
        call_info, put_info = await find_delta_strikes(session, front_exp, spot=580.0)
        if call_info and put_info:
            call_strike, call_symbol, call_delta = call_info
            put_strike, put_symbol, put_delta = put_info
            print(f"Call: {call_strike} @ {call_delta:.3f}Δ")
            print(f"Put: {put_strike} @ {put_delta:.3f}Δ")
    """
    # Step 1: Get reasonable strike range (e.g., ±20% from spot)
    # This avoids requesting Greeks for far OTM strikes
    strike_range_pct = 0.20
    min_strike = spot * (1 - strike_range_pct)
    max_strike = spot * (1 + strike_range_pct)

    # Filter strikes within range
    strikes_in_range = [
        s for s in expiration_obj.strikes
        if min_strike <= float(s.strike_price) <= max_strike
    ]

    if not strikes_in_range:
        return None, None

    # Step 2: Collect streamer symbols for Greeks request
    call_symbols = [s.call_streamer_symbol for s in strikes_in_range]
    put_symbols = [s.put_streamer_symbol for s in strikes_in_range]
    all_symbols = call_symbols + put_symbols

    # Step 3: Fetch Greeks (IV + delta) for all strikes
    greeks_map = await snapshot_greeks(session, all_symbols)

    # Step 4: Find best call strike (closest to +0.35Δ)
    best_call = None
    best_call_error = None

    for strike_obj in strikes_in_range:
        call_symbol = strike_obj.call_streamer_symbol
        greeks_tuple = greeks_map.get(call_symbol)

        if not greeks_tuple:
            continue

        iv, delta = greeks_tuple

        # Check if within tolerance
        error = abs(delta - target_delta_call)
        if error <= tolerance:
            if best_call_error is None or error < best_call_error:
                best_call_error = error
                best_call = (float(strike_obj.strike_price), call_symbol, delta)

    # Step 5: Find best put strike (closest to -0.35Δ)
    best_put = None
    best_put_error = None

    for strike_obj in strikes_in_range:
        put_symbol = strike_obj.put_streamer_symbol
        greeks_tuple = greeks_map.get(put_symbol)

        if not greeks_tuple:
            continue

        iv, delta = greeks_tuple

        # Check if within tolerance
        error = abs(delta - target_delta_put)
        if error <= tolerance:
            if best_put_error is None or error < best_put_error:
                best_put_error = error
                best_put = (float(strike_obj.strike_price), put_symbol, delta)

    return best_call, best_put
```

### CLI Flag to Add

```python
parser.add_argument('--delta-tolerance', type=float, default=0.05,
                    help='Max deviation from ±35Δ for double calendars (default: 0.05)')
```

### Error Handling

Add graceful handling when no strikes found:

```python
call_info, put_info = await find_delta_strikes(session, front_exp, spot, tolerance=args.delta_tolerance)

if not call_info or not put_info:
    print(f"[WARN] {symbol}: No strikes found within {args.delta_tolerance}Δ tolerance for double calendar, skipping")
    # Fall back to ATM-only for this symbol
    continue
```

## Deliverables

- [ ] `find_delta_strikes()` function implemented
- [ ] Strike range filtering logic (±20% from spot)
- [ ] Delta-based strike selection for calls and puts
- [ ] CLI flag `--delta-tolerance` added
- [ ] Graceful handling when no strikes within tolerance
- [ ] Console logging for strike selection failures

## Testing Checklist

- [ ] Test with SPY (liquid, many strikes): verify strikes found within tolerance
- [ ] Test with QQQ: verify call and put strikes are reasonable distances from ATM
- [ ] Test with `--delta-tolerance 0.10`: verify wider tolerance finds more strikes
- [ ] Test with very tight tolerance (0.01): verify graceful handling when no strikes found
- [ ] Test delta values: verify call deltas are positive (~0.30-0.40), put deltas are negative (~-0.30 to -0.40)
- [ ] Test with illiquid symbol: verify handling when Greeks don't arrive for all strikes

## Acceptance Criteria

- ✅ Finds strikes with delta closest to ±0.35 within tolerance
- ✅ Returns `(None, None)` when no strikes found (graceful failure)
- ✅ Filters strikes to reasonable range (±20% from spot) before Greeks request
- ✅ Handles partial Greeks data (some strikes timeout)
- ✅ Delta values are accurate (call: 0.30-0.40, put: -0.30 to -0.40 typically)
- ✅ Console warning logged when strikes not found

## Notes

- **Strike Range Optimization**: Only request Greeks for ±20% strikes to reduce API load
- **Tolerance Flexibility**: User can widen tolerance if strikes hard to find (e.g., weekly expirations)
- **Delta Asymmetry**: Call and put deltas may not be perfectly symmetric due to skew
- **Fallback Strategy**: If double calendar strikes not found, return ATM-only result for that symbol
