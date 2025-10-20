#!/usr/bin/env python3
"""
Test different symbol formats for futures quote streaming.
"""
import os
import asyncio
from tastytrade import Session
from tastytrade.dxfeed import Quote
from tastytrade.streamer import DXLinkStreamer
from tastytrade.instruments import NestedFutureOptionChain

async def test_futures_quote():
    # Authenticate
    username = os.getenv("TT_USERNAME")
    password = os.getenv("TT_PASSWORD")
    session = Session(username, password=password, is_test=False)

    # Get active contract
    chain = NestedFutureOptionChain.get(session, "/ES")
    active_contract = None
    for future in chain.futures:
        if hasattr(future, 'active_month') and future.active_month:
            active_contract = future.symbol
            break

    print(f"Active contract: {active_contract}")

    # Try different symbol formats
    test_symbols = [
        active_contract,  # /ESZ5
        active_contract.lstrip('/'),  # ESZ5
        f"/{active_contract.lstrip('/')}",  # Ensure leading slash
    ]

    for symbol in test_symbols:
        print(f"\n{'='*60}")
        print(f"Testing symbol: '{symbol}'")
        print(f"{'='*60}")

        try:
            async with DXLinkStreamer(session) as streamer:
                await streamer.subscribe(Quote, [symbol])

                async def get_quote():
                    async for quote in streamer.listen(Quote):
                        print(f"Got quote: {quote}")
                        return quote

                quote = await asyncio.wait_for(get_quote(), timeout=3.0)
                print(f"SUCCESS! Bid: {quote.bid_price}, Ask: {quote.ask_price}")
                break  # Found working format

        except asyncio.TimeoutError:
            print(f"TIMEOUT - No quote received for '{symbol}'")
        except Exception as e:
            print(f"ERROR: {e}")

if __name__ == "__main__":
    asyncio.run(test_futures_quote())
