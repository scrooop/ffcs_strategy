#!/bin/bash
# Integration test suite for ff_tastytrade_scanner.py v3.0
# Tests: output modes, CSV schema, flag combinations

TIMESTAMP=$(date +"%y%m%d_%H%M")
TEST_DIR="test_results/${TIMESTAMP}_integration_tests"
mkdir -p "$TEST_DIR"

TICKERS="SPY AAPL ASML"
PAIRS="30-60"

echo "=== Integration Test Suite ==="
echo "Test directory: $TEST_DIR"
echo "Test symbols: $TICKERS"
echo ""

# Test 1: Quiet mode
echo "[1/7] Testing quiet mode..."
timeout 120 python ff_tastytrade_scanner.py --tickers $TICKERS --pairs $PAIRS --quiet \
  --csv-out "$TEST_DIR/test1_quiet.csv" 2>&1 | tee "$TEST_DIR/test1_quiet.log"
echo ""

# Test 2: Normal mode (default)
echo "[2/7] Testing normal mode..."
timeout 120 python ff_tastytrade_scanner.py --tickers $TICKERS --pairs $PAIRS \
  --csv-out "$TEST_DIR/test2_normal.csv" 2>&1 | tee "$TEST_DIR/test2_normal.log"
echo ""

# Test 3: Verbose mode
echo "[3/7] Testing verbose mode..."
timeout 120 python ff_tastytrade_scanner.py --tickers $TICKERS --pairs $PAIRS --verbose \
  --csv-out "$TEST_DIR/test3_verbose.csv" 2>&1 | tee "$TEST_DIR/test3_verbose.log"
echo ""

# Test 4: Debug mode
echo "[4/7] Testing debug mode..."
timeout 120 python ff_tastytrade_scanner.py --tickers SPY --pairs $PAIRS --debug \
  --csv-out "$TEST_DIR/test4_debug.csv" 2>&1 | tee "$TEST_DIR/test4_debug.log"
echo ""

# Test 5: File logging
echo "[5/7] Testing file logging..."
timeout 120 python ff_tastytrade_scanner.py --tickers $TICKERS --pairs $PAIRS \
  --log-file "$TEST_DIR/test5_file.log" --csv-out "$TEST_DIR/test5_logfile.csv" 2>&1 | tee "$TEST_DIR/test5_terminal.log"
echo ""

# Test 6: Quiet + file logging
echo "[6/7] Testing quiet + file logging..."
timeout 120 python ff_tastytrade_scanner.py --tickers $TICKERS --pairs $PAIRS --quiet \
  --log-file "$TEST_DIR/test6_quiet_file.log" --csv-out "$TEST_DIR/test6_quiet.csv" 2>&1 | tee "$TEST_DIR/test6_terminal.log"
echo ""

# Test 7: Verbose + file logging
echo "[7/7] Testing verbose + file logging..."
timeout 120 python ff_tastytrade_scanner.py --tickers $TICKERS --pairs $PAIRS --verbose \
  --log-file "$TEST_DIR/test7_verbose_file.log" --csv-out "$TEST_DIR/test7_verbose.csv" 2>&1 | tee "$TEST_DIR/test7_terminal.log"
echo ""

echo "=== Test Summary ==="
ls -lh "$TEST_DIR"/*.csv 2>/dev/null | awk '{print $9, $5}'
echo ""
echo "Results saved to: $TEST_DIR"
