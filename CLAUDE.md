# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Forward Factor (FF) Calendar Spread** trading strategy implementation that scans liquid options to identify mispriced forward volatility opportunities. The core edge is detecting when front-month IV is "hot" (backwardation) relative to forward IV, creating profitable calendar spread setups.

**Core Concept:**
- Compute **Forward IV** between two expirations using variance decomposition
- Calculate **Forward Factor**: `FF = (Front_IV - Fwd_IV) / Fwd_IV`
- Trade calendar spreads when FF exceeds threshold (typically 0.20-0.23)
- Hold until front expiry, then close entire spread

**Version:** 2.0 - Enhanced quality filtering with earnings detection, liquidity screening, X-earn IV support, and double calendar structures

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

2. **Data Pipeline (v2.0):**
   - `fetch_market_metrics()` → batch fetch earnings dates + liquidity ratings for all symbols
   - Earnings/liquidity pre-filtering → skip symbols that don't meet quality thresholds
   - `get_market_data()` → underlying spot price
   - `NestedOptionChain.get()` → expirations & strikes with streamer symbols
   - `extract_xearn_iv()` → try X-earn IV (earnings-removed) from market metrics, fallback to Greeks IV
   - `snapshot_greeks()` → async dxFeed Greeks snapshot for IV + delta
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

6. **Quality Filtering (v2.0):**
   - **Earnings detection:** Skip symbols with earnings between today and back expiry (default: enabled)
   - **Liquidity screening:** Filter symbols by liquidity rating 0-5 (default: ≥3)
   - **X-earn IV support:** Prefer earnings-removed IV when available, graceful fallback to Greeks IV
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

# Force use of Greeks IV instead of X-earn IV
python scripts/ff_tastytrade_scanner.py \
  --tickers QQQ \
  --pairs 60-90 \
  --force-greeks-iv

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
- `--skip-earnings`: Skip positions with earnings conflicts (default: enabled)
- `--allow-earnings`: Allow trading through earnings (disable earnings filtering)
- `--show-earnings-conflicts`: Show filtered positions due to earnings

**Liquidity Screening:**
- `--min-liquidity-rating`: Minimum liquidity rating 0-5 (default: 3)
- `--skip-liquidity-check`: Disable liquidity filtering

**IV Data Source:**
- `--use-xearn-iv`: Try to use X-earn IV from market metrics (default: enabled)
- `--force-greeks-iv`: Force use of Greeks IV instead of X-earn IV

**Output Options:**
- `--csv-out`: Write results to CSV file (recommended, 25-column schema)
- `--json-out`: Write results to JSON file
- `--sandbox`: Use sandbox environment (production required for live Greeks)
- `--show-all-scans`: Show all scan results regardless of FF threshold (for testing)

## v2.0 Features

### Quality Filtering Thresholds

**Earnings Detection:**
- Default: Skip symbols with earnings between today and back expiry
- Threshold: Any earnings date that falls between today and back expiration (inclusive)
- Override: Use `--allow-earnings` to disable filtering
- Debugging: Use `--show-earnings-conflicts` to see filtered opportunities

**Liquidity Screening:**
- Default: Minimum liquidity rating of 3 (scale 0-5)
- Rating 3 ≈ ~10k contracts/day average option volume
- Rating 5 = highest liquidity (SPY, QQQ, AAPL, etc.)
- Override: Use `--skip-liquidity-check` to disable filtering

**Delta Tolerance (Double Calendars):**
- Target: ±35Δ strikes (0.35 call delta, -0.35 put delta)
- Default tolerance: ±5Δ (0.05)
- Range: 0.01 to 0.10 (tighter to looser selection)
- Tighter tolerance (0.03): More precise strikes, may skip symbols
- Looser tolerance (0.10): More opportunities, less precise deltas

### X-earn IV Implementation

**What is X-earn IV:**
- Earnings-removed implied volatility from tastytrade Market Metrics API
- More accurate forward IV when earnings are embedded in option prices
- Automatically tried when available, falls back to Greeks IV if missing

