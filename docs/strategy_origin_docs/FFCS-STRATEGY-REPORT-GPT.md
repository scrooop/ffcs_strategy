# Forward Factor Calendar Spread — Trader’s Reference (From Video Transcript)

**Source:** “This Simple Options Strategy Crushes SPY (27% CAGR, 2.4 Sharpe)” — Volatility Vibes.  
**Transcript date:** Oct 19, 2025.  
**Scope of this document:** An organized, implementation‑ready reference compiled strictly from the video transcript. No external data or opinions are added.

> **One‑line summary:** Use a **rule‑based long calendar (or double calendar) spread** only when the **Forward Factor (FF)** is sufficiently high. Enter, then **hold until just before the front expiry**, close the spread, and redeploy into fresh high‑FF signals.

---


> **DEFINITION BOX — “Front IV” (explicit; double‑calendar method is ambiguous in source)**  
> - **ATM Calendar:** *Front IV* = the **ATM (≈50Δ) option IV** for the **front expiry** at the **anchor strike** you will trade (same strike used in back expiry). A common robust proxy is the **ATM straddle mid‑IV** or the **50Δ call IV**—pick one and **use it consistently** across front/back expiries.  
> - **Double Calendar (±35Δ):** The transcript does **not** specify whether to compute FF per wing or from wing averages. Use one of the two consistent rules below and keep it consistent with your thresholds:
>   - **Option A — Per‑wing FF (strict/transparent):**  
>     Compute IV at **+35Δ call strike** and **−35Δ put strike** for **front (T1)** and **back (T2)**. For each wing **separately**:  
>     • Forward variance = \\((IV_{back}^2\\,T_2 - IV_{front}^2\\,T_1)/(T_2-T_1)\\) (with **T in years**).  
>     • Forward IV = sqrt(forward variance).  
>     • **FF_call** = \\((IV^{front}_{call} - IV^{fwd}_{call})/IV^{fwd}_{call}\\)**; **FF_put** analogously.  
>     Apply your entry rule to **both FFs** (e.g., both ≥ threshold, or use min/avg rule you define up‑front).
>   - **Option B — Averaged wings FF (compact/simpler):**  
>     Average the **front wing IVs**: \\(IV^{front}_{avg} = (IV^{front}_{call}+IV^{front}_{put})/2\\).  
>     Average the **back wing IVs** similarly. Use the averages in the forward‑variance formula to get **IV^{fwd}_{avg}**, then **FF_avg = (IV^{front}_{avg} - IV^{fwd}_{avg})/IV^{fwd}_{avg}** (single number).
> - **Earnings (ex‑earn IV):** If scheduled earnings fall between now and either expiry and you’re **not** excluding them, use **ex‑earn IV** (earnings effect removed) for *both* expiries so the term‑structure comparison is apples‑to‑apples.
> - **Units:** Always convert **DTE → years** for \(T_1, T_2\).


## 1) Executive Summary

- **Edge:** Harvest **term‑structure misalignment** in implied volatility (IV). The **forward implied volatility** between two expiries is often **mispriced** relative to the front period IV. A **positive FF** (front IV \> forward IV) signals **backwardation** and a favorable setup for a **long calendar** (long forward vol).  
- **Trade structures:**  
  1) **ATM Call Calendar** (sell front ATM call; buy back ATM call).  
  2) **35‑Delta Double Calendar** (sell ~+35Δ call & −35Δ put in front; buy same strikes in back).  
- **Expiries:** Tested pairs **30–60**, **30–90**, **60–90 DTE**, with **±5 DTE buffer**.  
- **Core rule:** **Enter only when FF exceeds a threshold.** Hold to **just before** front expiry, **close as a spread**.  
- **Why it works:** Options flow crowds **near‑dated** expiries (hedging/speculation), pushing **front IV** “too hot” vs the forward slice implied by the curve. **Calendars isolate forward vol**, letting you buy it **cheaply** when FF is high.  
- **Earnings:** Use **ex‑earn IV** (earnings effect stripped) or **avoid earnings** between entry and back expiry to keep apples‑to‑apples term‑structure comparisons.  
- **Sizing:** Favor **fractional Kelly (¼ or less)**; allocate **2–8%** per position (≈4% default). Rank by **highest FF**.  
- **Backtests (19 yrs, realistic frictions/caps):** All structures/pairs flip from negative when traded blindly to **positive when filtered by FF**, with **60–90 DTE** often the strongest blend of **CAGR and Sharpe**.

