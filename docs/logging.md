# Logging & terminal output policy

Goals:
- Keep terminal output **clean and human‑scannable**.
- Provide enough context for debugging without overwhelming normal runs.

Policy:
- Default to a concise summary (universe size, filters applied, #candidates, output path).
- Use structured log lines for notable events (retries, API errors).
- Suppress noisy third‑party debug logs in normal mode; enable via `--verbose`.
- When exporting long traces or benchmarks, write to file and **link from PR** instead of pasting into `CLAUDE.md`.
