#!/usr/bin/env python3
"""
Test using Trade event instead of Quote for futures.
"""
import os
import asyncio
from tastytrade import Session
from tastytrade.dxfeed import Trade
from tastytrade.streamer import DXLinkStreamer
from tastytrade.instruments import NestedFutureOptionChain

async def test_futures_trade():
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

    # Try Trade event
    print(f"\n{'='*60}")
    print(f"Testing Trade event with symbol: '{active_contract}'")
    print(f"{'='*60}")

    try:
        async with DXLinkStreamer(session) as streamer:
            await streamer.subscribe(Trade, [active_contract])

            async def get_trade():
                async for trade in streamer.listen(Trade):
                    print(f"Got trade: {trade}")
                    return trade

            trade = await asyncio.wait_for(get_trade(), timeout=5.0)
            print(f"SUCCESS! Price: {trade.price}, Size: {trade.size}")

    except asyncio.TimeoutError:
        print(f"TIMEOUT - No trade received")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    asyncio.run(test_futures_trade())