---

## 2) Key Concepts & Formulas

### 2.1 Forward Volatility (concept)
- Think in **variance** because **variances add through time**. If T1 is the front expiry and T2 is the back expiry, the **forward variance** between T1→T2 is the piece that, when added to the front variance, equals the back variance.

### 2.2 Definitions
- \( \sigma_1 \): annualized IV for **front** period; time to expiry \(T_1\) in **years**.  
- \( \sigma_2 \): annualized IV for **back** period; time to expiry \(T_2\) in **years** (\(T_2>T_1\)).  
- Variances: \( V_1 = \sigma_1^2,\; V_2 = \sigma_2^2 \).

### 2.3 Forward variance & forward volatility
- **Forward variance (annualized) over T1→T2:**  
  \[ V_{fwd} = \frac{V_2\,T_2 - V_1\,T_1}{T_2 - T_1} \]
- **Forward volatility:** \(\sigma_{fwd} = \sqrt{V_{fwd}}\).  
- **Time units:** **Always in years** (e.g., 30 days = 30/365).

### 2.4 Worked example (from transcript)
- Given **30‑day IV = 45%**, **60‑day IV = 35%**.  
- Forward vol between 30→60 is **~20.6%** (implied).  
- If front is 45% now but the implied 30‑day vol after roll is **~20.6%**, that’s steep **backwardation** and a **high FF** setup.

### 2.5 Forward Factor (FF)
- **Definition:**  
  \[ \text{FF} = \frac{\text{front IV} - \sigma_{fwd}}{\sigma_{fwd}} \]
- **Interpretation:**  
  - **FF \> 0:** front IV \> forward IV → typically **backwardation** → favors **long calendar** (long forward vol).  
  - **FF \< 0:** front IV \< forward IV → typically **contango** → weaker for long calendars.  
- **Earnings adjustment:** Use **ex‑earn IV** or **avoid earnings**; otherwise front IV may be **juiced** and comparisons distorted.

---

## 3) Trade Structures & Mechanics

### 3.1 Long Calendar = **Long Forward Vol**
- **Construction:** **Sell** front expiry, **buy** back expiry, typically **same strike** (ATM) or **wings** (~±35Δ) for a **double calendar**.
- **Intuition via variance additivity:** Back = Front + Forward. Selling Front and buying Back **removes Front exposure**, leaving you **long the Forward slice**.

### 3.2 Structures
- **ATM Call Calendar:** cleanest proxy to forward vol; simplest execution/costs.  
- **35Δ Double Calendar (calls & puts):** sells **richer front skew** and owns **cheaper back skew**; **wider profit tent**, **higher win rate**, but **more legs/costs**.

### 3.3 Expiry pairs & buffers
- Use **30–60**, **30–90**, **60–90 DTE** targets; allow **±5 DTE** so listings like 29/32 days still qualify.

### 3.4 Liquidity filter
- Trade names with **20‑day average option volume ≥ 10,000 contracts/day** (practical fills/capacity).

### 3.5 Path dependency & loss bound
- Large price moves can push P&L **outside the tent**; forward‑vol sensitivity **fades** there.  
- **Worst loss ≈ debit paid**, but measured losses **can print \< −100%** due to **slippage/commissions** on entry + exit (artifact, not broker taking more than debit).

---

## 4) Entry Criteria (FF thresholds)

### 4.1 Thresholds that flip mean returns positive
| Structure | DTE Pair | FF threshold → positive mean |
|---|---|---|
| ATM Call Calendar | 30–60 | **> 0.14** |
| ATM Call Calendar | 30–90 | **> 0.03** |
| ATM Call Calendar | 60–90 | **> 0.41** |
| 35Δ Double Calendar | 30–60 | **> 0.11** |
| 35Δ Double Calendar | 30–90 | **> 0.01** |
| 35Δ Double Calendar | 60–90 | **> 0.14** |

