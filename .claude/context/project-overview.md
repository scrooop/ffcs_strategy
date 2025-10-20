---
created: 2025-10-20T18:58:52Z
last_updated: 2025-10-20T18:58:52Z
version: 1.0
author: Claude Code PM System
---

# Project Overview

## Summary

FFCS Strategy is a Python CLI scanner that identifies profitable calendar spread opportunities by analyzing forward volatility mispricing in options markets. It calculates a "Forward Factor" (FF) ratio to detect when front-month IV is elevated relative to forward IV, creating calendar spread edges.

**Current Version:** 2.2 (Core calculation corrections)
**Next Version:** 2.3 (CSV consolidation + logging, 20% complete)

## Core Features

### 1. Forward Factor Calculation
**Status:** ✅ Production-ready (v2.2)

**Description:**
Calculates forward implied volatility between two expirations using variance decomposition, then computes Forward Factor as:
```
FF = (σ_front - σ_fwd) / σ_fwd
```

**Supported Structures:**
- **ATM Call Calendar:** Single calendar at 50Δ strike
  - Strike selection: Delta closest to 0.50 (absolute)
  - IV: Averaged call and put IV at 50Δ strike
  - Output: Single `atm_ff` ratio

- **Double Calendar:** Two calendars at ±35Δ strikes
  - Call calendar: +35Δ strike (call delta ~0.35)
  - Put calendar: -35Δ strike (put delta ~-0.35)
  - Output: Separate `call_ff`, `put_ff`, `min_ff`, `combined_ff`

**DTE Pairs Supported:**
- 30-60 (common, ~20 trades/month at FF ≥ 0.23)
- 30-90 (longer hold, ~20 trades/month at FF ≥ 0.23)
- 60-90 (alternative, ~20 trades/month at FF ≥ 0.20)
- Custom pairs (configurable via --pairs flag)

**Key Improvements (v2.2):**
- ATM strike now uses 50Δ delta anchor (theory-aligned)
- ATM FF simplified to single value (was dual call/put)
- Double calendar uses `min_ff` for filtering (conservative)

### 2. Fast Earnings Cache System
**Status:** ✅ Production-ready (v2.1)

**Description:**
Multi-source earnings pipeline with SQLite caching for 80-95% runtime reduction during heavy earnings weeks.

**Features:**
- **Multi-source pipeline:** Cache → Yahoo Finance → TastyTrade → Graceful degradation
- **Automatic invalidation:** Cache expires when earnings date passes
- **High hit rate:** >90% for daily scanning workflows
- **Performance:**
  - Cold cache: ~10s for 112 symbols
  - Warm cache: <1s for 112 symbols
  - Large scans: 1000 symbols ~8 min → <30s

**Data Sources (Priority Order):**
1. SQLite cache (`.cache/earnings.db`) - <10ms per symbol
2. Yahoo Finance - ~100ms per symbol (primary source)
3. TastyTrade API - ~500ms per symbol (fallback)
4. Graceful degradation - Allow through with warning if all fail

**Tracking:**
- `earnings_source` CSV column: cache/yahoo/tastytrade/none/skipped
- `earnings_date` CSV column: Next earnings date (YYYY-MM-DD)
- `earnings_conflict` CSV column: yes/no

### 3. Quality Filtering System
**Status:** ✅ Production-ready (v2.2)

**Description:**
Multi-stage filtering to ensure tradeable opportunities:

**Earnings Filtering:**
- Default: Enabled (skip symbols with earnings between today and back expiry)
- Rationale: Avoid gamma risk from earnings volatility crush
- Override: `--allow-earnings` flag
- Debugging: `--show-earnings-conflicts` to see filtered symbols

**Liquidity Filtering (Hybrid System):**
- **Default Mode (24/7):** Uses `liquidity_rating >= 3` from Market Metrics API
  - Rating scale: 0-5 (3 ≈ 10k volume equivalent)
  - Works pre-market and after-hours
  - Suitable for most scanning workflows

