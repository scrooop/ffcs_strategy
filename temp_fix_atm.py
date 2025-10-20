#!/usr/bin/env python3
"""Temporary script to apply ATM calendar logic changes for Issue #36."""

import re

def main():
    filepath = 'scripts/ff_tastytrade_scanner.py'

    with open(filepath, 'r') as f:
        content = f.read()

    # Pattern 1: Replace the ATM Greeks fetching section (starting at line ~1533)
    old_section_1 = '''            # Primary: Snapshot Greeks (to get IV and delta) for all ATM contracts
            try:
                greek_map = await snapshot_greeks(session, streamer_syms, timeout_s=timeout_s)
            except Exception as e:
                logger.warning(f"{sym}: Greeks streamer connection failed for {sym}: {e}. Falling back to X-earn IV.")
                greek_map = {}  # Empty map - will fall back to X-earn IV

            for target, ch in choices.items():
                call_iv = None
                put_iv = None
                # Unpack (iv, delta) tuples from greek_map
                if ch.call_streamer_symbol in greek_map:
                    iv, delta = greek_map[ch.call_streamer_symbol]
                    call_iv = iv if iv is not None and iv > 0 else None
                if ch.put_streamer_symbol in greek_map:
                    iv, delta = greek_map[ch.put_streamer_symbol]
                    put_iv = iv if iv is not None and iv > 0 else None

                # Store Greeks IV if available
                if call_iv:
                    call_iv_by_target[target] = call_iv
                    call_iv_source_by_target[target] = "greeks"
                if put_iv:
                    put_iv_by_target[target] = put_iv
                    put_iv_source_by_target[target] = "greeks"

            # Rare fallback: Use ex-earn IV for targets where Greeks IV is missing
            for target, ch in choices.items():
                # Check if we need fallback for call IV
                if target not in call_iv_by_target:
                    logger.warning(f"{sym} {target}DTE: Greeks IV missing for call, using ex-earn fallback")
                    xearn_iv = extract_xearn_iv(market_metrics, sym, ch.expiration)
                    if xearn_iv is not None and xearn_iv > 0:
                        call_iv_by_target[target] = xearn_iv
                        call_iv_source_by_target[target] = "exearn_fallback"

                # Check if we need fallback for put IV
                if target not in put_iv_by_target:
                    logger.warning(f"{sym} {target}DTE: Greeks IV missing for put, using ex-earn fallback")
                    xearn_iv = extract_xearn_iv(market_metrics, sym, ch.expiration)
                    if xearn_iv is not None and xearn_iv > 0:
                        put_iv_by_target[target] = xearn_iv
                        put_iv_source_by_target[target] = "exearn_fallback"'''

    new_section_1 = '''            # Conditionally fetch Greeks or use ex-earn IV based on use_exearn_iv flag
            if use_exearn_iv:
                # Use ex-earn IV as primary source (skip Greeks streaming)
                greek_map = {}  # Empty map - will use ex-earn IV below
            else:
                # Primary: Snapshot Greeks (to get IV and delta) for all ATM contracts
                try:
                    greek_map = await snapshot_greeks(session, streamer_syms, timeout_s=timeout_s)
                except Exception as e:
                    logger.warning(f"{sym}: Greeks streamer connection failed for {sym}: {e}. Falling back to X-earn IV.")
                    greek_map = {}  # Empty map - will fall back to X-earn IV

                for target, ch in choices.items():
                    call_iv = None
                    put_iv = None
                    # Unpack (iv, delta) tuples from greek_map
                    if ch.call_streamer_symbol in greek_map:
                        iv, delta = greek_map[ch.call_streamer_symbol]
                        call_iv = iv if iv is not None and iv > 0 else None
                    if ch.put_streamer_symbol in greek_map:
                        iv, delta = greek_map[ch.put_streamer_symbol]
                        put_iv = iv if iv is not None and iv > 0 else None

                    # Store Greeks IV if available
                    if call_iv:
                        call_iv_by_target[target] = call_iv
                        call_iv_source_by_target[target] = "greeks"
                    if put_iv:
                        put_iv_by_target[target] = put_iv
                        put_iv_source_by_target[target] = "greeks"

            # Use ex-earn IV for targets where Greeks IV is missing (or when --iv-ex-earn is enabled)
            for target, ch in choices.items():
                # Check if we need ex-earn IV for call IV
                if target not in call_iv_by_target:
                    if use_exearn_iv:
                        # Primary ex-earn IV mode (--iv-ex-earn flag)
                        xearn_iv = extract_xearn_iv(market_metrics, sym, ch.expiration)
                        if xearn_iv is not None and xearn_iv > 0:
                            call_iv_by_target[target] = xearn_iv
                            call_iv_source_by_target[target] = "exearn_primary"
                    else:
                        # Fallback mode (Greeks failed)
                        logger.warning(f"{sym} {target}DTE: Greeks IV missing for call, using ex-earn fallback")
                        xearn_iv = extract_xearn_iv(market_metrics, sym, ch.expiration)
                        if xearn_iv is not None and xearn_iv > 0:
                            call_iv_by_target[target] = xearn_iv
                            call_iv_source_by_target[target] = "exearn_fallback"

                # Check if we need ex-earn IV for put IV
                if target not in put_iv_by_target:
                    if use_exearn_iv:
                        # Primary ex-earn IV mode (--iv-ex-earn flag)
                        xearn_iv = extract_xearn_iv(market_metrics, sym, ch.expiration)
                        if xearn_iv is not None and xearn_iv > 0:
                            put_iv_by_target[target] = xearn_iv
                            put_iv_source_by_target[target] = "exearn_primary"
                    else:
                        # Fallback mode (Greeks failed)
                        logger.warning(f"{sym} {target}DTE: Greeks IV missing for put, using ex-earn fallback")
                        xearn_iv = extract_xearn_iv(market_metrics, sym, ch.expiration)
                        if xearn_iv is not None and xearn_iv > 0:
                            put_iv_by_target[target] = xearn_iv
                            put_iv_source_by_target[target] = "exearn_fallback"'''

    # Apply the replacement
    if old_section_1 in content:
        content = content.replace(old_section_1, new_section_1)
        print("✓ ATM Greeks fetching section updated")
    else:
        print("✗ ATM Greeks fetching section not found (may have already been updated)")

    # Write back
    with open(filepath, 'w') as f:
        f.write(content)

    print("Done!")

if __name__ == '__main__':
    main()
