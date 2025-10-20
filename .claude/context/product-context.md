---
created: 2025-10-20T18:58:52Z
last_updated: 2025-10-20T18:58:52Z
version: 1.0
author: Claude Code PM System
---

# Product Context

## Target Users

### Primary Persona: Active Options Trader
**Profile:**
- Experience: Intermediate to advanced options trading
- Trading frequency: Daily to weekly scans
- Capital: $50k-$500k+ trading account
- Goal: Find mispriced forward volatility opportunities
- Tools: TastyTrade platform, CLI-comfortable

**Pain Points:**
- Manual IV term structure analysis is time-consuming
- Difficult to scan 50+ symbols efficiently
- Need to filter out earnings conflicts
- Want liquid options only (avoid wide spreads)
- Need actionable FF ratios, not raw IV data

**Solution Provided:**
- Automated FF calculation for multiple symbols
- Fast earnings pre-filtering (80-95% faster with cache)
- Quality filters (liquidity, volume, delta tolerance)
- CSV output for Excel/Python analysis
- Both ATM and double calendar opportunities

### Secondary Persona: Algorithmic Trader
**Profile:**
- Experience: Advanced quantitative background
- Trading frequency: Automated daily scans
- Capital: $100k-$1M+ algorithmic trading account
- Goal: Integrate FF scanner into automated trading system
- Tools: Python, pandas, API integration

**Pain Points:**
- Need machine-readable output (CSV/JSON)
- Require consistent schema for parsing
- Need performance (1500+ symbols in reasonable time)
- Want extensibility for custom filters
- Need historical data tracking

**Solution Provided:**
- CSV output with 40-column schema (consistent format)
- JSON output for nested data structures
- Streaming CSV writer for large scans (v2.3+)
- Skip tracking for filter analysis
- IV source tracking for data provenance

### Tertiary Persona: Strategy Researcher
**Profile:**
- Experience: Quantitative analyst or researcher
- Trading frequency: Ad-hoc analysis, backtesting
- Goal: Understand forward volatility patterns
- Tools: Python, Jupyter notebooks, statistical analysis

**Pain Points:**
- Need historical FF data for pattern analysis
- Want to test different thresholds
- Need to understand filter impact
- Require reproducible results

**Solution Provided:**
- Configurable thresholds (FF, DTE, delta tolerance)
- Skip reason tracking (understand filter impact)
- Earnings source tracking (data provenance)
- Timestamp on all outputs (reproducibility)

## Core Use Cases

### Use Case 1: Daily Pre-Market Scan
**Scenario:** Trader wants to identify top 5-10 calendar spread opportunities before market open

**Flow:**
1. Run scanner with watchlist (50-100 symbols)
2. Filter: FF ≥ 0.23, 30-60 DTE, both structures
3. Review CSV output sorted by FF (highest first)
4. Select top opportunities (highest FF, good liquidity)
5. Place orders at market open

**Requirements:**
- Fast execution (< 2 minutes for 100 symbols)
- Earnings filtering (default on)
- Liquidity filtering (default rating ≥ 3)
- Clear ranking (sort by atm_ff or min_ff)

**Scanner Command:**
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers @watchlist.txt \
  --pairs 30-60 \
  --min-ff 0.23 \
  --structure both \
  --csv-out scan_$(date +%Y%m%d).csv
```

### Use Case 2: Targeted Symbol Analysis
**Scenario:** Trader heard about AAPL volatility and wants to check all DTE pairs

**Flow:**
1. Run scanner for single symbol, multiple DTE pairs
2. Review ATM vs double calendar opportunities
3. Compare FF across different term structures (30-60 vs 30-90 vs 60-90)
4. Select best structure/DTE combination

**Requirements:**
- Multiple DTE pairs in single scan
- Side-by-side comparison (CSV rows)
- Detailed IV breakdown (front, back, forward)
- Both ATM and double structures

**Scanner Command:**
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers AAPL \
  --pairs 30-60 30-90 60-90 \
  --structure both \
  --show-all-scans
```

