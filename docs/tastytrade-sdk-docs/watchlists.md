Watchlists - tastytrade 10.1.0 documentation












tastytrade 10.1.0 documentation

Watchlists






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
  + [Account Streamer](account-streamer.html)
  + [Data Streamer](data-streamer.html)
  + [Market Data](market-data.html)
  + [Backtesting](backtest.html)
  + [Market Sessions](market-sessions.html)
  + [Watchlists](watchlists.html#)
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

# Watchlists[¶](watchlists.html#watchlists "Link to this heading")

To use watchlists you’ll need a production session:

```
from tastytrade import Session
session = Session(user, password)

```

Let’s fetch an existing watchlist:

```
from tastytrade import PrivateWatchlist
watchlist = PrivateWatchlist.get(session, 'MyWatchlist')
print(watchlist.watchlist_entries)

```

```
>>> [{'symbol': 'AAPL', 'instrument-type': 'Equity'}, {'symbol': 'MSFT', 'instrument-type': 'Equity'}]

```

To add a symbol to the watchlist:

```
from tastytrade.instruments import InstrumentType
watchlist.add_symbol('SPY', InstrumentType.EQUITY)

```

In this case, the symbol is present locally, but not remotely, so we need to update the remote list:

```
watchlist.update(session)

```

We can also create a new watchlist from scratch, then publish it to the Tastytrade server:

```
new_watchlist = PrivateWatchlist(name='NewWatchlist')
new_watchlist.add_symbol('USO', InstrumentType.EQUITY)
new_watchlist.upload(session)

```

You can also fetch public watchlists:

```
from tastytrade import PublicWatchlist
public_watchlist = PublicWatchlist.get(session, "Tom's Watchlist")
print(public_watchlist.watchlist_entries)

```

[Back to top](watchlists.html#)


[Previous
Market Sessions](market-sessions.html)
[Next
tastytrade.account](api/account.html)

© Copyright 2025, tastyware.

Created using
[Sphinx](https://www.sphinx-doc.org/)
7.4.7.
and
[Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)