**Rule of thumb:** **FF ≥ 0.20** is typically tradable (using ex‑earn IV or avoiding earnings).

### 4.2 “~20 trades/month” calibrated thresholds (practical throughput)
| Structure | DTE Pair | Adjusted FF | Mean Return | Win Rate | Trades / mo |
|---|---:|---:|---:|---:|---:|
| ATM | 30–60 | **0.23** | **13.9%** | 47.8% | 20 |
| ATM | 30–90 | **0.23** | **9.3%** | 50.3% | 19 |
| ATM | 60–90 | **0.20** | **24.7%** | 45.4% | 21 |
| Double | 30–60 | **0.23** | **14.2%** | 56.0% | 20 |
| Double | 30–90 | **0.23** | **10.4%** | 57.9% | 19 |
| Double | 60–90 | **0.20** | **22.6%** | 55.8% | 21 |

> **Earnings filter:** Prefer **no earnings** between entry and back expiry; otherwise ensure **ex‑earn IV** is used consistently when computing FF.

---

## 5) Sizing & Portfolio Construction

### 5.1 Fractional Kelly (preferred)
- Reported **Kelly fractions** (per bucket):  
  - **ATM:** 30–60 **16.1%**, 30–90 **20.1%**, 60–90 **18.4%**.  
  - **Double:** 30–60 **25.7%**, 30–90 **31.5%**, 60–90 **29.1%**.
- **Practice:** Use **fractional Kelly** (¼ or less). Smaller bets → **higher Sharpe**, smoother equity, modest CAGR give‑up.

### 5.2 Position sizing & allocation
- **Per‑position cap:** **2–8%** of equity (**~4% default**).  
- **Ranking:** Allocate to **highest FF first** until portfolio is full.  
- **Exit:** **Close as a spread** just **before** front expiry to avoid pin/expiry frictions.

---

## 6) Backtest Summary (19 years, realistic frictions/caps)

> Tests cover >300k spread instances across buckets with liquidity filters, slippage/commissions, and capacity limits. Blind “always trade” calendars are **negative** on average; **FF‑filtered** calendars flip **positive** with robust profiles.

### 6.1 **Full Kelly**
| Structure | DTE Pair | CAGR | Sharpe |
|---|---|---:|---:|
| ATM | 30–60 | **21.5%** | **1.58** |
| ATM | 30–90 | **22.6%** | **1.93** |
| ATM | 60–90 | **28.0%** | **1.72** |
| Double | 30–60 | **21.9%** | **2.11** |
| Double | 30–90 | **21.5%** | **1.97** |
| Double | 60–90 | **27.0%** | **2.27** |

### 6.2 **Half Kelly**
| Structure | DTE Pair | CAGR | Sharpe |
|---|---|---:|---:|
| ATM | 30–60 | **20.5%** | **1.92** |
| ATM | 30–90 | **21.9%** | **2.06** |
| ATM | 60–90 | **27.8%** | **1.97** |
| Double | 30–60 | **21.5%** | **2.07** |
| Double | 30–90 | **21.4%** | **≈2.0** *(Sharpe value truncated in transcript)* |
| Double | 60–90 | **27.0%** | **2.38** |

### 6.3 **Quarter Kelly**
| Structure | DTE Pair | CAGR | Sharpe |
|---|---|---:|---:|
| ATM | 30–60 | **16.9%** | **2.37** |
| ATM | 30–90 | **20.0%** | **2.64** |
| ATM | 60–90 | **26.7%** | **2.40** |
| Double | 30–60 | **20.0%** | **2.31** |
| Double | 30–90 | **20.3%** | **2.34** |
| Double | 60–90 | **26.5%** | **2.42** |

**Practical takeaways:**  
- **60–90 DTE** often best blend of **CAGR & Sharpe** across structures.  
- **Double calendars** often show **slightly higher Sharpe** (skew harvest + wider tent) with more legs/cost.  
- **Fractional Kelly (¼)** often **maximizes Sharpe** with only modest CAGR reduction.

