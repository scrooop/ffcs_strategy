# Architecture overview

End‑to‑end data flow (high level):

1. **Universe selection** → tickers from CLI
2. **Pre‑filters** → earnings window, avg options volume
3. **Market data fetch** → spot, IV surfaces/Greeks (production)
4. **Pairing logic** → front/back expiry selection from `--pairs`
5. **Math** → Forward IV (variance decomposition), Forward Factor (FF)
6. **Structure evaluation** → ATM calendars and, if selected, double‑calendars
7. **Output** → CSV (schema v3.0), logs per policy

See `docs/usage.md` for flags and `docs/csv-schema-v3.md` for the CSV contract.
