tastytrade.account - tastytrade 10.1.0 documentation







[Skip to content](account.html#tastytrade.account.Account)

tastytrade 10.1.0 documentation

tastytrade.account






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
  + tastytrade.account

    [tastytrade.account](account.html#)



    tastytrade.account
    - [tastytrade.account.Account](account.html#tastytrade.account.Account)

      * [Fields](account.html#tastytrade.account.Account-fields)
      * [Ma\_delete\_complex\_order](account.html#tastytrade.account.Account.a_delete_complex_order)

        + [Parameters](account.html#tastytrade.account.Account.a_delete_complex_order-parameters)

          - [psession](account.html#tastytrade.account.Account.a_delete_complex_order.session)
          - [porder\_id](account.html#tastytrade.account.Account.a_delete_complex_order.order_id)
      * [Ma\_delete\_order](account.html#tastytrade.account.Account.a_delete_order)

        + [Parameters](account.html#tastytrade.account.Account.a_delete_order-parameters)

          - [psession](account.html#tastytrade.account.Account.a_delete_order.session)
          - [porder\_id](account.html#tastytrade.account.Account.a_delete_order.order_id)
      * [Ma\_get](account.html#tastytrade.account.Account.a_get)

        + [Parameters](account.html#tastytrade.account.Account.a_get-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get.session)
          - [pinclude\_closed](account.html#tastytrade.account.Account.a_get.include_closed)
      * [Ma\_get\_balance\_snapshots](account.html#tastytrade.account.Account.a_get_balance_snapshots)

        + [Parameters](account.html#tastytrade.account.Account.a_get_balance_snapshots-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_balance_snapshots.session)
          - [pcurrency](account.html#tastytrade.account.Account.a_get_balance_snapshots.currency)
          - [pstart\_date](account.html#tastytrade.account.Account.a_get_balance_snapshots.start_date)
          - [pend\_date](account.html#tastytrade.account.Account.a_get_balance_snapshots.end_date)
          - [psnapshot\_date](account.html#tastytrade.account.Account.a_get_balance_snapshots.snapshot_date)
          - [ptime\_of\_day](account.html#tastytrade.account.Account.a_get_balance_snapshots.time_of_day)
      * [Ma\_get\_balances](account.html#tastytrade.account.Account.a_get_balances)

        + [Parameters](account.html#tastytrade.account.Account.a_get_balances-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_balances.session)
      * [Ma\_get\_complex\_order](account.html#tastytrade.account.Account.a_get_complex_order)

        + [Parameters](account.html#tastytrade.account.Account.a_get_complex_order-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_complex_order.session)
          - [porder\_id](account.html#tastytrade.account.Account.a_get_complex_order.order_id)
      * [Ma\_get\_complex\_order\_history](account.html#tastytrade.account.Account.a_get_complex_order_history)

        + [Parameters](account.html#tastytrade.account.Account.a_get_complex_order_history-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_complex_order_history.session)
          - [pper\_page](account.html#tastytrade.account.Account.a_get_complex_order_history.per_page)
          - [ppage\_offset](account.html#tastytrade.account.Account.a_get_complex_order_history.page_offset)
      * [Ma\_get\_effective\_margin\_requirements](account.html#tastytrade.account.Account.a_get_effective_margin_requirements)

        + [Parameters](account.html#tastytrade.account.Account.a_get_effective_margin_requirements-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_effective_margin_requirements.session)
          - [psymbol](account.html#tastytrade.account.Account.a_get_effective_margin_requirements.symbol)
      * [Ma\_get\_history](account.html#tastytrade.account.Account.a_get_history)

        + [Parameters](account.html#tastytrade.account.Account.a_get_history-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_history.session)
          - [pper\_page](account.html#tastytrade.account.Account.a_get_history.per_page)
          - [ppage\_offset](account.html#tastytrade.account.Account.a_get_history.page_offset)
          - [psort](account.html#tastytrade.account.Account.a_get_history.sort)
          - [ptype](account.html#tastytrade.account.Account.a_get_history.type)
          - [ptypes](account.html#tastytrade.account.Account.a_get_history.types)
          - [psub\_types](account.html#tastytrade.account.Account.a_get_history.sub_types)
          - [pstart\_date](account.html#tastytrade.account.Account.a_get_history.start_date)
          - [pend\_date](account.html#tastytrade.account.Account.a_get_history.end_date)
          - [pinstrument\_type](account.html#tastytrade.account.Account.a_get_history.instrument_type)
          - [psymbol](account.html#tastytrade.account.Account.a_get_history.symbol)
          - [punderlying\_symbol](account.html#tastytrade.account.Account.a_get_history.underlying_symbol)
          - [paction](account.html#tastytrade.account.Account.a_get_history.action)
          - [ppartition\_key](account.html#tastytrade.account.Account.a_get_history.partition_key)
          - [pfutures\_symbol](account.html#tastytrade.account.Account.a_get_history.futures_symbol)
          - [pstart\_at](account.html#tastytrade.account.Account.a_get_history.start_at)
          - [pend\_at](account.html#tastytrade.account.Account.a_get_history.end_at)
      * [Ma\_get\_live\_complex\_orders](account.html#tastytrade.account.Account.a_get_live_complex_orders)

        + [Parameters](account.html#tastytrade.account.Account.a_get_live_complex_orders-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_live_complex_orders.session)
      * [Ma\_get\_live\_orders](account.html#tastytrade.account.Account.a_get_live_orders)

        + [Parameters](account.html#tastytrade.account.Account.a_get_live_orders-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_live_orders.session)
      * [Ma\_get\_margin\_requirements](account.html#tastytrade.account.Account.a_get_margin_requirements)

        + [Parameters](account.html#tastytrade.account.Account.a_get_margin_requirements-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_margin_requirements.session)
      * [Ma\_get\_net\_liquidating\_value\_history](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history)

        + [Parameters](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history.session)
          - [ptime\_back](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history.time_back)
          - [pstart\_time](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history.start_time)
      * [Ma\_get\_order](account.html#tastytrade.account.Account.a_get_order)

        + [Parameters](account.html#tastytrade.account.Account.a_get_order-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_order.session)
          - [porder\_id](account.html#tastytrade.account.Account.a_get_order.order_id)
      * [Ma\_get\_order\_chains](account.html#tastytrade.account.Account.a_get_order_chains)

        + [Parameters](account.html#tastytrade.account.Account.a_get_order_chains-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_order_chains.session)
          - [psymbol](account.html#tastytrade.account.Account.a_get_order_chains.symbol)
          - [pstart\_time](account.html#tastytrade.account.Account.a_get_order_chains.start_time)
          - [pend\_time](account.html#tastytrade.account.Account.a_get_order_chains.end_time)
      * [Ma\_get\_order\_history](account.html#tastytrade.account.Account.a_get_order_history)

        + [Parameters](account.html#tastytrade.account.Account.a_get_order_history-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_order_history.session)
          - [pper\_page](account.html#tastytrade.account.Account.a_get_order_history.per_page)
          - [ppage\_offset](account.html#tastytrade.account.Account.a_get_order_history.page_offset)
          - [pstart\_date](account.html#tastytrade.account.Account.a_get_order_history.start_date)
          - [pend\_date](account.html#tastytrade.account.Account.a_get_order_history.end_date)
          - [punderlying\_symbol](account.html#tastytrade.account.Account.a_get_order_history.underlying_symbol)
          - [pstatuses](account.html#tastytrade.account.Account.a_get_order_history.statuses)
          - [pfutures\_symbol](account.html#tastytrade.account.Account.a_get_order_history.futures_symbol)
          - [punderlying\_instrument\_type](account.html#tastytrade.account.Account.a_get_order_history.underlying_instrument_type)
          - [psort](account.html#tastytrade.account.Account.a_get_order_history.sort)
          - [pstart\_at](account.html#tastytrade.account.Account.a_get_order_history.start_at)
          - [pend\_at](account.html#tastytrade.account.Account.a_get_order_history.end_at)
      * [Ma\_get\_position\_limit](account.html#tastytrade.account.Account.a_get_position_limit)

        + [Parameters](account.html#tastytrade.account.Account.a_get_position_limit-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_position_limit.session)
      * [Ma\_get\_positions](account.html#tastytrade.account.Account.a_get_positions)

        + [Parameters](account.html#tastytrade.account.Account.a_get_positions-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_positions.session)
          - [punderlying\_symbols](account.html#tastytrade.account.Account.a_get_positions.underlying_symbols)
          - [psymbol](account.html#tastytrade.account.Account.a_get_positions.symbol)
          - [pinstrument\_type](account.html#tastytrade.account.Account.a_get_positions.instrument_type)
          - [pinclude\_closed](account.html#tastytrade.account.Account.a_get_positions.include_closed)
          - [punderlying\_product\_code](account.html#tastytrade.account.Account.a_get_positions.underlying_product_code)
          - [ppartition\_keys](account.html#tastytrade.account.Account.a_get_positions.partition_keys)
          - [pnet\_positions](account.html#tastytrade.account.Account.a_get_positions.net_positions)
          - [pinclude\_marks](account.html#tastytrade.account.Account.a_get_positions.include_marks)
      * [Ma\_get\_total\_fees](account.html#tastytrade.account.Account.a_get_total_fees)

        + [Parameters](account.html#tastytrade.account.Account.a_get_total_fees-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_total_fees.session)
          - [pday](account.html#tastytrade.account.Account.a_get_total_fees.day)
      * [Ma\_get\_trading\_status](account.html#tastytrade.account.Account.a_get_trading_status)

        + [Parameters](account.html#tastytrade.account.Account.a_get_trading_status-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_trading_status.session)
      * [Ma\_get\_transaction](account.html#tastytrade.account.Account.a_get_transaction)

        + [Parameters](account.html#tastytrade.account.Account.a_get_transaction-parameters)

          - [psession](account.html#tastytrade.account.Account.a_get_transaction.session)
          - [pid](account.html#tastytrade.account.Account.a_get_transaction.id)
      * [Ma\_place\_complex\_order](account.html#tastytrade.account.Account.a_place_complex_order)

        + [Parameters](account.html#tastytrade.account.Account.a_place_complex_order-parameters)

          - [psession](account.html#tastytrade.account.Account.a_place_complex_order.session)
          - [porder](account.html#tastytrade.account.Account.a_place_complex_order.order)
          - [pdry\_run](account.html#tastytrade.account.Account.a_place_complex_order.dry_run)
      * [Ma\_place\_order](account.html#tastytrade.account.Account.a_place_order)

        + [Parameters](account.html#tastytrade.account.Account.a_place_order-parameters)

          - [psession](account.html#tastytrade.account.Account.a_place_order.session)
          - [porder](account.html#tastytrade.account.Account.a_place_order.order)
          - [pdry\_run](account.html#tastytrade.account.Account.a_place_order.dry_run)
      * [Ma\_replace\_order](account.html#tastytrade.account.Account.a_replace_order)

        + [Parameters](account.html#tastytrade.account.Account.a_replace_order-parameters)

          - [psession](account.html#tastytrade.account.Account.a_replace_order.session)
          - [pold\_order\_id](account.html#tastytrade.account.Account.a_replace_order.old_order_id)
          - [pnew\_order](account.html#tastytrade.account.Account.a_replace_order.new_order)
      * [Mdelete\_complex\_order](account.html#tastytrade.account.Account.delete_complex_order)

        + [Parameters](account.html#tastytrade.account.Account.delete_complex_order-parameters)

          - [psession](account.html#tastytrade.account.Account.delete_complex_order.session)
          - [porder\_id](account.html#tastytrade.account.Account.delete_complex_order.order_id)
      * [Mdelete\_order](account.html#tastytrade.account.Account.delete_order)

        + [Parameters](account.html#tastytrade.account.Account.delete_order-parameters)

          - [psession](account.html#tastytrade.account.Account.delete_order.session)
          - [porder\_id](account.html#tastytrade.account.Account.delete_order.order_id)
      * [Mget](account.html#tastytrade.account.Account.get)

        + [Parameters](account.html#tastytrade.account.Account.get-parameters)

          - [psession](account.html#tastytrade.account.Account.get.session)
          - [pinclude\_closed](account.html#tastytrade.account.Account.get.include_closed)
        + [Returns](account.html#tastytrade.account.Account.get-returns)
      * [Mget\_balance\_snapshots](account.html#tastytrade.account.Account.get_balance_snapshots)

        + [Parameters](account.html#tastytrade.account.Account.get_balance_snapshots-parameters)

          - [psession](account.html#tastytrade.account.Account.get_balance_snapshots.session)
          - [pcurrency](account.html#tastytrade.account.Account.get_balance_snapshots.currency)
          - [pstart\_date](account.html#tastytrade.account.Account.get_balance_snapshots.start_date)
          - [pend\_date](account.html#tastytrade.account.Account.get_balance_snapshots.end_date)
          - [psnapshot\_date](account.html#tastytrade.account.Account.get_balance_snapshots.snapshot_date)
          - [ptime\_of\_day](account.html#tastytrade.account.Account.get_balance_snapshots.time_of_day)
      * [Mget\_balances](account.html#tastytrade.account.Account.get_balances)

        + [Parameters](account.html#tastytrade.account.Account.get_balances-parameters)

          - [psession](account.html#tastytrade.account.Account.get_balances.session)
      * [Mget\_complex\_order](account.html#tastytrade.account.Account.get_complex_order)

        + [Parameters](account.html#tastytrade.account.Account.get_complex_order-parameters)

          - [psession](account.html#tastytrade.account.Account.get_complex_order.session)
          - [porder\_id](account.html#tastytrade.account.Account.get_complex_order.order_id)
      * [Mget\_complex\_order\_history](account.html#tastytrade.account.Account.get_complex_order_history)

        + [Parameters](account.html#tastytrade.account.Account.get_complex_order_history-parameters)

          - [psession](account.html#tastytrade.account.Account.get_complex_order_history.session)
          - [pper\_page](account.html#tastytrade.account.Account.get_complex_order_history.per_page)
          - [ppage\_offset](account.html#tastytrade.account.Account.get_complex_order_history.page_offset)
      * [Mget\_effective\_margin\_requirements](account.html#tastytrade.account.Account.get_effective_margin_requirements)

        + [Parameters](account.html#tastytrade.account.Account.get_effective_margin_requirements-parameters)

          - [psession](account.html#tastytrade.account.Account.get_effective_margin_requirements.session)
          - [psymbol](account.html#tastytrade.account.Account.get_effective_margin_requirements.symbol)
      * [Mget\_history](account.html#tastytrade.account.Account.get_history)

        + [Parameters](account.html#tastytrade.account.Account.get_history-parameters)

          - [psession](account.html#tastytrade.account.Account.get_history.session)
          - [pper\_page](account.html#tastytrade.account.Account.get_history.per_page)
          - [ppage\_offset](account.html#tastytrade.account.Account.get_history.page_offset)
          - [psort](account.html#tastytrade.account.Account.get_history.sort)
          - [ptype](account.html#tastytrade.account.Account.get_history.type)
          - [ptypes](account.html#tastytrade.account.Account.get_history.types)
          - [psub\_types](account.html#tastytrade.account.Account.get_history.sub_types)
          - [pstart\_date](account.html#tastytrade.account.Account.get_history.start_date)
          - [pend\_date](account.html#tastytrade.account.Account.get_history.end_date)
          - [pinstrument\_type](account.html#tastytrade.account.Account.get_history.instrument_type)
          - [psymbol](account.html#tastytrade.account.Account.get_history.symbol)
          - [punderlying\_symbol](account.html#tastytrade.account.Account.get_history.underlying_symbol)
          - [paction](account.html#tastytrade.account.Account.get_history.action)
          - [ppartition\_key](account.html#tastytrade.account.Account.get_history.partition_key)
          - [pfutures\_symbol](account.html#tastytrade.account.Account.get_history.futures_symbol)
          - [pstart\_at](account.html#tastytrade.account.Account.get_history.start_at)
          - [pend\_at](account.html#tastytrade.account.Account.get_history.end_at)
      * [Mget\_live\_complex\_orders](account.html#tastytrade.account.Account.get_live_complex_orders)

        + [Parameters](account.html#tastytrade.account.Account.get_live_complex_orders-parameters)

          - [psession](account.html#tastytrade.account.Account.get_live_complex_orders.session)
      * [Mget\_live\_orders](account.html#tastytrade.account.Account.get_live_orders)

        + [Parameters](account.html#tastytrade.account.Account.get_live_orders-parameters)

          - [psession](account.html#tastytrade.account.Account.get_live_orders.session)
      * [Mget\_margin\_requirements](account.html#tastytrade.account.Account.get_margin_requirements)

        + [Parameters](account.html#tastytrade.account.Account.get_margin_requirements-parameters)

          - [psession](account.html#tastytrade.account.Account.get_margin_requirements.session)
      * [Mget\_net\_liquidating\_value\_history](account.html#tastytrade.account.Account.get_net_liquidating_value_history)

        + [Parameters](account.html#tastytrade.account.Account.get_net_liquidating_value_history-parameters)

          - [psession](account.html#tastytrade.account.Account.get_net_liquidating_value_history.session)
          - [ptime\_back](account.html#tastytrade.account.Account.get_net_liquidating_value_history.time_back)
          - [pstart\_time](account.html#tastytrade.account.Account.get_net_liquidating_value_history.start_time)
      * [Mget\_order](account.html#tastytrade.account.Account.get_order)

        + [Parameters](account.html#tastytrade.account.Account.get_order-parameters)

          - [psession](account.html#tastytrade.account.Account.get_order.session)
          - [porder\_id](account.html#tastytrade.account.Account.get_order.order_id)
      * [Mget\_order\_chains](account.html#tastytrade.account.Account.get_order_chains)

        + [Parameters](account.html#tastytrade.account.Account.get_order_chains-parameters)

          - [psession](account.html#tastytrade.account.Account.get_order_chains.session)
          - [psymbol](account.html#tastytrade.account.Account.get_order_chains.symbol)
          - [pstart\_time](account.html#tastytrade.account.Account.get_order_chains.start_time)
          - [pend\_time](account.html#tastytrade.account.Account.get_order_chains.end_time)
      * [Mget\_order\_history](account.html#tastytrade.account.Account.get_order_history)

        + [Parameters](account.html#tastytrade.account.Account.get_order_history-parameters)

          - [psession](account.html#tastytrade.account.Account.get_order_history.session)
          - [pper\_page](account.html#tastytrade.account.Account.get_order_history.per_page)
          - [ppage\_offset](account.html#tastytrade.account.Account.get_order_history.page_offset)
          - [pstart\_date](account.html#tastytrade.account.Account.get_order_history.start_date)
          - [pend\_date](account.html#tastytrade.account.Account.get_order_history.end_date)
          - [punderlying\_symbol](account.html#tastytrade.account.Account.get_order_history.underlying_symbol)
          - [pstatuses](account.html#tastytrade.account.Account.get_order_history.statuses)
          - [pfutures\_symbol](account.html#tastytrade.account.Account.get_order_history.futures_symbol)
          - [punderlying\_instrument\_type](account.html#tastytrade.account.Account.get_order_history.underlying_instrument_type)
          - [psort](account.html#tastytrade.account.Account.get_order_history.sort)
          - [pstart\_at](account.html#tastytrade.account.Account.get_order_history.start_at)
          - [pend\_at](account.html#tastytrade.account.Account.get_order_history.end_at)
      * [Mget\_position\_limit](account.html#tastytrade.account.Account.get_position_limit)

        + [Parameters](account.html#tastytrade.account.Account.get_position_limit-parameters)

          - [psession](account.html#tastytrade.account.Account.get_position_limit.session)
      * [Mget\_positions](account.html#tastytrade.account.Account.get_positions)

        + [Parameters](account.html#tastytrade.account.Account.get_positions-parameters)

          - [psession](account.html#tastytrade.account.Account.get_positions.session)
          - [punderlying\_symbols](account.html#tastytrade.account.Account.get_positions.underlying_symbols)
          - [psymbol](account.html#tastytrade.account.Account.get_positions.symbol)
          - [pinstrument\_type](account.html#tastytrade.account.Account.get_positions.instrument_type)
          - [pinclude\_closed](account.html#tastytrade.account.Account.get_positions.include_closed)
          - [punderlying\_product\_code](account.html#tastytrade.account.Account.get_positions.underlying_product_code)
          - [ppartition\_keys](account.html#tastytrade.account.Account.get_positions.partition_keys)
          - [pnet\_positions](account.html#tastytrade.account.Account.get_positions.net_positions)
          - [pinclude\_marks](account.html#tastytrade.account.Account.get_positions.include_marks)
      * [Mget\_total\_fees](account.html#tastytrade.account.Account.get_total_fees)

        + [Parameters](account.html#tastytrade.account.Account.get_total_fees-parameters)

          - [psession](account.html#tastytrade.account.Account.get_total_fees.session)
          - [pday](account.html#tastytrade.account.Account.get_total_fees.day)
      * [Mget\_trading\_status](account.html#tastytrade.account.Account.get_trading_status)

        + [Parameters](account.html#tastytrade.account.Account.get_trading_status-parameters)

          - [psession](account.html#tastytrade.account.Account.get_trading_status.session)
      * [Mget\_transaction](account.html#tastytrade.account.Account.get_transaction)

        + [Parameters](account.html#tastytrade.account.Account.get_transaction-parameters)

          - [psession](account.html#tastytrade.account.Account.get_transaction.session)
          - [pid](account.html#tastytrade.account.Account.get_transaction.id)
      * [Mplace\_complex\_order](account.html#tastytrade.account.Account.place_complex_order)

        + [Parameters](account.html#tastytrade.account.Account.place_complex_order-parameters)

          - [psession](account.html#tastytrade.account.Account.place_complex_order.session)
          - [porder](account.html#tastytrade.account.Account.place_complex_order.order)
          - [pdry\_run](account.html#tastytrade.account.Account.place_complex_order.dry_run)
      * [Mplace\_order](account.html#tastytrade.account.Account.place_order)

        + [Parameters](account.html#tastytrade.account.Account.place_order-parameters)

          - [psession](account.html#tastytrade.account.Account.place_order.session)
          - [porder](account.html#tastytrade.account.Account.place_order.order)
          - [pdry\_run](account.html#tastytrade.account.Account.place_order.dry_run)
      * [Mreplace\_order](account.html#tastytrade.account.Account.replace_order)

        + [Parameters](account.html#tastytrade.account.Account.replace_order-parameters)

          - [psession](account.html#tastytrade.account.Account.replace_order.session)
          - [pold\_order\_id](account.html#tastytrade.account.Account.replace_order.old_order_id)
          - [pnew\_order](account.html#tastytrade.account.Account.replace_order.new_order)
    - [tastytrade.account.AccountBalance](account.html#tastytrade.account.AccountBalance)

      * [Fields](account.html#tastytrade.account.AccountBalance-fields)
      * [Validators](account.html#tastytrade.account.AccountBalance-validators)
    - [tastytrade.account.AccountBalanceSnapshot](account.html#tastytrade.account.AccountBalanceSnapshot)

      * [Fields](account.html#tastytrade.account.AccountBalanceSnapshot-fields)
      * [Validators](account.html#tastytrade.account.AccountBalanceSnapshot-validators)
    - [tastytrade.account.CurrentPosition](account.html#tastytrade.account.CurrentPosition)

      * [Fields](account.html#tastytrade.account.CurrentPosition-fields)
      * [Validators](account.html#tastytrade.account.CurrentPosition-validators)
    - [tastytrade.account.EmptyDict](account.html#tastytrade.account.EmptyDict)
    - [tastytrade.account.FeesInfo](account.html#tastytrade.account.FeesInfo)

      * [Fields](account.html#tastytrade.account.FeesInfo-fields)
      * [Validators](account.html#tastytrade.account.FeesInfo-validators)
    - [tastytrade.account.Lot](account.html#tastytrade.account.Lot)

      * [Fields](account.html#tastytrade.account.Lot-fields)
    - [tastytrade.account.MarginReport](account.html#tastytrade.account.MarginReport)

      * [Fields](account.html#tastytrade.account.MarginReport-fields)
      * [Validators](account.html#tastytrade.account.MarginReport-validators)
    - [tastytrade.account.MarginReportEntry](account.html#tastytrade.account.MarginReportEntry)

      * [Fields](account.html#tastytrade.account.MarginReportEntry-fields)
      * [Validators](account.html#tastytrade.account.MarginReportEntry-validators)
    - [tastytrade.account.MarginRequirement](account.html#tastytrade.account.MarginRequirement)

      * [Fields](account.html#tastytrade.account.MarginRequirement-fields)
    - [tastytrade.account.NetLiqOhlc](account.html#tastytrade.account.NetLiqOhlc)

      * [Fields](account.html#tastytrade.account.NetLiqOhlc-fields)
    - [tastytrade.account.PositionLimit](account.html#tastytrade.account.PositionLimit)

      * [Fields](account.html#tastytrade.account.PositionLimit-fields)
    - [tastytrade.account.TradingStatus](account.html#tastytrade.account.TradingStatus)

      * [Fields](account.html#tastytrade.account.TradingStatus-fields)
    - [tastytrade.account.Transaction](account.html#tastytrade.account.Transaction)

      * [Fields](account.html#tastytrade.account.Transaction-fields)
      * [Validators](account.html#tastytrade.account.Transaction-validators)
  + [tastytrade.backtest](backtesting.html)
  + [tastytrade.dxfeed](dxfeed.html)
  + [tastytrade.instruments](instruments.html)
  + [tastytrade.market\_sessions](market-sessions.html)
  + [tastytrade.metrics](metrics.html)
  + [tastytrade.order](order.html)
  + [tastytrade.search](search.html)
  + [tastytrade.session](session.html)
  + [tastytrade.streamer](streamer.html)
  + [tastytrade.utils](utils.html)
  + [tastytrade.watchlists](watchlists.html)

tastytrade.account

* [tastytrade.account.Account](account.html#tastytrade.account.Account)

  + [Fields](account.html#tastytrade.account.Account-fields)
  + [Ma\_delete\_complex\_order](account.html#tastytrade.account.Account.a_delete_complex_order)

    - [Parameters](account.html#tastytrade.account.Account.a_delete_complex_order-parameters)

      * [psession](account.html#tastytrade.account.Account.a_delete_complex_order.session)
      * [porder\_id](account.html#tastytrade.account.Account.a_delete_complex_order.order_id)
  + [Ma\_delete\_order](account.html#tastytrade.account.Account.a_delete_order)

    - [Parameters](account.html#tastytrade.account.Account.a_delete_order-parameters)

      * [psession](account.html#tastytrade.account.Account.a_delete_order.session)
      * [porder\_id](account.html#tastytrade.account.Account.a_delete_order.order_id)
  + [Ma\_get](account.html#tastytrade.account.Account.a_get)

    - [Parameters](account.html#tastytrade.account.Account.a_get-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get.session)
      * [pinclude\_closed](account.html#tastytrade.account.Account.a_get.include_closed)
  + [Ma\_get\_balance\_snapshots](account.html#tastytrade.account.Account.a_get_balance_snapshots)

    - [Parameters](account.html#tastytrade.account.Account.a_get_balance_snapshots-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_balance_snapshots.session)
      * [pcurrency](account.html#tastytrade.account.Account.a_get_balance_snapshots.currency)
      * [pstart\_date](account.html#tastytrade.account.Account.a_get_balance_snapshots.start_date)
      * [pend\_date](account.html#tastytrade.account.Account.a_get_balance_snapshots.end_date)
      * [psnapshot\_date](account.html#tastytrade.account.Account.a_get_balance_snapshots.snapshot_date)
      * [ptime\_of\_day](account.html#tastytrade.account.Account.a_get_balance_snapshots.time_of_day)
  + [Ma\_get\_balances](account.html#tastytrade.account.Account.a_get_balances)

    - [Parameters](account.html#tastytrade.account.Account.a_get_balances-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_balances.session)
  + [Ma\_get\_complex\_order](account.html#tastytrade.account.Account.a_get_complex_order)

    - [Parameters](account.html#tastytrade.account.Account.a_get_complex_order-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_complex_order.session)
      * [porder\_id](account.html#tastytrade.account.Account.a_get_complex_order.order_id)
  + [Ma\_get\_complex\_order\_history](account.html#tastytrade.account.Account.a_get_complex_order_history)

    - [Parameters](account.html#tastytrade.account.Account.a_get_complex_order_history-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_complex_order_history.session)
      * [pper\_page](account.html#tastytrade.account.Account.a_get_complex_order_history.per_page)
      * [ppage\_offset](account.html#tastytrade.account.Account.a_get_complex_order_history.page_offset)
  + [Ma\_get\_effective\_margin\_requirements](account.html#tastytrade.account.Account.a_get_effective_margin_requirements)

    - [Parameters](account.html#tastytrade.account.Account.a_get_effective_margin_requirements-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_effective_margin_requirements.session)
      * [psymbol](account.html#tastytrade.account.Account.a_get_effective_margin_requirements.symbol)
  + [Ma\_get\_history](account.html#tastytrade.account.Account.a_get_history)

    - [Parameters](account.html#tastytrade.account.Account.a_get_history-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_history.session)
      * [pper\_page](account.html#tastytrade.account.Account.a_get_history.per_page)
      * [ppage\_offset](account.html#tastytrade.account.Account.a_get_history.page_offset)
      * [psort](account.html#tastytrade.account.Account.a_get_history.sort)
      * [ptype](account.html#tastytrade.account.Account.a_get_history.type)
      * [ptypes](account.html#tastytrade.account.Account.a_get_history.types)
      * [psub\_types](account.html#tastytrade.account.Account.a_get_history.sub_types)
      * [pstart\_date](account.html#tastytrade.account.Account.a_get_history.start_date)
      * [pend\_date](account.html#tastytrade.account.Account.a_get_history.end_date)
      * [pinstrument\_type](account.html#tastytrade.account.Account.a_get_history.instrument_type)
      * [psymbol](account.html#tastytrade.account.Account.a_get_history.symbol)
      * [punderlying\_symbol](account.html#tastytrade.account.Account.a_get_history.underlying_symbol)
      * [paction](account.html#tastytrade.account.Account.a_get_history.action)
      * [ppartition\_key](account.html#tastytrade.account.Account.a_get_history.partition_key)
      * [pfutures\_symbol](account.html#tastytrade.account.Account.a_get_history.futures_symbol)
      * [pstart\_at](account.html#tastytrade.account.Account.a_get_history.start_at)
      * [pend\_at](account.html#tastytrade.account.Account.a_get_history.end_at)
  + [Ma\_get\_live\_complex\_orders](account.html#tastytrade.account.Account.a_get_live_complex_orders)

    - [Parameters](account.html#tastytrade.account.Account.a_get_live_complex_orders-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_live_complex_orders.session)
  + [Ma\_get\_live\_orders](account.html#tastytrade.account.Account.a_get_live_orders)

    - [Parameters](account.html#tastytrade.account.Account.a_get_live_orders-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_live_orders.session)
  + [Ma\_get\_margin\_requirements](account.html#tastytrade.account.Account.a_get_margin_requirements)

    - [Parameters](account.html#tastytrade.account.Account.a_get_margin_requirements-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_margin_requirements.session)
  + [Ma\_get\_net\_liquidating\_value\_history](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history)

    - [Parameters](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history.session)
      * [ptime\_back](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history.time_back)
      * [pstart\_time](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history.start_time)
  + [Ma\_get\_order](account.html#tastytrade.account.Account.a_get_order)

    - [Parameters](account.html#tastytrade.account.Account.a_get_order-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_order.session)
      * [porder\_id](account.html#tastytrade.account.Account.a_get_order.order_id)
  + [Ma\_get\_order\_chains](account.html#tastytrade.account.Account.a_get_order_chains)

    - [Parameters](account.html#tastytrade.account.Account.a_get_order_chains-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_order_chains.session)
      * [psymbol](account.html#tastytrade.account.Account.a_get_order_chains.symbol)
      * [pstart\_time](account.html#tastytrade.account.Account.a_get_order_chains.start_time)
      * [pend\_time](account.html#tastytrade.account.Account.a_get_order_chains.end_time)
  + [Ma\_get\_order\_history](account.html#tastytrade.account.Account.a_get_order_history)

    - [Parameters](account.html#tastytrade.account.Account.a_get_order_history-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_order_history.session)
      * [pper\_page](account.html#tastytrade.account.Account.a_get_order_history.per_page)
      * [ppage\_offset](account.html#tastytrade.account.Account.a_get_order_history.page_offset)
      * [pstart\_date](account.html#tastytrade.account.Account.a_get_order_history.start_date)
      * [pend\_date](account.html#tastytrade.account.Account.a_get_order_history.end_date)
      * [punderlying\_symbol](account.html#tastytrade.account.Account.a_get_order_history.underlying_symbol)
      * [pstatuses](account.html#tastytrade.account.Account.a_get_order_history.statuses)
      * [pfutures\_symbol](account.html#tastytrade.account.Account.a_get_order_history.futures_symbol)
      * [punderlying\_instrument\_type](account.html#tastytrade.account.Account.a_get_order_history.underlying_instrument_type)
      * [psort](account.html#tastytrade.account.Account.a_get_order_history.sort)
      * [pstart\_at](account.html#tastytrade.account.Account.a_get_order_history.start_at)
      * [pend\_at](account.html#tastytrade.account.Account.a_get_order_history.end_at)
  + [Ma\_get\_position\_limit](account.html#tastytrade.account.Account.a_get_position_limit)

    - [Parameters](account.html#tastytrade.account.Account.a_get_position_limit-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_position_limit.session)
  + [Ma\_get\_positions](account.html#tastytrade.account.Account.a_get_positions)

    - [Parameters](account.html#tastytrade.account.Account.a_get_positions-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_positions.session)
      * [punderlying\_symbols](account.html#tastytrade.account.Account.a_get_positions.underlying_symbols)
      * [psymbol](account.html#tastytrade.account.Account.a_get_positions.symbol)
      * [pinstrument\_type](account.html#tastytrade.account.Account.a_get_positions.instrument_type)
      * [pinclude\_closed](account.html#tastytrade.account.Account.a_get_positions.include_closed)
      * [punderlying\_product\_code](account.html#tastytrade.account.Account.a_get_positions.underlying_product_code)
      * [ppartition\_keys](account.html#tastytrade.account.Account.a_get_positions.partition_keys)
      * [pnet\_positions](account.html#tastytrade.account.Account.a_get_positions.net_positions)
      * [pinclude\_marks](account.html#tastytrade.account.Account.a_get_positions.include_marks)
  + [Ma\_get\_total\_fees](account.html#tastytrade.account.Account.a_get_total_fees)

    - [Parameters](account.html#tastytrade.account.Account.a_get_total_fees-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_total_fees.session)
      * [pday](account.html#tastytrade.account.Account.a_get_total_fees.day)
  + [Ma\_get\_trading\_status](account.html#tastytrade.account.Account.a_get_trading_status)

    - [Parameters](account.html#tastytrade.account.Account.a_get_trading_status-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_trading_status.session)
  + [Ma\_get\_transaction](account.html#tastytrade.account.Account.a_get_transaction)

    - [Parameters](account.html#tastytrade.account.Account.a_get_transaction-parameters)

      * [psession](account.html#tastytrade.account.Account.a_get_transaction.session)
      * [pid](account.html#tastytrade.account.Account.a_get_transaction.id)
  + [Ma\_place\_complex\_order](account.html#tastytrade.account.Account.a_place_complex_order)

    - [Parameters](account.html#tastytrade.account.Account.a_place_complex_order-parameters)

      * [psession](account.html#tastytrade.account.Account.a_place_complex_order.session)
      * [porder](account.html#tastytrade.account.Account.a_place_complex_order.order)
      * [pdry\_run](account.html#tastytrade.account.Account.a_place_complex_order.dry_run)
  + [Ma\_place\_order](account.html#tastytrade.account.Account.a_place_order)

    - [Parameters](account.html#tastytrade.account.Account.a_place_order-parameters)

      * [psession](account.html#tastytrade.account.Account.a_place_order.session)
      * [porder](account.html#tastytrade.account.Account.a_place_order.order)
      * [pdry\_run](account.html#tastytrade.account.Account.a_place_order.dry_run)
  + [Ma\_replace\_order](account.html#tastytrade.account.Account.a_replace_order)

    - [Parameters](account.html#tastytrade.account.Account.a_replace_order-parameters)

      * [psession](account.html#tastytrade.account.Account.a_replace_order.session)
      * [pold\_order\_id](account.html#tastytrade.account.Account.a_replace_order.old_order_id)
      * [pnew\_order](account.html#tastytrade.account.Account.a_replace_order.new_order)
  + [Mdelete\_complex\_order](account.html#tastytrade.account.Account.delete_complex_order)

    - [Parameters](account.html#tastytrade.account.Account.delete_complex_order-parameters)

      * [psession](account.html#tastytrade.account.Account.delete_complex_order.session)
      * [porder\_id](account.html#tastytrade.account.Account.delete_complex_order.order_id)
  + [Mdelete\_order](account.html#tastytrade.account.Account.delete_order)

    - [Parameters](account.html#tastytrade.account.Account.delete_order-parameters)

      * [psession](account.html#tastytrade.account.Account.delete_order.session)
      * [porder\_id](account.html#tastytrade.account.Account.delete_order.order_id)
  + [Mget](account.html#tastytrade.account.Account.get)

    - [Parameters](account.html#tastytrade.account.Account.get-parameters)

      * [psession](account.html#tastytrade.account.Account.get.session)
      * [pinclude\_closed](account.html#tastytrade.account.Account.get.include_closed)
    - [Returns](account.html#tastytrade.account.Account.get-returns)
  + [Mget\_balance\_snapshots](account.html#tastytrade.account.Account.get_balance_snapshots)

    - [Parameters](account.html#tastytrade.account.Account.get_balance_snapshots-parameters)

      * [psession](account.html#tastytrade.account.Account.get_balance_snapshots.session)
      * [pcurrency](account.html#tastytrade.account.Account.get_balance_snapshots.currency)
      * [pstart\_date](account.html#tastytrade.account.Account.get_balance_snapshots.start_date)
      * [pend\_date](account.html#tastytrade.account.Account.get_balance_snapshots.end_date)
      * [psnapshot\_date](account.html#tastytrade.account.Account.get_balance_snapshots.snapshot_date)
      * [ptime\_of\_day](account.html#tastytrade.account.Account.get_balance_snapshots.time_of_day)
  + [Mget\_balances](account.html#tastytrade.account.Account.get_balances)

    - [Parameters](account.html#tastytrade.account.Account.get_balances-parameters)

      * [psession](account.html#tastytrade.account.Account.get_balances.session)
  + [Mget\_complex\_order](account.html#tastytrade.account.Account.get_complex_order)

    - [Parameters](account.html#tastytrade.account.Account.get_complex_order-parameters)

      * [psession](account.html#tastytrade.account.Account.get_complex_order.session)
      * [porder\_id](account.html#tastytrade.account.Account.get_complex_order.order_id)
  + [Mget\_complex\_order\_history](account.html#tastytrade.account.Account.get_complex_order_history)

    - [Parameters](account.html#tastytrade.account.Account.get_complex_order_history-parameters)

      * [psession](account.html#tastytrade.account.Account.get_complex_order_history.session)
      * [pper\_page](account.html#tastytrade.account.Account.get_complex_order_history.per_page)
      * [ppage\_offset](account.html#tastytrade.account.Account.get_complex_order_history.page_offset)
  + [Mget\_effective\_margin\_requirements](account.html#tastytrade.account.Account.get_effective_margin_requirements)

    - [Parameters](account.html#tastytrade.account.Account.get_effective_margin_requirements-parameters)

      * [psession](account.html#tastytrade.account.Account.get_effective_margin_requirements.session)
      * [psymbol](account.html#tastytrade.account.Account.get_effective_margin_requirements.symbol)
  + [Mget\_history](account.html#tastytrade.account.Account.get_history)

    - [Parameters](account.html#tastytrade.account.Account.get_history-parameters)

      * [psession](account.html#tastytrade.account.Account.get_history.session)
      * [pper\_page](account.html#tastytrade.account.Account.get_history.per_page)
      * [ppage\_offset](account.html#tastytrade.account.Account.get_history.page_offset)
      * [psort](account.html#tastytrade.account.Account.get_history.sort)
      * [ptype](account.html#tastytrade.account.Account.get_history.type)
      * [ptypes](account.html#tastytrade.account.Account.get_history.types)
      * [psub\_types](account.html#tastytrade.account.Account.get_history.sub_types)
      * [pstart\_date](account.html#tastytrade.account.Account.get_history.start_date)
      * [pend\_date](account.html#tastytrade.account.Account.get_history.end_date)
      * [pinstrument\_type](account.html#tastytrade.account.Account.get_history.instrument_type)
      * [psymbol](account.html#tastytrade.account.Account.get_history.symbol)
      * [punderlying\_symbol](account.html#tastytrade.account.Account.get_history.underlying_symbol)
      * [paction](account.html#tastytrade.account.Account.get_history.action)
      * [ppartition\_key](account.html#tastytrade.account.Account.get_history.partition_key)
      * [pfutures\_symbol](account.html#tastytrade.account.Account.get_history.futures_symbol)
      * [pstart\_at](account.html#tastytrade.account.Account.get_history.start_at)
      * [pend\_at](account.html#tastytrade.account.Account.get_history.end_at)
  + [Mget\_live\_complex\_orders](account.html#tastytrade.account.Account.get_live_complex_orders)

    - [Parameters](account.html#tastytrade.account.Account.get_live_complex_orders-parameters)

      * [psession](account.html#tastytrade.account.Account.get_live_complex_orders.session)
  + [Mget\_live\_orders](account.html#tastytrade.account.Account.get_live_orders)

    - [Parameters](account.html#tastytrade.account.Account.get_live_orders-parameters)

      * [psession](account.html#tastytrade.account.Account.get_live_orders.session)
  + [Mget\_margin\_requirements](account.html#tastytrade.account.Account.get_margin_requirements)

    - [Parameters](account.html#tastytrade.account.Account.get_margin_requirements-parameters)

      * [psession](account.html#tastytrade.account.Account.get_margin_requirements.session)
  + [Mget\_net\_liquidating\_value\_history](account.html#tastytrade.account.Account.get_net_liquidating_value_history)

    - [Parameters](account.html#tastytrade.account.Account.get_net_liquidating_value_history-parameters)

      * [psession](account.html#tastytrade.account.Account.get_net_liquidating_value_history.session)
      * [ptime\_back](account.html#tastytrade.account.Account.get_net_liquidating_value_history.time_back)
      * [pstart\_time](account.html#tastytrade.account.Account.get_net_liquidating_value_history.start_time)
  + [Mget\_order](account.html#tastytrade.account.Account.get_order)

    - [Parameters](account.html#tastytrade.account.Account.get_order-parameters)

      * [psession](account.html#tastytrade.account.Account.get_order.session)
      * [porder\_id](account.html#tastytrade.account.Account.get_order.order_id)
  + [Mget\_order\_chains](account.html#tastytrade.account.Account.get_order_chains)

    - [Parameters](account.html#tastytrade.account.Account.get_order_chains-parameters)

      * [psession](account.html#tastytrade.account.Account.get_order_chains.session)
      * [psymbol](account.html#tastytrade.account.Account.get_order_chains.symbol)
      * [pstart\_time](account.html#tastytrade.account.Account.get_order_chains.start_time)
      * [pend\_time](account.html#tastytrade.account.Account.get_order_chains.end_time)
  + [Mget\_order\_history](account.html#tastytrade.account.Account.get_order_history)

    - [Parameters](account.html#tastytrade.account.Account.get_order_history-parameters)

      * [psession](account.html#tastytrade.account.Account.get_order_history.session)
      * [pper\_page](account.html#tastytrade.account.Account.get_order_history.per_page)
      * [ppage\_offset](account.html#tastytrade.account.Account.get_order_history.page_offset)
      * [pstart\_date](account.html#tastytrade.account.Account.get_order_history.start_date)
      * [pend\_date](account.html#tastytrade.account.Account.get_order_history.end_date)
      * [punderlying\_symbol](account.html#tastytrade.account.Account.get_order_history.underlying_symbol)
      * [pstatuses](account.html#tastytrade.account.Account.get_order_history.statuses)
      * [pfutures\_symbol](account.html#tastytrade.account.Account.get_order_history.futures_symbol)
      * [punderlying\_instrument\_type](account.html#tastytrade.account.Account.get_order_history.underlying_instrument_type)
      * [psort](account.html#tastytrade.account.Account.get_order_history.sort)
      * [pstart\_at](account.html#tastytrade.account.Account.get_order_history.start_at)
      * [pend\_at](account.html#tastytrade.account.Account.get_order_history.end_at)
  + [Mget\_position\_limit](account.html#tastytrade.account.Account.get_position_limit)

    - [Parameters](account.html#tastytrade.account.Account.get_position_limit-parameters)

      * [psession](account.html#tastytrade.account.Account.get_position_limit.session)
  + [Mget\_positions](account.html#tastytrade.account.Account.get_positions)

    - [Parameters](account.html#tastytrade.account.Account.get_positions-parameters)

      * [psession](account.html#tastytrade.account.Account.get_positions.session)
      * [punderlying\_symbols](account.html#tastytrade.account.Account.get_positions.underlying_symbols)
      * [psymbol](account.html#tastytrade.account.Account.get_positions.symbol)
      * [pinstrument\_type](account.html#tastytrade.account.Account.get_positions.instrument_type)
      * [pinclude\_closed](account.html#tastytrade.account.Account.get_positions.include_closed)
      * [punderlying\_product\_code](account.html#tastytrade.account.Account.get_positions.underlying_product_code)
      * [ppartition\_keys](account.html#tastytrade.account.Account.get_positions.partition_keys)
      * [pnet\_positions](account.html#tastytrade.account.Account.get_positions.net_positions)
      * [pinclude\_marks](account.html#tastytrade.account.Account.get_positions.include_marks)
  + [Mget\_total\_fees](account.html#tastytrade.account.Account.get_total_fees)

    - [Parameters](account.html#tastytrade.account.Account.get_total_fees-parameters)

      * [psession](account.html#tastytrade.account.Account.get_total_fees.session)
      * [pday](account.html#tastytrade.account.Account.get_total_fees.day)
  + [Mget\_trading\_status](account.html#tastytrade.account.Account.get_trading_status)

    - [Parameters](account.html#tastytrade.account.Account.get_trading_status-parameters)

      * [psession](account.html#tastytrade.account.Account.get_trading_status.session)
  + [Mget\_transaction](account.html#tastytrade.account.Account.get_transaction)

    - [Parameters](account.html#tastytrade.account.Account.get_transaction-parameters)

      * [psession](account.html#tastytrade.account.Account.get_transaction.session)
      * [pid](account.html#tastytrade.account.Account.get_transaction.id)
  + [Mplace\_complex\_order](account.html#tastytrade.account.Account.place_complex_order)

    - [Parameters](account.html#tastytrade.account.Account.place_complex_order-parameters)

      * [psession](account.html#tastytrade.account.Account.place_complex_order.session)
      * [porder](account.html#tastytrade.account.Account.place_complex_order.order)
      * [pdry\_run](account.html#tastytrade.account.Account.place_complex_order.dry_run)
  + [Mplace\_order](account.html#tastytrade.account.Account.place_order)

    - [Parameters](account.html#tastytrade.account.Account.place_order-parameters)

      * [psession](account.html#tastytrade.account.Account.place_order.session)
      * [porder](account.html#tastytrade.account.Account.place_order.order)
      * [pdry\_run](account.html#tastytrade.account.Account.place_order.dry_run)
  + [Mreplace\_order](account.html#tastytrade.account.Account.replace_order)

    - [Parameters](account.html#tastytrade.account.Account.replace_order-parameters)

      * [psession](account.html#tastytrade.account.Account.replace_order.session)
      * [pold\_order\_id](account.html#tastytrade.account.Account.replace_order.old_order_id)
      * [pnew\_order](account.html#tastytrade.account.Account.replace_order.new_order)
* [tastytrade.account.AccountBalance](account.html#tastytrade.account.AccountBalance)

  + [Fields](account.html#tastytrade.account.AccountBalance-fields)
  + [Validators](account.html#tastytrade.account.AccountBalance-validators)
* [tastytrade.account.AccountBalanceSnapshot](account.html#tastytrade.account.AccountBalanceSnapshot)

  + [Fields](account.html#tastytrade.account.AccountBalanceSnapshot-fields)
  + [Validators](account.html#tastytrade.account.AccountBalanceSnapshot-validators)
* [tastytrade.account.CurrentPosition](account.html#tastytrade.account.CurrentPosition)

  + [Fields](account.html#tastytrade.account.CurrentPosition-fields)
  + [Validators](account.html#tastytrade.account.CurrentPosition-validators)
* [tastytrade.account.EmptyDict](account.html#tastytrade.account.EmptyDict)
* [tastytrade.account.FeesInfo](account.html#tastytrade.account.FeesInfo)

  + [Fields](account.html#tastytrade.account.FeesInfo-fields)
  + [Validators](account.html#tastytrade.account.FeesInfo-validators)
* [tastytrade.account.Lot](account.html#tastytrade.account.Lot)

  + [Fields](account.html#tastytrade.account.Lot-fields)
* [tastytrade.account.MarginReport](account.html#tastytrade.account.MarginReport)

  + [Fields](account.html#tastytrade.account.MarginReport-fields)
  + [Validators](account.html#tastytrade.account.MarginReport-validators)
* [tastytrade.account.MarginReportEntry](account.html#tastytrade.account.MarginReportEntry)

  + [Fields](account.html#tastytrade.account.MarginReportEntry-fields)
  + [Validators](account.html#tastytrade.account.MarginReportEntry-validators)
* [tastytrade.account.MarginRequirement](account.html#tastytrade.account.MarginRequirement)

  + [Fields](account.html#tastytrade.account.MarginRequirement-fields)
* [tastytrade.account.NetLiqOhlc](account.html#tastytrade.account.NetLiqOhlc)

  + [Fields](account.html#tastytrade.account.NetLiqOhlc-fields)
* [tastytrade.account.PositionLimit](account.html#tastytrade.account.PositionLimit)

  + [Fields](account.html#tastytrade.account.PositionLimit-fields)
* [tastytrade.account.TradingStatus](account.html#tastytrade.account.TradingStatus)

  + [Fields](account.html#tastytrade.account.TradingStatus-fields)
* [tastytrade.account.Transaction](account.html#tastytrade.account.Transaction)

  + [Fields](account.html#tastytrade.account.Transaction-fields)
  + [Validators](account.html#tastytrade.account.Transaction-validators)

# tastytrade.account[¶](account.html#module-tastytrade.account "Link to this heading")

*pydantic model* tastytrade.account.Account(*\**, *[account\_number](account.html#tastytrade.account.Account "tastytrade.account.Account.account_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[opened\_at](account.html#tastytrade.account.Account "tastytrade.account.Account.opened_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[nickname](account.html#tastytrade.account.Account "tastytrade.account.Account.nickname (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[account\_type\_name](account.html#tastytrade.account.Account "tastytrade.account.Account.account_type_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[is\_closed](account.html#tastytrade.account.Account "tastytrade.account.Account.is_closed (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[day\_trader\_status](account.html#tastytrade.account.Account "tastytrade.account.Account.day_trader_status (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_firm\_error](account.html#tastytrade.account.Account "tastytrade.account.Account.is_firm_error (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_firm\_proprietary](account.html#tastytrade.account.Account "tastytrade.account.Account.is_firm_proprietary (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_futures\_approved](account.html#tastytrade.account.Account "tastytrade.account.Account.is_futures_approved (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_test\_drive](account.html#tastytrade.account.Account "tastytrade.account.Account.is_test_drive (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`*, *[margin\_or\_cash](account.html#tastytrade.account.Account "tastytrade.account.Account.margin_or_cash (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[is\_foreign](account.html#tastytrade.account.Account "tastytrade.account.Account.is_foreign (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[created\_at](account.html#tastytrade.account.Account "tastytrade.account.Account.created_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[external\_id](account.html#tastytrade.account.Account "tastytrade.account.Account.external_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[closed\_at](account.html#tastytrade.account.Account "tastytrade.account.Account.closed_at (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[funding\_date](account.html#tastytrade.account.Account "tastytrade.account.Account.funding_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[investment\_objective](account.html#tastytrade.account.Account "tastytrade.account.Account.investment_objective (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[liquidity\_needs](account.html#tastytrade.account.Account "tastytrade.account.Account.liquidity_needs (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[risk\_tolerance](account.html#tastytrade.account.Account "tastytrade.account.Account.risk_tolerance (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[investment\_time\_horizon](account.html#tastytrade.account.Account "tastytrade.account.Account.investment_time_horizon (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[futures\_account\_purpose](account.html#tastytrade.account.Account "tastytrade.account.Account.futures_account_purpose (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[external\_fdid](account.html#tastytrade.account.Account "tastytrade.account.Account.external_fdid (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[suitable\_options\_level](account.html#tastytrade.account.Account "tastytrade.account.Account.suitable_options_level (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[submitting\_user\_id](account.html#tastytrade.account.Account "tastytrade.account.Account.submitting_user_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](account.html#tastytrade.account.Account "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass that represents a Tastytrade account object, containing
    methods for retrieving information about the account, placing orders,
    and retrieving past transactions.

    Show JSON schema

    ```
    {
       "title": "Account",
       "description": "Dataclass that represents a Tastytrade account object, containing\nmethods for retrieving information about the account, placing orders,\nand retrieving past transactions.",
       "type": "object",
       "properties": {
          "account-number": {
             "title": "Account-Number",
             "type": "string"
          },
          "opened-at": {
             "format": "date-time",
             "title": "Opened-At",
             "type": "string"
          },
          "nickname": {
             "title": "Nickname",
             "type": "string"
          },
          "account-type-name": {
             "title": "Account-Type-Name",
             "type": "string"
          },
          "is-closed": {
             "title": "Is-Closed",
             "type": "boolean"
          },
          "day-trader-status": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "boolean"
                }
             ],
             "title": "Day-Trader-Status"
          },
          "is-firm-error": {
             "title": "Is-Firm-Error",
             "type": "boolean"
          },
          "is-firm-proprietary": {
             "title": "Is-Firm-Proprietary",
             "type": "boolean"
          },
          "is-futures-approved": {
             "title": "Is-Futures-Approved",
             "type": "boolean"
          },
          "is-test-drive": {
             "default": false,
             "title": "Is-Test-Drive",
             "type": "boolean"
          },
          "margin-or-cash": {
             "title": "Margin-Or-Cash",
             "type": "string"
          },
          "is-foreign": {
             "title": "Is-Foreign",
             "type": "boolean"
          },
          "created-at": {
             "format": "date-time",
             "title": "Created-At",
             "type": "string"
          },
          "external-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "External-Id"
          },
          "closed-at": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Closed-At"
          },
          "funding-date": {
             "anyOf": [
                {
                   "format": "date",
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Funding-Date"
          },
          "investment-objective": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Investment-Objective"
          },
          "liquidity-needs": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Liquidity-Needs"
          },
          "risk-tolerance": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Risk-Tolerance"
          },
          "investment-time-horizon": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Investment-Time-Horizon"
          },
          "futures-account-purpose": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Futures-Account-Purpose"
          },
          "external-fdid": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "External-Fdid"
          },
          "suitable-options-level": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Suitable-Options-Level"
          },
          "submitting-user-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Submitting-User-Id"
          }
       },
       "required": [
          "account-number",
          "opened-at",
          "nickname",
          "account-type-name",
          "is-closed",
          "day-trader-status",
          "is-firm-error",
          "is-firm-proprietary",
          "is-futures-approved",
          "margin-or-cash",
          "is-foreign",
          "created-at"
       ]
    }

    ```

    Fields:[¶](account.html#tastytrade.account.Account-fields "Permalink to this headline")
    :   * [`account_number (str)`](account.html#tastytrade.account.Account "tastytrade.account.Account.account_number (Python parameter)")
        * [`account_type_name (str)`](account.html#tastytrade.account.Account "tastytrade.account.Account.account_type_name (Python parameter)")
        * [`closed_at (str | None)`](account.html#tastytrade.account.Account "tastytrade.account.Account.closed_at (Python parameter)")
        * [`created_at (datetime.datetime)`](account.html#tastytrade.account.Account "tastytrade.account.Account.created_at (Python parameter)")
        * [`day_trader_status (str | bool)`](account.html#tastytrade.account.Account "tastytrade.account.Account.day_trader_status (Python parameter)")
        * [`external_fdid (str | None)`](account.html#tastytrade.account.Account "tastytrade.account.Account.external_fdid (Python parameter)")
        * [`external_id (str | None)`](account.html#tastytrade.account.Account "tastytrade.account.Account.external_id (Python parameter)")
        * [`funding_date (datetime.date | None)`](account.html#tastytrade.account.Account "tastytrade.account.Account.funding_date (Python parameter)")
        * [`futures_account_purpose (str | None)`](account.html#tastytrade.account.Account "tastytrade.account.Account.futures_account_purpose (Python parameter)")
        * [`investment_objective (str | None)`](account.html#tastytrade.account.Account "tastytrade.account.Account.investment_objective (Python parameter)")
        * [`investment_time_horizon (str | None)`](account.html#tastytrade.account.Account "tastytrade.account.Account.investment_time_horizon (Python parameter)")
        * [`is_closed (bool)`](account.html#tastytrade.account.Account "tastytrade.account.Account.is_closed (Python parameter)")
        * [`is_firm_error (bool)`](account.html#tastytrade.account.Account "tastytrade.account.Account.is_firm_error (Python parameter)")
        * [`is_firm_proprietary (bool)`](account.html#tastytrade.account.Account "tastytrade.account.Account.is_firm_proprietary (Python parameter)")
        * [`is_foreign (bool)`](account.html#tastytrade.account.Account "tastytrade.account.Account.is_foreign (Python parameter)")
        * [`is_futures_approved (bool)`](account.html#tastytrade.account.Account "tastytrade.account.Account.is_futures_approved (Python parameter)")
        * [`is_test_drive (bool)`](account.html#tastytrade.account.Account "tastytrade.account.Account.is_test_drive (Python parameter)")
        * [`liquidity_needs (str | None)`](account.html#tastytrade.account.Account "tastytrade.account.Account.liquidity_needs (Python parameter)")
        * [`margin_or_cash (str)`](account.html#tastytrade.account.Account "tastytrade.account.Account.margin_or_cash (Python parameter)")
        * [`nickname (str)`](account.html#tastytrade.account.Account "tastytrade.account.Account.nickname (Python parameter)")
        * [`opened_at (datetime.datetime)`](account.html#tastytrade.account.Account "tastytrade.account.Account.opened_at (Python parameter)")
        * [`risk_tolerance (str | None)`](account.html#tastytrade.account.Account "tastytrade.account.Account.risk_tolerance (Python parameter)")
        * [`submitting_user_id (str | None)`](account.html#tastytrade.account.Account "tastytrade.account.Account.submitting_user_id (Python parameter)")
        * [`suitable_options_level (str | None)`](account.html#tastytrade.account.Account "tastytrade.account.Account.suitable_options_level (Python parameter)")

    *async* a\_delete\_complex\_order(*[session](account.html#tastytrade.account.Account.a_delete_complex_order.session "tastytrade.account.Account.a_delete_complex_order.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[order\_id](account.html#tastytrade.account.Account.a_delete_complex_order.order_id "tastytrade.account.Account.a_delete_complex_order.order_id (Python parameter) — the ID of the order to delete."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.a_delete_complex_order "Link to this definition")
    :   Delete a complex order by ID.

        Parameters:[¶](account.html#tastytrade.account.Account.a_delete_complex_order-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_delete_complex_order.session "Permalink to this definition")
            :   the session to use for the request.

            order\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.a_delete_complex_order.order_id "Permalink to this definition")
            :   the ID of the order to delete.

    *async* a\_delete\_order(*[session](account.html#tastytrade.account.Account.a_delete_order.session "tastytrade.account.Account.a_delete_order.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[order\_id](account.html#tastytrade.account.Account.a_delete_order.order_id "tastytrade.account.Account.a_delete_order.order_id (Python parameter) — the ID of the order to delete."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.a_delete_order "Link to this definition")
    :   Delete an order by ID.

        Parameters:[¶](account.html#tastytrade.account.Account.a_delete_order-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_delete_order.session "Permalink to this definition")
            :   the session to use for the request.

            order\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.a_delete_order.order_id "Permalink to this definition")
            :   the ID of the order to delete.

    *async classmethod* a\_get(*[session](account.html#tastytrade.account.Account.a_get.session "tastytrade.account.Account.a_get.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *\**, *[include\_closed](account.html#tastytrade.account.Account.a_get.include_closed "tastytrade.account.Account.a_get.include_closed (Python parameter) — whether to include closed accounts in the results"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.13)")][¶](account.html#tastytrade.account.Account.a_get "Link to this definition")

    *async classmethod* a\_get(*[session](account.html#tastytrade.account.Account.a_get.session "tastytrade.account.Account.a_get.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[account\_number](account.html#tastytrade.account.Account.a_get.account_number "tastytrade.account.Account.a_get.account_number (Python parameter) — the account ID to get."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.13)")
    :   Gets all trading accounts associated with the Tastytrade user, or a specific
        one if given an account ID.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get.session "Permalink to this definition")
            :   the session to use for the request.

            account\_number: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")
            :   the account ID to get.

            include\_closed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`[¶](account.html#tastytrade.account.Account.a_get.include_closed "Permalink to this definition")
            :   whether to include closed accounts in the results

    *async* a\_get\_balance\_snapshots(*[session](account.html#tastytrade.account.Account.a_get_balance_snapshots.session "tastytrade.account.Account.a_get_balance_snapshots.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[per\_page](account.html#tastytrade.account.Account.a_get_balance_snapshots "tastytrade.account.Account.a_get_balance_snapshots.per_page (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `250`*, *[page\_offset](account.html#tastytrade.account.Account.a_get_balance_snapshots "tastytrade.account.Account.a_get_balance_snapshots.page_offset (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[currency](account.html#tastytrade.account.Account.a_get_balance_snapshots.currency "tastytrade.account.Account.a_get_balance_snapshots.currency (Python parameter) — the currency to show balances in."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `'USD'`*, *[end\_date](account.html#tastytrade.account.Account.a_get_balance_snapshots.end_date "tastytrade.account.Account.a_get_balance_snapshots.end_date (Python parameter) — the ending date of the range."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[start\_date](account.html#tastytrade.account.Account.a_get_balance_snapshots.start_date "tastytrade.account.Account.a_get_balance_snapshots.start_date (Python parameter) — the starting date of the range."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[snapshot\_date](account.html#tastytrade.account.Account.a_get_balance_snapshots.snapshot_date "tastytrade.account.Account.a_get_balance_snapshots.snapshot_date (Python parameter) — the date of the snapshot to get."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[time\_of\_day](account.html#tastytrade.account.Account.a_get_balance_snapshots.time_of_day "tastytrade.account.Account.a_get_balance_snapshots.time_of_day (Python parameter) — the time of day of the snapshots to get, either 'EOD' (End Of Day) or 'BOD' (Beginning Of Day)."): 'BOD' | 'EOD' = `'EOD'`*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[AccountBalanceSnapshot](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.a_get_balance_snapshots "Link to this definition")
    :   Returns a list of balance snapshots. This list will
        just have a few snapshots if you don’t pass a start
        date; otherwise, it will be each day’s balances in
        the given range.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_balance_snapshots-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_balance_snapshots.session "Permalink to this definition")
            :   the session to use for the request.

            currency: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `'USD'`[¶](account.html#tastytrade.account.Account.a_get_balance_snapshots.currency "Permalink to this definition")
            :   the currency to show balances in.

            start\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_balance_snapshots.start_date "Permalink to this definition")
            :   the starting date of the range.

            end\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_balance_snapshots.end_date "Permalink to this definition")
            :   the ending date of the range.

            snapshot\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_balance_snapshots.snapshot_date "Permalink to this definition")
            :   the date of the snapshot to get.

            time\_of\_day: 'BOD' | 'EOD' = `'EOD'`[¶](account.html#tastytrade.account.Account.a_get_balance_snapshots.time_of_day "Permalink to this definition")
            :   the time of day of the snapshots to get, either ‘EOD’ (End Of Day) or ‘BOD’ (Beginning Of Day).

    *async* a\_get\_balances(*[session](account.html#tastytrade.account.Account.a_get_balances.session "tastytrade.account.Account.a_get_balances.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [AccountBalance](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_get_balances "Link to this definition")
    :   Get the current balances of the account.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_balances-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_balances.session "Permalink to this definition")
            :   the session to use for the request.

    *async* a\_get\_complex\_order(*[session](account.html#tastytrade.account.Account.a_get_complex_order.session "tastytrade.account.Account.a_get_complex_order.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[order\_id](account.html#tastytrade.account.Account.a_get_complex_order.order_id "tastytrade.account.Account.a_get_complex_order.order_id (Python parameter) — the ID of the order to fetch."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*) → [PlacedComplexOrder](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_get_complex_order "Link to this definition")
    :   Gets a complex order with the given ID.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_complex_order-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_complex_order.session "Permalink to this definition")
            :   the session to use for the request.

            order\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.a_get_complex_order.order_id "Permalink to this definition")
            :   the ID of the order to fetch.

    *async* a\_get\_complex\_order\_history(*[session](account.html#tastytrade.account.Account.a_get_complex_order_history.session "tastytrade.account.Account.a_get_complex_order_history.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[per\_page](account.html#tastytrade.account.Account.a_get_complex_order_history.per_page "tastytrade.account.Account.a_get_complex_order_history.per_page (Python parameter) — the number of results to return per page."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `50`*, *[page\_offset](account.html#tastytrade.account.Account.a_get_complex_order_history.page_offset "tastytrade.account.Account.a_get_complex_order_history.page_offset (Python parameter) — provide a specific page to get; if not provided, get all pages"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[PlacedComplexOrder](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.a_get_complex_order_history "Link to this definition")
    :   Get order history of the account.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_complex_order_history-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_complex_order_history.session "Permalink to this definition")
            :   the session to use for the request.

            per\_page: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `50`[¶](account.html#tastytrade.account.Account.a_get_complex_order_history.per_page "Permalink to this definition")
            :   the number of results to return per page.

            page\_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_complex_order_history.page_offset "Permalink to this definition")
            :   provide a specific page to get; if not provided, get all pages

    *async* a\_get\_effective\_margin\_requirements(*[session](account.html#tastytrade.account.Account.a_get_effective_margin_requirements.session "tastytrade.account.Account.a_get_effective_margin_requirements.session (Python parameter) — the session to use for the request, can't be certification"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[symbol](account.html#tastytrade.account.Account.a_get_effective_margin_requirements.symbol "tastytrade.account.Account.a_get_effective_margin_requirements.symbol (Python parameter) — the symbol to get margin requirements for."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*) → [MarginRequirement](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_get_effective_margin_requirements "Link to this definition")
    :   Get the effective margin requirements for a given symbol.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_effective_margin_requirements-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_effective_margin_requirements.session "Permalink to this definition")
            :   the session to use for the request, can’t be certification

            symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.a_get_effective_margin_requirements.symbol "Permalink to this definition")
            :   the symbol to get margin requirements for.

    *async* a\_get\_history(*[session](account.html#tastytrade.account.Account.a_get_history.session "tastytrade.account.Account.a_get_history.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[per\_page](account.html#tastytrade.account.Account.a_get_history.per_page "tastytrade.account.Account.a_get_history.per_page (Python parameter) — the number of results to return per page."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `250`*, *[page\_offset](account.html#tastytrade.account.Account.a_get_history.page_offset "tastytrade.account.Account.a_get_history.page_offset (Python parameter) — provide a specific page to get; if not provided, get all pages"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[sort](account.html#tastytrade.account.Account.a_get_history.sort "tastytrade.account.Account.a_get_history.sort (Python parameter) — the order to sort results in, either 'Desc' or 'Asc'."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `'Desc'`*, *[type](account.html#tastytrade.account.Account.a_get_history.type "tastytrade.account.Account.a_get_history.type (Python parameter) — the type of transaction."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[types](account.html#tastytrade.account.Account.a_get_history.types "tastytrade.account.Account.a_get_history.types (Python parameter) — a list of transaction types to filter by."): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[sub\_types](account.html#tastytrade.account.Account.a_get_history.sub_types "tastytrade.account.Account.a_get_history.sub_types (Python parameter) — an array of transaction subtypes to filter by."): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[start\_date](account.html#tastytrade.account.Account.a_get_history.start_date "tastytrade.account.Account.a_get_history.start_date (Python parameter) — the start date of transactions to query."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[end\_date](account.html#tastytrade.account.Account.a_get_history.end_date "tastytrade.account.Account.a_get_history.end_date (Python parameter) — the end date of transactions to query."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[instrument\_type](account.html#tastytrade.account.Account.a_get_history.instrument_type "tastytrade.account.Account.a_get_history.instrument_type (Python parameter) — the type of instrument."): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[symbol](account.html#tastytrade.account.Account.a_get_history.symbol "tastytrade.account.Account.a_get_history.symbol (Python parameter) — a single symbol."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[underlying\_symbol](account.html#tastytrade.account.Account.a_get_history.underlying_symbol "tastytrade.account.Account.a_get_history.underlying_symbol (Python parameter) — the underlying symbol."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[action](account.html#tastytrade.account.Account.a_get_history.action "tastytrade.account.Account.a_get_history.action (Python parameter) — the action of the transaction: 'Sell to Open', 'Sell to Close', 'Buy to Open', 'Buy to Close', 'Sell' or 'Buy'."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[partition\_key](account.html#tastytrade.account.Account.a_get_history.partition_key "tastytrade.account.Account.a_get_history.partition_key (Python parameter) — account partition key."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[futures\_symbol](account.html#tastytrade.account.Account.a_get_history.futures_symbol "tastytrade.account.Account.a_get_history.futures_symbol (Python parameter) — the full TW Future Symbol, e.g."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[start\_at](account.html#tastytrade.account.Account.a_get_history.start_at "tastytrade.account.Account.a_get_history.start_at (Python parameter) — datetime start range for filtering transactions in full date-time."): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[end\_at](account.html#tastytrade.account.Account.a_get_history.end_at "tastytrade.account.Account.a_get_history.end_at (Python parameter) — datetime end range for filtering transactions in full date-time."): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[Transaction](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.a_get_history "Link to this definition")
    :   Get transaction history of the account.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_history-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_history.session "Permalink to this definition")
            :   the session to use for the request.

            per\_page: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `250`[¶](account.html#tastytrade.account.Account.a_get_history.per_page "Permalink to this definition")
            :   the number of results to return per page.

            page\_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_history.page_offset "Permalink to this definition")
            :   provide a specific page to get; if not provided, get all pages

            sort: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `'Desc'`[¶](account.html#tastytrade.account.Account.a_get_history.sort "Permalink to this definition")
            :   the order to sort results in, either ‘Desc’ or ‘Asc’.

            type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_history.type "Permalink to this definition")
            :   the type of transaction.

            types: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_history.types "Permalink to this definition")
            :   a list of transaction types to filter by.

            sub\_types: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_history.sub_types "Permalink to this definition")
            :   an array of transaction subtypes to filter by.

            start\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_history.start_date "Permalink to this definition")
            :   the start date of transactions to query.

            end\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_history.end_date "Permalink to this definition")
            :   the end date of transactions to query.

            instrument\_type: [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_history.instrument_type "Permalink to this definition")
            :   the type of instrument.

            symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_history.symbol "Permalink to this definition")
            :   a single symbol.

            underlying\_symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_history.underlying_symbol "Permalink to this definition")
            :   the underlying symbol.

            action: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_history.action "Permalink to this definition")
            :   the action of the transaction: ‘Sell to Open’, ‘Sell to Close’,
                ‘Buy to Open’, ‘Buy to Close’, ‘Sell’ or ‘Buy’.

            partition\_key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_history.partition_key "Permalink to this definition")
            :   account partition key.

            futures\_symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_history.futures_symbol "Permalink to this definition")
            :   the full TW Future Symbol, e.g. /ESZ9, /NGZ19.

            start\_at: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_history.start_at "Permalink to this definition")
            :   datetime start range for filtering transactions in full date-time.

            end\_at: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_history.end_at "Permalink to this definition")
            :   datetime end range for filtering transactions in full date-time.

    *async* a\_get\_live\_complex\_orders(*[session](account.html#tastytrade.account.Account.a_get_live_complex_orders.session "tastytrade.account.Account.a_get_live_complex_orders.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[PlacedComplexOrder](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.a_get_live_complex_orders "Link to this definition")
    :   Get complex orders placed today for the account.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_live_complex_orders-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_live_complex_orders.session "Permalink to this definition")
            :   the session to use for the request.

    *async* a\_get\_live\_orders(*[session](account.html#tastytrade.account.Account.a_get_live_orders.session "tastytrade.account.Account.a_get_live_orders.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[PlacedOrder](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.a_get_live_orders "Link to this definition")
    :   Get orders placed today for the account.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_live_orders-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_live_orders.session "Permalink to this definition")
            :   the session to use for the request.

    *async* a\_get\_margin\_requirements(*[session](account.html#tastytrade.account.Account.a_get_margin_requirements.session "tastytrade.account.Account.a_get_margin_requirements.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [MarginReport](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_get_margin_requirements "Link to this definition")
    :   Get the margin report for the account, with total margin requirements
        as well as a breakdown per symbol/instrument.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_margin_requirements-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_margin_requirements.session "Permalink to this definition")
            :   the session to use for the request.

    *async* a\_get\_net\_liquidating\_value\_history(*[session](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history.session "tastytrade.account.Account.a_get_net_liquidating_value_history.session (Python parameter) — the session to use for the request, can't be certification."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[time\_back](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history.time_back "tastytrade.account.Account.a_get_net_liquidating_value_history.time_back (Python parameter) — the time period to get net liquidating value snapshots for."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[start\_time](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history.start_time "tastytrade.account.Account.a_get_net_liquidating_value_history.start_time (Python parameter) — the start point for the query."): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[NetLiqOhlc](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history "Link to this definition")
    :   Returns a list of account net liquidating value snapshots over the
        specified time period.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history.session "Permalink to this definition")
            :   the session to use for the request, can’t be certification.

            time\_back: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history.time_back "Permalink to this definition")
            :   the time period to get net liquidating value snapshots for. This
                param is required if start\_time is not given. Possible values are:
                ‘1d’, ‘1m’, ‘3m’, ‘6m’, ‘1y’, ‘all’.

            start\_time: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_net_liquidating_value_history.start_time "Permalink to this definition")
            :   the start point for the query. This param is required is time-back
                is not given. If given, will take precedence over time-back.

    *async* a\_get\_order(*[session](account.html#tastytrade.account.Account.a_get_order.session "tastytrade.account.Account.a_get_order.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[order\_id](account.html#tastytrade.account.Account.a_get_order.order_id "tastytrade.account.Account.a_get_order.order_id (Python parameter) — the ID of the order to fetch."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*) → [PlacedOrder](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_get_order "Link to this definition")
    :   Gets an order with the given ID.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_order-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_order.session "Permalink to this definition")
            :   the session to use for the request.

            order\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.a_get_order.order_id "Permalink to this definition")
            :   the ID of the order to fetch.

    *async* a\_get\_order\_chains(*[session](account.html#tastytrade.account.Account.a_get_order_chains.session "tastytrade.account.Account.a_get_order_chains.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[symbol](account.html#tastytrade.account.Account.a_get_order_chains.symbol "tastytrade.account.Account.a_get_order_chains.symbol (Python parameter) — the underlying symbol for the chains."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[start\_time](account.html#tastytrade.account.Account.a_get_order_chains.start_time "tastytrade.account.Account.a_get_order_chains.start_time (Python parameter) — the beginning time of the query."): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[end\_time](account.html#tastytrade.account.Account.a_get_order_chains.end_time "tastytrade.account.Account.a_get_order_chains.end_time (Python parameter) — the ending time of the query."): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[OrderChain](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.a_get_order_chains "Link to this definition")
    :   Get a list of order chains (open + rolls + close) for given symbol
        over the given time frame, with total P/L, commissions, etc.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_order_chains-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_order_chains.session "Permalink to this definition")
            :   the session to use for the request.

            symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.a_get_order_chains.symbol "Permalink to this definition")
            :   the underlying symbol for the chains.

            start\_time: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.a_get_order_chains.start_time "Permalink to this definition")
            :   the beginning time of the query.

            end\_time: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.a_get_order_chains.end_time "Permalink to this definition")
            :   the ending time of the query.

    *async* a\_get\_order\_history(*[session](account.html#tastytrade.account.Account.a_get_order_history.session "tastytrade.account.Account.a_get_order_history.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[per\_page](account.html#tastytrade.account.Account.a_get_order_history.per_page "tastytrade.account.Account.a_get_order_history.per_page (Python parameter) — the number of results to return per page."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `50`*, *[page\_offset](account.html#tastytrade.account.Account.a_get_order_history.page_offset "tastytrade.account.Account.a_get_order_history.page_offset (Python parameter) — provide a specific page to get; if not provided, get all pages"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[start\_date](account.html#tastytrade.account.Account.a_get_order_history.start_date "tastytrade.account.Account.a_get_order_history.start_date (Python parameter) — the start date of orders to query."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[end\_date](account.html#tastytrade.account.Account.a_get_order_history.end_date "tastytrade.account.Account.a_get_order_history.end_date (Python parameter) — the end date of orders to query."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[underlying\_symbol](account.html#tastytrade.account.Account.a_get_order_history.underlying_symbol "tastytrade.account.Account.a_get_order_history.underlying_symbol (Python parameter) — underlying symbol to filter by."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[statuses](account.html#tastytrade.account.Account.a_get_order_history.statuses "tastytrade.account.Account.a_get_order_history.statuses (Python parameter) — a list of statuses to filter by."): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[OrderStatus](order.html#tastytrade.order.OrderStatus "tastytrade.order.OrderStatus (Python enum) — Bases: str, Enum")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[futures\_symbol](account.html#tastytrade.account.Account.a_get_order_history.futures_symbol "tastytrade.account.Account.a_get_order_history.futures_symbol (Python parameter) — Tastytrade future symbol for futures and future options."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[underlying\_instrument\_type](account.html#tastytrade.account.Account.a_get_order_history.underlying_instrument_type "tastytrade.account.Account.a_get_order_history.underlying_instrument_type (Python parameter) — the type of instrument to filter by"): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[sort](account.html#tastytrade.account.Account.a_get_order_history.sort "tastytrade.account.Account.a_get_order_history.sort (Python parameter) — the order to sort results in, either 'Desc' or 'Asc'."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[start\_at](account.html#tastytrade.account.Account.a_get_order_history.start_at "tastytrade.account.Account.a_get_order_history.start_at (Python parameter) — datetime start range for filtering transactions in full date-time."): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[end\_at](account.html#tastytrade.account.Account.a_get_order_history.end_at "tastytrade.account.Account.a_get_order_history.end_at (Python parameter) — datetime end range for filtering transactions in full date-time."): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[PlacedOrder](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.a_get_order_history "Link to this definition")
    :   Get order history of the account.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_order_history-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_order_history.session "Permalink to this definition")
            :   the session to use for the request.

            per\_page: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `50`[¶](account.html#tastytrade.account.Account.a_get_order_history.per_page "Permalink to this definition")
            :   the number of results to return per page.

            page\_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_order_history.page_offset "Permalink to this definition")
            :   provide a specific page to get; if not provided, get all pages

            start\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_order_history.start_date "Permalink to this definition")
            :   the start date of orders to query.

            end\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_order_history.end_date "Permalink to this definition")
            :   the end date of orders to query.

            underlying\_symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_order_history.underlying_symbol "Permalink to this definition")
            :   underlying symbol to filter by.

            statuses: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[OrderStatus](order.html#tastytrade.order.OrderStatus "tastytrade.order.OrderStatus (Python enum) — Bases: str, Enum")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_order_history.statuses "Permalink to this definition")
            :   a list of statuses to filter by.

            futures\_symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_order_history.futures_symbol "Permalink to this definition")
            :   Tastytrade future symbol for futures and future options.

            underlying\_instrument\_type: [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_order_history.underlying_instrument_type "Permalink to this definition")
            :   the type of instrument to filter by

            sort: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_order_history.sort "Permalink to this definition")
            :   the order to sort results in, either ‘Desc’ or ‘Asc’.

            start\_at: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_order_history.start_at "Permalink to this definition")
            :   datetime start range for filtering transactions in full date-time.

            end\_at: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_order_history.end_at "Permalink to this definition")
            :   datetime end range for filtering transactions in full date-time.

    *async* a\_get\_position\_limit(*[session](account.html#tastytrade.account.Account.a_get_position_limit.session "tastytrade.account.Account.a_get_position_limit.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [PositionLimit](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_get_position_limit "Link to this definition")
    :   Get the maximum order size information for the account.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_position_limit-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_position_limit.session "Permalink to this definition")
            :   the session to use for the request.

    *async* a\_get\_positions(*[session](account.html#tastytrade.account.Account.a_get_positions.session "tastytrade.account.Account.a_get_positions.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[underlying\_symbols](account.html#tastytrade.account.Account.a_get_positions.underlying_symbols "tastytrade.account.Account.a_get_positions.underlying_symbols (Python parameter) — an array of underlying symbols for positions."): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[symbol](account.html#tastytrade.account.Account.a_get_positions.symbol "tastytrade.account.Account.a_get_positions.symbol (Python parameter) — a single symbol."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[instrument\_type](account.html#tastytrade.account.Account.a_get_positions.instrument_type "tastytrade.account.Account.a_get_positions.instrument_type (Python parameter) — the type of instrument."): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[include\_closed](account.html#tastytrade.account.Account.a_get_positions.include_closed "tastytrade.account.Account.a_get_positions.include_closed (Python parameter) — if closed positions should be included in the query."): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[underlying\_product\_code](account.html#tastytrade.account.Account.a_get_positions.underlying_product_code "tastytrade.account.Account.a_get_positions.underlying_product_code (Python parameter) — the underlying future's product code."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[partition\_keys](account.html#tastytrade.account.Account.a_get_positions.partition_keys "tastytrade.account.Account.a_get_positions.partition_keys (Python parameter) — account partition keys."): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[net\_positions](account.html#tastytrade.account.Account.a_get_positions.net_positions "tastytrade.account.Account.a_get_positions.net_positions (Python parameter) — returns net positions grouped by instrument type and symbol."): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[include\_marks](account.html#tastytrade.account.Account.a_get_positions.include_marks "tastytrade.account.Account.a_get_positions.include_marks (Python parameter) — include current quote mark (note: can decrease performance)."): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[CurrentPosition](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.a_get_positions "Link to this definition")
    :   Get the current positions of the account.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_positions-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_positions.session "Permalink to this definition")
            :   the session to use for the request.

            underlying\_symbols: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_positions.underlying_symbols "Permalink to this definition")
            :   an array of underlying symbols for positions.

            symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_positions.symbol "Permalink to this definition")
            :   a single symbol.

            instrument\_type: [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_positions.instrument_type "Permalink to this definition")
            :   the type of instrument.

            include\_closed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_positions.include_closed "Permalink to this definition")
            :   if closed positions should be included in the query.

            underlying\_product\_code: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_positions.underlying_product_code "Permalink to this definition")
            :   the underlying future’s product code.

            partition\_keys: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_positions.partition_keys "Permalink to this definition")
            :   account partition keys.

            net\_positions: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_positions.net_positions "Permalink to this definition")
            :   returns net positions grouped by instrument type and symbol.

            include\_marks: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_positions.include_marks "Permalink to this definition")
            :   include current quote mark (note: can decrease performance).

    *async* a\_get\_total\_fees(*[session](account.html#tastytrade.account.Account.a_get_total_fees.session "tastytrade.account.Account.a_get_total_fees.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[day](account.html#tastytrade.account.Account.a_get_total_fees.day "tastytrade.account.Account.a_get_total_fees.day (Python parameter) — the date to get fees for."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*) → [FeesInfo](account.html#tastytrade.account.FeesInfo "tastytrade.account.FeesInfo (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_get_total_fees "Link to this definition")
    :   Get the total fees for a given date.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_total_fees-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_total_fees.session "Permalink to this definition")
            :   the session to use for the request.

            day: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.a_get_total_fees.day "Permalink to this definition")
            :   the date to get fees for.

    *async* a\_get\_trading\_status(*[session](account.html#tastytrade.account.Account.a_get_trading_status.session "tastytrade.account.Account.a_get_trading_status.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [TradingStatus](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_get_trading_status "Link to this definition")
    :   Get the trading status of the account.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_trading_status-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_trading_status.session "Permalink to this definition")
            :   the session to use for the request.

    *async* a\_get\_transaction(*[session](account.html#tastytrade.account.Account.a_get_transaction.session "tastytrade.account.Account.a_get_transaction.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[id](account.html#tastytrade.account.Account.a_get_transaction.id "tastytrade.account.Account.a_get_transaction.id (Python parameter) — the ID of the transaction to fetch."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*) → [Transaction](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_get_transaction "Link to this definition")
    :   Get a single transaction by ID.

        Parameters:[¶](account.html#tastytrade.account.Account.a_get_transaction-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_get_transaction.session "Permalink to this definition")
            :   the session to use for the request.

            id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.a_get_transaction.id "Permalink to this definition")
            :   the ID of the transaction to fetch.

    *async* a\_place\_complex\_order(*[session](account.html#tastytrade.account.Account.a_place_complex_order.session "tastytrade.account.Account.a_place_complex_order.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[order](account.html#tastytrade.account.Account.a_place_complex_order.order "tastytrade.account.Account.a_place_complex_order.order (Python parameter) — the order to place."): [NewComplexOrder](order.html#tastytrade.order.NewComplexOrder "tastytrade.order.NewComplexOrder (Python model) — Bases: TastytradeData")*, *[dry\_run](account.html#tastytrade.account.Account.a_place_complex_order.dry_run "tastytrade.account.Account.a_place_complex_order.dry_run (Python parameter) — whether this is a test order or not."): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `True`*) → [PlacedComplexOrderResponse](order.html#tastytrade.order.PlacedComplexOrderResponse "tastytrade.order.PlacedComplexOrderResponse (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_place_complex_order "Link to this definition")
    :   Place the given order.

        Parameters:[¶](account.html#tastytrade.account.Account.a_place_complex_order-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_place_complex_order.session "Permalink to this definition")
            :   the session to use for the request.

            order: [NewComplexOrder](order.html#tastytrade.order.NewComplexOrder "tastytrade.order.NewComplexOrder (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_place_complex_order.order "Permalink to this definition")
            :   the order to place.

            dry\_run: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `True`[¶](account.html#tastytrade.account.Account.a_place_complex_order.dry_run "Permalink to this definition")
            :   whether this is a test order or not.

    *async* a\_place\_order(*[session](account.html#tastytrade.account.Account.a_place_order.session "tastytrade.account.Account.a_place_order.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[order](account.html#tastytrade.account.Account.a_place_order.order "tastytrade.account.Account.a_place_order.order (Python parameter) — the order to place."): [NewOrder](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder (Python model) — Bases: TastytradeData")*, *[dry\_run](account.html#tastytrade.account.Account.a_place_order.dry_run "tastytrade.account.Account.a_place_order.dry_run (Python parameter) — whether this is a test order or not."): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `True`*) → [PlacedOrderResponse](order.html#tastytrade.order.PlacedOrderResponse "tastytrade.order.PlacedOrderResponse (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_place_order "Link to this definition")
    :   Place the given order.

        Parameters:[¶](account.html#tastytrade.account.Account.a_place_order-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_place_order.session "Permalink to this definition")
            :   the session to use for the request.

            order: [NewOrder](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_place_order.order "Permalink to this definition")
            :   the order to place.

            dry\_run: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `True`[¶](account.html#tastytrade.account.Account.a_place_order.dry_run "Permalink to this definition")
            :   whether this is a test order or not.

    *async* a\_replace\_order(*[session](account.html#tastytrade.account.Account.a_replace_order.session "tastytrade.account.Account.a_replace_order.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[old\_order\_id](account.html#tastytrade.account.Account.a_replace_order.old_order_id "tastytrade.account.Account.a_replace_order.old_order_id (Python parameter) — the ID of the order to replace."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[new\_order](account.html#tastytrade.account.Account.a_replace_order.new_order "tastytrade.account.Account.a_replace_order.new_order (Python parameter) — the new order to replace the old order with."): [NewOrder](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder (Python model) — Bases: TastytradeData")*) → [PlacedOrder](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_replace_order "Link to this definition")
    :   Replace an order with a new order with different characteristics (but
        same legs).

        Parameters:[¶](account.html#tastytrade.account.Account.a_replace_order-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.a_replace_order.session "Permalink to this definition")
            :   the session to use for the request.

            old\_order\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.a_replace_order.old_order_id "Permalink to this definition")
            :   the ID of the order to replace.

            new\_order: [NewOrder](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.a_replace_order.new_order "Permalink to this definition")
            :   the new order to replace the old order with.

    delete\_complex\_order(*[session](account.html#tastytrade.account.Account.delete_complex_order.session "tastytrade.account.Account.delete_complex_order.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[order\_id](account.html#tastytrade.account.Account.delete_complex_order.order_id "tastytrade.account.Account.delete_complex_order.order_id (Python parameter) — the ID of the order to delete."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.delete_complex_order "Link to this definition")
    :   Delete a complex order by ID.

        Parameters:[¶](account.html#tastytrade.account.Account.delete_complex_order-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.delete_complex_order.session "Permalink to this definition")
            :   the session to use for the request.

            order\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.delete_complex_order.order_id "Permalink to this definition")
            :   the ID of the order to delete.

    delete\_order(*[session](account.html#tastytrade.account.Account.delete_order.session "tastytrade.account.Account.delete_order.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[order\_id](account.html#tastytrade.account.Account.delete_order.order_id "tastytrade.account.Account.delete_order.order_id (Python parameter) — the ID of the order to delete."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.delete_order "Link to this definition")
    :   Delete an order by ID.

        Parameters:[¶](account.html#tastytrade.account.Account.delete_order-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.delete_order.session "Permalink to this definition")
            :   the session to use for the request.

            order\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.delete_order.order_id "Permalink to this definition")
            :   the ID of the order to delete.

    *classmethod* get(*[session](account.html#tastytrade.account.Account.get.session "tastytrade.account.Account.get.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *\**, *[include\_closed](account.html#tastytrade.account.Account.get.include_closed "tastytrade.account.Account.get.include_closed (Python parameter) — whether to include closed accounts in the results"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.13)")][¶](account.html#tastytrade.account.Account.get "Link to this definition")

    *classmethod* get(*[session](account.html#tastytrade.account.Account.get.session "tastytrade.account.Account.get.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[account\_number](account.html#tastytrade.account.Account.get.account_number "tastytrade.account.Account.get.account_number (Python parameter) — the account ID to get."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.13)")
    :   Gets all trading accounts associated with the Tastytrade user, or a specific
        one if given an account ID.

        Parameters:[¶](account.html#tastytrade.account.Account.get-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get.session "Permalink to this definition")
            :   the session to use for the request.

            account\_number: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")
            :   the account ID to get.

            include\_closed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`[¶](account.html#tastytrade.account.Account.get.include_closed "Permalink to this definition")
            :   whether to include closed accounts in the results

        Returns:[¶](account.html#tastytrade.account.Account.get-returns "Permalink to this headline")
        :   an account if an ID was provided; otherwise, a single account.

    get\_balance\_snapshots(*[session](account.html#tastytrade.account.Account.get_balance_snapshots.session "tastytrade.account.Account.get_balance_snapshots.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[per\_page](account.html#tastytrade.account.Account.get_balance_snapshots "tastytrade.account.Account.get_balance_snapshots.per_page (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `250`*, *[page\_offset](account.html#tastytrade.account.Account.get_balance_snapshots "tastytrade.account.Account.get_balance_snapshots.page_offset (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[currency](account.html#tastytrade.account.Account.get_balance_snapshots.currency "tastytrade.account.Account.get_balance_snapshots.currency (Python parameter) — the currency to show balances in."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `'USD'`*, *[end\_date](account.html#tastytrade.account.Account.get_balance_snapshots.end_date "tastytrade.account.Account.get_balance_snapshots.end_date (Python parameter) — the ending date of the range."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[start\_date](account.html#tastytrade.account.Account.get_balance_snapshots.start_date "tastytrade.account.Account.get_balance_snapshots.start_date (Python parameter) — the starting date of the range."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[snapshot\_date](account.html#tastytrade.account.Account.get_balance_snapshots.snapshot_date "tastytrade.account.Account.get_balance_snapshots.snapshot_date (Python parameter) — the date of the snapshot to get."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[time\_of\_day](account.html#tastytrade.account.Account.get_balance_snapshots.time_of_day "tastytrade.account.Account.get_balance_snapshots.time_of_day (Python parameter) — the time of day of the snapshots to get, either 'EOD' (End Of Day) or 'BOD' (Beginning Of Day)."): 'BOD' | 'EOD' = `'EOD'`*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[AccountBalanceSnapshot](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.get_balance_snapshots "Link to this definition")
    :   Returns a list of balance snapshots. This list will
        just have a few snapshots if you don’t pass a start
        date; otherwise, it will be each day’s balances in
        the given range.

        Parameters:[¶](account.html#tastytrade.account.Account.get_balance_snapshots-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_balance_snapshots.session "Permalink to this definition")
            :   the session to use for the request.

            currency: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `'USD'`[¶](account.html#tastytrade.account.Account.get_balance_snapshots.currency "Permalink to this definition")
            :   the currency to show balances in.

            start\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_balance_snapshots.start_date "Permalink to this definition")
            :   the starting date of the range.

            end\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_balance_snapshots.end_date "Permalink to this definition")
            :   the ending date of the range.

            snapshot\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_balance_snapshots.snapshot_date "Permalink to this definition")
            :   the date of the snapshot to get.

            time\_of\_day: 'BOD' | 'EOD' = `'EOD'`[¶](account.html#tastytrade.account.Account.get_balance_snapshots.time_of_day "Permalink to this definition")
            :   the time of day of the snapshots to get, either ‘EOD’ (End Of Day) or ‘BOD’ (Beginning Of Day).

    get\_balances(*[session](account.html#tastytrade.account.Account.get_balances.session "tastytrade.account.Account.get_balances.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [AccountBalance](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.get_balances "Link to this definition")
    :   Get the current balances of the account.

        Parameters:[¶](account.html#tastytrade.account.Account.get_balances-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_balances.session "Permalink to this definition")
            :   the session to use for the request.

    get\_complex\_order(*[session](account.html#tastytrade.account.Account.get_complex_order.session "tastytrade.account.Account.get_complex_order.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[order\_id](account.html#tastytrade.account.Account.get_complex_order.order_id "tastytrade.account.Account.get_complex_order.order_id (Python parameter) — the ID of the order to fetch."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*) → [PlacedComplexOrder](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.get_complex_order "Link to this definition")
    :   Gets a complex order with the given ID.

        Parameters:[¶](account.html#tastytrade.account.Account.get_complex_order-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_complex_order.session "Permalink to this definition")
            :   the session to use for the request.

            order\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.get_complex_order.order_id "Permalink to this definition")
            :   the ID of the order to fetch.

    get\_complex\_order\_history(*[session](account.html#tastytrade.account.Account.get_complex_order_history.session "tastytrade.account.Account.get_complex_order_history.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[per\_page](account.html#tastytrade.account.Account.get_complex_order_history.per_page "tastytrade.account.Account.get_complex_order_history.per_page (Python parameter) — the number of results to return per page."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `50`*, *[page\_offset](account.html#tastytrade.account.Account.get_complex_order_history.page_offset "tastytrade.account.Account.get_complex_order_history.page_offset (Python parameter) — provide a specific page to get; if not provided, get all pages"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[PlacedComplexOrder](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.get_complex_order_history "Link to this definition")
    :   Get order history of the account.

        Parameters:[¶](account.html#tastytrade.account.Account.get_complex_order_history-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_complex_order_history.session "Permalink to this definition")
            :   the session to use for the request.

            per\_page: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `50`[¶](account.html#tastytrade.account.Account.get_complex_order_history.per_page "Permalink to this definition")
            :   the number of results to return per page.

            page\_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_complex_order_history.page_offset "Permalink to this definition")
            :   provide a specific page to get; if not provided, get all pages

    get\_effective\_margin\_requirements(*[session](account.html#tastytrade.account.Account.get_effective_margin_requirements.session "tastytrade.account.Account.get_effective_margin_requirements.session (Python parameter) — the session to use for the request, can't be certification"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[symbol](account.html#tastytrade.account.Account.get_effective_margin_requirements.symbol "tastytrade.account.Account.get_effective_margin_requirements.symbol (Python parameter) — the symbol to get margin requirements for."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*) → [MarginRequirement](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.get_effective_margin_requirements "Link to this definition")
    :   Get the effective margin requirements for a given symbol.

        Parameters:[¶](account.html#tastytrade.account.Account.get_effective_margin_requirements-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_effective_margin_requirements.session "Permalink to this definition")
            :   the session to use for the request, can’t be certification

            symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.get_effective_margin_requirements.symbol "Permalink to this definition")
            :   the symbol to get margin requirements for.

    get\_history(*[session](account.html#tastytrade.account.Account.get_history.session "tastytrade.account.Account.get_history.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[per\_page](account.html#tastytrade.account.Account.get_history.per_page "tastytrade.account.Account.get_history.per_page (Python parameter) — the number of results to return per page."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `250`*, *[page\_offset](account.html#tastytrade.account.Account.get_history.page_offset "tastytrade.account.Account.get_history.page_offset (Python parameter) — provide a specific page to get; if not provided, get all pages"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[sort](account.html#tastytrade.account.Account.get_history.sort "tastytrade.account.Account.get_history.sort (Python parameter) — the order to sort results in, either 'Desc' or 'Asc'."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `'Desc'`*, *[type](account.html#tastytrade.account.Account.get_history.type "tastytrade.account.Account.get_history.type (Python parameter) — the type of transaction."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[types](account.html#tastytrade.account.Account.get_history.types "tastytrade.account.Account.get_history.types (Python parameter) — a list of transaction types to filter by."): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[sub\_types](account.html#tastytrade.account.Account.get_history.sub_types "tastytrade.account.Account.get_history.sub_types (Python parameter) — an array of transaction subtypes to filter by."): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[start\_date](account.html#tastytrade.account.Account.get_history.start_date "tastytrade.account.Account.get_history.start_date (Python parameter) — the start date of transactions to query."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[end\_date](account.html#tastytrade.account.Account.get_history.end_date "tastytrade.account.Account.get_history.end_date (Python parameter) — the end date of transactions to query."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[instrument\_type](account.html#tastytrade.account.Account.get_history.instrument_type "tastytrade.account.Account.get_history.instrument_type (Python parameter) — the type of instrument."): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[symbol](account.html#tastytrade.account.Account.get_history.symbol "tastytrade.account.Account.get_history.symbol (Python parameter) — a single symbol."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[underlying\_symbol](account.html#tastytrade.account.Account.get_history.underlying_symbol "tastytrade.account.Account.get_history.underlying_symbol (Python parameter) — the underlying symbol."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[action](account.html#tastytrade.account.Account.get_history.action "tastytrade.account.Account.get_history.action (Python parameter) — the action of the transaction: 'Sell to Open', 'Sell to Close', 'Buy to Open', 'Buy to Close', 'Sell' or 'Buy'."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[partition\_key](account.html#tastytrade.account.Account.get_history.partition_key "tastytrade.account.Account.get_history.partition_key (Python parameter) — account partition key."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[futures\_symbol](account.html#tastytrade.account.Account.get_history.futures_symbol "tastytrade.account.Account.get_history.futures_symbol (Python parameter) — the full TW Future Symbol, e.g."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[start\_at](account.html#tastytrade.account.Account.get_history.start_at "tastytrade.account.Account.get_history.start_at (Python parameter) — datetime start range for filtering transactions in full date-time."): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[end\_at](account.html#tastytrade.account.Account.get_history.end_at "tastytrade.account.Account.get_history.end_at (Python parameter) — datetime end range for filtering transactions in full date-time."): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[Transaction](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.get_history "Link to this definition")
    :   Get transaction history of the account.

        Parameters:[¶](account.html#tastytrade.account.Account.get_history-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_history.session "Permalink to this definition")
            :   the session to use for the request.

            per\_page: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `250`[¶](account.html#tastytrade.account.Account.get_history.per_page "Permalink to this definition")
            :   the number of results to return per page.

            page\_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_history.page_offset "Permalink to this definition")
            :   provide a specific page to get; if not provided, get all pages

            sort: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `'Desc'`[¶](account.html#tastytrade.account.Account.get_history.sort "Permalink to this definition")
            :   the order to sort results in, either ‘Desc’ or ‘Asc’.

            type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_history.type "Permalink to this definition")
            :   the type of transaction.

            types: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_history.types "Permalink to this definition")
            :   a list of transaction types to filter by.

            sub\_types: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_history.sub_types "Permalink to this definition")
            :   an array of transaction subtypes to filter by.

            start\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_history.start_date "Permalink to this definition")
            :   the start date of transactions to query.

            end\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_history.end_date "Permalink to this definition")
            :   the end date of transactions to query.

            instrument\_type: [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_history.instrument_type "Permalink to this definition")
            :   the type of instrument.

            symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_history.symbol "Permalink to this definition")
            :   a single symbol.

            underlying\_symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_history.underlying_symbol "Permalink to this definition")
            :   the underlying symbol.

            action: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_history.action "Permalink to this definition")
            :   the action of the transaction: ‘Sell to Open’, ‘Sell to Close’,
                ‘Buy to Open’, ‘Buy to Close’, ‘Sell’ or ‘Buy’.

            partition\_key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_history.partition_key "Permalink to this definition")
            :   account partition key.

            futures\_symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_history.futures_symbol "Permalink to this definition")
            :   the full TW Future Symbol, e.g. /ESZ9, /NGZ19.

            start\_at: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_history.start_at "Permalink to this definition")
            :   datetime start range for filtering transactions in full date-time.

            end\_at: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_history.end_at "Permalink to this definition")
            :   datetime end range for filtering transactions in full date-time.

    get\_live\_complex\_orders(*[session](account.html#tastytrade.account.Account.get_live_complex_orders.session "tastytrade.account.Account.get_live_complex_orders.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[PlacedComplexOrder](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.get_live_complex_orders "Link to this definition")
    :   Get complex orders placed today for the account.

        Parameters:[¶](account.html#tastytrade.account.Account.get_live_complex_orders-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_live_complex_orders.session "Permalink to this definition")
            :   the session to use for the request.

    get\_live\_orders(*[session](account.html#tastytrade.account.Account.get_live_orders.session "tastytrade.account.Account.get_live_orders.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[PlacedOrder](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.get_live_orders "Link to this definition")
    :   Get orders placed today for the account.

        Parameters:[¶](account.html#tastytrade.account.Account.get_live_orders-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_live_orders.session "Permalink to this definition")
            :   the session to use for the request.

    get\_margin\_requirements(*[session](account.html#tastytrade.account.Account.get_margin_requirements.session "tastytrade.account.Account.get_margin_requirements.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [MarginReport](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.get_margin_requirements "Link to this definition")
    :   Get the margin report for the account, with total margin requirements
        as well as a breakdown per symbol/instrument.

        Parameters:[¶](account.html#tastytrade.account.Account.get_margin_requirements-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_margin_requirements.session "Permalink to this definition")
            :   the session to use for the request.

    get\_net\_liquidating\_value\_history(*[session](account.html#tastytrade.account.Account.get_net_liquidating_value_history.session "tastytrade.account.Account.get_net_liquidating_value_history.session (Python parameter) — the session to use for the request, can't be certification."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[time\_back](account.html#tastytrade.account.Account.get_net_liquidating_value_history.time_back "tastytrade.account.Account.get_net_liquidating_value_history.time_back (Python parameter) — the time period to get net liquidating value snapshots for."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[start\_time](account.html#tastytrade.account.Account.get_net_liquidating_value_history.start_time "tastytrade.account.Account.get_net_liquidating_value_history.start_time (Python parameter) — the start point for the query."): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[NetLiqOhlc](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.get_net_liquidating_value_history "Link to this definition")
    :   Returns a list of account net liquidating value snapshots over the
        specified time period.

        Parameters:[¶](account.html#tastytrade.account.Account.get_net_liquidating_value_history-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_net_liquidating_value_history.session "Permalink to this definition")
            :   the session to use for the request, can’t be certification.

            time\_back: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_net_liquidating_value_history.time_back "Permalink to this definition")
            :   the time period to get net liquidating value snapshots for. This
                param is required if start\_time is not given. Possible values are:
                ‘1d’, ‘1m’, ‘3m’, ‘6m’, ‘1y’, ‘all’.

            start\_time: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_net_liquidating_value_history.start_time "Permalink to this definition")
            :   the start point for the query. This param is required is time-back
                is not given. If given, will take precedence over time-back.

    get\_order(*[session](account.html#tastytrade.account.Account.get_order.session "tastytrade.account.Account.get_order.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[order\_id](account.html#tastytrade.account.Account.get_order.order_id "tastytrade.account.Account.get_order.order_id (Python parameter) — the ID of the order to fetch."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*) → [PlacedOrder](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.get_order "Link to this definition")
    :   Gets an order with the given ID.

        Parameters:[¶](account.html#tastytrade.account.Account.get_order-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_order.session "Permalink to this definition")
            :   the session to use for the request.

            order\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.get_order.order_id "Permalink to this definition")
            :   the ID of the order to fetch.

    get\_order\_chains(*[session](account.html#tastytrade.account.Account.get_order_chains.session "tastytrade.account.Account.get_order_chains.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[symbol](account.html#tastytrade.account.Account.get_order_chains.symbol "tastytrade.account.Account.get_order_chains.symbol (Python parameter) — the underlying symbol for the chains."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[start\_time](account.html#tastytrade.account.Account.get_order_chains.start_time "tastytrade.account.Account.get_order_chains.start_time (Python parameter) — the beginning time of the query."): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[end\_time](account.html#tastytrade.account.Account.get_order_chains.end_time "tastytrade.account.Account.get_order_chains.end_time (Python parameter) — the ending time of the query."): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[OrderChain](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.get_order_chains "Link to this definition")
    :   Get a list of order chains (open + rolls + close) for given symbol
        over the given time frame, with total P/L, commissions, etc.

        Parameters:[¶](account.html#tastytrade.account.Account.get_order_chains-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_order_chains.session "Permalink to this definition")
            :   the session to use for the request.

            symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.get_order_chains.symbol "Permalink to this definition")
            :   the underlying symbol for the chains.

            start\_time: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.get_order_chains.start_time "Permalink to this definition")
            :   the beginning time of the query.

            end\_time: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.get_order_chains.end_time "Permalink to this definition")
            :   the ending time of the query.

    get\_order\_history(*[session](account.html#tastytrade.account.Account.get_order_history.session "tastytrade.account.Account.get_order_history.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[per\_page](account.html#tastytrade.account.Account.get_order_history.per_page "tastytrade.account.Account.get_order_history.per_page (Python parameter) — the number of results to return per page."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `50`*, *[page\_offset](account.html#tastytrade.account.Account.get_order_history.page_offset "tastytrade.account.Account.get_order_history.page_offset (Python parameter) — provide a specific page to get; if not provided, get all pages"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[start\_date](account.html#tastytrade.account.Account.get_order_history.start_date "tastytrade.account.Account.get_order_history.start_date (Python parameter) — the start date of orders to query."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[end\_date](account.html#tastytrade.account.Account.get_order_history.end_date "tastytrade.account.Account.get_order_history.end_date (Python parameter) — the end date of orders to query."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[underlying\_symbol](account.html#tastytrade.account.Account.get_order_history.underlying_symbol "tastytrade.account.Account.get_order_history.underlying_symbol (Python parameter) — underlying symbol to filter by."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[statuses](account.html#tastytrade.account.Account.get_order_history.statuses "tastytrade.account.Account.get_order_history.statuses (Python parameter) — a list of statuses to filter by."): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[OrderStatus](order.html#tastytrade.order.OrderStatus "tastytrade.order.OrderStatus (Python enum) — Bases: str, Enum")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[futures\_symbol](account.html#tastytrade.account.Account.get_order_history.futures_symbol "tastytrade.account.Account.get_order_history.futures_symbol (Python parameter) — Tastytrade future symbol for futures and future options."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[underlying\_instrument\_type](account.html#tastytrade.account.Account.get_order_history.underlying_instrument_type "tastytrade.account.Account.get_order_history.underlying_instrument_type (Python parameter) — the type of instrument to filter by"): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[sort](account.html#tastytrade.account.Account.get_order_history.sort "tastytrade.account.Account.get_order_history.sort (Python parameter) — the order to sort results in, either 'Desc' or 'Asc'."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[start\_at](account.html#tastytrade.account.Account.get_order_history.start_at "tastytrade.account.Account.get_order_history.start_at (Python parameter) — datetime start range for filtering transactions in full date-time."): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[end\_at](account.html#tastytrade.account.Account.get_order_history.end_at "tastytrade.account.Account.get_order_history.end_at (Python parameter) — datetime end range for filtering transactions in full date-time."): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[PlacedOrder](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.get_order_history "Link to this definition")
    :   Get order history of the account.

        Parameters:[¶](account.html#tastytrade.account.Account.get_order_history-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_order_history.session "Permalink to this definition")
            :   the session to use for the request.

            per\_page: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `50`[¶](account.html#tastytrade.account.Account.get_order_history.per_page "Permalink to this definition")
            :   the number of results to return per page.

            page\_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_order_history.page_offset "Permalink to this definition")
            :   provide a specific page to get; if not provided, get all pages

            start\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_order_history.start_date "Permalink to this definition")
            :   the start date of orders to query.

            end\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_order_history.end_date "Permalink to this definition")
            :   the end date of orders to query.

            underlying\_symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_order_history.underlying_symbol "Permalink to this definition")
            :   underlying symbol to filter by.

            statuses: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[OrderStatus](order.html#tastytrade.order.OrderStatus "tastytrade.order.OrderStatus (Python enum) — Bases: str, Enum")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_order_history.statuses "Permalink to this definition")
            :   a list of statuses to filter by.

            futures\_symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_order_history.futures_symbol "Permalink to this definition")
            :   Tastytrade future symbol for futures and future options.

            underlying\_instrument\_type: [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_order_history.underlying_instrument_type "Permalink to this definition")
            :   the type of instrument to filter by

            sort: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_order_history.sort "Permalink to this definition")
            :   the order to sort results in, either ‘Desc’ or ‘Asc’.

            start\_at: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_order_history.start_at "Permalink to this definition")
            :   datetime start range for filtering transactions in full date-time.

            end\_at: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_order_history.end_at "Permalink to this definition")
            :   datetime end range for filtering transactions in full date-time.

    get\_position\_limit(*[session](account.html#tastytrade.account.Account.get_position_limit.session "tastytrade.account.Account.get_position_limit.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [PositionLimit](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.get_position_limit "Link to this definition")
    :   Get the maximum order size information for the account.

        Parameters:[¶](account.html#tastytrade.account.Account.get_position_limit-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_position_limit.session "Permalink to this definition")
            :   the session to use for the request.

    get\_positions(*[session](account.html#tastytrade.account.Account.get_positions.session "tastytrade.account.Account.get_positions.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[underlying\_symbols](account.html#tastytrade.account.Account.get_positions.underlying_symbols "tastytrade.account.Account.get_positions.underlying_symbols (Python parameter) — an array of underlying symbols for positions."): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[symbol](account.html#tastytrade.account.Account.get_positions.symbol "tastytrade.account.Account.get_positions.symbol (Python parameter) — a single symbol."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[instrument\_type](account.html#tastytrade.account.Account.get_positions.instrument_type "tastytrade.account.Account.get_positions.instrument_type (Python parameter) — the type of instrument."): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[include\_closed](account.html#tastytrade.account.Account.get_positions.include_closed "tastytrade.account.Account.get_positions.include_closed (Python parameter) — if closed positions should be included in the query."): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[underlying\_product\_code](account.html#tastytrade.account.Account.get_positions.underlying_product_code "tastytrade.account.Account.get_positions.underlying_product_code (Python parameter) — the underlying future's product code."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[partition\_keys](account.html#tastytrade.account.Account.get_positions.partition_keys "tastytrade.account.Account.get_positions.partition_keys (Python parameter) — account partition keys."): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[net\_positions](account.html#tastytrade.account.Account.get_positions.net_positions "tastytrade.account.Account.get_positions.net_positions (Python parameter) — returns net positions grouped by instrument type and symbol."): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[include\_marks](account.html#tastytrade.account.Account.get_positions.include_marks "tastytrade.account.Account.get_positions.include_marks (Python parameter) — include current quote mark (note: can decrease performance)."): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[CurrentPosition](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition (Python model) — Bases: TastytradeData")][¶](account.html#tastytrade.account.Account.get_positions "Link to this definition")
    :   Get the current positions of the account.

        Parameters:[¶](account.html#tastytrade.account.Account.get_positions-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_positions.session "Permalink to this definition")
            :   the session to use for the request.

            underlying\_symbols: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_positions.underlying_symbols "Permalink to this definition")
            :   an array of underlying symbols for positions.

            symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_positions.symbol "Permalink to this definition")
            :   a single symbol.

            instrument\_type: [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_positions.instrument_type "Permalink to this definition")
            :   the type of instrument.

            include\_closed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_positions.include_closed "Permalink to this definition")
            :   if closed positions should be included in the query.

            underlying\_product\_code: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_positions.underlying_product_code "Permalink to this definition")
            :   the underlying future’s product code.

            partition\_keys: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_positions.partition_keys "Permalink to this definition")
            :   account partition keys.

            net\_positions: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_positions.net_positions "Permalink to this definition")
            :   returns net positions grouped by instrument type and symbol.

            include\_marks: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_positions.include_marks "Permalink to this definition")
            :   include current quote mark (note: can decrease performance).

    get\_total\_fees(*[session](account.html#tastytrade.account.Account.get_total_fees.session "tastytrade.account.Account.get_total_fees.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[day](account.html#tastytrade.account.Account.get_total_fees.day "tastytrade.account.Account.get_total_fees.day (Python parameter) — the date to get fees for."): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*) → [FeesInfo](account.html#tastytrade.account.FeesInfo "tastytrade.account.FeesInfo (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.get_total_fees "Link to this definition")
    :   Get the total fees for a given date.

        Parameters:[¶](account.html#tastytrade.account.Account.get_total_fees-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_total_fees.session "Permalink to this definition")
            :   the session to use for the request.

            day: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](account.html#tastytrade.account.Account.get_total_fees.day "Permalink to this definition")
            :   the date to get fees for.

    get\_trading\_status(*[session](account.html#tastytrade.account.Account.get_trading_status.session "tastytrade.account.Account.get_trading_status.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [TradingStatus](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.get_trading_status "Link to this definition")
    :   Get the trading status of the account.

        Parameters:[¶](account.html#tastytrade.account.Account.get_trading_status-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_trading_status.session "Permalink to this definition")
            :   the session to use for the request.

    get\_transaction(*[session](account.html#tastytrade.account.Account.get_transaction.session "tastytrade.account.Account.get_transaction.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[id](account.html#tastytrade.account.Account.get_transaction.id "tastytrade.account.Account.get_transaction.id (Python parameter) — the ID of the transaction to fetch."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*) → [Transaction](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.get_transaction "Link to this definition")
    :   Get a single transaction by ID.

        Parameters:[¶](account.html#tastytrade.account.Account.get_transaction-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.get_transaction.session "Permalink to this definition")
            :   the session to use for the request.

            id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.get_transaction.id "Permalink to this definition")
            :   the ID of the transaction to fetch.

    place\_complex\_order(*[session](account.html#tastytrade.account.Account.place_complex_order.session "tastytrade.account.Account.place_complex_order.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[order](account.html#tastytrade.account.Account.place_complex_order.order "tastytrade.account.Account.place_complex_order.order (Python parameter) — the order to place."): [NewComplexOrder](order.html#tastytrade.order.NewComplexOrder "tastytrade.order.NewComplexOrder (Python model) — Bases: TastytradeData")*, *[dry\_run](account.html#tastytrade.account.Account.place_complex_order.dry_run "tastytrade.account.Account.place_complex_order.dry_run (Python parameter) — whether this is a test order or not."): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `True`*) → [PlacedComplexOrderResponse](order.html#tastytrade.order.PlacedComplexOrderResponse "tastytrade.order.PlacedComplexOrderResponse (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.place_complex_order "Link to this definition")
    :   Place the given order.

        Parameters:[¶](account.html#tastytrade.account.Account.place_complex_order-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.place_complex_order.session "Permalink to this definition")
            :   the session to use for the request.

            order: [NewComplexOrder](order.html#tastytrade.order.NewComplexOrder "tastytrade.order.NewComplexOrder (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.place_complex_order.order "Permalink to this definition")
            :   the order to place.

            dry\_run: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `True`[¶](account.html#tastytrade.account.Account.place_complex_order.dry_run "Permalink to this definition")
            :   whether this is a test order or not.

    place\_order(*[session](account.html#tastytrade.account.Account.place_order.session "tastytrade.account.Account.place_order.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[order](account.html#tastytrade.account.Account.place_order.order "tastytrade.account.Account.place_order.order (Python parameter) — the order to place."): [NewOrder](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder (Python model) — Bases: TastytradeData")*, *[dry\_run](account.html#tastytrade.account.Account.place_order.dry_run "tastytrade.account.Account.place_order.dry_run (Python parameter) — whether this is a test order or not."): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `True`*) → [PlacedOrderResponse](order.html#tastytrade.order.PlacedOrderResponse "tastytrade.order.PlacedOrderResponse (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.place_order "Link to this definition")
    :   Place the given order.

        Parameters:[¶](account.html#tastytrade.account.Account.place_order-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.place_order.session "Permalink to this definition")
            :   the session to use for the request.

            order: [NewOrder](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.place_order.order "Permalink to this definition")
            :   the order to place.

            dry\_run: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `True`[¶](account.html#tastytrade.account.Account.place_order.dry_run "Permalink to this definition")
            :   whether this is a test order or not.

    replace\_order(*[session](account.html#tastytrade.account.Account.replace_order.session "tastytrade.account.Account.replace_order.session (Python parameter) — the session to use for the request."): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[old\_order\_id](account.html#tastytrade.account.Account.replace_order.old_order_id "tastytrade.account.Account.replace_order.old_order_id (Python parameter) — the ID of the order to replace."): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[new\_order](account.html#tastytrade.account.Account.replace_order.new_order "tastytrade.account.Account.replace_order.new_order (Python parameter) — the new order to replace the old order with."): [NewOrder](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder (Python model) — Bases: TastytradeData")*) → [PlacedOrder](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.replace_order "Link to this definition")
    :   Replace an order with a new order with different characteristics (but
        same legs).

        Parameters:[¶](account.html#tastytrade.account.Account.replace_order-parameters "Permalink to this headline")
        :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](account.html#tastytrade.account.Account.replace_order.session "Permalink to this definition")
            :   the session to use for the request.

            old\_order\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[¶](account.html#tastytrade.account.Account.replace_order.old_order_id "Permalink to this definition")
            :   the ID of the order to replace.

            new\_order: [NewOrder](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder (Python model) — Bases: TastytradeData")[¶](account.html#tastytrade.account.Account.replace_order.new_order "Permalink to this definition")
            :   the new order to replace the old order with.

*pydantic model* tastytrade.account.AccountBalance(*\**, *[account\_number](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.account_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[cash\_balance](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.cash_balance (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[long\_equity\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.long_equity_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[short\_equity\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.short_equity_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[long\_derivative\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.long_derivative_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[short\_derivative\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.short_derivative_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[long\_futures\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.long_futures_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[short\_futures\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.short_futures_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[long\_futures\_derivative\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.long_futures_derivative_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[short\_futures\_derivative\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.short_futures_derivative_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[long\_margineable\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.long_margineable_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[short\_margineable\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.short_margineable_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[margin\_equity](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.margin_equity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[equity\_buying\_power](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.equity_buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[derivative\_buying\_power](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.derivative_buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[day\_trading\_buying\_power](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.day_trading_buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[futures\_margin\_requirement](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.futures_margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[available\_trading\_funds](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.available_trading_funds (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[maintenance\_requirement](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.maintenance_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[maintenance\_call\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.maintenance_call_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[reg\_t\_call\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.reg_t_call_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[day\_trading\_call\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.day_trading_call_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[day\_equity\_call\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.day_equity_call_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[net\_liquidating\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.net_liquidating_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[cash\_available\_to\_withdraw](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.cash_available_to_withdraw (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[day\_trade\_excess](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.day_trade_excess (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[pending\_cash](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.pending_cash (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[long\_cryptocurrency\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.long_cryptocurrency_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[short\_cryptocurrency\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.short_cryptocurrency_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[cryptocurrency\_margin\_requirement](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.cryptocurrency_margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[unsettled\_cryptocurrency\_fiat\_amount](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.unsettled_cryptocurrency_fiat_amount (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[closed\_loop\_available\_balance](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.closed_loop_available_balance (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[equity\_offering\_margin\_requirement](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.equity_offering_margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[long\_bond\_value](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.long_bond_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[bond\_margin\_requirement](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.bond_margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[used\_derivative\_buying\_power](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.used_derivative_buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[snapshot\_date](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.snapshot_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*, *[reg\_t\_margin\_requirement](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.reg_t_margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[futures\_overnight\_margin\_requirement](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.futures_overnight_margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[futures\_intraday\_margin\_requirement](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.futures_intraday_margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[maintenance\_excess](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.maintenance_excess (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[pending\_margin\_interest](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.pending_margin_interest (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[effective\_cryptocurrency\_buying\_power](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.effective_cryptocurrency_buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[updated\_at](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.updated_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[apex\_starting\_day\_margin\_equity](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.apex_starting_day_margin_equity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[buying\_power\_adjustment](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.buying_power_adjustment (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[time\_of\_day](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.time_of_day (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](account.html#tastytrade.account.AccountBalance "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing account balance information.

    Show JSON schema

    ```
    {
       "title": "AccountBalance",
       "description": "Dataclass containing account balance information.",
       "type": "object",
       "properties": {
          "account-number": {
             "title": "Account-Number",
             "type": "string"
          },
          "cash-balance": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Cash-Balance"
          },
          "long-equity-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Long-Equity-Value"
          },
          "short-equity-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Short-Equity-Value"
          },
          "long-derivative-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Long-Derivative-Value"
          },
          "short-derivative-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Short-Derivative-Value"
          },
          "long-futures-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Long-Futures-Value"
          },
          "short-futures-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Short-Futures-Value"
          },
          "long-futures-derivative-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Long-Futures-Derivative-Value"
          },
          "short-futures-derivative-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Short-Futures-Derivative-Value"
          },
          "long-margineable-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Long-Margineable-Value"
          },
          "short-margineable-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Short-Margineable-Value"
          },
          "margin-equity": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Margin-Equity"
          },
          "equity-buying-power": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Equity-Buying-Power"
          },
          "derivative-buying-power": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Derivative-Buying-Power"
          },
          "day-trading-buying-power": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Day-Trading-Buying-Power"
          },
          "futures-margin-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Futures-Margin-Requirement"
          },
          "available-trading-funds": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Available-Trading-Funds"
          },
          "maintenance-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Maintenance-Requirement"
          },
          "maintenance-call-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Maintenance-Call-Value"
          },
          "reg-t-call-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Reg-T-Call-Value"
          },
          "day-trading-call-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Day-Trading-Call-Value"
          },
          "day-equity-call-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Day-Equity-Call-Value"
          },
          "net-liquidating-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Net-Liquidating-Value"
          },
          "cash-available-to-withdraw": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Cash-Available-To-Withdraw"
          },
          "day-trade-excess": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Day-Trade-Excess"
          },
          "pending-cash": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Pending-Cash"
          },
          "long-cryptocurrency-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Long-Cryptocurrency-Value"
          },
          "short-cryptocurrency-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Short-Cryptocurrency-Value"
          },
          "cryptocurrency-margin-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Cryptocurrency-Margin-Requirement"
          },
          "unsettled-cryptocurrency-fiat-amount": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Unsettled-Cryptocurrency-Fiat-Amount"
          },
          "closed-loop-available-balance": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Closed-Loop-Available-Balance"
          },
          "equity-offering-margin-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Equity-Offering-Margin-Requirement"
          },
          "long-bond-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Long-Bond-Value"
          },
          "bond-margin-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Bond-Margin-Requirement"
          },
          "used-derivative-buying-power": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Used-Derivative-Buying-Power"
          },
          "snapshot-date": {
             "format": "date",
             "title": "Snapshot-Date",
             "type": "string"
          },
          "reg-t-margin-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Reg-T-Margin-Requirement"
          },
          "futures-overnight-margin-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Futures-Overnight-Margin-Requirement"
          },
          "futures-intraday-margin-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Futures-Intraday-Margin-Requirement"
          },
          "maintenance-excess": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Maintenance-Excess"
          },
          "pending-margin-interest": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Pending-Margin-Interest"
          },
          "effective-cryptocurrency-buying-power": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Effective-Cryptocurrency-Buying-Power"
          },
          "updated-at": {
             "format": "date-time",
             "title": "Updated-At",
             "type": "string"
          },
          "apex-starting-day-margin-equity": {
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
             "title": "Apex-Starting-Day-Margin-Equity"
          },
          "buying-power-adjustment": {
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
             "title": "Buying-Power-Adjustment"
          },
          "time-of-day": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Time-Of-Day"
          }
       },
       "required": [
          "account-number",
          "cash-balance",
          "long-equity-value",
          "short-equity-value",
          "long-derivative-value",
          "short-derivative-value",
          "long-futures-value",
          "short-futures-value",
          "long-futures-derivative-value",
          "short-futures-derivative-value",
          "long-margineable-value",
          "short-margineable-value",
          "margin-equity",
          "equity-buying-power",
          "derivative-buying-power",
          "day-trading-buying-power",
          "futures-margin-requirement",
          "available-trading-funds",
          "maintenance-requirement",
          "maintenance-call-value",
          "reg-t-call-value",
          "day-trading-call-value",
          "day-equity-call-value",
          "net-liquidating-value",
          "cash-available-to-withdraw",
          "day-trade-excess",
          "pending-cash",
          "long-cryptocurrency-value",
          "short-cryptocurrency-value",
          "cryptocurrency-margin-requirement",
          "unsettled-cryptocurrency-fiat-amount",
          "closed-loop-available-balance",
          "equity-offering-margin-requirement",
          "long-bond-value",
          "bond-margin-requirement",
          "used-derivative-buying-power",
          "snapshot-date",
          "reg-t-margin-requirement",
          "futures-overnight-margin-requirement",
          "futures-intraday-margin-requirement",
          "maintenance-excess",
          "pending-margin-interest",
          "effective-cryptocurrency-buying-power",
          "updated-at"
       ]
    }

    ```

    Fields:[¶](account.html#tastytrade.account.AccountBalance-fields "Permalink to this headline")
    :   * [`account_number (str)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.account_number (Python parameter)")
        * [`apex_starting_day_margin_equity (decimal.Decimal | None)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.apex_starting_day_margin_equity (Python parameter)")
        * [`available_trading_funds (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.available_trading_funds (Python parameter)")
        * [`bond_margin_requirement (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.bond_margin_requirement (Python parameter)")
        * [`buying_power_adjustment (decimal.Decimal | None)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.buying_power_adjustment (Python parameter)")
        * [`cash_available_to_withdraw (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.cash_available_to_withdraw (Python parameter)")
        * [`cash_balance (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.cash_balance (Python parameter)")
        * [`closed_loop_available_balance (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.closed_loop_available_balance (Python parameter)")
        * [`cryptocurrency_margin_requirement (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.cryptocurrency_margin_requirement (Python parameter)")
        * [`day_equity_call_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.day_equity_call_value (Python parameter)")
        * [`day_trade_excess (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.day_trade_excess (Python parameter)")
        * [`day_trading_buying_power (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.day_trading_buying_power (Python parameter)")
        * [`day_trading_call_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.day_trading_call_value (Python parameter)")
        * [`derivative_buying_power (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.derivative_buying_power (Python parameter)")
        * [`effective_cryptocurrency_buying_power (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.effective_cryptocurrency_buying_power (Python parameter)")
        * [`equity_buying_power (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.equity_buying_power (Python parameter)")
        * [`equity_offering_margin_requirement (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.equity_offering_margin_requirement (Python parameter)")
        * [`futures_intraday_margin_requirement (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.futures_intraday_margin_requirement (Python parameter)")
        * [`futures_margin_requirement (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.futures_margin_requirement (Python parameter)")
        * [`futures_overnight_margin_requirement (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.futures_overnight_margin_requirement (Python parameter)")
        * [`long_bond_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.long_bond_value (Python parameter)")
        * [`long_cryptocurrency_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.long_cryptocurrency_value (Python parameter)")
        * [`long_derivative_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.long_derivative_value (Python parameter)")
        * [`long_equity_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.long_equity_value (Python parameter)")
        * [`long_futures_derivative_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.long_futures_derivative_value (Python parameter)")
        * [`long_futures_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.long_futures_value (Python parameter)")
        * [`long_margineable_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.long_margineable_value (Python parameter)")
        * [`maintenance_call_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.maintenance_call_value (Python parameter)")
        * [`maintenance_excess (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.maintenance_excess (Python parameter)")
        * [`maintenance_requirement (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.maintenance_requirement (Python parameter)")
        * [`margin_equity (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.margin_equity (Python parameter)")
        * [`net_liquidating_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.net_liquidating_value (Python parameter)")
        * [`pending_cash (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.pending_cash (Python parameter)")
        * [`pending_margin_interest (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.pending_margin_interest (Python parameter)")
        * [`reg_t_call_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.reg_t_call_value (Python parameter)")
        * [`reg_t_margin_requirement (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.reg_t_margin_requirement (Python parameter)")
        * [`short_cryptocurrency_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.short_cryptocurrency_value (Python parameter)")
        * [`short_derivative_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.short_derivative_value (Python parameter)")
        * [`short_equity_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.short_equity_value (Python parameter)")
        * [`short_futures_derivative_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.short_futures_derivative_value (Python parameter)")
        * [`short_futures_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.short_futures_value (Python parameter)")
        * [`short_margineable_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.short_margineable_value (Python parameter)")
        * [`snapshot_date (datetime.date)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.snapshot_date (Python parameter)")
        * [`time_of_day (str | None)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.time_of_day (Python parameter)")
        * [`unsettled_cryptocurrency_fiat_amount (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.unsettled_cryptocurrency_fiat_amount (Python parameter)")
        * [`updated_at (datetime.datetime)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.updated_at (Python parameter)")
        * [`used_derivative_buying_power (decimal.Decimal)`](account.html#tastytrade.account.AccountBalance "tastytrade.account.AccountBalance.used_derivative_buying_power (Python parameter)")

    Validators:[¶](account.html#tastytrade.account.AccountBalance-validators "Permalink to this headline")
    :   * `validate_price_effects` » `all fields`

*pydantic model* tastytrade.account.AccountBalanceSnapshot(*\**, *[account\_number](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.account_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[cash\_balance](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.cash_balance (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[long\_equity\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.long_equity_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[short\_equity\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.short_equity_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[long\_derivative\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.long_derivative_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[short\_derivative\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.short_derivative_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[long\_futures\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.long_futures_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[short\_futures\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.short_futures_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[long\_futures\_derivative\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.long_futures_derivative_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[short\_futures\_derivative\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.short_futures_derivative_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[long\_margineable\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.long_margineable_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[short\_margineable\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.short_margineable_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[margin\_equity](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.margin_equity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[equity\_buying\_power](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.equity_buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[derivative\_buying\_power](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.derivative_buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[day\_trading\_buying\_power](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.day_trading_buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[futures\_margin\_requirement](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.futures_margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[available\_trading\_funds](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.available_trading_funds (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[maintenance\_requirement](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.maintenance_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[maintenance\_call\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.maintenance_call_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[reg\_t\_call\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.reg_t_call_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[day\_trading\_call\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.day_trading_call_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[day\_equity\_call\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.day_equity_call_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[net\_liquidating\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.net_liquidating_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[cash\_available\_to\_withdraw](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.cash_available_to_withdraw (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[day\_trade\_excess](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.day_trade_excess (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[pending\_cash](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.pending_cash (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[snapshot\_date](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.snapshot_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*, *[time\_of\_day](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.time_of_day (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[long\_cryptocurrency\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.long_cryptocurrency_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[short\_cryptocurrency\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.short_cryptocurrency_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[cryptocurrency\_margin\_requirement](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.cryptocurrency_margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[unsettled\_cryptocurrency\_fiat\_amount](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.unsettled_cryptocurrency_fiat_amount (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[closed\_loop\_available\_balance](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.closed_loop_available_balance (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[equity\_offering\_margin\_requirement](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.equity_offering_margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[long\_bond\_value](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.long_bond_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[bond\_margin\_requirement](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.bond_margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[used\_derivative\_buying\_power](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.used_derivative_buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](account.html#tastytrade.account.AccountBalanceSnapshot "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing account balance for a moment in time (snapshot).

    Show JSON schema

    ```
    {
       "title": "AccountBalanceSnapshot",
       "description": "Dataclass containing account balance for a moment in time (snapshot).",
       "type": "object",
       "properties": {
          "account-number": {
             "title": "Account-Number",
             "type": "string"
          },
          "cash-balance": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Cash-Balance"
          },
          "long-equity-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Long-Equity-Value"
          },
          "short-equity-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Short-Equity-Value"
          },
          "long-derivative-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Long-Derivative-Value"
          },
          "short-derivative-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Short-Derivative-Value"
          },
          "long-futures-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Long-Futures-Value"
          },
          "short-futures-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Short-Futures-Value"
          },
          "long-futures-derivative-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Long-Futures-Derivative-Value"
          },
          "short-futures-derivative-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Short-Futures-Derivative-Value"
          },
          "long-margineable-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Long-Margineable-Value"
          },
          "short-margineable-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Short-Margineable-Value"
          },
          "margin-equity": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Margin-Equity"
          },
          "equity-buying-power": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Equity-Buying-Power"
          },
          "derivative-buying-power": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Derivative-Buying-Power"
          },
          "day-trading-buying-power": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Day-Trading-Buying-Power"
          },
          "futures-margin-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Futures-Margin-Requirement"
          },
          "available-trading-funds": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Available-Trading-Funds"
          },
          "maintenance-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Maintenance-Requirement"
          },
          "maintenance-call-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Maintenance-Call-Value"
          },
          "reg-t-call-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Reg-T-Call-Value"
          },
          "day-trading-call-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Day-Trading-Call-Value"
          },
          "day-equity-call-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Day-Equity-Call-Value"
          },
          "net-liquidating-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Net-Liquidating-Value"
          },
          "cash-available-to-withdraw": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Cash-Available-To-Withdraw"
          },
          "day-trade-excess": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Day-Trade-Excess"
          },
          "pending-cash": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Pending-Cash"
          },
          "snapshot-date": {
             "format": "date",
             "title": "Snapshot-Date",
             "type": "string"
          },
          "time-of-day": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Time-Of-Day"
          },
          "long-cryptocurrency-value": {
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
             "title": "Long-Cryptocurrency-Value"
          },
          "short-cryptocurrency-value": {
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
             "title": "Short-Cryptocurrency-Value"
          },
          "cryptocurrency-margin-requirement": {
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
             "title": "Cryptocurrency-Margin-Requirement"
          },
          "unsettled-cryptocurrency-fiat-amount": {
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
             "title": "Unsettled-Cryptocurrency-Fiat-Amount"
          },
          "closed-loop-available-balance": {
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
             "title": "Closed-Loop-Available-Balance"
          },
          "equity-offering-margin-requirement": {
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
             "title": "Equity-Offering-Margin-Requirement"
          },
          "long-bond-value": {
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
             "title": "Long-Bond-Value"
          },
          "bond-margin-requirement": {
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
             "title": "Bond-Margin-Requirement"
          },
          "used-derivative-buying-power": {
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
             "title": "Used-Derivative-Buying-Power"
          }
       },
       "required": [
          "account-number",
          "cash-balance",
          "long-equity-value",
          "short-equity-value",
          "long-derivative-value",
          "short-derivative-value",
          "long-futures-value",
          "short-futures-value",
          "long-futures-derivative-value",
          "short-futures-derivative-value",
          "long-margineable-value",
          "short-margineable-value",
          "margin-equity",
          "equity-buying-power",
          "derivative-buying-power",
          "day-trading-buying-power",
          "futures-margin-requirement",
          "available-trading-funds",
          "maintenance-requirement",
          "maintenance-call-value",
          "reg-t-call-value",
          "day-trading-call-value",
          "day-equity-call-value",
          "net-liquidating-value",
          "cash-available-to-withdraw",
          "day-trade-excess",
          "pending-cash",
          "snapshot-date"
       ]
    }

    ```

    Fields:[¶](account.html#tastytrade.account.AccountBalanceSnapshot-fields "Permalink to this headline")
    :   * [`account_number (str)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.account_number (Python parameter)")
        * [`available_trading_funds (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.available_trading_funds (Python parameter)")
        * [`bond_margin_requirement (decimal.Decimal | None)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.bond_margin_requirement (Python parameter)")
        * [`cash_available_to_withdraw (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.cash_available_to_withdraw (Python parameter)")
        * [`cash_balance (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.cash_balance (Python parameter)")
        * [`closed_loop_available_balance (decimal.Decimal | None)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.closed_loop_available_balance (Python parameter)")
        * [`cryptocurrency_margin_requirement (decimal.Decimal | None)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.cryptocurrency_margin_requirement (Python parameter)")
        * [`day_equity_call_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.day_equity_call_value (Python parameter)")
        * [`day_trade_excess (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.day_trade_excess (Python parameter)")
        * [`day_trading_buying_power (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.day_trading_buying_power (Python parameter)")
        * [`day_trading_call_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.day_trading_call_value (Python parameter)")
        * [`derivative_buying_power (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.derivative_buying_power (Python parameter)")
        * [`equity_buying_power (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.equity_buying_power (Python parameter)")
        * [`equity_offering_margin_requirement (decimal.Decimal | None)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.equity_offering_margin_requirement (Python parameter)")
        * [`futures_margin_requirement (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.futures_margin_requirement (Python parameter)")
        * [`long_bond_value (decimal.Decimal | None)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.long_bond_value (Python parameter)")
        * [`long_cryptocurrency_value (decimal.Decimal | None)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.long_cryptocurrency_value (Python parameter)")
        * [`long_derivative_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.long_derivative_value (Python parameter)")
        * [`long_equity_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.long_equity_value (Python parameter)")
        * [`long_futures_derivative_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.long_futures_derivative_value (Python parameter)")
        * [`long_futures_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.long_futures_value (Python parameter)")
        * [`long_margineable_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.long_margineable_value (Python parameter)")
        * [`maintenance_call_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.maintenance_call_value (Python parameter)")
        * [`maintenance_requirement (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.maintenance_requirement (Python parameter)")
        * [`margin_equity (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.margin_equity (Python parameter)")
        * [`net_liquidating_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.net_liquidating_value (Python parameter)")
        * [`pending_cash (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.pending_cash (Python parameter)")
        * [`reg_t_call_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.reg_t_call_value (Python parameter)")
        * [`short_cryptocurrency_value (decimal.Decimal | None)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.short_cryptocurrency_value (Python parameter)")
        * [`short_derivative_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.short_derivative_value (Python parameter)")
        * [`short_equity_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.short_equity_value (Python parameter)")
        * [`short_futures_derivative_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.short_futures_derivative_value (Python parameter)")
        * [`short_futures_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.short_futures_value (Python parameter)")
        * [`short_margineable_value (decimal.Decimal)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.short_margineable_value (Python parameter)")
        * [`snapshot_date (datetime.date)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.snapshot_date (Python parameter)")
        * [`time_of_day (str | None)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.time_of_day (Python parameter)")
        * [`unsettled_cryptocurrency_fiat_amount (decimal.Decimal | None)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.unsettled_cryptocurrency_fiat_amount (Python parameter)")
        * [`used_derivative_buying_power (decimal.Decimal | None)`](account.html#tastytrade.account.AccountBalanceSnapshot "tastytrade.account.AccountBalanceSnapshot.used_derivative_buying_power (Python parameter)")

    Validators:[¶](account.html#tastytrade.account.AccountBalanceSnapshot-validators "Permalink to this headline")
    :   * `validate_price_effects` » `all fields`

*pydantic model* tastytrade.account.CurrentPosition(*\**, *[account\_number](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.account_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[symbol](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[instrument\_type](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.instrument_type (Python parameter)"): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum")*, *[underlying\_symbol](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.underlying_symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[quantity](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.quantity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[quantity\_direction](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.quantity_direction (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[close\_price](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.close_price (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[average\_open\_price](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.average_open_price (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[multiplier](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.multiplier (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[cost\_effect](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.cost_effect (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[is\_suppressed](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.is_suppressed (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_frozen](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.is_frozen (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[realized\_day\_gain](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.realized_day_gain (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[realized\_today](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.realized_today (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[created\_at](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.created_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[updated\_at](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.updated_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[mark](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.mark (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[mark\_price](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.mark_price (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[restricted\_quantity](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.restricted_quantity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[expires\_at](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.expires_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[fixing\_price](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.fixing_price (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[deliverable\_type](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.deliverable_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[average\_yearly\_market\_close\_price](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.average_yearly_market_close_price (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[average\_daily\_market\_close\_price](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.average_daily_market_close_price (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[realized\_day\_gain\_date](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.realized_day_gain_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[realized\_today\_date](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.realized_today_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](account.html#tastytrade.account.CurrentPosition "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing imformation about an individual position in a
    portfolio.

    Show JSON schema

    ```
    {
       "title": "CurrentPosition",
       "description": "Dataclass containing imformation about an individual position in a\nportfolio.",
       "type": "object",
       "properties": {
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
          "underlying-symbol": {
             "title": "Underlying-Symbol",
             "type": "string"
          },
          "quantity": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Quantity"
          },
          "quantity-direction": {
             "title": "Quantity-Direction",
             "type": "string"
          },
          "close-price": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Close-Price"
          },
          "average-open-price": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Average-Open-Price"
          },
          "multiplier": {
             "title": "Multiplier",
             "type": "integer"
          },
          "cost-effect": {
             "title": "Cost-Effect",
             "type": "string"
          },
          "is-suppressed": {
             "title": "Is-Suppressed",
             "type": "boolean"
          },
          "is-frozen": {
             "title": "Is-Frozen",
             "type": "boolean"
          },
          "realized-day-gain": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Realized-Day-Gain"
          },
          "realized-today": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Realized-Today"
          },
          "created-at": {
             "format": "date-time",
             "title": "Created-At",
             "type": "string"
          },
          "updated-at": {
             "format": "date-time",
             "title": "Updated-At",
             "type": "string"
          },
          "mark": {
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
             "title": "Mark"
          },
          "mark-price": {
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
             "title": "Mark-Price"
          },
          "restricted-quantity": {
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
             "title": "Restricted-Quantity"
          },
          "expires-at": {
             "anyOf": [
                {
                   "format": "date-time",
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Expires-At"
          },
          "fixing-price": {
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
             "title": "Fixing-Price"
          },
          "deliverable-type": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Deliverable-Type"
          },
          "average-yearly-market-close-price": {
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
             "title": "Average-Yearly-Market-Close-Price"
          },
          "average-daily-market-close-price": {
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
             "title": "Average-Daily-Market-Close-Price"
          },
          "realized-day-gain-date": {
             "anyOf": [
                {
                   "format": "date",
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Realized-Day-Gain-Date"
          },
          "realized-today-date": {
             "anyOf": [
                {
                   "format": "date",
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Realized-Today-Date"
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
          "account-number",
          "symbol",
          "instrument-type",
          "underlying-symbol",
          "quantity",
          "quantity-direction",
          "close-price",
          "average-open-price",
          "multiplier",
          "cost-effect",
          "is-suppressed",
          "is-frozen",
          "realized-day-gain",
          "realized-today",
          "created-at",
          "updated-at"
       ]
    }

    ```

    Fields:[¶](account.html#tastytrade.account.CurrentPosition-fields "Permalink to this headline")
    :   * [`account_number (str)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.account_number (Python parameter)")
        * [`average_daily_market_close_price (decimal.Decimal | None)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.average_daily_market_close_price (Python parameter)")
        * [`average_open_price (decimal.Decimal)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.average_open_price (Python parameter)")
        * [`average_yearly_market_close_price (decimal.Decimal | None)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.average_yearly_market_close_price (Python parameter)")
        * [`close_price (decimal.Decimal)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.close_price (Python parameter)")
        * [`cost_effect (str)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.cost_effect (Python parameter)")
        * [`created_at (datetime.datetime)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.created_at (Python parameter)")
        * [`deliverable_type (str | None)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.deliverable_type (Python parameter)")
        * [`expires_at (datetime.datetime | None)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.expires_at (Python parameter)")
        * [`fixing_price (decimal.Decimal | None)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.fixing_price (Python parameter)")
        * [`instrument_type (tastytrade.order.InstrumentType)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.instrument_type (Python parameter)")
        * [`is_frozen (bool)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.is_frozen (Python parameter)")
        * [`is_suppressed (bool)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.is_suppressed (Python parameter)")
        * [`mark (decimal.Decimal | None)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.mark (Python parameter)")
        * [`mark_price (decimal.Decimal | None)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.mark_price (Python parameter)")
        * [`multiplier (int)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.multiplier (Python parameter)")
        * [`quantity (decimal.Decimal)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.quantity (Python parameter)")
        * [`quantity_direction (str)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.quantity_direction (Python parameter)")
        * [`realized_day_gain (decimal.Decimal)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.realized_day_gain (Python parameter)")
        * [`realized_day_gain_date (datetime.date | None)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.realized_day_gain_date (Python parameter)")
        * [`realized_today (decimal.Decimal)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.realized_today (Python parameter)")
        * [`realized_today_date (datetime.date | None)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.realized_today_date (Python parameter)")
        * [`restricted_quantity (decimal.Decimal | None)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.restricted_quantity (Python parameter)")
        * [`symbol (str)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.symbol (Python parameter)")
        * [`underlying_symbol (str)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.underlying_symbol (Python parameter)")
        * [`updated_at (datetime.datetime)`](account.html#tastytrade.account.CurrentPosition "tastytrade.account.CurrentPosition.updated_at (Python parameter)")

    Validators:[¶](account.html#tastytrade.account.CurrentPosition-validators "Permalink to this headline")
    :   * `validate_price_effects` » `all fields`

*pydantic model* tastytrade.account.EmptyDict[¶](account.html#tastytrade.account.EmptyDict "Link to this definition")
:   Bases: `BaseModel`

    Show JSON schema

    ```
    {
       "title": "EmptyDict",
       "type": "object",
       "properties": {},
       "additionalProperties": false
    }

    ```

*pydantic model* tastytrade.account.FeesInfo(*\**, *[total\_fees](account.html#tastytrade.account.FeesInfo "tastytrade.account.FeesInfo.total_fees (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*)[¶](account.html#tastytrade.account.FeesInfo "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Show JSON schema

    ```
    {
       "title": "FeesInfo",
       "type": "object",
       "properties": {
          "total-fees": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Total-Fees"
          }
       },
       "required": [
          "total-fees"
       ]
    }

    ```

    Fields:[¶](account.html#tastytrade.account.FeesInfo-fields "Permalink to this headline")
    :   * [`total_fees (decimal.Decimal)`](account.html#tastytrade.account.FeesInfo "tastytrade.account.FeesInfo.total_fees (Python parameter)")

    Validators:[¶](account.html#tastytrade.account.FeesInfo-validators "Permalink to this headline")
    :   * `validate_price_effects` » `all fields`

*pydantic model* tastytrade.account.Lot(*\**, *[id](account.html#tastytrade.account.Lot "tastytrade.account.Lot.id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[transaction\_id](account.html#tastytrade.account.Lot "tastytrade.account.Lot.transaction_id (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[quantity](account.html#tastytrade.account.Lot "tastytrade.account.Lot.quantity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[price](account.html#tastytrade.account.Lot "tastytrade.account.Lot.price (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[quantity\_direction](account.html#tastytrade.account.Lot "tastytrade.account.Lot.quantity_direction (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[executed\_at](account.html#tastytrade.account.Lot "tastytrade.account.Lot.executed_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[transaction\_date](account.html#tastytrade.account.Lot "tastytrade.account.Lot.transaction_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*)[¶](account.html#tastytrade.account.Lot "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about the lot of a position.

    Show JSON schema

    ```
    {
       "title": "Lot",
       "description": "Dataclass containing information about the lot of a position.",
       "type": "object",
       "properties": {
          "id": {
             "title": "Id",
             "type": "string"
          },
          "transaction-id": {
             "title": "Transaction-Id",
             "type": "integer"
          },
          "quantity": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Quantity"
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
          "quantity-direction": {
             "title": "Quantity-Direction",
             "type": "string"
          },
          "executed-at": {
             "format": "date-time",
             "title": "Executed-At",
             "type": "string"
          },
          "transaction-date": {
             "format": "date",
             "title": "Transaction-Date",
             "type": "string"
          }
       },
       "required": [
          "id",
          "transaction-id",
          "quantity",
          "price",
          "quantity-direction",
          "executed-at",
          "transaction-date"
       ]
    }

    ```

    Fields:[¶](account.html#tastytrade.account.Lot-fields "Permalink to this headline")
    :   * [`executed_at (datetime.datetime)`](account.html#tastytrade.account.Lot "tastytrade.account.Lot.executed_at (Python parameter)")
        * [`id (str)`](account.html#tastytrade.account.Lot "tastytrade.account.Lot.id (Python parameter)")
        * [`price (decimal.Decimal)`](account.html#tastytrade.account.Lot "tastytrade.account.Lot.price (Python parameter)")
        * [`quantity (decimal.Decimal)`](account.html#tastytrade.account.Lot "tastytrade.account.Lot.quantity (Python parameter)")
        * [`quantity_direction (str)`](account.html#tastytrade.account.Lot "tastytrade.account.Lot.quantity_direction (Python parameter)")
        * [`transaction_date (datetime.date)`](account.html#tastytrade.account.Lot "tastytrade.account.Lot.transaction_date (Python parameter)")
        * [`transaction_id (int)`](account.html#tastytrade.account.Lot "tastytrade.account.Lot.transaction_id (Python parameter)")

*pydantic model* tastytrade.account.MarginReport(*\**, *[account\_number](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.account_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[description](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[margin\_calculation\_type](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.margin_calculation_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[option\_level](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.option_level (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[margin\_requirement](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[maintenance\_requirement](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.maintenance_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[margin\_equity](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.margin_equity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[option\_buying\_power](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.option_buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[reg\_t\_margin\_requirement](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.reg_t_margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[reg\_t\_option\_buying\_power](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.reg_t_option_buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[maintenance\_excess](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.maintenance_excess (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[last\_state\_timestamp](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.last_state_timestamp (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[groups](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.groups (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[MarginReportEntry](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry (Python model) — Bases: TastytradeData") | [EmptyDict](account.html#tastytrade.account.EmptyDict "tastytrade.account.EmptyDict (Python model) — Bases: BaseModel")]*, *[initial\_requirement](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.initial_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](account.html#tastytrade.account.MarginReport "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing an overall portfolio margin report.

    Show JSON schema

    ```
    {
       "title": "MarginReport",
       "description": "Dataclass containing an overall portfolio margin report.",
       "type": "object",
       "properties": {
          "account-number": {
             "title": "Account-Number",
             "type": "string"
          },
          "description": {
             "title": "Description",
             "type": "string"
          },
          "margin-calculation-type": {
             "title": "Margin-Calculation-Type",
             "type": "string"
          },
          "option-level": {
             "title": "Option-Level",
             "type": "string"
          },
          "margin-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Margin-Requirement"
          },
          "maintenance-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Maintenance-Requirement"
          },
          "margin-equity": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Margin-Equity"
          },
          "option-buying-power": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Option-Buying-Power"
          },
          "reg-t-margin-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Reg-T-Margin-Requirement"
          },
          "reg-t-option-buying-power": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Reg-T-Option-Buying-Power"
          },
          "maintenance-excess": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Maintenance-Excess"
          },
          "last-state-timestamp": {
             "title": "Last-State-Timestamp",
             "type": "integer"
          },
          "groups": {
             "items": {
                "anyOf": [
                   {
                      "$ref": "#/$defs/MarginReportEntry"
                   },
                   {
                      "$ref": "#/$defs/EmptyDict"
                   }
                ]
             },
             "title": "Groups",
             "type": "array"
          },
          "initial-requirement": {
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
             "title": "Initial-Requirement"
          }
       },
       "$defs": {
          "EmptyDict": {
             "additionalProperties": false,
             "properties": {},
             "title": "EmptyDict",
             "type": "object"
          },
          "MarginReportEntry": {
             "description": "Dataclass containing an individual entry (relating to a specific position)\nas part of the overall margin report.",
             "properties": {
                "description": {
                   "title": "Description",
                   "type": "string"
                },
                "code": {
                   "title": "Code",
                   "type": "string"
                },
                "buying-power": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Buying-Power"
                },
                "margin-calculation-type": {
                   "title": "Margin-Calculation-Type",
                   "type": "string"
                },
                "margin-requirement": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Margin-Requirement"
                },
                "expected-price-range-up-percent": {
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
                   "title": "Expected-Price-Range-Up-Percent"
                },
                "expected-price-range-down-percent": {
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
                   "title": "Expected-Price-Range-Down-Percent"
                },
                "groups": {
                   "anyOf": [
                      {
                         "items": {
                            "type": "object"
                         },
                         "type": "array"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Groups"
                },
                "initial-requirement": {
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
                   "title": "Initial-Requirement"
                },
                "maintenance-requirement": {
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
                   "title": "Maintenance-Requirement"
                },
                "point-of-no-return-percent": {
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
                   "title": "Point-Of-No-Return-Percent"
                },
                "price-increase-percent": {
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
                   "title": "Price-Increase-Percent"
                },
                "price-decrease-percent": {
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
                   "title": "Price-Decrease-Percent"
                },
                "underlying-symbol": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Underlying-Symbol"
                },
                "underlying-type": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Underlying-Type"
                }
             },
             "required": [
                "description",
                "code",
                "buying-power",
                "margin-calculation-type",
                "margin-requirement"
             ],
             "title": "MarginReportEntry",
             "type": "object"
          }
       },
       "required": [
          "account-number",
          "description",
          "margin-calculation-type",
          "option-level",
          "margin-requirement",
          "maintenance-requirement",
          "margin-equity",
          "option-buying-power",
          "reg-t-margin-requirement",
          "reg-t-option-buying-power",
          "maintenance-excess",
          "last-state-timestamp",
          "groups"
       ]
    }

    ```

    Fields:[¶](account.html#tastytrade.account.MarginReport-fields "Permalink to this headline")
    :   * [`account_number (str)`](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.account_number (Python parameter)")
        * [`description (str)`](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.description (Python parameter)")
        * [`groups (list[tastytrade.account.MarginReportEntry | tastytrade.account.EmptyDict])`](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.groups (Python parameter)")
        * [`initial_requirement (decimal.Decimal | None)`](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.initial_requirement (Python parameter)")
        * [`last_state_timestamp (int)`](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.last_state_timestamp (Python parameter)")
        * [`maintenance_excess (decimal.Decimal)`](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.maintenance_excess (Python parameter)")
        * [`maintenance_requirement (decimal.Decimal)`](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.maintenance_requirement (Python parameter)")
        * [`margin_calculation_type (str)`](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.margin_calculation_type (Python parameter)")
        * [`margin_equity (decimal.Decimal)`](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.margin_equity (Python parameter)")
        * [`margin_requirement (decimal.Decimal)`](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.margin_requirement (Python parameter)")
        * [`option_buying_power (decimal.Decimal)`](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.option_buying_power (Python parameter)")
        * [`option_level (str)`](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.option_level (Python parameter)")
        * [`reg_t_margin_requirement (decimal.Decimal)`](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.reg_t_margin_requirement (Python parameter)")
        * [`reg_t_option_buying_power (decimal.Decimal)`](account.html#tastytrade.account.MarginReport "tastytrade.account.MarginReport.reg_t_option_buying_power (Python parameter)")

    Validators:[¶](account.html#tastytrade.account.MarginReport-validators "Permalink to this headline")
    :   * `validate_price_effects` » `all fields`

*pydantic model* tastytrade.account.MarginReportEntry(*\**, *[description](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[code](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.code (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[buying\_power](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[margin\_calculation\_type](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.margin_calculation_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[margin\_requirement](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[expected\_price\_range\_up\_percent](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.expected_price_range_up_percent (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[expected\_price\_range\_down\_percent](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.expected_price_range_down_percent (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[groups](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.groups (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[initial\_requirement](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.initial_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[maintenance\_requirement](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.maintenance_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[point\_of\_no\_return\_percent](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.point_of_no_return_percent (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[price\_increase\_percent](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.price_increase_percent (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[price\_decrease\_percent](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.price_decrease_percent (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[underlying\_symbol](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.underlying_symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[underlying\_type](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.underlying_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](account.html#tastytrade.account.MarginReportEntry "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing an individual entry (relating to a specific position)
    as part of the overall margin report.

    Show JSON schema

    ```
    {
       "title": "MarginReportEntry",
       "description": "Dataclass containing an individual entry (relating to a specific position)\nas part of the overall margin report.",
       "type": "object",
       "properties": {
          "description": {
             "title": "Description",
             "type": "string"
          },
          "code": {
             "title": "Code",
             "type": "string"
          },
          "buying-power": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Buying-Power"
          },
          "margin-calculation-type": {
             "title": "Margin-Calculation-Type",
             "type": "string"
          },
          "margin-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Margin-Requirement"
          },
          "expected-price-range-up-percent": {
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
             "title": "Expected-Price-Range-Up-Percent"
          },
          "expected-price-range-down-percent": {
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
             "title": "Expected-Price-Range-Down-Percent"
          },
          "groups": {
             "anyOf": [
                {
                   "items": {
                      "type": "object"
                   },
                   "type": "array"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Groups"
          },
          "initial-requirement": {
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
             "title": "Initial-Requirement"
          },
          "maintenance-requirement": {
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
             "title": "Maintenance-Requirement"
          },
          "point-of-no-return-percent": {
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
             "title": "Point-Of-No-Return-Percent"
          },
          "price-increase-percent": {
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
             "title": "Price-Increase-Percent"
          },
          "price-decrease-percent": {
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
             "title": "Price-Decrease-Percent"
          },
          "underlying-symbol": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Underlying-Symbol"
          },
          "underlying-type": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Underlying-Type"
          }
       },
       "required": [
          "description",
          "code",
          "buying-power",
          "margin-calculation-type",
          "margin-requirement"
       ]
    }

    ```

    Fields:[¶](account.html#tastytrade.account.MarginReportEntry-fields "Permalink to this headline")
    :   * [`buying_power (decimal.Decimal)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.buying_power (Python parameter)")
        * [`code (str)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.code (Python parameter)")
        * [`description (str)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.description (Python parameter)")
        * [`expected_price_range_down_percent (decimal.Decimal | None)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.expected_price_range_down_percent (Python parameter)")
        * [`expected_price_range_up_percent (decimal.Decimal | None)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.expected_price_range_up_percent (Python parameter)")
        * [`groups (list[dict[str, Any]] | None)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.groups (Python parameter)")
        * [`initial_requirement (decimal.Decimal | None)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.initial_requirement (Python parameter)")
        * [`maintenance_requirement (decimal.Decimal | None)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.maintenance_requirement (Python parameter)")
        * [`margin_calculation_type (str)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.margin_calculation_type (Python parameter)")
        * [`margin_requirement (decimal.Decimal)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.margin_requirement (Python parameter)")
        * [`point_of_no_return_percent (decimal.Decimal | None)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.point_of_no_return_percent (Python parameter)")
        * [`price_decrease_percent (decimal.Decimal | None)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.price_decrease_percent (Python parameter)")
        * [`price_increase_percent (decimal.Decimal | None)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.price_increase_percent (Python parameter)")
        * [`underlying_symbol (str | None)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.underlying_symbol (Python parameter)")
        * [`underlying_type (str | None)`](account.html#tastytrade.account.MarginReportEntry "tastytrade.account.MarginReportEntry.underlying_type (Python parameter)")

    Validators:[¶](account.html#tastytrade.account.MarginReportEntry-validators "Permalink to this headline")
    :   * `validate_price_effects` » `all fields`

*pydantic model* tastytrade.account.MarginRequirement(*\**, *[underlying\_symbol](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.underlying_symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[long\_equity\_initial](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.long_equity_initial (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[short\_equity\_initial](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.short_equity_initial (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[long\_equity\_maintenance](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.long_equity_maintenance (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[short\_equity\_maintenance](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.short_equity_maintenance (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[naked\_option\_standard](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.naked_option_standard (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[naked\_option\_minimum](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.naked_option_minimum (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[naked\_option\_floor](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.naked_option_floor (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[clearing\_identifier](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.clearing_identifier (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[is\_deleted](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.is_deleted (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](account.html#tastytrade.account.MarginRequirement "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing general margin requirement information for a symbol.

    Show JSON schema

    ```
    {
       "title": "MarginRequirement",
       "description": "Dataclass containing general margin requirement information for a symbol.",
       "type": "object",
       "properties": {
          "underlying-symbol": {
             "title": "Underlying-Symbol",
             "type": "string"
          },
          "long-equity-initial": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Long-Equity-Initial"
          },
          "short-equity-initial": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Short-Equity-Initial"
          },
          "long-equity-maintenance": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Long-Equity-Maintenance"
          },
          "short-equity-maintenance": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Short-Equity-Maintenance"
          },
          "naked-option-standard": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Naked-Option-Standard"
          },
          "naked-option-minimum": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Naked-Option-Minimum"
          },
          "naked-option-floor": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Naked-Option-Floor"
          },
          "clearing-identifier": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Clearing-Identifier"
          },
          "is-deleted": {
             "anyOf": [
                {
                   "type": "boolean"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Is-Deleted"
          }
       },
       "required": [
          "underlying-symbol",
          "long-equity-initial",
          "short-equity-initial",
          "long-equity-maintenance",
          "short-equity-maintenance",
          "naked-option-standard",
          "naked-option-minimum",
          "naked-option-floor"
       ]
    }

    ```

    Fields:[¶](account.html#tastytrade.account.MarginRequirement-fields "Permalink to this headline")
    :   * [`clearing_identifier (str | None)`](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.clearing_identifier (Python parameter)")
        * [`is_deleted (bool | None)`](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.is_deleted (Python parameter)")
        * [`long_equity_initial (decimal.Decimal)`](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.long_equity_initial (Python parameter)")
        * [`long_equity_maintenance (decimal.Decimal)`](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.long_equity_maintenance (Python parameter)")
        * [`naked_option_floor (decimal.Decimal)`](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.naked_option_floor (Python parameter)")
        * [`naked_option_minimum (decimal.Decimal)`](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.naked_option_minimum (Python parameter)")
        * [`naked_option_standard (decimal.Decimal)`](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.naked_option_standard (Python parameter)")
        * [`short_equity_initial (decimal.Decimal)`](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.short_equity_initial (Python parameter)")
        * [`short_equity_maintenance (decimal.Decimal)`](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.short_equity_maintenance (Python parameter)")
        * [`underlying_symbol (str)`](account.html#tastytrade.account.MarginRequirement "tastytrade.account.MarginRequirement.underlying_symbol (Python parameter)")

*pydantic model* tastytrade.account.NetLiqOhlc(*\**, *[open](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.open (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[high](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.high (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[low](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.low (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[close](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.close (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[pending\_cash\_open](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.pending_cash_open (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[pending\_cash\_high](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.pending_cash_high (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[pending\_cash\_low](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.pending_cash_low (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[pending\_cash\_close](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.pending_cash_close (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[total\_open](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.total_open (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[total\_high](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.total_high (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[total\_low](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.total_low (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[total\_close](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.total_close (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[time](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.time (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)[¶](account.html#tastytrade.account.NetLiqOhlc "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing historical net liquidation data in OHLC format
    (open, high, low, close), with a timestamp.

    Show JSON schema

    ```
    {
       "title": "NetLiqOhlc",
       "description": "Dataclass containing historical net liquidation data in OHLC format\n(open, high, low, close), with a timestamp.",
       "type": "object",
       "properties": {
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
          },
          "pending-cash-open": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Pending-Cash-Open"
          },
          "pending-cash-high": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Pending-Cash-High"
          },
          "pending-cash-low": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Pending-Cash-Low"
          },
          "pending-cash-close": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Pending-Cash-Close"
          },
          "total-open": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Total-Open"
          },
          "total-high": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Total-High"
          },
          "total-low": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Total-Low"
          },
          "total-close": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Total-Close"
          },
          "time": {
             "title": "Time",
             "type": "string"
          }
       },
       "required": [
          "open",
          "high",
          "low",
          "close",
          "pending-cash-open",
          "pending-cash-high",
          "pending-cash-low",
          "pending-cash-close",
          "total-open",
          "total-high",
          "total-low",
          "total-close",
          "time"
       ]
    }

    ```

    Fields:[¶](account.html#tastytrade.account.NetLiqOhlc-fields "Permalink to this headline")
    :   * [`close (decimal.Decimal)`](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.close (Python parameter)")
        * [`high (decimal.Decimal)`](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.high (Python parameter)")
        * [`low (decimal.Decimal)`](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.low (Python parameter)")
        * [`open (decimal.Decimal)`](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.open (Python parameter)")
        * [`pending_cash_close (decimal.Decimal)`](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.pending_cash_close (Python parameter)")
        * [`pending_cash_high (decimal.Decimal)`](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.pending_cash_high (Python parameter)")
        * [`pending_cash_low (decimal.Decimal)`](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.pending_cash_low (Python parameter)")
        * [`pending_cash_open (decimal.Decimal)`](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.pending_cash_open (Python parameter)")
        * [`time (str)`](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.time (Python parameter)")
        * [`total_close (decimal.Decimal)`](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.total_close (Python parameter)")
        * [`total_high (decimal.Decimal)`](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.total_high (Python parameter)")
        * [`total_low (decimal.Decimal)`](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.total_low (Python parameter)")
        * [`total_open (decimal.Decimal)`](account.html#tastytrade.account.NetLiqOhlc "tastytrade.account.NetLiqOhlc.total_open (Python parameter)")

*pydantic model* tastytrade.account.PositionLimit(*\**, *[account\_number](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.account_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[equity\_order\_size](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.equity_order_size (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[equity\_option\_order\_size](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.equity_option_order_size (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[future\_order\_size](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.future_order_size (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[future\_option\_order\_size](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.future_option_order_size (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[underlying\_opening\_order\_limit](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.underlying_opening_order_limit (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[equity\_position\_size](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.equity_position_size (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[equity\_option\_position\_size](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.equity_option_position_size (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[future\_position\_size](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.future_position_size (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[future\_option\_position\_size](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.future_option_position_size (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*)[¶](account.html#tastytrade.account.PositionLimit "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about general account limits.

    Show JSON schema

    ```
    {
       "title": "PositionLimit",
       "description": "Dataclass containing information about general account limits.",
       "type": "object",
       "properties": {
          "account-number": {
             "title": "Account-Number",
             "type": "string"
          },
          "equity-order-size": {
             "title": "Equity-Order-Size",
             "type": "integer"
          },
          "equity-option-order-size": {
             "title": "Equity-Option-Order-Size",
             "type": "integer"
          },
          "future-order-size": {
             "title": "Future-Order-Size",
             "type": "integer"
          },
          "future-option-order-size": {
             "title": "Future-Option-Order-Size",
             "type": "integer"
          },
          "underlying-opening-order-limit": {
             "title": "Underlying-Opening-Order-Limit",
             "type": "integer"
          },
          "equity-position-size": {
             "title": "Equity-Position-Size",
             "type": "integer"
          },
          "equity-option-position-size": {
             "title": "Equity-Option-Position-Size",
             "type": "integer"
          },
          "future-position-size": {
             "title": "Future-Position-Size",
             "type": "integer"
          },
          "future-option-position-size": {
             "title": "Future-Option-Position-Size",
             "type": "integer"
          }
       },
       "required": [
          "account-number",
          "equity-order-size",
          "equity-option-order-size",
          "future-order-size",
          "future-option-order-size",
          "underlying-opening-order-limit",
          "equity-position-size",
          "equity-option-position-size",
          "future-position-size",
          "future-option-position-size"
       ]
    }

    ```

    Fields:[¶](account.html#tastytrade.account.PositionLimit-fields "Permalink to this headline")
    :   * [`account_number (str)`](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.account_number (Python parameter)")
        * [`equity_option_order_size (int)`](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.equity_option_order_size (Python parameter)")
        * [`equity_option_position_size (int)`](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.equity_option_position_size (Python parameter)")
        * [`equity_order_size (int)`](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.equity_order_size (Python parameter)")
        * [`equity_position_size (int)`](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.equity_position_size (Python parameter)")
        * [`future_option_order_size (int)`](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.future_option_order_size (Python parameter)")
        * [`future_option_position_size (int)`](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.future_option_position_size (Python parameter)")
        * [`future_order_size (int)`](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.future_order_size (Python parameter)")
        * [`future_position_size (int)`](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.future_position_size (Python parameter)")
        * [`underlying_opening_order_limit (int)`](account.html#tastytrade.account.PositionLimit "tastytrade.account.PositionLimit.underlying_opening_order_limit (Python parameter)")

*pydantic model* tastytrade.account.TradingStatus(*\**, *[account\_number](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.account_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[equities\_margin\_calculation\_type](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.equities_margin_calculation_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[fee\_schedule\_name](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.fee_schedule_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[futures\_margin\_rate\_multiplier](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.futures_margin_rate_multiplier (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[has\_intraday\_equities\_margin](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.has_intraday_equities_margin (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[id](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.id (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[is\_aggregated\_at\_clearing](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_aggregated_at_clearing (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_closed](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_closed (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_closing\_only](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_closing_only (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_cryptocurrency\_enabled](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_cryptocurrency_enabled (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_frozen](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_frozen (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_full\_equity\_margin\_required](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_full_equity_margin_required (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_futures\_closing\_only](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_futures_closing_only (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_futures\_intra\_day\_enabled](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_futures_intra_day_enabled (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_futures\_enabled](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_futures_enabled (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_in\_day\_trade\_equity\_maintenance\_call](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_in_day_trade_equity_maintenance_call (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_in\_margin\_call](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_in_margin_call (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_pattern\_day\_trader](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_pattern_day_trader (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_small\_notional\_futures\_intra\_day\_enabled](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_small_notional_futures_intra_day_enabled (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_roll\_the\_day\_forward\_enabled](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_roll_the_day_forward_enabled (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[are\_far\_otm\_net\_options\_restricted](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.are_far_otm_net_options_restricted (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[options\_level](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.options_level (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[short\_calls\_enabled](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.short_calls_enabled (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[small\_notional\_futures\_margin\_rate\_multiplier](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.small_notional_futures_margin_rate_multiplier (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[is\_equity\_offering\_enabled](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_equity_offering_enabled (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_equity\_offering\_closing\_only](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_equity_offering_closing_only (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[updated\_at](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.updated_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[is\_portfolio\_margin\_enabled](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_portfolio_margin_enabled (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[is\_risk\_reducing\_only](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_risk_reducing_only (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[day\_trade\_count](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.day_trade_count (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[autotrade\_account\_type](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.autotrade_account_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[clearing\_account\_number](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.clearing_account_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[clearing\_aggregation\_identifier](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.clearing_aggregation_identifier (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[is\_cryptocurrency\_closing\_only](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_cryptocurrency_closing_only (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[pdt\_reset\_on](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.pdt_reset_on (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[cmta\_override](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.cmta_override (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[enhanced\_fraud\_safeguards\_enabled\_at](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.enhanced_fraud_safeguards_enabled_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](account.html#tastytrade.account.TradingStatus "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about an account’s trading status, such
    as what types of trades are allowed (e.g. margin, crypto, futures)

    Show JSON schema

    ```
    {
       "title": "TradingStatus",
       "description": "Dataclass containing information about an account's trading status, such\nas what types of trades are allowed (e.g. margin, crypto, futures)",
       "type": "object",
       "properties": {
          "account-number": {
             "title": "Account-Number",
             "type": "string"
          },
          "equities-margin-calculation-type": {
             "title": "Equities-Margin-Calculation-Type",
             "type": "string"
          },
          "fee-schedule-name": {
             "title": "Fee-Schedule-Name",
             "type": "string"
          },
          "futures-margin-rate-multiplier": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Futures-Margin-Rate-Multiplier"
          },
          "has-intraday-equities-margin": {
             "title": "Has-Intraday-Equities-Margin",
             "type": "boolean"
          },
          "id": {
             "title": "Id",
             "type": "integer"
          },
          "is-aggregated-at-clearing": {
             "title": "Is-Aggregated-At-Clearing",
             "type": "boolean"
          },
          "is-closed": {
             "title": "Is-Closed",
             "type": "boolean"
          },
          "is-closing-only": {
             "title": "Is-Closing-Only",
             "type": "boolean"
          },
          "is-cryptocurrency-enabled": {
             "title": "Is-Cryptocurrency-Enabled",
             "type": "boolean"
          },
          "is-frozen": {
             "title": "Is-Frozen",
             "type": "boolean"
          },
          "is-full-equity-margin-required": {
             "title": "Is-Full-Equity-Margin-Required",
             "type": "boolean"
          },
          "is-futures-closing-only": {
             "title": "Is-Futures-Closing-Only",
             "type": "boolean"
          },
          "is-futures-intra-day-enabled": {
             "title": "Is-Futures-Intra-Day-Enabled",
             "type": "boolean"
          },
          "is-futures-enabled": {
             "title": "Is-Futures-Enabled",
             "type": "boolean"
          },
          "is-in-day-trade-equity-maintenance-call": {
             "title": "Is-In-Day-Trade-Equity-Maintenance-Call",
             "type": "boolean"
          },
          "is-in-margin-call": {
             "title": "Is-In-Margin-Call",
             "type": "boolean"
          },
          "is-pattern-day-trader": {
             "title": "Is-Pattern-Day-Trader",
             "type": "boolean"
          },
          "is-small-notional-futures-intra-day-enabled": {
             "title": "Is-Small-Notional-Futures-Intra-Day-Enabled",
             "type": "boolean"
          },
          "is-roll-the-day-forward-enabled": {
             "title": "Is-Roll-The-Day-Forward-Enabled",
             "type": "boolean"
          },
          "are-far-otm-net-options-restricted": {
             "title": "Are-Far-Otm-Net-Options-Restricted",
             "type": "boolean"
          },
          "options-level": {
             "title": "Options-Level",
             "type": "string"
          },
          "short-calls-enabled": {
             "title": "Short-Calls-Enabled",
             "type": "boolean"
          },
          "small-notional-futures-margin-rate-multiplier": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Small-Notional-Futures-Margin-Rate-Multiplier"
          },
          "is-equity-offering-enabled": {
             "title": "Is-Equity-Offering-Enabled",
             "type": "boolean"
          },
          "is-equity-offering-closing-only": {
             "title": "Is-Equity-Offering-Closing-Only",
             "type": "boolean"
          },
          "updated-at": {
             "format": "date-time",
             "title": "Updated-At",
             "type": "string"
          },
          "is-portfolio-margin-enabled": {
             "anyOf": [
                {
                   "type": "boolean"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Is-Portfolio-Margin-Enabled"
          },
          "is-risk-reducing-only": {
             "anyOf": [
                {
                   "type": "boolean"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Is-Risk-Reducing-Only"
          },
          "day-trade-count": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Day-Trade-Count"
          },
          "autotrade-account-type": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Autotrade-Account-Type"
          },
          "clearing-account-number": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Clearing-Account-Number"
          },
          "clearing-aggregation-identifier": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Clearing-Aggregation-Identifier"
          },
          "is-cryptocurrency-closing-only": {
             "anyOf": [
                {
                   "type": "boolean"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Is-Cryptocurrency-Closing-Only"
          },
          "pdt-reset-on": {
             "anyOf": [
                {
                   "format": "date",
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Pdt-Reset-On"
          },
          "cmta-override": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Cmta-Override"
          },
          "enhanced-fraud-safeguards-enabled-at": {
             "anyOf": [
                {
                   "format": "date-time",
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Enhanced-Fraud-Safeguards-Enabled-At"
          }
       },
       "required": [
          "account-number",
          "equities-margin-calculation-type",
          "fee-schedule-name",
          "futures-margin-rate-multiplier",
          "has-intraday-equities-margin",
          "id",
          "is-aggregated-at-clearing",
          "is-closed",
          "is-closing-only",
          "is-cryptocurrency-enabled",
          "is-frozen",
          "is-full-equity-margin-required",
          "is-futures-closing-only",
          "is-futures-intra-day-enabled",
          "is-futures-enabled",
          "is-in-day-trade-equity-maintenance-call",
          "is-in-margin-call",
          "is-pattern-day-trader",
          "is-small-notional-futures-intra-day-enabled",
          "is-roll-the-day-forward-enabled",
          "are-far-otm-net-options-restricted",
          "options-level",
          "short-calls-enabled",
          "small-notional-futures-margin-rate-multiplier",
          "is-equity-offering-enabled",
          "is-equity-offering-closing-only",
          "updated-at"
       ]
    }

    ```

    Fields:[¶](account.html#tastytrade.account.TradingStatus-fields "Permalink to this headline")
    :   * [`account_number (str)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.account_number (Python parameter)")
        * [`are_far_otm_net_options_restricted (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.are_far_otm_net_options_restricted (Python parameter)")
        * [`autotrade_account_type (str | None)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.autotrade_account_type (Python parameter)")
        * [`clearing_account_number (str | None)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.clearing_account_number (Python parameter)")
        * [`clearing_aggregation_identifier (str | None)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.clearing_aggregation_identifier (Python parameter)")
        * [`cmta_override (int | None)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.cmta_override (Python parameter)")
        * [`day_trade_count (int | None)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.day_trade_count (Python parameter)")
        * [`enhanced_fraud_safeguards_enabled_at (datetime.datetime | None)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.enhanced_fraud_safeguards_enabled_at (Python parameter)")
        * [`equities_margin_calculation_type (str)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.equities_margin_calculation_type (Python parameter)")
        * [`fee_schedule_name (str)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.fee_schedule_name (Python parameter)")
        * [`futures_margin_rate_multiplier (decimal.Decimal)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.futures_margin_rate_multiplier (Python parameter)")
        * [`has_intraday_equities_margin (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.has_intraday_equities_margin (Python parameter)")
        * [`id (int)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.id (Python parameter)")
        * [`is_aggregated_at_clearing (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_aggregated_at_clearing (Python parameter)")
        * [`is_closed (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_closed (Python parameter)")
        * [`is_closing_only (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_closing_only (Python parameter)")
        * [`is_cryptocurrency_closing_only (bool | None)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_cryptocurrency_closing_only (Python parameter)")
        * [`is_cryptocurrency_enabled (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_cryptocurrency_enabled (Python parameter)")
        * [`is_equity_offering_closing_only (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_equity_offering_closing_only (Python parameter)")
        * [`is_equity_offering_enabled (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_equity_offering_enabled (Python parameter)")
        * [`is_frozen (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_frozen (Python parameter)")
        * [`is_full_equity_margin_required (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_full_equity_margin_required (Python parameter)")
        * [`is_futures_closing_only (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_futures_closing_only (Python parameter)")
        * [`is_futures_enabled (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_futures_enabled (Python parameter)")
        * [`is_futures_intra_day_enabled (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_futures_intra_day_enabled (Python parameter)")
        * [`is_in_day_trade_equity_maintenance_call (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_in_day_trade_equity_maintenance_call (Python parameter)")
        * [`is_in_margin_call (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_in_margin_call (Python parameter)")
        * [`is_pattern_day_trader (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_pattern_day_trader (Python parameter)")
        * [`is_portfolio_margin_enabled (bool | None)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_portfolio_margin_enabled (Python parameter)")
        * [`is_risk_reducing_only (bool | None)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_risk_reducing_only (Python parameter)")
        * [`is_roll_the_day_forward_enabled (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_roll_the_day_forward_enabled (Python parameter)")
        * [`is_small_notional_futures_intra_day_enabled (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.is_small_notional_futures_intra_day_enabled (Python parameter)")
        * [`options_level (str)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.options_level (Python parameter)")
        * [`pdt_reset_on (datetime.date | None)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.pdt_reset_on (Python parameter)")
        * [`short_calls_enabled (bool)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.short_calls_enabled (Python parameter)")
        * [`small_notional_futures_margin_rate_multiplier (decimal.Decimal)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.small_notional_futures_margin_rate_multiplier (Python parameter)")
        * [`updated_at (datetime.datetime)`](account.html#tastytrade.account.TradingStatus "tastytrade.account.TradingStatus.updated_at (Python parameter)")

*pydantic model* tastytrade.account.Transaction(*\**, *[id](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.id (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[account\_number](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.account_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[transaction\_type](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.transaction_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[transaction\_sub\_type](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.transaction_sub_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[description](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[executed\_at](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.executed_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[transaction\_date](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.transaction_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*, *[value](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[net\_value](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.net_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[is\_estimated\_fee](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.is_estimated_fee (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[symbol](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[instrument\_type](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.instrument_type (Python parameter)"): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[underlying\_symbol](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.underlying_symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[action](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.action (Python parameter)"): [OrderAction](order.html#tastytrade.order.OrderAction "tastytrade.order.OrderAction (Python enum) — Bases: str, Enum") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[quantity](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.quantity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[price](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.price (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[regulatory\_fees](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.regulatory_fees (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[clearing\_fees](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.clearing_fees (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[commission](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.commission (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[proprietary\_index\_option\_fees](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.proprietary_index_option_fees (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[ext\_exchange\_order\_number](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.ext_exchange_order_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[ext\_global\_order\_number](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.ext_global_order_number (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[ext\_group\_id](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.ext_group_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[ext\_group\_fill\_id](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.ext_group_fill_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[ext\_exec\_id](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.ext_exec_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[exec\_id](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.exec_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[exchange](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.exchange (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[order\_id](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.order_id (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[exchange\_affiliation\_identifier](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.exchange_affiliation_identifier (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[leg\_count](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.leg_count (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[destination\_venue](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.destination_venue (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[other\_charge](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.other_charge (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[other\_charge\_description](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.other_charge_description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[reverses\_id](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.reverses_id (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[cost\_basis\_reconciliation\_date](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.cost_basis_reconciliation_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[lots](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.lots (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[Lot](account.html#tastytrade.account.Lot "tastytrade.account.Lot (Python model) — Bases: TastytradeData")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[agency\_price](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.agency_price (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[principal\_price](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.principal_price (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](account.html#tastytrade.account.Transaction "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about a past transaction.

    Show JSON schema

    ```
    {
       "title": "Transaction",
       "description": "Dataclass containing information about a past transaction.",
       "type": "object",
       "properties": {
          "id": {
             "title": "Id",
             "type": "integer"
          },
          "account-number": {
             "title": "Account-Number",
             "type": "string"
          },
          "transaction-type": {
             "title": "Transaction-Type",
             "type": "string"
          },
          "transaction-sub-type": {
             "title": "Transaction-Sub-Type",
             "type": "string"
          },
          "description": {
             "title": "Description",
             "type": "string"
          },
          "executed-at": {
             "format": "date-time",
             "title": "Executed-At",
             "type": "string"
          },
          "transaction-date": {
             "format": "date",
             "title": "Transaction-Date",
             "type": "string"
          },
          "value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Value"
          },
          "net-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Net-Value"
          },
          "is-estimated-fee": {
             "title": "Is-Estimated-Fee",
             "type": "boolean"
          },
          "symbol": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Symbol"
          },
          "instrument-type": {
             "anyOf": [
                {
                   "$ref": "#/$defs/InstrumentType"
                },
                {
                   "type": "null"
                }
             ],
             "default": null
          },
          "underlying-symbol": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Underlying-Symbol"
          },
          "action": {
             "anyOf": [
                {
                   "$ref": "#/$defs/OrderAction"
                },
                {
                   "type": "null"
                }
             ],
             "default": null
          },
          "quantity": {
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
             "title": "Quantity"
          },
          "price": {
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
             "title": "Price"
          },
          "regulatory-fees": {
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
             "title": "Regulatory-Fees"
          },
          "clearing-fees": {
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
             "title": "Clearing-Fees"
          },
          "commission": {
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
             "title": "Commission"
          },
          "proprietary-index-option-fees": {
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
             "title": "Proprietary-Index-Option-Fees"
          },
          "ext-exchange-order-number": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Ext-Exchange-Order-Number"
          },
          "ext-global-order-number": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Ext-Global-Order-Number"
          },
          "ext-group-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Ext-Group-Id"
          },
          "ext-group-fill-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Ext-Group-Fill-Id"
          },
          "ext-exec-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Ext-Exec-Id"
          },
          "exec-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Exec-Id"
          },
          "exchange": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Exchange"
          },
          "order-id": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Order-Id"
          },
          "exchange-affiliation-identifier": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Exchange-Affiliation-Identifier"
          },
          "leg-count": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Leg-Count"
          },
          "destination-venue": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Destination-Venue"
          },
          "other-charge": {
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
             "title": "Other-Charge"
          },
          "other-charge-description": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Other-Charge-Description"
          },
          "reverses-id": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Reverses-Id"
          },
          "cost-basis-reconciliation-date": {
             "anyOf": [
                {
                   "format": "date",
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Cost-Basis-Reconciliation-Date"
          },
          "lots": {
             "anyOf": [
                {
                   "items": {
                      "$ref": "#/$defs/Lot"
                   },
                   "type": "array"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Lots"
          },
          "agency-price": {
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
             "title": "Agency-Price"
          },
          "principal-price": {
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
             "title": "Principal-Price"
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
          },
          "Lot": {
             "description": "Dataclass containing information about the lot of a position.",
             "properties": {
                "id": {
                   "title": "Id",
                   "type": "string"
                },
                "transaction-id": {
                   "title": "Transaction-Id",
                   "type": "integer"
                },
                "quantity": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Quantity"
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
                "quantity-direction": {
                   "title": "Quantity-Direction",
                   "type": "string"
                },
                "executed-at": {
                   "format": "date-time",
                   "title": "Executed-At",
                   "type": "string"
                },
                "transaction-date": {
                   "format": "date",
                   "title": "Transaction-Date",
                   "type": "string"
                }
             },
             "required": [
                "id",
                "transaction-id",
                "quantity",
                "price",
                "quantity-direction",
                "executed-at",
                "transaction-date"
             ],
             "title": "Lot",
             "type": "object"
          },
          "OrderAction": {
             "description": "This is an :class:`~enum.Enum` that contains the valid order actions.",
             "enum": [
                "Buy to Open",
                "Buy to Close",
                "Sell to Open",
                "Sell to Close",
                "Buy",
                "Sell"
             ],
             "title": "OrderAction",
             "type": "string"
          }
       },
       "required": [
          "id",
          "account-number",
          "transaction-type",
          "transaction-sub-type",
          "description",
          "executed-at",
          "transaction-date",
          "value",
          "net-value",
          "is-estimated-fee"
       ]
    }

    ```

    Fields:[¶](account.html#tastytrade.account.Transaction-fields "Permalink to this headline")
    :   * [`account_number (str)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.account_number (Python parameter)")
        * [`action (tastytrade.order.OrderAction | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.action (Python parameter)")
        * [`agency_price (decimal.Decimal | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.agency_price (Python parameter)")
        * [`clearing_fees (decimal.Decimal | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.clearing_fees (Python parameter)")
        * [`commission (decimal.Decimal | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.commission (Python parameter)")
        * [`cost_basis_reconciliation_date (datetime.date | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.cost_basis_reconciliation_date (Python parameter)")
        * [`description (str)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.description (Python parameter)")
        * [`destination_venue (str | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.destination_venue (Python parameter)")
        * [`exchange (str | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.exchange (Python parameter)")
        * [`exchange_affiliation_identifier (str | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.exchange_affiliation_identifier (Python parameter)")
        * [`exec_id (str | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.exec_id (Python parameter)")
        * [`executed_at (datetime.datetime)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.executed_at (Python parameter)")
        * [`ext_exchange_order_number (str | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.ext_exchange_order_number (Python parameter)")
        * [`ext_exec_id (str | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.ext_exec_id (Python parameter)")
        * [`ext_global_order_number (int | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.ext_global_order_number (Python parameter)")
        * [`ext_group_fill_id (str | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.ext_group_fill_id (Python parameter)")
        * [`ext_group_id (str | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.ext_group_id (Python parameter)")
        * [`id (int)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.id (Python parameter)")
        * [`instrument_type (tastytrade.order.InstrumentType | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.instrument_type (Python parameter)")
        * [`is_estimated_fee (bool)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.is_estimated_fee (Python parameter)")
        * [`leg_count (int | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.leg_count (Python parameter)")
        * [`lots (list[tastytrade.account.Lot] | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.lots (Python parameter)")
        * [`net_value (decimal.Decimal)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.net_value (Python parameter)")
        * [`order_id (int | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.order_id (Python parameter)")
        * [`other_charge (decimal.Decimal | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.other_charge (Python parameter)")
        * [`other_charge_description (str | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.other_charge_description (Python parameter)")
        * [`price (decimal.Decimal | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.price (Python parameter)")
        * [`principal_price (decimal.Decimal | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.principal_price (Python parameter)")
        * [`proprietary_index_option_fees (decimal.Decimal | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.proprietary_index_option_fees (Python parameter)")
        * [`quantity (decimal.Decimal | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.quantity (Python parameter)")
        * [`regulatory_fees (decimal.Decimal | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.regulatory_fees (Python parameter)")
        * [`reverses_id (int | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.reverses_id (Python parameter)")
        * [`symbol (str | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.symbol (Python parameter)")
        * [`transaction_date (datetime.date)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.transaction_date (Python parameter)")
        * [`transaction_sub_type (str)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.transaction_sub_type (Python parameter)")
        * [`transaction_type (str)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.transaction_type (Python parameter)")
        * [`underlying_symbol (str | None)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.underlying_symbol (Python parameter)")
        * [`value (decimal.Decimal)`](account.html#tastytrade.account.Transaction "tastytrade.account.Transaction.value (Python parameter)")

    Validators:[¶](account.html#tastytrade.account.Transaction-validators "Permalink to this headline")
    :   * `validate_price_effects` » `all fields`

[Back to top](account.html#)


[Previous
Watchlists](../watchlists.html)
[Next
tastytrade.backtest](backtesting.html)

© Copyright 2025, tastyware.

Created using
[Sphinx](https://www.sphinx-doc.org/)
7.4.7.
and
[Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)