---

## 7) Step‑by‑Step Playbook (Explicit Pipelines)

### 7.1 Common Pre‑Checks
1. **Liquidity filter:** underlying has **≥ 10k options/day (20‑day avg)**.  
2. **Earnings policy:** either **exclude earnings** between entry and back expiry **or** use **ex‑earn IV** consistently.  
3. **Pick expiries:** choose **30–60**, **30–90**, or **60–90 DTE** pairs (**±5 DTE** buffer ok). Convert DTE to **years** for \(T_1, T_2\).

### 7.2 ATM Call Calendar (same‑strike ATM)
1. **Anchor strike:** choose the **ATM (≈50Δ)** strike to be used for **both expiries**.  
2. **Collect IVs:** read **IV_front = IV(K_{ATM}, T_1)** and **IV_back = IV(K_{ATM}, T_2)**. (Use **50Δ call IV** or **ATM straddle mid‑IV**—be consistent across both expiries and all names.)  
3. **Compute forward vol:**  
   \[ V_{fwd} = \frac{IV_{back}^2\,T_2 - IV_{front}^2\,T_1}{T_2 - T_1},\quad IV_{fwd} = \sqrt{V_{fwd}} \]
4. **Forward Factor (FF):**  
   \[ FF = \frac{IV_{front} - IV_{fwd}}{IV_{fwd}} \]
5. **Entry filter:** Enter only if **FF ≥ threshold** for your chosen DTE pair (see Section 4).  
6. **Build & size:** **Sell** front ATM call, **buy** back ATM call (same strike). Size **2–8%** of equity (≈**4%** default), **≤ ¼ Kelly**.  
7. **Exit:** **Close the spread** just **before** front expiry; redeploy into next high‑FF signals.

### 7.3 Double Calendar (±35Δ wings)
**Pick one rule and stick to it.**

**Option A — Per‑wing FF (strict/transparent):**
1. **Anchor strikes:** determine **+35Δ call** strike \(K_c\) and **−35Δ put** strike \(K_p\) for both expiries.  
2. **Collect IVs:**  
   - Front: \(IV^{front}_{call} = IV(K_c, T_1),\; IV^{front}_{put} = IV(K_p, T_1)\)  
   - Back:  \(IV^{back}_{call}  = IV(K_c, T_2),\; IV^{back}_{put}  = IV(K_p, T_2)\)  
3. **Compute forward vols per wing:**  
   - Call: \(V^{fwd}_{call} = (IV^{back}_{call}{}^2 T_2 - IV^{front}_{call}{}^2 T_1)/(T_2-T_1),\; IV^{fwd}_{call} = \sqrt{\cdot}\)  
   - Put:  \(V^{fwd}_{put}  = (IV^{back}_{put}{}^2  T_2 - IV^{front}_{put}{}^2  T_1)/(T_2-T_1),\; IV^{fwd}_{put}  = \sqrt{\cdot}\)  
4. **Compute FF per wing:**  
   - \(FF_{call} = (IV^{front}_{call} - IV^{fwd}_{call})/IV^{fwd}_{call}\)  
   - \(FF_{put}  = (IV^{front}_{put}  - IV^{fwd}_{put}) /IV^{fwd}_{put} \)  
5. **Entry filter:** require your rule (e.g., **both ≥ threshold**, or **min(FF_{call}, FF_{put}) ≥ threshold**).  
6. **Build & size:** **Sell** front +35Δ call & −35Δ put; **buy** same strikes in back. Size **2–8%**, **≤ ¼ Kelly**.  
7. **Exit:** **Close as a spread** just **before** front expiry; redeploy.

**Option B — Averaged wings FF (compact/simpler):**
1. **Anchor strikes:** as above (\(K_c, K_p\)).  
2. **Average IVs:**  
   - Front average: \(IV^{front}_{avg} = (IV^{front}_{call} + IV^{front}_{put})/2\)  
   - Back  average: \(IV^{back}_{avg}  = (IV^{back}_{call}  + IV^{back}_{put})/2\)  
