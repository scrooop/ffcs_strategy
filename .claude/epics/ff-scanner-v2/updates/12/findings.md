# Futures Options Support Investigation - Findings

**Investigation Date:** 2025-10-19
**Investigator:** Claude Code (Task #12)
**Test Account:** tastytrade production account

## Executive Summary

The FF scanner **CAN support futures options** with code modifications. The tastytrade API provides option chain data for futures symbols (`/ES`, `/GC`, etc.), but requires different handling compared to equity options.

**Recommendation:** **PARTIAL SUPPORT** - Requires code changes (Estimated 2-3 hours)

---

## Test Results

### Phase 1: API Documentation Review

**Finding:** tastytrade SDK fully supports futures and futures options

**Evidence from SDK docs:**
- `InstrumentType.FUTURE` and `InstrumentType.FUTURE_OPTION` are supported
- `Future.get()` and `FutureOption.get()` methods available
- `NestedFutureOptionChain` class provides structured futures option chain access
- `get_future_option_chain()` function available
- Market data example shows futures symbols: `/MCLG6`, `/MCLF6`

**Key SDK Insights:**
- Futures symbols use `/` prefix (e.g., `/ES`, `/GC`, `/NQ`, `/CL`)
- Futures options have different symbol structure: `./ESZ5 E3AV5 251020C6995`
- Futures option chain structure differs from equity options
- dxFeed Greeks available for futures options (confirmed in docs)

### Phase 2: Live API Testing

**Test Script:** `/Users/wnv/cc/personal_finance/ffcs_strategy/test_futures_api.py`

#### Test 1: Get market data for /ES as FUTURE
```python
md = get_market_data(session, "/ES", InstrumentType.FUTURE)
```
**Result:** ❌ **FAILED**
**Error:** `'str' object has no attribute 'get'`
**Analysis:** API endpoint `/market-data/Future//ES` returns error response. The root symbol `/ES` is not a tradeable contract - need specific contract month (e.g., `/ESZ5`).

#### Test 2: Get Future instrument for /ES
```python
future = Future.get(session, "/ES")
```
**Result:** ❌ **FAILED**
**Error:** `record_not_found: Couldn't find Future. Unique customer support identifier: cb9a83e96dfbb170e69e941d3a9ef966`
**Analysis:** `/ES` is a root symbol, not a specific contract. Futures contracts have expiration months (e.g., `/ESZ5` = Dec 2025).

#### Test 3: Get option chain for /ES using NestedOptionChain
```python
chain = NestedOptionChain.get(session, "/ES")
```
**Result:** ✅ **SUCCESS**
**Output:** Found 4 expirations
**First expiration:** 2025-11-21
**Analysis:** `NestedOptionChain` works with futures root symbols! This is the same API used by the equity scanner.

#### Test 4: Get futures option chain using NestedFutureOptionChain
```python
chain = NestedFutureOptionChain.get(session, "/ES")
```
**Result:** ✅ **SUCCESS**
**Output:**
- 7 underlying futures contracts found (ESU6, ESZ5, ESZ7, ESH7, ESH6, ESM6, ESZ6)
- Active month: `/ESZ5` (Dec 2025, 61 DTE)
- Multiple option expirations available
- Strike structure: `./ESZ5 E3AV5 251020C6995`
- Streamer symbols: `./E3AV25C6995:XCME`

**Key Finding:** Futures options in tastytrade are tied to specific underlying futures contracts (e.g., `/ESZ5`), not the root symbol (`/ES`).

#### Test 5: Get market data for /GC as FUTURE
```python
md = get_market_data(session, "/GC", InstrumentType.FUTURE)
```
**Result:** ❌ **FAILED** (same error as Test 1)

#### Test 6: Get market data for ES (no /) as EQUITY
```python
md = get_market_data(session, "ES", InstrumentType.EQUITY)
```
**Result:** ❌ **FAILED**
**Error:** `No data present in response: {}`
**Analysis:** `ES` without `/` is not recognized as an equity symbol.

### Phase 3: Scanner Code Analysis

**Current Implementation Issues:**

1. **Line 659: Hardcoded InstrumentType.EQUITY**
   ```python
   md = get_market_data(session, sym, InstrumentType.EQUITY)
   ```
   - Assumes all symbols are equities
   - Fails for futures symbols

2. **Spot Price Retrieval**
   - Current code expects `md.last` or `md.mark` from equity market data
   - For futures, need to:
     - Identify active futures contract from `NestedFutureOptionChain`
     - Get market data for that specific contract (e.g., `/ESZ5`)
     - Use contract price as "spot" reference

3. **Earnings Filtering (Lines 670-673, 690-697)**
   - Scanner checks for earnings conflicts
   - Futures don't have earnings - this check should be skipped
   - **BUG DISCOVERED:** `--allow-earnings` flag doesn't work due to argparse configuration
     - Line 1034: `--skip-earnings` has `default=True`
     - Line 1077: Check fails when both flags are True
     - Makes it impossible to bypass earnings filter via CLI

4. **Option Chain Retrieval (Line 676)**
   ```python
   chain_list = NestedOptionChain.get(session, sym)
   ```
   - **Good news:** This already works for futures! (Test 3 confirmed)
   - No changes needed for basic option chain retrieval

5. **Greeks Streaming**
   - Scanner uses `snapshot_greeks()` with dxFeed streamer symbols
   - Futures option streamer symbols have different format: `./E3AV25C6995:XCME`
   - May require testing to confirm Greeks data availability

---

## Required Code Changes

### 1. Symbol Type Detection
**Location:** Early in `scan()` function
**Change:** Add function to detect if symbol is futures or equity

```python
def get_instrument_type(symbol: str) -> InstrumentType:
    """Determine if symbol is futures (starts with /) or equity."""
    return InstrumentType.FUTURE if symbol.startswith("/") else InstrumentType.EQUITY
```

### 2. Spot Price Retrieval for Futures
**Location:** Line 658-663 (replace current market data fetch)
**Change:**

```python
instrument_type = get_instrument_type(sym)

if instrument_type == InstrumentType.FUTURE:
    # Get active futures contract from option chain
    futures_chain = NestedFutureOptionChain.get(session, sym)
    if not futures_chain or not futures_chain.futures:
        print(f"[WARN] No futures contracts for {sym}, skipping.", file=sys.stderr)
        continue

    # Find active month contract
    active_contract = next((f for f in futures_chain.futures if f.active_month), None)
    if not active_contract:
        active_contract = futures_chain.futures[0]  # Use first if no active_month flag

    # Get market data for specific contract
    md = get_market_data(session, active_contract.symbol, InstrumentType.FUTURE)
    if md is None or md.last is None:
        print(f"[WARN] No quote for {active_contract.symbol}, skipping.", file=sys.stderr)
        continue
    spot = float(md.last) if md.last is not None else float(md.mark)

else:
    # Existing equity logic
    md = get_market_data(session, sym, InstrumentType.EQUITY)
    if md is None or md.last is None:
        print(f"[WARN] No quote for {sym}, skipping.", file=sys.stderr)
        continue
    spot = float(md.last) if md.last is not None else float(md.mark)
```

### 3. Skip Earnings Filter for Futures
**Location:** Lines 665-673, 690-697
**Change:** Wrap earnings logic in `if instrument_type == InstrumentType.EQUITY:`

```python
# 2) Extract earnings and liquidity data for this symbol
earnings_date = None
liquidity_rating = None
if instrument_type == InstrumentType.EQUITY and sym in market_metrics:
    metric_info = market_metrics[sym]
    earnings = getattr(metric_info, 'earnings', None)
    if earnings:
        earnings_date = getattr(earnings, 'expected_report_date', None)
    liquidity_rating = getattr(metric_info, 'liquidity_rating', None)
```

```python
# 2.5) Pre-filtering: Check earnings conflicts and liquidity
max_back_dte = max([back for _, back in pairs])
max_back_exp = nearest_expiration(chain, max_back_dte, dte_tolerance)

if instrument_type == InstrumentType.EQUITY and max_back_exp and skip_earnings:
    passes, reason = check_earnings_conflict(sym, market_metrics, max_back_exp, today)
    if not passes:
        print(f"[FILTERED] {sym}: {reason}", file=sys.stderr)
        if show_earnings_conflicts:
            filtered_rows.append({"symbol": sym, "reason": reason})
        continue
```

### 4. Fix Earnings Flag Bug
**Location:** Lines 1034-1037
**Change:** Use mutually exclusive group or fix default logic

**Option A: Use argparse mutually exclusive group**
```python
earnings_group = ap.add_mutually_exclusive_group()
earnings_group.add_argument("--skip-earnings", dest="skip_earnings", action="store_true",
                           help="Skip positions with earnings conflicts (default).")
earnings_group.add_argument("--allow-earnings", dest="skip_earnings", action="store_false",
                           help="Allow trading through earnings (disable earnings filtering).")
ap.set_defaults(skip_earnings=True)
```

**Option B: Remove conflicting default**
```python
ap.add_argument("--skip-earnings", dest="skip_earnings", action="store_true",
                help="Skip positions with earnings conflicts (default).")
ap.add_argument("--allow-earnings", dest="skip_earnings", action="store_false",
                help="Allow trading through earnings (disable earnings filtering).")
ap.set_defaults(skip_earnings=True)  # Set default once at end
```

Then remove the conflict check at line 1077.

---

## Differences: Equity Options vs Futures Options

| Aspect | Equity Options | Futures Options |
|--------|---------------|-----------------|
| **Underlying Symbol** | Ticker (SPY, AAPL) | Root symbol (/ES, /GC) + contract month (/ESZ5) |
| **Spot Price** | Stock/ETF last price | Active futures contract price |
| **Earnings** | Yes - must check | No - N/A |
| **Expiration Cycles** | Standard (monthly, weekly) | Monthly, quarterly, varies by product |
| **Contract Size** | 100 shares | Varies (e.g., /ES = $50 per point) |
| **OCC Symbol Format** | `SPY   240417C00437000` | `./ESZ5 E3AV5 251020C6995` |
| **Streamer Symbol** | `.SPY240417C437` | `./E3AV25C6995:XCME` |
| **Greeks Source** | dxFeed Greeks.volatility | dxFeed Greeks.volatility (same) |
| **IV Calculation** | Same | Same (variance decomposition) |
| **Liquidity Metrics** | Available via market_metrics | May not be available (needs testing) |

---

## Greeks Availability (Needs Verification)

**Question:** Do futures option Greeks arrive via `snapshot_greeks()` in the same format as equity options?

**Hypothesis:** Yes, because:
- dxFeed supports futures options (confirmed in SDK docs)
- Streamer symbols are provided in `NestedFutureOptionChain` output
- `Greeks.volatility` is instrument-agnostic

**Recommendation:** Test with modified scanner to verify Greeks data arrives for futures options.

---

## Testing Gaps

**Not tested in this investigation:**
1. Greeks data retrieval for futures options via dxFeed
2. Liquidity ratings for futures (may not exist)
3. X-earn IV for futures (probably not available)
4. Multiple futures products (/NQ, /CL, /GC)
5. Strike selection for futures (different increments)
6. Full end-to-end scanner run with futures

**Next Steps for Full Validation:**
1. Implement code changes 1-3 above
2. Run scanner with `/ES --min-ff 0.0` to get results
3. Verify CSV output format
4. Compare futures FF values with equity FF values
5. Test with 2-3 additional futures products

---

## Effort Estimate

**Code Changes:** 2-3 hours
- Symbol type detection: 15 min
- Spot price logic for futures: 45 min
- Earnings filter bypass: 15 min
- Earnings flag bug fix: 15 min
- Testing and debugging: 60-90 min

**Testing:** 1-2 hours
- Greeks verification
- Multi-product testing
- CSV output validation

**Total:** 3-5 hours

---

## Recommendation

**Status:** ✅ **PARTIAL SUPPORT - RECOMMENDED FOR IMPLEMENTATION**

**Rationale:**
1. API fully supports futures options (confirmed via tests)
2. Code changes are isolated and low-risk
3. Futures options are liquid and strategic for volatility trading
4. Forward IV strategy is equally valid for futures options
5. No fundamental blockers discovered

**Implementation Priority:**
1. Fix earnings flag bug (affects both equity and futures usage)
2. Add symbol type detection
3. Add futures spot price retrieval
4. Skip earnings filter for futures
5. Test with /ES, /GC, /NQ
6. Document futures-specific usage in README

**Breaking Changes:** None - futures support is additive

**Backward Compatibility:** ✅ Full backward compatibility maintained

---

## Appendix: Test Commands

### Successful Tests
```bash
# API compatibility test
python test_futures_api.py

# Equity baseline (works)
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --min-ff 0.0 --csv-out equity_test.csv
```

### Failed Tests (Due to Code Limitations)
```bash
# Futures with / prefix (fails at market data fetch)
python scripts/ff_tastytrade_scanner.py --tickers /ES /GC --pairs 30-60 --min-ff 0.20 --skip-earnings

# Futures without / (treated as equity, fails)
python scripts/ff_tastytrade_scanner.py --tickers ES GC --pairs 30-60 --min-ff 0.20 --allow-earnings
# Error: --skip-earnings and --allow-earnings are mutually exclusive (CLI bug)
```

### After Implementation (Expected to Work)
```bash
# Futures scan with fixed scanner
python scripts/ff_tastytrade_scanner.py --tickers /ES /GC /NQ --pairs 30-60 --min-ff 0.20 --csv-out futures_scan.csv

# Mixed equities and futures
python scripts/ff_tastytrade_scanner.py --tickers SPY QQQ /ES /GC --pairs 30-60 60-90 --min-ff 0.23 --csv-out mixed_scan.csv
```

---

## Files Created/Modified

**Test Files (Investigation Only):**
- `/Users/wnv/cc/personal_finance/ffcs_strategy/test_futures_api.py` (can be deleted after review)
- `/Users/wnv/cc/personal_finance/ffcs_strategy/equity_test.csv` (baseline test output)
- `/Users/wnv/cc/personal_finance/ffcs_strategy/futures_test.csv` (not created - test failed)

**Documentation:**
- `/Users/wnv/cc/personal_finance/ffcs_strategy/.claude/epics/ff-scanner-v2/updates/12/findings.md` (this file)
- `/Users/wnv/cc/personal_finance/ffcs_strategy/.claude/epics/ff-scanner-v2/updates/12/stream-A.md` (progress tracking)

**Code Changes Required:**
- `scripts/ff_tastytrade_scanner.py` (modifications outlined above)

---

**Investigation Complete: 2025-10-19**
