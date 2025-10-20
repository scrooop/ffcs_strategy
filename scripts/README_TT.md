# FF Scanner v2.1 - Forward Factor Calendar Spread Scanner

**Version**: 2.1
**Last Updated**: October 20, 2025

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Quick Start](#quick-start)
4. [Basic Usage](#basic-usage)
5. [Command Line Flags](#command-line-flags)
6. [Feature Details](#feature-details)
7. [CSV Output Schema](#csv-output-schema)
8. [Thresholds & Strategy Guidelines](#thresholds--strategy-guidelines)
9. [Troubleshooting](#troubleshooting)
10. [Advanced Examples](#advanced-examples)

---

## Overview

The FF Scanner is a production-ready CLI tool that scans liquid options to identify mispriced forward volatility opportunities for calendar spread trading. It uses the **tastytrade API** (official Python SDK) and **dxFeed Greeks streamer** to compute Forward IV and Forward Factor ratios.

**What it does:**
- Fetches ATM and ±35Δ implied volatilities from dxFeed Greeks
- Computes Forward IV using variance decomposition: `FwdIV = sqrt((T2*IV2² - T1*IV1²)/(T2 - T1))`
- Calculates Forward Factor: `FF = (Front_IV - Fwd_IV) / Fwd_IV`
- Filters for earnings conflicts, liquidity, and delta targets
- Outputs both ATM call calendars and double calendars (±35Δ)
- Supports X-earn IV (earnings-removed implied volatility) with graceful fallback to Greeks IV

**v2.1 Enhancements:**
- ✅ **Fast Earnings Check**: 80-95% runtime reduction with SQLite cache (1000 symbols: 8min → <30s)
- ✅ **Multi-Source Earnings Pipeline**: Cache → Yahoo Finance → TastyTrade with graceful degradation
- ✅ **Futures Options Support**: Scan futures symbols like /ES, /GC, /NQ, /CL
- ✅ **CLI Bug Fix**: `--allow-earnings` flag now works correctly

**v2.0 Enhancements:**
- ✅ **Earnings Filtering**: Automatically skip positions with earnings between today and back expiry
- ✅ **Liquidity Screening**: Filter by tastytrade liquidity rating (0-5 scale)
- ✅ **X-earn IV Support**: Use earnings-removed IV when available, fall back to Greeks IV (works for both ATM and double calendars)
- ✅ **Double Calendar Scanning**: Find ±35Δ strikes for call and put calendars (requires BOTH legs)
- ✅ **Enhanced CSV Output**: 30-column schema with call/put-specific IVs, timestamps, deltas, and IV sources
- ✅ **Flexible Structure Selection**: Scan ATM-only, double-only, or both simultaneously

---

## Performance Improvements (v2.1)

The scanner now uses a **fast earnings pre-filter with caching** to eliminate 80-95% of scan runtime during heavy earnings weeks.

**Key Features:**
- **Yahoo Finance as primary source**: Fast earnings date lookup (~100ms vs 500ms TastyTrade)
- **SQLite persistent cache**: Instant lookups for previously scanned symbols (<10ms per symbol)
- **Pipeline reordering**: Filter symbols BEFORE expensive TastyTrade API calls
- **Graceful degradation**: Cache → Yahoo → TastyTrade → None (skip symbol)

**Performance Impact:**

| Scenario | Old Time (v2.0) | New Time (v2.1) | Improvement |
|----------|-----------------|-----------------|-------------|
| 1000 symbols (heavy earnings week) | ~8 minutes | <30 seconds | 94% faster |
| 112 symbols (cold cache) | ~90 seconds | ~10 seconds | 89% faster |
| Same-day rescan (warm cache) | ~90 seconds | <1 second | 99% faster |

**Cache Location**: `.cache/earnings.db` in project root
- Safe to delete manually: `rm .cache/earnings.db` (rebuilds automatically)
- See `.cache/README.md` for cache management details

**CSV Tracking**: The `earnings_source` column (31st column) tracks data provenance:
- `cache`: Retrieved from SQLite cache (instant)
- `yahoo`: Fetched from Yahoo Finance (~100ms)
- `tastytrade`: Fetched from TastyTrade API (~500ms)
- `none`: No earnings data available
- `skipped`: Symbol skipped by earnings filter

---

## Installation

### Prerequisites

- Python 3.12+ (tested with 3.12.3)
- tastytrade production account (sandbox has limited market data)

### Step 1: Create Virtual Environment

**IMPORTANT:** Always use a virtual environment to isolate dependencies.

```bash
# Navigate to project directory
cd /path/to/ffcs_strategy

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows
```

**You must activate the venv every time you open a new terminal:**
```bash
source venv/bin/activate  # Run this in each new terminal session
```

### Step 2: Install SDK

**With venv activated**, install the tastytrade SDK:

```bash
python -m pip install --upgrade tastytrade
```

### Step 3: Set Environment Variables

Add to your `~/.zshrc` or `~/.bashrc`:

```bash
export TT_USERNAME="your_username"
export TT_PASSWORD="your_password"
```

Then reload your shell:

```bash
source ~/.zshrc  # or source ~/.bashrc
```

### Step 4: Verify Installation

**With venv activated**, verify the scanner works:

```bash
python scripts/ff_tastytrade_scanner.py --help
```

**If you see `ModuleNotFoundError: No module named 'tastytrade'`:**
- You forgot to activate the venv (run `source venv/bin/activate`)
- Or you installed tastytrade outside the venv (reinstall with venv active)

---

## Quick Start

**Daily pre-market scan (recommended for production):**

```bash
# Activate venv first (if not already active)
source venv/bin/activate

# Run daily scan
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL TSLA NVDA META AMZN GOOGL MSFT AMD \
  --pairs 30-60 30-90 60-90 \
  --min-ff 0.23 \
  --min-liquidity-rating 3 \
  --structure both \
  --csv-out "$(date +%y%m%d_%H%M)_ff_scan.csv"
```

**Expected output:** 3-5 high-quality opportunities sorted by Forward Factor (highest first).

---

## Basic Usage

### Example 1: Simple ATM Calendar Scan

Scan SPY and QQQ for ATM call calendars with 30-60 DTE:

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 \
  --min-ff 0.23 \
  --structure atm-call
```

### Example 2: Double Calendar Scan (60-90 DTE)

Focus on ±35Δ double calendars for longer-dated expirations:

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ IWM \
  --pairs 60-90 \
  --min-ff 0.20 \
  --structure double \
  --csv-out double_calendars.csv
```

### Example 3: Scan Both ATM and Double Calendars

Get all tradable structures (most comprehensive):

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL \
  --pairs 30-60 60-90 \
  --structure both \
  --min-ff 0.20 \
  --csv-out scan.csv
```

### Example 4: Allow Trading Through Earnings

Disable earnings filtering (use X-earn IV for earnings-adjusted FF calculations):

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers AAPL \
  --pairs 30-90 \
  --allow-earnings \
  --use-xearn-iv
```

### Example 5: Debug Why Symbol Was Filtered

See which positions were excluded due to earnings conflicts:

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers AAPL TSLA \
  --pairs 30-60 \
  --show-earnings-conflicts \
  --skip-liquidity-check
```

---

## Command Line Flags

### Core Scanner Parameters

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--tickers` | list | **required** | List of ticker symbols (space or comma-separated). Example: `SPY QQQ AAPL` |
| `--pairs` | list | **required** | DTE pairs as `front-back`. Example: `30-60 30-90 60-90` |
| `--min-ff` | float | `0.20` | Minimum Forward Factor threshold. Use `0.23` for ~20 trades/month. |
| `--dte-tolerance` | int | `5` | Max deviation from target DTE in days. |
| `--timeout` | float | `3.0` | Greeks streaming timeout in seconds. |

### Structure Selection

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--structure` | choice | `both` | Calendar structure to scan: `atm-call`, `double`, or `both`. |
| `--delta-tolerance` | float | `0.05` | Max delta deviation for ±35Δ strikes (range: 0.01-0.10). |

**Structure Options:**
- `atm-call`: ATM call calendars only (simplest, cheapest)
- `double`: Double calendars only (±35Δ call + put calendars, higher win rate)
- `both`: Scan both structures simultaneously (recommended)

### Earnings Filtering

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--allow-earnings` | flag | `False` | Allow trading through earnings (disables earnings filtering). Default behavior is to skip positions with earnings conflicts. |
| `--show-earnings-conflicts` | flag | `False` | Show filtered positions due to earnings (diagnostic mode). |

**Default Behavior**: Earnings filtering is **enabled by default**. Symbols with earnings between today and back expiration are automatically skipped.

### Liquidity Screening

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--min-liquidity-rating` | int | `3` | Minimum liquidity rating (0-5 scale). See [Liquidity Rating System](#liquidity-rating-system). |
| `--skip-liquidity-check` | flag | `False` | Disable liquidity filtering (not recommended). |

**Recommended Thresholds:**
- `3`: Standard (≈10k+ contracts/day avg volume)
- `4`: High liquidity (≈50k+ contracts/day)
- `5`: Extremely liquid (≈100k+ contracts/day)

### X-earn IV Support

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--use-xearn-iv` | flag | **True** | Try to use X-earn IV (earnings-removed implied volatility) from Market Metrics API. Falls back to Greeks IV if unavailable. |
| `--force-greeks-iv` | flag | `False` | Force use of Greeks IV instead of X-earn IV (for testing/comparison). |

**Mutually Exclusive:** Cannot use both `--use-xearn-iv` and `--force-greeks-iv`.

### Output Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--csv-out` | string | *(none)* | Write results to CSV file. **Recommended for production.** |
| `--json-out` | string | *(none)* | Write results to JSON file. |
| `--sandbox` | flag | `False` | Use sandbox environment (limited market data, not recommended). |

### Debug/Analysis Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--show-all-scans` | flag | `False` | Show all scan results regardless of FF threshold (for data pipeline testing). |

---

## Feature Details

### Earnings Filtering (Fast Pre-Filter v2.1)

**How It Works:**

The scanner uses a **multi-source earnings pipeline with persistent caching** to check if earnings fall between **today and the back leg expiration (inclusive)**. If a conflict is detected, the position is excluded from results.

**Data Sources (Priority Order):**
1. **SQLite Cache** (`.cache/earnings.db`): Instant lookup (<10ms per symbol)
2. **Yahoo Finance**: Fast primary source (~100ms per symbol, 5s timeout)
3. **TastyTrade API**: Fallback source (~500ms per symbol)
4. **Graceful degradation**: If all sources fail, symbol is allowed through with warning

**Cache Behavior:**
- **Location**: `.cache/earnings.db` (SQLite database in project root)
- **Invalidation**: Automatic when cached earnings date has passed
- **Persistence**: Survives restarts, shared across all scans
- **Rebuilds**: Automatically rebuilds if deleted or corrupted

**Earnings Filter Period:** Today through back expiration date (inclusive). Example: If today is Oct 19 and back expiry is Nov 21, any earnings date from Oct 19 to Nov 21 triggers a conflict.

**Why This Matters:**

Calendar spreads rely on stable forward volatility. Earnings events cause volatility spikes that violate this assumption and can destroy the trade. The original research methodology explicitly required "no earnings between today and back expiry" for this reason.

**Flags:**

- **Default behavior**: Earnings filtering is enabled (no flag needed)
- `--allow-earnings`: Disable earnings filtering (use with `--use-xearn-iv` for earnings strategies)
- `--show-earnings-conflicts`: Show filtered positions with reasons (diagnostic mode)

**Example Output (with `--show-earnings-conflicts`):**

```
[FILTERED] AAPL: Earnings on 2025-11-01 conflicts with back expiry 2025-11-05 (source: cache)
[FILTERED] TSLA: Earnings on 2025-10-23 conflicts with back expiry 2025-10-30 (source: yahoo)
```

**Edge Cases:**

- If earnings data is unavailable for a symbol, scanner logs a warning and allows the position through (fail-safe behavior)
- If earnings date is `None` in API response, position is allowed through
- Cache automatically refreshes when cached earnings dates pass

**Best Practices:**

- For production scanning: Use default behavior (earnings filtering enabled)
- For earnings strategies: Use `--allow-earnings --use-xearn-iv` to get earnings-adjusted IV
- For cache issues: Delete cache (`rm .cache/earnings.db`) and let it rebuild

---

### Liquidity Screening

**How It Works:**

The scanner fetches tastytrade's proprietary `liquidity_rating` (0-5 scale) from Market Metrics API and filters out symbols below the specified threshold.

**Liquidity Rating System:**

| Rating | Description | Approx. 20-Day Avg Option Volume |
|--------|-------------|----------------------------------|
| 0-1 | Very illiquid | < 1,000 contracts/day |
| 2 | Low liquidity | 1,000 - 5,000 contracts/day |
| **3** | **Standard** (default) | **10,000+ contracts/day** |
| 4 | High liquidity | 50,000+ contracts/day |
| 5 | Extremely liquid | 100,000+ contracts/day |

**Why This Matters:**

The original research required "20-day average option volume above 10,000 contracts per day" to ensure executable pricing. Trading illiquid options leads to:
- Wide bid-ask spreads (slippage)
- Difficulty closing positions
- Potential for adverse selection

**Flags:**

- `--min-liquidity-rating 3`: Default threshold (≈10k+ contracts/day)
- `--skip-liquidity-check`: Disable liquidity filtering (not recommended)

**Example:**

```bash
# Standard liquidity (≈10k+ contracts/day)
python scripts/ff_tastytrade_scanner.py --tickers SPY QQQ AAPL --min-liquidity-rating 3

# High liquidity only (≈50k+ contracts/day)
python scripts/ff_tastytrade_scanner.py --tickers SPY QQQ --min-liquidity-rating 4

# Allow lower liquidity (≈1k+ contracts/day)
python scripts/ff_tastytrade_scanner.py --tickers SPY QQQ AAPL TSLA --min-liquidity-rating 2
```

**Edge Cases:**

- If liquidity rating is unavailable, scanner logs a warning and allows position through
- Rating is symbol-level, not expiration-specific (assumes all expirations have similar liquidity)

---

### X-earn IV Support

**What is X-earn IV?**

X-earn IV (earnings-removed implied volatility) is tastytrade's proprietary calculation that removes the expected earnings volatility component from standard implied volatility. This provides a cleaner measure of "normal" volatility for Forward Factor calculations.

**How It Works:**

1. Scanner attempts to fetch `option_expiration_implied_volatilities` from Market Metrics API
2. If X-earn IV is available for both front and back expirations, it is used
3. If unavailable (or flag disabled), scanner falls back to Greeks IV from dxFeed
4. CSV output includes `iv_source_call_front`, `iv_source_call_back`, `iv_source_put_front`, `iv_source_put_back` columns to track which source was used for each leg

**Graceful Fallback:**

The scanner is designed to work with partial data:
- Front expiration: X-earn IV → uses X-earn IV
- Back expiration: X-earn IV unavailable → uses Greeks IV for back leg only
- Both unavailable → uses Greeks IV for both legs (v1.0 behavior)

**Flags:**

- `--use-xearn-iv` (default): Try X-earn IV first, fall back to Greeks IV
- `--force-greeks-iv`: Always use Greeks IV (for comparison/testing)

**Example:**

```bash
# Use X-earn IV when available (default)
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --use-xearn-iv

# Force Greeks IV (disable X-earn IV)
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --force-greeks-iv
```

**CSV Output Tracking:**

The `iv_source_call_front`, `iv_source_call_back`, `iv_source_put_front`, `iv_source_put_back` columns show which IV source was used for each leg:
- `xearn`: X-earn IV from Market Metrics API
- `greeks`: Black-Scholes IV from dxFeed Greeks

**Console Logs:**

When X-earn IV is unavailable, scanner logs informational messages:

```
[INFO] SPY 30DTE: X-earn IV unavailable, using Greeks IV
[INFO] QQQ 60DTE: X-earn IV unavailable, using Greeks IV
```

**When to Use Each:**

- **X-earn IV (default)**: Best for standard scanning, especially around earnings cycles
- **Greeks IV**: Use when comparing to v1.0 results or when X-earn IV has data quality issues

---

### Double Calendar Structures

**What are Double Calendars?**

A double calendar spread consists of TWO simultaneous calendar spreads:
- One **+35Δ call calendar** (sell front 35-delta call, buy back 35-delta call)
- One **-35Δ put calendar** (sell front 35-delta put, buy back 35-delta put)

This structure has **higher win rates** than ATM call calendars according to the original research.

**CRITICAL: Both Legs Required**

The scanner **requires BOTH call and put legs** to output a double calendar. If only one leg meets delta tolerance, the symbol is skipped for double calendar structure (but may still appear as ATM calendar if `--structure both`).

**How It Works:**

1. Scanner fetches Greeks for a ±25% strike range around spot price
2. For each expiration, finds strikes closest to:
   - Call: +0.35 delta (±5Δ tolerance by default)
   - Put: -0.35 delta (±5Δ tolerance by default)
3. **Verifies BOTH legs exist** - if not, skips this symbol for double calendar
4. Calculates Forward Factor for both call and put calendars independently
5. Outputs **ONE row** per double calendar with both strikes and both FFs populated

**Delta Tolerance:**

By default, scanner allows ±5Δ deviation from target (0.30-0.40 delta for calls, -0.40 to -0.30 for puts). You can adjust this:

```bash
# Stricter delta targeting (±3Δ)
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 60-90 --structure double --delta-tolerance 0.03

# Wider tolerance (±8Δ)
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 60-90 --structure double --delta-tolerance 0.08
```

**Combined FF Calculation:**

For double calendars:
- `call_ff` = Forward Factor for call leg (from +35Δ strike IVs)
- `put_ff` = Forward Factor for put leg (from -35Δ strike IVs)
- `combined_ff` = (call_ff + put_ff) / 2 (average of both legs)

For ATM calendars:
- `call_ff` = Forward Factor from call at ATM strike
- `put_ff` = Forward Factor from put at ATM strike
- `combined_ff` = (call_ff + put_ff) / 2 (average of both legs)

The `combined_ff` column is used for sorting all results (highest first).

**Structure Types in CSV:**

- `atm-call`: ATM call calendar (same strike for call and put, IVs from ATM strike)
- `double`: Double calendar (BOTH +35Δ call and -35Δ put calendars, different strikes)

**Example Output:**

```csv
timestamp,symbol,structure,call_ff,put_ff,combined_ff,spot_price,front_dte,back_dte,...,call_strike,put_strike,call_delta,put_delta
2025-10-19T14:30:00+00:00,SPY,double,0.2547,0.2398,0.2473,580.50,30,60,...,595.00,565.00,0.3498,-0.3512
2025-10-19T14:30:00+00:00,SPY,atm-call,0.2312,0.2311,0.2312,580.50,30,60,...,,,,,
```

Note: The double calendar is **ONE row** with both `call_strike` and `put_strike` populated.

**When Delta Strikes Are Unavailable:**

If scanner cannot find strikes within tolerance for BOTH call and put:
- Double calendar: Skipped entirely (no row output)
- ATM calendar: Still scanned (if `--structure both` or `--structure atm-call`)

**Performance Note:**

Double calendar scanning requires fetching Greeks for more strikes (8-12 strikes vs 2 for ATM), which adds ~2-3 seconds per symbol. Total scan time for 10 symbols is typically 25-30 seconds with `--structure both`.

---

### IV Variation Across Strikes: Understanding FF Differences

**CRITICAL CONCEPT:** The scanner uses IV from the **actual strikes being traded**, not a generic "term structure IV". This means ATM calendars and double calendars will show **different FF values** for the same underlying, even though both trade the same term structure edge.

**Which IVs Are Used:**

| Structure | Front IV (σ₁) | Back IV (σ₂) |
|-----------|--------------|--------------|
| **ATM Call Calendar** | IV from ATM strike at front expiration (average of call + put IV) | IV from ATM strike at back expiration (average of call + put IV) |
| **+35Δ Call Calendar** | IV from +35Δ call strike at front expiration | IV from +35Δ call strike at back expiration |
| **−35Δ Put Calendar** | IV from −35Δ put strike at front expiration | IV from −35Δ put strike at back expiration |

**Why IV Varies Across Strikes (Volatility Skew):**

Implied volatility is **not constant** across the option chain. In equity markets, you typically see:
- **OTM puts:** Higher IV than ATM (downside protection premium)
- **OTM calls:** Lower IV than ATM
- **Typical magnitude:** 5-10 percentage points difference

**Real-World Example (SPY):**

Assume SPY is at $580 with these IV levels:
- **ATM (580 strike, 50Δ):** 20% IV
- **+35Δ call (595 strike):** 18% IV (10% lower than ATM)
- **−35Δ put (565 strike):** 25% IV (25% higher than ATM)

For a 30-60 DTE calendar spread, the scanner will report **three different FF values**:
1. **ATM calendar:** FF = 0.23 (based on 20% IV)
2. **+35Δ call calendar:** FF = 0.21 (based on 18% IV, ~9% lower FF)
3. **−35Δ put calendar:** FF = 0.29 (based on 25% IV, ~26% higher FF)

**Why This Matters:**

1. **Double calendars "tap into skew"** - You're trading both term structure mispricing AND strike-level mispricing
2. **Put calendars typically rank higher** - Higher IV at OTM put strikes leads to higher FF values
3. **This is by design** - You're trading the actual strikes, so the scanner uses those strikes' IVs
4. **Apples-to-apples comparison** - Compare ATM calendars to ATM calendars, double calendars to double calendars

**Practical Implications:**

- If scanning with `--structure both`, you'll see the same ticker appear **three times** in results with different FFs
- The **−35Δ put calendar will often rank highest** due to equity volatility skew
- This doesn't mean it's a "better" trade - it's a **different** trade with different strikes and different skew exposure
- Use `combined_ff` for sorting, but understand that higher FF on a put calendar reflects **both term structure AND skew**

**How the Scanner Implements This:**

1. **`pick_atm_strike()`**: Finds strike closest to spot price
2. **`pick_delta_strike()`**: Finds strike closest to target delta (±35Δ)
3. **`snapshot_greeks()`**: Fetches actual IV from dxFeed for each specific strike
4. **`forward_iv()`**: Uses those strike-specific IVs (not interpolated surface values)
5. **FF calculation**: `FF = (strike_IV_front - fwd_IV) / fwd_IV`

**Key Takeaway:** When you see "front IV" and "back IV" in the documentation or CSV output, these refer to the IV **from the specific strikes being traded** (ATM for ATM calendars, ±35Δ for double calendars), not a generic market-wide implied volatility index.

---

## CSV Output Schema

### 31-Column Schema (v2.1)

The scanner outputs a unified CSV schema that supports both ATM and double calendar structures. Empty columns are left blank (not "N/A" or "null").

**Key Design Principle:**
- ALL IVs are stored in call-specific and put-specific columns
- For ATM calendars: Call and put IVs are from the SAME strike (may differ slightly)
- For double calendars: Call and put IVs are from DIFFERENT strikes (+35Δ vs -35Δ)
- This design provides maximum transparency and consistency across structures

| Column | Type | Description | ATM Calendar | Double Calendar |
|--------|------|-------------|--------------|-----------------|
| `timestamp` | ISO 8601 | UTC timestamp when scan was run (RFC 3339: "+00:00" suffix) | ✅ | ✅ |
| `symbol` | string | Ticker symbol (e.g., "SPY") | ✅ | ✅ |
| `structure` | enum | `atm-call` or `double` | ✅ | ✅ |
| `call_ff` | float | Forward Factor for call leg | ✅ | ✅ |
| `put_ff` | float | Forward Factor for put leg | ✅ | ✅ |
| `combined_ff` | float | Average of call_ff and put_ff (primary sorting metric) | ✅ | ✅ |
| `spot_price` | float | Underlying last price | ✅ | ✅ |
| `front_dte` | int | Front leg days to expiration | ✅ | ✅ |
| `back_dte` | int | Back leg days to expiration | ✅ | ✅ |
| `front_expiry` | date | Front leg expiration date (YYYY-MM-DD) | ✅ | ✅ |
| `back_expiry` | date | Back leg expiration date (YYYY-MM-DD) | ✅ | ✅ |
| `atm_strike` | float | ATM strike price (same for call and put) | ✅ | *(empty)* |
| `call_strike` | float | +35Δ call strike for double calendar | *(empty)* | ✅ |
| `put_strike` | float | -35Δ put strike for double calendar | *(empty)* | ✅ |
| `call_delta` | float | Actual delta of call strike | *(empty)* | ✅ |
| `put_delta` | float | Actual delta of put strike | *(empty)* | ✅ |
| `call_front_iv` | float | Call IV at front expiration (decimal: 0.25 = 25%) | ✅ | ✅ |
| `call_back_iv` | float | Call IV at back expiration | ✅ | ✅ |
| `call_fwd_iv` | float | Forward IV for call leg (computed) | ✅ | ✅ |
| `put_front_iv` | float | Put IV at front expiration | ✅ | ✅ |
| `put_back_iv` | float | Put IV at back expiration | ✅ | ✅ |
| `put_fwd_iv` | float | Forward IV for put leg (computed) | ✅ | ✅ |
| `earnings_conflict` | enum | `yes` or `no` | ✅ | ✅ |
| `earnings_date` | date | Expected earnings report date (YYYY-MM-DD, empty if none) | ✅ | ✅ |
| `liquidity_rating` | int | tastytrade liquidity rating (0-5 scale) | ✅ | ✅ |
| `liquidity_value` | float | *(reserved for future use, currently empty)* | *(empty)* | *(empty)* |
| `iv_source_call_front` | enum | Call IV source for front expiration: `xearn` or `greeks` | ✅ | ✅ |
| `iv_source_call_back` | enum | Call IV source for back expiration: `xearn` or `greeks` | ✅ | ✅ |
| `iv_source_put_front` | enum | Put IV source for front expiration: `xearn` or `greeks` | ✅ | ✅ |
| `iv_source_put_back` | enum | Put IV source for back expiration: `xearn` or `greeks` | ✅ | ✅ |
| `earnings_source` | enum | Earnings data source: `cache`, `yahoo`, `tastytrade`, `none`, or `skipped` | ✅ | ✅ |

### Example CSV Output

**ATM Call Calendar:**

```csv
timestamp,symbol,structure,call_ff,put_ff,combined_ff,spot_price,front_dte,back_dte,front_expiry,back_expiry,atm_strike,call_strike,put_strike,call_delta,put_delta,call_front_iv,call_back_iv,call_fwd_iv,put_front_iv,put_back_iv,put_fwd_iv,earnings_conflict,earnings_date,liquidity_rating,liquidity_value,iv_source_call_front,iv_source_call_back,iv_source_put_front,iv_source_put_back,earnings_source
2025-10-19T14:30:00+00:00,SPY,atm-call,0.166234,0.165890,0.166062,580.50,30,60,2025-11-18,2025-12-18,580.00,,,,,0.185432,0.172145,0.158967,0.185001,0.171890,0.158745,no,,5,,xearn,xearn,xearn,xearn,cache
```

**Double Calendar:**

```csv
timestamp,symbol,structure,call_ff,put_ff,combined_ff,spot_price,front_dte,back_dte,front_expiry,back_expiry,atm_strike,call_strike,put_strike,call_delta,put_delta,call_front_iv,call_back_iv,call_fwd_iv,put_front_iv,put_back_iv,put_fwd_iv,earnings_conflict,earnings_date,liquidity_rating,liquidity_value,iv_source_call_front,iv_source_call_back,iv_source_put_front,iv_source_put_back,earnings_source
2025-10-19T14:30:00+00:00,SPY,double,0.177123,0.167523,0.172323,580.50,30,60,2025-11-18,2025-12-18,,595.00,565.00,0.3498,-0.3512,0.192456,0.175234,0.163512,0.188234,0.173456,0.161234,no,,5,,greeks,greeks,greeks,greeks,yahoo
```

**Key Differences:**
- **ATM Calendar:** `atm_strike` populated, `call_strike` and `put_strike` empty, call/put IVs from SAME strike
- **Double Calendar:** `call_strike` and `put_strike` populated, `atm_strike` empty, call/put IVs from DIFFERENT strikes
- **X-earn IV:** ATM calendar shows `xearn` for all IV sources (when available)
- **Greeks IV:** Double calendar shows `greeks` (X-earn IV works for double calendars too, this example just shows Greeks)
- **Earnings Source (v2.1):** ATM calendar shows `cache` (instant lookup), double calendar shows `yahoo` (fresh fetch)

### Sorting

Results are sorted by:
1. `combined_ff` descending (highest Forward Factor first)
2. `symbol` ascending (alphabetical for ties)

### Null Handling

Structure-specific columns are left **empty** (not "N/A" or "null") when not applicable:
- **ATM calendars:** `call_strike`, `put_strike`, `call_delta`, `put_delta` are empty
- **Double calendars:** `atm_strike` is empty

Note: All other columns are populated for both structures. The key difference is which strike columns are used.

---

## Thresholds & Strategy Guidelines

### Forward Factor Thresholds

**General Rule of Thumb (from original research):**

> "If your forward factor reads at **0.20 or higher**, we can go long the calendar or double calendar."

**When Returns Start Becoming Positive:**

> "Visibly, we can see from the graph that a factor at or above around **0.1 to 0.2** is when returns start becoming positive."

**Optimized Thresholds for ~20 Trades/Month:**

| Structure | DTE Pair | Recommended FF Threshold |
|-----------|----------|--------------------------|
| ATM Call Calendar | 30-60 | ≥ 0.23 |
| ATM Call Calendar | 30-90 | ≥ 0.23 |
| ATM Call Calendar | 60-90 | ≥ 0.20 |
| Double Calendar | 30-60 | ≥ 0.23 |
| Double Calendar | 30-90 | ≥ 0.23 |
| Double Calendar | 60-90 | ≥ 0.20 |

**Usage:**

```bash
# Conservative (higher quality, fewer trades)
python scripts/ff_tastytrade_scanner.py --tickers SPY QQQ --pairs 30-60 --min-ff 0.23

# Moderate (balanced quality/quantity)
python scripts/ff_tastytrade_scanner.py --tickers SPY QQQ --pairs 60-90 --min-ff 0.20

# Aggressive (more opportunities, lower win rate)
python scripts/ff_tastytrade_scanner.py --tickers SPY QQQ --pairs 30-60 60-90 --min-ff 0.15
```

### Liquidity Thresholds

**Recommended:**
- `--min-liquidity-rating 3`: Standard (≈10k+ contracts/day) - **Use for production**
- `--min-liquidity-rating 4`: High liquidity (≈50k+ contracts/day) - **Use for large position sizes**

**Not Recommended:**
- `--min-liquidity-rating 2`: Low liquidity (≈1-5k contracts/day) - Risk of wide spreads
- `--skip-liquidity-check`: No filtering - Risk of illiquid options

### Position Sizing Guidelines

From the original strategy SOP:

- **Default**: 2-8% of equity per trade (4% typical)
- **Alternative**: Fractional Kelly (~¼-Kelly)
- **Priority**: Allocate to highest FF names first until risk caps met

### Trade Management

- **Entry**: Long calendar spread (sell front, buy back) as single spread order
- **Hold**: No adjustments, hold until front expiry day
- **Exit**: Close entire spread just before front expiry (avoid pin risk)
- **No legging**: Close as spread unless necessary for fills

---

## Troubleshooting

### Cache Issues (v2.1)

#### Cache Performance Issues

**Problem:** Scanner is slow even with cache enabled
**Symptoms:** Scan takes longer than expected, low cache hit rate in console output

**Solutions:**
1. **Check cache hit rate** in console output during scan
2. **Verify cache exists:** `ls -lh .cache/earnings.db`
3. **Clear corrupted cache:**
   ```bash
   rm .cache/earnings.db  # Scanner will rebuild automatically on next run
   ```
4. **Check cache statistics:**
   ```bash
   sqlite3 .cache/earnings.db "SELECT COUNT(*) FROM earnings;"
   sqlite3 .cache/earnings.db "SELECT data_source, COUNT(*) FROM earnings GROUP BY data_source;"
   ```

**Expected Performance:**
- First scan (cold cache): ~10s for 112 symbols
- Subsequent scans (warm cache): <1s for 112 symbols
- Cache hit rate: Should be >90% for daily scanning

#### Stale Earnings Dates

**Problem:** Earnings dates in cache seem outdated
**Symptoms:** Past earnings dates still showing in CSV output

**Solutions:**
- **Automatic refresh:** Cache auto-refreshes when dates pass (no action needed)
- **Manual refresh:**
  ```bash
  rm .cache/earnings.db  # Force re-fetch all earnings from fresh sources
  ```

**How It Works:**
- Scanner checks if cached earnings date < today → re-fetches automatically
- No TTL expiration - cache persists until dates pass

#### Database Locked Errors

**Problem:** `SQLite database locked` error during scan
**Cause:** Multiple scanner instances accessing cache simultaneously

**Solutions:**
1. **Wait for other processes to finish**
2. **Kill other scanner instances:**
   ```bash
   ps aux | grep ff_tastytrade_scanner
   kill <PID>  # Replace <PID> with process ID
   ```
3. **Delete lock file** (if processes already terminated):
   ```bash
   rm .cache/earnings.db-wal .cache/earnings.db-shm  # SQLite WAL files
   ```

#### Cache Directory Missing

**Problem:** `.cache` directory doesn't exist
**Cause:** First run or directory was deleted

**Solution:**
- Scanner creates directory automatically on first run
- If permissions issue, manually create:
  ```bash
  mkdir -p .cache
  chmod 755 .cache
  ```

---

### Common Issues

#### 1. "No quote for [SYMBOL], skipping"

**Cause:** Symbol not found or has no live market data.

**Solutions:**
- Verify symbol is correct (use uppercase: `SPY` not `spy`)
- Ensure you're using production environment (not `--sandbox`)
- Check if market is open (Greeks data is limited outside market hours)

#### 2. "No option chain for [SYMBOL], skipping"

**Cause:** Symbol has no listed options or API returned empty chain.

**Solutions:**
- Verify symbol has weekly/monthly options (use tastytrade platform to check)
- Try again during market hours
- Check if symbol is an equity (not index or futures)

#### 3. "No expirations matched tolerance for [SYMBOL]"

**Cause:** No expirations within `--dte-tolerance` of target DTEs.

**Solutions:**
- Increase `--dte-tolerance` (try `--dte-tolerance 7` or `10`)
- Adjust target DTEs to match actual option expiration cycle
- Check if symbol has weekly options (monthly-only symbols may not have 30 DTE)

**Example:**

```bash
# Increase tolerance to ±7 days
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --dte-tolerance 7
```

#### 4. "Market metrics unavailable, skipping earnings check"

**Cause:** Market Metrics API failed to return data for symbol.

**Solutions:**
- This is a warning, not an error - scan continues
- Scanner allows position through (fail-safe behavior)
- If persistent, check tastytrade API status

#### 5. "X-earn IV unavailable, using Greeks IV"

**Cause:** Market Metrics API doesn't have X-earn IV for this expiration.

**Solutions:**
- This is informational, not an error - scan continues
- Scanner automatically falls back to Greeks IV (v1.0 behavior)
- If you prefer to force Greeks IV always: Use `--force-greeks-iv`

#### 6. Scanner returns 0 results

**Possible Causes:**

1. **All symbols filtered by earnings**
   - **Solution:** Run with `--show-earnings-conflicts` to see what was filtered
   - **Solution:** If intentional, use `--allow-earnings` to disable filter

2. **All symbols filtered by liquidity**
   - **Solution:** Lower `--min-liquidity-rating` (try `2` instead of `3`)
   - **Solution:** Use `--skip-liquidity-check` for testing

3. **FF threshold too high**
   - **Solution:** Lower `--min-ff` (try `0.15` or `0.10`)
   - **Solution:** Use `--show-all-scans` to see all calculations

4. **No strikes within delta tolerance (double calendars)**
   - **Solution:** Increase `--delta-tolerance` (try `0.08` or `0.10`)
   - **Solution:** Switch to `--structure atm-call` temporarily

**Diagnostic Command:**

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL \
  --pairs 30-60 \
  --min-ff 0.10 \
  --show-earnings-conflicts \
  --skip-liquidity-check \
  --show-all-scans
```

#### 7. "ERROR: Set TT_USERNAME and TT_PASSWORD env vars"

**Cause:** Environment variables not set.

**Solutions:**

```bash
# Temporary (current session only)
export TT_USERNAME="your_username"
export TT_PASSWORD="your_password"

# Permanent (add to ~/.zshrc or ~/.bashrc)
echo 'export TT_USERNAME="your_username"' >> ~/.zshrc
echo 'export TT_PASSWORD="your_password"' >> ~/.zshrc
source ~/.zshrc
```

#### 8. Scanner takes too long (>60 seconds for 10 symbols)

**Possible Causes:**

1. **Network latency to dxFeed servers**
   - **Solution:** Increase `--timeout` (try `5.0` instead of `3.0`)
   - **Note:** This is for Greeks timeout per symbol, not total scan time

2. **Too many DTE pairs**
   - **Solution:** Reduce to 1-2 pairs instead of 3
   - **Example:** `--pairs 30-60 60-90` instead of `--pairs 30-60 30-90 60-90 90-120`

3. **Double calendar mode fetching many strikes**
   - **Solution:** Use `--structure atm-call` for faster scans
   - **Note:** Double calendars require 4-6x more Greeks subscriptions

**Expected Performance:**

- 10 symbols, 2 DTE pairs, ATM-only: ~15-20 seconds
- 10 symbols, 2 DTE pairs, both structures: ~25-35 seconds
- 20 symbols, 3 DTE pairs, both structures: ~50-70 seconds

#### 9. CSV output has empty columns

**Cause:** Structure-specific columns are intentionally empty (not errors).

**Expected Behavior:**

- ATM calendars: `call_strike`, `put_strike`, `call_delta`, `put_delta` are empty
- Double calendars: `atm_strike` is empty

This is **correct** - the schema is unified for all structures. All IV and FF columns are populated for both structures. Use `structure` column to identify which strike columns are relevant.

#### 10. Earnings Filtering Behavior

**Default Behavior:** Earnings filtering is **enabled by default** (no flag needed).

**To disable earnings filtering:**
```bash
# Allow trading through earnings
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --allow-earnings
```

**To debug earnings filtering:**
```bash
# Show which symbols were filtered due to earnings
python scripts/ff_tastytrade_scanner.py --tickers SPY QQQ AAPL --pairs 30-60 --show-earnings-conflicts
```

---

## Advanced Examples

### Example 1: Production Daily Scan with Timestamped Output

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL TSLA NVDA META AMZN GOOGL MSFT AMD \
  --pairs 30-60 30-90 60-90 \
  --min-ff 0.23 \
  --min-liquidity-rating 3 \
  --structure both \
  --csv-out "$(date +%y%m%d_%H%M)_ff_scan.csv"
```

**Output:** File like `251019_0945_ff_scan.csv` with timestamped opportunities.

### Example 2: Compare X-earn IV vs Greeks IV

Run two scans and compare results:

```bash
# Scan 1: X-earn IV (default)
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 \
  --use-xearn-iv \
  --csv-out xearn_scan.csv

# Scan 2: Greeks IV (forced)
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 \
  --force-greeks-iv \
  --csv-out greeks_scan.csv

# Compare results in spreadsheet or with diff tool
diff xearn_scan.csv greeks_scan.csv
```

### Example 3: Aggressive Scan for Research

Lower all thresholds to capture more data:

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ IWM AAPL TSLA NVDA META AMZN GOOGL MSFT AMD \
  --pairs 30-60 60-90 \
  --min-ff 0.10 \
  --min-liquidity-rating 2 \
  --structure both \
  --allow-earnings \
  --csv-out aggressive_scan.csv
```

**Use Case:** Collect larger dataset for backtesting or strategy analysis.

### Example 4: Focus on High-Liquidity Mega-Caps

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 60-90 \
  --min-ff 0.20 \
  --min-liquidity-rating 5 \
  --structure both \
  --csv-out megacap_scan.csv
```

**Use Case:** Large position sizes requiring extremely liquid underlyings.

### Example 5: Intraday Re-scan for Volatility Spikes

```bash
# Morning scan (9:45 AM)
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL TSLA NVDA \
  --pairs 30-60 \
  --min-ff 0.23 \
  --structure both \
  --csv-out morning_scan.csv

# Afternoon re-scan (2:30 PM)
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL TSLA NVDA \
  --pairs 30-60 \
  --min-ff 0.23 \
  --structure both \
  --csv-out afternoon_scan.csv

# Compare to find new opportunities
diff morning_scan.csv afternoon_scan.csv
```

**Use Case:** Detect intraday volatility changes that create new calendar opportunities.

### Example 6: Weekly Options Focus (Tight DTE Pairs)

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 7-14 14-21 \
  --min-ff 0.25 \
  --dte-tolerance 2 \
  --structure both \
  --csv-out weekly_scan.csv
```

**Use Case:** Trade weekly expirations for faster theta decay (requires higher FF threshold).

### Example 7: Multi-Month Hold Period

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ IWM \
  --pairs 60-120 90-120 \
  --min-ff 0.18 \
  --structure both \
  --csv-out longterm_scan.csv
```

**Use Case:** Longer-dated calendars for lower volatility environments (can use lower FF threshold).

### Example 8: Scan Futures Options (v2.1)

**Supported Futures (8 verified working):**
- **Equity Indexes:** `/ES`, `/NQ`, `/RTY`, `/MES`, `/MNQ` ✅
- **Commodities:** `/GC` (Gold), `/CL` (Crude Oil), `/MCL` (Micro Crude) ✅

**Partially Supported (chains exist but non-standard expirations):**
- `/NG`, `/LE`, `/6A`, `/6B`, `/6C`, `/6E`, `/6J`, `/BTC`, `/ETH` - May work with different DTE pairs

**Note:** Many futures only have monthly/quarterly options, which don't match standard 30-60 DTE pairs. Other futures like /SI, /ZB, /ZN, /ZF, /ZT, /ZC, /ZS, /ZW, /HG, /HE, /SR3 have no option chains on tastytrade.

```bash
# Scan major equity index futures
python scripts/ff_tastytrade_scanner.py \
  --tickers /ES /NQ /RTY \
  --pairs 30-60 \
  --min-ff 0.20 \
  --csv-out futures_scan.csv

# Scan all supported futures (recommended)
python scripts/ff_tastytrade_scanner.py \
  --tickers /ES /NQ /RTY /GC /CL /MES /MNQ /MCL \
  --pairs 30-60 30-90 60-90 \
  --min-ff 0.20 \
  --csv-out all_futures_scan.csv
```

**Output:**

```csv
timestamp,symbol,structure,call_ff,put_ff,combined_ff,spot_price,front_dte,back_dte,atm_strike,...
2025-10-19T20:23:05+00:00,/ES,atm-call,0.2134,0.2129,0.2132,6702.50,30,61,6700.00,...
2025-10-19T20:23:05+00:00,/NQ,atm-call,0.2543,0.2538,0.2541,24986.50,33,61,25000.00,...
2025-10-19T20:23:05+00:00,/GC,atm-call,0.1987,0.1982,0.1985,4213.30,30,65,4215.00,...
2025-10-19T20:23:05+00:00,/CL,atm-call,0.2456,0.2451,0.2454,57.54,29,58,57.50,...
```

**Use Case:** Scan liquid futures for calendar spread opportunities. Futures don't have earnings, so earnings filtering is automatically bypassed.

**Mixed Equities and Futures:**

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY /ES QQQ /NQ IWM /RTY AAPL \
  --pairs 30-60 \
  --min-ff 0.20 \
  --csv-out mixed_scan.csv
```

**Requirements:**
- `pip install yfinance` (spot prices fetched from Yahoo Finance)
- Futures options trading approval on tastytrade account
- Note: Liquidity filtering applies to futures (use `--skip-liquidity-check` if needed)

---

### Example 9: Debug Symbol with Suspected Earnings Conflict

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers AAPL \
  --pairs 30-60 30-90 \
  --show-earnings-conflicts \
  --skip-liquidity-check \
  --show-all-scans
```

**Output:**

```
[FILTERED] AAPL: Earnings on 2025-11-01 conflicts with back expiry 2025-11-05
```

**Use Case:** Understand why specific symbol isn't appearing in production scan.

---

## Notes

### Production vs Sandbox

- **Production environment required** for live Greeks and market data
- Sandbox returns minimal/no live data for most symbols
- Use `--sandbox` only for API testing, not for real scanning

### Greeks Data Handling

- If only one leg (call or put) IV arrives, scanner uses that single value
- If both legs fail to arrive within timeout, that target DTE is skipped
- `Greeks.volatility` is Black-Scholes IV (annualized, decimal format: 0.25 = 25%)
- `Greeks.delta` is decimal format (0.35 = 35 delta)

### Rate Limiting

Scanner adds a 500ms delay between symbols to avoid rate limiting. This is handled automatically.

### Time Zone

All dates and timestamps use **America/New_York** (broker convention) for consistency with tastytrade platform.

### Market Hours

Best results during regular market hours (9:30 AM - 4:00 PM ET) when Greeks data is actively updated. Outside market hours, data may be stale or unavailable.

---

## Uninstallation

```bash
python -m pip uninstall tastytrade
```

---

## Version History

- **v2.1** (October 2025): Fast earnings check with caching (80-95% runtime reduction), multi-source earnings pipeline (Cache → Yahoo → TastyTrade), 31-column CSV schema with earnings_source tracking, CLI cleanup
- **v2.0** (October 2025): Earnings filtering, liquidity screening, X-earn IV support, double calendar scanning, enhanced CSV output (28 columns)
- **v1.0** (Initial release): ATM calendar scanning with Forward Factor calculation

---

## Support & Feedback

For issues or questions:
1. Check [Troubleshooting](#troubleshooting) section
2. Review scanner code comments: `scripts/ff_tastytrade_scanner.py`
3. Consult tastytrade SDK docs: `docs/tastytrade-sdk-docs/`

**Disclaimer:** This scanner is for educational purposes. Trading involves risk. Past performance does not guarantee future results.
