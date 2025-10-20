---
name: output-csv-terminal-flags
description: Refactor CSV schema to eliminate redundancy and implement professional terminal output with logging and formatting improvements
status: backlog
created: 2025-10-20T10:58:10Z
---

# PRD: output-csv-terminal-flags

## Executive Summary

The Forward Factor scanner currently produces a 40-column CSV with redundant/confusing columns and outputs messy, inconsistent terminal logs that make daily scanning workflows difficult. This PRD addresses three core problems: (1) CSV schema redundancy between ATM and double calendar structures, (2) unprofessional terminal output with mixed logging formats, and (3) missing features for high-volume scanning (1000+ symbols). The solution will reduce CSV columns from 40 to ~30, implement structured logging with multiple output modes, fix critical bugs preventing large scans, and add missing IV source control.

**Impact:** Cleaner CSV files for analysis, professional terminal output for daily workflow, ability to scan 1000+ symbols without crashes, and user control over IV data source.

## Problem Statement

### What problem are we solving?

**Problem 1: CSV Schema Confusion (Redundancy & Empty Columns)**
- ATM calendars populate 8 `atm_*` columns but user points out "ATM is always EITHER a call OR a put" - the separate atm_* namespace is confusing when there are already `call_*` and `put_*` columns
- The `combined_ff` column is empty for ATM structures (line 1577 of scanner), populated for double structures - unclear when to use it vs `atm_ff` vs `min_ff`
- Multiple empty columns per structure: ATM rows leave 8 double-specific columns empty, double rows leave 8 ATM-specific columns empty
- Current schema: 40 columns with 16 columns always empty per row (depending on structure)

**Problem 2: Terminal Output Chaos**
Current terminal output mixes multiple logging formats without structure:
```
2025-10-20 02:45:43,720 - __main__ - WARNING - ABT 30DTE: Greeks IV missing for call, using ex-earn fallback
2025-10-20 02:36:23,117 - yfinance - ERROR - HTTP Error 404: {"quoteSummary":{"result":null,"error":...}}}
[INFO] JEPI: No earnings data available from any source (no earnings to avoid)
[FILTERED] FUL: Liquidity rating 2 < 3
[WARN] Could not get market data for GEFB: No data present in response: {}, skipping.
```

Issues:
- Mixed logging formats: Python logger timestamps, bracketed prefixes ([INFO], [FILTERED], [WARN])
- Verbose yfinance HTTP 404 errors with full JSON dumps (not graceful)
- No consistent spacing or structure
- No single-line summary per symbol (user request: "one line, concise, good formatting")
- No verbose mode to show ALL symbols (currently only shows errors/warnings/passed opportunities)

**Problem 3: High-Volume Scanning Bug**
Scanner crashes when scanning 1000+ symbols:
```
pydantic_core._pydantic_core.ValidationError: 1 validation error for NestedOptionChain
expirations.1.strikes
  Field required [type=missing, input_value={'expiration-type': 'Regu...'settlement-type': 'PM'}, input_type=dict]
```
Root cause: tastytrade API sometimes returns expirations without 'strikes' field, causing Pydantic validation failure in SDK's `NestedOptionChain.get()`.

**Problem 4: Missing IV Source Control**
User wants ability to override default Greeks IV and force ex-earn IV usage via CLI flag (currently no such flag exists).

### Why is this important now?

1. **Daily workflow friction:** User scans daily for trading opportunities - messy terminal output slows decision-making
2. **CSV analysis confusion:** Redundant columns make it unclear which columns to use for filtering/analysis
3. **Scalability blocker:** Cannot scan 1000+ symbols without crashes (critical for universe-wide scans)
4. **Data source control:** User needs ability to test ex-earn IV vs Greeks IV for strategy validation

## User Stories

### Primary Personas

**Persona 1: Active Trader (Daily Scanner User)**
- Runs pre-market scans every morning (5-10 scans/day)
- Wants minimal, clean terminal output to quickly identify opportunities
- Exports CSV to spreadsheet for deeper analysis
- Needs real-time feedback as scan progresses (100-500 symbols)

