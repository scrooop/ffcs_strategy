# Terminal Output & Logging Policy

## Overview

The FFCS scanner uses **Rich library** for professional terminal formatting with Unicode symbols and colors, aligned with the EVC tool's formatting standards.

## Output Modes

### Quiet Mode (`--quiet`)
- Only ERROR messages displayed
- Minimal output for automated scripts
- Example: `python ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --quiet`

### Normal Mode (default)
- Standard output with INFO/WARN/ERROR messages
- Progress counters for symbol processing
- Unicode status symbols with colors
- Summary statistics at end
- Example: `python ff_tastytrade_scanner.py --tickers SPY --pairs 30-60`

### Verbose Mode (`--verbose`)
- Shows ALL symbols (pass, filter, skip, error)
- Detailed status for each symbol
- All skipped/filtered symbols with reasons
- Example: `python ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --verbose`

### Debug Mode (`--debug`)
- Like verbose, with additional debug information
- Timestamps on all messages
- Logger names for troubleshooting
- Example: `python ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --debug`

## Terminal Formatting Standards (EVC-Aligned)

### Status Symbols
- `[✓]` Success (green) - Pre-filter passed, file written successfully
- `[✗]` Error (red) - Market data errors, API failures
- `[~]` Skip (dim) - Symbol skipped (no quote, no chain, etc.)
- `[▸]` Action (bright cyan) - Active process running
- `[▪]` Info (cyan) - General information messages
- `[?]` Warning (yellow) - Non-critical issues

### Progress Counter Format
```
[ 1/125] NVR
[ 2/125] ELV            [✗] Market data error
[ 3/125] MOH
```

Each symbol appears on its own line with:
- Aligned counter: `[{current:>width}/{total}]`
- Symbol padded to 15 characters
- Inline status message (if applicable)

### Color Scheme
- **Green** - Success, passed filters
- **Red** - Errors, failures
- **Yellow** - Warnings
- **Cyan/Bright Cyan** - Info, actions
- **Dim** - Skipped/filtered, separators
- **White** - Message text

## Log Files (`--log-file`)

When `--log-file` is specified:
- ALL output is written to file (ANSI codes stripped)
- Terminal output retains colors and formatting
- File receives clean plaintext for parsing
- Log file is truncated on each run (fresh log)

Example:
```bash
python ff_tastytrade_scanner.py --tickers SPY --pairs 30-60 --log-file scan.log
```

## Implementation Details

### Rich Console
- Uses `Console(force_terminal=True)` for color even when redirected
- ANSI code stripping via regex for log files
- Unicode symbols for professional appearance

### Suppressed Loggers
To keep output clean, these third-party loggers are suppressed:
- `yfinance` → ERROR level only (no HTTP 404 spam)
- `tastytrade` → WARNING level
- `httpx` → WARNING level
- `earnings_cache` → WARNING level

## Best Practices

1. **Keep terminal output clean** - Use status symbols instead of verbose text
2. **Provide context** - Progress counters show scan progress
3. **Structured output** - Consistent format for parsing
4. **Suppress noise** - Third-party debug logs disabled by default
5. **Log to file** - Use `--log-file` for complete audit trails
