---
id: 02
name: Enhanced Greeks Collection
status: todo
priority: critical
estimated_hours: 1-2
dependencies: []
phase: 1
created: 2025-10-19T08:35:09Z
---

# Task 02: Enhanced Greeks Collection

## Objective

Modify existing `snapshot_greeks()` function to return both IV and delta values from dxFeed Greeks, enabling double calendar strike selection while maintaining backward compatibility.

## Scope

Extend `snapshot_greeks()` to collect delta in addition to IV, with minimal changes to existing code.

## Technical Details

### Files to Modify
- `scripts/ff_tastytrade_scanner.py` (modify existing `snapshot_greeks()` function)

### Current Implementation (v1.0)

```python
async def snapshot_greeks(session, symbols: List[str], timeout=3.0) -> Dict[str, float]:
    """Returns {symbol: iv} for each symbol that arrives within timeout."""
    # ... existing implementation ...
    # Currently only extracts Greeks.volatility (IV)
```

### Enhanced Implementation (v2.0)

```python
async def snapshot_greeks(session, symbols: List[str], timeout=3.0) -> Dict[str, Tuple[float, float]]:
    """
    Collect IV and delta from dxFeed Greeks snapshot.

    Args:
        session: tastytrade Session
        symbols: List of streamer symbols (option contracts)
        timeout: Snapshot timeout in seconds (default: 3.0)

    Returns:
        Dict mapping streamer_symbol → (iv, delta)
        Returns empty dict {} if no Greeks arrive within timeout

    Example:
        greeks = await snapshot_greeks(session, ['.SPY251121C580', '.SPY251219C580'])
        if '.SPY251121C580' in greeks:
            iv, delta = greeks['.SPY251121C580']
            print(f"IV: {iv:.4f}, Delta: {delta:.4f}")
    """
    from tastytrade.dxfeed import Greeks

    result = {}
    async with DXLinkStreamer(session) as streamer:
        await streamer.subscribe(Greeks, symbols)

        start = asyncio.get_event_loop().time()
        async for event in streamer.listen(Greeks):
            # Extract both IV and delta
            iv = float(event.volatility) if event.volatility is not None else None
            delta = float(event.delta) if event.delta is not None else None

            # Only store if both IV and delta are available
            if iv is not None and delta is not None:
                result[event.eventSymbol] = (iv, delta)

            # Check timeout
            if asyncio.get_event_loop().time() - start > timeout:
                break

            # Exit early if we got all symbols
            if len(result) >= len(symbols):
                break

    return result
```

### Update Call Sites

Modify all places where `snapshot_greeks()` is called to handle the new return format:

**Current (v1.0)**:
```python
greeks_map = await snapshot_greeks(session, symbols)
iv = greeks_map.get(call_symbol)  # Returns float or None
```

**Enhanced (v2.0)**:
```python
greeks_map = await snapshot_greeks(session, symbols)
greeks_tuple = greeks_map.get(call_symbol)  # Returns (iv, delta) or None
if greeks_tuple:
    iv, delta = greeks_tuple
else:
    # Handle missing Greeks data
    continue
```

### Backward Compatibility Strategy

Update existing ATM scanning code to use new tuple format:

```python
# OLD: iv_front = greeks_map.get(front_call_symbol)
# NEW:
greeks_front = greeks_map.get(front_call_symbol)
if greeks_front:
    iv_front, delta_front = greeks_front
else:
    print(f"[WARN] Greeks unavailable for {front_call_symbol}, skipping")
    continue
```

## Deliverables

- [ ] `snapshot_greeks()` modified to return `(iv, delta)` tuples
- [ ] All call sites updated to handle new return format
- [ ] ATM scanning logic updated (existing code)
- [ ] Error handling for missing Greeks data maintained
- [ ] Docstring updated with type hints and examples

## Testing Checklist

- [ ] Test ATM scanning with new Greeks format: verify IV values match v1.0
- [ ] Test delta extraction: verify delta values are reasonable (0-1 for calls, 0 to -1 for puts)
- [ ] Test Greeks timeout: verify graceful handling when Greeks don't arrive
- [ ] Test partial Greeks: verify handling when some symbols arrive, others timeout
- [ ] Test with SPY, QQQ: verify both IV and delta are extracted correctly

## Acceptance Criteria

- ✅ `snapshot_greeks()` returns `Dict[str, Tuple[float, float]]` (iv, delta)
- ✅ Existing ATM scanning logic continues to work
- ✅ Delta values are correctly extracted from Greeks.delta
- ✅ Timeout handling remains robust (partial results OK)
- ✅ No performance regression (same timeout behavior as v1.0)

## Notes

- **Why Both IV and Delta**: Delta is required for Task 03 (double calendar strike selection)
- **Graceful Degradation**: If only IV arrives (delta=None), skip that symbol (both required)
- **Performance**: No additional API calls or subscriptions needed - Greeks already provides delta
- **Type Safety**: Consider adding type hints: `Dict[str, Tuple[float, float]]` for clarity