**Persona 2: Quant Researcher (Bulk Scanner User)**
- Runs universe-wide scans (1000+ symbols) for backtesting
- Needs reliable scanning without crashes
- Wants verbose logging for debugging data quality issues
- Requires CSV with clear, non-redundant columns for pandas analysis

**Persona 3: Strategy Developer (IV Source Tester)**
- Testing whether ex-earn IV or Greeks IV produces better signals
- Needs ability to switch IV sources via CLI flag
- Wants to compare results side-by-side (run scan twice with different flags)

### Detailed User Journeys

**Journey 1: Pre-Market Daily Scan (Active Trader)**
1. User runs scan with 50 symbols, 3 DTE pairs (150 opportunities max)
2. **Current experience:** Terminal floods with mixed log formats, yfinance 404 errors, inconsistent spacing
3. **Desired experience:** Clean one-line output per symbol showing: symbol, status (pass/filter/error), key metrics if passed (FF, strikes, expirations)
4. **Outcome:** User quickly identifies top 5 opportunities, exports CSV for detailed review

**Journey 2: Universe Scan (Quant Researcher)**
1. User runs scan with 1500 symbols from S&P 1500 index
2. **Current experience:** Scanner crashes after ~800 symbols with Pydantic validation error
3. **Desired experience:** Scanner handles missing 'strikes' field gracefully, continues scanning remaining symbols, outputs verbose logs showing exactly which symbols failed and why
4. **Outcome:** Complete scan results in CSV, detailed log file for debugging data quality

**Journey 3: IV Source Comparison (Strategy Developer)**
1. User wants to test if ex-earn IV produces more stable FF calculations
2. **Current experience:** No way to force ex-earn IV (scanner always uses Greeks IV as primary)
3. **Desired experience:** Run scan with `--iv-ex-earn` flag to override Greeks IV, compare CSV outputs side-by-side
4. **Outcome:** Clear comparison showing which IV source produces better signal-to-noise ratio

### Pain Points Being Addressed

1. **CSV confusion:** "Which column do I filter on? `atm_ff`, `combined_ff`, or `min_ff`?"
2. **Terminal chaos:** "I can't quickly see which symbols passed - too much noise"
3. **Scan crashes:** "I have to manually split my symbol list into batches to avoid crashes"
4. **No IV control:** "I can't test my hypothesis about ex-earn IV vs Greeks IV"
5. **yfinance spam:** "HTTP 404 errors dump entire JSON response - I don't need to see that"
6. **No progress visibility:** "I want to know scan progress without verbose logging every symbol"

## Requirements

### Functional Requirements

#### FR1: CSV Schema Refactor (Eliminate Redundancy)

**FR1.1: Unified Strike/Delta/FF Columns**
- Remove separate `atm_*` namespace (8 columns eliminated)
- Use unified columns for both structures:
  - `strike` (ATM structure: single strike, double structure: call strike)
  - `put_strike` (ATM: empty, double: put strike)
  - `delta` (ATM: 50Δ delta, double: call delta)
  - `put_delta` (ATM: empty, double: put delta)
  - `ff` (ATM: single FF, double: call FF)
  - `put_ff` (ATM: empty, double: put FF)
  - `min_ff` (ATM: same as `ff`, double: min of call/put)
- **Acceptance Criteria:**
  - ATM rows populate: `strike`, `delta`, `ff`, `min_ff` (4 columns)
  - Double rows populate: `strike`, `put_strike`, `delta`, `put_delta`, `ff`, `put_ff`, `min_ff` (7 columns)
  - Column count reduced from 40 to ~32

**FR1.2: Resolve combined_ff Ambiguity**
Based on code analysis:
- `combined_ff` = average of (call_ff, put_ff) for double calendars
- Used as secondary sorting metric (line 1608: `key=lambda r: (-r["min_ff"], -r["combined_ff"], r["symbol"])`)
- Empty for ATM structures

**Decision needed:** Keep or remove?
- **Option A (Remove):** Eliminate `combined_ff` entirely, use only `min_ff` for filtering/sorting (more conservative, both wings must pass)
- **Option B (Keep):** Keep for secondary sorting/ranking, clearly document usage in CLAUDE.md
- **Recommendation:** Option B - keep for double calendars as ranking metric after min_ff filtering

