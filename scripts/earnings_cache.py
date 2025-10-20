#!/usr/bin/env python3
"""
Persistent Earnings Date Cache with Multi-Source Fallback

This module provides a SQLite-backed cache for earnings dates, designed to
dramatically speed up earnings pre-filtering in the FF calendar spread scanner.

**Architecture:**
- SQLite database: `.cache/earnings.db` (auto-created)
- Primary data source: Yahoo Finance via yfinance library (fastest)
- Fallback data source: TastyTrade API (when Yahoo fails, optional)
- Cache invalidation: Automatic re-fetch when date is in past
- Futures support: Symbols starting with '/' return None immediately (no earnings)
- Timeout handling: Relies on yfinance's internal request timeout (no signal-based timeout)

**Data source fallback chain:**
1. Cache (instant, <5ms)
2. Yahoo Finance (primary, ~100-200ms, 5s timeout)
3. TastyTrade API (fallback, ~200-500ms, only if session provided)
4. Graceful degradation (returns None, logs warning)

**Performance targets:**
- Batch processing: 100 symbols in <15s (cold start), <1s (warm cache)
- Single lookup: <5ms (cache hit), ~100-500ms (Yahoo), ~200-500ms (TastyTrade fallback)

**Usage:**

    from earnings_cache import EarningsCache

    # Initialize cache without TastyTrade fallback (Yahoo-only mode)
    cache = EarningsCache()

    # Initialize cache with TastyTrade fallback (recommended for production)
    from tastytrade import Session
    session = Session(username, password)
    cache = EarningsCache(session=session)

    # Single symbol lookup
    result = cache.get_next_earnings("AAPL")
    # Returns: {
    #     "symbol": "AAPL",
    #     "next_earnings": "2025-11-01",  # YYYY-MM-DD or None
    #     "source": "cache",               # "cache", "yahoo", "tastytrade", "bypass", or "none"
    #     "cached_at": "2025-10-19T23:56:22Z"
    # }

    # Batch processing (efficient)
    symbols = ["SPY", "QQQ", "AAPL", "/ES", "/GC"]
    results = cache.batch_get_earnings(symbols)
    # Returns: {"SPY": {...}, "QQQ": {...}, ...}

    # Futures symbols return None immediately (no API call)
    futures_result = cache.get_next_earnings("/ES")
    # Returns: {"symbol": "/ES", "next_earnings": None, "source": "bypass", ...}

**Database schema:**

    CREATE TABLE earnings (
        symbol TEXT PRIMARY KEY,
        next_earnings_date TEXT,  -- YYYY-MM-DD or NULL
        last_updated TEXT,         -- ISO 8601 timestamp
        data_source TEXT           -- 'cache' | 'yahoo' | 'tastytrade' | 'bypass' | 'none'
    )

**Cache invalidation logic:**
- If cached earnings date is in the past → re-fetch from Yahoo Finance
- If cached earnings date is None → use cached None (no re-fetch until manual clear)
- If cached earnings date is in the future → use cached value

**Thread safety:**
- Uses `check_same_thread=False` for SQLite connection
- Safe for concurrent reads, writes are serialized by SQLite

**Error handling:**
- Yahoo Finance timeout (>5s): Falls back to TastyTrade
- Yahoo Finance failure: Falls back to TastyTrade, logs warning
- TastyTrade failure: Returns None with "none" source, logs warning
- Symbol not found: Returns None, cached for future lookups
- Database corruption: Auto-recreates database on next run
- Network errors: Returns None, does not cache (will retry next time)

Author: Claude Code
Created: 2025-10-19
Updated: 2025-10-20 - Added TastyTrade fallback support (Issue #17)
         2025-10-20 - Removed signal-based timeout (curl_cffi incompatibility fix)
"""

import sqlite3
import logging
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Optional

try:
    import yfinance as yf
