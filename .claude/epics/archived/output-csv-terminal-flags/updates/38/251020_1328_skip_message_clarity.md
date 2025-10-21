# Update: Improve Skip Message Clarity

**Task:** #38 - Add Professional Logging Infrastructure
**Date:** 2025-10-20T18:28:00Z
**Type:** Enhancement Request (User Feedback)

## Issue Report

User reported confusing terminal output showing:
```
Skip breakdown:
  - both_legs_required: 35
```

User didn't understand what "both_legs_required: 35" means or why it's happening.

## Investigation

**Root Cause:** Skip message is technically correct but not user-friendly.

**Current Behavior (scripts/ff_tastytrade_scanner.py:1230-1233):**
```python
# Skip if we don't have BOTH call and put calendars
if not (has_call_calendar and has_put_calendar):
    skip_stats[SKIP_BOTH_LEGS_REQUIRED] += 1
    logger.debug(f"Skipping {sym} double {front}-{back}: {SKIP_BOTH_LEGS_REQUIRED}")
    continue
```

**What's happening:**
- Double calendar structures require BOTH a ±35Δ call calendar AND a ±35Δ put calendar
- If only one leg (call OR put) meets delta tolerance, the symbol is skipped
- 35 symbols were skipped because they lacked both legs
- This is **expected behavior**, not a bug
- Message is unclear because:
  1. "both_legs_required" is technical jargon
  2. Doesn't explain what "legs" means (call + put calendars)
  3. Doesn't indicate this is for double calendar structure only
  4. Users might think it's an error rather than a filtering decision

## Proposed Solution

As part of Task #38 logging infrastructure improvements, enhance skip messages:

**Option 1: Detailed skip breakdown (recommended)**
```
Skip breakdown:
  - No double calendar (missing call or put leg): 35
  - Below FF threshold: 12
  - Earnings conflict: 8
```

**Option 2: Add explanatory note**
```
Skip breakdown:
  - both_legs_required: 35 (double calendar needs both ±35Δ call AND put)
  - below_ff_threshold: 12
```

**Option 3: Separate counters**
```
Skip breakdown:
  - Missing call leg (double): 18
  - Missing put leg (double): 17
  - Below FF threshold: 12
```

## Recommendation

Implement **Option 1** as part of Task #38's user-facing output improvements:
- Rename all skip reason constants to be more descriptive
- Update terminal output formatting for clarity
- Add context about which structure caused the skip (ATM vs double)
- Consider adding `--verbose-skips` flag to show per-symbol skip reasons

## Impact

- **Priority:** Low (cosmetic/UX improvement)
- **Effort:** 15 minutes (part of Task #38 refactor)
- **Benefit:** Reduces user confusion, improves debugging experience

## References

- Code location: `scripts/ff_tastytrade_scanner.py:1230-1233` (skip logic)
- Code location: `scripts/ff_tastytrade_scanner.py:1901-1904` (skip breakdown output)
- Documentation: `CLAUDE.md` - "Double Calendar Specific" section already explains requirement
- Related constant: `SKIP_BOTH_LEGS_REQUIRED = "both_legs_required"` (line 60)

## Action Items

- [ ] Rename skip reason constants for clarity (e.g., `SKIP_DOUBLE_MISSING_LEG`)
- [ ] Update terminal skip breakdown formatting (Option 1)
- [ ] Add docstring explaining skip reason meanings
- [ ] Test with real scanner output to verify clarity
