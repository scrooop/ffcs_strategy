# CSV schema v3.0 (32 columns)

This is the **authoritative contract** for downstream consumers. The scanner emits **exactly 32 columns** in v3.0.

> If you change fieldnames or semantics, update this file, bump the schema version if needed, add a short note to `docs/changelog.md`, and write a migration note in `docs/migrations/`.

## Minimum required columns (also listed in root `CLAUDE.md`)

| name                | type   | description |
|---------------------|--------|-------------|
| symbol              | str    | Underlying ticker |
| structure           | enum   | `ATM_CAL` or `DBL_CAL` |
| front_expiry        | date   | YYYY‑MM‑DD |
| back_expiry         | date   | YYYY‑MM‑DD |
| front_iv            | float  | Implied vol of front expiry (annualized) |
| forward_iv          | float  | Forward IV between front/back (variance decomposition) |
| ff                  | float  | Forward Factor = (front_iv − forward_iv)/forward_iv |
| earnings_window_days| int    | Days between now and next earnings if inside window; else 0 |
| avg_options_volume  | int    | Average daily options volume used for quality filtering |

## Full column table (add remaining 23 fields here)

> Keep names stable and snake_case. Document units and null behavior precisely.
> For any optional field, define default value and when it can be blank/zero.

| name | type | description |
|------|------|-------------|
| ...  | ...  | ...         |