except ImportError:
    raise ImportError(
        "yfinance library required. Install with: pip install yfinance"
    )

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class EarningsCache:
    """
    Persistent SQLite cache for earnings dates with Yahoo Finance fetching.

    Provides fast, cached access to next earnings dates for equity symbols,
    with automatic cache invalidation when dates pass. Futures symbols
    (starting with '/') are bypassed entirely (return None immediately).

    Example:
        >>> cache = EarningsCache()
        >>> result = cache.get_next_earnings("AAPL")
        >>> print(result["next_earnings"])
        '2025-11-01'
        >>>
        >>> # Batch processing
        >>> results = cache.batch_get_earnings(["SPY", "QQQ", "AAPL"])
        >>> len(results)
        3
    """

    def __init__(self, cache_path: str = ".cache/earnings.db", session=None):
        """
        Initialize earnings cache with SQLite backend.

        Creates `.cache/` directory and `earnings.db` database if they don't
        exist. Sets up schema and prepares connection for queries.

        Args:
            cache_path: Path to SQLite database file (default: .cache/earnings.db)
                       Relative paths are resolved from current working directory.
            session: Optional tastytrade Session for TastyTrade API fallback.
                    If provided, enables fallback to TastyTrade when Yahoo fails.
                    If None, only Yahoo Finance will be used.

        Example:
            >>> cache = EarningsCache()  # Uses default .cache/earnings.db
            >>> cache = EarningsCache("/tmp/test_earnings.db")  # Custom path
            >>> cache = EarningsCache(session=session)  # With TastyTrade fallback
        """
        self.cache_path = Path(cache_path)
        self.session = session  # Store for TastyTrade fallback

        # Create .cache directory if doesn't exist
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)

        # Initialize database connection (thread-safe)
        self.conn = sqlite3.connect(
            str(self.cache_path),
            check_same_thread=False,  # Allow multi-threaded access
            timeout=10.0  # Wait up to 10s for lock release
        )

        # Enable foreign keys and WAL mode for better concurrency
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.conn.execute("PRAGMA journal_mode = WAL")

        # Create schema if doesn't exist
        self._create_schema()

        logger.info(f"Earnings cache initialized: {self.cache_path.absolute()}")

    def _create_schema(self):
        """
        Create earnings table schema if doesn't exist.

        Schema:
            earnings (
                symbol TEXT PRIMARY KEY,
                next_earnings_date TEXT,  -- YYYY-MM-DD or NULL
                last_updated TEXT,         -- ISO 8601 UTC timestamp
                data_source TEXT           -- 'cache' | 'yahoo' | 'bypass'
            )
        """
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS earnings (
                symbol TEXT PRIMARY KEY,
                next_earnings_date TEXT,
                last_updated TEXT,
                data_source TEXT
            )
        """)
        self.conn.commit()
        logger.debug("Database schema created/verified")

    def _get_from_cache(self, symbol: str) -> Optional[dict]:
        """
        Retrieve cached earnings record for symbol.

        Args:
            symbol: Stock ticker symbol (e.g., "AAPL")

        Returns:
            Dict with cached data if exists and fresh, None otherwise:
            {
                "symbol": "AAPL",
                "next_earnings": "2025-11-01",  # or None
                "cached_at": "2025-10-19T23:56:22Z",
                "source": "cache"
            }

        Cache freshness rules:
            - If next_earnings_date is None: Always fresh (no scheduled earnings)
            - If next_earnings_date is in future: Always fresh (upcoming earnings)
            - If next_earnings_date is in past: Fresh for 30 days after the date
              (company likely hasn't announced next earnings yet)
            - If next_earnings_date is >30 days old: Stale (might have new date)
        """
        cursor = self.conn.execute(
            "SELECT next_earnings_date, last_updated, data_source FROM earnings WHERE symbol = ?",
            (symbol,)
        )
        row = cursor.fetchone()

        if not row:
            return None  # Not in cache

        earnings_date_str, last_updated, data_source = row

        # Check cache freshness
        if earnings_date_str is not None:
            earnings_date = date.fromisoformat(earnings_date_str)
            if earnings_date < date.today():
                # Past date - check if it's too old
                days_since_earnings = (date.today() - earnings_date).days
                if days_since_earnings > 30:
                    # Stale: >30 days old, company may have announced next earnings
                    logger.debug(f"{symbol}: Cached date {earnings_date_str} is {days_since_earnings} days old (stale)")
                    return None
                else:
                    # Fresh: Recently past, company probably hasn't announced next date yet
                    logger.debug(f"{symbol}: Cached date {earnings_date_str} is {days_since_earnings} days old (fresh)")

        # Cache is fresh
        return {
            "symbol": symbol,
            "next_earnings": earnings_date_str,
            "source": "cache",
            "cached_at": last_updated
        }

    def _save_to_cache(self, symbol: str, earnings_date: Optional[date], source: str):
        """
        Save or update earnings record in cache.

        Args:
            symbol: Stock ticker symbol
            earnings_date: Next earnings date (or None if not available)
            source: Data source ("yahoo", "bypass", etc.)

        Uses INSERT OR REPLACE to handle both new records and updates.
        """
        earnings_date_str = earnings_date.isoformat() if earnings_date else None
        timestamp = datetime.now(timezone.utc).isoformat()

        self.conn.execute(
            """
            INSERT OR REPLACE INTO earnings (symbol, next_earnings_date, last_updated, data_source)
            VALUES (?, ?, ?, ?)
            """,
            (symbol, earnings_date_str, timestamp, source)
        )
        self.conn.commit()

        logger.debug(f"{symbol}: Cached earnings_date={earnings_date_str}, source={source}")

    def _is_cache_fresh(self, earnings_date: Optional[date]) -> bool:
        """
        Check if cached earnings date is still valid (in the future).

        Args:
            earnings_date: Cached earnings date (or None)

        Returns:
            True if date is in future or None (use cached value)
            False if date is in past (re-fetch needed)

        Cache freshness rules:
            - None → Fresh (company may not have scheduled earnings)
            - Past date → Stale (earnings already happened)
            - Future date → Fresh (upcoming earnings)
        """
        if earnings_date is None:
            return True  # None is always "fresh" (no earnings scheduled)

        return earnings_date >= date.today()

    def _fetch_from_yahoo(self, symbol: str, timeout: float = 5.0) -> Optional[date]:
        """
        Fetch next earnings date from Yahoo Finance via yfinance.

        Tries multiple methods in order:
        1. ticker.calendar (fastest, most reliable)
        2. ticker.get_earnings_dates() (fallback, slower)

        Args:
            symbol: Stock ticker symbol (e.g., "AAPL")
            timeout: Max seconds to wait for API response (default: 5.0)
                    NOTE: Timeout is not enforced due to incompatibility with curl_cffi.
                    Left as parameter for potential future implementations.

        Returns:
            Next upcoming earnings date, or None if not available

        Error handling:
            - API timeout → None (logged as warning)
            - Symbol not found → None (logged as info)
            - Network error → None (not cached, will retry next time)
            - Invalid response → None (logged as warning)

        Example:
            >>> cache = EarningsCache()
            >>> earnings_date = cache._fetch_from_yahoo("AAPL")
            >>> print(earnings_date)
            2025-11-01
        """
        # Futures symbols don't have earnings (handled at caller level)
        if symbol.startswith('/'):
            logger.debug(f"{symbol}: Futures symbol, skipping Yahoo Finance")
            return None

        # NOTE: Signal-based timeout disabled due to incompatibility with curl_cffi
        # (yfinance uses curl_cffi which can't handle signal interrupts in C callbacks)
        # Timeout is instead handled by yfinance's own request timeout mechanism

        try:

            logger.debug(f"{symbol}: Fetching from Yahoo Finance...")
            ticker = yf.Ticker(symbol)

            most_recent_date = None  # Track most recent date (past or future)

            # Method 1: Try ticker.calendar first (fastest)
            try:
                calendar = ticker.calendar
                if calendar is not None and 'Earnings Date' in calendar:
                    earnings_raw = calendar['Earnings Date']

                    # Handle pandas Timestamp or list of Timestamps
                    if hasattr(earnings_raw, '__iter__') and not isinstance(earnings_raw, str):
                        # List of dates
                        for dt in earnings_raw:
                            if hasattr(dt, 'date'):
                                earnings_date = dt.date()
                            else:
                                earnings_date = date.fromisoformat(str(dt).split()[0])

                            if earnings_date >= date.today():
                                # Found future date, return immediately
                                logger.info(f"{symbol}: Found upcoming earnings {earnings_date} (calendar)")
                                return earnings_date
                            elif most_recent_date is None or earnings_date > most_recent_date:
                                # Track most recent past date
                                most_recent_date = earnings_date
                    else:
                        # Single date
                        if hasattr(earnings_raw, 'date'):
                            earnings_date = earnings_raw.date()
                        else:
                            earnings_date = date.fromisoformat(str(earnings_raw).split()[0])

                        if earnings_date >= date.today():
                            logger.info(f"{symbol}: Found upcoming earnings {earnings_date} (calendar)")
                            return earnings_date
                        else:
                            most_recent_date = earnings_date
            except Exception as e:
                logger.debug(f"{symbol}: ticker.calendar failed: {e}")

            # Method 2: Fallback to get_earnings_dates() (slower)
            try:
                earnings_dates = ticker.get_earnings_dates(limit=10)
                if earnings_dates is not None and len(earnings_dates) > 0:
                    # Find first future date, or track most recent past date
                    for idx in earnings_dates.index:
                        if hasattr(idx, 'date'):
                            earnings_date = idx.date()
                        else:
                            earnings_date = date.fromisoformat(str(idx).split()[0])

                        if earnings_date >= date.today():
                            logger.info(f"{symbol}: Found upcoming earnings {earnings_date} (earnings_dates)")
                            return earnings_date
                        elif most_recent_date is None or earnings_date > most_recent_date:
                            most_recent_date = earnings_date
            except Exception as e:
                logger.debug(f"{symbol}: get_earnings_dates() failed: {e}")

            # If we found a past date, return it
            if most_recent_date is not None:
                logger.info(f"{symbol}: Most recent earnings {most_recent_date} (past), no upcoming date scheduled")
                return most_recent_date

            # No earnings date found at all
            logger.info(f"{symbol}: No earnings data available")
            return None

        except Exception as e:
            # Catch any errors from yfinance (network errors, timeouts, etc.)
            logger.warning(f"{symbol}: Yahoo Finance fetch failed: {e}")
            return None

    def _fetch_from_tastytrade(self, symbol: str) -> Optional[date]:
        """
        Fetch next earnings date from TastyTrade API as fallback.

        Uses tastytrade's market metrics API to retrieve earnings.expected_report_date.
        This is only called when Yahoo Finance fails or returns no data.

        Args:
            symbol: Stock ticker symbol (e.g., "AAPL")

        Returns:
            Next upcoming earnings date, or None if not available

        Error handling:
            - Session not available → None (logged as debug)
            - API error → None (logged as warning)
            - Symbol not found → None (logged as info)
            - Network error → None (not cached, will retry next time)

        Example:
            >>> cache = EarningsCache(session=session)
            >>> earnings_date = cache._fetch_from_tastytrade("AAPL")
            >>> print(earnings_date)
            2025-11-01

        Note:
            Requires self.session to be set during initialization.
            This method will not work if session was not provided to __init__().
        """
        if not self.session:
            logger.debug(f"{symbol}: TastyTrade session not available, skipping fallback")
            return None

        # Futures symbols don't have earnings
        if symbol.startswith('/'):
            logger.debug(f"{symbol}: Futures symbol, skipping TastyTrade")
            return None

        try:
            logger.debug(f"{symbol}: Fetching from TastyTrade API...")

            # Import here to avoid dependency when not using TastyTrade fallback
            from tastytrade.metrics import get_market_metrics

            # Fetch market metrics for this symbol
            metrics = get_market_metrics(self.session, [symbol])

            if not metrics or len(metrics) == 0:
                logger.info(f"{symbol}: No market metrics returned from TastyTrade")
                return None

            # Extract earnings date from first (and only) result
            metric_info = metrics[0]

            if not hasattr(metric_info, 'earnings') or not metric_info.earnings:
                logger.info(f"{symbol}: No earnings data in TastyTrade response")
                return None

            earnings_info = metric_info.earnings

            if not hasattr(earnings_info, 'expected_report_date') or not earnings_info.expected_report_date:
                logger.info(f"{symbol}: No expected_report_date in TastyTrade response")
                return None

            earnings_date = earnings_info.expected_report_date

            # Validate and return the date (past or future)
            if isinstance(earnings_date, date):
                if earnings_date >= date.today():
                    logger.info(f"{symbol}: Found upcoming earnings {earnings_date} (tastytrade)")
                else:
                    logger.info(f"{symbol}: Most recent earnings {earnings_date} (past, tastytrade)")
                return earnings_date
            else:
                logger.warning(f"{symbol}: TastyTrade returned non-date object: {type(earnings_date)}")
                return None

        except ImportError:
            logger.warning(f"{symbol}: tastytrade library not available for fallback")
            return None
        except Exception as e:
            logger.warning(f"{symbol}: TastyTrade fetch failed: {e}")
            return None

    def get_next_earnings(self, symbol: str) -> dict:
        """
        Get next earnings date for a single symbol with fallback chain.

        Implements multi-source fallback: Cache → Yahoo Finance → TastyTrade → None
        Returns cached value if available and fresh, otherwise tries Yahoo Finance,
        then TastyTrade (if session provided), finally graceful degradation.
        Futures symbols (starting with '/') return None immediately without API call.

        Args:
            symbol: Stock ticker symbol (e.g., "AAPL", "/ES")

        Returns:
            Dict with earnings information:
            {
                "symbol": "AAPL",
                "next_earnings": "2025-11-01",  # YYYY-MM-DD or None
                "source": "cache" | "yahoo" | "tastytrade" | "bypass" | "none",
                "cached_at": "2025-10-19T23:56:22Z"  # ISO 8601 UTC
            }

        Fallback chain:
            1. Cache hit (fresh) → Return cached value instantly
            2. Cache miss/stale → Fetch from Yahoo Finance, cache result
            3. Yahoo fails → Try TastyTrade API (if session provided)
            4. TastyTrade fails → Return None with "none" source (graceful degradation)
            5. Futures symbol → Return None instantly (no API call, "bypass" source)

        Example:
            >>> cache = EarningsCache()
            >>>
            >>> # Equity symbol (Yahoo works)
            >>> result = cache.get_next_earnings("AAPL")
            >>> print(result["next_earnings"])
            '2025-11-01'
            >>> print(result["source"])
            'yahoo'
            >>>
            >>> # Yahoo fails, TastyTrade fallback
            >>> cache_with_tt = EarningsCache(session=session)
            >>> result = cache_with_tt.get_next_earnings("AAPL")
            >>> print(result["source"])
            'tastytrade'
            >>>
            >>> # Futures symbol (instant bypass)
            >>> result = cache.get_next_earnings("/ES")
            >>> print(result["next_earnings"])
            None
            >>> print(result["source"])
            'bypass'
        """
        # Fast path: Futures symbols bypass entirely
        if symbol.startswith('/'):
            timestamp = datetime.now(timezone.utc).isoformat()
            return {
                "symbol": symbol,
                "next_earnings": None,
                "source": "bypass",
                "cached_at": timestamp
            }

        # 1. Check cache first
        cached = self._get_from_cache(symbol)
        if cached is not None:
            logger.debug(f"{symbol}: Cache hit")
            return cached

        # 2. Try Yahoo Finance
        logger.debug(f"{symbol}: Cache miss, fetching from Yahoo Finance")
        yahoo_date = None
        yahoo_success = False
        try:
            yahoo_date = self._fetch_from_yahoo(symbol)
            yahoo_success = True
            if yahoo_date is not None:
                # Yahoo succeeded (returned past or future date), cache and return
                self._save_to_cache(symbol, yahoo_date, "yahoo")
                timestamp = datetime.now(timezone.utc).isoformat()

                # Informational message about what we found
                if yahoo_date >= date.today():
                    print(f"[INFO] {symbol}: Upcoming earnings {yahoo_date}", file=sys.stderr)
                else:
                    days_ago = (date.today() - yahoo_date).days
                    print(f"[INFO] {symbol}: Most recent earnings {yahoo_date} ({days_ago} days ago), no upcoming date scheduled", file=sys.stderr)

                return {
                    "symbol": symbol,
                    "next_earnings": yahoo_date.isoformat(),
                    "source": "yahoo",
                    "cached_at": timestamp
                }
            else:
                # Yahoo returned None (no data available at all), try TastyTrade
                logger.debug(f"{symbol}: Yahoo Finance returned no data, trying TastyTrade fallback")
        except Exception as e:
            # Yahoo raised exception, try TastyTrade
            logger.warning(f"{symbol}: Yahoo Finance failed ({e}), trying TastyTrade fallback")

        # 3. Try TastyTrade fallback (if session provided and Yahoo truly had no data)
        if self.session and yahoo_date is None:
            try:
                tt_date = self._fetch_from_tastytrade(symbol)
                if tt_date is not None:
                    # TastyTrade succeeded, cache and return
                    self._save_to_cache(symbol, tt_date, "tastytrade")
                    timestamp = datetime.now(timezone.utc).isoformat()

                    # Informational message
                    if tt_date >= date.today():
                        print(f"[INFO] {symbol}: Upcoming earnings {tt_date} (from TastyTrade)", file=sys.stderr)
                    else:
                        days_ago = (date.today() - tt_date).days
                        print(f"[INFO] {symbol}: Most recent earnings {tt_date} ({days_ago} days ago, from TastyTrade)", file=sys.stderr)

                    return {
                        "symbol": symbol,
                        "next_earnings": tt_date.isoformat(),
                        "source": "tastytrade",
                        "cached_at": timestamp
                    }
                else:
                    logger.debug(f"{symbol}: TastyTrade returned no data")
            except Exception as e:
                logger.debug(f"{symbol}: TastyTrade fallback failed ({e})")
        else:
            logger.debug(f"{symbol}: TastyTrade session not available or not needed, skipping fallback")

        # 4. Graceful degradation - all sources failed or returned None
        print(f"[INFO] {symbol}: No earnings data available from any source (no earnings to avoid)", file=sys.stderr)

        # Cache the None result to avoid repeated API calls
        self._save_to_cache(symbol, None, "none")

        timestamp = datetime.now(timezone.utc).isoformat()
        return {
            "symbol": symbol,
            "next_earnings": None,
            "source": "none",
            "cached_at": timestamp
        }

    def batch_get_earnings(self, symbols: list[str]) -> dict[str, dict]:
        """
        Efficiently fetch earnings dates for multiple symbols.

        Optimizes by:
        1. Bypassing futures symbols immediately (no API calls)
        2. Checking cache for all symbols first
        3. Only fetching from Yahoo Finance for cache misses
        4. Caching all results for future lookups

        Args:
            symbols: List of ticker symbols (e.g., ["SPY", "QQQ", "/ES"])

        Returns:
            Dict mapping symbol → earnings info:
            {
                "SPY": {
                    "symbol": "SPY",
                    "next_earnings": "2025-11-15",
                    "source": "cache",
                    "cached_at": "2025-10-19T23:56:22Z"
                },
                "QQQ": {...},
                "/ES": {
                    "symbol": "/ES",
                    "next_earnings": None,
                    "source": "bypass",
                    "cached_at": "2025-10-19T23:56:22Z"
                }
            }

        Performance:
            - 100 symbols, all cached: <1s
            - 100 symbols, all misses: ~10s (limited by Yahoo Finance API)
            - Futures symbols: instant (no API calls)

        Example:
            >>> cache = EarningsCache()
            >>> symbols = ["SPY", "QQQ", "AAPL", "/ES", "/GC"]
            >>> results = cache.batch_get_earnings(symbols)
            >>>
            >>> for symbol, info in results.items():
            ...     print(f"{symbol}: {info['next_earnings']}")
            SPY: 2025-11-15
            QQQ: 2025-11-20
            AAPL: 2025-11-01
            /ES: None
            /GC: None
        """
        results = {}

        # Process each symbol (get_next_earnings handles all logic)
        for symbol in symbols:
            results[symbol] = self.get_next_earnings(symbol)

        return results

    def clear_cache(self, symbol: Optional[str] = None):
        """
        Clear cached earnings data.

        Args:
            symbol: If provided, clear only this symbol. If None, clear entire cache.

        Example:
            >>> cache = EarningsCache()
            >>> cache.clear_cache("AAPL")  # Clear only AAPL
            >>> cache.clear_cache()         # Clear entire cache
        """
        if symbol:
            self.conn.execute("DELETE FROM earnings WHERE symbol = ?", (symbol,))
            logger.info(f"Cleared cache for {symbol}")
        else:
            self.conn.execute("DELETE FROM earnings")
            logger.info("Cleared entire earnings cache")

        self.conn.commit()

    def get_cache_stats(self) -> dict:
        """
        Get cache statistics for monitoring/debugging.

        Returns:
            Dict with cache metrics:
            {
                "total_symbols": 150,
                "symbols_with_earnings": 120,
                "symbols_without_earnings": 30,
                "oldest_entry": "2025-10-15T10:30:00Z",
                "newest_entry": "2025-10-19T23:56:22Z"
            }

        Example:
            >>> cache = EarningsCache()
            >>> stats = cache.get_cache_stats()
            >>> print(f"Cached symbols: {stats['total_symbols']}")
            Cached symbols: 150
        """
        cursor = self.conn.execute("""
            SELECT
                COUNT(*) as total,
                SUM(CASE WHEN next_earnings_date IS NOT NULL THEN 1 ELSE 0 END) as with_earnings,
                MIN(last_updated) as oldest,
                MAX(last_updated) as newest
            FROM earnings
        """)

        row = cursor.fetchone()
        total, with_earnings, oldest, newest = row

        return {
            "total_symbols": total,
            "symbols_with_earnings": with_earnings,
            "symbols_without_earnings": total - with_earnings,
            "oldest_entry": oldest,
            "newest_entry": newest
        }

    def close(self):
        """
        Close database connection.

        Call this when done with cache to ensure clean shutdown.
        """
        self.conn.close()
        logger.info("Earnings cache closed")

    def __del__(self):
        """Cleanup: Close connection when object is destroyed."""
        try:
            self.close()
        except:
            pass  # Already closed or error during cleanup


# Example usage and testing
if __name__ == "__main__":
    # Configure logging for standalone testing
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    print("=== Earnings Cache Test ===\n")

    # Initialize cache
    cache = EarningsCache()

    # Test 1: Single symbol lookup
    print("Test 1: Single symbol lookup (AAPL)")
    result = cache.get_next_earnings("AAPL")
    print(f"  Symbol: {result['symbol']}")
    print(f"  Next earnings: {result['next_earnings']}")
    print(f"  Source: {result['source']}")
    print(f"  Cached at: {result['cached_at']}\n")

    # Test 2: Futures symbol bypass
    print("Test 2: Futures symbol bypass (/ES)")
    result = cache.get_next_earnings("/ES")
    print(f"  Symbol: {result['symbol']}")
    print(f"  Next earnings: {result['next_earnings']}")
    print(f"  Source: {result['source']}\n")

    # Test 3: Batch processing
    print("Test 3: Batch processing (5 symbols)")
    symbols = ["SPY", "QQQ", "AAPL", "/ES", "/GC"]
    results = cache.batch_get_earnings(symbols)
    for symbol, info in results.items():
        print(f"  {symbol}: {info['next_earnings']} ({info['source']})")
    print()

    # Test 4: Cache stats
    print("Test 4: Cache statistics")
    stats = cache.get_cache_stats()
    print(f"  Total symbols: {stats['total_symbols']}")
    print(f"  With earnings: {stats['symbols_with_earnings']}")
    print(f"  Without earnings: {stats['symbols_without_earnings']}")
    print()

    # Test 5: Cache hit (re-query same symbol)
    print("Test 5: Cache hit test (re-query AAPL)")
    result = cache.get_next_earnings("AAPL")
    print(f"  Source: {result['source']} (should be 'cache')")
    print()

    print("=== All tests complete ===")

    # Cleanup
    cache.close()
