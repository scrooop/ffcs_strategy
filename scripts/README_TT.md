# FF Scanner v2.1 - Forward Factor Calendar Spread Scanner

**Version**: 2.0
**Last Updated**: October 19, 2025

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
- ✅ **Futures Options Support**: Scan futures symbols like /ES, /GC, /NQ, /CL
- ✅ **CLI Bug Fix**: `--allow-earnings` flag now works correctly

**v2.0 Enhancements:**
- ✅ **Earnings Filtering**: Automatically skip positions with earnings between today and back expiry
- ✅ **Liquidity Screening**: Filter by tastytrade liquidity rating (0-5 scale)
- ✅ **X-earn IV Support**: Use earnings-removed IV when available, fall back to Greeks IV
- ✅ **Double Calendar Scanning**: Find ±35Δ strikes for call and put calendars
- ✅ **Enhanced CSV Output**: 25-column schema with timestamps, deltas, structure types, and IV sources
- ✅ **Flexible Structure Selection**: Scan ATM-only, double-only, or both simultaneously

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
  --skip-earnings \
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
| `--skip-earnings` | flag | **True** | Skip positions with earnings conflicts (default behavior). |
| `--allow-earnings` | flag | `False` | Allow trading through earnings (disables earnings filtering). |
| `--show-earnings-conflicts` | flag | `False` | Show filtered positions due to earnings (diagnostic mode). |

**Mutually Exclusive:** Cannot use both `--skip-earnings` and `--allow-earnings`.

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

### Earnings Filtering

**How It Works:**

The scanner fetches earnings data from tastytrade's Market Metrics API and checks if the expected earnings report date falls between today and the back leg expiration (inclusive). If a conflict is detected, the position is excluded from results.

**Why This Matters:**

Calendar spreads rely on stable forward volatility. Earnings events cause volatility spikes that violate this assumption and can destroy the trade. The original research methodology explicitly required "no earnings between today and back expiry" for this reason.

**Flags:**

- `--skip-earnings` (default): Filter out positions with earnings conflicts
- `--allow-earnings`: Disable earnings filtering (use with `--use-xearn-iv`)
- `--show-earnings-conflicts`: Show filtered positions with reasons (diagnostic)

**Example Output (with `--show-earnings-conflicts`):**

```
[FILTERED] AAPL: Earnings on 2025-11-01 conflicts with back expiry 2025-11-05
[FILTERED] TSLA: Earnings on 2025-10-23 conflicts with back expiry 2025-10-30
```

**Edge Cases:**

- If earnings data is unavailable for a symbol, scanner logs a warning and allows the position through (fail-safe behavior)
- If earnings date is `None` in API response, position is allowed through

**Best Practices:**

- For production scanning: Use `--skip-earnings` (default)
- For earnings strategies: Use `--allow-earnings --use-xearn-iv` to get earnings-adjusted IV

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
4. CSV output includes `iv_source_front` and `iv_source_back` columns to track which source was used

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

The `iv_source_front` and `iv_source_back` columns show which IV source was used:
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

A double calendar spread consists of:
- One **+35Δ call calendar** (sell front 35-delta call, buy back 35-delta call)
- One **-35Δ put calendar** (sell front 35-delta put, buy back 35-delta put)

This structure has **higher win rates** than ATM call calendars according to the original research.

**How It Works:**

1. Scanner fetches Greeks for a ±25% strike range around spot price
2. For each expiration, finds strikes closest to:
   - Call: +0.35 delta (±5Δ tolerance by default)
   - Put: -0.35 delta (±5Δ tolerance by default)
3. Calculates Forward Factor for both call and put calendars independently
4. Outputs separate rows for `double-call` and `double-put` structures

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
- `combined_ff = call_ff` (for `double-call` structure)
- `combined_ff = put_ff` (for `double-put` structure)

For ATM calendars:
- `combined_ff = ff` (single FF value)

The `combined_ff` column is used for sorting all results (highest first).

**Structure Types in CSV:**

- `atm-call`: ATM call calendar (same strike, sell front call / buy back call)
- `double-call`: +35Δ call calendar (sell front 35Δ call / buy back 35Δ call)
- `double-put`: -35Δ put calendar (sell front 35Δ put / buy back 35Δ put)

**Example Output:**

