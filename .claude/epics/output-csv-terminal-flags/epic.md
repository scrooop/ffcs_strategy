---
name: output-csv-terminal-flags
status: in-progress
created: 2025-10-20T17:46:00Z
updated: 2025-10-20T20:03:38Z
progress: 60%
prd: .claude/prds/output-csv-terminal-flags.md
github: https://github.com/scrooop/ffcs_strategy/issues/34
---

# Epic: output-csv-terminal-flags

## Overview

Refactor FF scanner to eliminate CSV redundancy (40 → 32 columns), implement professional logging system with output modes, fix high-volume scanning crashes, and add IV source control. This epic focuses on pragmatic improvements using Python's built-in logging infrastructure and minimal code changes to existing `ff_tastytrade_scanner.py`.

**Key Technical Decisions:**
- Leverage Python's native `logging` module (no external deps)
- Use single-pass CSV schema migration (eliminate `atm_*` namespace)
- Wrap external API calls in try/except for graceful degradation
- Add conditional logic for `--iv-ex-earn` flag to skip Greeks streaming

## Architecture Decisions

### AD1: Unified CSV Schema (Breaking Change)
**Decision:** Eliminate separate `atm_*` column namespace, use unified columns for both structures
**Rationale:**
- Reduces confusion ("ATM is always either call or put")
- Eliminates 16 empty columns per row (40% of current schema)
- Simplifies CSV parsing logic (single namespace for strikes/deltas/FF)

**Implementation:**
- Rename: `call_strike` → `strike`, `call_delta` → `delta`, `call_ff` → `ff`
- Remove: 8 `atm_*` columns (atm_strike, atm_delta, atm_ff, atm_iv_front/back/fwd, atm_iv_source_front/back)
- ATM rows: Populate `strike`, `delta`, `ff`, `min_ff` (leave `put_*` empty)
- Double rows: Populate `strike`, `put_strike`, `delta`, `put_delta`, `ff`, `put_ff`, `min_ff`, `combined_ff`

**Migration Path:** Provide column mapping table in CLAUDE.md, update version to v3.0

### AD2: Hierarchical Logging System
**Decision:** Use Python `logging` module with named sub-loggers
**Rationale:**
- Native to Python (no dependencies)
- Supports filtering by log level and logger name
- Easy to add file handlers for `--log-file` flag
- Can suppress third-party loggers (yfinance) at module level

**Logger Hierarchy:**
```
scanner (root)
├── scanner.earnings (earnings cache/fetch events)
├── scanner.market_data (spot price, option chains)
├── scanner.greeks (Greeks IV streaming)
└── scanner.quality (filtering: liquidity, earnings, delta)
```

**Output Modes:**
- `--quiet`: `scanner` logger at ERROR level
- Normal (default): `scanner` logger at INFO level, formatted as `[SYMBOL] STATUS: details`
- `--verbose`: `scanner` logger at INFO level, show ALL symbols (including those that pass filters)
- `--debug`: All loggers at DEBUG level (existing behavior)

### AD3: Error Handling Strategy
**Decision:** Wrap all external API calls in try/except, skip symbols on failure, track skip reasons
**Rationale:**
- tastytrade API returns inconsistent data (missing 'strikes' field)
- yfinance API returns unpredictable 404s
- User needs 100% scan completion rate (no crashes)

**Critical Wraps:**
1. `NestedOptionChain.get()` → catch `pydantic.ValidationError`
2. `get_market_data()` → catch generic exceptions
3. `yfinance` calls → already handled in earnings_cache.py

**Skip Tracking:**
- Add `SKIP_INVALID_CHAIN = "invalid_chain_data"` constant
- Update `skip_stats` dict to count all skip reasons
- Populate `skip_reason` CSV column for debugging

