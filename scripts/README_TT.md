# FF Scanner (tastytrade API + dxFeed)

This CLI scans one or more symbols, pulls **ATM IV** for two target expirations using the **tastytrade** Open API & dxFeed streamer, computes **Forward IV** and the **FF ratio ((Front IV - Fwd IV) / Fwd IV)**, and prints rows that meet a minimum FF threshold.

> Greeks.volatility from the dxFeed feed is **Black-Scholes implied volatility** per contract — we average the ATM call & put.

## 0) Install & prerequisites

```bash
python -m pip install --upgrade tastytrade
```

You need **tastytrade credentials** (username and password).

- Put these in your shell env:
  ```bash
  export TT_USERNAME="your_username"
  export TT_PASSWORD="your_password"
  ```

References: See "Sessions" in the tastytrade SDK docs for authentication details.

## 1) Run it

```bash
# General threshold (0.20)
python ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 30-90 60-90 \
  --min-ff 0.20 \
  --csv-out ff_scan.csv

# Optimized threshold for ~20 trades/month (0.23 for 30-60, 30-90)
python ff_tastytrade_scanner.py \
  --tickers SPY QQQ AAPL TSLA NVDA \
  --pairs 30-60 30-90 \
  --min-ff 0.23
```

**Flags**

- `--tickers`: symbols (space or comma separated).
- `--pairs`: DTE pairs like `30-60 30-90` (front-back).
- `--min-ff`: keep rows with `FF >= min-ff` (default 0.20).
- `--dte-tolerance`: allowed deviation from target DTE (default 5 days).
- `--timeout`: seconds to wait for the greeks snapshot (default 3s).
- `--sandbox`: use sandbox (most market data requires production).
- `--csv-out`, `--json-out`: optional file outputs.

## 2) What it does

1. Fetches **underlying last price** via `get_market_data`.
2. Pulls the **nested option chain** to discover expirations and strikes.
3. Picks the **ATM strike** for each target expiration (closest to spot).
4. Subscribes once to **dxFeed Greeks** for the ATM call & put (`call_streamer_symbol` / `put_streamer_symbol`) and grabs a snapshot.
5. Computes:
   - `ATM_IV_front` = mean(call IV, put IV)
   - `ATM_IV_back` = mean(call IV, put IV)
   - `FwdIV = sqrt((T2*IV2^2 - T1*IV1^2)/(T2 - T1))` with `T = DTE/365`
   - `FF = (ATM_IV_front - FwdIV) / FwdIV`
6. Emits rows meeting `min-ff`, sorted by highest FF.

## 4) Threshold Guidance (from Video Transcript)

**General Rule:** FF ≥ 0.20 is tradable.

**Optimized Thresholds (~20 trades/month):**
- 30-60 DTE: FF ≥ 0.23
- 30-90 DTE: FF ≥ 0.23
- 60-90 DTE: FF ≥ 0.20

**Returns Turn Positive:** Around FF ≥ 0.10 to 0.20

## 5) Notes / caveats

- **Production** environment is required for live Greeks & market data. Sandbox returns little/no live data.
- If one of call/put IVs is missing, the script uses the leg that arrived.
- You can widen `--dte-tolerance` if you want more leeway around targets like 30/60/90.
- This script only computes IV/FF. It does not place orders.

## 6) Uninstall

```bash
python -m pip uninstall tastytrade
```