**FR1.3: Populate Empty IV Columns**
Current empty columns (user complaint):
- `call_fwd_iv`, `put_front_iv`, `put_back_iv`, `put_fwd_iv`

Investigation needed: Are these genuinely unused or is there a bug?
- Check if these should contain calculated forward IVs for each leg
- If truly unused, remove from schema

**FR1.4: Column Reordering (Trading-Focused Layout)**
User request: "Move FF values and expiration dates/strikes closer to right for trade placement"

New column order (left to right):
1. **Metadata:** `timestamp`, `symbol`, `structure`, `spot_price`
2. **Expiration/Strikes (Trading Info):** `front_dte`, `back_dte`, `front_expiry`, `back_expiry`, `strike`, `put_strike`, `delta`, `put_delta`
3. **FF Metrics (Decision Criteria):** `ff`, `put_ff`, `min_ff`, `combined_ff`
4. **IV Detail:** `call_front_iv`, `call_back_iv`, `call_fwd_iv`, `put_front_iv`, `put_back_iv`, `put_fwd_iv`, `iv_source_call_front`, `iv_source_call_back`, `iv_source_put_front`, `iv_source_put_back`
5. **Quality Filters:** `earnings_conflict`, `earnings_date`, `option_volume_today`, `liq_rating`, `earnings_source`, `skip_reason`

**Acceptance Criteria:**
- FF columns grouped together on right side of CSV
- Strike/expiry columns grouped together before FF columns
- Easy to scan visually: symbol → strikes/expirations → FF → filter reasons

#### FR2: Terminal Output Improvements

**FR2.1: Structured Logging System**
Replace mixed logging formats with unified Python logging:
- **Logger hierarchy:**
  - `scanner` (main logger): scan progress, summary stats
  - `scanner.earnings` (sub-logger): earnings cache/fetch events
  - `scanner.market_data` (sub-logger): market data fetch events
  - `scanner.greeks` (sub-logger): Greeks IV fetch events
  - `scanner.quality` (sub-logger): filtering events (liquidity, earnings, delta)
- **Log levels:**
  - `DEBUG`: Detailed data fetching (IV values, delta calculations, API responses)
  - `INFO`: Per-symbol progress (passed/filtered status, one-line summary)
  - `WARNING`: Graceful degradation (fallback to ex-earn IV, missing data)
  - `ERROR`: Hard failures (API errors, validation errors, crashes)

**FR2.2: Output Modes (CLI Flags)**
Implement multiple terminal output modes:

**Mode 1: Quiet (--quiet)**
- Suppress all output except final summary and errors
- Use case: Automated workflows, CSV-only output
- Output: "Scan complete: 150 scanned, 23 passed, 127 filtered (82s)"

**Mode 2: Normal (default, no flag)**
- One-line summary per symbol (user request: "concise, one line, good formatting")
- Real-time output as symbols complete
- Format: `[SYMBOL] STATUS: key_info` with consistent spacing
- Examples:
  ```
  [SPY   ] PASS: FF=0.285 (30-60 DTE, strike=450.0, double)
  [QQQ   ] FILTER: earnings_conflict (2025-11-15 within back expiry)
  [AAPL  ] FILTER: volume_too_low (3.2k < 10k)
  [META  ] ERROR: no_market_data (API timeout)
  ```

**Mode 3: Verbose (--verbose)**
- Show ALL symbols (user request: "verbose terminal output so ALL symbols have a line printed")
- Include symbols that pass, fail, and are skipped
- Additional details: delta values, IV sources, expiration dates
- Examples:
  ```
  [SPY   ] PASS: FF=0.285 (call=0.29, put=0.28), 30-60 DTE (2025-11-19→2025-12-19), strike=450.0/445.0 (double)
  [QQQ   ] FILTER: earnings_conflict (2025-11-15 within back expiry 2026-01-16)
  [AAPL  ] FILTER: volume_too_low (3.2k < 10k threshold, liq_rating=2)
  [TSLA  ] SKIP: delta_not_found (no strikes within ±5Δ of ±35Δ target)
  [META  ] ERROR: no_market_data (tastytrade API timeout after 3s)
  [NVDA  ] PASS: FF=0.215 (60-90 DTE, strike=880.0, atm-call, iv_source=greeks)
  ```

