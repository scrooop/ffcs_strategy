Sessions - tastytrade 10.1.0 documentation







[Skip to content](sessions.html#creating-a-session)

tastytrade 10.1.0 documentation

Sessions






Initializing search

[tastytrade](https://github.com/tastyware/tastytrade "Go to repository")

tastytrade 10.1.0 documentation

[tastytrade](https://github.com/tastyware/tastytrade "Go to repository")

* Documentation




  Documentation
  + [Installation](installation.html)
  + Sessions

    [Sessions](sessions.html#)



    Sessions
    - [Creating a session](sessions.html#creating-a-session)
  + [sync/async](sync-async.html)
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

Sessions

* [Creating a session](sessions.html#creating-a-session)

# Sessions[¶](sessions.html#sessions "Link to this heading")

## Creating a session[¶](sessions.html#creating-a-session "Link to this heading")

A session object is required to authenticate your requests to the Tastytrade API.
To create a production (real) session using your normal login:

```
from tastytrade import Session
session = Session('username', 'password')

```

A certification (test) account can be created [here](https://developer.tastytrade.com/sandbox/), then used to create a session.

```
from tastytrade import Session
session = Session('username', 'password', is_test=True)

```

You can make a session persistent by generating a remember token, which is valid for 24 hours:

```
session = Session('username', 'password', remember_me=True)
remember_token = session.remember_token
# remember token replaces the password for the next login
new_session = Session('username', remember_token=remember_token)

```

Note

If you used a certification (test) account to create the session associated with the remember\_token, you must set is\_test=True when creating subsequent sessions.

[Back to top](sessions.html#)


[Previous
Installation](installation.html)
[Next
sync/async](sync-async.html)

© Copyright 2025, tastyware.

Created using
[Sphinx](https://www.sphinx-doc.org/)
7.4.7.
and
[Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)