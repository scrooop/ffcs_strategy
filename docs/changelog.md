# Changelog

## v3.0.1 (2025-10-20)
- **BREAKING CHANGE**: FF columns renamed and reordered for clarity:
  - `ff` → `call_ff` (clarifies this is the call leg FF)
  - `combined_ff` → `avg_ff` (clarifies this is the average of call and put FF)
  - Column order changed: `min_ff, call_ff, put_ff, avg_ff` (min_ff moved to first position as primary sort key)
- CSV sorting uses `min_ff` as primary sort key (largest to smallest) for both ATM and double calendars
- Updated documentation across all files (code, csv-schema-v3.md, README_TT.md) to reflect changes

## v3.0
- CSV schema reduced 40 → **32** columns and names stabilized.
- Root `CLAUDE.md` trimmed; long content relocated under `docs/`.
- Logging policy clarified.

## v2.2
- Pre‑filter speed‑ups; improved earnings/volume checks.