```csv
timestamp,symbol,structure,spot_price,front_dte,back_dte,...,call_strike,put_strike,call_delta,put_delta,call_ff,put_ff,combined_ff
2025-10-19T14:30:00Z,SPY,double-call,580.50,30,60,...,595.00,,0.3498,,0.2547,,0.2547
2025-10-19T14:30:00Z,SPY,double-put,580.50,30,60,...,,565.00,,-0.3512,,0.2398,0.2398
2025-10-19T14:30:00Z,SPY,atm-call,580.50,30,60,...,580.00,,,,,0.2312,0.2312
```

**When Delta Strikes Are Unavailable:**

If scanner cannot find a strike within tolerance:
- Call calendar: Skipped (no row output)
- Put calendar: Skipped (no row output)
- ATM calendar: Still scanned (if `--structure both` or `--structure atm-call`)

**Performance Note:**

Double calendar scanning requires fetching Greeks for more strikes (8-12 strikes vs 2 for ATM), which adds ~2-3 seconds per symbol. Total scan time for 10 symbols is typically 25-30 seconds with `--structure both`.

---

## CSV Output Schema

### 25-Column Schema (v2.0)

The scanner outputs a unified CSV schema that supports both ATM and double calendar structures. Empty columns are left blank (not "N/A" or "null").

| Column | Type | Description | ATM Calendar | Double Calendar |
|--------|------|-------------|--------------|-----------------|
| `timestamp` | ISO 8601 | UTC timestamp when scan was run | ✅ | ✅ |
| `symbol` | string | Ticker symbol (e.g., "SPY") | ✅ | ✅ |
| `structure` | enum | `atm-call`, `double-call`, or `double-put` | ✅ | ✅ |
| `spot_price` | float | Underlying last price | ✅ | ✅ |
| `front_dte` | int | Front leg days to expiration | ✅ | ✅ |
| `back_dte` | int | Back leg days to expiration | ✅ | ✅ |
| `front_expiry` | date | Front leg expiration date (ISO 8601) | ✅ | ✅ |
| `back_expiry` | date | Back leg expiration date (ISO 8601) | ✅ | ✅ |
| `atm_strike` | float | ATM strike price | ✅ | *(empty)* |
| `call_strike` | float | Call strike for double calendar | *(empty)* | ✅ (call only) |
| `put_strike` | float | Put strike for double calendar | *(empty)* | ✅ (put only) |
| `call_delta` | float | Call delta for double calendar | *(empty)* | ✅ (call only) |
| `put_delta` | float | Put delta for double calendar | *(empty)* | ✅ (put only) |
| `front_iv` | float | Front leg implied volatility (decimal) | ✅ | ✅ |
| `back_iv` | float | Back leg implied volatility (decimal) | ✅ | ✅ |
| `fwd_iv` | float | Forward IV (computed) | ✅ | ✅ |
| `ff` | float | Forward Factor for ATM calendar | ✅ | *(empty)* |
| `call_ff` | float | Forward Factor for call calendar | *(empty)* | ✅ (call only) |
| `put_ff` | float | Forward Factor for put calendar | *(empty)* | ✅ (put only) |
| `combined_ff` | float | FF used for sorting (same as `ff` for ATM, `call_ff` or `put_ff` for double) | ✅ | ✅ |
| `earnings_date` | date | Expected earnings report date (ISO 8601, empty if none) | ✅ | ✅ |
| `earnings_conflict` | enum | `no` if no conflict, empty if earnings_date is empty | ✅ | ✅ |
| `liquidity_rating` | int | tastytrade liquidity rating (0-5 scale) | ✅ | ✅ |
| `liquidity_value` | float | *(reserved for future use, currently empty)* | *(empty)* | *(empty)* |
| `iv_source_front` | enum | `xearn` or `greeks` | ✅ | ✅ |
| `iv_source_back` | enum | `xearn` or `greeks` | ✅ | ✅ |

### Example CSV Output

**ATM Call Calendar:**

```csv
timestamp,symbol,structure,spot_price,front_dte,back_dte,front_expiry,back_expiry,atm_strike,call_strike,put_strike,call_delta,put_delta,front_iv,back_iv,fwd_iv,ff,call_ff,put_ff,combined_ff,earnings_date,earnings_conflict,liquidity_rating,liquidity_value,iv_source_front,iv_source_back
2025-10-19T14:30:00Z,SPY,atm-call,580.50,30,60,2025-11-18,2025-12-18,580.00,,,,,0.185432,0.172145,0.158967,0.166234,,,0.166234,,no,5,,greeks,greeks
```

