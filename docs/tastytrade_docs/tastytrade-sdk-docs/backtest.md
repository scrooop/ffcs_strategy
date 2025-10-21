Backtesting - tastytrade 10.1.0 documentation












tastytrade 10.1.0 documentation

Backtesting






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
  + [Backtesting](backtest.html#)
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

# Backtesting[¶](backtest.html#backtesting "Link to this heading")

Backtesting is a beta feature recently added to Tastytrade, so please report any issues!

Let’s see how to perform a backtest:

```
from datetime import timedelta
from tastytrade.backtest import (
    Backtest,
    BacktestEntry,
    BacktestExit,
    BacktestLeg,
    BacktestSession,
    today_in_new_york
 )
 from tqdm.asyncio import tqdm  # progress bar
 backtest_session = BacktestSession(session)
 backtest = Backtest(
     symbol="SPY",
     entry_conditions=BacktestEntry(),
     exit_conditions=BacktestExit(at_days_to_expiration=21),
     legs=[BacktestLeg(), BacktestLeg(side="put")],
     start_date=today_in_new_york() - timedelta(days=365)
 )
 results = [r async for r in tqdm(backtest_session.run(backtest))]
 print(results[-1])

```

There are lots of configuration options you can find in the documentation for each class.
The `run` function is an `AsyncGenerator`, so you can do something else while a backtest is running, show a progress bar, or maybe even run several at once!

[Back to top](backtest.html#)


[Previous
Market Data](market-data.html)
[Next
Market Sessions](market-sessions.html)

© Copyright 2025, tastyware.

Created using
[Sphinx](https://www.sphinx-doc.org/)
7.4.7.
and
[Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)