### AD4: IV Source Control (Conditional Logic)
**Decision:** Add `--iv-ex-earn` flag, skip Greeks streaming when enabled
**Rationale:**
- User wants to A/B test Greeks IV vs ex-earn IV
- Skipping Greeks streaming saves 20-30% runtime (no async dxFeed snapshot)
- Ex-earn IV available from Market Metrics API (already fetched)

**Implementation:**
- Add `use_exearn_iv` boolean parameter to `scan()` function
- Check flag before calling `snapshot_greeks()` in ATM/double calendar logic
- Update `iv_source_*` columns: "greeks" vs "exearn_primary" vs "exearn_fallback"

## Technical Approach

### Python Logging Configuration

**Single Logging Setup Function:**
```python
def setup_logging(mode: str, log_file: Optional[str] = None):
    """
    Configure logging hierarchy based on output mode.

    Args:
        mode: "quiet", "normal", "verbose", or "debug"
        log_file: Optional file path for logging output
    """
    # Root scanner logger
    scanner_logger = logging.getLogger("scanner")

    # Set level based on mode
    if mode == "quiet":
        scanner_logger.setLevel(logging.ERROR)
    elif mode == "debug":
        scanner_logger.setLevel(logging.DEBUG)
    else:  # normal, verbose
        scanner_logger.setLevel(logging.INFO)

    # Terminal handler (formatted)
    console = logging.StreamHandler()
    if mode == "debug":
        console.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    else:
        # Custom formatter: [SYMBOL] STATUS: details (no timestamps)
        console.setFormatter(SymbolFormatter())
    scanner_logger.addHandler(console)

    # File handler (if --log-file provided)
    if log_file:
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)  # File gets all levels
        fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        scanner_logger.addHandler(fh)

    # Suppress yfinance logger (only show ERROR+)
    logging.getLogger("yfinance").setLevel(logging.ERROR)
```

**Custom Formatter for Symbol Messages:**
```python
class SymbolFormatter(logging.Formatter):
    """Format log messages as [SYMBOL] STATUS: details"""
    def format(self, record):
        # Extract symbol from message (assume format: "SYMBOL: message")
        if ':' in record.msg:
            parts = record.msg.split(':', 1)
            symbol = parts[0].strip()
            message = parts[1].strip()
            status = record.levelname[:4].upper()  # PASS, FILT, ERRO, SKIP
            return f"[{symbol:6}] {status}: {message}"
        return record.msg
```

### CSV Schema Migration

**Current Schema (v2.2, 40 columns):**
```python
CSV_COLUMNS = [
    "timestamp", "symbol", "structure", "spot_price",
    "front_dte", "back_dte", "front_expiry", "back_expiry",
    "atm_strike", "atm_delta", "atm_ff", ...  # 8 atm_* columns
    "call_strike", "put_strike", ...           # 8 call/put columns
    ...
]
```

**New Schema (v3.0, 32 columns):**
```python
CSV_COLUMNS = [
    # Metadata (4)
    "timestamp", "symbol", "structure", "spot_price",
    # Expirations (4)
    "front_dte", "back_dte", "front_expiry", "back_expiry",
    # Strikes/Deltas (4) - unified namespace
    "strike", "put_strike", "delta", "put_delta",
    # FF Metrics (4)
    "ff", "put_ff", "min_ff", "combined_ff",
    # IV Detail (6)
    "call_front_iv", "call_back_iv", "call_fwd_iv",
    "put_front_iv", "put_back_iv", "put_fwd_iv",
    # IV Sources (4)
    "iv_source_call_front", "iv_source_call_back",
    "iv_source_put_front", "iv_source_put_back",
    # Quality Filters (6)
    "earnings_conflict", "earnings_date", "option_volume_today",
    "liq_rating", "earnings_source", "skip_reason"
]
```

