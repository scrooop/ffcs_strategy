---
issue: 10
epic: ff-scanner-v2
analyzed: 2025-10-19T18:23:17Z
status: ready
---

# Issue #10 Analysis: Documentation Updates

## Overview

Update all project documentation to reflect v2.0 scanner features. This task can be parallelized across 4 independent documentation files since there are no file conflicts.

## Parallel Work Streams

### Stream A: CLAUDE.md Updates
**Agent**: general-purpose
**Can Start**: Immediately (no dependencies)
**Files**:
- `CLAUDE.md`

**Scope**:
- Add v2.0 feature overview section
- Update "Running the Scanner" with new CLI flags:
  - `--structure {atm-call,double,both}`
  - `--skip-earnings` / `--allow-earnings` / `--show-earnings-conflicts`
  - `--min-liquidity-rating` / `--skip-liquidity-check`
  - `--delta-tolerance`
  - `--use-xearn-iv` / `--force-greeks-iv`
- Add thresholds section (earnings, liquidity, delta tolerance)
- Document X-earn IV implementation status (with graceful fallback)
- Update "Strategy Implementation Notes" if needed
- Keep CLAUDE.md concise (high-level overview)

**Deliverable**: Updated CLAUDE.md with v2.0 features documented

---

### Stream B: README_TT.md Updates
**Agent**: general-purpose
**Can Start**: Immediately (no dependencies)
**Files**:
- `scripts/README_TT.md`

**Scope**:
- Rewrite "Basic Usage" section with v2.0 examples from PRD Appendix C
- Add "Command Line Flags" section documenting all flags
- Add "Feature Details" sections:
  - Earnings Filtering (how it works, flags, examples)
  - Liquidity Screening (rating system, thresholds)
  - X-earn IV Support (with fallback to Greeks IV)
  - Double Calendar Structures (±35Δ, combined_ff calculation)
- Include example output CSV showing new 25-column schema
- Add troubleshooting section (common issues, solutions)
- Make README comprehensive and detailed (user reference)

**Deliverable**: Comprehensive README_TT.md with detailed examples

---

### Stream C: Function Docstrings
**Agent**: general-purpose
**Can Start**: Immediately (no dependencies)
**Files**:
- `scripts/ff_tastytrade_scanner.py`

**Scope**:
Add comprehensive docstrings with type hints to ALL new v2.0 functions:
- `fetch_market_metrics()`
- `check_earnings_conflict()`
- `check_liquidity()`
- `extract_xearn_iv()`
- `pick_delta_strike()`
- `snapshot_greeks_for_range()`
- `get_double_calendar_strikes()`
- Any other undocumented functions added in tasks 001-007

**Format Example**:
```python
async def fetch_market_metrics(session: Session, symbols: List[str]) -> Dict[str, MarketMetricInfo]:
    """
    Batch fetch earnings and liquidity data for all symbols.

    Args:
        session: Active tastytrade session
        symbols: List of ticker symbols (e.g., ['SPY', 'QQQ'])

    Returns:
        Dict mapping symbol → MarketMetricInfo with earnings dates and liquidity ratings

    Raises:
        None (returns empty dict on failure, logs error)

    Example:
        >>> metrics = await fetch_market_metrics(session, ['SPY', 'QQQ'])
        >>> metrics['SPY'].liquidity_rating
        5
    """
```

**Deliverable**: All new functions have comprehensive docstrings

---

### Stream D: Setup Instructions (Optional)
**Agent**: general-purpose
**Can Start**: Immediately (no dependencies)
**Files**:
- `docs/gpt-setup-instructions1.txt` (if still relevant)

**Scope**:
- Check if this file is still actively used
- If yes: Update with v2.0 usage examples and new flags
- If no: Document that it's deprecated or remove it
- Keep updates minimal (quick reference only)

**Deliverable**: Updated or deprecated setup instructions

---

## Dependencies Between Streams

**None** - All streams are fully independent:
- Stream A (CLAUDE.md) → No file conflicts with B, C, D
- Stream B (README_TT.md) → No file conflicts with A, C, D
- Stream C (ff_tastytrade_scanner.py) → No file conflicts with A, B, D
- Stream D (gpt-setup-instructions1.txt) → No file conflicts with A, B, C

All 4 streams can be launched in parallel immediately.

## Coordination Notes

**File Ownership**:
- Stream A owns: `CLAUDE.md`
- Stream B owns: `scripts/README_TT.md`
- Stream C owns: `scripts/ff_tastytrade_scanner.py`
- Stream D owns: `docs/gpt-setup-instructions1.txt`

**No conflicts possible** - each stream has exclusive write access to its file(s).

## Success Criteria

All streams complete when:
- [ ] CLAUDE.md updated with v2.0 overview and examples
- [ ] README_TT.md comprehensive with detailed usage guide
- [ ] All new functions have docstrings with type hints
- [ ] Setup instructions updated or deprecated
- [ ] Documentation enables new user to run scanner without external help
- [ ] Limitations clearly documented (e.g., X-earn IV with fallback)

## Estimated Timeline

- **Stream A**: 30-45 minutes (CLAUDE.md is concise)
- **Stream B**: 60-90 minutes (README is detailed)
- **Stream C**: 45-60 minutes (docstrings for ~7-10 functions)
- **Stream D**: 15-30 minutes (quick reference or deprecation)

**Total parallel time**: ~90 minutes (longest stream is B)
**Total sequential time**: ~3-4 hours (if done one at a time)

## Notes

- All documentation should reflect actual implementation from tasks 001-007
- Include real CLI examples that users can copy-paste
- Document X-earn IV graceful fallback to Greeks IV
- CSV schema: 25 columns (timestamp, structure, call/put strikes, deltas, FFs, earnings, liquidity, IV sources)
- Thresholds: FF ≥ 0.20 (general), ≥ 0.23 (30-60, 30-90 DTE pairs)
