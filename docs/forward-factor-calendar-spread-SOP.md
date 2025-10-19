# Forward Factor Calendar Spread Strategy — SOP

A step‑by‑step, repeatable process for trading **forward volatility** using listed options calendars/double‑calendars, as described in the transcript. Designed so a competent options trader can run it daily with minimal discretion.

---

## 0) Overview (What you’re doing)
- **Trade type:** Long **calendar** (ATM calls) *or* long **double‑calendar** (±35Δ calls & puts).
- **Edge/Signal:** **Forward Factor (FF)** — how “hot” front‑month IV is vs **forward IV** (implied for the next window).
- **When to trade:** Only when **FF ≥ threshold** (see §4). Hold the spread **until the front expiry day**, then **close the spread**.
- **Why it works:** Short‑dated options often get bid up (backwardation) while the next window is underpriced; calendars isolate and buy that forward slice at a discount.
- **Sizing:** Use **fractional Kelly (≈¼‑Kelly)** or a **fixed 2–8%** of equity per position (4% typical).

---

## 1) Inputs you need each day
1. **Universe / Liquidity filter**
   - Equities/ETFs with **20‑day avg option volume > 10k** contracts/day.
2. **Two expirations per trade**
   - Target DTE pairs: **30‑60**, **30‑90**, **60‑90** (±5 DTE buffer acceptable).
3. **Implied volatilities** for each target expiry (prefer **ex‑earnings IV**; or simply avoid earnings in the window).
4. **Earnings dates** for each ticker (to exclude trades that span earnings unless you have true ex‑earnings IV).

---

## 2) Compute Forward IV and Forward Factor (FF)
Let:
- \(\sigma_1\): annualized IV for the **front** expiry (time to expiry \(T_1\) in **years**).
- \(\sigma_2\): annualized IV for the **back** expiry (time to expiry \(T_2>T_1\) in **years**).

**Forward variance** between \(T_1\) and \(T_2\):
\[
\operatorname{Var}_{fwd} = \frac{\sigma_2^2\,T_2 - \sigma_1^2\,T_1}{T_2 - T_1}
\]

**Forward IV**:
\[
\sigma_{fwd} = \sqrt{\operatorname{Var}_{fwd}}
\]

**Forward Factor (FF):**
\[
\mathrm{FF} = \frac{\sigma_1 - \sigma_{fwd}}{\sigma_{fwd}}
\]
- **Interpretation:** FF > 0 ⇒ front IV “hot” vs forward IV (backwardation) ⇒ **go long forward vol** (via long calendar).

> **Time units:** Convert DTE to years, e.g., 30 days → 30/365, 60 days → 60/365.

---

## 3) Pre‑trade checks
- **No earnings** between **today and the back expiry** (or use **ex‑earnings IV**).
- **DTE buffers ok:** if the chain lists 29/32/etc, treat as 30 within ±5 DTE.
- **Capacity & fills:** avoid names with thin OI/volume; cap per‑name contracts if needed.

---

## 4) Forward Factor thresholds (actionable)
- **General, simple rule of thumb:** **FF ≥ 0.20** is typically tradable.
- Thresholds tuned for ~**≈20 trades/month** (per DTE pair & structure):
  - **ATM Call Calendar:** 
    - **30‑60:** FF ≈ **0.23**
    - **30‑90:** FF ≈ **0.23**
    - **60‑90:** FF ≈ **0.20**
  - **Double‑Calendar (±35Δ calls & puts, ±5Δ ok):**
    - **30‑60:** FF ≈ **0.23**
    - **30‑90:** FF ≈ **0.23**
    - **60‑90:** FF ≈ **0.20**

> Empirically, **60‑90 DTE** buckets often show the best blend of CAGR & Sharpe; double‑calendars tend to have slightly higher win rates, with somewhat higher costs/complexity.

---

## 5) Entry rules (mechanical)
1. **Choose structure:**
   - **Simple:** ATM **call calendar** (same strike, sell front/buy back).
   - **Alternative:** **Double‑calendar** at **+35Δ call** and **−35Δ put** (front sold; back bought).
2. **Pick expirations:** One of **30‑60 / 30‑90 / 60‑90** (±5 DTE ok).
3. **Compute FF** with ex‑earnings IV (or verify **no earnings** in window).
4. **Trade only if FF ≥ threshold** for the selected DTE pair/structure.
5. **Place as a spread** (limit): **Sell front**, **Buy back**; expect **net debit**.
6. **Position size:** **2–8%** of equity per trade (default **4%**), or use ≈**¼‑Kelly**. Prioritize **highest FF** names first until portfolio risk caps are met.

---

## 6) Management & exit (mechanical)
- **No adjustments** (accept path dependency).
- **Hold** until the **front contract’s expiry day**.
- **Exit:** **Close the entire spread** **just before** front expiry (avoid pin/expiry frictions). **Do not leg** unless necessary for fills.
- **Re‑deploy** freed capital into the next **highest‑FF** opportunities.

---

## 7) Risk, costs, and expectations
- **Max loss ≈ debit paid** (+ round‑trip costs); near expiry, wide markets can make measured loss slightly >100% of debit (artifact of slippage/fees).
- **Most trades small winners/losers;** outliers drive edge ⇒ stick to **signal discipline**.
- **Diversify across tickers**; smaller per‑trade sizing often **improves Sharpe** with modest CAGR impact.
- **Path risk:** Large underlier moves can push P&L outside the tent; that’s acceptable for vanilla listed options in lieu of OTC forward‑vol instruments.

---

## 8) Daily runbook (checklist)
1. **Scan liquid universe** (vol >10k/day).  
2. For each ticker, build valid **DTE pairs** (30‑60 / 30‑90 / 60‑90; ±5 ok).  
3. **Exclude earnings‑spanning pairs** (or use ex‑earnings IV).  
4. **Compute FF** for each pair/structure.  
5. **Rank by FF**; **filter FF ≥ threshold** (per §4).  
6. **Place spreads** (sell front, buy back) with **sensible limits**.  
7. **Size** each at **2–8%** (or ≈¼‑Kelly); **cap per‑name** if needed.  
8. **Log**: ticker, structure, expiries, strikes/deltas, FF, debit, size.  
9. On **front expiry day**: **close spreads** before the bell; record P&L.  
10. **Repeat**.

---

## 9) Quick example (pattern)
- Front IV (30D) high vs Back IV (60D) ⇒ computed **FF = 0.86** (>0.20).  
- **ATM call calendar**: Sell 30D ATM call; Buy 60D ATM call; small net **debit**.  
- **Hold** to 30D expiry day; **close spread**; **recycle** capital.

---

## 10) Notes & variants
- **Structure choice:** If new, start with **ATM call calendar** (simpler, cheaper to execute).  
- **Double‑calendar** can improve win rate and widen profit tent but increases contracts/fees.  
- **Any DTE pairing** works if the **term‑structure mispricing** (high FF) is present.

---

### Appendix — Minimal formulas (for a spreadsheet)
```
T1 = DTE_front/365
T2 = DTE_back/365
fwd_var = (IV2^2*T2 - IV1^2*T1)/(T2 - T1)
fwd_iv  = SQRT(fwd_var)
FF      = (IV1 - fwd_iv)/fwd_iv
```

---

**That’s it:** Compute FF → Trade only when **FF ≥ threshold** → **Hold** → **Exit on front expiry day** → **Repeat**.
