# Issue #40: Add File Logging Support (--log-file) - COMPLETE

**Status:** ✅ COMPLETE
**Date:** 2025-10-20 14:53 CDT
**Branch:** epic/output-csv-terminal-flags
**Commits:** c91bb91, 77f3b60

## Summary

Successfully implemented `--log-file` flag for file logging with timestamps. File receives ALL log levels (DEBUG and above) while terminal respects output mode (quiet/normal/verbose/debug), enabling true "tee" functionality for archiving scan results.

## Changes Made

### 1. Core Implementation (c91bb91)
- Added `--log-file` argparse flag with PATH metavar
- Updated `setup_logging()` signature to accept `log_file: Optional[str] = None`
- Added FileHandler when log_file provided
- File output includes timestamps and logger names
- File is truncated on start (fresh log each run)
- Error handling for IOError and PermissionError

### 2. Multi-Handler Architecture Fix (77f3b60)
- **Critical fix:** Logger level set to DEBUG when log_file provided (captures all messages)
- Console handler level set independently based on mode
- File handler always receives ALL log levels (DEBUG and above)
- Terminal output still respects output mode correctly

## Testing Results

All acceptance criteria verified:

### ✅ File Logging Functionality
- `--log-file <path>` flag added to argparse
- FileHandler added to scanner logger when flag provided
- File receives ALL log levels (DEBUG and above) - verified in quiet mode
- File output includes timestamps and logger names
- File created/truncated on scan start (mode='w')

### ✅ Terminal Independence
- Terminal still receives filtered logs based on mode:
  - **Quiet mode:** Terminal silent (0 lines), file receives INFO/WARN messages
  - **Normal mode:** Terminal shows [SYMBOL] format, file shows timestamped format
  - **Debug mode:** Both show timestamped format with debug messages

### ✅ Error Handling
- Invalid path: Logs error and continues scanning
  ```
  [SCANNER] ERROR: Failed to create log file /nonexistent/dir/test.log: [Errno 2] No such file or directory
  ```
- Scanner continues successfully despite file creation failure

### ✅ Path Support
- Absolute paths: `/tmp/test_scan.log` ✅
- Relative paths: `test_relative.log` ✅
- File truncation: Fresh log each run ✅

## Example Usage

```bash
# Basic file logging with normal mode
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 \
  --min-ff 0.20 \
  --log-file scan_results.log

# Quiet terminal, full file logging
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 \
  --min-ff 0.20 \
  --log-file scan_results.log \
  --quiet

# Debug mode with file archiving
python scripts/ff_tastytrade_scanner.py \
  --tickers SPY QQQ \
  --pairs 30-60 \
  --min-ff 0.20 \
  --log-file debug_scan.log \
  --debug
```

## Output Examples

**Terminal (normal mode):**
```
[SCANNER] INFO : Earnings pre-filter: 1 → 1 passed (0 filtered)
[SPY   ] WARN : Earnings date unavailable, skipping earnings check
[SCANNER] INFO : No results passing filters
```

**File (all modes):**
```
2025-10-20 14:52:21,674 - scanner - INFO - SCANNER: Earnings pre-filter: 1 → 1 passed (0 filtered)
2025-10-20 14:52:22,040 - scanner.earnings - WARNING - SPY: Earnings date unavailable, skipping earnings check
2025-10-20 14:52:26,768 - scanner - INFO - SCANNER: No results passing filters
```

## Architecture Notes

### Multi-Handler Logging Design

The implementation uses a sophisticated multi-handler approach:

1. **Logger Level:** Set to DEBUG when log_file provided (allows all messages through)
2. **Console Handler Level:** Set based on mode (quiet=ERROR, normal/verbose=INFO, debug=DEBUG)
3. **File Handler Level:** Always set to DEBUG (captures everything)

This architecture ensures:
- File receives all messages regardless of terminal mode
- Terminal filtering works independently
- No message duplication or loss
- Clean separation of concerns

### Key Code Sections

**Logger initialization:**
```python
# Set level based on mode
# If log_file is provided, set logger to DEBUG so file handler receives all messages
# Console handler will still filter based on mode
if log_file:
    scanner_logger.setLevel(logging.DEBUG)  # Logger must accept all levels for file
elif mode == "quiet":
    scanner_logger.setLevel(logging.ERROR)
# ...
```

**Console handler (independent filtering):**
```python
# Set console handler level based on mode (independent of logger level)
if mode == "quiet":
    console.setLevel(logging.ERROR)
elif mode == "debug":
    console.setLevel(logging.DEBUG)
else:  # normal, verbose
    console.setLevel(logging.INFO)
```

**File handler (always captures all):**
```python
if log_file:
    try:
        fh = logging.FileHandler(log_file, mode='w')  # Truncate on start
        fh.setLevel(logging.DEBUG)  # File gets ALL levels
        fh.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        ))
        scanner_logger.addHandler(fh)
    except (IOError, PermissionError) as e:
        scanner_logger.error(f"SCANNER: Failed to create log file {log_file}: {e}")
```

## Files Modified

- `scripts/ff_tastytrade_scanner.py`:
  - Line 119-211: Updated `setup_logging()` function
  - Line 1895-1896: Added `--log-file` argparse flag
  - Line 1939: Updated `setup_logging()` call to pass log_file

## Next Steps

Task #40 is complete. Ready for Phase 4 integration testing with other terminal output tasks (#38, #39).

## Definition of Done

- [x] `--log-file <path>` flag implemented
- [x] FileHandler added to scanner logger
- [x] File receives ALL log levels (verified with DEBUG messages in quiet mode)
- [x] Terminal still respects output mode (quiet/normal/verbose)
- [x] File includes timestamps and logger names
- [x] File created/truncated on scan start
- [x] Error handling tested (invalid path, no write permission)
- [x] Tested with various paths (absolute, relative, subdirectories)
- [x] Progress update created
- [x] Code committed with detailed commit messages
