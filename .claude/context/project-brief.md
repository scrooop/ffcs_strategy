---
created: 2025-10-20T18:58:52Z
last_updated: 2025-10-20T18:58:52Z
version: 1.0
author: Claude Code PM System
---

# Project Brief

## What It Is

**FFCS Strategy** (Forward Factor Calendar Spread) is a Python CLI scanner that identifies mispriced forward volatility opportunities in options markets. It analyzes implied volatility term structure across multiple expirations and calculates a "Forward Factor" (FF) to detect when front-month options are overpriced relative to forward-dated options - creating profitable calendar spread setups.

## Why It Exists

### The Problem
Options traders face several challenges when hunting for calendar spread opportunities:

1. **Manual IV Analysis is Slow**
   - Checking 50+ symbols manually takes hours
   - Term structure comparison across multiple DTEs is tedious
   - Easy to miss opportunities during market hours

2. **Existing Tools are Limited**
   - TastyTrade shows IV rank/percentile (single expiration), not forward IV
   - No tools calculate Forward Factor (FF = (σ₁ - σ_fwd) / σ_fwd)
   - Manual Excel work required for multi-symbol analysis

3. **Quality Filtering is Manual**
   - Must manually check earnings calendars (avoid gamma risk)
   - Need to verify liquidity and volume (avoid wide spreads)
   - Strike selection requires delta calculation or guesswork

4. **Data Accuracy Issues**
   - Some tools use price-based ATM strikes (inaccurate)
   - Ex-earn IV often unavailable or expensive
   - Volume proxies (like liquidity_value) are inconsistent

### The Solution
Automated scanner that:
- Calculates forward IV and FF ratio for multiple symbols in minutes
- Pre-filters earnings conflicts (80-95% faster with caching)
- Selects strikes by delta (50Δ ATM, ±35Δ double calendars)
- Uses Greeks IV (strike-level precision) with ex-earn fallback
- Outputs actionable CSV/JSON with quality metadata

## Core Objectives

### Primary Goals
1. **Find High-FF Opportunities Fast**
   - Scan 50-100 symbols in < 2 minutes
   - Identify FF ≥ 0.20-0.23 (profitable threshold)
   - Support both ATM and double calendar structures

2. **Ensure Trade Quality**
   - Filter out earnings conflicts (avoid undefined risk)
   - Check liquidity (rating ≥ 3 or volume ≥ 10k)
   - Validate strike availability (delta within tolerance)

3. **Provide Actionable Output**
   - CSV format for Excel analysis
   - Sorted by FF (highest opportunities first)
   - Include all metadata (IVs, strikes, deltas, skip reasons)

### Secondary Goals
1. **Performance Optimization**
   - Fast earnings cache (80-95% speedup on rescans)
   - Streaming CSV writer for 1500+ symbol scans
   - Efficient API usage (batch fetching, early rejection)

2. **Flexibility**
   - Support equities and futures options
   - Configurable thresholds (FF, DTE, delta tolerance)
   - Multiple output modes (CSV, JSON)

3. **Data Quality**
   - Multi-source earnings data (cache → yahoo → tastytrade)
   - Greeks IV primary (strike-level), ex-earn IV fallback
   - Transparent data provenance tracking

## Success Criteria

### Technical Success
- ✅ Accurate FF calculation (variance decomposition)
- ✅ < 2 minute scan time for 100 symbols (with cache)
- ✅ > 90% earnings cache hit rate (daily scanning)
- ✅ > 95% Greeks IV coverage (primary source)
- ✅ 40-column CSV schema (v2.2, consolidating to 32 in v2.3)
- ✅ Support for 1500+ symbol scans (streaming writer)

### User Success
- ✅ Trader can scan watchlist in < 2 minutes pre-market
- ✅ Top 5-10 opportunities clearly ranked by FF
- ✅ No manual earnings calendar checking required
- ✅ Both ATM and double calendar structures available
- ✅ Futures options supported (/ES, /NQ, /CL, etc.)

### Business Success
- Open source CLI tool (personal use, no monetization)
- Educational value (demonstrates forward volatility concepts)
- Potential for integration with TastyTrade auto-execution (future)

## Scope

### In Scope
1. **Forward IV Calculation**
   - Variance decomposition formula
   - Multiple DTE pairs (30-60, 30-90, 60-90)
   - ATM and double calendar structures

2. **Quality Filtering**
   - Earnings conflict detection (multi-source pipeline)
   - Liquidity screening (rating or volume)
   - Strike availability validation (delta tolerance)

3. **Data Integration**
   - TastyTrade API (option chains, Greeks, market metrics)
   - dxFeed streaming (real-time IV and delta)
   - Yahoo Finance (earnings, futures prices)

4. **Output Formats**
   - CSV (40 columns v2.2, reducing to 32 in v2.3)
   - JSON (nested structure)
   - Console output (summary)

5. **Supported Assets**
   - US equity options (SPY, AAPL, TSLA, etc.)
   - US futures options (/ES, /NQ, /RTY, /CL, /GC, etc.)

### Out of Scope (Current Version)
1. **Order Execution**
   - No automated order placement
   - No position tracking
   - Manual trade entry on TastyTrade platform

