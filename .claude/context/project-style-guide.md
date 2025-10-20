---
created: 2025-10-20T18:58:52Z
last_updated: 2025-10-20T18:58:52Z
version: 1.0
author: Claude Code PM System
---

# Project Style Guide

## Code Style

### Python Conventions

#### General Style
- **PEP 8 Compliance:** Follow Python Enhancement Proposal 8 for code style
- **Line Length:** Maximum 100 characters (not strict 79)
- **Indentation:** 4 spaces (no tabs)
- **Encoding:** UTF-8 for all Python files

#### Naming Conventions
```python
# Functions and variables: snake_case
def calculate_forward_iv(iv_front, iv_back, dte_front, dte_back):
    forward_variance = compute_variance(...)
    return math.sqrt(forward_variance)

# Classes: PascalCase
class EarningsCache:
    def __init__(self, db_path):
        self.db_path = db_path

# Constants: UPPER_SNAKE_CASE
DEFAULT_TIMEOUT = 3.0
MIN_FF_THRESHOLD = 0.20

# Private methods/variables: leading underscore
def _internal_helper(data):
    pass

_private_cache = {}
```

#### Function Design
```python
# Good: Clear purpose, single responsibility
def pick_atm_strike(chain, target_delta=0.50):
    """Select strike with delta closest to 50Δ (ATM).

    Args:
        chain: List of option strikes with delta values
        target_delta: Target delta for ATM (default 0.50)

    Returns:
        Strike object with delta closest to target, or None if not found
    """
    best_strike = None
    min_delta_diff = float('inf')

    for strike in chain:
        delta_diff = abs(abs(strike.delta) - target_delta)
        if delta_diff < min_delta_diff:
            min_delta_diff = delta_diff
            best_strike = strike

    return best_strike

# Bad: Multiple responsibilities, unclear purpose
def process_data(data):
    # Does too many things: fetching, calculating, filtering, output
    pass
```

#### Error Handling
```python
# Good: Specific exceptions, graceful degradation
try:
    earnings_date = fetch_yahoo_earnings(symbol)
except requests.Timeout:
    logger.warning(f"Yahoo timeout for {symbol}, trying TastyTrade")
    try:
        earnings_date = fetch_tastytrade_earnings(symbol)
    except Exception as e:
        logger.warning(f"All earnings sources failed for {symbol}: {e}")
        earnings_date = None  # Graceful degradation

# Bad: Bare except, no logging
try:
    earnings_date = fetch_earnings(symbol)
except:
    earnings_date = None
```

#### Async Code
```python
# Good: Clear timeout, partial results accepted
async def snapshot_greeks(session, symbols, timeout=3.0):
    """Fetch Greeks snapshot from dxFeed streamer.

    Args:
        session: TastyTrade session
        symbols: List of streamer symbols to fetch
        timeout: Max wait time in seconds (default 3.0)

    Returns:
        Dict mapping symbols to Greeks events (partial results if timeout)
    """
    streamer = await DXLinkStreamer.create(session)
    await streamer.subscribe(Greeks, symbols)

    results = {}
    try:
        async with asyncio.timeout(timeout):
            while len(results) < len(symbols):
                event = await streamer.get_event()
                results[event.eventSymbol] = event
    except asyncio.TimeoutError:
        logger.warning(f"Greeks timeout, got {len(results)}/{len(symbols)}")

    return results  # Return partial results

# Bad: No timeout, blocks indefinitely
async def fetch_greeks(symbols):
    results = {}
    while len(results) < len(symbols):
        event = await streamer.get_event()
        results[event.eventSymbol] = event
    return results
```

### Docstring Style

#### Module Docstrings
```python
"""Forward Factor Calendar Spread Scanner.

This module implements a CLI scanner that identifies mispriced forward
volatility opportunities in options markets by calculating Forward Factor
(FF) ratios across multiple expirations and structures.

Key Features:
- Forward IV calculation via variance decomposition
- Multi-structure support (ATM, double calendars)
- Quality filtering (earnings, liquidity, volume)
- Fast earnings cache (80-95% speedup)

Usage:
    python ff_tastytrade_scanner.py \
        --tickers SPY QQQ AAPL \
        --pairs 30-60 \
        --min-ff 0.23 \
        --csv-out scan.csv

Author: wnv72
Version: 2.2
Last Updated: October 2025
"""
```

