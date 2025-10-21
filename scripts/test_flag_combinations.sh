#!/bin/bash
# Flag combination tests

TIMESTAMP=$(date +"%y%m%d_%H%M")
TEST_DIR="test_results/${TIMESTAMP}_flag_combinations"
mkdir -p "$TEST_DIR"

TICKERS="SPY AAPL ASML"
PAIRS="30-60"

echo "=== Flag Combination Tests ==="
echo "Test directory: $TEST_DIR"
echo ""

# Test 1: --quiet + --csv-out
echo "[1/10] --quiet + --csv-out"
timeout 90 python ff_tastytrade_scanner.py --tickers $TICKERS --pairs $PAIRS --quiet --show-all-scans --csv-out "$TEST_DIR/test1.csv" 2>&1 | wc -l

# Test 2: --verbose + --log-file
echo "[2/10] --verbose + --log-file"
timeout 90 python ff_tastytrade_scanner.py --tickers $TICKERS --pairs $PAIRS --verbose --log-file "$TEST_DIR/test2.log" 2>&1 | wc -l

# Test 3: --verbose + --csv-out
echo "[3/10] --verbose + --csv-out"
timeout 90 python ff_tastytrade_scanner.py --tickers $TICKERS --pairs $PAIRS --verbose --show-all-scans --csv-out "$TEST_DIR/test3.csv" 2>&1 | wc -l

# Test 4: --quiet + --log-file + --csv-out
echo "[4/10] --quiet + --log-file + --csv-out"
timeout 90 python ff_tastytrade_scanner.py --tickers $TICKERS --pairs $PAIRS --quiet --log-file "$TEST_DIR/test4.log" --show-all-scans --csv-out "$TEST_DIR/test4.csv" 2>&1 | wc -l

# Test 5: --verbose + --log-file + --csv-out
echo "[5/10] --verbose + --log-file + --csv-out"
timeout 90 python ff_tastytrade_scanner.py --tickers $TICKERS --pairs $PAIRS --verbose --log-file "$TEST_DIR/test5.log" --show-all-scans --csv-out "$TEST_DIR/test5.csv" 2>&1 | wc -l

# Test 6: --allow-earnings + --verbose
echo "[6/10] --allow-earnings + --verbose"
timeout 90 python ff_tastytrade_scanner.py --tickers $TICKERS --pairs $PAIRS --allow-earnings --verbose 2>&1 | grep -c "AAPL"

# Test 7: --structure double + --verbose
echo "[7/10] --structure double + --verbose"
timeout 90 python ff_tastytrade_scanner.py --tickers SPY --pairs $PAIRS --structure double --verbose --show-all-scans --csv-out "$TEST_DIR/test7.csv" 2>&1 | grep -c "double"

# Test 8: --structure atm-call + --verbose
echo "[8/10] --structure atm-call + --verbose"
timeout 90 python ff_tastytrade_scanner.py --tickers SPY --pairs $PAIRS --structure atm-call --verbose --show-all-scans --csv-out "$TEST_DIR/test8.csv" 2>&1 | grep -c "atm-call"

# Test 9: --skip-liquidity-check
echo "[9/10] --skip-liquidity-check"
timeout 90 python ff_tastytrade_scanner.py --tickers ASML --pairs $PAIRS --skip-liquidity-check --show-all-scans --csv-out "$TEST_DIR/test9.csv" 2>&1 | tail -5

# Test 10: --debug + --log-file
echo "[10/10] --debug + --log-file"
timeout 90 python ff_tastytrade_scanner.py --tickers SPY --pairs $PAIRS --debug --log-file "$TEST_DIR/test10.log" 2>&1 | head -3

echo ""
echo "=== Results Summary ==="
ls -lh "$TEST_DIR"/ | grep -E "\.(csv|log)$" | awk '{print $9, $5}'
