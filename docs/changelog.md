# Changelog

## v3.0.1 (2025-10-20)
- **BREAKING CHANGE**: Column names corrected and reordered for clarity:
  - Strike/delta columns: Use explicit names `call_strike`, `call_delta` (not ambiguous "strike", "delta")
  - FF columns renamed: `ff` → `call_ff`, `combined_ff` → `avg_ff`
  - FF column order changed: `min_ff, call_ff, put_ff, avg_ff` (min_ff first as primary sort key)
- CSV sorting uses `min_ff` as primary sort key (largest to smallest) for both ATM and double calendars
- Updated documentation across all files (code, csv-schema-v3.md, README_TT.md) to reflect changes
- **Rationale:** "strike" and "delta" were ambiguous column names that could confuse users about which leg they referred to

## v3.0
- CSV schema reduced 40 → **32** columns and names stabilized.
- Root `CLAUDE.md` trimmed; long content relocated under `docs/`.
- Logging policy clarified.

## v2.2
- Pre‑filter speed‑ups; improved earnings/volume checks.
