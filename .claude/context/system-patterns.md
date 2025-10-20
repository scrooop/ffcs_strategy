---
created: 2025-10-20T18:58:52Z
last_updated: 2025-10-20T18:58:52Z
version: 1.0
author: Claude Code PM System
---

# System Patterns and Architecture

## Architectural Style

### CLI-First Design
**Pattern:** Command-Line Interface application with no GUI
**Rationale:**
- Simple, direct access for traders
- Scriptable and automatable
- No UI complexity overhead
- Fast iteration and testing

### Stateless Scanner
**Pattern:** Each scanner run is independent, no persistent state
**Rationale:**
- Market data changes constantly
- No data staleness concerns
- Simple operational model
- Easy to test and debug

**Exception:** Earnings cache is stateful (performance optimization)

### Functional Pipeline Architecture
**Pattern:** Data flows through processing stages sequentially

```
Input (CLI args)
  ↓
Authentication
  ↓
Pre-filtering (Earnings cache)
  ↓
Market Data Fetching (API calls)
  ↓
Greeks Streaming (dxFeed)
  ↓
Strike Selection (Delta-based)
  ↓
Forward IV Calculation (Variance decomposition)
  ↓
Quality Filtering (Earnings, volume, liquidity)
  ↓
Output (CSV/JSON)
```

## Core Design Patterns

### 1. Multi-Source Data Pipeline (Earnings)
**Pattern:** Cascading fallback with caching

```
Cache (SQLite)
  ├─ Hit (>90% rate) → Return immediately
  └─ Miss → Fetch from sources
      ├─ 1. Yahoo Finance (primary, ~100ms)
      ├─ 2. TastyTrade API (fallback, ~500ms)
      └─ 3. Graceful degradation (allow through with warning)
```

**Benefits:**
- 80-95% runtime reduction
- Resilient to single-source failures
- Transparent data provenance (tracked in CSV)

**Implementation:**
```python
def fetch_earnings_date(symbol):
    # Check cache first
    if cached := cache.get(symbol):
        return cached

    # Try Yahoo Finance
    try:
        return fetch_yahoo_earnings(symbol)
    except:
        pass

    # Fallback to TastyTrade
    try:
        return fetch_tastytrade_earnings(symbol)
    except:
        return None  # Allow through
```

### 2. Async Streaming with Timeout
**Pattern:** Asyncio-based event collection with graceful timeout

```python
async def snapshot_greeks(session, symbols, timeout=3.0):
    streamer = await DXLinkStreamer.create(session)
    await streamer.subscribe(Greeks, symbols)

    results = {}
    try:
        # Collect events until timeout
        async with asyncio.timeout(timeout):
            while len(results) < len(symbols):
                event = await streamer.get_event()
                results[event.eventSymbol] = event
    except asyncio.TimeoutError:
        # Return partial results (graceful degradation)
        pass

    return results
```

**Benefits:**
- Non-blocking data collection
- Partial results accepted (better than all-or-nothing)
- Configurable timeout per use case

### 3. Delta-Based Strike Selection
**Pattern:** Find strikes by target delta, not price

**ATM Strike Selection:**
```python
def pick_atm_strike(chain, target_delta=0.50):
    """Select strike with delta closest to 50Δ (ATM)"""
    best_strike = None
    min_delta_diff = float('inf')

    for strike in chain:
        delta_diff = abs(abs(strike.delta) - target_delta)
        if delta_diff < min_delta_diff:
            min_delta_diff = delta_diff
            best_strike = strike

    return best_strike
```

**Double Calendar Strike Selection:**
```python
def pick_delta_strike(chain, target_delta, tolerance=0.05):
    """Select strike with delta within tolerance of target"""
    for strike in chain:
        if abs(abs(strike.delta) - target_delta) <= tolerance:
            return strike
    return None  # No strike within tolerance
```

**Benefits:**
- More accurate than price-based selection
- Accounts for volatility and time decay
- Aligns with options theory (delta = probability)

### 4. Variance Decomposition (Forward IV)
**Pattern:** Mathematical decomposition of implied variance

**Formula:**
```
σ_fwd² = (σ₂² T₂ - σ₁² T₁) / (T₂ - T₁)

Where:
- σ₁ = Front expiration IV (decimal, e.g., 0.25 = 25%)
- σ₂ = Back expiration IV
- T₁ = Front DTE / 365
- T₂ = Back DTE / 365
- σ_fwd = Forward IV between T₁ and T₂
```

**Forward Factor:**
```
FF = (σ₁ - σ_fwd) / σ_fwd

Interpretation:
- FF > 0.20 → Front IV "hot" relative to forward IV (trade opportunity)
- FF < 0 → Front IV "cold" (no backwardation, skip)
```

