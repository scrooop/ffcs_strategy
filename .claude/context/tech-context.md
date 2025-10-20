---
created: 2025-10-20T18:58:52Z
last_updated: 2025-10-20T18:58:52Z
version: 1.0
author: Claude Code PM System
---

# Technical Context

## Technology Stack

### Core Language and Runtime
- **Python:** 3.14
  - **Known Issue:** Asyncio recursion bug in task cancellation
  - **Workaround:** Increased recursion limit from 1000 → 10000
  - **Status:** Stable until Python 3.14.1+ fixes upstream
  - **Reference:** https://github.com/python/cpython/issues/126211

### Development Environment
- **Environment Manager:** venv (Python virtual environment)
- **Package Manager:** pip
- **IDE/Editor:** VS Code (assumed, Claude Code integration)
- **Version Control:** Git (GitHub repository)

### Repository
- **URL:** https://github.com/scrooop/ffcs_strategy.git
- **Branch:** master
- **Remote:** origin

## Core Dependencies

### TastyTrade SDK (Primary Integration)
**Package:** `tastytrade` (official SDK)
**Purpose:** Options market data and trading infrastructure

**Key Modules Used:**
```python
from tastytrade import Session
from tastytrade.instruments import NestedOptionChain, NestedFutureOptionChain
from tastytrade.dxfeed import Greeks, DXLinkStreamer, Underlying
from tastytrade.metrics import get_market_metrics
```

**Features Used:**
1. **Session Management**
   - Production environment authentication
   - OAuth token handling
   - Session persistence

2. **Market Data Streaming (dxFeed)**
   - Greeks events (IV, delta, gamma, theta, vega)
   - Underlying events (spot price, option volume)
   - WebSocket-based streaming via DXLinkStreamer
   - Snapshot mode with timeout handling

3. **Instrument Lookup**
   - NestedOptionChain for equity options
   - NestedFutureOptionChain for futures options
   - Expiration and strike discovery
   - Streamer symbol generation

4. **Market Metrics API**
   - Earnings dates
   - Liquidity rating (0-5 scale)
   - IV rank and percentile
   - Ex-earn IV (earnings-removed implied volatility)

**API Endpoints Used:**
- `/sessions` - Authentication
- `/market-metrics` - Earnings, liquidity, IV data
- `/instruments/equity-options` - Equity option chains
- `/instruments/future-options` - Futures option chains
- dxFeed WebSocket - Real-time Greeks and underlying data

### Yahoo Finance (yfinance)
**Package:** `yfinance`
**Purpose:** Supplemental market data and earnings

**Usage:**
1. **Futures Spot Prices**
   - TastyTrade API doesn't provide futures quotes
   - Yahoo Finance provides real-time futures prices
   - Used for /ES, /NQ, /CL, /GC, etc.

2. **Earnings Date Fetching (Primary Source)**
   - Fast earnings date lookup (~100ms per symbol)
   - Primary source in multi-source pipeline
   - Fallback to TastyTrade if Yahoo fails

**Example:**
```python
import yfinance as yf
ticker = yf.Ticker("AAPL")
earnings_date = ticker.calendar.get('Earnings Date')
```

### SQLite (Built-in)
**Package:** `sqlite3` (Python standard library)
**Purpose:** Earnings cache persistence

**Schema:**
```sql
CREATE TABLE earnings (
    symbol TEXT PRIMARY KEY,
    earnings_date TEXT,
    source TEXT,
    fetched_at TEXT
);
```

**Features:**
- Automatic cache invalidation (earnings date passed)
- Multi-source data tracking (cache/yahoo/tastytrade)
- Thread-safe operations
- Location: `.cache/earnings.db`

### Asyncio (Built-in)
**Package:** `asyncio` (Python standard library)
**Purpose:** Concurrent API operations and streaming

**Usage:**
1. **dxFeed Greeks Streaming**
   - Async DXLinkStreamer connection
   - Concurrent subscription to multiple strikes
   - Timeout handling with asyncio.wait_for()

