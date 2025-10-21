tastytrade.streamer - tastytrade 10.1.0 documentation







[Skip to content](streamer.html#tastytrade.streamer.AlertStreamer)

tastytrade 10.1.0 documentation

tastytrade.streamer






Initializing search

[tastytrade](https://github.com/tastyware/tastytrade "Go to repository")

tastytrade 10.1.0 documentation

[tastytrade](https://github.com/tastyware/tastytrade "Go to repository")

* Documentation




  Documentation
  + [Installation](../installation.html)
  + [Sessions](../sessions.html)
  + [sync/async](../sync-async.html)
  + [Accounts](../accounts.html)
  + [Instruments](../instruments.html)
  + [Orders](../orders.html)
  + [Account Streamer](../account-streamer.html)
  + [Data Streamer](../data-streamer.html)
  + [Market Data](../market-data.html)
  + [Backtesting](../backtest.html)
  + [Market Sessions](../market-sessions.html)
  + [Watchlists](../watchlists.html)
* SDK Reference




  SDK Reference
  + [tastytrade.account](account.html)
  + [tastytrade.backtest](backtesting.html)
  + [tastytrade.dxfeed](dxfeed.html)
  + [tastytrade.instruments](instruments.html)
  + [tastytrade.market\_sessions](market-sessions.html)
  + [tastytrade.metrics](metrics.html)
  + [tastytrade.order](order.html)
  + [tastytrade.search](search.html)
  + [tastytrade.session](session.html)
  + tastytrade.streamer

    [tastytrade.streamer](streamer.html#)



    tastytrade.streamer
    - [Ctastytrade.streamer.AlertStreamer](streamer.html#tastytrade.streamer.AlertStreamer)

      * [Abase\_url](streamer.html#tastytrade.streamer.AlertStreamer.base_url)
      * [Mclose](streamer.html#tastytrade.streamer.AlertStreamer.close)
      * [Mlisten](streamer.html#tastytrade.streamer.AlertStreamer.listen)

        + [Parameters](streamer.html#tastytrade.streamer.AlertStreamer.listen-parameters)

          - [palert\_class](streamer.html#tastytrade.streamer.AlertStreamer.listen.alert_class)
      * [Aproxy](streamer.html#tastytrade.streamer.AlertStreamer.proxy)
      * [Areconnect\_args](streamer.html#tastytrade.streamer.AlertStreamer.reconnect_args)
      * [Areconnect\_fn](streamer.html#tastytrade.streamer.AlertStreamer.reconnect_fn)
      * [Arequest\_id](streamer.html#tastytrade.streamer.AlertStreamer.request_id)
      * [Msubscribe\_accounts](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_accounts)

        + [Parameters](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_accounts-parameters)

          - [paccounts](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_accounts.accounts)
      * [Msubscribe\_public\_watchlists](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_public_watchlists)
      * [Msubscribe\_quote\_alerts](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_quote_alerts)
      * [Msubscribe\_user\_messages](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_user_messages)
      * [Atoken](streamer.html#tastytrade.streamer.AlertStreamer.token)
    - [Vtastytrade.streamer.AlertType](streamer.html#tastytrade.streamer.AlertType)
    - [Ctastytrade.streamer.DXLinkStreamer](streamer.html#tastytrade.streamer.DXLinkStreamer)

      * [Mclose](streamer.html#tastytrade.streamer.DXLinkStreamer.close)
      * [Mget\_event](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event)

        + [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event-parameters)

          - [pevent\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event.event_class)
      * [Mget\_event\_nowait](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event_nowait)

        + [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event_nowait-parameters)

          - [pevent\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event_nowait.event_class)
      * [Mlisten](streamer.html#tastytrade.streamer.DXLinkStreamer.listen)

        + [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.listen-parameters)

          - [pevent\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.listen.event_class)
      * [Aproxy](streamer.html#tastytrade.streamer.DXLinkStreamer.proxy)
      * [Areconnect\_args](streamer.html#tastytrade.streamer.DXLinkStreamer.reconnect_args)
      * [Areconnect\_fn](streamer.html#tastytrade.streamer.DXLinkStreamer.reconnect_fn)
      * [Msubscribe](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe)

        + [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe-parameters)

          - [pevent\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe.event_class)
          - [psymbols](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe.symbols)
          - [prefresh\_interval](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe.refresh_interval)
      * [Msubscribe\_candle](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle)

        + [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle-parameters)

          - [psymbols](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.symbols)
          - [pinterval](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.interval)
          - [pstart\_time](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.start_time)
          - [pextended\_trading\_hours](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.extended_trading_hours)
          - [prefresh\_interval](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.refresh_interval)
      * [Munsubscribe](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe)

        + [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe-parameters)

          - [pevent\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe.event_class)
          - [psymbols](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe.symbols)
      * [Munsubscribe\_all](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_all)

        + [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_all-parameters)

          - [pevent\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_all.event_class)
      * [Munsubscribe\_candle](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle)

        + [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle-parameters)

          - [pticker](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.ticker)
          - [pinterval](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.interval)
          - [pextended\_trading\_hours](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.extended_trading_hours)
    - [Vtastytrade.streamer.EventType](streamer.html#tastytrade.streamer.EventType)
    - [tastytrade.streamer.QuoteAlert](streamer.html#tastytrade.streamer.QuoteAlert)

      * [Fields](streamer.html#tastytrade.streamer.QuoteAlert-fields)
    - [tastytrade.streamer.SubscriptionType](streamer.html#tastytrade.streamer.SubscriptionType)

      * [Member Type](streamer.html#tastytrade.streamer.SubscriptionType-member-type)
      * [AACCOUNT](streamer.html#tastytrade.streamer.SubscriptionType.ACCOUNT)
      * [AHEARTBEAT](streamer.html#tastytrade.streamer.SubscriptionType.HEARTBEAT)
      * [APUBLIC\_WATCHLISTS](streamer.html#tastytrade.streamer.SubscriptionType.PUBLIC_WATCHLISTS)
      * [AQUOTE\_ALERTS](streamer.html#tastytrade.streamer.SubscriptionType.QUOTE_ALERTS)
      * [AUSER\_MESSAGE](streamer.html#tastytrade.streamer.SubscriptionType.USER_MESSAGE)
    - [tastytrade.streamer.UnderlyingYearGainSummary](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary)

      * [Fields](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary-fields)
      * [Validators](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary-validators)
  + [tastytrade.utils](utils.html)
  + [tastytrade.watchlists](watchlists.html)

tastytrade.streamer

* [Ctastytrade.streamer.AlertStreamer](streamer.html#tastytrade.streamer.AlertStreamer)

  + [Abase\_url](streamer.html#tastytrade.streamer.AlertStreamer.base_url)
  + [Mclose](streamer.html#tastytrade.streamer.AlertStreamer.close)
  + [Mlisten](streamer.html#tastytrade.streamer.AlertStreamer.listen)

    - [Parameters](streamer.html#tastytrade.streamer.AlertStreamer.listen-parameters)

      * [palert\_class](streamer.html#tastytrade.streamer.AlertStreamer.listen.alert_class)
  + [Aproxy](streamer.html#tastytrade.streamer.AlertStreamer.proxy)
  + [Areconnect\_args](streamer.html#tastytrade.streamer.AlertStreamer.reconnect_args)
  + [Areconnect\_fn](streamer.html#tastytrade.streamer.AlertStreamer.reconnect_fn)
  + [Arequest\_id](streamer.html#tastytrade.streamer.AlertStreamer.request_id)
  + [Msubscribe\_accounts](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_accounts)

    - [Parameters](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_accounts-parameters)

      * [paccounts](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_accounts.accounts)
  + [Msubscribe\_public\_watchlists](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_public_watchlists)
  + [Msubscribe\_quote\_alerts](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_quote_alerts)
  + [Msubscribe\_user\_messages](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_user_messages)
  + [Atoken](streamer.html#tastytrade.streamer.AlertStreamer.token)
* [Vtastytrade.streamer.AlertType](streamer.html#tastytrade.streamer.AlertType)
* [Ctastytrade.streamer.DXLinkStreamer](streamer.html#tastytrade.streamer.DXLinkStreamer)

  + [Mclose](streamer.html#tastytrade.streamer.DXLinkStreamer.close)
  + [Mget\_event](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event)

    - [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event-parameters)

      * [pevent\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event.event_class)
  + [Mget\_event\_nowait](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event_nowait)

    - [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event_nowait-parameters)

      * [pevent\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event_nowait.event_class)
  + [Mlisten](streamer.html#tastytrade.streamer.DXLinkStreamer.listen)

    - [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.listen-parameters)

      * [pevent\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.listen.event_class)
  + [Aproxy](streamer.html#tastytrade.streamer.DXLinkStreamer.proxy)
  + [Areconnect\_args](streamer.html#tastytrade.streamer.DXLinkStreamer.reconnect_args)
  + [Areconnect\_fn](streamer.html#tastytrade.streamer.DXLinkStreamer.reconnect_fn)
  + [Msubscribe](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe)

    - [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe-parameters)

      * [pevent\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe.event_class)
      * [psymbols](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe.symbols)
      * [prefresh\_interval](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe.refresh_interval)
  + [Msubscribe\_candle](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle)

    - [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle-parameters)

      * [psymbols](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.symbols)
      * [pinterval](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.interval)
      * [pstart\_time](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.start_time)
      * [pextended\_trading\_hours](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.extended_trading_hours)
      * [prefresh\_interval](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.refresh_interval)
  + [Munsubscribe](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe)

    - [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe-parameters)

      * [pevent\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe.event_class)
      * [psymbols](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe.symbols)
  + [Munsubscribe\_all](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_all)

    - [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_all-parameters)

      * [pevent\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_all.event_class)
  + [Munsubscribe\_candle](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle)

    - [Parameters](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle-parameters)

      * [pticker](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.ticker)
      * [pinterval](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.interval)
      * [pextended\_trading\_hours](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.extended_trading_hours)
* [Vtastytrade.streamer.EventType](streamer.html#tastytrade.streamer.EventType)
* [tastytrade.streamer.QuoteAlert](streamer.html#tastytrade.streamer.QuoteAlert)

  + [Fields](streamer.html#tastytrade.streamer.QuoteAlert-fields)
* [tastytrade.streamer.SubscriptionType](streamer.html#tastytrade.streamer.SubscriptionType)

  + [Member Type](streamer.html#tastytrade.streamer.SubscriptionType-member-type)
  + [AACCOUNT](streamer.html#tastytrade.streamer.SubscriptionType.ACCOUNT)
  + [AHEARTBEAT](streamer.html#tastytrade.streamer.SubscriptionType.HEARTBEAT)
  + [APUBLIC\_WATCHLISTS](streamer.html#tastytrade.streamer.SubscriptionType.PUBLIC_WATCHLISTS)
  + [AQUOTE\_ALERTS](streamer.html#tastytrade.streamer.SubscriptionType.QUOTE_ALERTS)
  + [AUSER\_MESSAGE](streamer.html#tastytrade.streamer.SubscriptionType.USER_MESSAGE)
* [tastytrade.streamer.UnderlyingYearGainSummary](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary)

  + [Fields](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary-fields)
  + [Validators](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary-validators)

# tastytrade.streamer[¶](streamer.html#module-tastytrade.streamer "Link to this heading")

*class* tastytrade.streamer.AlertStreamer(*[session](streamer.html#tastytrade.streamer.AlertStreamer "tastytrade.streamer.AlertStreamer.__init__.session (Python parameter)"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[reconnect\_args](streamer.html#tastytrade.streamer.AlertStreamer "tastytrade.streamer.AlertStreamer.__init__.reconnect_args (Python parameter)"): [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)"), ...] = `()`*, *[reconnect\_fn](streamer.html#tastytrade.streamer.AlertStreamer "tastytrade.streamer.AlertStreamer.__init__.reconnect_fn (Python parameter)"): [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.13)")[[...], [Coroutine](https://docs.python.org/3/library/collections.abc.html#collections.abc.Coroutine "(in Python v3.13)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](streamer.html#tastytrade.streamer.AlertStreamer "Link to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    Used to subscribe to account-level updates (balances, orders, positions),
    public watchlist updates, quote alerts, and user-level messages. It should
    always be initialized as an async context manager, or by awaiting it,
    since the object cannot be fully instantiated without async.

    Example usage:

    ```
    from tastytrade import Account, AlertStreamer
    from tastytrade.order import PlacedOrder

    async with AlertStreamer(session) as streamer:
        accounts = Account.get_accounts(session)

        # updates to balances, orders, and positions
        await streamer.subscribe_accounts(accounts)
        # changes in public watchlists
        await streamer.subscribe_public_watchlists()
        # quote alerts configured by the user
        await streamer.subscribe_quote_alerts()

        async for order in streamer.listen(PlacedOrder):
            print(order)

    ```

    Or:

    ```
    streamer = await AlertStreamer(session)

    ```

    base\_url : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.AlertStreamer.base_url "Link to this definition")
    :   The base url for the streamer websocket

    *async* close() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.AlertStreamer.close "Link to this definition")
    :   Closes the websocket connection and cancels the pending tasks.

    *async* listen(*[alert\_class](streamer.html#tastytrade.streamer.AlertStreamer.listen.alert_class "tastytrade.streamer.AlertStreamer.listen.alert_class (Python parameter) — the type of alert to listen for, should be of AlertType"): [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.13)")[T]*) → [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "(in Python v3.13)")[T][¶](streamer.html#tastytrade.streamer.AlertStreamer.listen "Link to this definition")
    :   Iterate over non-heartbeat messages received from the streamer,
        mapping them to their appropriate data class and yielding them.

        This is designed to be friendly for type checking; the return
        type will be the same class you pass in.

        Parameters:[¶](streamer.html#tastytrade.streamer.AlertStreamer.listen-parameters "Permalink to this headline")
        :   alert\_class: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.13)")[T][¶](streamer.html#tastytrade.streamer.AlertStreamer.listen.alert_class "Permalink to this definition")
            :   the type of alert to listen for, should be of [`AlertType`](streamer.html#tastytrade.streamer.AlertType "tastytrade.streamer.AlertType (Python data) — List of all possible types to stream with the alert streamer")

    proxy[¶](streamer.html#tastytrade.streamer.AlertStreamer.proxy "Link to this definition")
    :   The proxy URL, if any, associated with the session

    reconnect\_args[¶](streamer.html#tastytrade.streamer.AlertStreamer.reconnect_args "Link to this definition")
    :   Variable number of arguments to pass to the reconnect function

    reconnect\_fn[¶](streamer.html#tastytrade.streamer.AlertStreamer.reconnect_fn "Link to this definition")
    :   An async function to be called upon reconnection. The first argument must be
        of type AlertStreamer and will be a reference to the streamer object.

    request\_id[¶](streamer.html#tastytrade.streamer.AlertStreamer.request_id "Link to this definition")
    :   Counter used to track the request ID for the streamer

    *async* subscribe\_accounts(*[accounts](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_accounts.accounts "tastytrade.streamer.AlertStreamer.subscribe_accounts.accounts (Python parameter) — list of Account to subscribe to updates for"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[Account](account.html#tastytrade.account.Account "tastytrade.account.Account (Python model) — Bases: TastytradeData")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_accounts "Link to this definition")
    :   Subscribes to account-level updates (balances, orders, positions).

        Parameters:[¶](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_accounts-parameters "Permalink to this headline")
        :   accounts: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[Account](account.html#tastytrade.account.Account "tastytrade.account.Account (Python model) — Bases: TastytradeData")][¶](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_accounts.accounts "Permalink to this definition")
            :   list of `Account` to subscribe to updates for

    *async* subscribe\_public\_watchlists() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_public_watchlists "Link to this definition")
    :   Subscribes to public watchlist updates.

    *async* subscribe\_quote\_alerts() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_quote_alerts "Link to this definition")
    :   Subscribes to quote alerts (which are configured at a user level).

    *async* subscribe\_user\_messages(*[session](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_user_messages "tastytrade.streamer.AlertStreamer.subscribe_user_messages.session (Python parameter)"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.AlertStreamer.subscribe_user_messages "Link to this definition")
    :   Subscribes to user-level messages, e.g. new account creation.

    token : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.AlertStreamer.token "Link to this definition")
    :   The active session used to initiate the streamer or make requests

tastytrade.streamer.AlertType[¶](streamer.html#tastytrade.streamer.AlertType "Link to this definition")
:   List of all possible types to stream with the alert streamer

    alias of [`AccountBalance`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance (Python model) — Bases: TastytradeData") | [`PlacedComplexOrder`](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder (Python model) — Bases: TastytradeData") | [`PlacedOrder`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder (Python model) — Bases: TastytradeData") | [`OrderChain`](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain (Python model) — Bases: TastytradeData") | [`CurrentPosition`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition (Python model) — Bases: TastytradeData") | [`QuoteAlert`](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert (Python model) — Bases: TastytradeData") | [`TradingStatus`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus (Python model) — Bases: TastytradeData") | [`UnderlyingYearGainSummary`](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary (Python model) — Bases: TastytradeData") | [`Watchlist`](watchlists.html#tastytrade.watchlists.Watchlist "tastytrade.watchlists.Watchlist (Python model) — Bases: TastytradeData")

*class* tastytrade.streamer.DXLinkStreamer(*session: ~tastytrade.session.Session, reconnect\_args: tuple[~typing.Any, ...] = (), reconnect\_fn: ~typing.Callable[[...], ~typing.Coroutine[~typing.Any, ~typing.Any, None]] | None = None, ssl\_context: ~ssl.SSLContext = <ssl.SSLContext object>*)[¶](streamer.html#tastytrade.streamer.DXLinkStreamer "Link to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    A [`DXLinkStreamer`](streamer.html#tastytrade.streamer.DXLinkStreamer "tastytrade.streamer.DXLinkStreamer (Python class) — Bases: object") object is used to fetch quotes or greeks for a
    given symbol or list of symbols. It should always be initialized as an
    async context manager, or by awaiting it, since the object cannot be
    fully instantiated without async.

    Example usage:

    ```
    from tastytrade import DXLinkStreamer
    from tastytrade.dxfeed import Quote

    # must be a production session
    async with DXLinkStreamer(session) as streamer:
        subs = ['SPY']  # list of quotes to subscribe to
        await streamer.subscribe(Quote, subs)
        quote = await streamer.get_event(Quote)
        print(quote)

    ```

    Or:

    ```
    streamer = await DXLinkStreamer(session)

    ```

    *async* close() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.close "Link to this definition")
    :   Closes the websocket connection and cancels the heartbeat task.

    *async* get\_event(*[event\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event.event_class "tastytrade.streamer.DXLinkStreamer.get_event.event_class (Python parameter) — the type of alert to listen for, should be of EventType"): [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.13)")[U]*) → U[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event "Link to this definition")
    :   Using the existing subscription, pulls an event of the given type and
        returns it.

        This is designed to be friendly for type checking; the return
        type will be the same class you pass in.

        Parameters:[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event-parameters "Permalink to this headline")
        :   event\_class: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.13)")[U][¶](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event.event_class "Permalink to this definition")
            :   the type of alert to listen for, should be of [`EventType`](streamer.html#tastytrade.streamer.EventType "tastytrade.streamer.EventType (Python data) — List of all possible types to stream with the data streamer")

    get\_event\_nowait(*[event\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event_nowait.event_class "tastytrade.streamer.DXLinkStreamer.get_event_nowait.event_class (Python parameter) — the type of alert to listen for, should be of EventType"): [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.13)")[U]*) → U | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event_nowait "Link to this definition")
    :   Using the existing subscriptions, pulls an event of the given type and
        returns it. If the queue is empty None is returned.

        This is designed to be friendly for type checking; the return
        type will be the same class you pass in.

        Parameters:[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event_nowait-parameters "Permalink to this headline")
        :   event\_class: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.13)")[U][¶](streamer.html#tastytrade.streamer.DXLinkStreamer.get_event_nowait.event_class "Permalink to this definition")
            :   the type of alert to listen for, should be of [`EventType`](streamer.html#tastytrade.streamer.EventType "tastytrade.streamer.EventType (Python data) — List of all possible types to stream with the data streamer")

    *async* listen(*[event\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.listen.event_class "tastytrade.streamer.DXLinkStreamer.listen.event_class (Python parameter) — the type of alert to listen for, should be of EventType"): [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.13)")[U]*) → [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "(in Python v3.13)")[U][¶](streamer.html#tastytrade.streamer.DXLinkStreamer.listen "Link to this definition")
    :   Using the existing subscriptions, pulls events of the given type and
        yield returns them. Never exits unless there’s an error or the channel
        is closed.

        This is designed to be friendly for type checking; the return
        type will be the same class you pass in.

        Parameters:[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.listen-parameters "Permalink to this headline")
        :   event\_class: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.13)")[U][¶](streamer.html#tastytrade.streamer.DXLinkStreamer.listen.event_class "Permalink to this definition")
            :   the type of alert to listen for, should be of [`EventType`](streamer.html#tastytrade.streamer.EventType "tastytrade.streamer.EventType (Python data) — List of all possible types to stream with the data streamer")

    proxy[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.proxy "Link to this definition")
    :   The proxy URL, if any, associated with the session

    reconnect\_args[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.reconnect_args "Link to this definition")
    :   Variable number of arguments to pass to the reconnect function

    reconnect\_fn[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.reconnect_fn "Link to this definition")
    :   An async function to be called upon reconnection. The first argument must be
        of type DXLinkStreamer and will be a reference to the streamer object.

    *async* subscribe(*[event\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe.event_class "tastytrade.streamer.DXLinkStreamer.subscribe.event_class (Python parameter) — type of subscription to add, should be of EventType"): [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.13)")[[Candle](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle (Python model) — Bases: IndexedEvent") | [Greeks](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks (Python model) — Bases: IndexedEvent") | [Profile](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile (Python model) — Bases: Event") | [Quote](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote (Python model) — Bases: Event") | [Summary](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary (Python model) — Bases: Event") | [TheoPrice](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice (Python model) — Bases: IndexedEvent") | [TimeAndSale](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale (Python model) — Bases: IndexedEvent") | [Trade](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade (Python model) — Bases: Event") | [Underlying](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying (Python model) — Bases: IndexedEvent")]*, *[symbols](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe.symbols "tastytrade.streamer.DXLinkStreamer.subscribe.symbols (Python parameter) — list of symbols to subscribe for"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")]*, *[refresh\_interval](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe.refresh_interval "tastytrade.streamer.DXLinkStreamer.subscribe.refresh_interval (Python parameter) — Time in seconds between fetching new events from dxfeed for this event_class. You can try a higher value if processing quote updates quickly is not a high priority. Once refresh_interval is set for this event_class and channel is opened, it cannot be changed later."): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") = `0.1`*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe "Link to this definition")
    :   Subscribes to quotes for given list of symbols. Used for recurring data
        feeds.
        For candles, use [`subscribe_candle()`](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle "tastytrade.streamer.DXLinkStreamer.subscribe_candle (Python method) — Subscribes to candle data for the given list of symbols.") instead.

        Parameters:[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe-parameters "Permalink to this headline")
        :   event\_class: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.13)")[[Candle](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle (Python model) — Bases: IndexedEvent") | [Greeks](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks (Python model) — Bases: IndexedEvent") | [Profile](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile (Python model) — Bases: Event") | [Quote](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote (Python model) — Bases: Event") | [Summary](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary (Python model) — Bases: Event") | [TheoPrice](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice (Python model) — Bases: IndexedEvent") | [TimeAndSale](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale (Python model) — Bases: IndexedEvent") | [Trade](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade (Python model) — Bases: Event") | [Underlying](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying (Python model) — Bases: IndexedEvent")][¶](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe.event_class "Permalink to this definition")
            :   type of subscription to add, should be of [`EventType`](streamer.html#tastytrade.streamer.EventType "tastytrade.streamer.EventType (Python data) — List of all possible types to stream with the data streamer")

            symbols: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")][¶](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe.symbols "Permalink to this definition")
            :   list of symbols to subscribe for

            refresh\_interval: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") = `0.1`[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe.refresh_interval "Permalink to this definition")
            :   Time in seconds between fetching new events from dxfeed for this event\_class.
                You can try a higher value if processing quote updates quickly is not a high priority.
                Once refresh\_interval is set for this event\_class and channel is opened, it cannot be changed later.

    *async* subscribe\_candle(*[symbols](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.symbols "tastytrade.streamer.DXLinkStreamer.subscribe_candle.symbols (Python parameter) — list of symbols to get data for"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")]*, *[interval](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.interval "tastytrade.streamer.DXLinkStreamer.subscribe_candle.interval (Python parameter) — the width of each candle in time, e.g."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[start\_time](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.start_time "tastytrade.streamer.DXLinkStreamer.subscribe_candle.start_time (Python parameter) — starting time for the data range"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[extended\_trading\_hours](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.extended_trading_hours "tastytrade.streamer.DXLinkStreamer.subscribe_candle.extended_trading_hours (Python parameter) — whether to include extended trading"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`*, *[refresh\_interval](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.refresh_interval "tastytrade.streamer.DXLinkStreamer.subscribe_candle.refresh_interval (Python parameter) — Time in seconds between fetching new events from dxfeed for this event_class. You can try a higher value if processing quote updates quickly is not a high priority. Once refresh_interval is set for this event_class and channel is opened, it cannot be changed later."): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") = `0.1`*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle "Link to this definition")
    :   Subscribes to candle data for the given list of symbols.

        Parameters:[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle-parameters "Permalink to this headline")
        :   symbols: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")][¶](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.symbols "Permalink to this definition")
            :   list of symbols to get data for

            interval: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.interval "Permalink to this definition")
            :   the width of each candle in time, e.g. ’15s’, ‘5m’, ‘1h’, ‘3d’,
                ‘1w’, ‘1mo’

            start\_time: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.start_time "Permalink to this definition")
            :   starting time for the data range

            end\_time
            :   ending time for the data range

            extended\_trading\_hours: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.extended_trading_hours "Permalink to this definition")
            :   whether to include extended trading

            refresh\_interval: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") = `0.1`[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.subscribe_candle.refresh_interval "Permalink to this definition")
            :   Time in seconds between fetching new events from dxfeed for this event\_class.
                You can try a higher value if processing quote updates quickly is not a high priority.
                Once refresh\_interval is set for this event\_class and channel is opened, it cannot be changed later.

    *async* unsubscribe(*[event\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe.event_class "tastytrade.streamer.DXLinkStreamer.unsubscribe.event_class (Python parameter) — type of subscription to remove"): [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.13)")[[Candle](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle (Python model) — Bases: IndexedEvent") | [Greeks](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks (Python model) — Bases: IndexedEvent") | [Profile](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile (Python model) — Bases: Event") | [Quote](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote (Python model) — Bases: Event") | [Summary](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary (Python model) — Bases: Event") | [TheoPrice](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice (Python model) — Bases: IndexedEvent") | [TimeAndSale](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale (Python model) — Bases: IndexedEvent") | [Trade](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade (Python model) — Bases: Event") | [Underlying](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying (Python model) — Bases: IndexedEvent")]*, *[symbols](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe.symbols "tastytrade.streamer.DXLinkStreamer.unsubscribe.symbols (Python parameter) — list of symbols to unsubscribe from"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe "Link to this definition")
    :   Removes existing subscription for given list of symbols.
        For candles, use [`unsubscribe_candle()`](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle "tastytrade.streamer.DXLinkStreamer.unsubscribe_candle (Python method) — Removes existing subscription for a candle.") instead.

        Parameters:[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe-parameters "Permalink to this headline")
        :   event\_class: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.13)")[[Candle](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle (Python model) — Bases: IndexedEvent") | [Greeks](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks (Python model) — Bases: IndexedEvent") | [Profile](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile (Python model) — Bases: Event") | [Quote](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote (Python model) — Bases: Event") | [Summary](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary (Python model) — Bases: Event") | [TheoPrice](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice (Python model) — Bases: IndexedEvent") | [TimeAndSale](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale (Python model) — Bases: IndexedEvent") | [Trade](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade (Python model) — Bases: Event") | [Underlying](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying (Python model) — Bases: IndexedEvent")][¶](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe.event_class "Permalink to this definition")
            :   type of subscription to remove

            symbols: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")][¶](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe.symbols "Permalink to this definition")
            :   list of symbols to unsubscribe from

    *async* unsubscribe\_all(*[event\_class](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_all.event_class "tastytrade.streamer.DXLinkStreamer.unsubscribe_all.event_class (Python parameter) — type of event to unsubscribe from."): [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.13)")[[Candle](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle (Python model) — Bases: IndexedEvent") | [Greeks](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks (Python model) — Bases: IndexedEvent") | [Profile](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile (Python model) — Bases: Event") | [Quote](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote (Python model) — Bases: Event") | [Summary](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary (Python model) — Bases: Event") | [TheoPrice](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice (Python model) — Bases: IndexedEvent") | [TimeAndSale](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale (Python model) — Bases: IndexedEvent") | [Trade](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade (Python model) — Bases: Event") | [Underlying](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying (Python model) — Bases: IndexedEvent")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_all "Link to this definition")
    :   Unsubscribes to all events of the given event type.

        Parameters:[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_all-parameters "Permalink to this headline")
        :   event\_class: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.13)")[[Candle](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle (Python model) — Bases: IndexedEvent") | [Greeks](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks (Python model) — Bases: IndexedEvent") | [Profile](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile (Python model) — Bases: Event") | [Quote](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote (Python model) — Bases: Event") | [Summary](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary (Python model) — Bases: Event") | [TheoPrice](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice (Python model) — Bases: IndexedEvent") | [TimeAndSale](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale (Python model) — Bases: IndexedEvent") | [Trade](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade (Python model) — Bases: Event") | [Underlying](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying (Python model) — Bases: IndexedEvent")][¶](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_all.event_class "Permalink to this definition")
            :   type of event to unsubscribe from.

    *async* unsubscribe\_candle(*[ticker](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.ticker "tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.ticker (Python parameter) — symbol to unsubscribe from"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[interval](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.interval "tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.interval (Python parameter) — candle width to unsubscribe from"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[extended\_trading\_hours](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.extended_trading_hours "tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.extended_trading_hours (Python parameter) — whether candle to unsubscribe from contains extended trading hours"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle "Link to this definition")
    :   Removes existing subscription for a candle.

        Parameters:[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle-parameters "Permalink to this headline")
        :   ticker: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.ticker "Permalink to this definition")
            :   symbol to unsubscribe from

            interval: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.interval "Permalink to this definition")
            :   candle width to unsubscribe from

            extended\_trading\_hours: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`[¶](streamer.html#tastytrade.streamer.DXLinkStreamer.unsubscribe_candle.extended_trading_hours "Permalink to this definition")
            :   whether candle to unsubscribe from contains extended trading hours

tastytrade.streamer.EventType[¶](streamer.html#tastytrade.streamer.EventType "Link to this definition")
:   List of all possible types to stream with the data streamer

    alias of [`Candle`](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle (Python model) — Bases: IndexedEvent") | [`Greeks`](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks (Python model) — Bases: IndexedEvent") | [`Profile`](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile (Python model) — Bases: Event") | [`Quote`](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote (Python model) — Bases: Event") | [`Summary`](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary (Python model) — Bases: Event") | [`TheoPrice`](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice (Python model) — Bases: IndexedEvent") | [`TimeAndSale`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale (Python model) — Bases: IndexedEvent") | [`Trade`](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade (Python model) — Bases: Event") | [`Underlying`](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying (Python model) — Bases: IndexedEvent")

*pydantic model* tastytrade.streamer.QuoteAlert(*\**, *[user\_external\_id](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.user_external_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[symbol](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[alert\_external\_id](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.alert_external_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[expires\_at](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.expires_at (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[completed\_at](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.completed_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[created\_at](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.created_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[triggered\_at](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.triggered_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[field](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.field (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[operator](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.operator (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[threshold](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.threshold (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[threshold\_numeric](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.threshold_numeric (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[dx\_symbol](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.dx_symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)[¶](streamer.html#tastytrade.streamer.QuoteAlert "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass that contains information about a quote alert

    Show JSON schema

    ```
    {
       "title": "QuoteAlert",
       "description": "Dataclass that contains information about a quote alert",
       "type": "object",
       "properties": {
          "user-external-id": {
             "title": "User-External-Id",
             "type": "string"
          },
          "symbol": {
             "title": "Symbol",
             "type": "string"
          },
          "alert-external-id": {
             "title": "Alert-External-Id",
             "type": "string"
          },
          "expires-at": {
             "title": "Expires-At",
             "type": "integer"
          },
          "completed-at": {
             "format": "date-time",
             "title": "Completed-At",
             "type": "string"
          },
          "created-at": {
             "format": "date-time",
             "title": "Created-At",
             "type": "string"
          },
          "triggered-at": {
             "format": "date-time",
             "title": "Triggered-At",
             "type": "string"
          },
          "field": {
             "title": "Field",
             "type": "string"
          },
          "operator": {
             "title": "Operator",
             "type": "string"
          },
          "threshold": {
             "title": "Threshold",
             "type": "string"
          },
          "threshold-numeric": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Threshold-Numeric"
          },
          "dx-symbol": {
             "title": "Dx-Symbol",
             "type": "string"
          }
       },
       "required": [
          "user-external-id",
          "symbol",
          "alert-external-id",
          "expires-at",
          "completed-at",
          "created-at",
          "triggered-at",
          "field",
          "operator",
          "threshold",
          "threshold-numeric",
          "dx-symbol"
       ]
    }

    ```

    Fields:[¶](streamer.html#tastytrade.streamer.QuoteAlert-fields "Permalink to this headline")
    :   * [`alert_external_id (str)`](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.alert_external_id (Python parameter)")
        * [`completed_at (datetime.datetime)`](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.completed_at (Python parameter)")
        * [`created_at (datetime.datetime)`](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.created_at (Python parameter)")
        * [`dx_symbol (str)`](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.dx_symbol (Python parameter)")
        * [`expires_at (int)`](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.expires_at (Python parameter)")
        * [`field (str)`](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.field (Python parameter)")
        * [`operator (str)`](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.operator (Python parameter)")
        * [`symbol (str)`](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.symbol (Python parameter)")
        * [`threshold (str)`](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.threshold (Python parameter)")
        * [`threshold_numeric (decimal.Decimal)`](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.threshold_numeric (Python parameter)")
        * [`triggered_at (datetime.datetime)`](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.triggered_at (Python parameter)")
        * [`user_external_id (str)`](streamer.html#tastytrade.streamer.QuoteAlert "tastytrade.streamer.QuoteAlert.user_external_id (Python parameter)")

*enum* tastytrade.streamer.SubscriptionType(*[value](streamer.html#tastytrade.streamer.SubscriptionType "tastytrade.streamer.SubscriptionType.value (Python parameter)")*)[¶](streamer.html#tastytrade.streamer.SubscriptionType "Link to this definition")
:   Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.13)")

    This is an [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.13)") that contains the subscription types
    for the alert streamer.

    Member Type:[¶](streamer.html#tastytrade.streamer.SubscriptionType-member-type "Permalink to this headline")
    :   [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Valid values are as follows:

    ACCOUNT = `<SubscriptionType.ACCOUNT: 'connect'>`[¶](streamer.html#tastytrade.streamer.SubscriptionType.ACCOUNT "Link to this definition")

    HEARTBEAT = `<SubscriptionType.HEARTBEAT: 'heartbeat'>`[¶](streamer.html#tastytrade.streamer.SubscriptionType.HEARTBEAT "Link to this definition")

    PUBLIC\_WATCHLISTS = `<SubscriptionType.PUBLIC_WATCHLISTS: 'public-watchlists-subscribe'>`[¶](streamer.html#tastytrade.streamer.SubscriptionType.PUBLIC_WATCHLISTS "Link to this definition")

    QUOTE\_ALERTS = `<SubscriptionType.QUOTE_ALERTS: 'quote-alerts-subscribe'>`[¶](streamer.html#tastytrade.streamer.SubscriptionType.QUOTE_ALERTS "Link to this definition")

    USER\_MESSAGE = `<SubscriptionType.USER_MESSAGE: 'user-message-subscribe'>`[¶](streamer.html#tastytrade.streamer.SubscriptionType.USER_MESSAGE "Link to this definition")

*pydantic model* tastytrade.streamer.UnderlyingYearGainSummary(*\**, *[year](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.year (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[account\_number](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.account_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[symbol](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[instrument\_type](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.instrument_type (Python parameter)"): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum")*, *[fees](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.fees (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[commissions](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.commissions (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[yearly\_realized\_gain](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.yearly_realized_gain (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[realized\_lot\_gain](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.realized_lot_gain (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*)[¶](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass that contains information about the yearly gain
    or loss for an underlying

    Show JSON schema

    ```
    {
       "title": "UnderlyingYearGainSummary",
       "description": "Dataclass that contains information about the yearly gain\nor loss for an underlying",
       "type": "object",
       "properties": {
          "year": {
             "title": "Year",
             "type": "integer"
          },
          "account-number": {
             "title": "Account-Number",
             "type": "string"
          },
          "symbol": {
             "title": "Symbol",
             "type": "string"
          },
          "instrument-type": {
             "$ref": "#/$defs/InstrumentType"
          },
          "fees": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Fees"
          },
          "commissions": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Commissions"
          },
          "yearly-realized-gain": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Yearly-Realized-Gain"
          },
          "realized-lot-gain": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Realized-Lot-Gain"
          }
       },
       "$defs": {
          "InstrumentType": {
             "description": "This is an :class:`~enum.Enum` that contains the valid types of instruments\nand their representation in the API.",
             "enum": [
                "Bond",
                "Cryptocurrency",
                "Currency Pair",
                "Equity",
                "Equity Offering",
                "Equity Option",
                "Fixed Income Security",
                "Future",
                "Future Option",
                "Index",
                "Liquidity Pool",
                "Unknown",
                "Warrant"
             ],
             "title": "InstrumentType",
             "type": "string"
          }
       },
       "required": [
          "year",
          "account-number",
          "symbol",
          "instrument-type",
          "fees",
          "commissions",
          "yearly-realized-gain",
          "realized-lot-gain"
       ]
    }

    ```

    Fields:[¶](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary-fields "Permalink to this headline")
    :   * [`account_number (str)`](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.account_number (Python parameter)")
        * [`commissions (decimal.Decimal)`](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.commissions (Python parameter)")
        * [`fees (decimal.Decimal)`](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.fees (Python parameter)")
        * [`instrument_type (tastytrade.order.InstrumentType)`](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.instrument_type (Python parameter)")
        * [`realized_lot_gain (decimal.Decimal)`](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.realized_lot_gain (Python parameter)")
        * [`symbol (str)`](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.symbol (Python parameter)")
        * [`year (int)`](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.year (Python parameter)")
        * [`yearly_realized_gain (decimal.Decimal)`](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary "tastytrade.streamer.UnderlyingYearGainSummary.yearly_realized_gain (Python parameter)")

    Validators:[¶](streamer.html#tastytrade.streamer.UnderlyingYearGainSummary-validators "Permalink to this headline")
    :   * `validate_price_effects` » `all fields`

[Back to top](streamer.html#)


[Previous
tastytrade.session](session.html)
[Next
tastytrade.utils](utils.html)

© Copyright 2025, tastyware.

Created using
[Sphinx](https://www.sphinx-doc.org/)
7.4.7.
and
[Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)