#### Function Docstrings (Google Style)
```python
def calculate_forward_factor(iv_front, fwd_iv):
    """Calculate Forward Factor ratio.

    Forward Factor (FF) measures how much front-month IV is elevated
    relative to forward IV. Positive FF indicates backwardation
    (calendar spread opportunity).

    Formula: FF = (σ_front - σ_fwd) / σ_fwd

    Args:
        iv_front (float): Front expiration IV (decimal, e.g., 0.25 = 25%)
        fwd_iv (float): Forward IV between front and back expirations

    Returns:
        float: Forward Factor ratio (e.g., 0.23 = 23% premium)

    Example:
        >>> calculate_forward_factor(0.25, 0.20)
        0.25  # Front IV is 25% higher than forward IV

    Note:
        - FF >= 0.20 typically indicates a tradeable opportunity
        - FF < 0 indicates contango (front IV lower than forward)
        - Returns None if fwd_iv is 0 or negative (invalid)
    """
    if fwd_iv <= 0:
        return None
    return (iv_front - fwd_iv) / fwd_iv
```

#### Class Docstrings
```python
class EarningsCache:
    """SQLite-backed cache for earnings dates with multi-source fetching.

    Implements a three-tier fetching strategy:
    1. SQLite cache (< 10ms per symbol)
    2. Yahoo Finance API (~ 100ms per symbol, primary source)
    3. TastyTrade API (~ 500ms per symbol, fallback)

    Cache automatically invalidates when earnings dates pass. Provides
    80-95% speedup for daily scanning workflows.

    Attributes:
        db_path (str): Path to SQLite database file
        cache_hit_rate (float): Percentage of cache hits (0-1)

    Example:
        cache = EarningsCache('.cache/earnings.db')
        earnings_date = cache.get_earnings_date('AAPL')
        if earnings_date:
            print(f"AAPL earnings: {earnings_date}")
    """
```

## File Organization

### Directory Structure
```
scripts/
├── ff_tastytrade_scanner.py    # Main scanner (1000+ lines, core logic)
├── earnings_cache.py            # Earnings cache module (200+ lines)
└── test_*.py                    # Test scripts (ad-hoc testing)

tests/
├── __init__.py
└── test_ff_calculations.py      # Unit tests for core calculations

docs/
├── strategy_origin_docs/        # Original research materials
├── tastytrade-openapi-docs/     # API specifications
└── tastytrade-sdk-docs/         # SDK documentation

.claude/
├── context/                     # Living project documentation
├── epics/                       # Epic-based task tracking
└── rules/                       # Project rules and standards
```

### File Naming Conventions
- **Python scripts:** `snake_case.py` (e.g., `ff_tastytrade_scanner.py`)
- **Test scripts:** `test_*.py` prefix (e.g., `test_earnings_cache.py`)
- **Documentation:** `UPPERCASE_WITH_UNDERSCORES.md` (e.g., `CLAUDE.md`)
- **Epic docs:** `lowercase-with-hyphens.md` (e.g., `execution-status.md`)
- **Timestamps:** `YYMMDD_HHMM_description` (e.g., `251020_1830_analysis.csv`)

### Import Organization
```python
# Standard library imports (alphabetical)
import asyncio
import logging
import math
import sys
from datetime import datetime, timedelta

# Third-party imports (alphabetical)
import yfinance as yf
from tastytrade import Session
from tastytrade.dxfeed import Greeks, DXLinkStreamer
from tastytrade.instruments import NestedOptionChain

# Local imports (alphabetical)
from earnings_cache import EarningsCache

# Constants
DEFAULT_TIMEOUT = 3.0
MIN_FF_THRESHOLD = 0.20
```

## Documentation Standards

### README Files
- **Purpose Statement:** What this does in 1-2 sentences
- **Quick Start:** Minimal steps to get running
- **Usage Examples:** 3-5 common use cases with commands
- **Configuration:** Required environment variables, optional flags
- **Troubleshooting:** Common issues and solutions

### Inline Comments
```python
# Good: Explain WHY, not WHAT
# Use 50Δ instead of spot-based ATM to account for volatility skew
atm_strike = pick_atm_strike(chain, target_delta=0.50)

# Calculate forward variance using variance decomposition
# Formula: σ_fwd² = (σ₂² T₂ - σ₁² T₁) / (T₂ - T₁)
fwd_var = (iv_back**2 * T2 - iv_front**2 * T1) / (T2 - T1)

# Bad: Redundant comments that just restate code
# Set x to 10
x = 10

# Call the function
result = calculate_forward_factor(iv_front, fwd_iv)
```

