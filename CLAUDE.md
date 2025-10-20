# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Forward Factor (FF) Calendar Spread** trading strategy implementation that scans liquid options to identify mispriced forward volatility opportunities. The core edge is detecting when front-month IV is "hot" (backwardation) relative to forward IV, creating profitable calendar spread setups.

**Core Concept:**
- Compute **Forward IV** between two expirations using variance decomposition
- Calculate **Forward Factor**: `FF = (Front_IV - Fwd_IV) / Fwd_IV`
- Trade calendar spreads when FF exceeds threshold (typically 0.20-0.23)
- Hold until front expiry, then close entire spread

**Version:** 2.2 - Greeks IV priority inversion (strike-level precision) + fast earnings check with caching for 80-95% runtime reduction + enhanced quality filtering with earnings detection, volume screening, and double calendar structures

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
```

## Core Architecture

### ff_tastytrade_scanner.py

**Purpose:** CLI scanner that fetches implied volatilities from tastytrade's dxFeed streamer, computes forward IV and FF ratios, and reports tradable opportunities for both ATM and double calendar spreads.

**Key Components:**

1. **Authentication:**
   - Requires `TT_USERNAME` and `TT_PASSWORD` environment variables
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
   - ATM: Uses `pick_atm_strike()` to find strike nearest to spot
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

**Volume Filtering:**
- `--min-avg-volume`: Minimum average options volume (default: 10000 contracts/day)
- `--skip-liquidity-check`: Disable volume filtering

**Output Options:**
- `--csv-out`: Write results to CSV file (recommended, 31-column schema)
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
- `earnings_source` column (31st column) tracks data provenance
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
  - ATM strike = strike price closest to current spot
  - IV = average of (call IV, put IV) at that strike
- **σ₂ (back IV):** IV from the **ATM strike** at back expiration
- **FF Calculation:** `FF = (σ₁ - σ_fwd) / σ_fwd` where σ_fwd uses ATM IVs

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
- `pick_atm_strike()`: Selects strike closest to spot, returns its Greeks symbols
- `pick_delta_strike()`: Selects strike closest to target delta, returns IV from that strike
- `snapshot_greeks()`: Fetches actual IV from dxFeed for each specific strike
- Forward IV calculation uses these strike-specific IVs, not interpolated surface values

### CSV Output Schema (31 Columns)

Results are sorted by `combined_ff` descending (highest opportunities first).

**IMPORTANT:** Double calendars REQUIRE BOTH call and put legs. If only one leg meets delta tolerance, the symbol is skipped for double calendar structure (but may still appear in ATM structure if `--structure both`).

**Key Design Principle:**
- ALL IVs are stored in call-specific and put-specific columns (no generic IV columns)
- For ATM calendars: Call and put IVs are from the SAME strike (may differ slightly due to skew)
- For double calendars: Call and put IVs are from DIFFERENT strikes (+35Δ vs -35Δ)
- This design provides maximum transparency and consistency across structures

**Common Columns (All Structures):**
- `timestamp`: ISO 8601 UTC timestamp (e.g., "2025-10-19T14:30:00+00:00")
- `symbol`: Ticker symbol
- `structure`: "atm-call" or "double"
- `call_ff`: Forward factor for call leg
- `put_ff`: Forward factor for put leg
- `combined_ff`: Average of call_ff and put_ff (primary sorting metric)
- `spot_price`: Current underlying price
- `front_dte`, `back_dte`: Days to expiration
- `front_expiry`, `back_expiry`: Expiration dates (YYYY-MM-DD)
- `call_front_iv`, `call_back_iv`, `call_fwd_iv`: Call leg IVs (decimal: 0.25 = 25%)
- `put_front_iv`, `put_back_iv`, `put_fwd_iv`: Put leg IVs (decimal: 0.25 = 25%)
- `earnings_conflict`: "yes" or "no"
- `earnings_date`: Next earnings date (YYYY-MM-DD, empty if none)
- `avg_options_volume`: Average options volume (from liquidity_value field)
- `iv_source_call_front`, `iv_source_call_back`: Call IV sources ("xearn" or "greeks")
- `iv_source_put_front`, `iv_source_put_back`: Put IV sources ("xearn" or "greeks")
- `earnings_source`: Earnings data source ("cache", "yahoo", "tastytrade", "none", or "skipped")

**ATM Calendar Specific (structure="atm-call"):**
- `atm_strike`: Strike closest to spot (same strike used for call and put)
- `call_front_iv`, `put_front_iv`: IVs from call and put at ATM strike (may differ)
- `call_ff`, `put_ff`: Separate FFs for call and put (usually very similar)
- Empty: `call_strike`, `put_strike`, `call_delta`, `put_delta`

**Double Calendar Specific (structure="double"):**
- `call_strike`, `put_strike`: +35Δ call strike and -35Δ put strike (different strikes)
- `call_delta`, `put_delta`: Actual deltas of selected strikes
- `call_front_iv`, `put_front_iv`: IVs from different strikes (skew creates differences)
- `call_ff`, `put_ff`: Separate FFs for each leg (may vary significantly due to skew)
- Empty: `atm_strike`

**Complete Column Order:**
`timestamp`, `symbol`, `structure`, `call_ff`, `put_ff`, `combined_ff`, `spot_price`, `front_dte`, `back_dte`, `front_expiry`, `back_expiry`, `atm_strike`, `call_strike`, `put_strike`, `call_delta`, `put_delta`, `call_front_iv`, `call_back_iv`, `call_fwd_iv`, `put_front_iv`, `put_back_iv`, `put_fwd_iv`, `earnings_conflict`, `earnings_date`, `avg_options_volume`, `iv_source_call_front`, `iv_source_call_back`, `iv_source_put_front`, `iv_source_put_back`, `earnings_source`

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

### Volume Filtering (v2.2)
- **Transparent volume-based filter:** Uses avg options volume from Market Metrics API
- Default: ≥10,000 contracts/day (liquidity_value field as proxy)
- Override: Use `--skip-liquidity-check` to disable filtering
- Adjustable: Use `--min-avg-volume` to set custom threshold
- Futures handling: Symbols without volume data are allowed through (not an error)

### Double Calendar Strike Selection (v2.0)
- Target: ±35Δ strikes with configurable tolerance
- If no strikes within tolerance, symbol is skipped for double calendar structure
- ATM structure still scanned if `--structure both` (default)
- Adjust `--delta-tolerance` if too many symbols are skipped

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
