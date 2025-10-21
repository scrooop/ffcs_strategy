# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Forward Factor (FF) Calendar Spread** trading strategy implementation that scans liquid options to identify mispriced forward volatility opportunities. The core edge is detecting when front-month IV is "hot" (backwardation) relative to forward IV, creating profitable calendar spread setups.

**Core Concept:**
- Compute **Forward IV** between two expirations using variance decomposition
- Calculate **Forward Factor**: `FF = (Front_IV - Fwd_IV) / Fwd_IV`
- Trade calendar spreads when FF exceeds threshold (typically 0.20-0.23)
- Hold until front expiry, then close entire spread

## Repository Structure

```
ffcs_strategy/
├── scripts/
│   ├── ff_tastytrade_scanner.py    # Main scanner (tastytrade API + dxFeed)
│   └── README_TT.md                 # Scanner usage guide
└── docs/
    ├── forward-factor-calendar-spread-SOP.md  # Complete trading strategy SOP
    ├── gpt-setup-instructions1.txt            # Quick setup reference
    └── youtube_transcript_*.txt               # Source material/research

ffcs_strategy
├── CCPM_COMPLETE_SOP.md        # CCPM project management tool usage
├── data                        # Stock ticker lists
├── docs
│   ├── architecture.md
│   ├── changelog.md
│   ├── csv-schema-v3.md
│   ├── logging.md
│   ├── migrations
│   ├── strategy
│   ├── strategy_origin_docs
│   ├── tastytrade_docs
│   ├── tastytrade-oauth.txt
│   ├── usage.md
│   ├── USEFUL_RELATED_PROJECTS.md
│   └── v1_IMPLEMENTATION_PLAN.md
├── massively_bloated_old_claudemd.md
├── new_proposed_claudemd_file.md
├── scripts
│   ├── __pycache__
│   ├── earnings_cache.py
│   ├── ff_tastytrade_scanner.py
│   ├── README_TT.md
│   ├── test_all_futures.py
│   ├── test_double_calendar_strikes.py
│   ├── test_earnings_cache.py
│   ├── test_future_chain_fields.py
│   ├── test_futures_api.py
│   ├── test_futures_quote.py
│   ├── test_futures_trade.py
│   ├── test_option_chain_for_futures.py
│   └── test_volume_fix.csv
├── test_iv_ex_earn.py
├── tests
│   ├── __init__.py
│   ├── __pycache__
│   ├── 251019_2117_ff_scan_log.txt
│   ├── 251019_2117_ff_scan_output.txt
│   ├── 251019_2117_ff_scan.csv
│   ├── 251019_2147_ff_scan_SP500.csv
│   ├── futures_scan.csv
│   ├── futures_test_results.txt
│   ├── futures_test.csv
│   └── test_ff_calculations.py
└── venv
    ├── bin
    ├── include
    ├── lib
    └── pyvenv.cfg
```

## Core Architecture

### ff_tastytrade_scanner.py

**Purpose:** CLI scanner that fetches implied volatilities from tastytrade's dxFeed streamer, computes forward IV and FF ratios, and reports tradable opportunities for both ATM and double calendar spreads.

**Key Components:**

1. **Authentication:**
   - Requires `TT_USERNAME` and `TT_PASSWORD` environment variables, which are saved in ~/.zshrc
   - Production environment required for live Greeks data (sandbox has limited market data)

2. **Data Pipeline (v2.2):**
   - **Fast earnings pre-filter** → Cache → Yahoo Finance → TastyTrade → Graceful degradation
   - `fetch_market_metrics()` → batch fetch earnings dates + avg options volume for all symbols
   - Earnings/volume pre-filtering → skip symbols BEFORE expensive API calls
   - `get_market_data()` → underlying spot price
   - `NestedOptionChain.get()` → expirations & strikes with streamer symbols
   - `snapshot_greeks()` → async dxFeed Greeks snapshot for IV + delta (PRIMARY IV source)
   - `extract_xearn_iv()` → ex-earn IV (earnings-removed) from market metrics (RARE fallback if Greeks missing)
   - Structure-based scanning: ATM-only, double calendar (±35Δ), or both

3. **Forward IV Calculation:**
   ```python
   # Variance decomposition approach
   T1 = DTE_front/365
   T2 = DTE_back/365
   fwd_var = (IV2^2*T2 - IV1^2*T1)/(T2 - T1)
   fwd_iv = sqrt(fwd_var)
   FF = (IV_front - fwd_iv) / fwd_iv  # Correct formula per transcript
   ```

4. **Expiration Matching:**
   - `nearest_expiration()` picks closest expiration to target DTE within tolerance (default ±5 days)
   - Common pairs: 30-60, 30-90, 60-90 DTE
   - ATM: Uses `pick_atm_strike()` to find strike with delta closest to 50Δ (0.50 absolute delta)
   - Double calendar: Uses `pick_delta_strike()` to find ±35Δ strikes within tolerance

5. **Greeks Streaming:**
   - `snapshot_greeks()` subscribes to dxFeed Greeks via DXLinkStreamer
   - Collects (IV, delta) tuples for each strike with timeout (default 3s)
   - Handles partial results if some legs fail to arrive

6. **Quality Filtering (v2.2):**
   - **Fast earnings check:** Multi-source pipeline with SQLite cache for 80-95% runtime reduction
   - **Earnings detection:** Skip symbols with earnings between today and back expiry (default: enabled)
   - **Volume filtering:** Filter symbols by average options volume (default: ≥10k contracts/day)
   - **Greeks IV priority:** Strike-level IV from dxFeed Greeks (preserves skew), rare ex-earn IV fallback
   - **Delta tolerance:** Control strike selection precision for double calendars (default: ±5Δ)

## Running the Scanner

### Setup (First Time)

```bash
# Install tastytrade SDK
python -m pip install --upgrade tastytrade

# Set environment variables (add to ~/.zshrc or ~/.bashrc)
export TT_USERNAME="your_username"
export TT_PASSWORD="your_password"
```

### Basic Usage

```bash
# Daily pre-market scan with quality filtering (ATM + double calendars)
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL TSLA NVDA META AMZN \
  --pairs 30-60 \
  --min-ff 0.23 \
  --csv-out scan.csv

# Scan both ATM and double calendar structures
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 30-90 60-90 \
  --structure both \
  --min-ff 0.20 \
  --csv-out ff_scan.csv

# Scan double calendars only (±35Δ call and put)
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 60-90 \
  --structure double \
  --min-ff 0.20

# Allow trading through earnings (disable earnings filter)
python scripts/ff_tastytrade_scanner.py \
  --tickers AAPL \
  --pairs 30-90 \
  --allow-earnings \
  --min-ff 0.23

# See what was filtered due to earnings
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL TSLA NVDA \
  --pairs 30-60 \
  --show-earnings-conflicts

# Adjust delta tolerance for double calendars (tighter selection)
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY \
  --pairs 30-60 \
  --structure double \
  --delta-tolerance 0.03
```