**Mode 4: Debug (--debug)**
- Existing debug mode, adds verbose data fetching logs
- Use case: Troubleshooting API issues, IV calculation debugging

**FR2.3: Graceful yfinance Error Handling**
User complaint: "print yfinance HTTP Error 404 messages gracefully/minimally"

Current output:
```
2025-10-20 02:36:23,117 - yfinance - ERROR - HTTP Error 404: {"quoteSummary":{"result":null,"error":{"code":"Not Found","description":"No fundamentals data found for symbol: JEPI"}}}
```

Desired output:
```
[JEPI  ] INFO: No earnings data from yfinance (404), checking tastytrade...
```

**Implementation:**
- Suppress yfinance logger at WARNING level (allow only ERROR)
- Catch yfinance exceptions, log concisely via scanner.earnings logger
- Extract symbol from exception, format as one-line message

**FR2.4: Consistent Message Formatting**
User complaint: "clean up horrendous terminal output"

**Standards:**
- **Symbol padding:** Left-align symbols with fixed width (6 chars: `[SPY   ]`)
- **Status keywords:** Uppercase, fixed width (8 chars: `PASS    `, `FILTER  `, `ERROR   `, `SKIP    `, `INFO    `)
- **No timestamps in normal mode:** Timestamps only in debug/log files
- **Color coding (optional future enhancement):** Green=PASS, Yellow=FILTER, Red=ERROR, Blue=INFO

**FR2.5: Logging to File (--log-file)**
User request: "implement logging (tee)"

**Implementation:**
- Add `--log-file <path>` flag to write logs to file
- File receives ALL log levels (DEBUG and above)
- Terminal receives filtered logs based on mode (--quiet, normal, --verbose, --debug)
- Format: Same as terminal output but with timestamps prepended
- Use case: Archive scan results, debugging data quality issues

**Acceptance Criteria:**
- `--log-file scan.log` writes all logs to file
- Terminal output remains clean (no timestamps unless --debug)
- Log file includes timestamps, all log levels, raw API responses

#### FR3: High-Volume Scanning Bug Fix

**FR3.1: Handle Missing 'strikes' Field**
Current crash:
```
pydantic_core._pydantic_core.ValidationError: 1 validation error for NestedOptionChain
expirations.1.strikes
  Field required [type=missing, input_value={'expiration-type': 'Regu...'settlement-type': 'PM'}, input_type=dict]
```

**Root cause:** tastytrade API returns some expirations without 'strikes' field (likely illiquid/expired expirations)

**Solution:**
- Wrap `NestedOptionChain.get()` in try/except to catch Pydantic validation errors
- Log warning: `[SYMBOL] WARN: Invalid option chain data (missing strikes for expiration X), skipping symbol`
- Add skip reason: `SKIP_INVALID_CHAIN = "invalid_chain_data"`
- Continue to next symbol instead of crashing

**FR3.2: Graceful Degradation for API Failures**
Ensure all external API calls have proper error handling:
- `get_market_data()` → catch exceptions, skip symbol
- `NestedOptionChain.get()` → catch Pydantic errors, skip symbol
- `snapshot_greeks()` → timeout already handled, ensure no crashes
- `yfinance` earnings fetch → already handled via multi-source pipeline

**Acceptance Criteria:**
- Scan 1500+ symbols without crashes
- Invalid symbols logged clearly in `skip_stats` dict
- CSV output includes `skip_reason` column for debugging

#### FR4: IV Source Control

**FR4.1: Add --iv-ex-earn Flag**
User request: "add flag --iv-ex-earn that overrides the default greeks-based IV and uses ex-earn IV instead"

**Current behavior:**
- Scanner uses Greeks IV as primary (line 1270: "Use Greeks IV as primary")
- Falls back to ex-earn IV only if Greeks missing (line 1271: "Fallback to ex-earn IV only if Greeks data is missing")

**New behavior with --iv-ex-earn:**
- Force ex-earn IV as primary source
- Skip Greeks IV fetching entirely (performance optimization)
- Update `iv_source_*` columns to show "exearn_primary" instead of "greeks"