**Row Population Logic:**
```python
# ATM calendar row
row = {
    "strike": f"{atm_strike:.2f}",           # NEW: unified column
    "delta": round(atm_delta, 4),            # NEW: unified column
    "ff": round(atm_ff, 6),                  # NEW: unified column
    "min_ff": round(atm_ff, 6),              # Same as ff for ATM
    "put_strike": "",                        # Empty for ATM
    "put_delta": "",                         # Empty for ATM
    "put_ff": "",                            # Empty for ATM
    "combined_ff": "",                       # Empty for ATM
    ...
}

# Double calendar row
row = {
    "strike": f"{call_strike:.2f}",          # Renamed from call_strike
    "put_strike": f"{put_strike:.2f}",       # UNCHANGED
    "delta": round(call_delta, 4),           # Renamed from call_delta
    "put_delta": round(put_delta, 4),        # UNCHANGED
    "ff": round(call_ff, 6),                 # Renamed from call_ff
    "put_ff": round(put_ff, 6),              # UNCHANGED
    "min_ff": round(min(call_ff, put_ff), 6),  # UNCHANGED
    "combined_ff": round((call_ff + put_ff)/2, 6),  # UNCHANGED
    ...
}
```

### Error Handling Pattern

**Standardized Try/Except Wrapper:**
```python
# In scan() function, wrap NestedOptionChain.get()
try:
    if is_futures:
        chain_list = NestedFutureOptionChain.get(session, sym)
    else:
        chain_list = NestedOptionChain.get(session, sym)
except pydantic.ValidationError as e:
    logger.warning(f"{sym}: Invalid option chain data (Pydantic validation failed), skipping")
    skip_stats[SKIP_INVALID_CHAIN] = skip_stats.get(SKIP_INVALID_CHAIN, 0) + 1
    continue
except Exception as e:
    logger.error(f"{sym}: Failed to fetch option chain ({e}), skipping")
    skip_stats[SKIP_NO_CHAIN] = skip_stats.get(SKIP_NO_CHAIN, 0) + 1
    continue
```

### IV Source Control Implementation

**Modify scan() function signature:**
```python
async def scan(
    session: Session,
    tickers: List[str],
    pairs: List[Tuple[int, int]],
    min_ff: float = 0.20,
    dte_tolerance: int = 5,
    timeout: float = 3.0,
    allow_earnings: bool = False,
    skip_liquidity: bool = False,
    show_all: bool = False,
    structure_filter: str = "both",
    delta_tolerance: float = 0.05,
    use_exearn_iv: bool = False,  # NEW PARAMETER
    earnings_data: Optional[Dict[str, Tuple[Optional[date], str]]] = None
) -> Tuple[List[dict], Dict[str, int], int, int]:
```

**Conditional Greeks Fetching:**
```python
# In ATM calendar logic (around line 1417)
if use_exearn_iv:
    # Skip Greeks streaming, use ex-earn IV directly
    greeks_map = {}
    iv_source = "exearn_primary"
else:
    # Existing logic: fetch Greeks IV, fallback to ex-earn
    async with DXLinkStreamer(session) as streamer:
        greeks_map = await snapshot_greeks(...)
    iv_source = "greeks" if greeks_map else "exearn_fallback"
```

## Implementation Strategy

### Development Phases (Prioritized by User)

**Phase 1: IV Source Control** (1 day, HIGHEST PRIORITY)
- Quick win: Add `--iv-ex-earn` flag, skip Greeks streaming
- Immediate value: 20-30% performance improvement for testing

**Phase 2: Bug Fixes & Error Handling** (2 days)
- Critical: Wrap `NestedOptionChain.get()` to prevent crashes
- Enables: 1500+ symbol scans without manual batching

**Phase 3: CSV Schema Refactor** (2-3 days)
- Breaking change: Requires migration guide and version bump
- High value: Eliminates CSV confusion, reduces column count 20%

**Phase 4: Terminal Output & Logging** (3-4 days)
- User experience: Clean, consistent terminal output
- Complexity: Custom formatter, output modes, file logging

