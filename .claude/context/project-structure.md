---
created: 2025-10-20T18:58:52Z
last_updated: 2025-10-20T18:58:52Z
version: 1.0
author: Claude Code PM System
---

# Project Structure

## Repository Overview

```
ffcs_strategy/
├── .cache/                        # Runtime cache for performance optimization
│   └── earnings.db                # SQLite earnings cache (auto-invalidating)
├── .claude/                       # Claude Code project management
│   ├── archive/                   # Archived documentation
│   ├── context/                   # Project context documentation (this directory)
│   ├── epics/                     # Epic-based task tracking
│   │   ├── core-calc-corrections/ # v2.2 calculation corrections (COMPLETE)
│   │   ├── fast-earnings-check/   # v2.1 earnings cache system (COMPLETE)
│   │   ├── ff-scanner-v2/         # v2.0 quality filtering (COMPLETE)
│   │   └── output-csv-terminal-flags/ # v2.3 CSV/logging improvements (IN PROGRESS)
│   └── rules/                     # Project rules and standards
├── data/                          # Data files and outputs
├── docs/                          # Documentation
│   ├── strategy_origin_docs/      # Original strategy research materials
│   ├── tastytrade-openapi-docs/   # TastyTrade OpenAPI specifications
│   └── tastytrade-sdk-docs/       # TastyTrade SDK documentation
├── scripts/                       # Executable scripts and utilities
│   ├── ff_tastytrade_scanner.py   # Main scanner CLI (core implementation)
│   ├── earnings_cache.py          # Earnings cache management module
│   └── test_*.py                  # Test scripts for various features
├── tests/                         # Unit and integration tests
│   ├── __init__.py
│   └── test_ff_calculations.py    # Core calculation tests
├── venv/                          # Python virtual environment
├── CLAUDE.md                      # Project instructions for Claude Code
├── CCPM_COMPLETE_SOP.md          # Complete CCPM documentation
└── _TODO.txt                      # Manual task tracking file
```

## Directory Purposes

### `.cache/`
Runtime cache directory for performance optimization:
- **`earnings.db`** - SQLite database caching earnings dates from multiple sources
  - Automatic invalidation when earnings dates pass
  - Reduces API calls by 80-95% on subsequent runs
  - Shared across all scanner invocations
  - Safe to delete manually (rebuilds automatically)

### `.claude/`
Claude Code project management system:
- **`context/`** - Living project documentation (you are here)
- **`epics/`** - Epic-based task tracking with GitHub issue integration
- **`rules/`** - Project-specific rules and standards
- **`archive/`** - Historical documentation

### `.claude/epics/`
Epic-level task organization:

#### Completed Epics:
1. **`core-calc-corrections/`** (v2.2) - ATM strike selection, FF calculation fixes, volume filtering
2. **`fast-earnings-check/`** (v2.1) - Multi-source earnings pipeline with SQLite caching
3. **`ff-scanner-v2/`** (v2.0) - Quality filtering, double calendars, earnings detection

#### Active Epic:
4. **`output-csv-terminal-flags/`** (v2.3) - CSV schema consolidation, logging system, error handling

Each epic contains:
- `epic.md` - Epic definition and goals
- `prd.md` - Product requirements document
- `execution-status.md` - Task tracking and status updates
- `{task_id}.md` - Individual task definitions (linked to GitHub issues)
- `updates/` - Task-specific implementation updates and documentation

### `docs/`
Comprehensive project documentation:

#### `strategy_origin_docs/`
Original strategy research and source materials:
- `FFCS-ORIGIN-YOUTUBE-TRANSCRIPT.txt` - Original YouTube video transcript
- `FFCS-STRATEGY-REPORT-GPT.md` - GPT analysis of strategy
- `FFCS-SOP-FROM-GPT.md` - Standard operating procedures
- `FFCS-BACKTEST-PLOTS.pdf` - Backtest performance visualizations

#### `tastytrade-openapi-docs/`
TastyTrade API specifications:
- `tastytrade_official_API_docs_full_spec.json` - Complete OpenAPI 3.0.0 spec (393 KB)
- `open-api-spec_*.md` - Individual endpoint documentation (instruments, market-data, orders, etc.)