2. **Batch Market Data Fetching**
   - Parallel underlying price lookups
   - Concurrent market metrics fetching
   - Rate limiting and error handling

**Known Issues:**
- Python 3.14 recursion bug in task cancellation cleanup
- Workaround: `sys.setrecursionlimit(10000)` at script start

## Development Tools

### Testing
- **Framework:** pytest (assumed, tests/ directory exists)
- **Test Types:**
  - Unit tests: `tests/test_ff_calculations.py`
  - Integration tests: `scripts/test_*.py`
  - Live API tests: Manual scanner runs

### Code Quality
- **Linting:** Not specified (standard Python best practices followed)
- **Formatting:** Not specified (consistent style observed)
- **Type Hints:** Partial usage in core functions

### Documentation Tools
- **Markdown:** All documentation in Markdown format
- **Docstrings:** Python docstrings in scanner functions
- **API Docs:** OpenAPI 3.0.0 specs for TastyTrade

### Project Management
- **Epic Tracking:** Custom `.claude/epics/` system
- **Task Tracking:** GitHub Issues integration
- **Context Management:** Claude Code context system

## API Integrations

### TastyTrade Production API
**Environment:** Production (required for live Greeks)
**Authentication:** Username + Password → OAuth token
**Base URL:** `https://api.tastyworks.com` (assumed)

**Rate Limits:**
- Not explicitly documented in code
- No rate limiting currently implemented
- Scanner handles timeouts gracefully

**Error Handling:**
- Connection timeouts (default 3s for Greeks)
- Graceful degradation (partial results accepted)
- Retry logic for critical operations

### Yahoo Finance API
**Access:** Public, no authentication
**Rate Limits:** Informal (respectful usage)
**Timeout:** 5 seconds per request

**Reliability:**
- Primary source for earnings dates (~100ms)
- Occasional timeouts or missing data
- Fallback to TastyTrade in pipeline

### dxFeed Market Data
**Protocol:** WebSocket via DXLinkStreamer
**Authentication:** Via TastyTrade session token
**Data Types:**
- Greeks events (IV, delta, gamma, theta, vega, rho)
- Underlying events (spot, volume, open interest)

**Streaming Configuration:**
```python
streamer = await DXLinkStreamer.create(session)
await streamer.subscribe(Greeks, symbols)
quotes = await asyncio.wait_for(
    streamer.get_event_nowait(),
    timeout=3.0
)
```

## Data Storage

### File-Based Storage
1. **CSV Output**
   - Format: 40-column schema (v2.2), reducing to 32 columns (v2.3)
   - Location: User-specified via `--csv-out` flag
   - Writing: Streaming writer (v2.3+) for memory efficiency

2. **JSON Output**
   - Format: Nested structure with all metadata
   - Location: User-specified via `--json-out` flag
   - Usage: Machine-readable output for further processing

### Cache Storage
1. **Earnings Cache (SQLite)**
   - Location: `.cache/earnings.db`
   - Size: Minimal (100-1000 rows typical)
   - Persistence: Across runs, automatic invalidation
   - Backup: Not needed (rebuilds automatically)

### No Database Requirements
- No PostgreSQL, MySQL, or other RDBMS
- No persistent storage of market data
- No user data storage
- Stateless scanner design (each run independent)

## Performance Considerations

### Caching Strategy
1. **Earnings Cache (Primary Optimization)**
   - Cache hit: <10ms per symbol
   - Cache miss: 100-500ms per symbol
   - Hit rate: >90% for daily scanning
   - Impact: 80-95% runtime reduction

2. **No Market Data Caching**
   - Market data changes constantly (IV, prices)
   - Greeks fetched fresh every run
   - No stale data concerns

### Concurrency
1. **Parallel Operations**
   - Multiple symbol processing (sequential by symbol)
   - Batch market metrics fetching
   - Concurrent Greeks subscriptions (per symbol)

2. **Sequential Bottlenecks**
   - Authentication (once per run)
   - Per-symbol dxFeed streaming (3s timeout each)
   - CSV writing (streaming in v2.3+)

