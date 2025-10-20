---
issue: 32
approach: sequential
agent: general-purpose
started: 2025-10-20T08:27:52Z
status: in_progress
---

# Issue #32: Volume-Based Liquidity Filter Fix (Sequential Execution)

## Approach

Fix critical volume filtering bug by using correct data source: dxFeed `Underlying.optionVolume` instead of Market Metrics `liquidity_value`.

## Investigation Results

**API Investigation Complete** (2025-10-20T08:27:52Z):
- ❌ Market Metrics API: No `avg_options_volume_20d` field exists
- ❌ Market Metrics `liquidity_value`: Wrong metric (opaque liquidity score, not volume)
- ✅ dxFeed `Underlying.optionVolume`: **Correct metric** - today's total chain volume (contracts)

**Selected Solution:** Use dxFeed `Underlying.optionVolume`
- Metric: Total option contracts traded across entire chain today
- Type: Integer (number of contracts, not trades)
- Scope: All strikes, all expirations, calls + puts
- Limitation: Today's volume only (not 20-day average)
- Accuracy: ~70% vs requirement (correct metric, wrong timeframe)
- User approved: "even if not exactly 20 day average"

## Implementation Plan

### Phase 1: Add dxFeed Underlying Snapshot Function
1. Create `snapshot_underlying()` function similar to `snapshot_greeks()`
2. Use DXLinkStreamer to fetch `Underlying` event for symbol
3. Extract `option_volume` field (int)
4. Return value or None if unavailable

**Files:** `scripts/ff_tastytrade_scanner.py` (~line 400, after `snapshot_greeks`)

### Phase 2: Replace Volume Extraction
1. Remove `liquidity_value` usage in `fetch_market_metrics()`
2. Add `snapshot_underlying()` call in scan loop (before Greeks)
3. Extract `optionVolume` from Underlying event
4. Store in variable for filtering

**Files:** `scripts/ff_tastytrade_scanner.py` (scan loop, ~line 1200)

### Phase 3: Update Volume Filter Logic
1. Locate current volume check (`check_volume()` or inline filter)
2. Replace `liquidity_value` comparison with `option_volume`
3. Update threshold check: `option_volume >= args.min_avg_volume`
4. Keep `skip_reason = "volume_too_low"` for tracking

**Files:** `scripts/ff_tastytrade_scanner.py` (pre-filter section)

### Phase 4: Update CSV Output
1. Change column name: `avg_options_volume` → `option_volume_today`
2. Update CSV header row
3. Update row construction to use `option_volume` value
4. Verify column ordering

**Files:** `scripts/ff_tastytrade_scanner.py` (CSV construction ~line 1400)

### Phase 5: Add Diagnostic Logging
1. Add INFO logging for volume values: `logger.info(f"{symbol}: Option volume {option_volume}")`
2. Log when symbols are filtered: `logger.info(f"{symbol}: Avg volume {option_volume} < {threshold}, skipping")`
3. Show yesterday's volume for MSFT/META as sanity check

**Files:** `scripts/ff_tastytrade_scanner.py` (filter section)

### Phase 6: Update Documentation
1. Update CLAUDE.md CSV schema: column name and description
2. Update CLI flag help text: clarify "today's volume" not "20-day average"
3. Document limitation: real-time volume, not historical average
4. Update README_TT.md examples

**Files:** `CLAUDE.md`, `scripts/README_TT.md`

### Phase 7: Testing
1. Test with MSFT, META (expect >100k volume, should pass)
2. Test with illiquid symbols (expect <10k, should filter)
3. Verify diagnostic logging shows correct volumes
4. Check CSV output has correct column name
5. Test --skip-liquidity-check bypass

**Testing:** Manual scan with production symbols

## Key Code Changes

**New Function:**
```python
async def snapshot_underlying(session: ProductionSession, symbol: str, timeout_s: float = 3.0):
    """Fetch Underlying event from dxFeed for options volume data."""
    from tastytrade.dxfeed import Underlying
    from tastytrade.streamer import DXLinkStreamer

    async with DXLinkStreamer(session) as streamer:
        await streamer.subscribe(Underlying, [symbol])

        try:
            async with asyncio.timeout(timeout_s):
                async for event in streamer.listen(Underlying):
                    if event.eventSymbol == symbol:
                        return event
        except asyncio.TimeoutError:
            logger.warning(f"Timeout fetching Underlying for {symbol}")
            return None

    return None
```

**Volume Extraction:**
```python
# In scan loop, before Greeks fetching
try:
    underlying_event = await snapshot_underlying(session, symbol, timeout_s=3.0)
    option_volume = underlying_event.option_volume if underlying_event else None
except Exception as e:
    logger.warning(f"{symbol}: Failed to fetch Underlying event: {e}")
    option_volume = None

# Volume filter
if not args.skip_liquidity_check:
    if option_volume is None or option_volume < args.min_avg_volume:
        logger.info(f"{symbol}: Avg volume {option_volume} < {args.min_avg_volume}, skipping")
        skip_stats['volume_too_low'] += 1
        continue
```

**CSV Column Update:**
```python
# Change from:
"avg_options_volume": avg_volume

# To:
"option_volume_today": option_volume
```

## Expected Results

**MSFT Test:**
- Current (broken): 2774.2 volume → filtered incorrectly
- After fix: >100,000 volume → passes filter ✅

**META Test:**
- Current (broken): 2385.6 volume → filtered incorrectly
- After fix: >100,000 volume → passes filter ✅

**Illiquid Symbol Test:**
- Should show <10,000 volume → filtered correctly ✅

## Success Criteria

- [x] Investigation complete: Identified dxFeed Underlying.optionVolume as correct source
- [ ] snapshot_underlying() function implemented
- [ ] Volume extraction replaced (liquidity_value → option_volume)
- [ ] Filter logic updated with new volume source
- [ ] CSV column renamed and updated
- [ ] Diagnostic logging added (show actual volumes)
- [ ] Documentation updated (CLAUDE.md, README_TT.md)
- [ ] Testing complete: MSFT/META pass filter, volumes >100k
- [ ] Production test: Full scan shows correct filtering

## Notes

**Why not 20-day average:**
- No API endpoint provides historical options volume data
- Market Metrics API has no relevant field
- dxFeed has only today's volume
- Alternative would require summing individual contract volumes daily (too expensive)
- Today's volume is highly correlated with long-term average for liquid symbols

**Performance Impact:**
- Adds one dxFeed snapshot per symbol (Underlying event)
- Similar cost to existing Greeks snapshot
- Still filters BEFORE expensive Greeks chain fetching
- Net effect: Minimal performance impact

## Progress

Starting implementation...