- **Precise Mode (Market Hours):** Uses `--options-volume [THRESHOLD]` flag
  - Fetches dxFeed `Underlying.optionVolume` (today's total chain volume)
  - Default threshold: 10,000 contracts if no value specified
  - Custom threshold: e.g., `--options-volume 20000`
  - Requires market hours for accurate data

- **Override:** `--skip-liquidity-check` disables all filtering

**Strike Availability:**
- Validates strikes exist at target deltas (50Δ ATM, ±35Δ double)
- Configurable `--delta-tolerance` (default ±0.05, range 0.01-0.10)
- Skips symbols with no strikes within tolerance

**Skip Tracking:**
- `skip_reason` CSV column tracks why symbols filtered
- Values: earnings_conflict, volume_too_low, no_strikes, delta_not_found, etc.

### 4. Greeks IV with Ex-earn Fallback
**Status:** ✅ Production-ready (v2.2)

**Description:**
Dual IV sourcing strategy for maximum coverage and accuracy:

**Primary Source: Greeks IV (dxFeed)**
- Strike-specific IV from real-time Greeks streaming
- Preserves volatility smile/skew (critical for double calendars)
- Used for >95% of strikes
- Timeout: 3s default (configurable via --timeout flag)

**Fallback Source: Ex-earn IV (Market Metrics)**
- Earnings-removed IV from TastyTrade Market Metrics API
- Expiration-level only (single value per expiration)
- Used when Greeks IV missing/timeout (<5% of cases)
- Less accurate for wings (collapses skew)

**Tracking:**
- ATM structure: `atm_iv_source_front`, `atm_iv_source_back`
- Double structure: `iv_source_call_front`, `iv_source_call_back`, `iv_source_put_front`, `iv_source_put_back`
- Values: "greeks" (primary) or "exearn_fallback" (rare)

### 5. Multi-Structure Support
**Status:** ✅ Production-ready (v2.0)

**Description:**
Scan for both ATM and double calendar opportunities in single pass:

**Structure Selection (--structure flag):**
- `atm-call`: ATM call calendars only (simpler, cheaper, 50Δ)
- `double`: Double calendars only (higher win rate, ±35Δ)
- `both` (default): Scan both structures (recommended)

**Output:**
- Separate CSV rows per structure per symbol per DTE pair
- ATM rows: `atm_ff`, `atm_strike`, `atm_delta` populated
- Double rows: `call_ff`, `put_ff`, `min_ff`, `combined_ff` populated
- Sorting: ATM by `atm_ff`, double by `min_ff` (descending)

**Double Calendar Requirements:**
- BOTH call and put legs must be within delta tolerance
- If only one leg available, symbol skipped for double structure
- May still appear in ATM structure if `--structure both`

### 6. Futures Options Support
**Status:** ✅ Production-ready (v2.1)

**Description:**
Scan futures options (/ES, /NQ, /CL, /GC) in addition to equities:

**Supported Futures:**
- ✅ /ES (E-mini S&P 500)
- ✅ /NQ (E-mini Nasdaq-100)
- ✅ /RTY (E-mini Russell 2000)
- ✅ /GC (Gold)
- ✅ /CL (Crude Oil)
- ✅ /MES, /MNQ, /MCL (Micro contracts)

**Implementation:**
- Futures symbols: Leading slash (e.g., `/ES` not `ES`)
- Spot prices: Yahoo Finance (TastyTrade API doesn't provide)
- Option chains: TastyTrade `NestedFutureOptionChain`
- Earnings filter: Automatically bypassed (futures don't have earnings)

**Limitations:**
- Some futures lack option chains on TastyTrade
- Non-standard expiration cycles (not weekly like equities)

### 7. CSV/JSON Output
**Status:** ✅ Production-ready (v2.2)

**CSV Output:**
- **Schema:** 40 columns (v2.2), consolidating to 32 columns (v2.3)
- **Format:** Comma-separated, UTF-8 encoding
- **Sorting:** By `atm_ff` (ATM) or `min_ff` (double), descending
- **File:** User-specified via `--csv-out` flag

**Column Categories:**
- Common (8): timestamp, symbol, structure, spot_price, DTEs, expiry dates
- ATM-specific (8): atm_strike, atm_delta, atm_ff, atm_iv_*, atm_iv_source_*
- Double-specific (8): call/put strikes, deltas, FFs, min_ff, combined_ff
- IV details (6): call/put front/back/fwd IVs
- IV sources (4): iv_source_call/put_front/back (double only)
- Quality (5): earnings_conflict, earnings_date, option_volume_today, liq_rating, earnings_source
- Tracking (1): skip_reason

**JSON Output:**
- **Format:** Nested structure with all metadata
- **File:** User-specified via `--json-out` flag
- **Usage:** Machine-readable for further processing

**Streaming CSV Writer (v2.3):**
- Rows written incrementally (not batched)
- Constant memory usage
- Supports 1500+ symbol scans

### 8. Configurable Thresholds
**Status:** ✅ Production-ready (v2.0)

**CLI Flags:**
```bash
--min-ff 0.20              # Minimum FF ratio to include
--dte-tolerance 5          # Max deviation from target DTE (days)
--delta-tolerance 0.05     # Max delta deviation for strike selection
--timeout 3                # Greeks snapshot timeout (seconds)
--options-volume 10000     # Precise volume threshold (market hours)
```

**Usage Example:**
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL \
  --pairs 30-60 30-90 \
  --min-ff 0.23 \
  --delta-tolerance 0.03 \
  --options-volume 20000 \
  --csv-out scan.csv
```

## Feature Roadmap

### Current (v2.2) ✅
- Core calculation corrections
- ATM 50Δ anchor
- Hybrid volume filtering
- 40-column CSV schema
- Greeks IV primary, ex-earn fallback

### Next (v2.3) ⏳ 20% Complete
- CSV schema reduction (40 → 32 columns)
- Logging system (quiet/normal/verbose/debug)
- Error handling for 1500+ symbol scans
- IV source control (--iv-ex-earn flag) ✅
- Streaming CSV writer ✅

### Future (v3.0+) 📋 Planned
- Automated order placement (TastyTrade API)
- Position tracking and P&L monitoring
- Backtesting framework with historical IV
- Real-time monitoring and alerts
- Web interface (optional)

## Integration Points

### APIs Integrated
1. **TastyTrade Production API**
   - Authentication and session management
   - Market metrics (earnings, liquidity, ex-earn IV)
   - Option chains (equities and futures)
   - dxFeed streaming (Greeks, underlying data)

2. **Yahoo Finance API**
   - Earnings dates (primary source)
   - Futures spot prices (/ES, /NQ, /CL, etc.)

3. **SQLite Database**
   - Earnings cache storage
   - Automatic cache management

### Output Consumers
1. **Excel/Google Sheets** - CSV parsing for manual analysis
2. **Python/Pandas** - Programmatic CSV parsing
3. **Algorithmic Trading Systems** - JSON output for automation
4. **Terminal/Console** - Human-readable summary

## Performance Characteristics

### Scan Speed
- **100 symbols (cache hit):** < 2 minutes
- **100 symbols (cache miss):** 5-10 minutes
- **1000 symbols (cache hit):** < 30 seconds
- **1500+ symbols (streaming):** 30-60 minutes

### Memory Usage
- **Default (v2.2):** Linear growth with result set size
- **Streaming (v2.3+):** Constant memory (rows written incrementally)

### Cache Performance
- **Hit rate (daily scanning):** > 90%
- **Cache read:** < 10ms per symbol
- **Cache miss:** 100-500ms per symbol (Yahoo/TastyTrade)
- **Speedup:** 80-95% on rescans

### Data Quality
- **Greeks IV coverage:** > 95%
- **Earnings accuracy:** 100% (multi-source validation)
- **Liquidity coverage:** > 95% of high-volume symbols

## Known Limitations

### Technical Limitations
1. **Python 3.14 Asyncio Bug**
   - RecursionError on large scans with many timeouts
   - Workaround: Increased recursion limit (10,000)
   - Stable until Python 3.14.1+ fixes upstream

2. **Greeks Timeout**
   - 3s default timeout may miss some strikes
   - Partial results accepted (graceful degradation)
   - Increase timeout with `--timeout` flag if needed

3. **Volume Data Availability**
   - Precise volume requires market hours
   - Default liquidity rating works 24/7
   - Futures often lack volume data (allowed through)

### Business Limitations
1. **TastyTrade Account Required**
   - Production account (not sandbox)
   - Options approval needed
   - Live market data subscription

2. **No Automated Execution**
   - Manual trade entry on TastyTrade platform
   - No position tracking or P&L monitoring
   - No order management

3. **Single Strategy Focus**
   - Calendar spreads only
   - No strangles, iron condors, butterflies
   - No earnings plays (filtered out)

### Operational Limitations
1. **CLI-Only Interface**
   - No web dashboard or GUI
   - Requires terminal comfort
   - Manual execution

2. **No Historical Data**
   - No backtesting framework
   - No FF history tracking
   - One-time scans only

3. **Rate Limiting**
   - No explicit rate limiting implemented
   - Relies on API provider's limits
   - Respectful usage required

## Documentation

### User Documentation
- **CLAUDE.md** (39 KB) - Comprehensive project guide
  - Project overview and architecture
  - Scanner usage and CLI reference
  - CSV schema documentation
  - Version history and migration guides
  - Strategy theory and implementation notes

- **scripts/README_TT.md** - Scanner usage guide
  - Quick start instructions
  - CLI flag reference
  - Common usage examples

### API Documentation
- **docs/tastytrade-openapi-docs/** - OpenAPI 3.0.0 specs
- **docs/tastytrade-sdk-docs/** - TastyTrade SDK reference (v10.1.0)

### Strategy Documentation
- **docs/strategy_origin_docs/** - Original research materials
  - YouTube transcript (strategy source)
  - GPT analysis and SOP
  - Backtest plots

### Related Projects
- **docs/RELATED_PROJECTS.md** - Overview of similar TastyTrade scanners

## Testing Coverage

### Current Testing
1. **Unit Tests** - `tests/test_ff_calculations.py`
   - Forward IV calculation
   - Forward Factor calculation
   - Edge case validation

2. **Integration Tests** - `scripts/test_*.py`
   - Futures API integration
   - Double calendar strike selection
   - Earnings cache functionality
   - Option chain fetching

3. **Manual Testing** - Live scanner runs
   - Small ticker lists (5-10 symbols)
   - Validation of CSV output
   - Filter effectiveness

### Future Testing (Planned)
1. **Mock API Responses** - Deterministic testing
2. **Regression Tests** - CSV output validation
3. **Performance Tests** - Large scan benchmarks
4. **CI/CD Integration** - Automated test runs
