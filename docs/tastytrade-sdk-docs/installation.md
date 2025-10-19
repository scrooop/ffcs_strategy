Installation - tastytrade 10.1.0 documentation







[Skip to content](installation.html#via-pypi)

tastytrade 10.1.0 documentation

Installation






Initializing search

[tastytrade](https://github.com/tastyware/tastytrade "Go to repository")

tastytrade 10.1.0 documentation

[tastytrade](https://github.com/tastyware/tastytrade "Go to repository")

* Documentation




  Documentation
  + Installation

    [Installation](installation.html#)



    Installation
    - [Via pypi](installation.html#via-pypi)
    - [From source](installation.html#from-source)
    - [Windows](installation.html#windows)
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

Installation

* [Via pypi](installation.html#via-pypi)
* [From source](installation.html#from-source)
* [Windows](installation.html#windows)

# Installation[¶](installation.html#installation "Link to this heading")

## Via pypi[¶](installation.html#via-pypi "Link to this heading")

The easiest way to install the SDK is using pip:

```
$ pip install tastytrade

```

## From source[¶](installation.html#from-source "Link to this heading")

You can also install from source.
Make sure you have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed beforehand.

```
$ git clone https://github.com/tastyware/tastytrade.git
$ cd tastytrade
$ make install

```

If you’re contributing, you’ll want to run tests on your changes locally:

```
$ make lint
$ make test

```

If you want to build the documentation (usually not necessary):

```
$ make docs

```

## Windows[¶](installation.html#windows "Link to this heading")

If you want to install from source on Windows, you can’t use the Makefile, so just run the commands individually. For example:

```
$ git clone https://github.com/tastyware/tastytrade.git
$ cd tastytrade
$ uv sync
$ uv pip install -e .

```

[Back to top](installation.html#)


[Previous
Tastytrade Python SDK](index.html)
[Next
Sessions](sessions.html)

© Copyright 2025, tastyware.

Created using
[Sphinx](https://www.sphinx-doc.org/)
7.4.7.
and
[Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)