**How It Works:**
1. Scanner first attempts to fetch X-earn IV from `option_expiration_implied_volatilities` field
2. If unavailable or expiration not found, gracefully falls back to dxFeed Greeks IV
3. CSV output includes `iv_source_front` and `iv_source_back` columns to track data source
4. Source values: "xearn" (X-earn IV used) or "greeks" (dxFeed Greeks IV used)

**Override Behavior:**
- Default: `--use-xearn-iv` (try X-earn IV, fallback to Greeks IV)
- `--force-greeks-iv`: Always use Greeks IV, never attempt X-earn IV

### IV Variation Across Strikes: How It Affects FF Calculations

**CRITICAL IMPLEMENTATION DETAIL:** The scanner uses IV from the **actual strikes being traded**, not a generic "term structure IV".

**For ATM Call Calendars:**
- **σ₁ (front IV):** IV from the **ATM strike** at front expiration
  - ATM strike = strike price closest to current spot
  - IV = average of (call IV, put IV) at that strike
- **σ₂ (back IV):** IV from the **ATM strike** at back expiration
- **FF Calculation:** `FF = (σ₁ - σ_fwd) / σ_fwd` where σ_fwd uses ATM IVs

**For Double Calendars (±35Δ):**
- **Call calendar:** Uses IV from the **+35Δ call strike** at both expirations
- **Put calendar:** Uses IV from the **−35Δ put strike** at both expirations
- **Strike selection:** Finds strike with delta closest to ±0.35 (within ±0.05 tolerance)
- **Separate FF calculations:** Call and put calendars have independent FFs

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

### CSV Output Schema (25 Columns)

Results are sorted by `combined_ff` descending (highest opportunities first).

**Columns:**
- `timestamp`: ISO 8601 UTC timestamp (e.g., "2025-10-19T14:30:00Z")
- `symbol`: Ticker symbol
- `structure`: "ATM" or "DOUBLE"
- `spot_price`: Current underlying price
- `front_dte`, `back_dte`: Days to expiration
- `front_expiry`, `back_expiry`: Expiration dates (YYYY-MM-DD)
- `atm_strike`: ATM strike (for ATM structure, null for DOUBLE)
- `call_strike`, `put_strike`: Strikes for double calendar (null for ATM structure)
- `call_delta`, `put_delta`: Delta values for double calendar legs
- `front_iv`, `back_iv`: Front and back IVs (decimal format: 0.25 = 25%)
- `fwd_iv`: Computed forward IV
- `ff`: Forward factor for ATM structure
- `call_ff`, `put_ff`: Forward factors for call and put legs (double calendar)
- `combined_ff`: Average of call_ff and put_ff (used for sorting)
- `earnings_date`: Next earnings date (YYYY-MM-DD, null if none)
- `earnings_conflict`: Boolean indicating earnings conflict
- `liquidity_rating`: Liquidity rating 0-5
- `liquidity_value`: Numeric liquidity metric
- `iv_source_front`, `iv_source_back`: "xearn" or "greeks"

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
- X-earn IV gracefully falls back to Greeks IV if unavailable (see CSV `iv_source` columns)

### Earnings Filtering (v2.0)
- **Now automated:** Scanner fetches earnings dates and filters conflicts by default
- Threshold: Any earnings between today and back expiry (inclusive)
- Override: Use `--allow-earnings` to disable filtering
- Debugging: Use `--show-earnings-conflicts` to see what was filtered

### Liquidity Screening (v2.0)
- **Now automated:** Scanner filters by liquidity rating (0-5 scale)
- Default: Rating ≥3 (≈10k contracts/day avg volume)
- Override: Use `--skip-liquidity-check` to disable filtering
- Rating 5 = highest liquidity (SPY, QQQ, AAPL, etc.)

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
- Bid-ask spread quality checks (tighter filtering beyond liquidity rating)
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
