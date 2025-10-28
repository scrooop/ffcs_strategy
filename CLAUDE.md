# CLAUDE.md — Lean Agent Brief (Forward‑Factor Calendar Spread repo)

**Purpose of this file**  
Claude Code auto‑loads `CLAUDE.md` into every session, so keep this document short, operational, and **under 20,000 characters**. If content would push this file over the budget, **move it into `docs/` and add a one‑line link here**.

## Documentation index/link map (open these when needed)
- **Usage & CLI flags** → `docs/usage.md`
- **CSV schema v3.0 (32 columns)** → `docs/csv-schema-v3.md`
- **Architecture overview** → `docs/architecture.md`
- **Strategy primer (FF calendars)** → `docs/strategy/primer.md`
- **Logging & terminal output policy** → `docs/logging.md`
- **Migrations (v2.2 → v3.0)** → `docs/migrations/v2.2-to-v3.0.md`
- **Changelog** → `docs/changelog.md`

## RELATED PROJECTS 
- Documention describing potentially useful related projects: `docs/USEFUL_RELATED_PROJECTS.md`
- If you encounter problems during development, check if what you are trying to do has already been successfully implemented in these tools.

## Agent charter (what you should do here)
- Implement and maintain the **Forward Factor (FF) calendar‑spread scanner** and supporting docs.
- Prefer **small, reviewable diffs**; write tests for any parsing/math that can regress.
- When adding examples, long tables, or logs → **place in `docs/`** and link from here.
- When unclear, **open the code and `docs/`**; do not invent assumptions.

### Non‑goals & safety rails

- **Hierarchy & locality**: keep this root `CLAUDE.md` lean. If a submodule or directory needs detailed rules, place a **localized `CLAUDE.md`** inside that folder so Claude loads it **only when working there**.
- Do **not** expand this file with long tutorials, benchmark logs, or migration histories.
- Do **not** change the CSV contract casually. If required:
  1) update code + `docs/csv-schema-v3.md`,  
  2) bump schema version if semantics change,  
  3) note it in `docs/changelog.md`,  
  4) include a migration note in `docs/migrations/`.

## Repository Structure

```
ffcs_strategy
├── scripts
│   ├── ff_tastytrade_scanner.py        # Main scanner (tastytrade API + dxFeed)
│   └── README_TT.md                    # Scanner usage guide
├── docs
│   ├── usage.md                        # CLI flags and usage guide
│   ├── csv-schema-v3.md                # CSV output schema (32 columns)
│   ├── architecture.md                 # System architecture overview
│   ├── logging.md                      # Logging and terminal output policy
│   ├── changelog.md                    # Version history
│   ├── strategy/                       # Strategy documentation
│   ├── migrations/                     # Schema migration guides
│   └── USEFUL_RELATED_PROJECTS.md      # Related tastytrade tools
├── CCPM_COMPLETE_SOP.md                # CCPM project management tool usage
├── data                                # Stock ticker lists
├── tests                               # development testing directory
└── venv                                # required virtual environment
```

## Minimal ritual (run every time before proposing changes)
1. **Quick smoke run (small sample)**:
   ```bash
   python scripts/ff_tastytrade_scanner.py      --tickers SPY QQQ      --pairs 30-60
   ```
   Output will auto-save to `ff_scans/{timestamp}_FFSCAN.csv`
3. **Validate CSV contract** (headers present, non‑empty rows).
4. **Run tests** (if present) and **lint/format** (keep diffs minimal).
5. Write a **short summary** of changes and rationale in the PR body; link to any `docs/` you touched.

## Contracts & invariants (authoritative rules)
- **Forward IV**: compute via variance decomposition between front/back expirations.
- **Forward Factor (FF)**: `FF = (Front_IV − Forward_IV) / Forward_IV`. Keep numeric stability; document any smoothing in `docs/usage.md`.
- **Default filters:** earnings risk window enabled by default; add explicit flag to override (details in `docs/usage.md`). Keep pre‑filtering efficient.
- **Backwards compatibility:** If you must rename/remove a required column, update `docs/migrations/` and note it in `docs/changelog.md`.

## Environment & tooling
- **Auth:** `TT_USERNAME`, `TT_PASSWORD` are saved in ~/.zshrc
- **Market data:** Use **production** for Greeks; sandbox is insufficient for live signals.
- **CLI help:** The source of truth for flags/options is the tool’s `--help`. Capture the output into `docs/usage.md` when flags change.

## Contribution etiquette
- Keep commits focused; prefer one logical change per PR.
- Include reproduction steps and a tiny before/after data sample if behavior changes.
- Avoid large refactors mixed with feature changes; split them.
- Respect size budget: **if your edit enlarges this file**, move material to `docs/` and link it instead.

### Local Documentation

- **Official OpenAPI Spec:** `docs/tastytrade_official_API_docs_full_spec.json` (393 KB)
  - Complete REST API specification (OpenAPI 3.0.0)
  - Key endpoints: earnings reports, market metrics, option chains, margin requirements
  - See `docs/RELATED_PROJECTS.md` for endpoint details

- **tastytrade SDK Docs:** `docs/tastytrade-sdk-docs/` - Comprehensive API reference (v10.1.0)
  - `session.md` - Authentication and session management
  - `dxfeed.md` - Market data streaming with Greeks
  - `instruments.md` - Option chains and instrument lookup
  - `metrics.md` - IV rank, liquidity, market metrics
  - `order.md` - Order placement and execution
  - `account.md` - Account data and positions

- **Related Projects:** `docs/RELATED_PROJECTS.md` - Overview of related tastytrade scanners
  - CCR Scanner (`~/tools/ccrScan/`) - Short strangle scanner with earnings filtering
  - TTT Tool (`~/tools/ttt/`) - Account and position analysis CLI
  - Code reuse opportunities for adding features

### Data Sources

- **tastytrade API:** Official SDK (https://github.com/tastyware/tastytrade)
- **dxFeed:** Real-time Greeks streaming (via DXLinkStreamer)
- **NestedOptionChain:** Expiration/strike discovery with streamer symbols
- **Strategy SOP:** `docs/strategy_origin_docs/FFCS-SOP-FROM-GPT.md`
