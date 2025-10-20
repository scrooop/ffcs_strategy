---
issue: 27
title: Update Documentation (CLAUDE.md, README_TT.md)
analyzed: 2025-10-20T06:25:44Z
estimated_hours: 3-4
parallelization_factor: 1.8
---

# Parallel Work Analysis: Issue #27

## Overview

Update project documentation to reflect v2.2 changes from completed tasks. This includes CSV schema updates (31 → 39 columns), breaking changes, migration guide, CLI flag updates, troubleshooting section, and version history.

**Critical Context**: Task #24 finalized v2.2 schema with 39 columns (not 32 as originally estimated). Documentation must accurately reflect the actual implementation.

## Work Stream Analysis

### Option 1: Parallel Execution (Recommended if time-critical)

Two independent documentation files can be updated in parallel with shared change summary.

#### Stream A: CLAUDE.md Updates
**Scope**: Update main project documentation
**Files**:
- `CLAUDE.md`
**Agent Type**: general-purpose
**Can Start**: immediately (#24 complete)
**Estimated Hours**: 2-2.5
**Dependencies**: Needs v2.2 change summary from #24

**Work Items**:
1. Update CSV Output Schema section:
   - Change column count: 31 → 39
   - Add new columns: atm_delta, atm_ff, atm_iv_front/back/fwd, atm_iv_source_front/back, min_ff
   - Rename: avg_options_volume → avg_options_volume_20d
   - Document structure-specific columns (ATM vs double)
2. Add v2.1 → v2.2 Migration Guide:
   - Column mapping table
   - Breaking changes list
   - Migration steps for existing CSV consumers
3. Update CLI flags documentation:
   - Remove: --use-xearn-iv, --force-greeks-iv, --min-liquidity-rating
   - Update: --min-avg-volume (from #32)
   - Document skip reasons
4. Add Troubleshooting section:
   - Delta not found (50Δ selection tolerance)
   - Volume data missing (cache/API failures)
   - Skip reasons and meanings
5. Update Version History:
   - Add v2.2 entry with date
   - Summary: "Core calculation corrections for strategy alignment"
6. Update usage examples:
   - Show both ATM and double structure scans
   - Demonstrate new flags
7. Document IV source priority:
   - Greeks primary (rationale from #29)

#### Stream B: README_TT.md Updates
**Scope**: Update scripts documentation
**Files**:
- `scripts/README_TT.md`
**Agent Type**: general-purpose
**Can Start**: immediately (#24 complete)
**Estimated Hours**: 1.5-2
**Dependencies**: Needs same v2.2 change summary as Stream A

**Work Items**:
1. Update CSV schema documentation (same as CLAUDE.md)
2. Update command examples:
   - Remove deprecated flags
   - Add new flags
   - Show ATM and double structure examples
3. Update usage guide with v2.2 changes
4. Add troubleshooting section (condensed version)
5. Update version history

### Option 2: Sequential Execution (Safer, Recommended)

Single agent updates both files sequentially to ensure consistency.

#### Single Stream: Complete Documentation Update
**Scope**: Update both CLAUDE.md and README_TT.md
**Files**:
- `CLAUDE.md`
- `scripts/README_TT.md`
**Agent Type**: general-purpose
**Can Start**: immediately
**Estimated Hours**: 3-4
**Dependencies**: Task #24 complete ✅

**Phase 1: Gather v2.2 Changes (30m)**
1. Review Task #24 completion summary
2. Extract v2.2 CSV schema (39 columns)
3. Identify breaking changes:
   - Column additions (8 new columns)
   - Column renames (1 rename)
   - CLI flag changes
4. Create change summary document for reference

**Phase 2: Update CLAUDE.md (1.5-2h)**
1. CSV schema section
2. Migration guide
3. CLI flags
4. Troubleshooting
5. Version history
6. Usage examples
7. IV source priority

**Phase 3: Update README_TT.md (1-1.5h)**
1. Apply same changes as CLAUDE.md
2. Ensure consistency with main docs
3. Update command examples
4. Add troubleshooting

**Phase 4: Validation (30m)**
1. Verify column counts match implementation (39)
2. Check all CLI flags are current
3. Test example commands (syntax check)
4. Ensure consistency between docs

## Coordination Points

### Shared Content (if parallel)
Both files need identical information about:
- v2.2 CSV schema (39 columns)
- Breaking changes list
- Migration guide content
- CLI flag changes
- Troubleshooting topics

**Coordination Strategy**:
- Create shared "v2.2-changes-summary.md" first
- Both agents reference this document
- Reduces duplication and ensures consistency

### Sequential Requirements
1. Must review #24 completion before documenting
2. Migration guide requires full schema understanding
3. Troubleshooting needs implementation details

## Conflict Risk Assessment

**Parallel Execution**:
- **Low Risk**: Different files, no conflicts
- **Consistency Risk**: Medium - both files must have identical information
- **Coordination Overhead**: Moderate - shared change summary needed

**Sequential Execution**:
- **No Risk**: Single agent ensures consistency
- **Time**: Slightly longer wall time (+1-2h)

## Parallelization Strategy

**Recommended Approach**: Hybrid (leaning toward sequential)

**If time is critical** (parallel):
1. Create shared v2.2 changes summary (30m)
2. Launch Stream A (CLAUDE.md) and Stream B (README_TT.md) simultaneously
3. Both agents reference shared summary
4. Cross-validate after completion

**If consistency is priority** (sequential):
1. Phase 1: Gather v2.2 changes
2. Phase 2: Update CLAUDE.md
3. Phase 3: Update README_TT.md
4. Phase 4: Validation

**Task metadata shows `parallel: false`** → Sequential recommended

## Expected Timeline

**Parallel execution**:
- Stream A: 2-2.5 hours (CLAUDE.md)
- Stream B: 1.5-2 hours (README_TT.md)
- Overlap: Both run simultaneously
- **Wall time**: 2-2.5 hours (max of streams)
- **Efficiency gain**: 40-45%

**Sequential execution**:
- Phase 1: 30m (gather changes)
- Phase 2: 1.5-2h (CLAUDE.md)
- Phase 3: 1-1.5h (README_TT.md)
- Phase 4: 30m (validation)
- **Wall time**: 3.5-4.5 hours

## Notes

**Critical Corrections Needed**:
1. **Column count**: Task says "31 → 32" but actual is "31 → 39" (per #24)
2. **New columns**: 8 new columns added, not 1
3. **CLI flags**: Multiple flags removed/renamed (not just --min-avg-volume)

**v2.2 Changes Summary** (from #24):
- **Added columns (8)**:
  - atm_delta, atm_ff, atm_iv_front, atm_iv_back, atm_fwd_iv
  - atm_iv_source_front, atm_iv_source_back
  - min_ff
- **Renamed columns (1)**:
  - avg_options_volume → avg_options_volume_20d
- **Removed columns (2)**:
  - liquidity_rating, liquidity_value (already removed in #32)
- **Schema**: v2.1 (31 cols) → v2.2 (39 cols)

**Breaking Changes to Document**:
1. CSV schema: 31 → 39 columns
2. ATM structure: New atm-specific columns, empty double columns
3. Double structure: New min_ff column for filtering
4. Column rename: avg_options_volume → avg_options_volume_20d
5. CLI flags removed: --use-xearn-iv, --force-greeks-iv, --min-liquidity-rating
6. IV source priority: Greeks primary (not X-earn)

**Migration Guide Content**:
```markdown
# v2.1 → v2.2 Migration

## Schema Changes
- Column count: 31 → 39 (+8 columns)
- New ATM columns: atm_delta, atm_ff, atm_iv_front/back/fwd, atm_iv_source_front/back
- New double column: min_ff
- Renamed: avg_options_volume → avg_options_volume_20d

## Column Mapping
| v2.1 Column | v2.2 Column | Notes |
|-------------|-------------|-------|
| avg_options_volume | avg_options_volume_20d | Renamed for clarity |
| liquidity_rating | (removed) | Use avg_options_volume_20d instead |
| liquidity_value | (removed) | Use avg_options_volume_20d instead |
| N/A | atm_delta | New: Delta at ATM strike |
| N/A | atm_ff | New: Single FF for ATM structure |
| N/A | min_ff | New: Minimum FF for double calendars |
| ... | ... | ... |
```

**Troubleshooting Topics**:
1. **"Delta not found within tolerance"**: Increase --delta-tolerance
2. **"Volume data missing"**: Check cache, API connectivity
3. **Skip reasons**: earnings_conflict, volume_too_low, no_strikes, etc.
4. **Empty atm_ff**: Check if structure=double (atm_ff only for ATM)
5. **Empty min_ff**: Check if structure=atm-call (min_ff only for double)

**Examples to Update**:
- Basic scan with both structures
- ATM-only scan
- Double-only scan
- Earnings filtering examples
- Volume filtering examples

## Recommendation

**Execute sequentially** (Option 2) for maximum consistency and accuracy. The task is marked `parallel: false`, and documentation consistency is more important than the 1-2 hour time savings from parallelization.

The sequential approach ensures:
- Consistent information across both files
- No duplication errors
- Clear validation at the end
- Single source of truth for v2.2 changes

If time is absolutely critical, parallel execution is viable with a shared change summary document.