### Command Line Flags

**Core Parameters:**
- `--tickers`: Space or comma-separated symbols (required)
- `--pairs`: DTE pairs like `30-60 30-90` (front-back, required)
- `--min-ff`: Minimum FF ratio to include (default 0.20)
- `--dte-tolerance`: Max deviation from target DTE (default 5 days)
- `--timeout`: Streamer snapshot timeout in seconds (default 3s)

**Structure Selection:**
- `--structure {atm-call,double,both}`: Calendar structure type (default: both)
  - `atm-call`: ATM call calendars only
  - `double`: Double calendars (±35Δ call and put) only
  - `both`: Scan both structures (recommended)
- `--delta-tolerance`: Max delta deviation for double calendars (default: 0.05 = ±5Δ, range: 0.01-0.10)

**Earnings Filtering:**
- **Default behavior**: Earnings filtering is enabled (no flag needed)
- `--allow-earnings`: Allow trading through earnings (disable earnings filtering)
- `--show-earnings-conflicts`: Show filtered positions due to earnings

**Volume/Liquidity Filtering:**
- **Default:** Uses `liquidity_rating >= 3` from Market Metrics (24/7 available, ~10k volume equivalent)
- `--options-volume [THRESHOLD]`: Use precise dxFeed option volume filtering (requires market hours)
  - No value: threshold = 10,000 contracts
  - With value: threshold = custom value (e.g., `--options-volume 5000`)
- `--skip-liquidity-check`: Disable all volume/liquidity filtering

**Output Options:**
- `--csv-out`: Write results to CSV file (recommended, 40-column schema)
- `--json-out`: Write results to JSON file
- `--sandbox`: Use sandbox environment (production required for live Greeks)
- `--show-all-scans`: Show all scan results regardless of FF threshold (for testing)

## v2.1 Features

### Fast Earnings Check with Caching

**Performance Impact:**
- 80-95% runtime reduction during heavy earnings weeks
- 1000 symbols: ~8 minutes → <30 seconds
- Same-day rescans: <1 second (cache hits)

**Multi-Source Pipeline (Priority Order):**
1. **SQLite Cache** (`.cache/earnings.db`): Instant lookup (<10ms per symbol)
2. **Yahoo Finance**: Fast primary source (~100ms per symbol, 5s timeout)
3. **TastyTrade API**: Fallback source (~500ms per symbol)
4. **Graceful degradation**: If all sources fail, symbol allowed through with warning

**Cache Behavior:**
- **Location**: `.cache/earnings.db` (SQLite database in project root)
- **Invalidation**: Automatic when cached earnings date has passed
- **Persistence**: Survives restarts, shared across all scans
- **Management**: Safe to delete manually (`rm .cache/earnings.db`), rebuilds automatically

**CSV Tracking:**
- `earnings_source` column tracks data provenance
- Values: `cache`, `yahoo`, `tastytrade`, `none`, `skipped`

**Performance Benchmarks:**
- 112 symbols (cold cache): ~10s
- 112 symbols (warm cache): <1s
- Cache hit rate: >90% for daily scanning workflows

---

## v2.0 Features

### Quality Filtering Thresholds

**Earnings Detection:**
- Default: Skip symbols with earnings between today and back expiry
- Threshold: Any earnings date that falls between today and back expiration (inclusive)
- Override: Use `--allow-earnings` to disable filtering
- Debugging: Use `--show-earnings-conflicts` to see filtered opportunities

**Volume Filtering:**
- Default: Minimum average options volume of 10,000 contracts/day
- Uses liquidity_value field from Market Metrics API as volume proxy
- Transparent, numerical threshold (replaces opaque rating system)
- Override: Use `--skip-liquidity-check` to disable filtering

**Delta Tolerance (Double Calendars):**
- Target: ±35Δ strikes (0.35 call delta, -0.35 put delta)
- Default tolerance: ±5Δ (0.05)
- Range: 0.01 to 0.10 (tighter to looser selection)
- Tighter tolerance (0.03): More precise strikes, may skip symbols
- Looser tolerance (0.10): More opportunities, less precise deltas

### IV Source Priority (v2.2)

**Greeks IV is Primary (Strike-Level Precision):**
- Strike-specific IV from dxFeed Greeks (preserves volatility smile/skew)
- For double calendars: ±35Δ strikes may have 5-10% IV difference vs ATM
- Wing-exact FF requires strike-specific IV for accurate pricing
- Scanner always fetches Greeks IV first

**Ex-earn IV is Rare Fallback (Expiration-Level):**
- Earnings-removed IV from tastytrade Market Metrics API
- Expiration-level only (single value per expiration, collapses skew)
- Used only when Greeks IV missing/timeout for a specific leg
- Less accurate for wings due to lack of strike-level granularity

**How It Works (v2.2):**
1. Scanner fetches Greeks IV from dxFeed snapshot for all strikes (PRIMARY)
2. If Greeks IV missing/invalid for any leg, fallback to ex-earn IV (RARE)
3. CSV output tracks source per leg: `iv_source_call_front`, `iv_source_call_back`, `iv_source_put_front`, `iv_source_put_back`
4. Source values: "greeks" (primary) or "exearn_fallback" (rare fallback)
5. Logger warns when fallback used: `logger.warning("Greeks IV missing for X, using ex-earn fallback")`

### IV Variation Across Strikes: How It Affects FF Calculations

**CRITICAL IMPLEMENTATION DETAIL:** The scanner uses IV from the **actual strikes being traded**, not a generic "term structure IV".

**For ATM Call Calendars:**
- **σ₁ (front IV):** IV from the **ATM strike** at front expiration
  - ATM strike = strike with delta closest to 50Δ (0.50 absolute delta)
  - IV = average of (call IV, put IV) at that 50Δ strike
- **σ₂ (back IV):** IV from the **ATM strike** at back expiration
- **FF Calculation:** `atm_ff = (σ_atm_front - σ_atm_fwd) / σ_atm_fwd` using averaged ATM IVs

**For Double Calendars (±35Δ):**
- **REQUIRES BOTH LEGS:** Call calendar AND put calendar must both be available
  - If only one leg meets delta tolerance, symbol is skipped for double calendar structure
  - May still appear in ATM structure if `--structure both` (default)