### CSV Schema Documentation
```python
# Always document CSV output schema in function docstrings
def write_csv(results, output_file):
    """Write scan results to CSV file.

    CSV Schema (40 columns, v2.2):
    - Common (8): timestamp, symbol, structure, spot_price, ...
    - ATM (8): atm_strike, atm_delta, atm_ff, atm_iv_*, ...
    - Double (8): call_strike, put_strike, call_ff, put_ff, ...
    - IV Details (6): call/put front/back/fwd IVs
    - IV Sources (4): iv_source_* (greeks or exearn_fallback)
    - Quality (5): earnings_conflict, earnings_date, ...
    - Tracking (1): skip_reason

    Args:
        results: List of result dictionaries
        output_file: Path to output CSV file

    Note:
        Results are sorted by atm_ff (ATM) or min_ff (double) descending.
        See CLAUDE.md for complete schema documentation.
    """
```

### Version Documentation
```python
# Document breaking changes and migration paths
"""
Version 2.2 - Core Calculation Corrections

BREAKING CHANGES:
- ATM strike selection: Now uses 50Δ delta (was closest to spot)
- ATM CSV columns: atm_ff replaces dual call_ff/put_ff approach
- CSV schema: 31 → 40 columns (added atm_* and min_ff columns)

MIGRATION:
- Update CSV parsers to use atm_ff for ATM structures
- Update column count check: 31 → 40
- See CLAUDE.md migration guide for complete details

NEW FEATURES:
- Hybrid volume filtering (liquidity_rating + option_volume)
- Greeks IV primary (ex-earn IV rare fallback)
- Skip reason tracking (understand filtering)
"""
```

## Git Commit Standards

### Commit Message Format
```
[Type] Brief description (50 chars max)

Detailed explanation of changes (72 chars per line):
- What changed and why
- Impact on existing functionality
- Testing performed

Closes #123 (if applicable)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Commit Types
- **Issue #XX:** Task completion (linked to GitHub issue)
- **Fix:** Bug fix
- **Feature:** New feature
- **Refactor:** Code restructuring without behavior change
- **Docs:** Documentation updates
- **Test:** Test additions or modifications
- **Perf:** Performance improvements

### Examples
```bash
# Good: Clear, specific, linked to issue
git commit -m "$(cat <<'EOF'
Issue #32: Implement hybrid volume filtering system

Volume filtering now supports two modes:
- Default (24/7): Uses liquidity_rating >= 3 from Market Metrics
- Precise (market hours): Uses --options-volume flag for dxFeed volume

Changes:
- Scanner: Added check_liquidity_rating() and check_option_volume()
- CLI: Added --options-volume [THRESHOLD] flag
- CSV: Added liq_rating column (40 columns total)
- Docs: Updated CLAUDE.md and README_TT.md

Rationale: liquidity_value showed inconsistent scaling (7.8x-419x)
and cannot be used as reliable volume proxy. Hybrid system provides
both convenience (24/7) and precision (market hours).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"

# Bad: Vague, no context
git commit -m "Fix bug"
git commit -m "Update files"
```

## Testing Standards

### Unit Test Structure
```python
import pytest
from ff_tastytrade_scanner import calculate_forward_iv, calculate_forward_factor

class TestForwardIVCalculation:
    """Test forward IV calculation via variance decomposition."""

    def test_basic_forward_iv(self):
        """Test basic forward IV calculation with positive variance."""
        iv_front = 0.25  # 25%
        iv_back = 0.30   # 30%
        dte_front = 30
        dte_back = 60

        fwd_iv = calculate_forward_iv(iv_front, iv_back, dte_front, dte_back)

        assert fwd_iv is not None
        assert 0.30 < fwd_iv < 0.40  # Forward IV should be higher
        assert isinstance(fwd_iv, float)

    def test_negative_variance_handling(self):
        """Test that negative variance returns None (edge case)."""
        iv_front = 0.30  # Higher front IV
        iv_back = 0.20   # Lower back IV (unusual, but possible)
        dte_front = 30
        dte_back = 60

        fwd_iv = calculate_forward_iv(iv_front, iv_back, dte_front, dte_back)

        # Should handle gracefully (return None or raise)
        assert fwd_iv is None or fwd_iv < 0

    def test_forward_factor_calculation(self):
        """Test FF calculation with known inputs."""
        iv_front = 0.25
        fwd_iv = 0.20

        ff = calculate_forward_factor(iv_front, fwd_iv)

        assert ff == pytest.approx(0.25, rel=1e-2)  # 25% premium
        assert ff > 0.20  # Above typical threshold
