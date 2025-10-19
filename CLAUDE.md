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
```

## Core Architecture

### ff_tastytrade_scanner.py

**Purpose:** CLI scanner that fetches ATM implied volatilities from tastytrade's dxFeed streamer, computes forward IV and FF ratios, and reports tradable opportunities.

**Key Components:**

1. **Authentication:**
   - Requires `TT_USERNAME` and `TT_PASSWORD` environment variables
   - Production environment required for live Greeks data (sandbox has limited market data)

2. **Data Pipeline:**
   - `get_market_data()` → underlying spot price
   - `NestedOptionChain.get()` → expirations & strikes with streamer symbols
   - `snapshot_greeks()` → async dxFeed Greeks snapshot for ATM IV
   - Greeks.volatility = Black-Scholes IV per contract (average ATM call & put)

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
   - Uses `pick_atm_strike()` to find strike nearest to spot

5. **Greeks Streaming:**
   - `snapshot_greeks()` subscribes to dxFeed Greeks via DXLinkStreamer
   - Collects single snapshot with timeout (default 3s)
   - Handles partial results if some legs fail to arrive

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
# Scan SPY and QQQ for multiple DTE pairs (using general threshold)
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 30-90 60-90 \
  --min-ff 0.20 \
  --csv-out ff_scan.csv

# Use optimized threshold for 30-60 DTE (~20 trades/month)
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL TSLA NVDA META AMZN \
  --pairs 30-60 \
  --min-ff 0.23 \
  --dte-tolerance 7

# Lower threshold to see more opportunities (returns start positive around 0.10-0.20)
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 60-90 \
  --min-ff 0.15
```

### Command Line Flags

- `--tickers`: Space or comma-separated symbols (required)
- `--pairs`: DTE pairs like `30-60 30-90` (front-back, required)
- `--min-ff`: Minimum FF ratio to include (default 0.20)
- `--dte-tolerance`: Max deviation from target DTE (default 5 days)
- `--timeout`: Streamer snapshot timeout in seconds (default 3s)
- `--sandbox`: Use sandbox environment (production required for live Greeks)
- `--csv-out`: Write results to CSV file
- `--json-out`: Write results to JSON file

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

### Earnings Considerations
- Scanner does NOT currently filter for earnings
- SOP requires: no earnings between today and back expiry, OR use ex-earnings IV
- Future enhancement: add earnings date filtering via tastytrade API

### Liquidity Filters
- SOP recommends: 20-day avg option volume > 10k contracts/day
- Scanner does NOT currently enforce liquidity filters
- Future enhancement: add volume/OI checks

## Strategy Theory (from SOP)

### Why This Works
Short-dated options often get bid up (volatility backwardation) while the next window is underpriced. Calendar spreads isolate and buy that forward volatility slice at a discount.

### Forward Factor Formula
```
FF = (σ₁ - σ_fwd) / σ_fwd
```
Where:
- σ₁ = annualized IV for front expiry
- σ_fwd = forward IV between T₁ and T₂
- FF > 0 → front IV "hot" vs forward IV → go long forward vol (calendar)

This is the correct formula as defined in the video transcript and implemented in the scanner.

### Trade Structures
1. **ATM Call Calendar** (simpler, cheaper)
   - Same strike, sell front call / buy back call
2. **Double-Calendar** (higher win rate, more complex)
   - +35Δ call calendar AND -35Δ put calendar (±5Δ acceptable)

## Future Enhancements

Scanner could be extended with:
- Earnings date filtering (exclude or flag positions spanning earnings)
- Liquidity screens (avg option volume, open interest thresholds)
- Bid-ask spread quality checks
- Position tracking and P&L monitoring
- Auto-execution via tastytrade order API
- Backtest framework using historical IV data

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
