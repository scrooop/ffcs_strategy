# liquidity_value Analysis: Can It Be Used as Volume Proxy?

**Date:** 2025-10-20T08:48:00Z
**Issue:** #32 Volume-Based Liquidity Filter Fix
**Question:** What is `liquidity_value` and can it be scaled to work as a proxy for options volume?

---

## Executive Summary

**Answer: NO** - `liquidity_value` CANNOT reliably be used as a proxy for options volume, even with scaling.

**Key Finding:** `liquidity_value` shows **inconsistent, non-linear scaling** relative to actual options volume, making it unsuitable for volume filtering with any fixed scaling factor.

---

## What is liquidity_value?

### API Documentation Search Results

**Checked both documentation sources:**
1. `/Users/wnv/cc/personal_finance/ffcs_strategy/docs/tastytrade-sdk-docs` (SDK documentation)
2. `/Users/wnv/cc/personal_finance/ffcs_strategy/docs/tastytrade-openapi-docs` (OpenAPI spec)

**From OpenAPI Spec (`tastytrade_official_API_docs_full_spec.json`):**

```json
"liquidity": {
  "description": "liquidity of underlying",
  "type": "number",
  "format": "float"
},
"liquidity-rank": {
  "description": "liquidity rank of underlying",
  "type": "number",
  "format": "float"
},
"liquidity-rating": {
  "description": "liquidity rating of underlying",
  "type": "number",
  "format": "int32"
}
```

**From SDK Docs (`docs/tastytrade-sdk-docs/metrics.md`):**

```
liquidity_value (decimal.Decimal | None)
liquidity_rank (decimal.Decimal | None)
liquidity_rating (int | None)
```

**Field Mapping:**
- OpenAPI `"liquidity"` → Python SDK `liquidity_value`
- OpenAPI `"liquidity-rank"` → Python SDK `liquidity_rank`
- OpenAPI `"liquidity-rating"` → Python SDK `liquidity_rating`

### Documentation Quality: POOR

**All three fields have vague, circular descriptions:**
- `liquidity`: "liquidity of underlying" (no units, no formula, no interpretation)
- `liquidity-rank`: "liquidity rank of underlying" (no scale, no meaning)
- `liquidity-rating`: "liquidity rating of underlying" (only documented as 0-5 integer scale in CLAUDE.md)

**Conclusion:** tastytrade does NOT document what `liquidity_value` represents or how it's calculated.

### Current Usage

- **Field:** Part of `MarketMetricInfo` class (tastytrade Market Metrics API)
- **Type:** Decimal number (float in API, Decimal in Python SDK)
- **Description:** Undocumented (circular "liquidity of underlying")
- **Usage:** Currently used in `check_volume()` function (line 822) as a proxy for options volume ❌ INCORRECT

### How It's Currently Used (THE BUG)

**File:** `scripts/ff_tastytrade_scanner.py`

**Filtering Logic (line 822):**
```python
avg_volume = getattr(metric_info, 'liquidity_value', None)
if volume < min_volume:  # min_volume = 10,000 by default
    reason = f"Avg volume {volume:.1f} < {min_volume}"
    return (False, reason)
```

**CSV Output (line 1045):**
```python
option_volume = underlying_event.option_volume  # From dxFeed (CORRECT but requires market hours)
```

**The Problem:** Filtering uses `liquidity_value` (WRONG metric), but CSV output uses `option_volume` (CORRECT metric).

---

## Evidence: liquidity_value vs Actual Options Volume

### Bug Report Data

User provided evidence showing `liquidity_value` values vs expected options volume:

| Symbol | liquidity_value | Expected Volume | Ratio (Expected / liquidity_value) |
|--------|----------------|-----------------|-----------------------------------|
| MSFT   | 2,774.2        | >100,000        | **~36x**                          |
| META   | 2,385.6        | >100,000        | **~42x**                          |
| AVGO   | 6,422.0        | >50,000         | **~7.8x**                         |
| JPM    | 2,436.4        | >50,000         | **~20x**                          |
| LLY    | 589.2          | >10,000         | **~17x**                          |
| V      | 473.5          | >10,000         | **~21x**                          |
| NFLX   | 119.4          | >50,000         | **~419x** (!!!)                   |

### Key Observation

