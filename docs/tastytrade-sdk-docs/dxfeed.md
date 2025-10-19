tastytrade.dxfeed - tastytrade 10.1.0 documentation







[Skip to content](dxfeed.html#module-tastytrade.dxfeed.event)

tastytrade 10.1.0 documentation

tastytrade.dxfeed






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
  + tastytrade.dxfeed

    [tastytrade.dxfeed](dxfeed.html#)



    tastytrade.dxfeed
    - [Event](dxfeed.html#module-tastytrade.dxfeed.event)

      * [tastytrade.dxfeed.event.Event](dxfeed.html#tastytrade.dxfeed.event.Event)

        + [Fields](dxfeed.html#tastytrade.dxfeed.event.Event-fields)
        + [Validators](dxfeed.html#tastytrade.dxfeed.event.Event-validators)
        + [event\_symbol](dxfeed.html#tastytrade.dxfeed.event.Event.event_symbol)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.event.Event.event_symbol-validated-by)
        + [event\_time](dxfeed.html#tastytrade.dxfeed.event.Event.event_time)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.event.Event.event_time-validated-by)
        + [Mfrom\_stream](dxfeed.html#tastytrade.dxfeed.event.Event.from_stream)

          - [Parameters](dxfeed.html#tastytrade.dxfeed.event.Event.from_stream-parameters)

            * [pdata](dxfeed.html#tastytrade.dxfeed.event.Event.from_stream.data)
          - [Returns](dxfeed.html#tastytrade.dxfeed.event.Event.from_stream-returns)
      * [tastytrade.dxfeed.event.IndexedEvent](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent)

        + [Fields](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent-fields)
        + [Validators](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent-validators)
        + [event\_flags](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.event_flags)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.event_flags-validated-by)
        + [Ppending](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.pending)
        + [Premove](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.remove)
        + [Psnapshot\_begin](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.snapshot_begin)
        + [Psnapshot\_end](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.snapshot_end)
        + [Psnapshot\_mode](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.snapshot_mode)
        + [Psnapshot\_snip](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.snapshot_snip)
    - [Candle](dxfeed.html#module-tastytrade.dxfeed.candle)

      * [tastytrade.dxfeed.candle.Candle](dxfeed.html#tastytrade.dxfeed.candle.Candle)

        + [Fields](dxfeed.html#tastytrade.dxfeed.candle.Candle-fields)
        + [Validators](dxfeed.html#tastytrade.dxfeed.candle.Candle-validators)
        + [ask\_volume](dxfeed.html#tastytrade.dxfeed.candle.Candle.ask_volume)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.ask_volume-validated-by)
        + [bid\_volume](dxfeed.html#tastytrade.dxfeed.candle.Candle.bid_volume)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.bid_volume-validated-by)
        + [close](dxfeed.html#tastytrade.dxfeed.candle.Candle.close)

          - [Constraints](dxfeed.html#tastytrade.dxfeed.candle.Candle.close-constraints)
          - [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.close-validated-by)
        + [count](dxfeed.html#tastytrade.dxfeed.candle.Candle.count)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.count-validated-by)
        + [high](dxfeed.html#tastytrade.dxfeed.candle.Candle.high)

          - [Constraints](dxfeed.html#tastytrade.dxfeed.candle.Candle.high-constraints)
          - [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.high-validated-by)
        + [imp\_volatility](dxfeed.html#tastytrade.dxfeed.candle.Candle.imp_volatility)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.imp_volatility-validated-by)
        + [index](dxfeed.html#tastytrade.dxfeed.candle.Candle.index)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.index-validated-by)
        + [low](dxfeed.html#tastytrade.dxfeed.candle.Candle.low)

          - [Constraints](dxfeed.html#tastytrade.dxfeed.candle.Candle.low-constraints)
          - [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.low-validated-by)
        + [open](dxfeed.html#tastytrade.dxfeed.candle.Candle.open)

          - [Constraints](dxfeed.html#tastytrade.dxfeed.candle.Candle.open-constraints)
          - [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.open-validated-by)
        + [open\_interest](dxfeed.html#tastytrade.dxfeed.candle.Candle.open_interest)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.open_interest-validated-by)
        + [sequence](dxfeed.html#tastytrade.dxfeed.candle.Candle.sequence)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.sequence-validated-by)
        + [time](dxfeed.html#tastytrade.dxfeed.candle.Candle.time)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.time-validated-by)
        + [volume](dxfeed.html#tastytrade.dxfeed.candle.Candle.volume)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.volume-validated-by)
        + [vwap](dxfeed.html#tastytrade.dxfeed.candle.Candle.vwap)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.vwap-validated-by)
    - [Greeks](dxfeed.html#module-tastytrade.dxfeed.greeks)

      * [tastytrade.dxfeed.greeks.Greeks](dxfeed.html#tastytrade.dxfeed.greeks.Greeks)

        + [Fields](dxfeed.html#tastytrade.dxfeed.greeks.Greeks-fields)
        + [Validators](dxfeed.html#tastytrade.dxfeed.greeks.Greeks-validators)
        + [delta](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.delta)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.delta-validated-by)
        + [gamma](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.gamma)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.gamma-validated-by)
        + [index](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.index)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.index-validated-by)
        + [price](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.price-validated-by)
        + [rho](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.rho)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.rho-validated-by)
        + [sequence](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.sequence)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.sequence-validated-by)
        + [theta](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.theta)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.theta-validated-by)
        + [time](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.time)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.time-validated-by)
        + [vega](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.vega)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.vega-validated-by)
        + [volatility](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.volatility)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.volatility-validated-by)
    - [Profile](dxfeed.html#module-tastytrade.dxfeed.profile)

      * [tastytrade.dxfeed.profile.Profile](dxfeed.html#tastytrade.dxfeed.profile.Profile)

        + [Fields](dxfeed.html#tastytrade.dxfeed.profile.Profile-fields)
        + [Validators](dxfeed.html#tastytrade.dxfeed.profile.Profile-validators)
        + [beta](dxfeed.html#tastytrade.dxfeed.profile.Profile.beta)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.beta-validated-by)
        + [description](dxfeed.html#tastytrade.dxfeed.profile.Profile.description)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.description-validated-by)
        + [dividend\_frequency](dxfeed.html#tastytrade.dxfeed.profile.Profile.dividend_frequency)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.dividend_frequency-validated-by)
        + [earnings\_per\_share](dxfeed.html#tastytrade.dxfeed.profile.Profile.earnings_per_share)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.earnings_per_share-validated-by)
        + [ex\_dividend\_amount](dxfeed.html#tastytrade.dxfeed.profile.Profile.ex_dividend_amount)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.ex_dividend_amount-validated-by)
        + [ex\_dividend\_day\_id](dxfeed.html#tastytrade.dxfeed.profile.Profile.ex_dividend_day_id)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.ex_dividend_day_id-validated-by)
        + [free\_float](dxfeed.html#tastytrade.dxfeed.profile.Profile.free_float)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.free_float-validated-by)
        + [halt\_end\_time](dxfeed.html#tastytrade.dxfeed.profile.Profile.halt_end_time)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.halt_end_time-validated-by)
        + [halt\_start\_time](dxfeed.html#tastytrade.dxfeed.profile.Profile.halt_start_time)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.halt_start_time-validated-by)
        + [high\_52\_week\_price](dxfeed.html#tastytrade.dxfeed.profile.Profile.high_52_week_price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.high_52_week_price-validated-by)
        + [high\_limit\_price](dxfeed.html#tastytrade.dxfeed.profile.Profile.high_limit_price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.high_limit_price-validated-by)
        + [low\_52\_week\_price](dxfeed.html#tastytrade.dxfeed.profile.Profile.low_52_week_price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.low_52_week_price-validated-by)
        + [low\_limit\_price](dxfeed.html#tastytrade.dxfeed.profile.Profile.low_limit_price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.low_limit_price-validated-by)
        + [shares](dxfeed.html#tastytrade.dxfeed.profile.Profile.shares)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.shares-validated-by)
        + [short\_sale\_restriction](dxfeed.html#tastytrade.dxfeed.profile.Profile.short_sale_restriction)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.short_sale_restriction-validated-by)
        + [status\_reason](dxfeed.html#tastytrade.dxfeed.profile.Profile.status_reason)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.status_reason-validated-by)
        + [trading\_status](dxfeed.html#tastytrade.dxfeed.profile.Profile.trading_status)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.trading_status-validated-by)
    - [Quote](dxfeed.html#module-tastytrade.dxfeed.quote)

      * [tastytrade.dxfeed.quote.Quote](dxfeed.html#tastytrade.dxfeed.quote.Quote)

        + [Fields](dxfeed.html#tastytrade.dxfeed.quote.Quote-fields)
        + [Validators](dxfeed.html#tastytrade.dxfeed.quote.Quote-validators)
        + [ask\_exchange\_code](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_exchange_code)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_exchange_code-validated-by)
        + [ask\_price](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_price-validated-by)
        + [ask\_size](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_size)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_size-validated-by)
        + [ask\_time](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_time)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_time-validated-by)
        + [bid\_exchange\_code](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_exchange_code)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_exchange_code-validated-by)
        + [bid\_price](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_price-validated-by)
        + [bid\_size](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_size)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_size-validated-by)
        + [bid\_time](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_time)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_time-validated-by)
        + [sequence](dxfeed.html#tastytrade.dxfeed.quote.Quote.sequence)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.sequence-validated-by)
        + [time\_nano\_part](dxfeed.html#tastytrade.dxfeed.quote.Quote.time_nano_part)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.time_nano_part-validated-by)
    - [Summary](dxfeed.html#module-tastytrade.dxfeed.summary)

      * [tastytrade.dxfeed.summary.Summary](dxfeed.html#tastytrade.dxfeed.summary.Summary)

        + [Fields](dxfeed.html#tastytrade.dxfeed.summary.Summary-fields)
        + [Validators](dxfeed.html#tastytrade.dxfeed.summary.Summary-validators)
        + [day\_close\_price](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_close_price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_close_price-validated-by)
        + [day\_close\_price\_type](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_close_price_type)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_close_price_type-validated-by)
        + [day\_high\_price](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_high_price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_high_price-validated-by)
        + [day\_id](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_id)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_id-validated-by)
        + [day\_low\_price](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_low_price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_low_price-validated-by)
        + [day\_open\_price](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_open_price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_open_price-validated-by)
        + [open\_interest](dxfeed.html#tastytrade.dxfeed.summary.Summary.open_interest)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.open_interest-validated-by)
        + [prev\_day\_close\_price](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_close_price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_close_price-validated-by)
        + [prev\_day\_close\_price\_type](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_close_price_type)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_close_price_type-validated-by)
        + [prev\_day\_id](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_id)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_id-validated-by)
        + [prev\_day\_volume](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_volume)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_volume-validated-by)
    - [TimeAndSale](dxfeed.html#module-tastytrade.dxfeed.timeandsale)

      * [tastytrade.dxfeed.timeandsale.TimeAndSale](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale)

        + [Fields](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale-fields)
        + [Validators](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale-validators)
        + [aggressor\_side](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.aggressor_side)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.aggressor_side-validated-by)
        + [ask\_price](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.ask_price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.ask_price-validated-by)
        + [bid\_price](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.bid_price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.bid_price-validated-by)
        + [buyer](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.buyer)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.buyer-validated-by)
        + [exchange\_code](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_code)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_code-validated-by)
        + [exchange\_sale\_conditions](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_sale_conditions)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_sale_conditions-validated-by)
        + [extended\_trading\_hours](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.extended_trading_hours)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.extended_trading_hours-validated-by)
        + [index](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.index)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.index-validated-by)
        + [price](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.price-validated-by)
        + [seller](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.seller)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.seller-validated-by)
        + [sequence](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.sequence)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.sequence-validated-by)
        + [size](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.size)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.size-validated-by)
        + [spread\_leg](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.spread_leg)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.spread_leg-validated-by)
        + [time](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.time)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.time-validated-by)
        + [time\_nano\_part](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.time_nano_part)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.time_nano_part-validated-by)
        + [trade\_through\_exempt](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.trade_through_exempt)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.trade_through_exempt-validated-by)
        + [type](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.type)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.type-validated-by)
        + [valid\_tick](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.valid_tick)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.valid_tick-validated-by)
    - [TheoPrice](dxfeed.html#module-tastytrade.dxfeed.theoprice)

      * [tastytrade.dxfeed.theoprice.TheoPrice](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice)

        + [Fields](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice-fields)
        + [Validators](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice-validators)
        + [delta](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.delta)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.delta-validated-by)
        + [dividend](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.dividend)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.dividend-validated-by)
        + [gamma](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.gamma)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.gamma-validated-by)
        + [index](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.index)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.index-validated-by)
        + [interest](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.interest)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.interest-validated-by)
        + [price](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.price-validated-by)
        + [sequence](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.sequence)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.sequence-validated-by)
        + [time](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.time)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.time-validated-by)
        + [underlying\_price](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.underlying_price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.underlying_price-validated-by)
    - [Trade](dxfeed.html#module-tastytrade.dxfeed.trade)

      * [tastytrade.dxfeed.trade.Trade](dxfeed.html#tastytrade.dxfeed.trade.Trade)

        + [Fields](dxfeed.html#tastytrade.dxfeed.trade.Trade-fields)
        + [Validators](dxfeed.html#tastytrade.dxfeed.trade.Trade-validators)
        + [change](dxfeed.html#tastytrade.dxfeed.trade.Trade.change)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.change-validated-by)
        + [day\_id](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_id)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_id-validated-by)
        + [day\_turnover](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_turnover)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_turnover-validated-by)
        + [day\_volume](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_volume)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_volume-validated-by)
        + [exchange\_code](dxfeed.html#tastytrade.dxfeed.trade.Trade.exchange_code)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.exchange_code-validated-by)
        + [extended\_trading\_hours](dxfeed.html#tastytrade.dxfeed.trade.Trade.extended_trading_hours)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.extended_trading_hours-validated-by)
        + [price](dxfeed.html#tastytrade.dxfeed.trade.Trade.price)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.price-validated-by)
        + [sequence](dxfeed.html#tastytrade.dxfeed.trade.Trade.sequence)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.sequence-validated-by)
        + [size](dxfeed.html#tastytrade.dxfeed.trade.Trade.size)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.size-validated-by)
        + [tick\_direction](dxfeed.html#tastytrade.dxfeed.trade.Trade.tick_direction)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.tick_direction-validated-by)
        + [time](dxfeed.html#tastytrade.dxfeed.trade.Trade.time)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.time-validated-by)
        + [time\_nano\_part](dxfeed.html#tastytrade.dxfeed.trade.Trade.time_nano_part)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.time_nano_part-validated-by)
    - [Underlying](dxfeed.html#module-tastytrade.dxfeed.underlying)

      * [tastytrade.dxfeed.underlying.Underlying](dxfeed.html#tastytrade.dxfeed.underlying.Underlying)

        + [Fields](dxfeed.html#tastytrade.dxfeed.underlying.Underlying-fields)
        + [Validators](dxfeed.html#tastytrade.dxfeed.underlying.Underlying-validators)
        + [back\_volatility](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.back_volatility)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.back_volatility-validated-by)
        + [call\_volume](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.call_volume)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.call_volume-validated-by)
        + [front\_volatility](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.front_volatility)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.front_volatility-validated-by)
        + [index](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.index)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.index-validated-by)
        + [option\_volume](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.option_volume)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.option_volume-validated-by)
        + [put\_call\_ratio](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.put_call_ratio)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.put_call_ratio-validated-by)
        + [put\_volume](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.put_volume)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.put_volume-validated-by)
        + [sequence](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.sequence)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.sequence-validated-by)
        + [time](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.time)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.time-validated-by)
        + [volatility](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.volatility)

          - [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.volatility-validated-by)
  + [tastytrade.instruments](instruments.html)
  + [tastytrade.market\_sessions](market-sessions.html)
  + [tastytrade.metrics](metrics.html)
  + [tastytrade.order](order.html)
  + [tastytrade.search](search.html)
  + [tastytrade.session](session.html)
  + [tastytrade.streamer](streamer.html)
  + [tastytrade.utils](utils.html)
  + [tastytrade.watchlists](watchlists.html)

tastytrade.dxfeed

* [Event](dxfeed.html#module-tastytrade.dxfeed.event)

  + [tastytrade.dxfeed.event.Event](dxfeed.html#tastytrade.dxfeed.event.Event)

    - [Fields](dxfeed.html#tastytrade.dxfeed.event.Event-fields)
    - [Validators](dxfeed.html#tastytrade.dxfeed.event.Event-validators)
    - [event\_symbol](dxfeed.html#tastytrade.dxfeed.event.Event.event_symbol)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.event.Event.event_symbol-validated-by)
    - [event\_time](dxfeed.html#tastytrade.dxfeed.event.Event.event_time)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.event.Event.event_time-validated-by)
    - [Mfrom\_stream](dxfeed.html#tastytrade.dxfeed.event.Event.from_stream)

      * [Parameters](dxfeed.html#tastytrade.dxfeed.event.Event.from_stream-parameters)

        + [pdata](dxfeed.html#tastytrade.dxfeed.event.Event.from_stream.data)
      * [Returns](dxfeed.html#tastytrade.dxfeed.event.Event.from_stream-returns)
  + [tastytrade.dxfeed.event.IndexedEvent](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent)

    - [Fields](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent-fields)
    - [Validators](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent-validators)
    - [event\_flags](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.event_flags)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.event_flags-validated-by)
    - [Ppending](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.pending)
    - [Premove](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.remove)
    - [Psnapshot\_begin](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.snapshot_begin)
    - [Psnapshot\_end](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.snapshot_end)
    - [Psnapshot\_mode](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.snapshot_mode)
    - [Psnapshot\_snip](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.snapshot_snip)
* [Candle](dxfeed.html#module-tastytrade.dxfeed.candle)

  + [tastytrade.dxfeed.candle.Candle](dxfeed.html#tastytrade.dxfeed.candle.Candle)

    - [Fields](dxfeed.html#tastytrade.dxfeed.candle.Candle-fields)
    - [Validators](dxfeed.html#tastytrade.dxfeed.candle.Candle-validators)
    - [ask\_volume](dxfeed.html#tastytrade.dxfeed.candle.Candle.ask_volume)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.ask_volume-validated-by)
    - [bid\_volume](dxfeed.html#tastytrade.dxfeed.candle.Candle.bid_volume)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.bid_volume-validated-by)
    - [close](dxfeed.html#tastytrade.dxfeed.candle.Candle.close)

      * [Constraints](dxfeed.html#tastytrade.dxfeed.candle.Candle.close-constraints)
      * [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.close-validated-by)
    - [count](dxfeed.html#tastytrade.dxfeed.candle.Candle.count)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.count-validated-by)
    - [high](dxfeed.html#tastytrade.dxfeed.candle.Candle.high)

      * [Constraints](dxfeed.html#tastytrade.dxfeed.candle.Candle.high-constraints)
      * [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.high-validated-by)
    - [imp\_volatility](dxfeed.html#tastytrade.dxfeed.candle.Candle.imp_volatility)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.imp_volatility-validated-by)
    - [index](dxfeed.html#tastytrade.dxfeed.candle.Candle.index)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.index-validated-by)
    - [low](dxfeed.html#tastytrade.dxfeed.candle.Candle.low)

      * [Constraints](dxfeed.html#tastytrade.dxfeed.candle.Candle.low-constraints)
      * [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.low-validated-by)
    - [open](dxfeed.html#tastytrade.dxfeed.candle.Candle.open)

      * [Constraints](dxfeed.html#tastytrade.dxfeed.candle.Candle.open-constraints)
      * [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.open-validated-by)
    - [open\_interest](dxfeed.html#tastytrade.dxfeed.candle.Candle.open_interest)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.open_interest-validated-by)
    - [sequence](dxfeed.html#tastytrade.dxfeed.candle.Candle.sequence)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.sequence-validated-by)
    - [time](dxfeed.html#tastytrade.dxfeed.candle.Candle.time)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.time-validated-by)
    - [volume](dxfeed.html#tastytrade.dxfeed.candle.Candle.volume)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.volume-validated-by)
    - [vwap](dxfeed.html#tastytrade.dxfeed.candle.Candle.vwap)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.candle.Candle.vwap-validated-by)
* [Greeks](dxfeed.html#module-tastytrade.dxfeed.greeks)

  + [tastytrade.dxfeed.greeks.Greeks](dxfeed.html#tastytrade.dxfeed.greeks.Greeks)

    - [Fields](dxfeed.html#tastytrade.dxfeed.greeks.Greeks-fields)
    - [Validators](dxfeed.html#tastytrade.dxfeed.greeks.Greeks-validators)
    - [delta](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.delta)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.delta-validated-by)
    - [gamma](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.gamma)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.gamma-validated-by)
    - [index](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.index)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.index-validated-by)
    - [price](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.price-validated-by)
    - [rho](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.rho)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.rho-validated-by)
    - [sequence](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.sequence)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.sequence-validated-by)
    - [theta](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.theta)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.theta-validated-by)
    - [time](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.time)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.time-validated-by)
    - [vega](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.vega)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.vega-validated-by)
    - [volatility](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.volatility)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.volatility-validated-by)
* [Profile](dxfeed.html#module-tastytrade.dxfeed.profile)

  + [tastytrade.dxfeed.profile.Profile](dxfeed.html#tastytrade.dxfeed.profile.Profile)

    - [Fields](dxfeed.html#tastytrade.dxfeed.profile.Profile-fields)
    - [Validators](dxfeed.html#tastytrade.dxfeed.profile.Profile-validators)
    - [beta](dxfeed.html#tastytrade.dxfeed.profile.Profile.beta)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.beta-validated-by)
    - [description](dxfeed.html#tastytrade.dxfeed.profile.Profile.description)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.description-validated-by)
    - [dividend\_frequency](dxfeed.html#tastytrade.dxfeed.profile.Profile.dividend_frequency)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.dividend_frequency-validated-by)
    - [earnings\_per\_share](dxfeed.html#tastytrade.dxfeed.profile.Profile.earnings_per_share)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.earnings_per_share-validated-by)
    - [ex\_dividend\_amount](dxfeed.html#tastytrade.dxfeed.profile.Profile.ex_dividend_amount)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.ex_dividend_amount-validated-by)
    - [ex\_dividend\_day\_id](dxfeed.html#tastytrade.dxfeed.profile.Profile.ex_dividend_day_id)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.ex_dividend_day_id-validated-by)
    - [free\_float](dxfeed.html#tastytrade.dxfeed.profile.Profile.free_float)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.free_float-validated-by)
    - [halt\_end\_time](dxfeed.html#tastytrade.dxfeed.profile.Profile.halt_end_time)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.halt_end_time-validated-by)
    - [halt\_start\_time](dxfeed.html#tastytrade.dxfeed.profile.Profile.halt_start_time)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.halt_start_time-validated-by)
    - [high\_52\_week\_price](dxfeed.html#tastytrade.dxfeed.profile.Profile.high_52_week_price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.high_52_week_price-validated-by)
    - [high\_limit\_price](dxfeed.html#tastytrade.dxfeed.profile.Profile.high_limit_price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.high_limit_price-validated-by)
    - [low\_52\_week\_price](dxfeed.html#tastytrade.dxfeed.profile.Profile.low_52_week_price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.low_52_week_price-validated-by)
    - [low\_limit\_price](dxfeed.html#tastytrade.dxfeed.profile.Profile.low_limit_price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.low_limit_price-validated-by)
    - [shares](dxfeed.html#tastytrade.dxfeed.profile.Profile.shares)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.shares-validated-by)
    - [short\_sale\_restriction](dxfeed.html#tastytrade.dxfeed.profile.Profile.short_sale_restriction)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.short_sale_restriction-validated-by)
    - [status\_reason](dxfeed.html#tastytrade.dxfeed.profile.Profile.status_reason)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.status_reason-validated-by)
    - [trading\_status](dxfeed.html#tastytrade.dxfeed.profile.Profile.trading_status)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.profile.Profile.trading_status-validated-by)
* [Quote](dxfeed.html#module-tastytrade.dxfeed.quote)

  + [tastytrade.dxfeed.quote.Quote](dxfeed.html#tastytrade.dxfeed.quote.Quote)

    - [Fields](dxfeed.html#tastytrade.dxfeed.quote.Quote-fields)
    - [Validators](dxfeed.html#tastytrade.dxfeed.quote.Quote-validators)
    - [ask\_exchange\_code](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_exchange_code)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_exchange_code-validated-by)
    - [ask\_price](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_price-validated-by)
    - [ask\_size](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_size)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_size-validated-by)
    - [ask\_time](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_time)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_time-validated-by)
    - [bid\_exchange\_code](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_exchange_code)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_exchange_code-validated-by)
    - [bid\_price](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_price-validated-by)
    - [bid\_size](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_size)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_size-validated-by)
    - [bid\_time](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_time)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_time-validated-by)
    - [sequence](dxfeed.html#tastytrade.dxfeed.quote.Quote.sequence)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.sequence-validated-by)
    - [time\_nano\_part](dxfeed.html#tastytrade.dxfeed.quote.Quote.time_nano_part)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.quote.Quote.time_nano_part-validated-by)
* [Summary](dxfeed.html#module-tastytrade.dxfeed.summary)

  + [tastytrade.dxfeed.summary.Summary](dxfeed.html#tastytrade.dxfeed.summary.Summary)

    - [Fields](dxfeed.html#tastytrade.dxfeed.summary.Summary-fields)
    - [Validators](dxfeed.html#tastytrade.dxfeed.summary.Summary-validators)
    - [day\_close\_price](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_close_price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_close_price-validated-by)
    - [day\_close\_price\_type](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_close_price_type)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_close_price_type-validated-by)
    - [day\_high\_price](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_high_price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_high_price-validated-by)
    - [day\_id](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_id)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_id-validated-by)
    - [day\_low\_price](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_low_price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_low_price-validated-by)
    - [day\_open\_price](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_open_price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_open_price-validated-by)
    - [open\_interest](dxfeed.html#tastytrade.dxfeed.summary.Summary.open_interest)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.open_interest-validated-by)
    - [prev\_day\_close\_price](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_close_price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_close_price-validated-by)
    - [prev\_day\_close\_price\_type](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_close_price_type)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_close_price_type-validated-by)
    - [prev\_day\_id](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_id)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_id-validated-by)
    - [prev\_day\_volume](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_volume)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_volume-validated-by)
* [TimeAndSale](dxfeed.html#module-tastytrade.dxfeed.timeandsale)

  + [tastytrade.dxfeed.timeandsale.TimeAndSale](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale)

    - [Fields](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale-fields)
    - [Validators](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale-validators)
    - [aggressor\_side](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.aggressor_side)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.aggressor_side-validated-by)
    - [ask\_price](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.ask_price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.ask_price-validated-by)
    - [bid\_price](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.bid_price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.bid_price-validated-by)
    - [buyer](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.buyer)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.buyer-validated-by)
    - [exchange\_code](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_code)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_code-validated-by)
    - [exchange\_sale\_conditions](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_sale_conditions)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_sale_conditions-validated-by)
    - [extended\_trading\_hours](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.extended_trading_hours)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.extended_trading_hours-validated-by)
    - [index](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.index)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.index-validated-by)
    - [price](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.price-validated-by)
    - [seller](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.seller)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.seller-validated-by)
    - [sequence](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.sequence)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.sequence-validated-by)
    - [size](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.size)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.size-validated-by)
    - [spread\_leg](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.spread_leg)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.spread_leg-validated-by)
    - [time](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.time)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.time-validated-by)
    - [time\_nano\_part](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.time_nano_part)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.time_nano_part-validated-by)
    - [trade\_through\_exempt](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.trade_through_exempt)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.trade_through_exempt-validated-by)
    - [type](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.type)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.type-validated-by)
    - [valid\_tick](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.valid_tick)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.valid_tick-validated-by)
* [TheoPrice](dxfeed.html#module-tastytrade.dxfeed.theoprice)

  + [tastytrade.dxfeed.theoprice.TheoPrice](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice)

    - [Fields](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice-fields)
    - [Validators](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice-validators)
    - [delta](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.delta)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.delta-validated-by)
    - [dividend](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.dividend)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.dividend-validated-by)
    - [gamma](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.gamma)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.gamma-validated-by)
    - [index](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.index)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.index-validated-by)
    - [interest](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.interest)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.interest-validated-by)
    - [price](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.price-validated-by)
    - [sequence](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.sequence)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.sequence-validated-by)
    - [time](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.time)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.time-validated-by)
    - [underlying\_price](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.underlying_price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.underlying_price-validated-by)
* [Trade](dxfeed.html#module-tastytrade.dxfeed.trade)

  + [tastytrade.dxfeed.trade.Trade](dxfeed.html#tastytrade.dxfeed.trade.Trade)

    - [Fields](dxfeed.html#tastytrade.dxfeed.trade.Trade-fields)
    - [Validators](dxfeed.html#tastytrade.dxfeed.trade.Trade-validators)
    - [change](dxfeed.html#tastytrade.dxfeed.trade.Trade.change)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.change-validated-by)
    - [day\_id](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_id)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_id-validated-by)
    - [day\_turnover](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_turnover)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_turnover-validated-by)
    - [day\_volume](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_volume)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_volume-validated-by)
    - [exchange\_code](dxfeed.html#tastytrade.dxfeed.trade.Trade.exchange_code)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.exchange_code-validated-by)
    - [extended\_trading\_hours](dxfeed.html#tastytrade.dxfeed.trade.Trade.extended_trading_hours)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.extended_trading_hours-validated-by)
    - [price](dxfeed.html#tastytrade.dxfeed.trade.Trade.price)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.price-validated-by)
    - [sequence](dxfeed.html#tastytrade.dxfeed.trade.Trade.sequence)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.sequence-validated-by)
    - [size](dxfeed.html#tastytrade.dxfeed.trade.Trade.size)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.size-validated-by)
    - [tick\_direction](dxfeed.html#tastytrade.dxfeed.trade.Trade.tick_direction)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.tick_direction-validated-by)
    - [time](dxfeed.html#tastytrade.dxfeed.trade.Trade.time)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.time-validated-by)
    - [time\_nano\_part](dxfeed.html#tastytrade.dxfeed.trade.Trade.time_nano_part)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.trade.Trade.time_nano_part-validated-by)
* [Underlying](dxfeed.html#module-tastytrade.dxfeed.underlying)

  + [tastytrade.dxfeed.underlying.Underlying](dxfeed.html#tastytrade.dxfeed.underlying.Underlying)

    - [Fields](dxfeed.html#tastytrade.dxfeed.underlying.Underlying-fields)
    - [Validators](dxfeed.html#tastytrade.dxfeed.underlying.Underlying-validators)
    - [back\_volatility](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.back_volatility)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.back_volatility-validated-by)
    - [call\_volume](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.call_volume)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.call_volume-validated-by)
    - [front\_volatility](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.front_volatility)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.front_volatility-validated-by)
    - [index](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.index)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.index-validated-by)
    - [option\_volume](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.option_volume)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.option_volume-validated-by)
    - [put\_call\_ratio](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.put_call_ratio)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.put_call_ratio-validated-by)
    - [put\_volume](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.put_volume)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.put_volume-validated-by)
    - [sequence](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.sequence)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.sequence-validated-by)
    - [time](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.time)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.time-validated-by)
    - [volatility](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.volatility)

      * [Validated by](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.volatility-validated-by)

# tastytrade.dxfeed[¶](dxfeed.html#tastytrade-dxfeed "Link to this heading")

For general dxfeed symbology, go to [Formats](https://kb.dxfeed.com/en/data-model/symbology-guide/general-provisions.html#formats-60641), where you’ll find information on various kinds of formatting.

For options on futures symbology, go to [CME Group](https://cmegroup.com/) and look at the ‘Specs’ section for the given futures symbol.

If you want to double-check you typed the symbol right, or want to troubleshoot a hanging request, go to [dxfeed Symbol Lookup](https://symbol-lookup.dxfeed.com/) and type in the same symbol.

## Event[¶](dxfeed.html#module-tastytrade.dxfeed.event "Link to this heading")

*pydantic model* tastytrade.dxfeed.event.Event(*\**, *[eventSymbol](dxfeed.html#tastytrade.dxfeed.event.Event "tastytrade.dxfeed.event.Event.eventSymbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[eventTime](dxfeed.html#tastytrade.dxfeed.event.Event "tastytrade.dxfeed.event.Event.eventTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)[¶](dxfeed.html#tastytrade.dxfeed.event.Event "Link to this definition")
:   Base class for dxfeed events received from the data streamer.

    Show JSON schema

    ```
    {
       "title": "Event",
       "description": "Base class for dxfeed events received from the data streamer.",
       "type": "object",
       "properties": {
          "eventSymbol": {
             "title": "Eventsymbol",
             "type": "string"
          },
          "eventTime": {
             "title": "Eventtime",
             "type": "integer"
          }
       },
       "required": [
          "eventSymbol",
          "eventTime"
       ]
    }

    ```

    Fields:[¶](dxfeed.html#tastytrade.dxfeed.event.Event-fields "Permalink to this headline")
    :   * [`event_symbol (str)`](dxfeed.html#tastytrade.dxfeed.event.Event.event_symbol "tastytrade.dxfeed.event.Event.event_symbol (Python field) — symbol of this event")
        * [`event_time (int)`](dxfeed.html#tastytrade.dxfeed.event.Event.event_time "tastytrade.dxfeed.event.Event.event_time (Python field) — time of this event")

    Validators:[¶](dxfeed.html#tastytrade.dxfeed.event.Event-validators "Permalink to this headline")
    :   * `change_nan_to_none` » `all fields`

    *field* event\_symbol : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]* *(alias 'eventSymbol')*[¶](dxfeed.html#tastytrade.dxfeed.event.Event.event_symbol "Link to this definition")
    :   symbol of this event

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.event.Event.event_symbol-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* event\_time : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'eventTime')*[¶](dxfeed.html#tastytrade.dxfeed.event.Event.event_time "Link to this definition")
    :   time of this event

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.event.Event.event_time-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *classmethod* from\_stream(*[data](dxfeed.html#tastytrade.dxfeed.event.Event.from_stream.data "tastytrade.dxfeed.event.Event.from_stream.data (Python parameter) — list of raw quote data from streamer"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[Event](dxfeed.html#tastytrade.dxfeed.event.Event "tastytrade.dxfeed.event.Event (Python model) — Base class for dxfeed events received from the data streamer.")][¶](dxfeed.html#tastytrade.dxfeed.event.Event.from_stream "Link to this definition")
    :   Makes a list of event objects from a list of raw trade data fetched by
        a `DXFeedStreamer`.

        Parameters:[¶](dxfeed.html#tastytrade.dxfeed.event.Event.from_stream-parameters "Permalink to this headline")
        :   data: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[¶](dxfeed.html#tastytrade.dxfeed.event.Event.from_stream.data "Permalink to this definition")
            :   list of raw quote data from streamer

        Returns:[¶](dxfeed.html#tastytrade.dxfeed.event.Event.from_stream-returns "Permalink to this headline")
        :   list of event objects from data

*pydantic model* tastytrade.dxfeed.event.IndexedEvent(*\**, *[eventSymbol](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent "tastytrade.dxfeed.event.IndexedEvent.eventSymbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[eventTime](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent "tastytrade.dxfeed.event.IndexedEvent.eventTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[eventFlags](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent "tastytrade.dxfeed.event.IndexedEvent.eventFlags (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)[¶](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent "Link to this definition")
:   A dxfeed IndexedEvent with flags computed bitwise.
    For info see [here](https://docs.dxfeed.com/dxfeed/api/com/dxfeed/event/IndexedEvent.html).

    Show JSON schema

    ```
    {
       "title": "IndexedEvent",
       "description": "A dxfeed `IndexedEvent` with flags computed bitwise.\nFor info see `here <https://docs.dxfeed.com/dxfeed/api/com/dxfeed/event/IndexedEvent.html>`_.",
       "type": "object",
       "properties": {
          "eventSymbol": {
             "title": "Eventsymbol",
             "type": "string"
          },
          "eventTime": {
             "title": "Eventtime",
             "type": "integer"
          },
          "eventFlags": {
             "title": "Eventflags",
             "type": "integer"
          }
       },
       "required": [
          "eventSymbol",
          "eventTime",
          "eventFlags"
       ]
    }

    ```

    Fields:[¶](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent-fields "Permalink to this headline")
    :   * [`event_flags (int)`](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.event_flags "tastytrade.dxfeed.event.IndexedEvent.event_flags (Python field) — flags for the event")

    Validators:[¶](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent-validators "Permalink to this headline")

    *field* event\_flags : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'eventFlags')*[¶](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.event_flags "Link to this definition")
    :   flags for the event

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.event_flags-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *property* pending : [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[¶](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.pending "Link to this definition")
    :   TX\_PENDING is an indicator of pending transactional update.
        When txPending is true it means, that an ongoing transaction update that spans
        multiple events is in process. All events with txPending true shall be put into
        a separate pending list for each source id and should be processed later when
        an event for this source id with txPending false comes.

    *property* remove : [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[¶](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.remove "Link to this definition")
    :   REMOVE\_EVENT is used to indicate that that the event with the corresponding
        index has to be removed.

    *property* snapshot\_begin : [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[¶](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.snapshot_begin "Link to this definition")
    :   SNAPSHOT\_BEGIN is used to indicate when the loading of a snapshot starts.
        Snapshot load starts on new subscription and the first indexed event that
        arrives for each non-zero source id on new subscription may have snapshotBegin
        set to true. It means, that an ongoing snapshot consisting of multiple events is
        incoming. All events for this source id shall be put into a separate pending
        list for each source id.

    *property* snapshot\_end : [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[¶](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.snapshot_end "Link to this definition")
    :   SNAPSHOT\_END or SNAPSHOT\_SNIP are used to indicate the end of a snapshot.
        The last event of a snapshot is marked with either snapshotEnd or snapshotSnip.
        At this time, all events from a pending list for the corresponding source can be
        processed, unless txPending is also set to true. In the later case, the
        processing shall be further delayed due to ongoing transaction.

        The difference between snapshotEnd and snapshotSnip is the following:
        snapshotEnd indicates that the data source had sent all the data pertaining to
        the subscription for the corresponding indexed event, while snapshotSnip
        indicates that some limit on the amount of data was reached and while there
        still might be more data available, it will not be provided.

    *property* snapshot\_mode : [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[¶](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.snapshot_mode "Link to this definition")
    :   SNAPSHOT\_MODE is used to instruct dxFeed to use snapshot mode. It is intended to
        be used only for publishing to activate (if not yet activated) snapshot mode.
        The difference from SNAPSHOT\_BEGIN flag is that SNAPSHOT\_MODE only switches on
        snapshot mode without starting snapshot synchronization protocol.
        When a snapshot is empty or consists of a single event, then the event can have
        both snapshotBegin and snapshotEnd or snapshotSnip flags. In case of an empty
        snapshot, removeEvent on this event is also set to true.

    *property* snapshot\_snip : [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[¶](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent.snapshot_snip "Link to this definition")
    :   SNAPSHOT\_END or SNAPSHOT\_SNIP are used to indicate the end of a snapshot.
        The last event of a snapshot is marked with either snapshotEnd or snapshotSnip.
        At this time, all events from a pending list for the corresponding source can be
        processed, unless txPending is also set to true. In the later case, the
        processing shall be further delayed due to ongoing transaction.

        The difference between snapshotEnd and snapshotSnip is the following:
        snapshotEnd indicates that the data source had sent all the data pertaining to
        the subscription for the corresponding indexed event, while snapshotSnip
        indicates that some limit on the amount of data was reached and while there
        still might be more data available, it will not be provided.

## Candle[¶](dxfeed.html#module-tastytrade.dxfeed.candle "Link to this heading")

*pydantic model* tastytrade.dxfeed.candle.Candle(*\**, *[eventSymbol](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.eventSymbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[eventTime](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.eventTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[eventFlags](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.eventFlags (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[index](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.index (Python parameter) — unique per-symbol index of this candle event"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[time](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.time (Python parameter) — timestamp of the candle in milliseconds"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[sequence](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.sequence (Python parameter) — sequence number of this event"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[count](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.count (Python parameter) — total number of events in the candle"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[volume](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.volume (Python parameter) — the total volume of the candle"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[vwap](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.vwap (Python parameter) — volume-weighted average price"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[bidVolume](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.bidVolume (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[askVolume](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.askVolume (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[impVolatility](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.impVolatility (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[openInterest](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.openInterest (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[open](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.open (Python parameter) — the first (open) price of the candle"): [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "(in Python v3.13)")[[Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)"), WrapValidator(func=zero\_from\_none, json\_schema\_input\_type=PydanticUndefined)]*, *[high](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.high (Python parameter) — the maximal (high) price of the candle"): [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "(in Python v3.13)")[[Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)"), WrapValidator(func=zero\_from\_none, json\_schema\_input\_type=PydanticUndefined)]*, *[low](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.low (Python parameter) — the minimal (low) price of the candle"): [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "(in Python v3.13)")[[Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)"), WrapValidator(func=zero\_from\_none, json\_schema\_input\_type=PydanticUndefined)]*, *[close](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.close (Python parameter) — the last (close) price of the candle"): [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "(in Python v3.13)")[[Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)"), WrapValidator(func=zero\_from\_none, json\_schema\_input\_type=PydanticUndefined)]*)[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle "Link to this definition")
:   Bases: [`IndexedEvent`](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent "tastytrade.dxfeed.event.IndexedEvent (Python model) — A dxfeed IndexedEvent with flags computed bitwise. For info see here.")

    A Candle event with open, high, low, close prices and other information
    for a specific period. Candles are build with a specified period using a
    specified price type with data taken from a specified exchange.

    Show JSON schema

    ```
    {
       "title": "Candle",
       "description": "A Candle event with open, high, low, close prices and other information\nfor a specific period. Candles are build with a specified period using a\nspecified price type with data taken from a specified exchange.",
       "type": "object",
       "properties": {
          "eventSymbol": {
             "title": "Eventsymbol",
             "type": "string"
          },
          "eventTime": {
             "title": "Eventtime",
             "type": "integer"
          },
          "eventFlags": {
             "title": "Eventflags",
             "type": "integer"
          },
          "index": {
             "title": "Index",
             "type": "integer"
          },
          "time": {
             "title": "Time",
             "type": "integer"
          },
          "sequence": {
             "title": "Sequence",
             "type": "integer"
          },
          "count": {
             "title": "Count",
             "type": "integer"
          },
          "volume": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Volume"
          },
          "vwap": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Vwap"
          },
          "bidVolume": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Bidvolume"
          },
          "askVolume": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Askvolume"
          },
          "impVolatility": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Impvolatility"
          },
          "openInterest": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Openinterest"
          },
          "open": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Open"
          },
          "high": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "High"
          },
          "low": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Low"
          },
          "close": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Close"
          }
       },
       "required": [
          "eventSymbol",
          "eventTime",
          "eventFlags",
          "index",
          "time",
          "sequence",
          "count",
          "open",
          "high",
          "low",
          "close"
       ]
    }

    ```

    Fields:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle-fields "Permalink to this headline")
    :   * [`ask_volume (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.candle.Candle.ask_volume "tastytrade.dxfeed.candle.Candle.ask_volume (Python field) — ask volume in the candle")
        * [`bid_volume (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.candle.Candle.bid_volume "tastytrade.dxfeed.candle.Candle.bid_volume (Python field) — bid volume in the candle")
        * [`close (Annotated[decimal.Decimal, pydantic.functional_validators.WrapValidator(func=tastytrade.dxfeed.candle.zero_from_none, json_schema_input_type=PydanticUndefined)])`](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.close (Python parameter) — the last (close) price of the candle")
        * [`count (int)`](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.count (Python parameter) — total number of events in the candle")
        * [`high (Annotated[decimal.Decimal, pydantic.functional_validators.WrapValidator(func=tastytrade.dxfeed.candle.zero_from_none, json_schema_input_type=PydanticUndefined)])`](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.high (Python parameter) — the maximal (high) price of the candle")
        * [`imp_volatility (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.candle.Candle.imp_volatility "tastytrade.dxfeed.candle.Candle.imp_volatility (Python field) — implied volatility in the candle")
        * [`index (int)`](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.index (Python parameter) — unique per-symbol index of this candle event")
        * [`low (Annotated[decimal.Decimal, pydantic.functional_validators.WrapValidator(func=tastytrade.dxfeed.candle.zero_from_none, json_schema_input_type=PydanticUndefined)])`](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.low (Python parameter) — the minimal (low) price of the candle")
        * [`open (Annotated[decimal.Decimal, pydantic.functional_validators.WrapValidator(func=tastytrade.dxfeed.candle.zero_from_none, json_schema_input_type=PydanticUndefined)])`](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.open (Python parameter) — the first (open) price of the candle")
        * [`open_interest (int | None)`](dxfeed.html#tastytrade.dxfeed.candle.Candle.open_interest "tastytrade.dxfeed.candle.Candle.open_interest (Python field) — open interest in the candle")
        * [`sequence (int)`](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.sequence (Python parameter) — sequence number of this event")
        * [`time (int)`](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.time (Python parameter) — timestamp of the candle in milliseconds")
        * [`volume (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.volume (Python parameter) — the total volume of the candle")
        * [`vwap (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.candle.Candle "tastytrade.dxfeed.candle.Candle.vwap (Python parameter) — volume-weighted average price")

    Validators:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle-validators "Permalink to this headline")

    *field* ask\_volume : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'askVolume')*[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.ask_volume "Link to this definition")
    :   ask volume in the candle

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.ask_volume-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* bid\_volume : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'bidVolume')*[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.bid_volume "Link to this definition")
    :   bid volume in the candle

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.bid_volume-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* close : [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "(in Python v3.13)")[[Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)"), WrapValidator(func=zero\_from\_none, json\_schema\_input\_type=PydanticUndefined)] *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.close "Link to this definition")
    :   the last (close) price of the candle

        Constraints:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.close-constraints "Permalink to this headline")
        :   * **func** = <function zero\_from\_none at 0x7e801629d5e0>
            * **json\_schema\_input\_type** = PydanticUndefined

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.close-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* count : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.count "Link to this definition")
    :   total number of events in the candle

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.count-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* high : [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "(in Python v3.13)")[[Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)"), WrapValidator(func=zero\_from\_none, json\_schema\_input\_type=PydanticUndefined)] *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.high "Link to this definition")
    :   the maximal (high) price of the candle

        Constraints:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.high-constraints "Permalink to this headline")
        :   * **func** = <function zero\_from\_none at 0x7e801629d5e0>
            * **json\_schema\_input\_type** = PydanticUndefined

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.high-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* imp\_volatility : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'impVolatility')*[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.imp_volatility "Link to this definition")
    :   implied volatility in the candle

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.imp_volatility-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* index : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.index "Link to this definition")
    :   unique per-symbol index of this candle event

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.index-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* low : [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "(in Python v3.13)")[[Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)"), WrapValidator(func=zero\_from\_none, json\_schema\_input\_type=PydanticUndefined)] *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.low "Link to this definition")
    :   the minimal (low) price of the candle

        Constraints:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.low-constraints "Permalink to this headline")
        :   * **func** = <function zero\_from\_none at 0x7e801629d5e0>
            * **json\_schema\_input\_type** = PydanticUndefined

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.low-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* open : [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "(in Python v3.13)")[[Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)"), WrapValidator(func=zero\_from\_none, json\_schema\_input\_type=PydanticUndefined)] *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.open "Link to this definition")
    :   the first (open) price of the candle

        Constraints:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.open-constraints "Permalink to this headline")
        :   * **func** = <function zero\_from\_none at 0x7e801629d5e0>
            * **json\_schema\_input\_type** = PydanticUndefined

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.open-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* open\_interest : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'openInterest')*[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.open_interest "Link to this definition")
    :   open interest in the candle

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.open_interest-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* sequence : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.sequence "Link to this definition")
    :   sequence number of this event

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.sequence-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* time : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.time "Link to this definition")
    :   timestamp of the candle in milliseconds

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.time-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* volume : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.volume "Link to this definition")
    :   the total volume of the candle

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.volume-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* vwap : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.vwap "Link to this definition")
    :   volume-weighted average price

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.candle.Candle.vwap-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

## Greeks[¶](dxfeed.html#module-tastytrade.dxfeed.greeks "Link to this heading")

*pydantic model* tastytrade.dxfeed.greeks.Greeks(*\**, *[eventSymbol](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.eventSymbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[eventTime](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.eventTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[eventFlags](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.eventFlags (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[index](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.index (Python parameter) — unique per-symbol index of this event"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[time](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.time (Python parameter) — timestamp of this event in milliseconds"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[sequence](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.sequence (Python parameter) — sequence number to distinguish events that have the same time"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[price](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.price (Python parameter) — option market price"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[volatility](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.volatility (Python parameter) — Black-Scholes implied volatility of the option"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[delta](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.delta (Python parameter) — option delta"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[gamma](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.gamma (Python parameter) — option gamma"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[theta](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.theta (Python parameter) — option theta"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[rho](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.rho (Python parameter) — option rho"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[vega](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.vega (Python parameter) — option vega"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*)[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "Link to this definition")
:   Bases: [`IndexedEvent`](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent "tastytrade.dxfeed.event.IndexedEvent (Python model) — A dxfeed IndexedEvent with flags computed bitwise. For info see here.")

    Greek ratios, or simply Greeks, are differential values that show how the
    price of an option depends on other market parameters: on the price of the
    underlying asset, its volatility, etc. Greeks are used to assess the risks
    of customer portfolios. Greeks are derivatives of the value of securities
    in different axes. If a derivative is very far from zero, then the
    portfolio has a risky sensitivity in this parameter.

    Show JSON schema

    ```
    {
       "title": "Greeks",
       "description": "Greek ratios, or simply Greeks, are differential values that show how the\nprice of an option depends on other market parameters: on the price of the\nunderlying asset, its volatility, etc. Greeks are used to assess the risks\nof customer portfolios. Greeks are derivatives of the value of securities\nin different axes. If a derivative is very far from zero, then the\nportfolio has a risky sensitivity in this parameter.",
       "type": "object",
       "properties": {
          "eventSymbol": {
             "title": "Eventsymbol",
             "type": "string"
          },
          "eventTime": {
             "title": "Eventtime",
             "type": "integer"
          },
          "eventFlags": {
             "title": "Eventflags",
             "type": "integer"
          },
          "index": {
             "title": "Index",
             "type": "integer"
          },
          "time": {
             "title": "Time",
             "type": "integer"
          },
          "sequence": {
             "title": "Sequence",
             "type": "integer"
          },
          "price": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Price"
          },
          "volatility": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Volatility"
          },
          "delta": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Delta"
          },
          "gamma": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Gamma"
          },
          "theta": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Theta"
          },
          "rho": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Rho"
          },
          "vega": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Vega"
          }
       },
       "required": [
          "eventSymbol",
          "eventTime",
          "eventFlags",
          "index",
          "time",
          "sequence",
          "price",
          "volatility",
          "delta",
          "gamma",
          "theta",
          "rho",
          "vega"
       ]
    }

    ```

    Fields:[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks-fields "Permalink to this headline")
    :   * [`delta (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.delta (Python parameter) — option delta")
        * [`gamma (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.gamma (Python parameter) — option gamma")
        * [`index (int)`](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.index (Python parameter) — unique per-symbol index of this event")
        * [`price (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.price (Python parameter) — option market price")
        * [`rho (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.rho (Python parameter) — option rho")
        * [`sequence (int)`](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.sequence (Python parameter) — sequence number to distinguish events that have the same time")
        * [`theta (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.theta (Python parameter) — option theta")
        * [`time (int)`](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.time (Python parameter) — timestamp of this event in milliseconds")
        * [`vega (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.vega (Python parameter) — option vega")
        * [`volatility (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.greeks.Greeks "tastytrade.dxfeed.greeks.Greeks.volatility (Python parameter) — Black-Scholes implied volatility of the option")

    Validators:[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks-validators "Permalink to this headline")

    *field* delta : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.delta "Link to this definition")
    :   option delta

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.delta-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* gamma : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.gamma "Link to this definition")
    :   option gamma

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.gamma-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* index : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.index "Link to this definition")
    :   unique per-symbol index of this event

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.index-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.price "Link to this definition")
    :   option market price

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* rho : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.rho "Link to this definition")
    :   option rho

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.rho-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* sequence : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.sequence "Link to this definition")
    :   sequence number to distinguish events that have the same time

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.sequence-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* theta : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.theta "Link to this definition")
    :   option theta

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.theta-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* time : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.time "Link to this definition")
    :   timestamp of this event in milliseconds

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.time-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* vega : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.vega "Link to this definition")
    :   option vega

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.vega-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* volatility : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.volatility "Link to this definition")
    :   Black-Scholes implied volatility of the option

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.greeks.Greeks.volatility-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

## Profile[¶](dxfeed.html#module-tastytrade.dxfeed.profile "Link to this heading")

*pydantic model* tastytrade.dxfeed.profile.Profile(*\**, *[eventSymbol](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.eventSymbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[eventTime](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.eventTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[description](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.description (Python parameter) — description of the security instrument"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[shortSaleRestriction](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.shortSaleRestriction (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[tradingStatus](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.tradingStatus (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[haltStartTime](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.haltStartTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[haltEndTime](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.haltEndTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[exDividendDayId](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.exDividendDayId (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[statusReason](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.statusReason (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[high52WeekPrice](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.high52WeekPrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[low52WeekPrice](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.low52WeekPrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[beta](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.beta (Python parameter) — the correlation coefficient of the instrument to the S&P500 index"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[shares](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.shares (Python parameter) — shares outstanding"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[highLimitPrice](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.highLimitPrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[lowLimitPrice](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.lowLimitPrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[earningsPerShare](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.earningsPerShare (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[exDividendAmount](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.exDividendAmount (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[dividendFrequency](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.dividendFrequency (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[freeFloat](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.freeFloat (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile "Link to this definition")
:   Bases: [`Event`](dxfeed.html#tastytrade.dxfeed.event.Event "tastytrade.dxfeed.event.Event (Python model) — Base class for dxfeed events received from the data streamer.")

    A Profile event provides the security instrument description. It
    represents the most recent information that is available about the
    traded security on the market at any given moment of time.

    Show JSON schema

    ```
    {
       "title": "Profile",
       "description": "A Profile event provides the security instrument description. It\nrepresents the most recent information that is available about the\ntraded security on the market at any given moment of time.",
       "type": "object",
       "properties": {
          "eventSymbol": {
             "title": "Eventsymbol",
             "type": "string"
          },
          "eventTime": {
             "title": "Eventtime",
             "type": "integer"
          },
          "description": {
             "title": "Description",
             "type": "string"
          },
          "shortSaleRestriction": {
             "title": "Shortsalerestriction",
             "type": "string"
          },
          "tradingStatus": {
             "title": "Tradingstatus",
             "type": "string"
          },
          "haltStartTime": {
             "title": "Haltstarttime",
             "type": "integer"
          },
          "haltEndTime": {
             "title": "Haltendtime",
             "type": "integer"
          },
          "exDividendDayId": {
             "title": "Exdividenddayid",
             "type": "integer"
          },
          "statusReason": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Statusreason"
          },
          "high52WeekPrice": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "High52Weekprice"
          },
          "low52WeekPrice": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Low52Weekprice"
          },
          "beta": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Beta"
          },
          "shares": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Shares"
          },
          "highLimitPrice": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Highlimitprice"
          },
          "lowLimitPrice": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Lowlimitprice"
          },
          "earningsPerShare": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Earningspershare"
          },
          "exDividendAmount": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Exdividendamount"
          },
          "dividendFrequency": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Dividendfrequency"
          },
          "freeFloat": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Freefloat"
          }
       },
       "required": [
          "eventSymbol",
          "eventTime",
          "description",
          "shortSaleRestriction",
          "tradingStatus",
          "haltStartTime",
          "haltEndTime",
          "exDividendDayId"
       ]
    }

    ```

    Fields:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile-fields "Permalink to this headline")
    :   * [`beta (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.beta (Python parameter) — the correlation coefficient of the instrument to the S&P500 index")
        * [`description (str)`](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.description (Python parameter) — description of the security instrument")
        * [`dividend_frequency (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.profile.Profile.dividend_frequency "tastytrade.dxfeed.profile.Profile.dividend_frequency (Python field) — frequency of cash dividends payments per year (calculated)")
        * [`earnings_per_share (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.profile.Profile.earnings_per_share "tastytrade.dxfeed.profile.Profile.earnings_per_share (Python field) — earnings per share")
        * [`ex_dividend_amount (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.profile.Profile.ex_dividend_amount "tastytrade.dxfeed.profile.Profile.ex_dividend_amount (Python field) — the amount of the last paid dividend")
        * [`ex_dividend_day_id (int)`](dxfeed.html#tastytrade.dxfeed.profile.Profile.ex_dividend_day_id "tastytrade.dxfeed.profile.Profile.ex_dividend_day_id (Python field) — identifier of the ex-dividend date")
        * [`free_float (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.profile.Profile.free_float "tastytrade.dxfeed.profile.Profile.free_float (Python field) — the number of shares that are available to the public for trade")
        * [`halt_end_time (int)`](dxfeed.html#tastytrade.dxfeed.profile.Profile.halt_end_time "tastytrade.dxfeed.profile.Profile.halt_end_time (Python field) — ending time of the trading halt interval")
        * [`halt_start_time (int)`](dxfeed.html#tastytrade.dxfeed.profile.Profile.halt_start_time "tastytrade.dxfeed.profile.Profile.halt_start_time (Python field) — starting time of the trading halt interval")
        * [`high_52_week_price (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.profile.Profile.high_52_week_price "tastytrade.dxfeed.profile.Profile.high_52_week_price (Python field) — maximal (high) price in last 52 weeks")
        * [`high_limit_price (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.profile.Profile.high_limit_price "tastytrade.dxfeed.profile.Profile.high_limit_price (Python field) — maximal (high) allowed price")
        * [`low_52_week_price (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.profile.Profile.low_52_week_price "tastytrade.dxfeed.profile.Profile.low_52_week_price (Python field) — minimal (low) price in last 52 weeks")
        * [`low_limit_price (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.profile.Profile.low_limit_price "tastytrade.dxfeed.profile.Profile.low_limit_price (Python field) — minimal (low) allowed price")
        * [`shares (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.profile.Profile "tastytrade.dxfeed.profile.Profile.shares (Python parameter) — shares outstanding")
        * [`short_sale_restriction (str)`](dxfeed.html#tastytrade.dxfeed.profile.Profile.short_sale_restriction "tastytrade.dxfeed.profile.Profile.short_sale_restriction (Python field) — short sale restriction of the security instrument possible values are ACTIVE | INACTIVE | UNDEFINED")
        * [`status_reason (str | None)`](dxfeed.html#tastytrade.dxfeed.profile.Profile.status_reason "tastytrade.dxfeed.profile.Profile.status_reason (Python field) — description of the reason that trading was halted")
        * [`trading_status (str)`](dxfeed.html#tastytrade.dxfeed.profile.Profile.trading_status "tastytrade.dxfeed.profile.Profile.trading_status (Python field) — trading status of the security instrument possible values are ACTIVE | HALTED | UNDEFINED")

    Validators:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile-validators "Permalink to this headline")

    *field* beta : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.beta "Link to this definition")
    :   the correlation coefficient of the instrument to the S&P500 index

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.beta-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* description : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.description "Link to this definition")
    :   description of the security instrument

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.description-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* dividend\_frequency : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'dividendFrequency')*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.dividend_frequency "Link to this definition")
    :   frequency of cash dividends payments per year (calculated)

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.dividend_frequency-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* earnings\_per\_share : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'earningsPerShare')*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.earnings_per_share "Link to this definition")
    :   earnings per share

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.earnings_per_share-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* ex\_dividend\_amount : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'exDividendAmount')*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.ex_dividend_amount "Link to this definition")
    :   the amount of the last paid dividend

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.ex_dividend_amount-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* ex\_dividend\_day\_id : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'exDividendDayId')*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.ex_dividend_day_id "Link to this definition")
    :   identifier of the ex-dividend date

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.ex_dividend_day_id-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* free\_float : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'freeFloat')*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.free_float "Link to this definition")
    :   the number of shares that are available to the public for trade

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.free_float-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* halt\_end\_time : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'haltEndTime')*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.halt_end_time "Link to this definition")
    :   ending time of the trading halt interval

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.halt_end_time-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* halt\_start\_time : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'haltStartTime')*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.halt_start_time "Link to this definition")
    :   starting time of the trading halt interval

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.halt_start_time-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* high\_52\_week\_price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'high52WeekPrice')*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.high_52_week_price "Link to this definition")
    :   maximal (high) price in last 52 weeks

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.high_52_week_price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* high\_limit\_price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'highLimitPrice')*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.high_limit_price "Link to this definition")
    :   maximal (high) allowed price

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.high_limit_price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* low\_52\_week\_price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'low52WeekPrice')*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.low_52_week_price "Link to this definition")
    :   minimal (low) price in last 52 weeks

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.low_52_week_price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* low\_limit\_price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'lowLimitPrice')*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.low_limit_price "Link to this definition")
    :   minimal (low) allowed price

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.low_limit_price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* shares : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.shares "Link to this definition")
    :   shares outstanding

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.shares-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* short\_sale\_restriction : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]* *(alias 'shortSaleRestriction')*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.short_sale_restriction "Link to this definition")
    :   short sale restriction of the security instrument
        possible values are ACTIVE | INACTIVE | UNDEFINED

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.short_sale_restriction-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* status\_reason : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'statusReason')*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.status_reason "Link to this definition")
    :   description of the reason that trading was halted

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.status_reason-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* trading\_status : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]* *(alias 'tradingStatus')*[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.trading_status "Link to this definition")
    :   trading status of the security instrument
        possible values are ACTIVE | HALTED | UNDEFINED

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.profile.Profile.trading_status-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

## Quote[¶](dxfeed.html#module-tastytrade.dxfeed.quote "Link to this heading")

*pydantic model* tastytrade.dxfeed.quote.Quote(*\**, *[eventSymbol](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote.eventSymbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[eventTime](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote.eventTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[sequence](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote.sequence (Python parameter) — sequence of this quote"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[timeNanoPart](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote.timeNanoPart (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[bidTime](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote.bidTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[bidExchangeCode](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote.bidExchangeCode (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[askTime](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote.askTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[askExchangeCode](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote.askExchangeCode (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[bidPrice](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote.bidPrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[askPrice](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote.askPrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[bidSize](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote.bidSize (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[askSize](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote.askSize (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote "Link to this definition")
:   Bases: [`Event`](dxfeed.html#tastytrade.dxfeed.event.Event "tastytrade.dxfeed.event.Event (Python model) — Base class for dxfeed events received from the data streamer.")

    A Quote event is a snapshot of the best bid and ask prices, and other
    fields that change with each quote.

    Show JSON schema

    ```
    {
       "title": "Quote",
       "description": "A Quote event is a snapshot of the best bid and ask prices, and other\nfields that change with each quote.",
       "type": "object",
       "properties": {
          "eventSymbol": {
             "title": "Eventsymbol",
             "type": "string"
          },
          "eventTime": {
             "title": "Eventtime",
             "type": "integer"
          },
          "sequence": {
             "title": "Sequence",
             "type": "integer"
          },
          "timeNanoPart": {
             "title": "Timenanopart",
             "type": "integer"
          },
          "bidTime": {
             "title": "Bidtime",
             "type": "integer"
          },
          "bidExchangeCode": {
             "title": "Bidexchangecode",
             "type": "string"
          },
          "askTime": {
             "title": "Asktime",
             "type": "integer"
          },
          "askExchangeCode": {
             "title": "Askexchangecode",
             "type": "string"
          },
          "bidPrice": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Bidprice"
          },
          "askPrice": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Askprice"
          },
          "bidSize": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Bidsize"
          },
          "askSize": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Asksize"
          }
       },
       "required": [
          "eventSymbol",
          "eventTime",
          "sequence",
          "timeNanoPart",
          "bidTime",
          "bidExchangeCode",
          "askTime",
          "askExchangeCode",
          "bidPrice",
          "askPrice"
       ]
    }

    ```

    Fields:[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote-fields "Permalink to this headline")
    :   * [`ask_exchange_code (str)`](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_exchange_code "tastytrade.dxfeed.quote.Quote.ask_exchange_code (Python field) — ask exchange code")
        * [`ask_price (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_price "tastytrade.dxfeed.quote.Quote.ask_price (Python field) — ask price")
        * [`ask_size (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_size "tastytrade.dxfeed.quote.Quote.ask_size (Python field) — ask size as integer number (rounded toward zero) or decimal for cryptocurrencies")
        * [`ask_time (int)`](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_time "tastytrade.dxfeed.quote.Quote.ask_time (Python field) — time of the last ask change")
        * [`bid_exchange_code (str)`](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_exchange_code "tastytrade.dxfeed.quote.Quote.bid_exchange_code (Python field) — bid exchange code")
        * [`bid_price (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_price "tastytrade.dxfeed.quote.Quote.bid_price (Python field) — bid price")
        * [`bid_size (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_size "tastytrade.dxfeed.quote.Quote.bid_size (Python field) — bid size as integer number (rounded toward zero) or decimal for cryptocurrencies")
        * [`bid_time (int)`](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_time "tastytrade.dxfeed.quote.Quote.bid_time (Python field) — time of the last bid change")
        * [`sequence (int)`](dxfeed.html#tastytrade.dxfeed.quote.Quote "tastytrade.dxfeed.quote.Quote.sequence (Python parameter) — sequence of this quote")
        * [`time_nano_part (int)`](dxfeed.html#tastytrade.dxfeed.quote.Quote.time_nano_part "tastytrade.dxfeed.quote.Quote.time_nano_part (Python field) — microseconds and nanoseconds part of time of the last bid or ask change")

    Validators:[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote-validators "Permalink to this headline")

    *field* ask\_exchange\_code : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]* *(alias 'askExchangeCode')*[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_exchange_code "Link to this definition")
    :   ask exchange code

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_exchange_code-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* ask\_price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]* *(alias 'askPrice')*[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_price "Link to this definition")
    :   ask price

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* ask\_size : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'askSize')*[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_size "Link to this definition")
    :   ask size as integer number (rounded toward zero)
        or decimal for cryptocurrencies

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_size-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* ask\_time : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'askTime')*[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_time "Link to this definition")
    :   time of the last ask change

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.ask_time-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* bid\_exchange\_code : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]* *(alias 'bidExchangeCode')*[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_exchange_code "Link to this definition")
    :   bid exchange code

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_exchange_code-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* bid\_price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]* *(alias 'bidPrice')*[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_price "Link to this definition")
    :   bid price

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* bid\_size : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'bidSize')*[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_size "Link to this definition")
    :   bid size as integer number (rounded toward zero)
        or decimal for cryptocurrencies

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_size-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* bid\_time : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'bidTime')*[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_time "Link to this definition")
    :   time of the last bid change

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.bid_time-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* sequence : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.sequence "Link to this definition")
    :   sequence of this quote

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.sequence-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* time\_nano\_part : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'timeNanoPart')*[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.time_nano_part "Link to this definition")
    :   microseconds and nanoseconds part of time of the last bid or ask change

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.quote.Quote.time_nano_part-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

## Summary[¶](dxfeed.html#module-tastytrade.dxfeed.summary "Link to this heading")

*pydantic model* tastytrade.dxfeed.summary.Summary(*\**, *[eventSymbol](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary.eventSymbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[eventTime](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary.eventTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[dayId](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary.dayId (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[dayClosePriceType](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary.dayClosePriceType (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[prevDayId](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary.prevDayId (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[prevDayClosePriceType](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary.prevDayClosePriceType (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[openInterest](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary.openInterest (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[dayOpenPrice](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary.dayOpenPrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[dayHighPrice](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary.dayHighPrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[dayLowPrice](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary.dayLowPrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[dayClosePrice](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary.dayClosePrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[prevDayClosePrice](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary.prevDayClosePrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[prevDayVolume](dxfeed.html#tastytrade.dxfeed.summary.Summary "tastytrade.dxfeed.summary.Summary.prevDayVolume (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary "Link to this definition")
:   Bases: [`Event`](dxfeed.html#tastytrade.dxfeed.event.Event "tastytrade.dxfeed.event.Event (Python model) — Base class for dxfeed events received from the data streamer.")

    Summary is an information snapshot about the trading session including
    session highs, lows, etc. This record has two goals: Transmit OHLC
    values, and provide data for charting. OHLC is required for a daily chart,
    and if an exchange does not provide it, the charting services refer to the
    Summary event.

    Before opening the bidding, the values are reset to N/A or NaN.

    Show JSON schema

    ```
    {
       "title": "Summary",
       "description": "Summary is an information snapshot about the trading session including\nsession highs, lows, etc. This record has two goals: Transmit OHLC\nvalues, and provide data for charting. OHLC is required for a daily chart,\nand if an exchange does not provide it, the charting services refer to the\nSummary event.\n\nBefore opening the bidding, the values are reset to N/A or NaN.",
       "type": "object",
       "properties": {
          "eventSymbol": {
             "title": "Eventsymbol",
             "type": "string"
          },
          "eventTime": {
             "title": "Eventtime",
             "type": "integer"
          },
          "dayId": {
             "title": "Dayid",
             "type": "integer"
          },
          "dayClosePriceType": {
             "title": "Dayclosepricetype",
             "type": "string"
          },
          "prevDayId": {
             "title": "Prevdayid",
             "type": "integer"
          },
          "prevDayClosePriceType": {
             "title": "Prevdayclosepricetype",
             "type": "string"
          },
          "openInterest": {
             "title": "Openinterest",
             "type": "integer"
          },
          "dayOpenPrice": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Dayopenprice"
          },
          "dayHighPrice": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Dayhighprice"
          },
          "dayLowPrice": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Daylowprice"
          },
          "dayClosePrice": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Daycloseprice"
          },
          "prevDayClosePrice": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Prevdaycloseprice"
          },
          "prevDayVolume": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Prevdayvolume"
          }
       },
       "required": [
          "eventSymbol",
          "eventTime",
          "dayId",
          "dayClosePriceType",
          "prevDayId",
          "prevDayClosePriceType",
          "openInterest"
       ]
    }

    ```

    Fields:[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary-fields "Permalink to this headline")
    :   * [`day_close_price (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_close_price "tastytrade.dxfeed.summary.Summary.day_close_price (Python field) — the last (close) price for the day")
        * [`day_close_price_type (str)`](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_close_price_type "tastytrade.dxfeed.summary.Summary.day_close_price_type (Python field) — the price type of the last (close) price for the day possible values are FINAL | INDICATIVE | PRELIMINARY | REGULAR")
        * [`day_high_price (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_high_price "tastytrade.dxfeed.summary.Summary.day_high_price (Python field) — the maximal (high) price for the day")
        * [`day_id (int)`](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_id "tastytrade.dxfeed.summary.Summary.day_id (Python field) — identifier of the day that this summary represents")
        * [`day_low_price (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_low_price "tastytrade.dxfeed.summary.Summary.day_low_price (Python field) — the minimal (low) price for the day")
        * [`day_open_price (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_open_price "tastytrade.dxfeed.summary.Summary.day_open_price (Python field) — the first (open) price for the day")
        * [`open_interest (int)`](dxfeed.html#tastytrade.dxfeed.summary.Summary.open_interest "tastytrade.dxfeed.summary.Summary.open_interest (Python field) — open interest of the symbol as the number of open contracts")
        * [`prev_day_close_price (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_close_price "tastytrade.dxfeed.summary.Summary.prev_day_close_price (Python field) — the last (close) price for the previous day")
        * [`prev_day_close_price_type (str)`](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_close_price_type "tastytrade.dxfeed.summary.Summary.prev_day_close_price_type (Python field) — the price type of the last (close) price for the previous day possible values are FINAL | INDICATIVE | PRELIMINARY | REGULAR")
        * [`prev_day_id (int)`](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_id "tastytrade.dxfeed.summary.Summary.prev_day_id (Python field) — identifier of the previous day that this summary represents")
        * [`prev_day_volume (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_volume "tastytrade.dxfeed.summary.Summary.prev_day_volume (Python field) — total volume traded for the previous day")

    Validators:[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary-validators "Permalink to this headline")

    *field* day\_close\_price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'dayClosePrice')*[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_close_price "Link to this definition")
    :   the last (close) price for the day

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_close_price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* day\_close\_price\_type : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]* *(alias 'dayClosePriceType')*[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_close_price_type "Link to this definition")
    :   the price type of the last (close) price for the day
        possible values are FINAL | INDICATIVE | PRELIMINARY | REGULAR

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_close_price_type-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* day\_high\_price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'dayHighPrice')*[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_high_price "Link to this definition")
    :   the maximal (high) price for the day

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_high_price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* day\_id : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'dayId')*[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_id "Link to this definition")
    :   identifier of the day that this summary represents

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_id-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* day\_low\_price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'dayLowPrice')*[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_low_price "Link to this definition")
    :   the minimal (low) price for the day

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_low_price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* day\_open\_price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'dayOpenPrice')*[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_open_price "Link to this definition")
    :   the first (open) price for the day

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.day_open_price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* open\_interest : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'openInterest')*[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.open_interest "Link to this definition")
    :   open interest of the symbol as the number of open contracts

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.open_interest-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* prev\_day\_close\_price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'prevDayClosePrice')*[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_close_price "Link to this definition")
    :   the last (close) price for the previous day

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_close_price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* prev\_day\_close\_price\_type : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]* *(alias 'prevDayClosePriceType')*[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_close_price_type "Link to this definition")
    :   the price type of the last (close) price for the previous day
        possible values are FINAL | INDICATIVE | PRELIMINARY | REGULAR

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_close_price_type-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* prev\_day\_id : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'prevDayId')*[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_id "Link to this definition")
    :   identifier of the previous day that this summary represents

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_id-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* prev\_day\_volume : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'prevDayVolume')*[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_volume "Link to this definition")
    :   total volume traded for the previous day

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.summary.Summary.prev_day_volume-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

## TimeAndSale[¶](dxfeed.html#module-tastytrade.dxfeed.timeandsale "Link to this heading")

*pydantic model* tastytrade.dxfeed.timeandsale.TimeAndSale(*\**, *[eventSymbol](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.eventSymbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[eventTime](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.eventTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[eventFlags](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.eventFlags (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[index](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.index (Python parameter) — unique per-symbol index of this time and sale event"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[time](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.time (Python parameter) — timestamp of the original event"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[timeNanoPart](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.timeNanoPart (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[sequence](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.sequence (Python parameter) — sequence of this quote"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[exchangeCode](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.exchangeCode (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[price](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.price (Python parameter) — price of this time and sale event"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[size](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.size (Python parameter) — size of this time and sale event as integer number (rounded toward zero)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[bidPrice](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.bidPrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[askPrice](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.askPrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[exchangeSaleConditions](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.exchangeSaleConditions (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[tradeThroughExempt](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.tradeThroughExempt (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[aggressorSide](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.aggressorSide (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[spreadLeg](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.spreadLeg (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[extendedTradingHours](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.extendedTradingHours (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[validTick](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.validTick (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[type](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.type (Python parameter) — type of event - 0: new, 1: correction, 2: cancellation"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[buyer](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.buyer (Python parameter) — Undocumented; always None"): [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*, *[seller](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.seller (Python parameter) — Undocumented; always None"): [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*)[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "Link to this definition")
:   Bases: [`IndexedEvent`](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent "tastytrade.dxfeed.event.IndexedEvent (Python model) — A dxfeed IndexedEvent with flags computed bitwise. For info see here.")

    TimeAndSale event represents a trade or other market event with a price,
    like market open/close price. TimeAndSale events are intended to provide
    information about trades in a continuous-time slice (unlike Trade events
    which are supposed to provide snapshots about the most recent trade).
    TimeAndSale events have a unique index that can be used for later
    correction/cancellation processing.

    Show JSON schema

    ```
    {
       "title": "TimeAndSale",
       "description": "TimeAndSale event represents a trade or other market event with a price,\nlike market open/close price. TimeAndSale events are intended to provide\ninformation about trades in a continuous-time slice (unlike Trade events\nwhich are supposed to provide snapshots about the most recent trade).\nTimeAndSale events have a unique index that can be used for later\ncorrection/cancellation processing.",
       "type": "object",
       "properties": {
          "eventSymbol": {
             "title": "Eventsymbol",
             "type": "string"
          },
          "eventTime": {
             "title": "Eventtime",
             "type": "integer"
          },
          "eventFlags": {
             "title": "Eventflags",
             "type": "integer"
          },
          "index": {
             "title": "Index",
             "type": "integer"
          },
          "time": {
             "title": "Time",
             "type": "integer"
          },
          "timeNanoPart": {
             "title": "Timenanopart",
             "type": "integer"
          },
          "sequence": {
             "title": "Sequence",
             "type": "integer"
          },
          "exchangeCode": {
             "title": "Exchangecode",
             "type": "string"
          },
          "price": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Price"
          },
          "size": {
             "title": "Size",
             "type": "integer"
          },
          "bidPrice": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Bidprice"
          },
          "askPrice": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Askprice"
          },
          "exchangeSaleConditions": {
             "title": "Exchangesaleconditions",
             "type": "string"
          },
          "tradeThroughExempt": {
             "title": "Tradethroughexempt",
             "type": "string"
          },
          "aggressorSide": {
             "title": "Aggressorside",
             "type": "string"
          },
          "spreadLeg": {
             "title": "Spreadleg",
             "type": "boolean"
          },
          "extendedTradingHours": {
             "title": "Extendedtradinghours",
             "type": "boolean"
          },
          "validTick": {
             "title": "Validtick",
             "type": "boolean"
          },
          "type": {
             "title": "Type",
             "type": "string"
          },
          "buyer": {
             "title": "Buyer",
             "type": "null"
          },
          "seller": {
             "title": "Seller",
             "type": "null"
          }
       },
       "required": [
          "eventSymbol",
          "eventTime",
          "eventFlags",
          "index",
          "time",
          "timeNanoPart",
          "sequence",
          "exchangeCode",
          "price",
          "size",
          "bidPrice",
          "askPrice",
          "exchangeSaleConditions",
          "tradeThroughExempt",
          "aggressorSide",
          "spreadLeg",
          "extendedTradingHours",
          "validTick",
          "type",
          "buyer",
          "seller"
       ]
    }

    ```

    Fields:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale-fields "Permalink to this headline")
    :   * [`aggressor_side (str)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.aggressor_side "tastytrade.dxfeed.timeandsale.TimeAndSale.aggressor_side (Python field) — initiator of the trade")
        * [`ask_price (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.ask_price "tastytrade.dxfeed.timeandsale.TimeAndSale.ask_price (Python field) — the ask price on the market when this time and sale event occured")
        * [`bid_price (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.bid_price "tastytrade.dxfeed.timeandsale.TimeAndSale.bid_price (Python field) — the bid price on the market when this time and sale event occured")
        * [`buyer (None)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.buyer (Python parameter) — Undocumented; always None")
        * [`exchange_code (str)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_code "tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_code (Python field) — exchange code of this time and sale event")
        * [`exchange_sale_conditions (str)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_sale_conditions "tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_sale_conditions (Python field) — sale conditions provided for this event by data feed")
        * [`extended_trading_hours (bool)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.extended_trading_hours "tastytrade.dxfeed.timeandsale.TimeAndSale.extended_trading_hours (Python field) — whether this transaction is completed during extended trading hours")
        * [`index (int)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.index (Python parameter) — unique per-symbol index of this time and sale event")
        * [`price (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.price (Python parameter) — price of this time and sale event")
        * [`seller (None)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.seller (Python parameter) — Undocumented; always None")
        * [`sequence (int)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.sequence (Python parameter) — sequence of this quote")
        * [`size (int)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.size (Python parameter) — size of this time and sale event as integer number (rounded toward zero)")
        * [`spread_leg (bool)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.spread_leg "tastytrade.dxfeed.timeandsale.TimeAndSale.spread_leg (Python field) — whether this transaction is a part of a multi-leg order")
        * [`time (int)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.time (Python parameter) — timestamp of the original event")
        * [`time_nano_part (int)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.time_nano_part "tastytrade.dxfeed.timeandsale.TimeAndSale.time_nano_part (Python field) — microseconds and nanoseconds part of time of the last bid or ask change")
        * [`trade_through_exempt (str)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.trade_through_exempt "tastytrade.dxfeed.timeandsale.TimeAndSale.trade_through_exempt (Python field) — transaction is concluded by exempting from compliance with some rule")
        * [`type (str)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale "tastytrade.dxfeed.timeandsale.TimeAndSale.type (Python parameter) — type of event - 0: new, 1: correction, 2: cancellation")
        * [`valid_tick (bool)`](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.valid_tick "tastytrade.dxfeed.timeandsale.TimeAndSale.valid_tick (Python field) — normalized SaleCondition flag")

    Validators:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale-validators "Permalink to this headline")

    *field* aggressor\_side : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]* *(alias 'aggressorSide')*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.aggressor_side "Link to this definition")
    :   initiator of the trade

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.aggressor_side-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* ask\_price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]* *(alias 'askPrice')*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.ask_price "Link to this definition")
    :   the ask price on the market when this time and sale event occured

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.ask_price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* bid\_price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]* *(alias 'bidPrice')*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.bid_price "Link to this definition")
    :   the bid price on the market when this time and sale event occured

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.bid_price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* buyer : [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.buyer "Link to this definition")
    :   Undocumented; always None

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.buyer-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* exchange\_code : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]* *(alias 'exchangeCode')*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_code "Link to this definition")
    :   exchange code of this time and sale event

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_code-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* exchange\_sale\_conditions : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]* *(alias 'exchangeSaleConditions')*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_sale_conditions "Link to this definition")
    :   sale conditions provided for this event by data feed

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.exchange_sale_conditions-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* extended\_trading\_hours : [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") *[Required]* *(alias 'extendedTradingHours')*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.extended_trading_hours "Link to this definition")
    :   whether this transaction is completed during extended trading hours

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.extended_trading_hours-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* index : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.index "Link to this definition")
    :   unique per-symbol index of this time and sale event

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.index-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.price "Link to this definition")
    :   price of this time and sale event

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* seller : [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.seller "Link to this definition")
    :   Undocumented; always None

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.seller-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* sequence : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.sequence "Link to this definition")
    :   sequence of this quote

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.sequence-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* size : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.size "Link to this definition")
    :   size of this time and sale event as integer number (rounded toward zero)

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.size-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* spread\_leg : [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") *[Required]* *(alias 'spreadLeg')*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.spread_leg "Link to this definition")
    :   whether this transaction is a part of a multi-leg order

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.spread_leg-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* time : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.time "Link to this definition")
    :   timestamp of the original event

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.time-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* time\_nano\_part : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'timeNanoPart')*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.time_nano_part "Link to this definition")
    :   microseconds and nanoseconds part of time of the last bid or ask change

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.time_nano_part-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* trade\_through\_exempt : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]* *(alias 'tradeThroughExempt')*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.trade_through_exempt "Link to this definition")
    :   transaction is concluded by exempting from compliance with some rule

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.trade_through_exempt-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* type : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.type "Link to this definition")
    :   type of event - 0: new, 1: correction, 2: cancellation

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.type-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* valid\_tick : [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") *[Required]* *(alias 'validTick')*[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.valid_tick "Link to this definition")
    :   normalized SaleCondition flag

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.timeandsale.TimeAndSale.valid_tick-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

## TheoPrice[¶](dxfeed.html#module-tastytrade.dxfeed.theoprice "Link to this heading")

*pydantic model* tastytrade.dxfeed.theoprice.TheoPrice(*\**, *[eventSymbol](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.eventSymbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[eventTime](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.eventTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[eventFlags](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.eventFlags (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[index](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.index (Python parameter) — unique per-symbol index of this event"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[time](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.time (Python parameter) — timestamp of this event in milliseconds"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[sequence](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.sequence (Python parameter) — sequence number to distinguish events that have the same time"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[price](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.price (Python parameter) — theoretical price"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[underlyingPrice](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.underlyingPrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[delta](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.delta (Python parameter) — delta of the theoretical price"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[gamma](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.gamma (Python parameter) — gamma of the theoretical price"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[dividend](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.dividend (Python parameter) — implied simple dividend return of the corresponding option series"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[interest](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.interest (Python parameter) — implied simple interest return of the corresponding option series"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*)[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "Link to this definition")
:   Bases: [`IndexedEvent`](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent "tastytrade.dxfeed.event.IndexedEvent (Python model) — A dxfeed IndexedEvent with flags computed bitwise. For info see here.")

    Theo price is a snapshot of the theoretical option price computation that
    is periodically performed by dxPrice model-free computation. dxFeed does
    not send recalculations for all options at the same time, so we provide
    you with a formula so you can perform calculations based on values from
    this event.

    Show JSON schema

    ```
    {
       "title": "TheoPrice",
       "description": "Theo price is a snapshot of the theoretical option price computation that\nis periodically performed by dxPrice model-free computation. dxFeed does\nnot send recalculations for all options at the same time, so we provide\nyou with a formula so you can perform calculations based on values from\nthis event.",
       "type": "object",
       "properties": {
          "eventSymbol": {
             "title": "Eventsymbol",
             "type": "string"
          },
          "eventTime": {
             "title": "Eventtime",
             "type": "integer"
          },
          "eventFlags": {
             "title": "Eventflags",
             "type": "integer"
          },
          "index": {
             "title": "Index",
             "type": "integer"
          },
          "time": {
             "title": "Time",
             "type": "integer"
          },
          "sequence": {
             "title": "Sequence",
             "type": "integer"
          },
          "price": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Price"
          },
          "underlyingPrice": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Underlyingprice"
          },
          "delta": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Delta"
          },
          "gamma": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Gamma"
          },
          "dividend": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Dividend"
          },
          "interest": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Interest"
          }
       },
       "required": [
          "eventSymbol",
          "eventTime",
          "eventFlags",
          "index",
          "time",
          "sequence",
          "price",
          "underlyingPrice",
          "delta",
          "gamma",
          "dividend",
          "interest"
       ]
    }

    ```

    Fields:[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice-fields "Permalink to this headline")
    :   * [`delta (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.delta (Python parameter) — delta of the theoretical price")
        * [`dividend (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.dividend (Python parameter) — implied simple dividend return of the corresponding option series")
        * [`gamma (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.gamma (Python parameter) — gamma of the theoretical price")
        * [`index (int)`](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.index (Python parameter) — unique per-symbol index of this event")
        * [`interest (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.interest (Python parameter) — implied simple interest return of the corresponding option series")
        * [`price (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.price (Python parameter) — theoretical price")
        * [`sequence (int)`](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.sequence (Python parameter) — sequence number to distinguish events that have the same time")
        * [`time (int)`](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice "tastytrade.dxfeed.theoprice.TheoPrice.time (Python parameter) — timestamp of this event in milliseconds")
        * [`underlying_price (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.underlying_price "tastytrade.dxfeed.theoprice.TheoPrice.underlying_price (Python field) — underlying price at the time of theo price computation")

    Validators:[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice-validators "Permalink to this headline")

    *field* delta : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.delta "Link to this definition")
    :   delta of the theoretical price

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.delta-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* dividend : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.dividend "Link to this definition")
    :   implied simple dividend return of the corresponding option series

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.dividend-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* gamma : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.gamma "Link to this definition")
    :   gamma of the theoretical price

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.gamma-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* index : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.index "Link to this definition")
    :   unique per-symbol index of this event

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.index-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* interest : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.interest "Link to this definition")
    :   implied simple interest return of the corresponding option series

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.interest-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.price "Link to this definition")
    :   theoretical price

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* sequence : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.sequence "Link to this definition")
    :   sequence number to distinguish events that have the same time

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.sequence-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* time : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.time "Link to this definition")
    :   timestamp of this event in milliseconds

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.time-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* underlying\_price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]* *(alias 'underlyingPrice')*[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.underlying_price "Link to this definition")
    :   underlying price at the time of theo price computation

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.theoprice.TheoPrice.underlying_price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

## Trade[¶](dxfeed.html#module-tastytrade.dxfeed.trade "Link to this heading")

*pydantic model* tastytrade.dxfeed.trade.Trade(*\**, *[eventSymbol](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.eventSymbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[eventTime](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.eventTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[time](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.time (Python parameter) — time of the last trade"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[timeNanoPart](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.timeNanoPart (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[sequence](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.sequence (Python parameter) — sequence of the last trade"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[exchangeCode](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.exchangeCode (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[dayId](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.dayId (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[tickDirection](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.tickDirection (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[extendedTradingHours](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.extendedTradingHours (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[price](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.price (Python parameter) — price of the last trade"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[change](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.change (Python parameter) — change of the last trade"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[size](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.size (Python parameter) — size of the last trade as integer number (rounded toward zero)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[dayVolume](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.dayVolume (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[dayTurnover](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.dayTurnover (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade "Link to this definition")
:   Bases: [`Event`](dxfeed.html#tastytrade.dxfeed.event.Event "tastytrade.dxfeed.event.Event (Python model) — Base class for dxfeed events received from the data streamer.")

    A Trade event provides prices and the volume of the last transaction in
    regular trading hours, as well as the total amount per day in the number
    of securities and in their value. This event does not contain information
    about all transactions, but only about the last transaction for a single
    instrument.

    Show JSON schema

    ```
    {
       "title": "Trade",
       "description": "A Trade event provides prices and the volume of the last transaction in\nregular trading hours, as well as the total amount per day in the number\nof securities and in their value. This event does not contain information\nabout all transactions, but only about the last transaction for a single\ninstrument.",
       "type": "object",
       "properties": {
          "eventSymbol": {
             "title": "Eventsymbol",
             "type": "string"
          },
          "eventTime": {
             "title": "Eventtime",
             "type": "integer"
          },
          "time": {
             "title": "Time",
             "type": "integer"
          },
          "timeNanoPart": {
             "title": "Timenanopart",
             "type": "integer"
          },
          "sequence": {
             "title": "Sequence",
             "type": "integer"
          },
          "exchangeCode": {
             "title": "Exchangecode",
             "type": "string"
          },
          "dayId": {
             "title": "Dayid",
             "type": "integer"
          },
          "tickDirection": {
             "title": "Tickdirection",
             "type": "string"
          },
          "extendedTradingHours": {
             "title": "Extendedtradinghours",
             "type": "boolean"
          },
          "price": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Price"
          },
          "change": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Change"
          },
          "size": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Size"
          },
          "dayVolume": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Dayvolume"
          },
          "dayTurnover": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Dayturnover"
          }
       },
       "required": [
          "eventSymbol",
          "eventTime",
          "time",
          "timeNanoPart",
          "sequence",
          "exchangeCode",
          "dayId",
          "tickDirection",
          "extendedTradingHours",
          "price"
       ]
    }

    ```

    Fields:[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade-fields "Permalink to this headline")
    :   * [`change (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.change (Python parameter) — change of the last trade")
        * [`day_id (int)`](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_id "tastytrade.dxfeed.trade.Trade.day_id (Python field) — identifier of the current trading day")
        * [`day_turnover (decimal.Decimal | None)`](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_turnover "tastytrade.dxfeed.trade.Trade.day_turnover (Python field) — total turnover traded for a day")
        * [`day_volume (int | None)`](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_volume "tastytrade.dxfeed.trade.Trade.day_volume (Python field) — total vlume traded for a day as integer number (rounded toward zero)")
        * [`exchange_code (str)`](dxfeed.html#tastytrade.dxfeed.trade.Trade.exchange_code "tastytrade.dxfeed.trade.Trade.exchange_code (Python field) — exchange code of the last trade")
        * [`extended_trading_hours (bool)`](dxfeed.html#tastytrade.dxfeed.trade.Trade.extended_trading_hours "tastytrade.dxfeed.trade.Trade.extended_trading_hours (Python field) — whether the last trade was in extended trading hours")
        * [`price (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.price (Python parameter) — price of the last trade")
        * [`sequence (int)`](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.sequence (Python parameter) — sequence of the last trade")
        * [`size (int | None)`](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.size (Python parameter) — size of the last trade as integer number (rounded toward zero)")
        * [`tick_direction (str)`](dxfeed.html#tastytrade.dxfeed.trade.Trade.tick_direction "tastytrade.dxfeed.trade.Trade.tick_direction (Python field) — tick direction of the last trade possible values are DOWN | UNDEFINED | UP | ZERO | ZERO_DOWN | ZERO_UP")
        * [`time (int)`](dxfeed.html#tastytrade.dxfeed.trade.Trade "tastytrade.dxfeed.trade.Trade.time (Python parameter) — time of the last trade")
        * [`time_nano_part (int)`](dxfeed.html#tastytrade.dxfeed.trade.Trade.time_nano_part "tastytrade.dxfeed.trade.Trade.time_nano_part (Python field) — microseconds and nanoseconds time part of the last trade")

    Validators:[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade-validators "Permalink to this headline")

    *field* change : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.change "Link to this definition")
    :   change of the last trade

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.change-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* day\_id : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'dayId')*[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_id "Link to this definition")
    :   identifier of the current trading day

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_id-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* day\_turnover : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'dayTurnover')*[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_turnover "Link to this definition")
    :   total turnover traded for a day

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_turnover-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* day\_volume : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'dayVolume')*[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_volume "Link to this definition")
    :   total vlume traded for a day as integer number (rounded toward zero)

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.day_volume-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* exchange\_code : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]* *(alias 'exchangeCode')*[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.exchange_code "Link to this definition")
    :   exchange code of the last trade

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.exchange_code-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* extended\_trading\_hours : [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") *[Required]* *(alias 'extendedTradingHours')*[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.extended_trading_hours "Link to this definition")
    :   whether the last trade was in extended trading hours

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.extended_trading_hours-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.price "Link to this definition")
    :   price of the last trade

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.price-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* sequence : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.sequence "Link to this definition")
    :   sequence of the last trade

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.sequence-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* size : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.size "Link to this definition")
    :   size of the last trade as integer number (rounded toward zero)

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.size-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* tick\_direction : [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *[Required]* *(alias 'tickDirection')*[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.tick_direction "Link to this definition")
    :   tick direction of the last trade
        possible values are DOWN | UNDEFINED | UP | ZERO | ZERO\_DOWN | ZERO\_UP

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.tick_direction-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* time : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.time "Link to this definition")
    :   time of the last trade

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.time-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* time\_nano\_part : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'timeNanoPart')*[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.time_nano_part "Link to this definition")
    :   microseconds and nanoseconds time part of the last trade

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.trade.Trade.time_nano_part-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

## Underlying[¶](dxfeed.html#module-tastytrade.dxfeed.underlying "Link to this heading")

*pydantic model* tastytrade.dxfeed.underlying.Underlying(*\**, *[eventSymbol](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.eventSymbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[eventTime](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.eventTime (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[eventFlags](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.eventFlags (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[index](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.index (Python parameter) — unique per-symbol index of this event"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[time](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.time (Python parameter) — timestamp of this event in milliseconds"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[sequence](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.sequence (Python parameter) — sequence number of this event to distinguish events with the same time"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[volatility](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.volatility (Python parameter) — 30-day implied volatility for this underlying based on VIX methodology"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[frontVolatility](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.frontVolatility (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[backVolatility](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.backVolatility (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[callVolume](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.callVolume (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[putVolume](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.putVolume (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[optionVolume](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.optionVolume (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[putCallRatio](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.putCallRatio (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*)[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "Link to this definition")
:   Bases: [`IndexedEvent`](dxfeed.html#tastytrade.dxfeed.event.IndexedEvent "tastytrade.dxfeed.event.IndexedEvent (Python model) — A dxfeed IndexedEvent with flags computed bitwise. For info see here.")

    Underlying event is a snapshot of computed values that are available for
    an option underlying symbol based on the option prices on the market. It
    represents the most recent information that is available about the
    corresponding values on the market at any given moment of time.

    Show JSON schema

    ```
    {
       "title": "Underlying",
       "description": "Underlying event is a snapshot of computed values that are available for\nan option underlying symbol based on the option prices on the market. It\nrepresents the most recent information that is available about the\ncorresponding values on the market at any given moment of time.",
       "type": "object",
       "properties": {
          "eventSymbol": {
             "title": "Eventsymbol",
             "type": "string"
          },
          "eventTime": {
             "title": "Eventtime",
             "type": "integer"
          },
          "eventFlags": {
             "title": "Eventflags",
             "type": "integer"
          },
          "index": {
             "title": "Index",
             "type": "integer"
          },
          "time": {
             "title": "Time",
             "type": "integer"
          },
          "sequence": {
             "title": "Sequence",
             "type": "integer"
          },
          "volatility": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Volatility"
          },
          "frontVolatility": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Frontvolatility"
          },
          "backVolatility": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Backvolatility"
          },
          "callVolume": {
             "title": "Callvolume",
             "type": "integer"
          },
          "putVolume": {
             "title": "Putvolume",
             "type": "integer"
          },
          "optionVolume": {
             "title": "Optionvolume",
             "type": "integer"
          },
          "putCallRatio": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Putcallratio"
          }
       },
       "required": [
          "eventSymbol",
          "eventTime",
          "eventFlags",
          "index",
          "time",
          "sequence",
          "volatility",
          "frontVolatility",
          "backVolatility",
          "callVolume",
          "putVolume",
          "optionVolume",
          "putCallRatio"
       ]
    }

    ```

    Fields:[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying-fields "Permalink to this headline")
    :   * [`back_volatility (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.back_volatility "tastytrade.dxfeed.underlying.Underlying.back_volatility (Python field) — back month implied volatility for the underlying using VIX methodology")
        * [`call_volume (int)`](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.call_volume "tastytrade.dxfeed.underlying.Underlying.call_volume (Python field) — call options traded volume for a day")
        * [`front_volatility (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.front_volatility "tastytrade.dxfeed.underlying.Underlying.front_volatility (Python field) — front month implied volatility for the underlying using VIX methodology")
        * [`index (int)`](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.index (Python parameter) — unique per-symbol index of this event")
        * [`option_volume (int)`](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.option_volume "tastytrade.dxfeed.underlying.Underlying.option_volume (Python field) — options traded volume for a day")
        * [`put_call_ratio (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.put_call_ratio "tastytrade.dxfeed.underlying.Underlying.put_call_ratio (Python field) — ratio of put options volume to call options volume for a day")
        * [`put_volume (int)`](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.put_volume "tastytrade.dxfeed.underlying.Underlying.put_volume (Python field) — put options traded volume for a day")
        * [`sequence (int)`](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.sequence (Python parameter) — sequence number of this event to distinguish events with the same time")
        * [`time (int)`](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.time (Python parameter) — timestamp of this event in milliseconds")
        * [`volatility (decimal.Decimal)`](dxfeed.html#tastytrade.dxfeed.underlying.Underlying "tastytrade.dxfeed.underlying.Underlying.volatility (Python parameter) — 30-day implied volatility for this underlying based on VIX methodology")

    Validators:[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying-validators "Permalink to this headline")

    *field* back\_volatility : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]* *(alias 'backVolatility')*[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.back_volatility "Link to this definition")
    :   back month implied volatility for the underlying using VIX methodology

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.back_volatility-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* call\_volume : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'callVolume')*[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.call_volume "Link to this definition")
    :   call options traded volume for a day

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.call_volume-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* front\_volatility : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]* *(alias 'frontVolatility')*[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.front_volatility "Link to this definition")
    :   front month implied volatility for the underlying using VIX methodology

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.front_volatility-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* index : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.index "Link to this definition")
    :   unique per-symbol index of this event

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.index-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* option\_volume : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'optionVolume')*[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.option_volume "Link to this definition")
    :   options traded volume for a day

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.option_volume-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* put\_call\_ratio : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]* *(alias 'putCallRatio')*[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.put_call_ratio "Link to this definition")
    :   ratio of put options volume to call options volume for a day

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.put_call_ratio-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* put\_volume : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]* *(alias 'putVolume')*[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.put_volume "Link to this definition")
    :   put options traded volume for a day

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.put_volume-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* sequence : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.sequence "Link to this definition")
    :   sequence number of this event to distinguish events with the same time

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.sequence-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* time : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.time "Link to this definition")
    :   timestamp of this event in milliseconds

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.time-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

    *field* volatility : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") *[Required]*[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.volatility "Link to this definition")
    :   30-day implied volatility for this underlying based on VIX methodology

        Validated by:[¶](dxfeed.html#tastytrade.dxfeed.underlying.Underlying.volatility-validated-by "Permalink to this headline")
        :   * `change_nan_to_none`

[Back to top](dxfeed.html#)


[Previous
tastytrade.backtest](backtesting.html)
[Next
tastytrade.instruments](instruments.html)

© Copyright 2025, tastyware.

Created using
[Sphinx](https://www.sphinx-doc.org/)
7.4.7.
and
[Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)