#### `tastytrade-sdk-docs/`
TastyTrade Python SDK documentation:
- `session.md` - Authentication and session management
- `dxfeed.md` - Market data streaming with Greeks
- `instruments.md` - Option chains and instrument lookup
- `metrics.md` - IV rank, liquidity, market metrics
- `order.md` - Order placement and execution
- Additional SDK reference documentation

#### Root-level docs:
- `RELATED_PROJECTS.md` - Overview of related TastyTrade scanner projects
- `issue-4-double-calendar-implementation.md` - Double calendar implementation notes
- `v1_IMPLEMENTATION_PLAN.md` - Original v1.0 implementation plan

### `scripts/`
Main implementation and test scripts:

#### Core Implementation:
- **`ff_tastytrade_scanner.py`** - Main scanner CLI (1000+ lines)
  - TastyTrade API integration
  - dxFeed Greeks streaming
  - Forward IV calculation
  - Multi-structure support (ATM/double calendars)
  - Quality filtering (earnings, volume, liquidity)
  - CSV/JSON output

#### Support Modules:
- **`earnings_cache.py`** - Earnings cache management
  - Multi-source fetching (Yahoo Finance, TastyTrade)
  - SQLite storage and retrieval
  - Automatic cache invalidation

#### Test Scripts:
- `test_futures_*.py` - Futures options testing
- `test_double_calendar_strikes.py` - Strike selection validation
- `test_earnings_cache.py` - Cache functionality testing
- Additional integration test scripts

### `tests/`
Formal test suite:
- `test_ff_calculations.py` - Unit tests for forward IV calculations
- `__init__.py` - Test package initialization
- Additional test modules (growing)

### Root Files

#### Configuration and Documentation:
- **`CLAUDE.md`** - Comprehensive project instructions (39 KB)
  - Project overview and architecture
  - Scanner usage guide
  - CSV schema documentation
  - Version history and migration guides
  - Strategy theory and implementation notes

- **`CCPM_COMPLETE_SOP.md`** - Complete CCPM (Claude Code Project Management) documentation
  - Epic management workflows
  - Task tracking procedures
  - GitHub issue integration

#### Project Management:
- **`_TODO.txt`** - Manual task tracking (37 KB)
  - Quick notes and task lists
  - Implementation checklists
  - Development session notes

## File Naming Conventions

### Python Scripts:
- Main scanner: `ff_tastytrade_scanner.py` (underscore-separated)
- Test scripts: `test_*.py` prefix
- Module files: `module_name.py` (underscore-separated)

### Documentation:
- Project docs: `UPPERCASE_WITH_UNDERSCORES.md`
- Epic docs: `lowercase-with-hyphens.md`
- Task docs: `{issue_number}.md` (numeric GitHub issue ID)

### Timestamps (per project rules):
- Format: `YYMMDD_HHMM_description`
- Example: `251020_1830_analysis_results.csv`
- Timezone: CDT (Central Daylight Time)

### Cache Files:
- SQLite databases: `.db` extension
- Located in `.cache/` directory
- Auto-managed (safe to delete)

## Module Organization

### Core Scanner Module (`ff_tastytrade_scanner.py`):
```python
# Authentication & Session
- TastyTrade API authentication
- Production environment configuration

# Data Fetching
- fetch_market_metrics()      # Batch fetch earnings + volume
- get_market_data()            # Underlying spot prices
- NestedOptionChain.get()      # Expirations & strikes
- snapshot_greeks()            # dxFeed Greeks streaming
- extract_xearn_iv()           # Ex-earn IV fallback

# Strike Selection
- pick_atm_strike()            # 50Δ ATM strike selection
- pick_delta_strike()          # ±35Δ strike selection
- nearest_expiration()         # DTE matching with tolerance

# Forward IV Calculation
- calculate_forward_iv()       # Variance decomposition
- calculate_forward_factor()   # FF = (σ₁ - σ_fwd) / σ_fwd

# Quality Filtering
- check_earnings()             # Earnings conflict detection
- check_liquidity_rating()     # Default 24/7 filtering
- check_option_volume()        # Precise market-hours filtering

# Output
- write_csv()                  # Streaming CSV writer (v2.2+)
- write_json()                 # JSON output
```