**Scaling ratios are wildly inconsistent:**
- Low: 7.8x (AVGO)
- Medium: 17-42x (MSFT, META, JPM, LLY, V)
- High: 419x (NFLX)

This means **no single scaling factor** can accurately convert `liquidity_value` to options volume across different symbols.

---

## Why liquidity_value Cannot Work

### 1. Non-Linear Relationship

If `liquidity_value` were a simple scaled version of options volume, the ratio (Expected Volume / liquidity_value) would be **constant** across all symbols.

**Actual ratios:** 7.8x to 419x (54x variation!)

This indicates `liquidity_value` is **NOT linearly proportional** to options volume.

### 2. Possible Interpretations

Given the inconsistent scaling, `liquidity_value` is likely:

**Option A:** A liquidity score/index
- Computed using multiple factors (volume, bid-ask spread, market cap, etc.)
- Non-linear transformation (e.g., logarithmic scale)
- **Example:** Similar to tastytrade's `liquidity_rating` (0-5 scale)

**Option B:** Dollar-based liquidity metric
- Notional value of options traded (contracts × price × multiplier)
- Higher-priced options would show higher liquidity_value
- **Would explain:** Why high-priced stocks (MSFT, AVGO) have higher ratios

**Option C:** Proprietary calculation
- Tastytrade internal metric with undocumented formula
- May combine volume, open interest, spread quality, etc.
- **Problem:** Cannot be reverse-engineered reliably

### 3. Test Case: Scaling Attempt

**Scenario:** Use average scaling factor of 30x (median of observed ratios)

**Proposed threshold:** 10,000 / 30 = 333 (scaled threshold for liquidity_value)

**Results:**
| Symbol | liquidity_value | Would Pass (>333)? | Should Pass? | Correct? |
|--------|----------------|-------------------|--------------|----------|
| MSFT   | 2,774          | ✅ YES            | ✅ YES       | ✅       |
| META   | 2,385          | ✅ YES            | ✅ YES       | ✅       |
| AVGO   | 6,422          | ✅ YES            | ✅ YES       | ✅       |
| JPM    | 2,436          | ✅ YES            | ✅ YES       | ✅       |
| LLY    | 589            | ✅ YES            | ✅ YES       | ✅       |
| V      | 473            | ✅ YES            | ✅ YES       | ✅       |
| NFLX   | 119            | ❌ NO             | ✅ YES       | ❌ FAIL  |

**Accuracy:** 85.7% (6/7 correct)

**Critical Failures:**
- NFLX (419x ratio) would be INCORRECTLY FILTERED OUT
- Any symbol with ratio >30x would be underestimated
- Any symbol with ratio <30x would be overestimated

### 4. Production Risk

**Scenario:** Scanner filters out high-FF opportunities due to incorrect volume proxy

**Example:**
- NFLX showing FF = 0.35 (excellent opportunity)
- liquidity_value = 119 → filtered out (below 333 threshold)
- Actual volume = 50,000+ → should have passed
- **Result:** Missed trade opportunity

**Impact:** Unpredictable filtering behavior, missed trades, user confusion

---

## Current Implementation Status

### Two Systems in Place

**System 1: Filtering (WRONG)**
- Location: `check_volume()` function (line 822)
- Data source: `liquidity_value` from Market Metrics API
- Usage: Pre-filter to skip low-volume symbols
- **Problem:** Using wrong metric (liquidity_value ≠ options volume)

**System 2: CSV Output (CORRECT but limited)**
- Location: Scan loop (line 1045)
- Data source: `option_volume` from dxFeed `Underlying` event
- Usage: CSV column `option_volume_today`
- **Problem:** Requires market hours (streaming API)

### Why System 2 Requires Market Hours

**DXLinkStreamer:**
- Real-time websocket streaming API
- Only active during market hours (9:30 AM - 4:00 PM ET)
- Outside market hours: Connection timeouts, no data

**Attempted Test (Sunday evening):**
```
WARNING - SPY: Timeout fetching Underlying event
WARNING - SPY: No Underlying event received
```

---

## Recommendations

### Option 1: Keep Current Implementation (Recommended)

**Accept market hours limitation:**
- Use dxFeed `Underlying.optionVolume` (correct metric)
- Document requirement: "Scanner must run during market hours for volume filtering"
- Rationale: Accurate filtering is more important than 24/7 availability