- **Call calendar:** Uses IV from the **+35Δ call strike** at both expirations
- **Put calendar:** Uses IV from the **−35Δ put strike** at both expirations
- **Strike selection:** Finds strike with delta closest to ±0.35 (within ±0.05 tolerance, default)
- **Separate FF calculations:** Call and put calendars have independent FFs
- **CSV output:** ONE row per double calendar with both call_strike and put_strike populated

**Why IV Variation Matters:**

Implied volatility varies significantly across the option chain due to **volatility skew**:
- **Typical magnitude:** 5-10 percentage points between ATM and OTM options
- **Equity skew pattern:**
  - OTM puts: Higher IV than ATM (downside protection premium)
  - OTM calls: Lower IV than ATM
- **Example (SPY):**
  - ATM (50Δ): 20% IV
  - +35Δ call: ~18% IV (10% lower)
  - −35Δ put: ~25% IV (25% higher)

**Impact on FF Calculations:**

Given the same underlying and term structure, the three calendar structures will show **different FF values**:
1. **ATM calendar:** FF based on 20% IV (baseline)
2. **+35Δ call calendar:** FF based on 18% IV (~10% lower FF)
3. **−35Δ put calendar:** FF based on 25% IV (~25% higher FF)

**Practical Implications:**
- Double calendars "tap into skew" by trading both term structure AND strike-level mispricing
- Put calendars typically show higher FF than ATM calendars on the same underlying
- This is **by design** - you're trading the actual strikes, so use those strikes' IVs
- Scanner outputs both `call_ff` and `put_ff` to show this variation
- `combined_ff` = average of call and put FFs for ranking/sorting

**Code Implementation:**
- `pick_atm_strike()`: Selects strike with delta closest to 50Δ (0.50 absolute delta), returns its Greeks symbols
- `pick_delta_strike()`: Selects strike closest to target delta, returns IV from that strike
- `snapshot_greeks()`: Fetches actual IV from dxFeed for each specific strike
- Forward IV calculation uses these strike-specific IVs, not interpolated surface values

### CSV Output Schema (32 Columns - v3.0)

Results are **unsorted** (written in scan order) due to streaming CSV writer for memory efficiency. Sort post-scan if needed: by `ff` (ATM) or `min_ff` (double) descending.

**IMPORTANT:** Double calendars REQUIRE BOTH call and put legs. If only one leg meets delta tolerance, the symbol is skipped for double calendar structure (but may still appear in ATM structure if `--structure both`).

**Key Design Principle (v3.0 Unified Namespace):**
- **Eliminated redundant `atm_*` columns** - ATM and double structures now use the same column names
- For ATM calendars: `ff` contains single forward factor using averaged IVs from 50Δ strike
- For double calendars: `ff` contains call leg FF, `put_ff` contains put leg FF, with `min_ff` for filtering
- This design reduces CSV from 40 → 32 columns (20% reduction), eliminating 16 empty columns per row

**Common Columns (All Structures - 8 columns):**
- `timestamp`: ISO 8601 UTC timestamp (e.g., "2025-10-19T14:30:00+00:00")
- `symbol`: Ticker symbol
- `structure`: "atm-call" or "double"
- `spot_price`: Current underlying price
- `front_dte`, `back_dte`: Days to expiration
- `front_expiry`, `back_expiry`: Expiration dates (YYYY-MM-DD)

**Strike/Delta Columns (Unified Namespace - 4 columns):**
- `strike`: Call strike (50Δ for ATM, +35Δ for double)
- `put_strike`: Put strike for double calendars (empty for ATM)
- `delta`: Call delta (0.50 for ATM, 0.35 for double)
- `put_delta`: Put delta for double calendars (empty for ATM)

**FF Metrics (Unified Namespace - 4 columns):**
- `ff`: Forward factor for call leg (or single FF for ATM)
- `put_ff`: Forward factor for put leg (empty for ATM)
- `min_ff`: Minimum of (ff, put_ff) for double; same as ff for ATM
- `combined_ff`: Average of (ff, put_ff) for double (empty for ATM)

**IV Detail Columns (All Structures - 6 columns):**
- `call_front_iv`, `call_back_iv`, `call_fwd_iv`: Call leg IVs (decimal: 0.25 = 25%)
- `put_front_iv`, `put_back_iv`, `put_fwd_iv`: Put leg IVs (decimal: 0.25 = 25%)
- For ATM: Average of call+put IVs from 50Δ strike
- For double: IVs from ±35Δ strikes (different from ATM IVs due to skew)

**IV Source Tracking (All Structures - 4 columns):**
- `iv_source_call_front`, `iv_source_call_back`: Call IV sources ("greeks" or "exearn_fallback")
- `iv_source_put_front`, `iv_source_put_back`: Put IV sources ("greeks" or "exearn_fallback")

**Quality Filter Columns (All Structures - 6 columns):**
- `earnings_conflict`: "yes" or "no"
- `earnings_date`: Next earnings date (YYYY-MM-DD, empty if none)
- `option_volume_today`: Today's total option chain volume (from dxFeed Underlying.optionVolume)
- `liq_rating`: Liquidity rating 0-5 from Market Metrics API (used for default 24/7 filtering)
- `earnings_source`: Earnings data source ("cache", "yahoo", "tastytrade", "none", or "skipped")
- `skip_reason`: Reason symbol was filtered (e.g., "earnings_conflict", "volume_too_low", empty if not skipped)

**Complete Column Order (32 columns):**
`timestamp`, `symbol`, `structure`, `spot_price`, `front_dte`, `back_dte`, `front_expiry`, `back_expiry`, `strike`, `put_strike`, `delta`, `put_delta`, `ff`, `put_ff`, `min_ff`, `combined_ff`, `call_front_iv`, `call_back_iv`, `call_fwd_iv`, `put_front_iv`, `put_back_iv`, `put_fwd_iv`, `iv_source_call_front`, `iv_source_call_back`, `iv_source_put_front`, `iv_source_put_back`, `earnings_conflict`, `earnings_date`, `option_volume_today`, `liq_rating`, `earnings_source`, `skip_reason`

### Migration Guide: v2.2 → v3.0

**Schema Changes:**
- Column count: 40 → 32 (-8 columns)
- Eliminated `atm_*` column namespace (unified with call columns)
- CSV output now unsorted (streaming writer for memory efficiency)

**Column Mapping Table:**