### Earnings Cache Module (`earnings_cache.py`):
```python
# Cache Management
- EarningsCache class          # SQLite cache interface
- fetch_earnings_date()        # Multi-source fetching
- is_valid()                   # Cache invalidation logic

# Data Sources (priority order)
1. SQLite cache                # <10ms per symbol
2. Yahoo Finance               # ~100ms per symbol
3. TastyTrade API              # ~500ms per symbol
4. Graceful degradation        # Allow through with warning
```

## Data Flow

### Scanner Execution Flow:
```
1. Authentication
   └─> TastyTrade Production Session

2. Pre-filtering (fast, cached)
   └─> Earnings dates (cache → yahoo → tastytrade)
   └─> Skip symbols with earnings conflicts

3. Market Data Fetching (parallel where possible)
   ├─> Underlying spot prices
   ├─> Option chain (expirations + strikes)
   └─> Market metrics (liquidity rating)

4. Greeks Streaming (per symbol)
   └─> dxFeed snapshot (IV + delta for all strikes)

5. Strike Selection
   ├─> ATM: 50Δ strike (delta closest to 0.50)
   └─> Double: ±35Δ strikes (call + put)

6. Forward IV Calculation
   ├─> Variance decomposition (σ₁² T₁ and σ₂² T₂)
   └─> Forward Factor: FF = (σ₁ - σ_fwd) / σ_fwd

7. Quality Filtering
   ├─> Earnings conflicts (default: enabled)
   ├─> Liquidity rating (default: ≥3)
   └─> Option volume (optional: --options-volume flag)

8. Output Generation
   ├─> CSV: 40 columns (v2.2) or streaming writer (v2.3+)
   └─> JSON: Nested structure with all metadata
```

## Growth Patterns

### Version Evolution:
- **v1.0** - Initial scanner (ATM only, 25 columns)
- **v2.0** - Quality filtering + double calendars (31 columns)
- **v2.1** - Fast earnings cache (performance optimization)
- **v2.2** - Core calculation corrections (40 columns)
- **v2.3** - CSV consolidation + logging (32 columns, in progress)

### File Growth:
- Main scanner: Started at ~500 lines, now 1000+ lines
- Documentation: CLAUDE.md grew from 10 KB → 39 KB
- Epic system: Added in v2.0, now 4 epics tracked
- Test coverage: Growing from core calculations to integration tests

## Dependencies Management

**Python Version:** 3.14 (with asyncio recursion workaround)
**Virtual Environment:** `venv/` directory
**Package Management:** pip-based (no requirements.txt yet)

**Key Dependencies:**
- `tastytrade` - Official SDK for TastyTrade API
- `yfinance` - Yahoo Finance for futures prices and earnings dates
- `sqlite3` - Built-in, for earnings cache
- `asyncio` - Built-in, for dxFeed streaming

## Access Patterns

### Typical Development Session:
1. Activate venv: `source venv/bin/activate`
2. Check epic status: `cat .claude/epics/{epic_name}/execution-status.md`
3. Run scanner: `python scripts/ff_tastytrade_scanner.py --tickers ... --pairs ...`
4. Review output: Check CSV in `data/` or console output
5. Update docs: Edit CLAUDE.md, epic files, context files
6. Commit changes: Git workflow with epic references

### Typical Testing Workflow:
1. Unit tests: `python -m pytest tests/`
2. Integration tests: `python scripts/test_*.py`
3. Live scanner test: `python scripts/ff_tastytrade_scanner.py --tickers AAPL --pairs 30-60`
4. Validate CSV: Check column count, FF calculations, filtering logic

## Project Size Metrics

- **Total Python files:** ~15 (excluding venv)
- **Main scanner:** ~1000 lines
- **Documentation:** ~100 KB total
- **Test scripts:** ~10 files
- **Epic documentation:** ~50 files across 4 epics
- **API documentation:** ~50 files (OpenAPI + SDK docs)
