---
id: 07
name: CLI Enhancement & Help Documentation
status: todo
priority: medium
estimated_hours: 1-2
dependencies: [01, 03, 04, 05]
phase: 3
created: 2025-10-19T08:35:09Z
---

# Task 07: CLI Enhancement & Help Documentation

## Objective

Update argument parser with all new CLI flags, improve `--help` output with examples, and validate flag combinations to prevent user error.

## Scope

Consolidate all new CLI flags, add comprehensive help text, and implement flag validation logic.

## Technical Details

### Files to Modify
- `scripts/ff_tastytrade_scanner.py` (argparse setup in `main()`)

### Complete Argparse Setup

```python
def parse_args():
    """Parse command-line arguments with comprehensive help text."""
    parser = argparse.ArgumentParser(
        description='Forward Factor Calendar Spread Scanner v2.0',
        epilog='''
Examples:
  # Daily pre-market scan with all filters
  %(prog)s --tickers SPY QQQ AAPL TSLA NVDA \\
    --pairs 30-60 30-90 60-90 \\
    --min-ff 0.23 \\
    --structure both \\
    --csv-out scan.csv

  # Focus on 60-90 DTE double calendars
  %(prog)s --tickers SPY QQQ IWM \\
    --pairs 60-90 \\
    --structure double \\
    --min-ff 0.20

  # Debug: why didn't AAPL show up?
  %(prog)s --tickers AAPL \\
    --pairs 30-60 \\
    --show-earnings-conflicts \\
    --skip-liquidity-check

  # Aggressive scan (lower thresholds)
  %(prog)s --tickers SPY QQQ \\
    --pairs 30-60 60-90 \\
    --min-ff 0.15 \\
    --min-liquidity-rating 2
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # === Existing Flags (v1.0) ===
    parser.add_argument('--tickers', nargs='+', required=True,
                        help='Space-separated ticker symbols (e.g., SPY QQQ AAPL)')
    parser.add_argument('--pairs', nargs='+', required=True,
                        help='DTE pairs like 30-60 30-90 (front-back)')
    parser.add_argument('--min-ff', type=float, default=0.20,
                        help='Minimum Forward Factor threshold (default: 0.20)')
    parser.add_argument('--dte-tolerance', type=int, default=5,
                        help='Max deviation from target DTE (default: 5 days)')
    parser.add_argument('--timeout', type=float, default=3.0,
                        help='Greeks snapshot timeout in seconds (default: 3.0)')
    parser.add_argument('--sandbox', action='store_true',
                        help='Use sandbox environment (default: production)')
    parser.add_argument('--csv-out', type=str,
                        help='Output CSV file path')
    parser.add_argument('--json-out', type=str,
                        help='Output JSON file path (if implemented)')

    # === Earnings Filtering (New in v2.0) ===
    earnings_group = parser.add_argument_group('Earnings Filtering')
    earnings_mutex = earnings_group.add_mutually_exclusive_group()
    earnings_mutex.add_argument('--skip-earnings', action='store_true', default=True,
                                 help='Skip positions with earnings conflicts (default: True)')
    earnings_mutex.add_argument('--allow-earnings', action='store_true',
                                 help='Allow trading through earnings (overrides --skip-earnings)')
    earnings_group.add_argument('--show-earnings-conflicts', action='store_true',
                                 help='Show filtered positions due to earnings')

    # === Liquidity Screening (New in v2.0) ===
    liquidity_group = parser.add_argument_group('Liquidity Screening')
    liquidity_group.add_argument('--min-liquidity-rating', type=int, default=3,
                                  help='Minimum liquidity rating 0-5 (default: 3)')
    liquidity_group.add_argument('--skip-liquidity-check', action='store_true',
                                  help='Disable liquidity filtering')

    # === X-earn IV Support (New in v2.0) ===
    iv_group = parser.add_argument_group('IV Data Source')
    iv_mutex = iv_group.add_mutually_exclusive_group()
    iv_mutex.add_argument('--use-xearn-iv', action='store_true', default=True,
                          help='Use X-earn IV from market metrics if available (default: True)')
    iv_mutex.add_argument('--force-greeks-iv', action='store_true',
                          help='Always use dxFeed Greeks IV')

    # === Double Calendar Structure (New in v2.0) ===
    structure_group = parser.add_argument_group('Calendar Structure')
    structure_group.add_argument('--structure', type=str, default='both',
                                  choices=['atm-call', 'double', 'both'],
                                  help='Structure type: atm-call, double, or both (default: both)')
    structure_group.add_argument('--delta-tolerance', type=float, default=0.05,
                                  help='Max delta deviation for double calendars (default: 0.05)')

    return parser.parse_args()
```

