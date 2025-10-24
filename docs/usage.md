# Usage & CLI flags

This page centralizes **how to run the scanner**, common recipes, and the **authoritative CLI flag reference**.

## Quick start

```bash
python scripts/ff_tastytrade_scanner.py   --tickers SPY QQQ   --pairs 30-60
```

- `--tickers` accepts space‑separated symbols.
- `--pairs` specifies front/back day‑count pairs (e.g., `30-60`).
- Results are written to CSV (see schema in `docs/csv-schema-v3.md`).
- **CSV output:** If `--csv-out` is not specified, automatically saves to `ff_scans/{timestamp}_FFSCAN.csv` where timestamp is `YYMMDD_HHMM` format.

## Common recipes

ATM + double calendars on a handful of symbols:
```bash
python scripts/ff_tastytrade_scanner.py   --tickers SPY QQQ AAPL   --pairs 30-60 30-90 60-90
```

With custom output path:
```bash
python scripts/ff_tastytrade_scanner.py   --tickers SPY QQQ AAPL   --pairs 30-60 30-90 60-90   --csv-out results/scan.csv
```

Disable earnings filter (trade through earnings **only if you intend to**):
```bash
python scripts/ff_tastytrade_scanner.py   --tickers AAPL   --pairs 30-90   --allow-earnings
```

Double‑calendars only:
```bash
python scripts/ff_tastytrade_scanner.py   --tickers SPY QQQ   --pairs 60-90   --structure double
```

## Flag reference (source of truth)

> The authoritative source is the tool’s `--help` output. Re‑capture it into this section whenever flags change.

```bash
python scripts/ff_tastytrade_scanner.py --help
```

Recommended sections to paste here in a stable order:
1. **Core selection:** `--tickers`, `--pairs`, structures (ATM / double)
2. **Quality filters:** earnings window, min avg options volume, etc.
3. **Output controls:** CSV path, append/overwrite, precision
4. **Performance:** batch sizes, timeouts, retries
5. **Logging:** verbosity, quiet/summary mode
