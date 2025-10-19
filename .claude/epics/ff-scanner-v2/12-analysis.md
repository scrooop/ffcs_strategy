---
issue: 12
epic: ff-scanner-v2
analyzed: 2025-10-19T18:57:13Z
status: ready
---

# Issue #12 Analysis: Futures Options Support

## Overview

Investigation and validation task to determine if the FF scanner works with futures options (e.g., /ES, /GC). This is a single-stream exploratory task - no parallel work needed since it's sequential testing and documentation.

## Single Work Stream

### Stream A: Futures Compatibility Investigation
**Agent**: general-purpose
**Can Start**: Immediately (no dependencies)
**Files**:
- No code modifications planned initially (investigation only)
- Will create test results document
- May update CLAUDE.md or README based on findings

**Scope**:

**Phase 1: API Exploration (30-45 min)**
1. Review tastytrade SDK documentation for futures support
2. Test basic API calls with futures symbols (/ES, /GC)
3. Check if `NestedOptionChain`, `get_market_data`, `snapshot_greeks` work with futures

**Phase 2: Scanner Testing (45-60 min)**
1. Run smoke test with /ES and /GC:
   ```bash
   python scripts/ff_tastytrade_scanner.py \
     --tickers /ES /GC \
     --pairs 30-60 \
     --min-ff 0.20 \
     --skip-earnings \
     --csv-out futures_test.csv
   ```
2. Document errors, warnings, or unexpected behavior
3. Compare output structure with equity options (SPY)

**Phase 3: Gap Analysis (30-45 min)**
1. Identify what works vs. what doesn't
2. Document required code changes (if any)
3. Assess effort: trivial fix, moderate changes, or major refactor

**Phase 4: Documentation (30 min)**
1. Create findings document with test results
2. Provide recommendation: supported / partial / not supported
3. Update CLAUDE.md or README with futures compatibility status
4. Create follow-up task if code changes needed

**Deliverables**:
- Test results document (markdown file with findings)
- Recommendation on futures support
- Updated documentation (CLAUDE.md or README)
- Follow-up task created if changes needed

---

## Work Stream Summary

**Total Streams**: 1 (sequential investigation, not parallelizable)

**Stream A**: Futures compatibility testing and documentation
**Estimated Time**: 2.5-3.5 hours

## Key Investigation Points

1. **Symbol Format**: Does `/ES` work or does it need `ES`?
2. **Option Chains**: Are futures option chains structured differently?
3. **Greeks Data**: Do futures options have Greeks via dxFeed?
4. **Expirations**: Different expiration cycles (weekly, monthly, quarterly)?
5. **Earnings Filter**: Should be N/A for futures (no earnings announcements)
6. **Liquidity**: How is liquidity measured for futures options?

## Success Criteria

- [ ] Scanner tested with at least 2 futures symbols (/ES, /GC)
- [ ] Test results documented (errors, warnings, output)
- [ ] API compatibility assessed (works / doesn't work / needs changes)
- [ ] Code change requirements identified (none / minor / major)
- [ ] Recommendation provided with rationale
- [ ] Documentation updated or follow-up task created

## Expected Outcomes

**Best Case**: Scanner works as-is with futures symbols
**Likely Case**: Minor tweaks needed (symbol format, earnings filter bypass)
**Worst Case**: Major refactor needed (different API endpoints, data structures)

## Notes

- This is exploratory work - no code changes planned initially
- Agent should document everything discovered during testing
- If major changes needed, create separate implementation task
- Focus on /ES and /GC as primary test cases (most liquid futures)
