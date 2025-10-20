# GitHub Issue Mapping

Epic: #22 - Core Calculation Corrections for FFCS Scanner
https://github.com/scrooop/ffcs_strategy/issues/22

## Tasks

- #23: Add Edge Case Validation & Unit Tests - https://github.com/scrooop/ffcs_strategy/issues/23
- #25: Implement Skip Tracking & Logging - https://github.com/scrooop/ffcs_strategy/issues/25
- #28: Refactor ATM Strike Selection (50Δ Anchor) - https://github.com/scrooop/ffcs_strategy/issues/28
- #31: Simplify ATM FF Computation (Single FF) - https://github.com/scrooop/ffcs_strategy/issues/31
- #26: Update Double Calendar Gating (Min-Gate) - https://github.com/scrooop/ffcs_strategy/issues/26
- #29: Invert IV Source Priority (Greeks Primary) - https://github.com/scrooop/ffcs_strategy/issues/29
- #32: Implement Volume-Based Liquidity Filter - https://github.com/scrooop/ffcs_strategy/issues/32
- #24: Update CSV Schema & Output Logic - https://github.com/scrooop/ffcs_strategy/issues/24
- #27: Update Documentation (CLAUDE.md, README_TT.md) - https://github.com/scrooop/ffcs_strategy/issues/27
- #30: Integration Testing & Validation - https://github.com/scrooop/ffcs_strategy/issues/30

## Summary

- **Total tasks:** 10
- **Parallel tasks:** 3 (#26, #29, #32 can run simultaneously after #23, #25 complete)
- **Sequential tasks:** 7 (have dependencies)

## Dependency Chain

```
Foundation:
  #23 (Validation) → #25 (Skip Tracking)
                       ↓
                       ├─→ #28 (ATM 50Δ) → #31 (ATM FF) ──┐
                       ├─→ #26 (Double Min-Gate) ─────────┤
                       ├─→ #29 (IV Priority) ─────────────┤
                       └─→ #32 (Volume Filter) ───────────┤
                                                           ↓
Integration:                                      #24 (CSV) → #27 (Docs)
                                                              ↓
Validation:                                                #30 (Testing)
```

## Sync Information

- **Synced:** 2025-10-20T04:49:50Z
- **Repository:** scrooop/ffcs_strategy
- **Epic file:** `.claude/epics/core-calc-corrections/epic.md`
- **Task files:** `.claude/epics/core-calc-corrections/{23,24,25,26,27,28,29,30,31,32}.md`