**Implementation:**
- Add `--iv-ex-earn` boolean flag to argparse
- Pass flag to `scan()` function
- Modify IV fetch logic to check flag before calling `snapshot_greeks()`
- Update CSV `iv_source` columns to distinguish "greeks" vs "exearn_primary" vs "exearn_fallback"

**Acceptance Criteria:**
- `--iv-ex-earn` flag forces ex-earn IV for all symbols
- Scan completes faster (no Greeks streaming overhead)
- CSV `iv_source` columns show "exearn_primary"
- Documentation updated with flag usage

### Non-Functional Requirements

#### NFR1: Performance
- Large scans (1000+ symbols) complete without crashes
- Logging overhead minimal (<5% performance impact vs no logging)
- CSV writing optimized (batch write, not per-row)

#### NFR2: Usability
- Terminal output readable at a glance (consistent formatting, spacing)
- CSV column order intuitive for trading workflow (strikes/expirations → FF → filters)
- CLI flags follow argparse conventions (--kebab-case)

#### NFR3: Maintainability
- Logging hierarchy modular (easy to add new sub-loggers)
- CSV schema documented in CLAUDE.md (column order, purpose, structure-specific fields)
- Error handling centralized (consistent try/except patterns)

#### NFR4: Backward Compatibility
- CSV schema v3.0 (breaking change from v2.2)
- Provide migration guide in CLAUDE.md (column mapping table)
- Existing CSV parsers break gracefully (clear error message if expecting 40 columns)

## Success Criteria

### Measurable Outcomes

**S1: CSV Schema Improvement**
- Column count reduced from 40 to ≤32 (20% reduction)
- Zero empty columns per row (currently 16 empty columns per row depending on structure)
- User can identify tradable opportunity in <5 seconds of CSV review

**S2: Terminal Output Quality**
- 100% of log messages follow consistent format (`[SYMBOL] STATUS: details`)
- Zero mixed logging formats (no more raw logger timestamps mixed with bracketed prefixes)
- User can scan 100 symbols and identify passed opportunities without scrolling (fit in single terminal screen)

**S3: Scan Reliability**
- 0 crashes when scanning 1500 symbols (S&P 1500 index)
- 100% of API errors handled gracefully (no uncaught exceptions)
- `skip_reason` column populated for all filtered symbols

**S4: IV Source Control**
- User can run identical scan with `--iv-ex-earn` flag and compare results
- Ex-earn IV scan completes 20-30% faster (no Greeks streaming overhead)

### Key Metrics and KPIs

**KPI 1: User Workflow Efficiency**
- Time to identify top 5 opportunities: <30 seconds (from scan start to decision)
- Terminal scrollback required: 0 screens (all info visible in single view)

**KPI 2: Scan Success Rate**
- Successful scan completion rate: 100% for any symbol list size
- API error recovery rate: 100% (no crashes, all errors logged)

**KPI 3: CSV Usability**
- Column redundancy: 0% (no duplicate/empty columns per structure)
- Time to locate trade info (strikes/FF): <5 seconds per row

## Constraints & Assumptions

### Constraints

**C1: Backward Compatibility**
- CSV schema v3.0 breaks existing parsers (users must update scripts)
- Migration guide required (column mapping table in CLAUDE.md)

**C2: External API Limitations**
- tastytrade API may return invalid data (missing 'strikes' field) - cannot fix upstream
- yfinance API may return 404 for valid symbols - graceful degradation required

**C3: Python Logging System**
- Cannot suppress yfinance logger entirely (used by other libraries)
- Must configure yfinance logger level, not remove it

### Assumptions

**A1: User Environment**
- User runs scanner from terminal (not GUI)
- User has write access to log file directory

**A2: Data Availability**
- Ex-earn IV available from tastytrade Market Metrics API for most liquid symbols
- Greeks IV available from dxFeed for most liquid symbols during market hours

**A3: User Workflow**
- User exports CSV to Excel/pandas for deeper analysis
- User reviews terminal output in real-time during scan
- User may run same scan multiple times with different flags for comparison

## Out of Scope

### Explicitly NOT Building

**OS1: Interactive Terminal UI**
- No ncurses/blessed progress bars or interactive menus
- Rationale: CLI-focused workflow, user wants simple text output

**OS2: Real-Time Streaming Updates**
- No live-updating terminal display (like `top` command)
- Rationale: Scans complete in <2 minutes for typical workflows, streaming overhead not justified

