---
id: 06
name: Enhanced CSV Output
status: todo
priority: high
estimated_hours: 2
dependencies: [01, 02, 04, 05]
phase: 3
created: 2025-10-19T08:35:09Z
---

# Task 06: Enhanced CSV Output

## Objective

Expand CSV schema to include all new columns from v2.0 features (earnings, liquidity, double calendar, X-earn IV), with proper formatting and sorting.

## Scope

Update CSV writing logic to output 25-column schema with ISO 8601 timestamps, structure indicators, and null handling for structure-specific fields.

## Technical Details

### Files to Modify
- `scripts/ff_tastytrade_scanner.py` (modify CSV writing logic)

### Full CSV Schema (25 Columns)

```csv
timestamp,symbol,structure,front_dte,back_dte,front_expiry,back_expiry,spot_price,
atm_strike,call_strike,put_strike,call_delta,put_delta,
front_iv,back_iv,fwd_iv,ff,call_ff,put_ff,combined_ff,
earnings_date,earnings_conflict,liquidity_rating,liquidity_value,
iv_source_front,iv_source_back
```

### Column Definitions

| Column | Type | Description | Null for ATM? | Null for Double? |
|--------|------|-------------|---------------|------------------|
| timestamp | ISO 8601 | Scan timestamp (UTC) | No | No |
| symbol | str | Ticker symbol | No | No |
| structure | str | "atm-call" or "double" | No | No |
| front_dte | int | Front DTE | No | No |
| back_dte | int | Back DTE | No | No |
| front_expiry | date | Front expiration (YYYY-MM-DD) | No | No |
| back_expiry | date | Back expiration (YYYY-MM-DD) | No | No |
| spot_price | float | Underlying price | No | No |
| atm_strike | float | ATM strike | No | Yes |
| call_strike | float | +35Δ call strike | Yes | No |
| put_strike | float | -35Δ put strike | Yes | No |
| call_delta | float | Call delta | Yes | No |
| put_delta | float | Put delta | Yes | No |
| front_iv | float | Front IV (or avg for double) | No | No |
| back_iv | float | Back IV (or avg for double) | No | No |
| fwd_iv | float | Forward IV (or avg for double) | No | No |
| ff | float | Forward Factor (ATM only) | No | Yes |
| call_ff | float | Call calendar FF (double only) | Yes | No |
| put_ff | float | Put calendar FF (double only) | Yes | No |
| combined_ff | float | Combined FF (or ff for ATM) | No | No |
| earnings_date | date | Next earnings (YYYY-MM-DD or null) | No | No |
| earnings_conflict | bool | "True" or "False" | No | No |
| liquidity_rating | float | Liquidity rating (0-5) | No | No |
| liquidity_value | float | Liquidity value (or null) | No | No |
| iv_source_front | str | "xearn" or "greeks" | No | No |
| iv_source_back | str | "xearn" or "greeks" | No | No |

### CSV Writing Function

```python
import csv
from datetime import datetime

def write_csv(results: List[Dict], output_file: str):
    """
    Write scan results to CSV with full schema.

    Args:
        results: List of result dicts from scan_symbol()
        output_file: Output CSV file path
    """
    if not results:
        print(f"[INFO] No results to write to {output_file}")
        return

    # Sort by combined_ff descending (highest opportunities first)
    sorted_results = sorted(results, key=lambda x: x.get('combined_ff', 0), reverse=True)

    # Get current timestamp (ISO 8601 UTC)
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Define column order
    columns = [
        'timestamp', 'symbol', 'structure', 'front_dte', 'back_dte',
        'front_expiry', 'back_expiry', 'spot_price',
        'atm_strike', 'call_strike', 'put_strike', 'call_delta', 'put_delta',
        'front_iv', 'back_iv', 'fwd_iv', 'ff', 'call_ff', 'put_ff', 'combined_ff',
        'earnings_date', 'earnings_conflict', 'liquidity_rating', 'liquidity_value',
        'iv_source_front', 'iv_source_back'
    ]

    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()

        for result in sorted_results:
            # Add timestamp to each row
            row = {'timestamp': timestamp}

            # Copy all result fields
            for col in columns[1:]:  # Skip timestamp (already added)
                value = result.get(col)

                # Handle None values (write empty string for null)
                if value is None:
                    row[col] = ''
                # Format dates as YYYY-MM-DD
                elif isinstance(value, date):
                    row[col] = value.strftime('%Y-%m-%d')
                # Format booleans as True/False
                elif isinstance(value, bool):
                    row[col] = str(value)
                # Format floats with precision
                elif isinstance(value, float):
                    row[col] = f"{value:.6f}"
                else:
                    row[col] = value

            writer.writerow(row)

    print(f"[INFO] Wrote {len(sorted_results)} results to {output_file}")
```

### Console Output Enhancement

Add summary statistics after scan:

```python
def print_summary(results: List[Dict]):
    """Print scan summary statistics."""
    if not results:
        print("[INFO] No opportunities found")
        return

    atm_count = sum(1 for r in results if r['structure'] == 'atm-call')
    double_count = sum(1 for r in results if r['structure'] == 'double')
    avg_ff = sum(r['combined_ff'] for r in results) / len(results)
    max_ff = max(r['combined_ff'] for r in results)

    print(f"\n[SUMMARY]")
    print(f"  Total opportunities: {len(results)}")
    print(f"  ATM calendars: {atm_count}")
    print(f"  Double calendars: {double_count}")
    print(f"  Average FF: {avg_ff:.4f}")
    print(f"  Max FF: {max_ff:.4f}")
```

## Deliverables

- [ ] `write_csv()` function updated with 25-column schema
- [ ] ISO 8601 timestamp added to all rows
- [ ] Sorting by combined_ff descending
- [ ] Null value handling for structure-specific columns
- [ ] Date formatting (YYYY-MM-DD)
- [ ] Float precision formatting (6 decimals)
- [ ] Console summary statistics function
- [ ] Column order matches specification

## Testing Checklist

- [ ] Test CSV output with ATM calendars: verify atm_strike populated, call/put strikes null
- [ ] Test CSV output with double calendars: verify call/put strikes populated, atm_strike null
- [ ] Test CSV output with `--structure both`: verify both structures in same CSV
- [ ] Test sorting: verify highest combined_ff is first row
- [ ] Test timestamp: verify ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
- [ ] Test null handling: verify empty string for null columns
- [ ] Test date formatting: verify YYYY-MM-DD format for expirations and earnings_date
- [ ] Test with no results: verify graceful handling (no file created or header-only)

## Acceptance Criteria

- ✅ CSV schema matches 25-column specification exactly
- ✅ Timestamp in ISO 8601 UTC format on all rows
- ✅ Sorted by combined_ff descending (highest first)
- ✅ Null columns show empty string (not "None" or "null")
- ✅ Dates formatted as YYYY-MM-DD
- ✅ Floats formatted with 6 decimal places
- ✅ Console summary shows opportunity counts and statistics
- ✅ Backward compatible with v1.0 CSV readers (superset of columns)

## Notes

- **Timestamp Consistency**: Use same timestamp for all rows in single scan
- **Sorting**: Critical for user workflow - highest FF opportunities shown first
- **Null Handling**: Empty string preferred over "None" for CSV parsing
- **Column Order**: Matches PRD Appendix B specification
- **Summary Statistics**: Helpful for quick assessment of scan quality