| v2.2 Column | v3.0 Column | Notes |
|-------------|-------------|-------|
| `atm_strike` | `strike` | Unified namespace (ATM & double use same column) |
| `atm_delta` | `delta` | Unified namespace |
| `atm_ff` | `ff` | Unified namespace (ATM rows) |
| `atm_iv_front` | *(removed)* | Redundant with `call_front_iv` + `put_front_iv` |
| `atm_iv_back` | *(removed)* | Redundant with `call_back_iv` + `put_back_iv` |
| `atm_fwd_iv` | *(removed)* | Redundant with `call_fwd_iv` + `put_fwd_iv` |
| `atm_iv_source_front` | *(removed)* | Use `iv_source_call_front` + `iv_source_put_front` |
| `atm_iv_source_back` | *(removed)* | Use `iv_source_call_back` + `iv_source_put_back` |
| `call_strike` | `strike` | Renamed to unified namespace |
| `call_delta` | `delta` | Renamed to unified namespace |
| `call_ff` | `ff` | Renamed to unified namespace (double rows) |
| `put_strike` | `put_strike` | Unchanged |
| `put_delta` | `put_delta` | Unchanged |
| `put_ff` | `put_ff` | Unchanged |
| `min_ff` | `min_ff` | Unchanged |
| `combined_ff` | `combined_ff` | Unchanged |
| All other columns | (unchanged) | IVs, sources, quality filters remain identical |

**Breaking Changes:**

1. **ATM Structure Workflow Change:**
   - v2.2: ATM rows populated `atm_strike`, `atm_delta`, `atm_ff` columns (dedicated namespace)
   - v3.0: ATM rows populate `strike`, `delta`, `ff` columns (unified namespace)
   - **Impact:** CSV parsers must use `ff` for both ATM and double structures

2. **Column Rename Impact:**
   - v2.2: `call_strike`, `call_delta`, `call_ff` for double calendars
   - v3.0: `strike`, `delta`, `ff` for double calendars
   - **Impact:** Update all column references to unified names

3. **CSV Output Unsorted:**
   - v2.2: Rows sorted by `atm_ff` (ATM) or `min_ff` (double) descending
   - v3.0: Rows unsorted (written in scan order for streaming efficiency)
   - **Impact:** Sort CSV post-scan if needed (`df.sort_values("ff", ascending=False)`)

4. **Removed Columns:**
   - v2.2: 8 `atm_*` columns existed
   - v3.0: All `atm_*` columns removed (use unified equivalents)
   - **Impact:** Update parsers to use `call_front_iv`, `put_front_iv` (etc.) for ATM rows

**Migration Steps for CSV Consumers:**

1. **Update column count:** 40 → 32
2. **Rename column references:**
   - `atm_ff` → `ff` (for ATM structure filtering)
   - `atm_strike` → `strike` (for ATM strike prices)
   - `atm_delta` → `delta` (for ATM deltas)
   - `call_strike` → `strike` (for double structure)
   - `call_delta` → `delta` (for double structure)
   - `call_ff` → `ff` (for double structure)
3. **Remove column references:** Delete all `atm_iv_*` and `atm_iv_source_*` from parsers
4. **Add post-scan sorting (if needed):** CSV no longer pre-sorted
5. **Update ATM IV extraction:** Use `call_front_iv`, `put_front_iv` (averaged) instead of `atm_iv_front`

**Example v3.0 CSV Parsing (Python):**

```python
import pandas as pd

# Read v3.0 CSV
df = pd.read_csv("scan_v3.0.csv")

# Filter ATM opportunities (use ff, not atm_ff)
atm_opps = df[df["structure"] == "atm-call"]
atm_opps = atm_opps[atm_opps["ff"] >= 0.23]  # v3.0: use ff
atm_opps = atm_opps.sort_values("ff", ascending=False)  # Manual sort

# Filter double opportunities (use min_ff for filtering, ff for ranking)
double_opps = df[df["structure"] == "double"]
double_opps = double_opps[double_opps["min_ff"] >= 0.20]  # v3.0: min_ff for filtering
double_opps = double_opps.sort_values("min_ff", ascending=False)  # Manual sort

# Access strikes using unified columns
for idx, row in atm_opps.iterrows():
    print(f"{row['symbol']}: ATM strike={row['strike']}, FF={row['ff']}")  # v3.0: strike, ff

for idx, row in double_opps.iterrows():
    print(f"{row['symbol']}: Call strike={row['strike']}, Put strike={row['put_strike']}")  # v3.0: unified
```

---

### Migration Guide: v2.1 → v2.2 (Historical Reference)

**Schema Changes:**
- Column count: 31 → 40 (+10 columns, -1 renamed)
- ATM structure: New dedicated columns for simplified single-FF workflow
- Double structure: Added `min_ff` for filtering worst-case leg
- Volume filtering: Hybrid system with liquidity_rating (default) and option_volume (optional)

**Column Mapping Table:**

| v2.1 Column | v2.2 Column | Notes |
|-------------|-------------|-------|
| `avg_options_volume` | `option_volume_today` | Changed to today's volume from dxFeed (only populated with --options-volume) |
| `liquidity_rating` | `liq_rating` | Now always exported to CSV (0-5 scale, used for default filtering) |
| `liquidity_value` | (removed) | Replaced by liq_rating and option_volume_today |
| N/A | `atm_strike` | NEW: Strike with delta closest to 50Δ |
| N/A | `atm_delta` | NEW: Actual delta of selected ATM strike |
| N/A | `atm_ff` | NEW: Single FF for ATM structure (replaces dual call_ff/put_ff) |
| N/A | `atm_iv_front` | NEW: Front IV at ATM strike |
| N/A | `atm_iv_back` | NEW: Back IV at ATM strike |
| N/A | `atm_fwd_iv` | NEW: Forward IV for ATM structure |
| N/A | `atm_iv_source_front` | NEW: IV source tracking for ATM front |
| N/A | `atm_iv_source_back` | NEW: IV source tracking for ATM back |
| N/A | `min_ff` | NEW: Minimum of (call_ff, put_ff) for double calendars |
| N/A | `skip_reason` | NEW: Tracking field for filtering reasons |
| `call_ff` | `call_ff` | Unchanged for double, empty for ATM |
| `put_ff` | `put_ff` | Unchanged for double, empty for ATM |
| `combined_ff` | `combined_ff` | Unchanged for double, empty for ATM |

**Breaking Changes:**

1. **ATM Structure Workflow Change:**
   - v2.1: ATM rows populated `call_ff`, `put_ff`, `combined_ff` (dual-FF approach)
   - v2.2: ATM rows populate `atm_ff` only (single-FF approach), double columns empty
   - **Impact:** CSV parsers must check `atm_ff` for ATM structures (not `combined_ff`)