**OS3: CSV Column Customization**
- No `--columns` flag to select subset of columns
- Rationale: User can filter columns post-export in Excel/pandas, not needed in scanner

**OS4: Multiple CSV Outputs**
- No separate ATM-only and double-only CSV files
- Rationale: Single CSV with `structure` column sufficient, user can filter in analysis

**OS5: Color Output Customization**
- No `--no-color` or `--color-scheme` flags (future enhancement)
- Rationale: Keep initial implementation simple, add later if requested

**OS6: Log File Rotation**
- No automatic log rotation/compression (future enhancement)
- Rationale: User can manage log files manually for now

## Dependencies

### External Dependencies

**D1: tastytrade SDK**
- Required: `tastytrade>=7.0` (Pydantic v2 support)
- Risk: SDK changes may break error handling
- Mitigation: Pin SDK version in requirements.txt

**D2: yfinance Library**
- Required: `yfinance>=0.2.0` for earnings fetching
- Risk: HTTP 404 errors unpredictable
- Mitigation: Multi-source earnings pipeline already handles failures

### Internal Dependencies

**D3: Earnings Cache Module**
- Required: `earnings_cache.py` must support new logging system
- Risk: None (internal module, full control)

**D4: CLAUDE.md Documentation**
- Required: Update CSV schema documentation, migration guide, CLI flag reference
- Risk: None (documentation, not code)

### Timeline Dependencies

**D5: Testing with Real Data**
- Required: Access to production tastytrade API during market hours
- Risk: Testing limited by market hours (9:30am-4pm ET)
- Mitigation: Use recorded test fixtures for off-hours development

## Implementation Roadmap

**Priority Order (User-Specified):**
1. IV Source Control
2. Bug Fixes & Error Handling
3. CSV Schema Refactor
4. Terminal Output & Logging
5. Documentation & Testing

### Phase 1: IV Source Control (HIGHEST PRIORITY)
**Duration:** 1 day
**Tasks:**
1. Add --iv-ex-earn flag to argparse
2. Modify IV fetch logic to check flag
3. Update iv_source columns to show "exearn_primary" vs "greeks"
4. Test performance improvement (skip Greeks streaming)
5. Document flag in CLAUDE.md and README_TT.md

**Acceptance:**
- [ ] --iv-ex-earn flag forces ex-earn IV
- [ ] CSV iv_source columns updated
- [ ] Performance improvement measurable (20-30% faster)
- [ ] Documentation complete

### Phase 2: Bug Fixes & Error Handling
**Duration:** 2 days
**Tasks:**
1. Wrap NestedOptionChain.get() in try/except for Pydantic errors
2. Add SKIP_INVALID_CHAIN skip reason
3. Test with 1500+ symbol list (S&P 1500)
4. Ensure all API calls have error handling
5. Update skip_stats dict to track all skip reasons

**Acceptance:**
- [ ] 1500-symbol scan completes without crashes
- [ ] Invalid chains logged clearly
- [ ] skip_reason column populated for all filtered symbols

### Phase 3: CSV Schema Refactor (Breaking Change)
**Duration:** 2-3 days
**Tasks:**
1. Design new unified column schema (eliminate `atm_*` namespace)
2. Update `scan()` function to populate new columns
3. Test ATM and double structures separately
4. Update CLAUDE.md with v3.0 schema and migration guide
5. Version bump in code comments/docstrings

**Acceptance:**
- [ ] Column count ≤32
- [ ] Zero empty columns per row
- [ ] CSV header matches new schema exactly
- [ ] Migration guide published in CLAUDE.md

### Phase 4: Terminal Output & Logging
**Duration:** 3-4 days
**Tasks:**
1. Implement logging hierarchy (scanner, scanner.earnings, scanner.market_data, scanner.greeks, scanner.quality)
2. Add output mode flags (--quiet, --verbose, --debug)
3. Implement consistent message formatting ([SYMBOL] STATUS: details)
4. Add --log-file flag with timestamp support
5. Suppress/handle yfinance logger gracefully
6. Update all print() statements to use logger

