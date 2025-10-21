# Related Projects and Resources

This document catalogs related tastytrade API projects and documentation available on this system.

## Tastytrade Documentation

### Official OpenAPI Documentation

**Location:** `docs/tastytrade-openapi-docs/` and `docs/tastytrade_official_API_docs_full_spec.json`

The official tastytrade API specification (OpenAPI 3.0.0 format) with 80+ REST endpoints.

**Key Endpoints for FF Scanner:**

1. **Earnings Reports** - `/market-metrics/historic-corporate-events/earnings-reports/{symbol}`
   - GET endpoint to fetch historical earnings dates
   - Parameters: symbol, start-date, end-date
   - **Use Case:** Filter out symbols with earnings between today and back expiry

2. **Market Metrics** - `/market-metrics`
   - GET endpoint for IV rank, IV percentile, liquidity data
   - Parameters: symbols (comma-separated)
   - **Use Case:** Add IV rank filtering (only scan when IV rank > threshold)

3. **Option Chains** - `/option-chains/{symbol}/nested`
   - GET endpoint for nested option chain structure
   - Returns expirations with strikes and streamer symbols
   - **Use Case:** Currently used by scanner via NestedOptionChain.get()

4. **Margin Requirements** - `/accounts/{account_number}/margin-requirements/{underlying_symbol}/effective`
   - POST endpoint to calculate buying power reduction for positions
   - **Use Case:** Could validate calendar spread capital requirements

**Full Spec:** `docs/tastytrade_official_API_docs_full_spec.json` (393 KB)
- Complete OpenAPI 3.0 specification
- All request/response schemas
- Parameter definitions and types

### Unofficial SDK Documentation

**Location:** `docs/tastytrade-sdk-docs/`

Comprehensive unofficial SDK documentation (v10.1.0) with 24 markdown files covering:

### Key Documentation Files:
- **session.md** (170 KB) - Authentication, session management
- **dxfeed.md** (210 KB) - Market data streaming with DXLinkStreamer
- **instruments.md** (7.4 KB) - NestedOptionChain, option chains, instrument lookup
- **order.md** (328 KB) - Order placement, execution, management
- **account.md** (410 KB) - Account data, positions, balances
- **metrics.md** (78 KB) - Market metrics (IV rank, liquidity, etc.)
- **market-data.md** (12 KB) - Quote data, market snapshots
- **backtesting.md** (88 KB) - Historical data and backtesting

### Usage:
These docs provide detailed API reference for all tastytrade SDK features. Consult when:
- Adding new data sources (earnings, liquidity filters, IV rank)
- Implementing order execution
- Adding account/position tracking
- Understanding dxFeed Greeks streaming behavior

## Related Options Scanning Projects

### 1. CCR Scanner (`~/tools/ccrScan/`)

**Purpose:** Short strangle scanner using Credit to Capital Ratio (CCR) metric

**Key Features:**
- Real-time buying power reduction (BPR) calculation via API
- Earnings exclusion filtering (customizable window)
- Liquidity filters (volume, open interest, bid/ask spread)
- IV rank and volatility metrics from SDK
- Multi-threaded symbol processing
- Monthly vs weekly expiration filtering
- Delta-based strike selection (default 0.20Δ)

**Notable Files:**
- `ccr.py` (104 KB) - Main scanner implementation
- `ccr_scanner.py` - Enhanced version with strategy presets
- `strangle_finder.py` - Strangle-specific logic
- `hybrid_ccr_scan.py` - Performance-optimized hybrid approach

**Useful Code Patterns:**
```python
# Earnings filtering
earnings_data = session.get_earnings_calendar(symbol)
if earnings_within_window(earnings_data, days=21):
    skip_symbol()

# BPR calculation via API
buying_power_effect = session.calculate_bpr(order_spec)

# IV rank from metrics
metrics = SDKMetrics.get(session, symbol)
iv_rank = metrics.iv_rank
```

### 2. TTT Tool (`~/tools/ttt/`)

**Purpose:** Comprehensive tastytrade account and position analysis CLI

**Key Features:**
- Account balances and margin tracking
- Position analysis with strategy identification
- P/L calculations and POP estimates
- Transaction history and order tracking
- Rich terminal UI with color-coded displays
- Data export and visualization

**Command Examples:**
```bash
ttt accounts      # List accounts
ttt balance       # Show balances
ttt positions     # Current positions with Greeks
ttt transactions  # Transaction history
ttt pnl          # P/L analysis with charts
```

**Useful for:**
- Understanding account data API structure
- Position tracking patterns
- P/L calculation methodologies
- Terminal UI design patterns

### 3. ccr.py Standalone (`~/tools/ccr.py`)

Single-file version of CCR scanner with comprehensive documentation and CLI interface.

## Code Reuse Opportunities for FF Scanner

### Immediate Enhancements:

1. **Earnings Filtering** (from CCR scanner)
   ```python
   # Add to ff_tastytrade_scanner.py
   from tastytrade.instruments import get_earnings_calendar

   def has_earnings_in_window(session, symbol, days=21):
       # Filter out symbols with earnings between today and back expiry
   ```

2. **Liquidity Screens** (from CCR scanner)
   ```python
   # Add volume and OI filters
   def check_liquidity(greeks_data, min_volume=10000, min_oi=1000):
       # Filter based on 20-day avg volume and open interest
   ```

3. **IV Rank/Percentile** (from SDK metrics)
   ```python
   from tastytrade.metrics import get_market_metrics

   def get_iv_rank(session, symbol):
       metrics = get_market_metrics(session, symbol)
       return metrics.iv_rank, metrics.iv_percentile
   ```

4. **Bid/Ask Spread Quality** (from CCR scanner)
   ```python
   def check_spread_quality(bid, ask, max_spread_pct=0.10):
       spread_pct = (ask - bid) / ((bid + ask) / 2)
       return spread_pct <= max_spread_pct
   ```

### Long-term Enhancements:

1. **Position Tracking** (from ttt)
   - Track entered calendar spreads
   - Monitor P/L until front expiry
   - Alert on exit opportunities

2. **Order Execution** (from order.md docs)
   - Auto-execute high FF opportunities
   - Spread order placement with limit prices
   - Fill confirmation and tracking

3. **Backtesting** (from backtesting.md)
   - Historical FF analysis
   - Strategy optimization
   - Performance metrics (Sharpe, CAGR, drawdown)

## Authentication Notes

All projects use similar authentication patterns:

**Environment Variables:**
```bash
TT_USERNAME="your_email@example.com"
TT_PASSWORD="your_password"
TT_ACCOUNT_NUMBER="U0000123456"  # Required for BPR calculations
```

**Or Credentials File:**
```bash
~/.tasty_creds.json:
{
  "username": "your_email@example.com",
  "password": "your_password",
  "account_number": "U0000123456"
}
```

## See Also

- **SOP:** `docs/forward-factor-calendar-spread-SOP.md` - Trading strategy documentation
- **Setup Guide:** `docs/gpt-setup-instructions1.txt` - Quick setup reference
- **SDK Docs:** `docs/tastytrade-sdk-docs/` - Full API reference