**Implementation:**
```python
def calculate_forward_iv(iv_front, iv_back, dte_front, dte_back):
    T1 = dte_front / 365.0
    T2 = dte_back / 365.0

    # Variance decomposition
    fwd_var = (iv_back**2 * T2 - iv_front**2 * T1) / (T2 - T1)

    # Handle negative variance (rare edge case)
    if fwd_var < 0:
        return None

    return math.sqrt(fwd_var)

def calculate_forward_factor(iv_front, fwd_iv):
    return (iv_front - fwd_iv) / fwd_iv
```

### 5. Hybrid Filtering System
**Pattern:** Two-mode filtering based on availability and precision needs

**Default Mode (24/7 available):**
```python
def check_liquidity_rating(metrics):
    """Use liquidity rating (0-5 scale) from Market Metrics API"""
    return metrics.liquidity_rating >= 3  # ~10k volume equivalent
```

**Precise Mode (market hours only):**
```python
def check_option_volume(underlying, threshold=10000):
    """Use dxFeed Underlying.optionVolume (today's total chain volume)"""
    return underlying.optionVolume >= threshold
```

**Benefits:**
- Default mode works 24/7 (pre-market scanning)
- Precise mode available during market hours
- User controls tradeoff (convenience vs precision)

### 6. Structure-Based Scanning
**Pattern:** Polymorphic scanning for different calendar structures

**ATM Structure:**
```python
def scan_atm_calendar(symbol, front_dte, back_dte):
    """Single calendar at 50Δ ATM strike"""
    atm_strike = pick_atm_strike(chain, target_delta=0.50)

    # Average call and put IV at ATM strike
    atm_iv_front = (call_iv + put_iv) / 2
    atm_iv_back = (call_iv_back + put_iv_back) / 2

    # Calculate single FF
    fwd_iv = calculate_forward_iv(...)
    atm_ff = calculate_forward_factor(atm_iv_front, fwd_iv)

    return {"atm_ff": atm_ff, "atm_strike": atm_strike, ...}
```

**Double Calendar Structure:**
```python
def scan_double_calendar(symbol, front_dte, back_dte):
    """Two calendars: +35Δ call and -35Δ put"""
    call_strike = pick_delta_strike(chain, target_delta=0.35)
    put_strike = pick_delta_strike(chain, target_delta=0.35, call=False)

    # Require BOTH legs within tolerance
    if not call_strike or not put_strike:
        return None  # Skip symbol

    # Separate FF calculations for each leg
    call_ff = calculate_forward_factor(call_iv_front, call_fwd_iv)
    put_ff = calculate_forward_factor(put_iv_front, put_fwd_iv)

    # Conservative filtering uses minimum FF
    min_ff = min(call_ff, put_ff)
    combined_ff = (call_ff + put_ff) / 2

    return {
        "call_ff": call_ff,
        "put_ff": put_ff,
        "min_ff": min_ff,
        "combined_ff": combined_ff,
        ...
    }
```

**Benefits:**
- Clear separation of concerns
- Structure-specific logic isolated
- Easy to add new structures (iron condor, butterfly, etc.)

## Data Flow Patterns

### 1. Batch-Then-Stream Pattern
**Usage:** Market metrics fetching

```python
# Batch fetch for ALL symbols upfront
all_metrics = fetch_market_metrics(session, tickers)

# Then stream Greeks per symbol (sequential)
for ticker in tickers:
    greeks = await snapshot_greeks(session, ticker)
    process_symbol(ticker, greeks, all_metrics[ticker])
```

**Benefits:**
- Reduce API calls (1 batch vs N individual)
- Pre-filter before expensive operations
- Fast early rejection (earnings conflicts)

### 2. Fail-Fast Validation
**Pattern:** Check cheap filters first, expensive operations last

```
1. Check cache (< 10ms) → Skip if earnings conflict
2. Fetch market metrics (batch, ~1s total) → Skip if low liquidity
3. Fetch option chain (~500ms) → Skip if no expirations
4. Stream Greeks (3s timeout) → Most expensive, done last
```

### 3. Graceful Degradation
**Pattern:** Accept partial data rather than complete failure