**Double Call Calendar:**

```csv
timestamp,symbol,structure,spot_price,front_dte,back_dte,front_expiry,back_expiry,atm_strike,call_strike,put_strike,call_delta,put_delta,front_iv,back_iv,fwd_iv,ff,call_ff,put_ff,combined_ff,earnings_date,earnings_conflict,liquidity_rating,liquidity_value,iv_source_front,iv_source_back
2025-10-19T14:30:00Z,SPY,double-call,580.50,30,60,2025-11-18,2025-12-18,,595.00,,0.3498,,0.192456,0.175234,0.163512,,0.177123,,0.177123,,no,5,,greeks,greeks
```

**Double Put Calendar:**

```csv
timestamp,symbol,structure,spot_price,front_dte,back_dte,front_expiry,back_expiry,atm_strike,call_strike,put_strike,call_delta,put_delta,front_iv,back_iv,fwd_iv,ff,call_ff,put_ff,combined_ff,earnings_date,earnings_conflict,liquidity_rating,liquidity_value,iv_source_front,iv_source_back
2025-10-19T14:30:00Z,SPY,double-put,580.50,30,60,2025-11-18,2025-12-18,,,565.00,,-0.3512,0.188234,0.173456,0.161234,,,0.167523,0.167523,,no,5,,greeks,greeks
```

### Sorting

Results are sorted by:
1. `combined_ff` descending (highest Forward Factor first)
2. `symbol` ascending (alphabetical for ties)

### Null Handling

Structure-specific columns are left **empty** (not "N/A" or "null") when not applicable:
- ATM calendars: `call_strike`, `put_strike`, `call_delta`, `put_delta`, `call_ff`, `put_ff` are empty
- Double call calendars: `atm_strike`, `put_strike`, `put_delta`, `ff`, `put_ff` are empty
- Double put calendars: `atm_strike`, `call_strike`, `call_delta`, `ff`, `call_ff` are empty

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

- ATM calendars: `call_strike`, `put_strike`, `call_delta`, `put_delta`, `call_ff`, `put_ff` are empty
- Double calendars: `atm_strike`, `ff` are empty

This is **correct** - the schema is unified for all structures. Use `structure` column to identify which columns are relevant.

#### 10. "ERROR: --skip-earnings and --allow-earnings are mutually exclusive"

**Cause:** Both flags were specified (conflicting instructions).

**Solution:** Use only one:

```bash
# Correct: Skip earnings (default)
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --skip-earnings

# Correct: Allow earnings
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --allow-earnings

# WRONG: Both flags (error)
python scripts/ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --skip-earnings --allow-earnings
```

---

## Advanced Examples

### Example 1: Production Daily Scan with Timestamped Output

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL TSLA NVDA META AMZN GOOGL MSFT AMD \
  --pairs 30-60 30-90 60-90 \
  --min-ff 0.23 \
  --skip-earnings \
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

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers /ES /GC /NQ \
  --pairs 30-60 \
  --min-ff 0.20 \
  --csv-out futures_scan.csv
```

**Output:**

```csv
timestamp,symbol,structure,spot_price,front_dte,back_dte,...
2025-10-19T19:41:07Z,/ES,double-call,65.00,33,61,...
2025-10-19T19:41:07Z,/ES,atm-call,65.00,33,61,...
```

**Use Case:** Scan liquid futures for calendar spread opportunities. Futures don't have earnings, so earnings filtering is automatically bypassed.

**Mixed Equities and Futures:**

```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY /ES QQQ /NQ AAPL \
  --pairs 30-60 \
  --min-ff 0.20 \
  --csv-out mixed_scan.csv
```

**Note:** Spot prices for futures are inferred from option chain strikes (API limitation).

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

- **v2.0** (October 2025): Earnings filtering, liquidity screening, X-earn IV support, double calendar scanning, enhanced CSV output
- **v1.0** (Initial release): ATM calendar scanning with Forward Factor calculation

---

## Support & Feedback

For issues or questions:
1. Check [Troubleshooting](#troubleshooting) section
2. Review scanner code comments: `scripts/ff_tastytrade_scanner.py`
3. Consult tastytrade SDK docs: `docs/tastytrade-sdk-docs/`

**Disclaimer:** This scanner is for educational purposes. Trading involves risk. Past performance does not guarantee future results.