```

### Integration Test Structure
```python
# scripts/test_earnings_cache.py
"""Integration test for earnings cache system.

Tests the full multi-source pipeline:
1. Cache miss → Yahoo Finance
2. Cache hit (subsequent call)
3. Fallback to TastyTrade if Yahoo fails
"""

import time
from earnings_cache import EarningsCache

def test_earnings_cache_pipeline():
    """Test full earnings cache pipeline."""
    cache = EarningsCache('.cache/test_earnings.db')

    # First call: Cache miss, fetch from Yahoo
    start = time.time()
    earnings_date = cache.get_earnings_date('AAPL')
    duration_miss = time.time() - start

    assert earnings_date is not None
    assert duration_miss > 0.05  # Yahoo takes ~100ms

    # Second call: Cache hit
    start = time.time()
    earnings_date_cached = cache.get_earnings_date('AAPL')
    duration_hit = time.time() - start

    assert earnings_date_cached == earnings_date
    assert duration_hit < 0.02  # Cache hit < 20ms
    assert duration_hit < duration_miss / 5  # At least 5x faster

    print(f"✅ Cache miss: {duration_miss*1000:.0f}ms")
    print(f"✅ Cache hit: {duration_hit*1000:.0f}ms")
    print(f"✅ Speedup: {duration_miss/duration_hit:.1f}x")
```

## Error Message Standards

### User-Facing Errors
```python
# Good: Clear, actionable, helpful
logger.error(
    f"Greeks timeout for {symbol} after {timeout}s. "
    f"Got {len(results)}/{len(symbols)} strikes. "
    f"Try increasing --timeout or check TastyTrade connectivity."
)

# Good: Specific filter reason
logger.info(
    f"Skipping {symbol}: earnings on {earnings_date} "
    f"(between today and back expiry {back_expiry}). "
    f"Use --allow-earnings to override."
)

# Bad: Vague, unhelpful
logger.error("Error occurred")
logger.warning("Something went wrong")
```

### Debug Messages
```python
# Good: Detailed context for troubleshooting
logger.debug(
    f"{symbol}: Selected ATM strike {strike_price} "
    f"(delta={strike_delta:.3f}, target=0.500, diff={abs(strike_delta-0.5):.3f})"
)

logger.debug(
    f"{symbol} {front_dte}-{back_dte}: "
    f"FF={ff:.3f}, front_iv={iv_front:.3f}, fwd_iv={fwd_iv:.3f}"
)

# Bad: Not enough context
logger.debug(f"Strike: {strike_price}")
logger.debug(f"FF: {ff}")
```

## Configuration Standards

### Environment Variables
```bash
# Required (fail if missing)
export TT_USERNAME="your_tastytrade_username"
export TT_PASSWORD="your_tastytrade_password"

# Optional (use defaults if missing)
export TT_ENVIRONMENT="production"  # Default: production
export LOG_LEVEL="INFO"              # Default: INFO
```

### CLI Defaults
```python
# Good: Sensible defaults that work for 80% of use cases
parser.add_argument('--min-ff', type=float, default=0.20,
    help="Minimum FF to include (default: 0.20)")
parser.add_argument('--dte-tolerance', type=int, default=5,
    help="Max DTE deviation in days (default: 5)")
parser.add_argument('--timeout', type=float, default=3.0,
    help="Greeks snapshot timeout in seconds (default: 3.0)")

# Bad: No defaults, user must specify everything
parser.add_argument('--min-ff', type=float, required=True)
```

## Performance Standards

### Benchmark Targets
- **Small scan (10 symbols):** < 30 seconds
- **Medium scan (100 symbols):** < 2 minutes (with cache)
- **Large scan (1000 symbols):** < 30 seconds (with cache)
- **Cache hit:** < 10ms per symbol
- **Cache miss:** 100-500ms per symbol (acceptable)

### Memory Limits
- **Default mode:** Linear growth OK (< 1GB for 1000 symbols)
- **Streaming mode:** Constant memory (< 100MB regardless of symbols)

### Code Review Checklist
- [ ] Function has clear purpose (single responsibility)
- [ ] Docstring explains purpose, args, returns, and examples
- [ ] Error handling with specific exceptions
- [ ] Logging at appropriate levels (debug, info, warning, error)
- [ ] Type hints for function signatures (when practical)
- [ ] Unit tests for core logic (calculation functions)
- [ ] Integration tests for API interactions
- [ ] Performance acceptable (< 2 min for 100 symbols)
- [ ] Documentation updated (CLAUDE.md, README_TT.md)
- [ ] Git commit message clear and linked to issue