**Examples:**
1. **Greeks Timeout:** Use partial results if some strikes arrived
2. **Earnings Missing:** Allow through with warning (don't block entire symbol)
3. **Volume Data Missing:** Futures often lack volume data, allow through
4. **Ex-earn IV Fallback:** Use Greeks IV (primary), fallback to ex-earn IV if missing

## Error Handling Patterns

### 1. Timeout with Partial Results
```python
try:
    async with asyncio.timeout(3.0):
        results = await fetch_all_greeks(symbols)
except asyncio.TimeoutError:
    # Accept partial results
    logger.warning(f"Greeks timeout, got {len(results)}/{len(symbols)}")
    return results  # Return what we have
```

### 2. Multi-Source Fallback
```python
try:
    data = fetch_primary_source()
except Exception:
    try:
        data = fetch_fallback_source()
    except Exception:
        data = None  # Graceful degradation
        logger.warning("All sources failed")
```

### 3. Skip Tracking
**Pattern:** Track why symbols are filtered out

```python
skip_reasons = {}

if earnings_conflict(symbol):
    skip_reasons[symbol] = "earnings_conflict"
    continue

if volume_too_low(symbol):
    skip_reasons[symbol] = "volume_too_low"
    continue

# ... process symbol ...

# Export skip reasons to CSV
for symbol, reason in skip_reasons.items():
    csv_row["skip_reason"] = reason
```

**Benefits:**
- Debugging visibility
- Understanding filter impact
- Tuning threshold decisions

## Code Organization Patterns

### 1. Single-File Monolith (Current)
**Pattern:** All scanner logic in `ff_tastytrade_scanner.py`
**Size:** ~1000 lines

**Sections:**
- Authentication
- Data fetching functions
- Calculation functions
- Strike selection functions
- Quality filtering functions
- Output functions
- CLI argument parsing
- Main execution

**Benefits:**
- Simple to understand (no module hunting)
- Easy to debug (single file)
- Fast iteration

**Drawbacks:**
- Growing file size
- Mixing concerns
- Harder to test in isolation

### 2. Separate Cache Module (Extracted)
**Pattern:** `earnings_cache.py` as standalone module
**Rationale:**
- Complex logic (multi-source, SQLite)
- Reusable across projects
- Isolated testing

### 3. Inline Test Scripts
**Pattern:** `test_*.py` scripts for feature validation
**Characteristics:**
- Standalone scripts, not formal test suite
- Quick validation during development
- Manual execution

## Scalability Patterns

### 1. Streaming CSV Writer (v2.3)
**Pattern:** Write rows incrementally, not batch

**Before (v2.2):**
```python
results = []
for symbol in symbols:
    result = scan_symbol(symbol)
    results.append(result)

write_csv(results)  # Write all at once
```

**After (v2.3):**
```python
csv_writer = StreamingCSVWriter(output_file)
csv_writer.write_header()

for symbol in symbols:
    result = scan_symbol(symbol)
    csv_writer.write_row(result)  # Write immediately

csv_writer.close()
```

**Benefits:**
- Constant memory usage
- Supports 1500+ symbol scans
- Faster time-to-first-result

### 2. Early Rejection
**Pattern:** Filter before expensive operations

```
1000 symbols
  ↓ Earnings check (cache) → 800 symbols remain
  ↓ Liquidity rating check → 600 symbols remain
  ↓ Greeks streaming (3s each) → 600 × 3s = 30 minutes
```

Without early rejection:
```
1000 symbols × 3s = 50 minutes
```

**Savings:** 40% time reduction

## Future Architectural Patterns (Planned)

### 1. Plugin Architecture (v3.0+)
**Pattern:** Extensible structure support

```python
class CalendarStructure(ABC):
    @abstractmethod
    def scan(self, symbol, chain, greeks):
        pass

class ATMCalendar(CalendarStructure):
    def scan(self, symbol, chain, greeks):
        # ATM-specific logic
        pass

class DoubleCalendar(CalendarStructure):
    def scan(self, symbol, chain, greeks):
        # Double-specific logic
        pass

# Register structures
structures = [ATMCalendar(), DoubleCalendar(), IronCondor()]
```

### 2. Async Symbol Processing (v3.0+)
**Pattern:** Parallel symbol scanning

```python
async def scan_symbols_parallel(symbols):
    tasks = [scan_symbol(symbol) for symbol in symbols]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results
```

**Benefits:**
- 5-10x speedup for large scans
- Better API utilization
- Requires careful rate limiting

### 3. Modular Filtering Pipeline (v3.0+)
**Pattern:** Composable filter chain

```python
filters = [
    EarningsFilter(allow_earnings=False),
    LiquidityFilter(min_rating=3),
    VolumeFilter(min_volume=10000),
    DeltaToleranceFilter(tolerance=0.05)
]

for symbol in symbols:
    for filter in filters:
        if not filter.check(symbol):
            skip_reasons[symbol] = filter.name
            break
```

## Testing Patterns

### Current Approach
1. **Unit Tests:** Core calculation functions (`tests/test_ff_calculations.py`)
2. **Integration Tests:** Standalone test scripts (`scripts/test_*.py`)
3. **Manual Testing:** Live scanner runs with small ticker lists

### Future Testing (Planned)
1. **Mock API Responses:** Deterministic testing without live API
2. **Regression Tests:** CSV output validation
3. **Performance Tests:** Large scan benchmarks
4. **CI/CD Integration:** Automated test runs on commit