**Acceptance:**
- [ ] All log messages follow [SYMBOL] STATUS format
- [ ] --quiet mode suppresses per-symbol output
- [ ] --verbose mode shows ALL symbols (100% coverage)
- [ ] --log-file writes all logs with timestamps
- [ ] Zero mixed logging formats in terminal

### Phase 5: Documentation & Testing
**Duration:** 1-2 days
**Tasks:**
1. Update CLAUDE.md (CSV schema v3.0, migration guide, CLI flags)
2. Update README_TT.md (new flags, output modes, examples)
3. Create test fixtures for all output modes
4. Test migration from v2.2 to v3.0 CSV
5. Test all combinations of flags (--verbose + --log-file, --quiet + --csv-out, etc.)

**Acceptance:**
- [ ] All docs updated
- [ ] Migration guide tested with real v2.2 CSV
- [ ] All flag combinations work correctly

## Appendices

### Appendix A: Proposed CSV Schema v3.0 (32 Columns)

**Column Order (Trading-Focused Layout):**

| # | Column | Type | ATM | Double | Description |
|---|--------|------|-----|--------|-------------|
| 1 | timestamp | ISO 8601 | ✓ | ✓ | Scan time (UTC) |
| 2 | symbol | string | ✓ | ✓ | Ticker symbol |
| 3 | structure | string | ✓ | ✓ | "atm-call" or "double" |
| 4 | spot_price | float | ✓ | ✓ | Current underlying price |
| 5 | front_dte | int | ✓ | ✓ | Days to front expiration |
| 6 | back_dte | int | ✓ | ✓ | Days to back expiration |
| 7 | front_expiry | date | ✓ | ✓ | Front expiration date |
| 8 | back_expiry | date | ✓ | ✓ | Back expiration date |
| 9 | strike | float | ✓ | ✓ | ATM: 50Δ strike, Double: call strike |
| 10 | put_strike | float | empty | ✓ | Double: -35Δ put strike |
| 11 | delta | float | ✓ | ✓ | ATM: 50Δ delta, Double: call delta |
| 12 | put_delta | float | empty | ✓ | Double: put delta |
| 13 | ff | float | ✓ | ✓ | ATM: single FF, Double: call FF |
| 14 | put_ff | float | empty | ✓ | Double: put FF |
| 15 | min_ff | float | ✓ | ✓ | ATM: same as ff, Double: min(ff, put_ff) |
| 16 | combined_ff | float | empty | ✓ | Double: avg(ff, put_ff) for ranking |
| 17 | call_front_iv | float | ✓ | ✓ | Front call IV |
| 18 | call_back_iv | float | ✓ | ✓ | Back call IV |
| 19 | call_fwd_iv | float | ✓ | ✓ | Forward call IV |
| 20 | put_front_iv | float | ✓ | ✓ | Front put IV |
| 21 | put_back_iv | float | ✓ | ✓ | Back put IV |
| 22 | put_fwd_iv | float | ✓ | ✓ | Forward put IV |
| 23 | iv_source_call_front | string | ✓ | ✓ | "greeks", "exearn_primary", or "exearn_fallback" |
| 24 | iv_source_call_back | string | ✓ | ✓ | IV source for back call |
| 25 | iv_source_put_front | string | ✓ | ✓ | IV source for front put |
| 26 | iv_source_put_back | string | ✓ | ✓ | IV source for back put |
| 27 | earnings_conflict | string | ✓ | ✓ | "yes" or "no" |
| 28 | earnings_date | date | ✓ | ✓ | Next earnings date |
| 29 | option_volume_today | int | ✓ | ✓ | Today's option chain volume |
| 30 | liq_rating | int | ✓ | ✓ | Liquidity rating 0-5 |
| 31 | earnings_source | string | ✓ | ✓ | "cache", "yahoo", "tastytrade", "none" |
| 32 | skip_reason | string | ✓ | ✓ | Reason filtered (empty if passed) |

**Changes from v2.2:**
- Removed: `atm_strike`, `atm_delta`, `atm_ff`, `atm_iv_front`, `atm_iv_back`, `atm_fwd_iv`, `atm_iv_source_front`, `atm_iv_source_back` (8 columns)
- Renamed: `call_strike` → `strike` (unified namespace)
- Renamed: `call_delta` → `delta` (unified namespace)
- Renamed: `call_ff` → `ff` (unified namespace)
- Total: 40 → 32 columns (20% reduction)