### Flag Validation Logic

```python
def validate_args(args):
    """
    Validate argument combinations and apply overrides.

    Raises:
        ValueError: If invalid argument combination
    """
    # Override: --allow-earnings disables --skip-earnings
    if args.allow_earnings:
        args.skip_earnings = False

    # Validation: min_liquidity_rating must be 0-5
    if not (0 <= args.min_liquidity_rating <= 5):
        raise ValueError(f"--min-liquidity-rating must be 0-5, got {args.min_liquidity_rating}")

    # Validation: delta_tolerance must be 0.0-0.20
    if not (0.0 <= args.delta_tolerance <= 0.20):
        raise ValueError(f"--delta-tolerance must be 0.0-0.20, got {args.delta_tolerance}")

    # Validation: min_ff should be reasonable (warn if > 0.50)
    if args.min_ff > 0.50:
        print(f"[WARN] --min-ff {args.min_ff} is very high, you may get zero results")

    # Validation: timeout must be positive
    if args.timeout <= 0:
        raise ValueError(f"--timeout must be positive, got {args.timeout}")

    # Info: production environment required for full data
    if args.sandbox:
        print("[WARN] Using sandbox environment - market data may be limited")

    return args
```

### Integration into Main

```python
async def main():
    """Main scanner entry point."""
    # Parse and validate arguments
    args = parse_args()
    args = validate_args(args)

    # Print configuration summary
    print(f"[CONFIG]")
    print(f"  Tickers: {', '.join(args.tickers)}")
    print(f"  DTE pairs: {', '.join(args.pairs)}")
    print(f"  Min FF: {args.min_ff}")
    print(f"  Structure: {args.structure}")
    print(f"  Skip earnings: {args.skip_earnings}")
    print(f"  Min liquidity rating: {args.min_liquidity_rating}")
    print(f"  Use X-earn IV: {args.use_xearn_iv}")
    print()

    # ... rest of main() ...
```

## Deliverables

- [ ] All CLI flags consolidated in argparse setup
- [ ] Argument groups for logical organization (earnings, liquidity, IV, structure)
- [ ] Mutually exclusive groups for conflicting flags
- [ ] Comprehensive `--help` output with examples
- [ ] `validate_args()` function for flag validation
- [ ] Configuration summary printed at start of scan
- [ ] Error messages for invalid flag combinations

## Testing Checklist

- [ ] Test `--help`: verify all flags documented with examples
- [ ] Test `--allow-earnings`: verify it overrides `--skip-earnings`
- [ ] Test invalid `--min-liquidity-rating 6`: verify error raised
- [ ] Test invalid `--delta-tolerance 0.3`: verify error raised
- [ ] Test `--structure invalid`: verify choices constraint works
- [ ] Test high `--min-ff 0.8`: verify warning printed
- [ ] Test `--sandbox`: verify warning about limited data
- [ ] Test config summary: verify printed at scan start

## Acceptance Criteria

- ✅ `--help` output is clear, comprehensive, and includes examples
- ✅ Argument groups organize flags logically (earnings, liquidity, IV, structure)
- ✅ Mutually exclusive flags enforced (e.g., --allow-earnings vs --skip-earnings)
- ✅ Invalid flag combinations raise clear error messages
- ✅ Configuration summary printed before scan starts
- ✅ All new flags documented with defaults and descriptions
- ✅ Examples in help text match actual usage scenarios

## Notes

- **Help Text Quality**: Users should be able to understand all flags without reading docs
- **Validation First**: Catch invalid flags before expensive API calls
- **Configuration Summary**: Helps user verify scan settings before waiting for results
- **Examples**: Cover common use cases from PRD Appendix C