### Memory Management
1. **Streaming CSV Writer (v2.3+)**
   - Rows written incrementally
   - No full result set in memory
   - Supports 1500+ symbol scans

2. **Greeks Data**
   - Short-lived (per symbol, then discarded)
   - No accumulation across symbols

### Network Optimization
1. **Batch Fetching**
   - Market metrics fetched in batch (all symbols)
   - Earnings cache reduces API calls by 80-95%

2. **Timeout Management**
   - Greeks timeout: 3s default (configurable)
   - Yahoo Finance timeout: 5s
   - TastyTrade API: No explicit timeout (uses SDK defaults)

## Environment Configuration

### Required Environment Variables
```bash
export TT_USERNAME="your_tastytrade_username"
export TT_PASSWORD="your_tastytrade_password"
```

**Security Notes:**
- Credentials stored in environment, not code
- Production environment required for live data
- No OAuth token storage (regenerated each run)

### Optional Configuration
- No config files currently used
- All options via CLI flags
- Default values hardcoded in scanner

## Build and Deployment

### Local Development
```bash
# Setup
python -m venv venv
source venv/bin/activate
pip install tastytrade yfinance

# Run
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 \
  --min-ff 0.20
```

### No CI/CD Pipeline
- Manual testing and deployment
- No automated builds
- No containerization (yet)

### No Production Deployment
- CLI tool for local use
- No server deployment
- No web interface
- No scheduled jobs

## Monitoring and Logging

### Current Logging
- Python `logging` module (assumed)
- Console output (default)
- Diagnostic messages for debugging

### Future Logging (v2.3 Epic)
- Output modes: quiet/normal/verbose/debug
- Structured logging
- Log file support
- Error tracking for large scans

### No External Monitoring
- No APM (Application Performance Monitoring)
- No error tracking service (Sentry, etc.)
- No metrics collection (Prometheus, etc.)

## Technical Debt and Known Issues

### Active Workarounds
1. **Python 3.14 Asyncio Bug**
   - Impact: RecursionError on large scans
   - Workaround: Increased recursion limit
   - Plan: Remove when Python 3.14.1+ released

### Missing Features
1. **Requirements.txt**
   - No formal dependency tracking
   - Dependencies documented in CLAUDE.md only

2. **Type Hints**
   - Partial coverage
   - No mypy validation

3. **Rate Limiting**
   - No explicit rate limiting on API calls
   - Relies on API provider's limits

4. **Retry Logic**
   - Basic timeout handling
   - No exponential backoff
   - No circuit breaker pattern

### Technical Improvements Planned
1. **v2.3 Epic** - Logging system, error handling
2. **Future** - Automated testing, CI/CD, containerization

## Dependency Graph

```
ff_tastytrade_scanner.py
├─> tastytrade SDK
│   ├─> Session (authentication)
│   ├─> NestedOptionChain (option chains)
│   ├─> DXLinkStreamer (Greeks streaming)
│   └─> get_market_metrics (earnings, liquidity)
├─> yfinance
│   └─> Ticker (earnings dates, futures prices)
├─> sqlite3 (built-in)
│   └─> earnings_cache.py
└─> asyncio (built-in)
    └─> Greeks streaming, concurrent operations

earnings_cache.py
├─> sqlite3 (cache storage)
├─> yfinance (primary earnings source)
└─> tastytrade SDK (fallback earnings source)
```

## Version Compatibility

### Python Version Requirements
- **Minimum:** Python 3.12 (asyncio features)
- **Recommended:** Python 3.14 (current development version)
- **Maximum:** Python 3.14 (tested, workaround for asyncio bug)

### SDK Version Constraints
- **tastytrade:** v10.1.0 (documented in SDK docs)
- **yfinance:** Latest (no version pinned)

### Breaking Changes History
- **v2.1 → v2.2:** CSV schema change (31 → 40 columns)
- **v2.2 → v2.3:** CSV schema change (40 → 32 columns, in progress)
