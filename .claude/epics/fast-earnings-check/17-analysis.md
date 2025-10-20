---
issue: 17
created: 2025-10-20T00:54:00Z
status: ready
---

# Analysis: Implement TastyTrade fallback for Yahoo Finance failures

## Overview
Add TastyTrade API as a fallback earnings data source when Yahoo Finance fails or returns no data. This ensures reliability even if Yahoo Finance API changes or experiences downtime. Implements the full fallback chain: Cache → Yahoo Finance → TastyTrade → Graceful degradation.

## Work Stream (Single-threaded, Sequential)

### Fallback Implementation (4-6 hours)
**Scope:** Add TastyTrade fallback to EarningsCache class
**Owner:** general-purpose agent

**Implementation details:**

1. **Modify EarningsCache.__init__():**
   ```python
   def __init__(self, cache_path: str = ".cache/earnings.db", session=None):
       """Initialize cache with optional TastyTrade session for fallback."""
       self.session = session  # Store session for TastyTrade fallback
       # ... existing init code ...
   ```

2. **Add _fetch_from_tastytrade() method:**
   ```python
   def _fetch_from_tastytrade(self, session, symbol: str) -> Optional[date]:
       """Fetch earnings from TastyTrade API as fallback."""
       # Call TastyTrade API (use existing market metrics endpoint)
       # Extract earnings.expected_report_date from response
       # Return as date object or None
   ```

3. **Modify get_next_earnings() fallback chain:**
   ```python
   def get_next_earnings(self, symbol: str) -> dict:
       # 1. Check cache first
       cached = self._get_from_cache(symbol)
       if cached and self._is_cache_fresh(cached['next_earnings_date']):
           return {"source": "cache", ...}

       # 2. Try Yahoo Finance
       try:
           yahoo_date = self._fetch_from_yahoo(symbol)
           if yahoo_date:
               self._save_to_cache(symbol, yahoo_date, "yahoo")
               return {"source": "yahoo", ...}
       except Exception as e:
           print(f"[WARN] {symbol}: Yahoo Finance failed, trying TastyTrade...", file=sys.stderr)

       # 3. Try TastyTrade fallback (if session provided)
       if self.session:
           try:
               tt_date = self._fetch_from_tastytrade(self.session, symbol)
               if tt_date:
                   self._save_to_cache(symbol, tt_date, "tastytrade")
                   return {"source": "tastytrade", ...}
           except Exception as e:
               print(f"[WARN] {symbol}: TastyTrade fallback failed", file=sys.stderr)

       # 4. Graceful degradation
       print(f"[WARN] {symbol}: No earnings data available (allow through)", file=sys.stderr)
       return {"source": "none", "next_earnings": None, ...}
   ```

4. **Modify scanner integration (ff_tastytrade_scanner.py):**
   ```python
   # Pass session to EarningsCache constructor
   cache = EarningsCache(session=session)
   ```

5. **Add timeout to Yahoo Finance:**
   ```python
   def _fetch_from_yahoo(self, symbol: str, timeout: int = 5) -> Optional[date]:
       """Fetch from Yahoo with 5-second timeout."""
       # Set timeout on yfinance call
   ```

**Files to modify:**
- `scripts/earnings_cache.py` (add session parameter, _fetch_from_tastytrade method, modify fallback chain)
- `scripts/ff_tastytrade_scanner.py` (pass session to EarningsCache constructor)

**Key considerations:**
- Reuse existing scanner's TastyTrade session (already authenticated)
- TastyTrade should be FALLBACK only (Yahoo Finance is primary)
- Handle all errors gracefully (no crashes)
- Log warnings when fallback is used (debugging)
- Track data source in returned dict ("cache", "yahoo", "tastytrade", "none")

**Testing approach:**
- Manual: Normal case (Yahoo works) - verify fast response
- Manual: Simulate Yahoo failure - verify TastyTrade fallback
- Manual: Simulate both failures - verify graceful degradation (no crash)
- Manual: Verify timeout prevents hanging (5s timeout)
- Manual: Session not provided - verify Yahoo-only mode works

## Dependencies
- ✅ Task #15 completed (EarningsCache module exists)
- ✅ Task #16 completed (Scanner integration with session available)
- Existing scanner session authentication

## Success Criteria
- [ ] `_fetch_from_tastytrade()` method added to EarningsCache
- [ ] Fallback chain implemented (Cache → Yahoo → TastyTrade → None)
- [ ] Session parameter added to EarningsCache.__init__()
- [ ] Yahoo Finance timeout set to 5 seconds
- [ ] Scanner passes session to EarningsCache constructor
- [ ] Data source tracked in returned dict
- [ ] All error scenarios handled gracefully
- [ ] Manual testing: All 5 scenarios pass

## Risks & Mitigations
**Risk:** TastyTrade fallback is too slow
- Mitigation: Fallback should be rare (<1% of requests)
- Target: Only use when Yahoo Finance fails

**Risk:** Breaking EarningsCache interface
- Mitigation: Session parameter is optional (defaults to None)
- Backward compatibility: Works without session (Yahoo-only mode)

**Risk:** TastyTrade API rate limiting
- Mitigation: Fallback should be rare, cache reduces API calls
- Expected usage: <1% of symbols per scan

## Notes
- Yahoo Finance remains PRIMARY source (fastest)
- TastyTrade is FALLBACK only (when Yahoo fails)
- Session parameter is optional (backward compatible)
- Module should still work standalone without TastyTrade session
