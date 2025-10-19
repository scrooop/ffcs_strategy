Account Streamer - tastytrade 10.1.0 documentation







[Skip to content](account-streamer.html#basic-usage)

tastytrade 10.1.0 documentation

Account Streamer






Initializing search

[tastytrade](https://github.com/tastyware/tastytrade "Go to repository")

tastytrade 10.1.0 documentation

[tastytrade](https://github.com/tastyware/tastytrade "Go to repository")

* Documentation




  Documentation
  + [Installation](installation.html)
  + [Sessions](sessions.html)
  + [sync/async](sync-async.html)
  + [Accounts](accounts.html)
  + [Instruments](instruments.html)
  + [Orders](orders.html)
  + Account Streamer

    [Account Streamer](account-streamer.html#)



    Account Streamer
    - [Basic usage](account-streamer.html#basic-usage)
    - [Retry callback](account-streamer.html#retry-callback)
  + [Data Streamer](data-streamer.html)
  + [Market Data](market-data.html)
  + [Backtesting](backtest.html)
  + [Market Sessions](market-sessions.html)
  + [Watchlists](watchlists.html)
* SDK Reference




  SDK Reference
  + [tastytrade.account](api/account.html)
  + [tastytrade.backtest](api/backtesting.html)
  + [tastytrade.dxfeed](api/dxfeed.html)
  + [tastytrade.instruments](api/instruments.html)
  + [tastytrade.market\_sessions](api/market-sessions.html)
  + [tastytrade.metrics](api/metrics.html)
  + [tastytrade.order](api/order.html)
  + [tastytrade.search](api/search.html)
  + [tastytrade.session](api/session.html)
  + [tastytrade.streamer](api/streamer.html)
  + [tastytrade.utils](api/utils.html)
  + [tastytrade.watchlists](api/watchlists.html)

Account Streamer

* [Basic usage](account-streamer.html#basic-usage)
* [Retry callback](account-streamer.html#retry-callback)

# Account Streamer[¶](account-streamer.html#account-streamer "Link to this heading")

## Basic usage[¶](account-streamer.html#basic-usage "Link to this heading")

The account streamer is used to track account-level updates, such as order fills, watchlist updates and quote alerts.
Typically, you’ll want a separate task running for the account streamer, which can then notify your application about important events.

Here’s an example of setting up an account streamer to continuously wait for events and print them:

```
from tastytrade import Account, AlertStreamer, Watchlist

async with AlertStreamer(session) as streamer:
    accounts = Account.get(session)

    # updates to balances, orders, and positions
    await streamer.subscribe_accounts(accounts)
    # changes in public watchlists
    await streamer.subscribe_public_watchlists()
    # quote alerts configured by the user
    await streamer.subscribe_quote_alerts()

    async for wl in streamer.listen(Watchlist):
        print(wl)

```

Probably the most important information the account streamer handles is order fills. We can listen just for orders like so:

```
from tastytrade.order import PlacedOrder

async with AlertStreamer(session) as streamer:
    accounts = Account.get(session)
    await streamer.subscribe_accounts(accounts)

    async for order in streamer.listen(PlacedOrder):
        print(order)

```

## Retry callback[¶](account-streamer.html#retry-callback "Link to this heading")

The account streamer has a special “callback” function which can be used to execute arbitrary code whenever the websocket reconnects. This is useful for re-subscribing to whatever alerts you wanted to subscribe to initially (in fact, you can probably use the same function/code you use when initializing the connection).
The callback function should look something like this:

```
async def callback(streamer: AlertStreamer, arg1, arg2):
    await streamer.subscribe_quote_alerts()

```

The requirements are that the first parameter be the AlertStreamer instance, and the function should be asynchronous. Other than that, you have the flexibility to decide what arguments you want to use.
This callback can then be used when creating the streamer:

```
async with AlertStreamer(session, reconnect_fn=callback, reconnect_args=(arg1, arg2)) as streamer:
    # ...

```

The reconnection uses websockets’ exponential backoff algorithm, which can be configured through environment variables [here](https://websockets.readthedocs.io/en/14.1/reference/variables.html).

[Back to top](account-streamer.html#)


[Previous
Orders](orders.html)
[Next
Data Streamer](data-streamer.html)

© Copyright 2025, tastyware.

Created using
[Sphinx](https://www.sphinx-doc.org/)
7.4.7.
and
[Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)