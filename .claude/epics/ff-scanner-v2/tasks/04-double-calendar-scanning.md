---
id: 04
name: Double Calendar Scanning Logic
status: todo
priority: high
estimated_hours: 3-4
dependencies: [02, 03]
phase: 2
created: 2025-10-19T08:35:09Z
---

# Task 04: Double Calendar Scanning Logic

## Objective

Add structure-based scanning to main loop, enabling ATM call calendars, double calendars (±35Δ), or both simultaneously based on `--structure` CLI flag.

## Scope

Modify scanner's main loop to support three scanning modes: `atm-call`, `double`, or `both`. Compute separate Forward Factors for call and put calendars in double structure.

## Technical Details

### Files to Modify
- `scripts/ff_tastytrade_scanner.py`

### CLI Flag to Add

```python
parser.add_argument('--structure', type=str, default='both',
                    choices=['atm-call', 'double', 'both'],
                    help='Calendar structure type: atm-call, double, or both (default: both)')
```

### Main Loop Modification

```python
async def scan_symbol(
    session: Session,
    symbol: str,
    front_dte: int,
    back_dte: int,
    dte_tolerance: int,
    structure: str,
    delta_tolerance: float,
    min_ff: float
) -> List[Dict]:
    """
    Scan symbol for calendar spread opportunities.

    Args:
        session: tastytrade Session
        symbol: Ticker symbol
        front_dte, back_dte: Target DTEs
        dte_tolerance: Max DTE deviation
        structure: 'atm-call', 'double', or 'both'
        delta_tolerance: Max delta deviation for double calendars
        min_ff: Minimum Forward Factor threshold

    Returns:
        List of result dicts (0-2 rows depending on structure)
    """
    results = []

    # Fetch spot price and option chain
    spot = get_market_data(session, symbol).last
    chain = await NestedOptionChain.get(session, symbol)

    # Find expirations
    front_exp_date = nearest_expiration(chain, front_dte, dte_tolerance)
    back_exp_date = nearest_expiration(chain, back_dte, dte_tolerance)

    if not front_exp_date or not back_exp_date:
        return results

    front_exp = next(e for e in chain.expirations if e.expiration_date == front_exp_date)
    back_exp = next(e for e in chain.expirations if e.expiration_date == back_exp_date)

    # Scan ATM call calendar (if requested)
    if structure in ['atm-call', 'both']:
        result = await scan_atm_calendar(
            session, symbol, spot, front_exp, back_exp, min_ff
        )
        if result:
            results.append(result)

    # Scan double calendar (if requested)
    if structure in ['double', 'both']:
        result = await scan_double_calendar(
            session, symbol, spot, front_exp, back_exp, min_ff, delta_tolerance
        )
        if result:
            results.append(result)

    return results
```

### ATM Calendar Scanner (Extract from Existing Code)

```python
async def scan_atm_calendar(
    session: Session,
    symbol: str,
    spot: float,
    front_exp,
    back_exp,
    min_ff: float
) -> Optional[Dict]:
    """
    Scan for ATM call calendar opportunity.

    Returns:
        Result dict or None if FF < min_ff
    """
    # Find ATM strike
    atm_strike, front_call_symbol, _ = pick_atm_strike(front_exp, spot)
    _, back_call_symbol, _ = pick_atm_strike(back_exp, spot)

    # Fetch Greeks (IV + delta)
    greeks_map = await snapshot_greeks(session, [front_call_symbol, back_call_symbol])

    front_greeks = greeks_map.get(front_call_symbol)
    back_greeks = greeks_map.get(back_call_symbol)

    if not front_greeks or not back_greeks:
        return None

    iv_front, _ = front_greeks
    iv_back, _ = back_greeks

    # Calculate Forward Factor (existing logic)
    T1 = dte(front_exp.expiration_date) / 365.0
    T2 = dte(back_exp.expiration_date) / 365.0
    fwd_var = (iv_back**2 * T2 - iv_front**2 * T1) / (T2 - T1)

    if fwd_var <= 0:
        return None

    fwd_iv = math.sqrt(fwd_var)
    ff = (iv_front - fwd_iv) / fwd_iv

    if ff < min_ff:
        return None

    return {
        'symbol': symbol,
        'structure': 'atm-call',
        'front_dte': dte(front_exp.expiration_date),
        'back_dte': dte(back_exp.expiration_date),
        'front_expiry': front_exp.expiration_date,
        'back_expiry': back_exp.expiration_date,
        'spot_price': spot,
        'atm_strike': atm_strike,
        'front_iv': iv_front,
        'back_iv': iv_back,
        'fwd_iv': fwd_iv,
        'ff': ff,
        'combined_ff': ff,  # For ATM, combined_ff = ff
        # Null values for double calendar columns
        'call_strike': None,
        'put_strike': None,
        'call_delta': None,
        'put_delta': None,
        'call_ff': None,
        'put_ff': None,
    }
```

### Double Calendar Scanner (New)