2. **Historical Analysis**
   - No backtesting framework
   - No historical FF data storage
   - No performance tracking

3. **Real-Time Monitoring**
   - No live alerts or notifications
   - No intraday FF updates
   - One-time scans only (no continuous monitoring)

4. **Web Interface**
   - CLI only (no GUI)
   - No web dashboard
   - No mobile app

5. **Other Strategies**
   - Calendars only (no strangles, iron condors, butterflies)
   - No earnings plays (explicitly filtered out)
   - No directional strategies

## Key Constraints

### Technical Constraints
1. **API Dependencies**
   - Requires TastyTrade production account (live Greeks data)
   - Yahoo Finance public API (no authentication)
   - No official API rate limits documented (respectful usage)

2. **Market Hours**
   - Precise volume filtering requires market hours
   - Default liquidity rating works 24/7
   - Greeks data quality lower outside market hours

3. **Python 3.14 Bug**
   - Asyncio recursion issue in task cancellation
   - Workaround: Increased recursion limit (10,000)
   - Stable until Python 3.14.1+ fixes upstream

### Business Constraints
1. **Personal Use**
   - Not intended for redistribution or commercial use
   - No support or warranties
   - Open source for learning purposes

2. **Data Licensing**
   - TastyTrade data subject to their terms of service
   - Yahoo Finance data for personal use only
   - No data redistribution

### Operational Constraints
1. **Manual Execution**
   - No scheduled jobs or automation (yet)
   - User runs scanner when needed
   - No cloud hosting (local CLI only)

2. **Performance Limits**
   - Large scans (1500+ symbols) take 30-60 minutes
   - Greeks timeout may miss some strikes (3s default)
   - Earnings cache reduces but doesn't eliminate API calls

## Project Timeline

### Version History
- **v1.0** (July 2025) - Initial release (ATM only, 25 columns)
- **v2.0** (August 2025) - Quality filtering + double calendars (31 columns)
- **v2.1** (September 2025) - Fast earnings cache (80-95% speedup)
- **v2.2** (October 2025) - Core calculation corrections (40 columns)
- **v2.3** (In Progress) - CSV consolidation + logging (32 columns)

### Current Status
- **Version:** 2.2 (stable)
- **Next Release:** 2.3 (20% complete - 2/10 tasks done)
- **Active Work:** Output CSV terminal flags epic

## Stakeholders

### Primary Stakeholder
- **Project Owner:** Personal project (wnv72)
- **Role:** Developer, tester, primary user

### Secondary Stakeholders
- **Active Options Traders** - Daily scan users
- **Algorithmic Traders** - CSV parsing for automation
- **Strategy Researchers** - Studying forward volatility patterns

## Dependencies

### External Dependencies
1. **TastyTrade Platform**
   - Production account required
   - Option approval level needed
   - API stability (no official SLA)

2. **Market Data Providers**
   - dxFeed (via TastyTrade)
   - Yahoo Finance
   - Market hours for best data quality

3. **Python Ecosystem**
   - Python 3.14 runtime
   - tastytrade SDK
   - yfinance library

### Internal Dependencies
1. **Epic Completion**
   - v2.3 epic must complete before v3.0 planning
   - CSV schema freeze required for downstream tools

2. **Testing Coverage**
   - Core calculations tested
   - Integration tests for new features
   - Live API validation

## Risk Assessment

### Technical Risks
1. **API Changes** (Medium)
   - TastyTrade may change API without notice
   - Mitigation: SDK abstracts API details, monitor updates

2. **Data Quality** (Low)
   - Greeks timeout may miss strikes
   - Mitigation: Graceful degradation, accept partial results

3. **Python 3.14 Bug** (Low)
   - Asyncio recursion issue
   - Mitigation: Workaround active, stable

### Business Risks
1. **TOS Violations** (Low)
   - Personal use within TastyTrade terms
   - No data redistribution

2. **Market Changes** (Medium)
   - Strategy may become less effective over time
   - Mitigation: Continuous backtesting, threshold tuning

### Operational Risks
1. **Performance Degradation** (Low)
   - Large scans may slow down
   - Mitigation: Streaming CSV writer, caching

2. **Maintenance Burden** (Medium)
   - One-person project
   - Mitigation: Good documentation, modular design

## Measurement and Tracking

### Key Performance Indicators (KPIs)
1. **Scan Speed:** < 2 minutes for 100 symbols (cache hit)
2. **Cache Hit Rate:** > 90% daily scanning
3. **Greeks Coverage:** > 95% IV from Greeks (primary)
4. **Filter Accuracy:** < 5% false positives

### Progress Tracking
1. **Epic System** - `.claude/epics/` directory
2. **GitHub Issues** - Task tracking (#23-#45)
3. **Context Updates** - Regular context refresh
4. **Version Tags** - Git tags for releases

### Quality Metrics
1. **Test Coverage** - Unit tests for core calculations
2. **Documentation** - CLAUDE.md, README_TT.md up to date
3. **Code Review** - Claude Code reviews for quality
4. **User Feedback** - Iterate based on personal usage
