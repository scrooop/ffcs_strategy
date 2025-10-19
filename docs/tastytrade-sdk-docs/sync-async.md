sync/async - tastytrade 10.1.0 documentation












tastytrade 10.1.0 documentation

sync/async






Initializing search

[tastytrade](https://github.com/tastyware/tastytrade "Go to repository")

tastytrade 10.1.0 documentation

[tastytrade](https://github.com/tastyware/tastytrade "Go to repository")

* Documentation




  Documentation
  + [Installation](installation.html)
  + [Sessions](sessions.html)
  + [sync/async](sync-async.html#)
  + [Accounts](accounts.html)
  + [Instruments](instruments.html)
  + [Orders](orders.html)
  + [Account Streamer](account-streamer.html)
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

# sync/async[¶](sync-async.html#sync-async "Link to this heading")

After creating a session (which is always initialized synchronously), the rest of the API endpoints implemented in the SDK have both sync and async implementations as of version 9.0.

Let’s see how this looks:

```
from tastytrade Account, Session
session = Session(username, password)
# using sync implementation
accounts = Account.get(session)

```

The async implementation is similar:

```
from tastytrade Account, Session
session = Session(username, password)
# using async implementation
accounts = await Account.a_get(session)

```

That’s it! All sync methods have a parallel async method that starts with a\_.

Note

Please note that two modules, tastytrade.backtest and tastytrade.streamer, only have async implementations. But for everything else, you can use what you’d like!

[Back to top](sync-async.html#)


[Previous
Sessions](sessions.html)
[Next
Accounts](accounts.html)

© Copyright 2025, tastyware.

Created using
[Sphinx](https://www.sphinx-doc.org/)
7.4.7.
and
[Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)