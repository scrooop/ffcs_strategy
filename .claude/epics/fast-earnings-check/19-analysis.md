---
issue: 19
created: 2025-10-20T00:54:30Z
status: ready
---

# Analysis: Remove --skip-earnings flag (breaking change)

## Overview
Remove the redundant `--skip-earnings` CLI flag from the scanner. Since earnings filtering is now the default behavior (Task #16), having both `--skip-earnings` and `--allow-earnings` flags is confusing and redundant. This is a breaking change that simplifies the CLI interface.

## Work Stream (Single-threaded, Quick)

### CLI Cleanup (1-2 hours)
**Scope:** Remove --skip-earnings flag from argparse configuration
**Owner:** general-purpose agent

**Implementation details:**

1. **Find and remove argparse mutually exclusive group:**
   Current code (confusing):
   ```python
   earnings_group = parser.add_mutually_exclusive_group()
   earnings_group.add_argument('--skip-earnings', action='store_true',
                               help='Skip symbols with earnings conflicts (default)')
   earnings_group.add_argument('--allow-earnings', action='store_true',
                               help='Allow trading through earnings')
   ```

   New code (simplified):
   ```python
   parser.add_argument('--allow-earnings', action='store_true',
                       help='Allow trading through earnings (default: filter earnings conflicts)')
   ```

2. **Update help text:**
   - Remove all references to `--skip-earnings`
   - Update `--allow-earnings` help text to clarify it disables filtering
   - Add "(default: filter earnings conflicts)" to help message

3. **Verify default behavior:**
   ```python
   # Default: filter earnings (unless --allow-earnings flag set)
   if not args.allow_earnings:
       # Run earnings pre-filter
       cache = EarningsCache()
       # ... filtering logic ...
   ```

4. **Test migration error (optional):**
   - argparse will automatically show "error: unrecognized arguments: --skip-earnings"
   - This is sufficient for user migration (no custom error needed)

**Files to modify:**
- `scripts/ff_tastytrade_scanner.py` (argparse section only, ~5 lines changed)

**Key considerations:**
- Remove mutually exclusive group (no longer needed)
- Keep `--allow-earnings` flag (unchanged behavior)
- Default is to filter earnings (no flag needed)
- argparse handles unknown flag error automatically
- No changes to filtering logic (only CLI interface)

**Testing approach:**
- Manual: Run with no flags - verify earnings filtering enabled (default)
- Manual: Run with `--allow-earnings` - verify earnings filtering disabled
- Manual: Run with `--skip-earnings` - verify error message shown
- Manual: Run `--help` - verify `--skip-earnings` not shown

## Dependencies
- ✅ Task #16 completed (earnings pre-filter integrated, default behavior established)

## Success Criteria
- [ ] `--skip-earnings` flag removed from argparse
- [ ] `--allow-earnings` flag still works (disables filtering)
- [ ] Default behavior filters earnings (no flag needed)
- [ ] `--help` output no longer shows `--skip-earnings`
- [ ] Running `--skip-earnings` shows argparse error
- [ ] Manual testing: All 4 scenarios pass

## Risks & Mitigations
**Risk:** Breaking existing user scripts
- Mitigation: This is intentional (breaking change for v2.1)
- argparse error message guides users to remove flag
- Documentation (Task #20) will explain migration

**Risk:** Confusion about new default behavior
- Mitigation: Help text clearly states "(default: filter earnings conflicts)"
- Console output shows filtering in action
- Documentation will clarify

## Notes
- **Breaking change:** Users with scripts using `--skip-earnings` must update
- **Migration is simple:** Just remove the flag (it's the default now)
- **No code logic changes:** Only argparse configuration
- This is a small, focused change (~5 lines of code)
- Can run in parallel with Task #17 (different code sections)
- Conflicts with Task #18 (both modify same file, but different sections)
