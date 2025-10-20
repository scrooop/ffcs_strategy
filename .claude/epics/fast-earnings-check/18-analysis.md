---
issue: 18
created: 2025-10-20T01:05:00Z
status: ready
---

# Analysis: Add earnings_source column to CSV output

## Overview
Extend the CSV output schema to include `earnings_source` column, tracking where earnings data came from ("cache", "yahoo", "tastytrade", "none"). This provides transparency and debugging capability for users to understand data provenance.

## Work Stream (Single-threaded, Quick)

### CSV Schema Extension (2-3 hours)
**Scope:** Add earnings_source column to CSV output
**Owner:** general-purpose agent

**Implementation details:**

1. **Locate CSV header definition:**
   - Find where CSV columns are defined (header row)
   - Current schema: 28 columns
   - New schema: 29 columns (add earnings_source at end)

2. **Update CSV header:**
   ```python
   # Add "earnings_source" to header row
   # Current: ...iv_source_put_front, iv_source_put_back
   # New: ...iv_source_put_front, iv_source_put_back, earnings_source
   ```

3. **Update CSV row writing:**
   - Find where CSV rows are written (result dict or list)
   - Add earnings_source value from earnings_data dict
   - Get value: `earnings_data[symbol]['source']`
   - Possible values: "cache", "yahoo", "tastytrade", "none", "skipped"

4. **Handle --allow-earnings case:**
   - If earnings filtering disabled, set earnings_source = "skipped"
   - This distinguishes "no earnings check" from "no earnings data found"

5. **Preserve earnings_data dict:**
   - Ensure earnings_data is available in scope where CSV is written
   - May need to pass earnings_data to scan() function or store globally

**Files to modify:**
- `scripts/ff_tastytrade_scanner.py` (CSV writing section)

**Key considerations:**
- Add column at END (29th position) for backward compatibility
- Readers using csv.DictReader will automatically pick up new column
- Readers expecting fixed 28 columns will ignore 29th column
- Values must match EarningsCache return format

**Testing approach:**
- Manual: Generate CSV with 10 symbols, verify column present
- Manual: Verify values are correct (cache, yahoo, tastytrade)
- Manual: Run with --allow-earnings, verify earnings_source = "skipped"
- Manual: Load CSV in Excel/spreadsheet, verify no parsing errors
- Backward compatibility: Old tools still work (ignore new column)

## Dependencies
- ✅ Task #16 completed (earnings_data dict available in main())
- ✅ Task #17 completed (earnings_source values populated by fallback chain)

## Success Criteria
- [ ] CSV header includes "earnings_source" (29th column)
- [ ] CSV rows populated with correct earnings_source values
- [ ] --allow-earnings case handled (earnings_source = "skipped")
- [ ] Backward compatible (existing CSV readers work)
- [ ] Manual testing: All 5 scenarios pass

## Risks & Mitigations
**Risk:** Breaking CSV parsing in existing tools
- Mitigation: Add column at end (least disruptive)
- Mitigation: Document as backward compatible addition

**Risk:** earnings_data not available in CSV writing scope
- Mitigation: Pass earnings_data to scan() function or store as global
- Alternative: Add earnings_source to result dict

**Risk:** Conflicting with Task #19 changes
- Note: Task #19 already completed, no conflict

## Notes
- This is a small, focused change (add 1 column to CSV)
- No logic changes, just data tracking
- Valuable for debugging (see which source provided data)
- Column position: 29th (after iv_source_put_back)
- Task #20 will update documentation with new schema