**Phase 5: Documentation & Testing** (1-2 days)
- Documentation: Update CLAUDE.md, README_TT.md with v3.0 schema and new flags
- Testing: Validate all flag combinations, test migration from v2.2

### Risk Mitigation

**Risk 1: CSV Breaking Change**
- Mitigation: Provide detailed migration guide with column mapping table
- Mitigation: Version bump to v3.0, warn users in release notes
- Mitigation: Test migration with real v2.2 CSV files

**Risk 2: Logging Performance Overhead**
- Mitigation: Profile logging impact (<5% acceptable)
- Mitigation: Use lazy string formatting (`logger.info("%s", msg)` not `logger.info(f"{msg}")`)

**Risk 3: yfinance Logger Suppression**
- Mitigation: Only suppress at WARNING level (allow ERROR to pass through)
- Mitigation: Test that other libraries using yfinance aren't affected

## Task Breakdown Preview

High-level task categories (≤10 tasks total):

1. **[Issue #1] Add `--iv-ex-earn` Flag & IV Source Control** (Priority 1)
   - Add argparse flag, pass to scan(), skip Greeks streaming when enabled
   - Update `iv_source_*` columns to show "exearn_primary"
   - Test performance improvement (measure runtime with/without flag)

2. **[Issue #2] Fix High-Volume Scanning Crash (Pydantic Error)** (Priority 2)
   - Wrap `NestedOptionChain.get()` in try/except for ValidationError
   - Add `SKIP_INVALID_CHAIN` constant and skip_stats tracking
   - Test with 1500+ symbol list (S&P 1500)

3. **[Issue #3] Implement Hierarchical Logging System** (Priority 4)
   - Create `setup_logging()` function with scanner.* sub-loggers
   - Add `SymbolFormatter` class for `[SYMBOL] STATUS: details` format
   - Suppress yfinance logger at WARNING level

4. **[Issue #4] Add Terminal Output Modes (--quiet, --verbose)** (Priority 4)
   - Add `--quiet` flag (ERROR level only, summary at end)
   - Add `--verbose` flag (INFO level, show ALL symbols)
   - Update existing `--debug` to use DEBUG level

5. **[Issue #5] Add File Logging Support (--log-file)** (Priority 4)
   - Add `--log-file <path>` argparse flag
   - Add FileHandler to scanner logger with DEBUG level
   - Test file output includes timestamps and all log levels

6. **[Issue #6] Refactor CSV Schema to v3.0 (Eliminate atm_* Columns)** (Priority 3)
   - Update `CSV_COLUMNS` list (40 → 32 columns)
   - Rename columns: `call_strike` → `strike`, `call_delta` → `delta`, `call_ff` → `ff`
   - Remove `atm_*` columns (8 total)
   - Update row population logic for ATM and double calendars

7. **[Issue #7] Reorder CSV Columns (Trading-Focused Layout)** (Priority 3)
   - Group columns: Metadata → Expirations/Strikes → FF Metrics → IV Detail → Quality Filters
   - Move FF columns closer to right side (after strikes/expirations)
   - Test CSV readability with sample data

8. **[Issue #8] Update Documentation (CLAUDE.md, README_TT.md)** (Priority 5)
   - Document v3.0 CSV schema with column mapping table (v2.2 → v3.0)
   - Document new CLI flags: `--iv-ex-earn`, `--quiet`, `--verbose`, `--log-file`
   - Add terminal output examples for each mode

9. **[Issue #9] Create Migration Guide v2.2 → v3.0** (Priority 5)
   - Write pandas code examples for v2.2 vs v3.0 parsing
   - Create column mapping reference table
   - Document breaking changes and migration steps

10. **[Issue #10] Integration Testing & Validation** (Priority 5)
    - Test all output modes: quiet, normal, verbose, debug
    - Test all flag combinations: `--verbose + --log-file`, `--quiet + --csv-out`, etc.
    - Test CSV migration with real v2.2 files
    - Test 1500+ symbol scan (S&P 1500 index)

## Dependencies

### External Dependencies
- **tastytrade SDK** (`tastytrade>=7.0`): Required for Pydantic v2 support
- **yfinance** (`yfinance>=0.2.0`): Required for earnings fetching
- **Python** (`>=3.10`): Required for match/case statements and modern typing

### Internal Dependencies
- **earnings_cache.py**: Must support new logging system (scanner.earnings logger)
- **Existing CSV parsers**: Will break on v3.0 schema (migration guide required)

### Timeline Dependencies
- **Market hours access**: Required for testing Greeks IV vs ex-earn IV comparison
- **Real data testing**: Need production tastytrade API access for validation

## Success Criteria (Technical)

### Performance Benchmarks
- **P1:** 1500-symbol scan completes without crashes (100% success rate)
- **P2:** Logging overhead <5% vs no logging
- **P3:** Ex-earn IV scan 20-30% faster than Greeks IV scan (measured runtime)

### Quality Gates
- **Q1:** Zero mixed logging formats in terminal output (100% `[SYMBOL] STATUS` format)
- **Q2:** CSV schema reduced from 40 → 32 columns (20% reduction)
- **Q3:** All external API calls wrapped in try/except (100% error handling coverage)

### Acceptance Criteria
- **A1:** `--iv-ex-earn` flag forces ex-earn IV, skips Greeks streaming
- **A2:** `--quiet` mode shows only summary, `--verbose` shows ALL symbols
- **A3:** `--log-file` writes all logs with timestamps to specified file
- **A4:** ATM calendars use unified `strike`, `delta`, `ff` columns (no `atm_*` columns)
- **A5:** Double calendars use unified `strike`, `delta`, `ff` for call leg, `put_*` for put leg
- **A6:** Migration guide tested with real v2.2 CSV files

## Estimated Effort

**Total Duration:** 9-12 days

**Breakdown by Phase:**
1. IV Source Control: 1 day
2. Bug Fixes & Error Handling: 2 days
3. CSV Schema Refactor: 2-3 days
4. Terminal Output & Logging: 3-4 days
5. Documentation & Testing: 1-2 days

**Critical Path:**
- Phase 2 (Bug Fixes) blocks Phase 5 (Testing) - must test large scans
- Phase 3 (CSV Refactor) blocks Phase 5 (Testing) - must test migration
- Phase 4 (Logging) is independent, can run parallel to Phase 3

**Resource Requirements:**
- 1 developer (full-time)
- Access to production tastytrade API
- Access to S&P 1500 symbol list for testing

**Key Assumptions:**
- Existing codebase is well-structured (single scanner file, modular functions)
- Python logging system is sufficient (no need for external logging libraries)
- CSV migration is one-time effort (users update parsers once)
[38;2;131;148;150m───────┬────────────────────────────────────────────────────────────────────────[0m
       [38;2;131;148;150m│ [0m[1mSTDIN[0m
[38;2;131;148;150m───────┼────────────────────────────────────────────────────────────────────────[0m
[38;2;131;148;150m   1[0m   [38;2;131;148;150m│[0m 
[38;2;131;148;150m   2[0m   [38;2;131;148;150m│[0m [38;2;248;248;242m## Tasks Created
- [ ] #36 - Add --iv-ex-earn Flag & IV Source Control
- [ ] #37 - Migrate CSV Schema from 40 to 32 Columns
- [ ] #38 - Add Professional Logging Infrastructure
- [ ] #39 - Add --output-mode CLI Flag
- [ ] #40 - Robust Error Handling for API Calls
- [ ] #41 - Memory-Efficient CSV Output
- [ ] #42 - Update Documentation for v2.3
- [ ] #43 - Integration Testing Suite
- [ ] #44 - CSV Backward Compatibility Tests
- [ ] #45 - High-Volume Scan Stress Test

Total tasks: 10
Parallel tasks: 10
Sequential tasks: 0