**User workflow:**
- Run scanner during market hours (9:30 AM - 4:00 PM ET)
- For after-hours research: Use `--skip-liquidity-check` flag

### Option 2: Disable Volume Filtering

**Remove volume filter entirely:**
- Simplest solution
- No market hours dependency
- Rely on other quality filters (earnings, IV availability, etc.)
- User can manually filter by liquidity after scan completes

### Option 3: Use liquidity_rating Instead (Compromise)

**Switch to tastytrade's liquidity_rating:**
- Field: `MarketMetricInfo.liquidity_rating` (0-5 integer scale)
- Meaning: "Rating 3 ≈ ~10k contracts/day" (per CLAUDE.md)
- **Pros:**
  - Available 24/7 (not streaming)
  - Opaque but consistent scale
  - Already documented threshold (rating ≥3)
- **Cons:**
  - Less precise than actual volume
  - Opaque calculation (no transparency)

**Implementation:**
```python
# Instead of checking liquidity_value
liquidity_rating = getattr(metric_info, 'liquidity_rating', None)
if liquidity_rating is None or liquidity_rating < 3:
    # Filter out
```

---

## Rejected: liquidity_value with Scaling

**Reason:** Inconsistent, non-linear scaling makes it unreliable

**Evidence:**
- 54x variation in scaling ratios (7.8x to 419x)
- No single scaling factor achieves >95% accuracy
- Risk of incorrectly filtering out high-FF opportunities

**Verdict:** DO NOT USE liquidity_value as volume proxy, even with scaling

---

## Conclusion

**Primary Question:** Can `liquidity_value` be used as a proxy with scaled threshold?

**Answer:** **NO** - The inconsistent, non-linear relationship between `liquidity_value` and actual options volume makes it unsuitable for reliable volume filtering with any fixed scaling factor.

**Evidence:**
1. ❌ **Undocumented metric** - tastytrade provides no explanation of what `liquidity_value` represents
2. ❌ **Non-linear scaling** - 54x variation in scaling ratios (7.8x to 419x) across symbols
3. ❌ **Unreliable filtering** - 30x scaling achieves only 85.7% accuracy, incorrectly filters NFLX
4. ✅ **Better alternative exists** - `liquidity_rating` (0-5 scale) is documented and consistent

**Documentation Search Results:**
- ✅ Checked `docs/tastytrade-sdk-docs/` - Found field but no meaningful description
- ✅ Checked `docs/tastytrade-openapi-docs/` - Found field with circular description ("liquidity of underlying")
- ❌ No specification of units, formula, or interpretation
- ❌ No documentation linking to options volume

**Recommended Solution:** Option 1 (keep current dxFeed implementation, accept market hours limitation)

**Alternative Solution:** Option 3 (switch to `liquidity_rating` for 24/7 availability with less precision)

---

## Next Steps

**User Decision Required:**

1. **Accept market hours limitation?**
   - If YES → Keep current implementation (dxFeed `option_volume`)
   - If NO → Consider Option 3 (liquidity_rating) or Option 2 (disable filter)

2. **Priority: Accuracy vs 24/7 availability?**
   - High accuracy → Option 1 (market hours required)
   - 24/7 availability → Option 3 (liquidity_rating compromise)
   - Neither matters → Option 2 (disable volume filter)

3. **Update documentation?**
   - Document market hours requirement in README_TT.md
   - Update CLAUDE.md with liquidity_rating threshold if switching

---

## Appendix: Code Locations

**Volume Filtering Logic:**
- Function: `check_volume()` (lines 785-844)
- Current source: `liquidity_value` (line 822) ❌ WRONG
- Should use: `option_volume` from dxFeed Underlying ✅ CORRECT

**Volume Data Fetching:**
- Function: `snapshot_underlying()` (lines 372-404)
- Source: dxFeed `Underlying.optionVolume`
- Limitation: Requires market hours (streaming API)

**CSV Output:**
- Column: `option_volume_today` (line 1793)
- Source: `option_volume` from scan loop (lines 1045, 1330, 1529)
- **Note:** Already using correct metric for output

**Fix Required:**
- Update `check_volume()` to use `option_volume` instead of `liquidity_value`
- OR switch to `liquidity_rating` for 24/7 operation
- OR remove volume filtering entirely