2. **ATM Strike Selection Change:**
   - v2.1: ATM strike = strike price closest to spot
   - v2.2: ATM strike = strike with delta closest to 50Δ (0.50 absolute delta)
   - **Impact:** More delta-accurate strike selection, may select different strikes

3. **Column Rename:**
   - v2.1: `avg_options_volume`
   - v2.2: `option_volume_today`
   - **Impact:** CSV parsers must update column name reference
   - **Data Change:** Now shows today's actual volume (dxFeed Underlying) instead of 20-day average

4. **Removed Columns:**
   - v2.1: `liquidity_rating`, `liquidity_value` (removed in v2.2, already gone in v2.1.1)
   - v2.2: Use `option_volume_today` for volume-based filtering
   - **Impact:** Update filters to use `option_volume_today >= 10000` instead of `liquidity_rating >= 3`

5. **Double Calendar Sorting Change:**
   - v2.1: Sorted by `combined_ff` (average of call and put FFs)
   - v2.2: Sorted by `min_ff` (minimum of call and put FFs)
   - **Impact:** More conservative filtering (worst-case leg must meet threshold)

**CLI Flag Changes:**

Removed (no longer supported):
- `--use-xearn-iv` (ex-earn IV now rare fallback, not primary)
- `--force-greeks-iv` (Greeks IV now always primary)
- `--min-liquidity-rating` (replaced by hybrid liquidity system)
- `--min-avg-volume` (replaced by --options-volume)

Updated:
- `--options-volume [THRESHOLD]`: Precise volume filtering (optional, requires market hours)
- `--skip-liquidity-check`: Disables all volume/liquidity filtering (unchanged)

**Migration Steps for CSV Consumers:**

1. **Update column count:** 31 → 40
2. **Add new columns:** Parse `atm_strike`, `atm_delta`, `atm_ff`, `atm_iv_*`, `min_ff`, `liq_rating`, `skip_reason`
3. **Rename column:** `avg_options_volume` → `option_volume_today` (may be empty if not using --options-volume)
4. **Rename column:** `liquidity_rating` → `liq_rating` (always populated now)
5. **Remove column references:** Delete `liquidity_value` from parsers
6. **Update ATM logic:** Check `atm_ff` for ATM structures (not `call_ff`/`put_ff`/`combined_ff`)
7. **Update double logic:** Use `min_ff` for filtering, `combined_ff` for ranking
7. **Update filters:** Replace liquidity rating checks with volume checks (`>= 10000`)

**Example v2.2 CSV Parsing (Python):**

```python
import pandas as pd

# Read v2.2 CSV
df = pd.read_csv("scan_results.csv")

# Filter ATM opportunities (use atm_ff, not combined_ff)
atm_opps = df[df["structure"] == "atm-call"]
atm_opps = atm_opps[atm_opps["atm_ff"] >= 0.23]  # v2.2: use atm_ff
atm_opps = atm_opps.sort_values("atm_ff", ascending=False)

# Filter double opportunities (use min_ff for filtering, combined_ff for ranking)
double_opps = df[df["structure"] == "double"]
double_opps = double_opps[double_opps["min_ff"] >= 0.20]  # v2.2: min_ff for filtering
double_opps = double_opps.sort_values("min_ff", ascending=False)  # or combined_ff for ranking

# Volume filtering (updated column name and data source)
filtered = df[df["option_volume_today"] >= 10000]  # v2.2: today's volume from dxFeed
```

## Terminal Output & Logging (v3.0)

### Hierarchical Logging System

The scanner uses a hierarchical Python logging system with clean, professional terminal output.

**Logger Hierarchy:**
```
scanner (root)
├── scanner.earnings (earnings data fetching)
├── scanner.market_data (quotes, chains, underlying events)
├── scanner.greeks (IV streaming, delta selection)
└── scanner.quality (earnings/volume/liquidity filtering)
```

**Output Modes:**

| Mode | Level | Use Case | Output Format |
|------|-------|----------|---------------|
| **normal** (default) | INFO | Daily scanning | `[SYMBOL] STATUS: details` |
| **debug** | DEBUG | Troubleshooting | `2025-10-20 14:30:15 - scanner.greeks - INFO - SPY: message` |

**SymbolFormatter Output (Normal Mode):**
```
[SPY   ] INFO : Option volume today: 150000
[QQQ   ] WARN : Greeks IV missing for call front leg, using ex-earn fallback
[AAPL  ] INFO : FILTER - Earnings on 2025-11-15 conflicts with back expiry 2025-11-30
SCANNER: INFO : === Scan Summary ===
SCANNER: INFO : Scanned: 7 symbols
SCANNER: INFO : Passed: 3 opportunities
```

**Third-Party Logger Suppression:**

The scanner automatically suppresses verbose output from:
- `yfinance` (ERROR level only - eliminates HTTP 404 spam for futures)
- `tastytrade` SDK (WARNING level)
- `httpx` HTTP client (WARNING level)
- `earnings_cache` (WARNING level)

This ensures clean terminal output without noise from external libraries.

### CSV Writer (Streaming)

The v3.0 scanner uses a streaming CSV writer for O(1) memory usage, enabling scans of 1500+ symbols without memory concerns.

**Key Features:**
- Writes rows immediately as they're scanned (no buffering)
- Constant memory usage regardless of symbol count
- CSV output unsorted (appears in scan order, not FF order)

**Trade-off:**
- v2.2: Sorted CSV output (all rows buffered, then sorted, then written)
- v3.0: Unsorted CSV output (rows written immediately for memory efficiency)

**Workaround:** Sort post-scan if needed:
```python
df = pd.read_csv("scan.csv")
df_sorted = df.sort_values("ff", ascending=False)  # ATM
df_sorted = df.sort_values("min_ff", ascending=False)  # Double
```

**Performance Benefits:**
- 1000 symbols: Constant ~500MB RAM (vs ~2GB buffered)
- 1500 symbols: Constant ~500MB RAM (vs ~3GB+ buffered, risk of OOM)
- No memory growth as symbol count increases

## Strategy Implementation Notes

### Trade Thresholds (from Video Transcript)

**General Rule of Thumb (per transcript):**
> "If your forward factor reads at **0.20 or higher**, we can go long the calendar or double calendar."

**When Returns Start Becoming Positive (scatter plot analysis):**
> "Visibly, we can see from the graph that a factor at or above around **0.1 to 0.2** is when returns start becoming positive."

**Optimized FF Thresholds for ~20 Trades/Month:**

*ATM Call Calendars:*
- 30-60 DTE: FF ≥ 0.23
- 30-90 DTE: FF ≥ 0.23
- 60-90 DTE: FF ≥ 0.20