```python
async def scan_double_calendar(
    session: Session,
    symbol: str,
    spot: float,
    front_exp,
    back_exp,
    min_ff: float,
    delta_tolerance: float
) -> Optional[Dict]:
    """
    Scan for double calendar opportunity (±35Δ call and put).

    Returns:
        Result dict or None if combined_ff < min_ff or strikes not found
    """
    # Find ±35Δ strikes for front
    front_call_info, front_put_info = await find_delta_strikes(
        session, front_exp, spot, tolerance=delta_tolerance
    )

    # Find ±35Δ strikes for back
    back_call_info, back_put_info = await find_delta_strikes(
        session, back_exp, spot, tolerance=delta_tolerance
    )

    if not all([front_call_info, front_put_info, back_call_info, back_put_info]):
        return None

    # Unpack strikes
    front_call_strike, front_call_symbol, front_call_delta = front_call_info
    front_put_strike, front_put_symbol, front_put_delta = front_put_info
    back_call_strike, back_call_symbol, back_call_delta = back_call_info
    back_put_strike, back_put_symbol, back_put_delta = back_put_info

    # Fetch Greeks for IVs (already have deltas)
    greeks_map = await snapshot_greeks(session, [
        front_call_symbol, back_call_symbol,
        front_put_symbol, back_put_symbol
    ])

    # Extract IVs
    front_call_iv, _ = greeks_map.get(front_call_symbol, (None, None))
    back_call_iv, _ = greeks_map.get(back_call_symbol, (None, None))
    front_put_iv, _ = greeks_map.get(front_put_symbol, (None, None))
    back_put_iv, _ = greeks_map.get(back_put_symbol, (None, None))

    if not all([front_call_iv, back_call_iv, front_put_iv, back_put_iv]):
        return None

    # Calculate Forward Factor for call calendar
    T1 = dte(front_exp.expiration_date) / 365.0
    T2 = dte(back_exp.expiration_date) / 365.0

    fwd_var_call = (back_call_iv**2 * T2 - front_call_iv**2 * T1) / (T2 - T1)
    if fwd_var_call <= 0:
        return None
    fwd_iv_call = math.sqrt(fwd_var_call)
    call_ff = (front_call_iv - fwd_iv_call) / fwd_iv_call

    # Calculate Forward Factor for put calendar
    fwd_var_put = (back_put_iv**2 * T2 - front_put_iv**2 * T1) / (T2 - T1)
    if fwd_var_put <= 0:
        return None
    fwd_iv_put = math.sqrt(fwd_var_put)
    put_ff = (front_put_iv - fwd_iv_put) / fwd_iv_put

    # Combined FF (arithmetic mean)
    combined_ff = (call_ff + put_ff) / 2.0

    if combined_ff < min_ff:
        return None

    return {
        'symbol': symbol,
        'structure': 'double',
        'front_dte': dte(front_exp.expiration_date),
        'back_dte': dte(back_exp.expiration_date),
        'front_expiry': front_exp.expiration_date,
        'back_expiry': back_exp.expiration_date,
        'spot_price': spot,
        'call_strike': front_call_strike,
        'put_strike': front_put_strike,
        'call_delta': front_call_delta,
        'put_delta': front_put_delta,
        'call_ff': call_ff,
        'put_ff': put_ff,
        'combined_ff': combined_ff,
        # Note: For double calendars, use call/put IVs separately
        'front_iv': (front_call_iv + front_put_iv) / 2.0,  # Average for display
        'back_iv': (back_call_iv + back_put_iv) / 2.0,
        'fwd_iv': (fwd_iv_call + fwd_iv_put) / 2.0,
        'ff': None,  # Not applicable for double
        'atm_strike': None,
    }
```

## Deliverables

- [ ] `scan_symbol()` orchestrator function implemented
- [ ] `scan_atm_calendar()` extracted from existing code
- [ ] `scan_double_calendar()` new function implemented
- [ ] CLI flag `--structure` added with choices
- [ ] Call and put FF calculations for double calendars
- [ ] Combined FF calculation (arithmetic mean)
- [ ] Min FF threshold applied to combined_ff

## Testing Checklist

- [ ] Test `--structure atm-call`: verify only ATM results returned
- [ ] Test `--structure double`: verify only double calendar results returned
- [ ] Test `--structure both` (default): verify both ATM and double results returned
- [ ] Test FF calculations: verify call_ff and put_ff are reasonable
- [ ] Test combined_ff: verify it's arithmetic mean of call_ff and put_ff
- [ ] Test with SPY 60-90 DTE: verify double calendar opportunities found
- [ ] Test min-ff threshold: verify combined_ff filtering works correctly

## Acceptance Criteria

- ✅ Scanner supports three structure modes: atm-call, double, both
- ✅ Double calendar computes separate FFs for call and put calendars
- ✅ Combined FF is arithmetic mean of call_ff and put_ff
- ✅ Min FF threshold applied to combined_ff for double calendars
- ✅ Both structures can be scanned simultaneously (--structure both)
- ✅ Results clearly indicate structure type in output

## Notes

- **Combined FF Formula**: Arithmetic mean chosen for simplicity (per PRD Q3)
- **IV Averaging**: For display, use average of call/put IVs (not used in FF calc)
- **Structure Flexibility**: User can focus on specific structure or scan both
- **Performance**: Sequential scanning (ATM then double) is acceptable - bottleneck is Greeks streaming