3. **Forward vol from averages:**  
   \(V^{fwd}_{avg} = (IV^{back}_{avg}{}^2 T_2 - IV^{front}_{avg}{}^2 T_1)/(T_2-T_1),\; IV^{fwd}_{avg} = \sqrt{\cdot}\)  
4. **FF from averages:**  
   \(FF_{avg} = (IV^{front}_{avg} - IV^{fwd}_{avg})/IV^{fwd}_{avg}\)  
5. **Entry filter:** **FF_{avg} ≥ threshold** for your chosen DTE pair.  
6. **Build & size:** Construct the **double calendar** at \(K_c\) and \(K_p\); size as above.  
7. **Exit:** **Close as a spread** just **before** front expiry; redeploy.


## 8) Real Trade Example (from transcript)

- **Ticker:** AES (screened as top FF).  
- **Earnings:** Est. Oct 30 → choose expiries that **end before earnings**.  
- **Legs (ATM):**  
  - **Sell:** Oct 17 (≈10 DTE) **14.5C** at **IV 61.97%**, price **$0.51**.  
  - **Buy:** Oct 24 (≈17 DTE) **14.5C** at **IV 52.11%**, price **$0.61**.  
- **Net debit:** **$0.10**.  
- **Computed:** **σ_fwd ≈ 33.37%**, **FF ≈ 86%** → **well above** 0.20 threshold.  
- **Plan:** **Hold** until **Oct 17** front expiry; **close spread** just before close.

This illustrates FF’s value in finding **extremely cheap calendars** when the forward slice is underpriced.

---

## 9) Practical Notes, Pitfalls & Variations

- **Slippage near expiry:** Markets widen; **close as a spread** just before front expiry.  
- **Path dependence:** Large price moves can push P&L beyond the tent; forward‑vol sensitivity diminishes there.  
- **Structure choice:** Differences between ATM vs Double are **modest**; **ATM** is simpler/cheaper to execute.  
- **Not tied to a specific pair:** The **FF signal generalizes** to many T1/T2 combinations (e.g., 7–14, 10–30, 12–21, etc.).  
- **Sizing robustness:** **Smaller, more numerous bets** across names → smoother equity and higher risk‑adjusted returns.

---

## 10) Glossary

- **Implied Volatility (IV):** Market‑implied annualized standard deviation of returns.  
- **Forward Volatility:** The **implied volatility** over a **future window** (T1→T2) implied by two expiries.  
- **Forward Factor (FF):** Relative gap between **front IV** and **forward IV**; **FF \> 0** = front hotter than forward.  
- **Backwardation/Contango:** Down‑sloping vs up‑sloping IV term structure.  
- **Calendar Spread:** Sell front, buy back (same strike) → proxy for **forward vol**.  
- **Double Calendar:** Two calendars at wing strikes (~±35Δ) to harvest skew and widen the tent.  
- **Ex‑earn IV:** IV with **scheduled earnings effect removed** to normalize term‑structure comparisons.  
- **Kelly Fraction:** Optimal growth fraction from Kelly criterion; **fractional Kelly** used in practice.

---

## 11) Implementation Checklist (Copy/Paste)

- [ ] Symbol passes **liquidity** filter (≥10k options/day).  
- [ ] **No earnings** or using **ex‑earn IV** consistently.  
- [ ] Choose **30–60 / 30–90 / 60–90** DTE pair (±5 buffer).  
- [ ] Compute **σ_fwd** and **FF** in **years**.  
- [ ] **Enter only if FF ≥ threshold** (e.g., 0.20 or Section 4 values).  
- [ ] Build **ATM calendar** (or **35Δ double**).  
- [ ] **Size** 2–8% (≈4%) ≤ **¼ Kelly**; rank by **highest FF**.  
- [ ] **Hold**; **close spread** just before **front expiry**.  
- [ ] **Redeploy** into next **high‑FF** names.

---

### Disclaimer
This reference **reproduces and organizes** the strategy description, examples, and statistics **as provided in the source transcript**. It is **not financial advice**. Performance metrics are from historical backtests described in that transcript and **may not reflect live results**.