### Use Case 3: Futures Options Scanning
**Scenario:** Trader wants to scan major index futures for calendar opportunities

**Flow:**
1. Run scanner with futures symbols (/ES, /NQ, /RTY)
2. Review opportunities (no earnings filtering needed)
3. Compare with equivalent equity index ETFs (SPY, QQQ, IWM)

**Requirements:**
- Futures support (/ES syntax)
- Yahoo Finance integration (futures prices)
- Automatic earnings bypass (futures don't have earnings)
- Works outside market hours

**Scanner Command:**
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers /ES /NQ /RTY SPY QQQ IWM \
  --pairs 30-60 \
  --min-ff 0.20
```

### Use Case 4: High-Volume Weekly Scan
**Scenario:** Trader wants to scan 1500+ symbols weekly to find rare high-FF opportunities

**Flow:**
1. Run scanner with full symbol universe (1500+ symbols)
2. Use streaming CSV writer (memory efficient)
3. Filter for extreme FF (≥ 0.30) and high liquidity
4. Review top 20-30 opportunities

**Requirements:**
- Streaming CSV writer (v2.3+)
- Memory efficiency (constant memory usage)
- Fast earnings cache (80-95% speedup)
- High FF threshold filtering

**Scanner Command:**
```bash
python scripts/ff_tastytrade_scanner.py \
  --tickers @full_universe.txt \
  --pairs 30-60 30-90 \
  --min-ff 0.30 \
  --csv-out weekly_scan_$(date +%Y%m%d).csv
```

### Use Case 5: Custom Filter Testing
**Scenario:** Researcher wants to analyze impact of different liquidity thresholds

**Flow:**
1. Run scanner multiple times with different thresholds
2. Compare filtered vs allowed symbols
3. Analyze skip_reason distribution
4. Optimize filtering strategy

**Requirements:**
- Configurable thresholds
- Skip reason tracking
- Show filtered symbols (--show-earnings-conflicts)
- Reproducible results (timestamps)

**Scanner Commands:**
```bash
# Test 1: No volume filtering
python scripts/ff_tastytrade_scanner.py \
  --tickers @test_symbols.txt \
  --pairs 30-60 \
  --skip-liquidity-check \
  --csv-out test_no_filter.csv

# Test 2: Default liquidity rating
python scripts/ff_tastytrade_scanner.py \
  --tickers @test_symbols.txt \
  --pairs 30-60 \
  --csv-out test_default.csv

# Test 3: Precise volume filtering
python scripts/ff_tastytrade_scanner.py \
  --tickers @test_symbols.txt \
  --pairs 30-60 \
  --options-volume 20000 \
  --csv-out test_precise.csv
```

## Key Features by Priority

### P0 (Must-Have)
1. **Forward Factor Calculation** - Core edge detection
2. **Multi-Symbol Scanning** - Batch processing
3. **Earnings Filtering** - Avoid gamma risk
4. **CSV Output** - Machine-readable results
5. **Greeks IV Source** - Strike-level precision

### P1 (Critical)
1. **Fast Earnings Cache** - 80-95% performance improvement
2. **Liquidity Filtering** - Avoid illiquid options
3. **Double Calendar Support** - Higher win rate structure
4. **DTE Pair Flexibility** - 30-60, 30-90, 60-90 combinations
5. **ATM 50Δ Strike Selection** - Theory-aligned strike picking

### P2 (Important)
1. **Futures Support** - /ES, /NQ, /CL, /GC options
2. **Hybrid Volume Filtering** - 24/7 (rating) or precise (volume)
3. **Skip Reason Tracking** - Understand filter impact
4. **Structure Selection** - ATM-only, double-only, or both
5. **Delta Tolerance Control** - Adjust strike selection precision

### P3 (Nice-to-Have)
1. **JSON Output** - Alternative format for nested data
2. **Streaming CSV Writer** - Memory efficiency for large scans
3. **Show All Scans** - Include below-threshold results
4. **IV Source Tracking** - Data provenance (Greeks vs ex-earn)
5. **Logging Modes** - Quiet/normal/verbose/debug (v2.3)

## Success Metrics

### Performance Metrics
- **Scan Speed:** < 2 minutes for 100 symbols (with cache)
- **Cache Hit Rate:** > 90% for daily scanning
- **Memory Usage:** Constant (streaming writer)
- **Accuracy:** 100% earnings date accuracy (multi-source validation)

### Usage Metrics
- **Typical Scan Size:** 50-100 symbols per scan
- **Daily Scans:** 1-3 scans per user
- **Large Scans:** 1500+ symbols weekly
- **FF Threshold:** 0.20-0.23 (80% of usage)

### Quality Metrics
- **Filtering Effectiveness:** 40-60% symbols filtered (earnings + liquidity)
- **Liquidity Coverage:** > 95% of high-volume symbols pass
- **Greeks IV Coverage:** > 95% (primary source)
- **False Positives:** < 5% (good liquidity, correct FF)

## User Feedback Integration

### Implemented Based on User Needs
1. **Earnings Filtering** - Users requested automatic earnings avoidance
2. **Fast Caching** - Users needed faster rescans during earnings season
3. **Double Calendars** - Users wanted higher win rate structure
4. **Hybrid Filtering** - Users wanted 24/7 scanning capability
5. **Skip Tracking** - Users wanted to understand why symbols filtered

### Future Enhancements (User Requests)
1. **Logging System** (v2.3 in progress) - Users want quiet mode for cron jobs
2. **CSV Schema Reduction** (v2.3 in progress) - Users want simpler Excel analysis
3. **Bid-Ask Spread Checking** - Users want to avoid wide markets
4. **Auto-Execution** - Algo traders want order placement integration
5. **Backtesting Framework** - Researchers want historical validation

## Integration Points

### Current Integrations
1. **TastyTrade Platform** - Primary brokerage and data source
2. **Yahoo Finance** - Supplemental earnings and futures prices
3. **Excel/Google Sheets** - CSV output consumed by spreadsheets
4. **Python/Pandas** - CSV output parsed for further analysis

### Planned Integrations
1. **TastyTrade Order API** - Automated order placement (v3.0+)
2. **Position Tracking** - Monitor open calendar spreads (v3.0+)
3. **Slack/Discord** - Notification on high-FF opportunities (v3.0+)
4. **Backtesting Engine** - Historical FF analysis (v3.0+)

## Competitive Landscape

### Similar Tools
1. **CCR Scanner** (`~/tools/ccrScan/`) - Short strangle scanner
   - Similar: Earnings filtering, TastyTrade integration
   - Different: Different strategy (strangles vs calendars)
   - Opportunity: Code reuse for common features

2. **Manual Term Structure Analysis** - Traders manually comparing IV
   - Advantage: Scanner is faster, more comprehensive
   - Disadvantage: Scanner requires CLI comfort

3. **TastyTrade Platform Tools** - Built-in IV rank, IV percentile
   - Advantage: Scanner provides FF (forward factor), not just IV rank
   - Disadvantage: Requires external tool (CLI)

### Unique Value Proposition
1. **Forward Factor Focus** - Only tool calculating FF (not just IV rank)
2. **Multi-Structure Support** - ATM and double calendars in one scan
3. **Fast Earnings Cache** - 80-95% faster than competitors
4. **Hybrid Filtering** - Works 24/7, not just market hours
5. **Open Source / Extensible** - Can be customized and integrated

## Product Roadmap Alignment

### Current Version (v2.2)
- ✅ Core calculation corrections
- ✅ ATM 50Δ anchor
- ✅ Hybrid volume filtering
- ✅ 40-column CSV schema

### Next Version (v2.3 - In Progress)
- ⏳ CSV schema reduction (40 → 32 columns)
- ⏳ Logging system (quiet/normal/verbose/debug)
- ⏳ Error handling for 1500+ symbol scans
- ⏳ IV source control (--iv-ex-earn flag)

### Future Versions
- **v3.0** - Automated execution + position tracking
- **v3.1** - Backtesting framework
- **v3.2** - Web interface (optional)
- **v4.0** - Real-time monitoring + alerts