*Double Calendars (±35Δ):*
- 30-60 DTE: FF ≥ 0.23
- 30-90 DTE: FF ≥ 0.23
- 60-90 DTE: FF ≥ 0.20

**Summary:** Use FF ≥ 0.20 as general threshold; use FF ≥ 0.23 for 30-60 and 30-90 DTE pairs to target ~20 quality trades per month.

### Position Sizing

- Default: 2-8% of equity per trade (4% typical)
- Alternative: Fractional Kelly (~¼-Kelly)
- Prioritize highest FF names first until risk caps met

### Trade Management

- **Entry:** Long calendar spread (sell front, buy back) as single spread order
- **Hold:** No adjustments, hold until front expiry day
- **Exit:** Close entire spread just before front expiry (avoid pin risk)
- **No legging:** Close as spread unless necessary for fills

## Important Caveats

### Production vs Sandbox
- **Production environment required** for live Greeks and market data
- Sandbox returns minimal/no live data for most symbols

### IV Data Handling
- If only one leg (call or put) IV arrives, scanner uses that single value
- If both legs fail to arrive within timeout, that target DTE is skipped
- Greeks.volatility is Black-Scholes IV (annualized, decimal format: 0.25 = 25%)
- Greeks IV is primary (strike-level), ex-earn IV is rare fallback (see CSV `iv_source` columns)

### Earnings Filtering (v2.1)
- **Fast pre-filter with caching:** Multi-source pipeline (Cache → Yahoo → TastyTrade) with 80-95% runtime reduction
- **Default behavior:** Filtering enabled automatically (no flag needed)
- Threshold: Any earnings between today and back expiry (inclusive)
- Override: Use `--allow-earnings` to disable filtering
- Debugging: Use `--show-earnings-conflicts` to see what was filtered
- Cache location: `.cache/earnings.db` (safe to delete, rebuilds automatically)

### Volume/Liquidity Filtering (v2.2)
- **Hybrid filtering system:** Choose between two modes
- **Default mode (24/7):** Uses `liquidity_rating >= 3` from Market Metrics API (~10k volume equivalent)
- **Precise mode (market hours):** Use `--options-volume [THRESHOLD]` for dxFeed option volume filtering
  - Without value: `--options-volume` uses 10,000 threshold
  - With value: `--options-volume 5000` uses custom threshold
- Override: Use `--skip-liquidity-check` to disable all filtering
- Futures handling: Symbols without data are allowed through (not an error)
- **liq_rating column:** Always exported to CSV for transparency (0-5 scale)

### Double Calendar Strike Selection (v2.0)
- Target: ±35Δ strikes with configurable tolerance
- If no strikes within tolerance, symbol is skipped for double calendar structure
- ATM structure still scanned if `--structure both` (default)
- Adjust `--delta-tolerance` if too many symbols are skipped

## Troubleshooting

### Common Issues and Solutions

**Issue: "Delta not found within tolerance" (ATM or double structure)**
- **Cause:** No strikes with delta close enough to target (50Δ for ATM, ±35Δ for double)
- **Solution 1:** Increase `--delta-tolerance` (default 0.05, try 0.08 or 0.10)
- **Solution 2:** Use `--structure both` to allow ATM fallback if double fails
- **Note:** Low-liquidity symbols may have wide strike spacing causing delta gaps

**Issue: "Volume data missing" or "skip_reason: volume_too_low"**
- **Cause:** Market Metrics API failed to return volume data, or volume below threshold
- **Solution 1:** Check `.cache/` directory exists and is writable
- **Solution 2:** Verify tastytrade API connectivity (production environment required)
- **Solution 3:** Disable volume filtering with `--skip-liquidity-check`
- **Solution 4:** Lower volume threshold with `--min-avg-volume 5000`
- **Note:** Futures often lack volume data and are allowed through automatically

**Issue: "Earnings conflict" filtering too many symbols**
- **Cause:** Symbol has earnings between today and back expiry (default filtering enabled)
- **Solution 1:** Disable earnings filtering with `--allow-earnings`
- **Solution 2:** Use shorter DTE pairs (30-60 instead of 30-90) to avoid earnings window
- **Solution 3:** Check `--show-earnings-conflicts` to see what's being filtered
- **Note:** Trading through earnings violates strategy rules (high gamma risk)

**Issue: Empty `atm_ff` column in CSV (ATM structure)**
- **Cause:** Likely parsing v2.1 CSV with v2.2 parser (or vice versa)
- **Solution:** Verify CSV version (31 cols = v2.1, 39 cols = v2.2)
- **Note:** v2.1 uses `call_ff`/`put_ff`/`combined_ff` for ATM, v2.2 uses `atm_ff`

**Issue: Empty `min_ff` column in CSV (double structure)**
- **Cause:** Likely parsing v2.1 CSV with v2.2 parser
- **Solution:** Regenerate CSV with v2.2 scanner
- **Note:** v2.1 does not have `min_ff` column (added in v2.2)

**Issue: Greeks IV timeout (partial results)**
- **Cause:** dxFeed streamer timeout (default 3s) before all Greeks arrived
- **Solution 1:** Increase `--timeout 5` (or 10 for slow connections)
- **Solution 2:** Verify production environment (sandbox has limited data)
- **Solution 3:** Check network connectivity to tastytrade servers
- **Note:** Scanner uses partial results if available, warns about missing legs

**Issue: Ex-earn IV fallback warnings in logs**
- **Cause:** Greeks IV missing/invalid for a specific leg, fallback to ex-earn IV
- **Solution:** This is expected behavior (graceful degradation)
- **Note:** Check `atm_iv_source_*` or `iv_source_*` columns to verify source
- **Impact:** Ex-earn IV is expiration-level (less accurate than strike-level Greeks)

**Issue: "No strikes found for target DTE"**
- **Cause:** Target DTE not available (e.g., requesting 30 DTE when only monthly expirations exist)
- **Solution 1:** Increase `--dte-tolerance 7` (default 5 days)
- **Solution 2:** Use standard DTE pairs: 30-60, 30-90, 60-90
- **Solution 3:** Check if symbol has weekly expirations (SPY, QQQ) vs monthly only
- **Note:** Some futures have non-standard expiration cycles

**Issue: CSV sorting unexpected (not by FF)**
- **Cause:** v2.2 sorts by `atm_ff` (ATM) or `min_ff` (double), not `combined_ff`
- **Solution:** Re-sort after loading CSV if needed
- **Note:** Sorting metric changed in v2.2 for more conservative filtering

### Skip Reason Codes

When symbols are filtered, `skip_reason` column contains:

- `earnings_conflict`: Earnings between today and back expiry
- `volume_too_low`: option_volume_today below threshold
- `no_strikes`: No strikes found for target DTE within tolerance
- `delta_not_found`: No strikes with delta within tolerance (ATM or double)
- `greeks_timeout`: Greeks IV timeout, no fallback available
- `no_market_data`: Failed to fetch underlying spot price
- `invalid_symbol`: Symbol not found or invalid on tastytrade
- (empty): Symbol not filtered, included in results

### Debug Commands

**Check earnings cache:**
```bash
# View cache contents (SQLite)
sqlite3 .cache/earnings.db "SELECT * FROM earnings WHERE symbol='AAPL';"

# Clear cache (force refresh)
rm .cache/earnings.db
```

**Test symbol scanning (verbose):**
```bash
# Single symbol with all flags visible
python scripts/ff_tastytrade_scanner.py \
  --tickers AAPL \
  --pairs 30-60 \
  --show-all-scans \
  --show-earnings-conflicts \
  --csv-out test.csv

# Check CSV column count
head -1 test.csv | awk -F',' '{print NF}'  # Should print 39 for v2.2
```

**Verify v2.2 schema:**
```bash
# Print CSV header
head -1 scan.csv | tr ',' '\n' | nl

# Check for v2.2-specific columns
head -1 scan.csv | grep -o "atm_ff"  # Should find atm_ff
head -1 scan.csv | grep -o "min_ff"  # Should find min_ff
```

## Strategy Theory (from SOP)

### Why This Works
Short-dated options often get bid up (volatility backwardation) while the next window is underpriced. Calendar spreads isolate and buy that forward volatility slice at a discount.

### Forward Factor Formula
```
FF = (σ₁ - σ_fwd) / σ_fwd
```
Where:
- σ₁ = annualized IV from the **strike being traded** at front expiry (ATM strike for ATM calendars, ±35Δ strike for double calendars)
- σ_fwd = forward IV between T₁ and T₂ (calculated from σ₁ and σ₂ using variance decomposition)
- FF > 0 → front IV "hot" vs forward IV → go long forward vol (calendar)

**Important:** The IV values come from the **specific strikes you're trading**, not a generic market-wide IV index. This means ATM calendars and double calendars will show different FF values for the same underlying due to volatility skew (see "IV Variation Across Strikes" section above).

### Trade Structures
1. **ATM Call Calendar** (simpler, cheaper)
   - Same strike, sell front call / buy back call
2. **Double-Calendar** (higher win rate, more complex)
   - +35Δ call calendar AND -35Δ put calendar (±5Δ acceptable)

## Futures Options Support (v2.1)

The scanner now supports futures options (e.g., /ES, /CL) in addition to equity options.