### Appendix B: Terminal Output Examples

**Normal Mode (Default):**
```
[SPY   ] PASS: FF=0.285 (30-60 DTE, strike=450.0, double)
[QQQ   ] FILTER: earnings_conflict (2025-11-15)
[AAPL  ] FILTER: volume_too_low (3.2k < 10k)
[TSLA  ] PASS: FF=0.235 (60-90 DTE, strike=880.0, atm-call)
[META  ] ERROR: no_market_data (API timeout)

Scan complete: 5 scanned, 2 passed, 2 filtered, 1 error (3.2s)
```

**Verbose Mode (--verbose):**
```
[SPY   ] PASS: FF=0.285 (call=0.29, put=0.28), 30-60 DTE (2025-11-19→2025-12-19), strike=450.0/445.0 (double), iv_source=greeks
[QQQ   ] FILTER: earnings_conflict (2025-11-15 within back expiry 2026-01-16)
[AAPL  ] FILTER: volume_too_low (3.2k < 10k threshold, liq_rating=2)
[TSLA  ] PASS: FF=0.235 (60-90 DTE, 2025-12-19→2026-01-16), strike=880.0 (atm-call, delta=0.51), iv_source=greeks
[META  ] ERROR: no_market_data (tastytrade API timeout after 3s)

Scan complete: 5 scanned, 2 passed, 2 filtered, 1 error (3.2s)
```

**Quiet Mode (--quiet):**
```
Scan complete: 5 scanned, 2 passed, 2 filtered, 1 error (3.2s)
```

### Appendix C: Migration Guide v2.2 → v3.0

**For CSV Parsers (Python/pandas):**

```python
# v2.2 parser (40 columns)
df = pd.read_csv("scan_v2.2.csv")
atm_opps = df[df["structure"] == "atm-call"]
atm_opps = atm_opps[atm_opps["atm_ff"] >= 0.23]  # OLD: atm_ff column

double_opps = df[df["structure"] == "double"]
double_opps = double_opps[double_opps["min_ff"] >= 0.20]

# v3.0 parser (32 columns)
df = pd.read_csv("scan_v3.0.csv")
atm_opps = df[df["structure"] == "atm-call"]
atm_opps = atm_opps[atm_opps["ff"] >= 0.23]  # NEW: unified ff column

double_opps = df[df["structure"] == "double"]
double_opps = double_opps[double_opps["min_ff"] >= 0.20]  # UNCHANGED
```

**Column Mapping Table:**

| v2.2 Column | v3.0 Column | Notes |
|-------------|-------------|-------|
| `atm_strike` | `strike` | Unified namespace (ATM uses `strike`) |
| `atm_delta` | `delta` | Unified namespace (ATM uses `delta`) |
| `atm_ff` | `ff` | Unified namespace (ATM uses `ff`) |
| `atm_iv_front` | `call_front_iv` | ATM uses same IV columns as double |
| `atm_iv_back` | `call_back_iv` | ATM uses same IV columns as double |
| `atm_fwd_iv` | `call_fwd_iv` | ATM uses same IV columns as double |
| `atm_iv_source_front` | `iv_source_call_front` | Unified IV source tracking |
| `atm_iv_source_back` | `iv_source_call_back` | Unified IV source tracking |
| `call_strike` | `strike` | Renamed for unified namespace (double uses `strike` for call strike) |
| `call_delta` | `delta` | Renamed for unified namespace (double uses `delta` for call delta) |
| `call_ff` | `ff` | Renamed for unified namespace (double uses `ff` for call FF) |
| `put_strike` | `put_strike` | UNCHANGED |
| `put_delta` | `put_delta` | UNCHANGED |
| `put_ff` | `put_ff` | UNCHANGED |
| `min_ff` | `min_ff` | UNCHANGED |
| `combined_ff` | `combined_ff` | UNCHANGED (kept for double structure ranking) |

---

## Next Steps

After PRD approval, create implementation epic using:
```bash
/pm:prd-parse output-csv-terminal-flags
```

This will break down the PRD into actionable tasks with estimates and dependencies.