**Implementation:**
- Futures symbols start with `/` (e.g., `/ES`, not `ES`)
- Spot prices fetched from **Yahoo Finance** (tastytrade API doesn't provide futures prices)
- Option chains fetched from **tastytrade** using `NestedFutureOptionChain`
- Earnings filter automatically bypassed (futures don't have earnings)
- Greeks/IV data from tastytrade dxFeed streamer (same as equities)

**Supported Futures (verified working):**
- **`/ES`** - E-mini S&P 500 ✅
- **`/NQ`** - E-mini Nasdaq-100 ✅
- **`/RTY`** - E-mini Russell 2000 ✅
- **`/GC`** - Gold ✅
- **`/CL`** - Crude Oil ✅
- **`/MES`** - Micro E-mini S&P 500 ✅
- **`/MNQ`** - Micro E-mini Nasdaq-100 ✅
- **`/MCL`** - Micro Crude Oil ✅

**Partially Supported (chains exist but non-standard expirations):**
- `/NG`, `/LE`, `/6A`, `/6B`, `/6C`, `/6E`, `/6J`, `/BTC`, `/ETH` - May work with different DTE pairs

**Unsupported (no option chains on tastytrade):**
- `/SI`, `/ZB`, `/ZN`, `/ZF`, `/ZT`, `/ZC`, `/ZS`, `/ZW`, `/HG`, `/HE`, `/SR3`

**Usage:**
```bash
# Scan major equity index futures
python scripts/ff_tastytrade_scanner.py \
  --tickers /ES /NQ /RTY \
  --pairs 30-60 \
  --min-ff 0.20

# Scan all supported futures
python scripts/ff_tastytrade_scanner.py \
  --tickers /ES /NQ /RTY /GC /CL /MES /MNQ /MCL \
  --pairs 30-60 30-90 60-90 \
  --min-ff 0.20

# Mixed equities and futures
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY /ES QQQ /NQ AAPL \
  --pairs 30-60 \
  --min-ff 0.20
```

**Requirements:**
- `yfinance` library installed (`pip install yfinance`)
- Futures options trading approval on tastytrade account
- Internet access for Yahoo Finance API

## Future Enhancements

Scanner could be extended with:
- **Additional futures support** - Expand to more futures when tastytrade adds option chains
- Bid-ask spread quality checks (tighter filtering beyond volume threshold)
- Position tracking and P&L monitoring (track open positions)
- Auto-execution via tastytrade order API (automated order placement)
- Backtest framework using historical IV data (strategy validation)
- Iron condor / iron butterfly structures (additional strategies)
- Multi-threaded scanning for 50+ symbols (performance optimization)

## Version History

### v3.0 - CSV Schema Refactor & Professional Logging (October 2025)

**Summary:** CSV schema reduction (40 → 32 columns), streaming CSV writer for memory efficiency, hierarchical logging system with clean terminal output

**Major Changes:**
- **CSV Schema Refactor:** Eliminated `atm_*` namespace, unified columns for both ATM and double structures
- **Streaming CSV Writer:** O(1) memory usage enabling 1500+ symbol scans (trade-off: unsorted output)
- **Hierarchical Logging:** Professional terminal output with `[SYMBOL] STATUS: details` format
- **Logger Suppression:** Automatic suppression of third-party library noise (yfinance, tastytrade, httpx)

**CSV Schema Changes:**
- Reduced from 40 to 32 columns (20% reduction)
- Removed 8 columns: `atm_strike`, `atm_delta`, `atm_ff`, `atm_iv_front/back/fwd`, `atm_iv_source_front/back`
- Renamed 3 columns: `call_strike` → `strike`, `call_delta` → `delta`, `call_ff` → `ff`
- Result: Unified namespace eliminates 16 empty columns per row

**New Features:**
- **Logger Hierarchy:** `scanner`, `scanner.earnings`, `scanner.market_data`, `scanner.greeks`, `scanner.quality`
- **Custom SymbolFormatter:** Clean `[SYMBOL] STATUS: message` output (normal mode)
- **Debug Mode:** Timestamps and logger names for troubleshooting
- **Memory Efficiency:** Constant ~500MB RAM for any symbol count (vs ~2-3GB buffered for 1000+ symbols)

**Breaking Changes:**
- CSV schema v3.0 incompatible with v2.2 parsers (migration guide provided)
- CSV output now unsorted (written in scan order for streaming efficiency)
- Column references must be updated: `atm_ff` → `ff`, `call_strike` → `strike`, etc.
- Post-scan sorting required if needed: `df.sort_values("ff", ascending=False)`

**Rationale:**
- Unified namespace simplifies CSV schema and eliminates redundancy
- Streaming writer enables large-scale scans (S&P 1500, Russell 2000) without memory issues
- Professional logging improves UX and debugging (clean output, granular control)

---

### v2.2 - Core Calculation Corrections (October 2025)

**Summary:** Core calculation corrections for strategy alignment

**Major Changes:**
- ATM strike selection: Now uses 50Δ strike (closest to 0.50 absolute delta) instead of spot-based selection
- ATM FF calculation: Simplified to single `atm_ff` using averaged IVs (replaced dual call_ff/put_ff approach)
- Double calendar filtering: Added `min_ff` (minimum of call_ff and put_ff) for conservative worst-case filtering
- Volume filtering: Hybrid system with liquidity_rating (default, 24/7) and option_volume (optional, market hours)
- CSV schema: Expanded from 31 to 40 columns (+10 new columns, -1 renamed)

**New Columns:**
- `atm_strike`, `atm_delta`, `atm_ff`: ATM-specific strike selection and FF calculation
- `atm_iv_front`, `atm_iv_back`, `atm_fwd_iv`: ATM IV values
- `atm_iv_source_front`, `atm_iv_source_back`: IV source tracking for ATM
- `min_ff`: Minimum FF for double calendars (filtering metric)
- `skip_reason`: Tracking field for filtering reasons

**Renamed/Removed:**
- `avg_options_volume` → `option_volume_today` (changed to today's volume from dxFeed Underlying.optionVolume)
- Removed: `liquidity_rating`, `liquidity_value` (replaced by transparent volume from dxFeed)

**CLI Changes:**
- Removed flags: `--use-xearn-iv`, `--force-greeks-iv`, `--min-liquidity-rating`
- Greeks IV now primary source (ex-earn IV rare fallback)

**Breaking Changes:**
- ATM CSV rows: Now populate `atm_ff` instead of `call_ff`/`put_ff`/`combined_ff`
- Double CSV rows: Sorted by `min_ff` instead of `combined_ff`
- Column count: 31 → 39 (CSV parsers must update)

**Rationale:** Aligns scanner with documented strategy theory (50Δ ATM, single-FF simplicity, conservative filtering)

### v2.1 - Fast Earnings Check with Caching (September 2025)

**Summary:** 80-95% runtime reduction during heavy earnings weeks

**Major Features:**
- Multi-source earnings pipeline: Cache → Yahoo Finance → TastyTrade → Graceful degradation
- SQLite earnings cache (`.cache/earnings.db`) with automatic invalidation
- 1000 symbols: ~8 minutes → <30 seconds
- Same-day rescans: <1 second (cache hits)

**New Columns:**
- `earnings_source`: Tracks data provenance (cache/yahoo/tastytrade/none/skipped)

**Performance:**
- 112 symbols (cold cache): ~10s
- 112 symbols (warm cache): <1s
- Cache hit rate: >90% for daily scanning workflows

### v2.0 - Quality Filtering and Structure Support (August 2025)

**Summary:** Enhanced quality filtering with earnings detection, liquidity screening, and double calendar support

**Major Features:**
- Earnings detection: Skip symbols with earnings between today and back expiry
- Liquidity screening: Filter by liquidity rating (0-5 scale, default ≥3)
- X-earn IV support: Earnings-removed IV when available, graceful fallback to Greeks IV
- Double calendar structures: ±35Δ call and put calendars with separate FFs
- Delta tolerance: Configurable strike selection precision

**New Columns:**
- `earnings_conflict`, `earnings_date`, `liquidity_rating`, `liquidity_value`
- `iv_source_call_front`, `iv_source_call_back`, `iv_source_put_front`, `iv_source_put_back`

**New Flags:**
- `--allow-earnings`, `--show-earnings-conflicts`
- `--min-liquidity-rating`, `--skip-liquidity-check`
- `--use-xearn-iv`, `--force-greeks-iv`
- `--structure {atm-call,double,both}`, `--delta-tolerance`

### v1.0 - Initial Release (July 2025)

**Summary:** Forward Factor calendar spread scanner with tastytrade API integration

**Core Features:**
- Forward IV calculation using variance decomposition
- FF ratio: (Front_IV - Fwd_IV) / Fwd_IV
- ATM call calendar scanning (30-60, 30-90, 60-90 DTE pairs)
- dxFeed Greeks streaming for real-time IV
- CSV output with 25 columns
- Configurable FF thresholds (default 0.20)

**Data Sources:**
- tastytrade API for option chains
- dxFeed for Greeks (IV, delta)
- Yahoo Finance for spot prices

## Documentation and Resources

### Local Documentation

- **Official OpenAPI Spec:** `docs/tastytrade_official_API_docs_full_spec.json` (393 KB)
  - Complete REST API specification (OpenAPI 3.0.0)
  - Key endpoints: earnings reports, market metrics, option chains, margin requirements
  - See `docs/RELATED_PROJECTS.md` for endpoint details

- **tastytrade SDK Docs:** `docs/tastytrade-sdk-docs/` - Comprehensive API reference (v10.1.0)
  - `session.md` - Authentication and session management
  - `dxfeed.md` - Market data streaming with Greeks
  - `instruments.md` - Option chains and instrument lookup
  - `metrics.md` - IV rank, liquidity, market metrics
  - `order.md` - Order placement and execution
  - `account.md` - Account data and positions

- **Related Projects:** `docs/RELATED_PROJECTS.md` - Overview of related tastytrade scanners
  - CCR Scanner (`~/tools/ccrScan/`) - Short strangle scanner with earnings filtering
  - TTT Tool (`~/tools/ttt/`) - Account and position analysis CLI
  - Code reuse opportunities for adding features

### Data Sources

- **tastytrade API:** Official SDK (https://github.com/tastyware/tastytrade)
- **dxFeed:** Real-time Greeks streaming (via DXLinkStreamer)
- **NestedOptionChain:** Expiration/strike discovery with streamer symbols
- **Strategy Source:** YouTube video on calendar spreads (see docs/youtube_transcript_*.txt)
