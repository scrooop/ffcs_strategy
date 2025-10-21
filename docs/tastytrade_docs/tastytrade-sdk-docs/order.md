tastytrade.order - tastytrade 10.1.0 documentation







[Skip to content](order.html#tastytrade.order.AdvancedInstructions)

tastytrade 10.1.0 documentation

tastytrade.order






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
  + tastytrade.order

    [tastytrade.order](order.html#)



    tastytrade.order
    - [tastytrade.order.AdvancedInstructions](order.html#tastytrade.order.AdvancedInstructions)

      * [Fields](order.html#tastytrade.order.AdvancedInstructions-fields)
      * [strict\_position\_effect\_validation](order.html#tastytrade.order.AdvancedInstructions.strict_position_effect_validation)
    - [tastytrade.order.BuyingPowerEffect](order.html#tastytrade.order.BuyingPowerEffect)

      * [Fields](order.html#tastytrade.order.BuyingPowerEffect-fields)
      * [Validators](order.html#tastytrade.order.BuyingPowerEffect-validators)
    - [tastytrade.order.ComplexOrderType](order.html#tastytrade.order.ComplexOrderType)

      * [Member Type](order.html#tastytrade.order.ComplexOrderType-member-type)
      * [AOCO](order.html#tastytrade.order.ComplexOrderType.OCO)
      * [AOTOCO](order.html#tastytrade.order.ComplexOrderType.OTOCO)
    - [tastytrade.order.ComputedData](order.html#tastytrade.order.ComputedData)

      * [Fields](order.html#tastytrade.order.ComputedData-fields)
      * [Validators](order.html#tastytrade.order.ComputedData-validators)
    - [tastytrade.order.FeeCalculation](order.html#tastytrade.order.FeeCalculation)

      * [Fields](order.html#tastytrade.order.FeeCalculation-fields)
      * [Validators](order.html#tastytrade.order.FeeCalculation-validators)
    - [tastytrade.order.FillInfo](order.html#tastytrade.order.FillInfo)

      * [Fields](order.html#tastytrade.order.FillInfo-fields)
    - [tastytrade.order.InstrumentType](order.html#tastytrade.order.InstrumentType)

      * [Member Type](order.html#tastytrade.order.InstrumentType-member-type)
      * [ABOND](order.html#tastytrade.order.InstrumentType.BOND)
      * [ACRYPTOCURRENCY](order.html#tastytrade.order.InstrumentType.CRYPTOCURRENCY)
      * [ACURRENCY\_PAIR](order.html#tastytrade.order.InstrumentType.CURRENCY_PAIR)
      * [AEQUITY](order.html#tastytrade.order.InstrumentType.EQUITY)
      * [AEQUITY\_OFFERING](order.html#tastytrade.order.InstrumentType.EQUITY_OFFERING)
      * [AEQUITY\_OPTION](order.html#tastytrade.order.InstrumentType.EQUITY_OPTION)
      * [AFIXED\_INCOME](order.html#tastytrade.order.InstrumentType.FIXED_INCOME)
      * [AFUTURE](order.html#tastytrade.order.InstrumentType.FUTURE)
      * [AFUTURE\_OPTION](order.html#tastytrade.order.InstrumentType.FUTURE_OPTION)
      * [AINDEX](order.html#tastytrade.order.InstrumentType.INDEX)
      * [ALIQUIDITY\_POOL](order.html#tastytrade.order.InstrumentType.LIQUIDITY_POOL)
      * [AUNKNOWN](order.html#tastytrade.order.InstrumentType.UNKNOWN)
      * [AWARRANT](order.html#tastytrade.order.InstrumentType.WARRANT)
    - [tastytrade.order.Leg](order.html#tastytrade.order.Leg)

      * [Fields](order.html#tastytrade.order.Leg-fields)
    - [tastytrade.order.Message](order.html#tastytrade.order.Message)

      * [Fields](order.html#tastytrade.order.Message-fields)
    - [tastytrade.order.NewComplexOrder](order.html#tastytrade.order.NewComplexOrder)

      * [Fields](order.html#tastytrade.order.NewComplexOrder-fields)
    - [tastytrade.order.NewOrder](order.html#tastytrade.order.NewOrder)

      * [Fields](order.html#tastytrade.order.NewOrder-fields)
      * [price](order.html#tastytrade.order.NewOrder.price)
      * [stop\_trigger](order.html#tastytrade.order.NewOrder.stop_trigger)
      * [value](order.html#tastytrade.order.NewOrder.value)
    - [tastytrade.order.OrderAction](order.html#tastytrade.order.OrderAction)

      * [Member Type](order.html#tastytrade.order.OrderAction-member-type)
      * [ABUY\_TO\_OPEN](order.html#tastytrade.order.OrderAction.BUY_TO_OPEN)
      * [ABUY\_TO\_CLOSE](order.html#tastytrade.order.OrderAction.BUY_TO_CLOSE)
      * [ASELL\_TO\_OPEN](order.html#tastytrade.order.OrderAction.SELL_TO_OPEN)
      * [ASELL\_TO\_CLOSE](order.html#tastytrade.order.OrderAction.SELL_TO_CLOSE)
      * [ABUY](order.html#tastytrade.order.OrderAction.BUY)
      * [ASELL](order.html#tastytrade.order.OrderAction.SELL)
    - [tastytrade.order.OrderChain](order.html#tastytrade.order.OrderChain)

      * [Fields](order.html#tastytrade.order.OrderChain-fields)
    - [tastytrade.order.OrderChainEntry](order.html#tastytrade.order.OrderChainEntry)

      * [Fields](order.html#tastytrade.order.OrderChainEntry-fields)
    - [tastytrade.order.OrderChainLeg](order.html#tastytrade.order.OrderChainLeg)

      * [Fields](order.html#tastytrade.order.OrderChainLeg-fields)
    - [tastytrade.order.OrderChainNode](order.html#tastytrade.order.OrderChainNode)

      * [Fields](order.html#tastytrade.order.OrderChainNode-fields)
      * [Validators](order.html#tastytrade.order.OrderChainNode-validators)
    - [tastytrade.order.OrderCondition](order.html#tastytrade.order.OrderCondition)

      * [Fields](order.html#tastytrade.order.OrderCondition-fields)
    - [tastytrade.order.OrderConditionPriceComponent](order.html#tastytrade.order.OrderConditionPriceComponent)

      * [Fields](order.html#tastytrade.order.OrderConditionPriceComponent-fields)
    - [tastytrade.order.OrderRule](order.html#tastytrade.order.OrderRule)

      * [Fields](order.html#tastytrade.order.OrderRule-fields)
    - [tastytrade.order.OrderStatus](order.html#tastytrade.order.OrderStatus)

      * [Member Type](order.html#tastytrade.order.OrderStatus-member-type)
      * [ARECEIVED](order.html#tastytrade.order.OrderStatus.RECEIVED)
      * [ACANCELLED](order.html#tastytrade.order.OrderStatus.CANCELLED)
      * [AFILLED](order.html#tastytrade.order.OrderStatus.FILLED)
      * [AEXPIRED](order.html#tastytrade.order.OrderStatus.EXPIRED)
      * [ALIVE](order.html#tastytrade.order.OrderStatus.LIVE)
      * [AREJECTED](order.html#tastytrade.order.OrderStatus.REJECTED)
      * [ACONTINGENT](order.html#tastytrade.order.OrderStatus.CONTINGENT)
      * [AROUTED](order.html#tastytrade.order.OrderStatus.ROUTED)
      * [AIN\_FLIGHT](order.html#tastytrade.order.OrderStatus.IN_FLIGHT)
      * [ACANCEL\_REQUESTED](order.html#tastytrade.order.OrderStatus.CANCEL_REQUESTED)
      * [AREPLACE\_REQUESTED](order.html#tastytrade.order.OrderStatus.REPLACE_REQUESTED)
      * [AREMOVED](order.html#tastytrade.order.OrderStatus.REMOVED)
      * [APARTIALLY\_REMOVED](order.html#tastytrade.order.OrderStatus.PARTIALLY_REMOVED)
    - [tastytrade.order.OrderTimeInForce](order.html#tastytrade.order.OrderTimeInForce)

      * [Member Type](order.html#tastytrade.order.OrderTimeInForce-member-type)
      * [ADAY](order.html#tastytrade.order.OrderTimeInForce.DAY)
      * [AGTC](order.html#tastytrade.order.OrderTimeInForce.GTC)
      * [AGTD](order.html#tastytrade.order.OrderTimeInForce.GTD)
      * [AEXT](order.html#tastytrade.order.OrderTimeInForce.EXT)
      * [AGTC\_EXT](order.html#tastytrade.order.OrderTimeInForce.GTC_EXT)
      * [AIOC](order.html#tastytrade.order.OrderTimeInForce.IOC)
    - [tastytrade.order.OrderType](order.html#tastytrade.order.OrderType)

      * [Member Type](order.html#tastytrade.order.OrderType-member-type)
      * [ALIMIT](order.html#tastytrade.order.OrderType.LIMIT)
      * [AMARKET](order.html#tastytrade.order.OrderType.MARKET)
      * [AMARKETABLE\_LIMIT](order.html#tastytrade.order.OrderType.MARKETABLE_LIMIT)
      * [ASTOP](order.html#tastytrade.order.OrderType.STOP)
      * [ASTOP\_LIMIT](order.html#tastytrade.order.OrderType.STOP_LIMIT)
      * [ANOTIONAL\_MARKET](order.html#tastytrade.order.OrderType.NOTIONAL_MARKET)
    - [tastytrade.order.PlacedComplexOrder](order.html#tastytrade.order.PlacedComplexOrder)

      * [Fields](order.html#tastytrade.order.PlacedComplexOrder-fields)
      * [id](order.html#tastytrade.order.PlacedComplexOrder.id)
    - [tastytrade.order.PlacedComplexOrderResponse](order.html#tastytrade.order.PlacedComplexOrderResponse)

      * [Fields](order.html#tastytrade.order.PlacedComplexOrderResponse-fields)
    - [tastytrade.order.PlacedOrder](order.html#tastytrade.order.PlacedOrder)

      * [Fields](order.html#tastytrade.order.PlacedOrder-fields)
      * [Validators](order.html#tastytrade.order.PlacedOrder-validators)
      * [id](order.html#tastytrade.order.PlacedOrder.id)

        + [Validated by](order.html#tastytrade.order.PlacedOrder.id-validated-by)
    - [tastytrade.order.PlacedOrderResponse](order.html#tastytrade.order.PlacedOrderResponse)

      * [Fields](order.html#tastytrade.order.PlacedOrderResponse-fields)
    - [tastytrade.order.TradeableTastytradeJsonDataclass](order.html#tastytrade.order.TradeableTastytradeJsonDataclass)

      * [Fields](order.html#tastytrade.order.TradeableTastytradeJsonDataclass-fields)
      * [Mbuild\_leg](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg)

        + [Parameters](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg-parameters)

          - [pquantity](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg.quantity)
          - [paction](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg.action)
        + [Returns](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg-returns)
  + [tastytrade.search](search.html)
  + [tastytrade.session](session.html)
  + [tastytrade.streamer](streamer.html)
  + [tastytrade.utils](utils.html)
  + [tastytrade.watchlists](watchlists.html)

tastytrade.order

* [tastytrade.order.AdvancedInstructions](order.html#tastytrade.order.AdvancedInstructions)

  + [Fields](order.html#tastytrade.order.AdvancedInstructions-fields)
  + [strict\_position\_effect\_validation](order.html#tastytrade.order.AdvancedInstructions.strict_position_effect_validation)
* [tastytrade.order.BuyingPowerEffect](order.html#tastytrade.order.BuyingPowerEffect)

  + [Fields](order.html#tastytrade.order.BuyingPowerEffect-fields)
  + [Validators](order.html#tastytrade.order.BuyingPowerEffect-validators)
* [tastytrade.order.ComplexOrderType](order.html#tastytrade.order.ComplexOrderType)

  + [Member Type](order.html#tastytrade.order.ComplexOrderType-member-type)
  + [AOCO](order.html#tastytrade.order.ComplexOrderType.OCO)
  + [AOTOCO](order.html#tastytrade.order.ComplexOrderType.OTOCO)
* [tastytrade.order.ComputedData](order.html#tastytrade.order.ComputedData)

  + [Fields](order.html#tastytrade.order.ComputedData-fields)
  + [Validators](order.html#tastytrade.order.ComputedData-validators)
* [tastytrade.order.FeeCalculation](order.html#tastytrade.order.FeeCalculation)

  + [Fields](order.html#tastytrade.order.FeeCalculation-fields)
  + [Validators](order.html#tastytrade.order.FeeCalculation-validators)
* [tastytrade.order.FillInfo](order.html#tastytrade.order.FillInfo)

  + [Fields](order.html#tastytrade.order.FillInfo-fields)
* [tastytrade.order.InstrumentType](order.html#tastytrade.order.InstrumentType)

  + [Member Type](order.html#tastytrade.order.InstrumentType-member-type)
  + [ABOND](order.html#tastytrade.order.InstrumentType.BOND)
  + [ACRYPTOCURRENCY](order.html#tastytrade.order.InstrumentType.CRYPTOCURRENCY)
  + [ACURRENCY\_PAIR](order.html#tastytrade.order.InstrumentType.CURRENCY_PAIR)
  + [AEQUITY](order.html#tastytrade.order.InstrumentType.EQUITY)
  + [AEQUITY\_OFFERING](order.html#tastytrade.order.InstrumentType.EQUITY_OFFERING)
  + [AEQUITY\_OPTION](order.html#tastytrade.order.InstrumentType.EQUITY_OPTION)
  + [AFIXED\_INCOME](order.html#tastytrade.order.InstrumentType.FIXED_INCOME)
  + [AFUTURE](order.html#tastytrade.order.InstrumentType.FUTURE)
  + [AFUTURE\_OPTION](order.html#tastytrade.order.InstrumentType.FUTURE_OPTION)
  + [AINDEX](order.html#tastytrade.order.InstrumentType.INDEX)
  + [ALIQUIDITY\_POOL](order.html#tastytrade.order.InstrumentType.LIQUIDITY_POOL)
  + [AUNKNOWN](order.html#tastytrade.order.InstrumentType.UNKNOWN)
  + [AWARRANT](order.html#tastytrade.order.InstrumentType.WARRANT)
* [tastytrade.order.Leg](order.html#tastytrade.order.Leg)

  + [Fields](order.html#tastytrade.order.Leg-fields)
* [tastytrade.order.Message](order.html#tastytrade.order.Message)

  + [Fields](order.html#tastytrade.order.Message-fields)
* [tastytrade.order.NewComplexOrder](order.html#tastytrade.order.NewComplexOrder)

  + [Fields](order.html#tastytrade.order.NewComplexOrder-fields)
* [tastytrade.order.NewOrder](order.html#tastytrade.order.NewOrder)

  + [Fields](order.html#tastytrade.order.NewOrder-fields)
  + [price](order.html#tastytrade.order.NewOrder.price)
  + [stop\_trigger](order.html#tastytrade.order.NewOrder.stop_trigger)
  + [value](order.html#tastytrade.order.NewOrder.value)
* [tastytrade.order.OrderAction](order.html#tastytrade.order.OrderAction)

  + [Member Type](order.html#tastytrade.order.OrderAction-member-type)
  + [ABUY\_TO\_OPEN](order.html#tastytrade.order.OrderAction.BUY_TO_OPEN)
  + [ABUY\_TO\_CLOSE](order.html#tastytrade.order.OrderAction.BUY_TO_CLOSE)
  + [ASELL\_TO\_OPEN](order.html#tastytrade.order.OrderAction.SELL_TO_OPEN)
  + [ASELL\_TO\_CLOSE](order.html#tastytrade.order.OrderAction.SELL_TO_CLOSE)
  + [ABUY](order.html#tastytrade.order.OrderAction.BUY)
  + [ASELL](order.html#tastytrade.order.OrderAction.SELL)
* [tastytrade.order.OrderChain](order.html#tastytrade.order.OrderChain)

  + [Fields](order.html#tastytrade.order.OrderChain-fields)
* [tastytrade.order.OrderChainEntry](order.html#tastytrade.order.OrderChainEntry)

  + [Fields](order.html#tastytrade.order.OrderChainEntry-fields)
* [tastytrade.order.OrderChainLeg](order.html#tastytrade.order.OrderChainLeg)

  + [Fields](order.html#tastytrade.order.OrderChainLeg-fields)
* [tastytrade.order.OrderChainNode](order.html#tastytrade.order.OrderChainNode)

  + [Fields](order.html#tastytrade.order.OrderChainNode-fields)
  + [Validators](order.html#tastytrade.order.OrderChainNode-validators)
* [tastytrade.order.OrderCondition](order.html#tastytrade.order.OrderCondition)

  + [Fields](order.html#tastytrade.order.OrderCondition-fields)
* [tastytrade.order.OrderConditionPriceComponent](order.html#tastytrade.order.OrderConditionPriceComponent)

  + [Fields](order.html#tastytrade.order.OrderConditionPriceComponent-fields)
* [tastytrade.order.OrderRule](order.html#tastytrade.order.OrderRule)

  + [Fields](order.html#tastytrade.order.OrderRule-fields)
* [tastytrade.order.OrderStatus](order.html#tastytrade.order.OrderStatus)

  + [Member Type](order.html#tastytrade.order.OrderStatus-member-type)
  + [ARECEIVED](order.html#tastytrade.order.OrderStatus.RECEIVED)
  + [ACANCELLED](order.html#tastytrade.order.OrderStatus.CANCELLED)
  + [AFILLED](order.html#tastytrade.order.OrderStatus.FILLED)
  + [AEXPIRED](order.html#tastytrade.order.OrderStatus.EXPIRED)
  + [ALIVE](order.html#tastytrade.order.OrderStatus.LIVE)
  + [AREJECTED](order.html#tastytrade.order.OrderStatus.REJECTED)
  + [ACONTINGENT](order.html#tastytrade.order.OrderStatus.CONTINGENT)
  + [AROUTED](order.html#tastytrade.order.OrderStatus.ROUTED)
  + [AIN\_FLIGHT](order.html#tastytrade.order.OrderStatus.IN_FLIGHT)
  + [ACANCEL\_REQUESTED](order.html#tastytrade.order.OrderStatus.CANCEL_REQUESTED)
  + [AREPLACE\_REQUESTED](order.html#tastytrade.order.OrderStatus.REPLACE_REQUESTED)
  + [AREMOVED](order.html#tastytrade.order.OrderStatus.REMOVED)
  + [APARTIALLY\_REMOVED](order.html#tastytrade.order.OrderStatus.PARTIALLY_REMOVED)
* [tastytrade.order.OrderTimeInForce](order.html#tastytrade.order.OrderTimeInForce)

  + [Member Type](order.html#tastytrade.order.OrderTimeInForce-member-type)
  + [ADAY](order.html#tastytrade.order.OrderTimeInForce.DAY)
  + [AGTC](order.html#tastytrade.order.OrderTimeInForce.GTC)
  + [AGTD](order.html#tastytrade.order.OrderTimeInForce.GTD)
  + [AEXT](order.html#tastytrade.order.OrderTimeInForce.EXT)
  + [AGTC\_EXT](order.html#tastytrade.order.OrderTimeInForce.GTC_EXT)
  + [AIOC](order.html#tastytrade.order.OrderTimeInForce.IOC)
* [tastytrade.order.OrderType](order.html#tastytrade.order.OrderType)

  + [Member Type](order.html#tastytrade.order.OrderType-member-type)
  + [ALIMIT](order.html#tastytrade.order.OrderType.LIMIT)
  + [AMARKET](order.html#tastytrade.order.OrderType.MARKET)
  + [AMARKETABLE\_LIMIT](order.html#tastytrade.order.OrderType.MARKETABLE_LIMIT)
  + [ASTOP](order.html#tastytrade.order.OrderType.STOP)
  + [ASTOP\_LIMIT](order.html#tastytrade.order.OrderType.STOP_LIMIT)
  + [ANOTIONAL\_MARKET](order.html#tastytrade.order.OrderType.NOTIONAL_MARKET)
* [tastytrade.order.PlacedComplexOrder](order.html#tastytrade.order.PlacedComplexOrder)

  + [Fields](order.html#tastytrade.order.PlacedComplexOrder-fields)
  + [id](order.html#tastytrade.order.PlacedComplexOrder.id)
* [tastytrade.order.PlacedComplexOrderResponse](order.html#tastytrade.order.PlacedComplexOrderResponse)

  + [Fields](order.html#tastytrade.order.PlacedComplexOrderResponse-fields)
* [tastytrade.order.PlacedOrder](order.html#tastytrade.order.PlacedOrder)

  + [Fields](order.html#tastytrade.order.PlacedOrder-fields)
  + [Validators](order.html#tastytrade.order.PlacedOrder-validators)
  + [id](order.html#tastytrade.order.PlacedOrder.id)

    - [Validated by](order.html#tastytrade.order.PlacedOrder.id-validated-by)
* [tastytrade.order.PlacedOrderResponse](order.html#tastytrade.order.PlacedOrderResponse)

  + [Fields](order.html#tastytrade.order.PlacedOrderResponse-fields)
* [tastytrade.order.TradeableTastytradeJsonDataclass](order.html#tastytrade.order.TradeableTastytradeJsonDataclass)

  + [Fields](order.html#tastytrade.order.TradeableTastytradeJsonDataclass-fields)
  + [Mbuild\_leg](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg)

    - [Parameters](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg-parameters)

      * [pquantity](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg.quantity)
      * [paction](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg.action)
    - [Returns](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg-returns)

# tastytrade.order[¶](order.html#module-tastytrade.order "Link to this heading")

*pydantic model* tastytrade.order.AdvancedInstructions(*\**, *[strict\_position\_effect\_validation](order.html#tastytrade.order.AdvancedInstructions "tastytrade.order.AdvancedInstructions.strict_position_effect_validation (Python parameter) — By default, if a position meant to be closed by a closing order is no longer open, the API will turn it into an opening order. With this flag, the API would instead discard the closing order."): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`*)[¶](order.html#tastytrade.order.AdvancedInstructions "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing advanced order rules.

    Show JSON schema

    ```
    {
       "title": "AdvancedInstructions",
       "description": "Dataclass containing advanced order rules.",
       "type": "object",
       "properties": {
          "strict-position-effect-validation": {
             "default": false,
             "title": "Strict-Position-Effect-Validation",
             "type": "boolean"
          }
       }
    }

    ```

    Fields:[¶](order.html#tastytrade.order.AdvancedInstructions-fields "Permalink to this headline")
    :   * [`strict_position_effect_validation (bool)`](order.html#tastytrade.order.AdvancedInstructions "tastytrade.order.AdvancedInstructions.strict_position_effect_validation (Python parameter) — By default, if a position meant to be closed by a closing order is no longer open, the API will turn it into an opening order. With this flag, the API would instead discard the closing order.")

    *field* strict\_position\_effect\_validation : [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False` *(alias 'strict-position-effect-validation')*[¶](order.html#tastytrade.order.AdvancedInstructions.strict_position_effect_validation "Link to this definition")
    :   By default, if a position meant to be closed by a closing order is no longer
        open, the API will turn it into an opening order. With this flag, the API would
        instead discard the closing order.

*pydantic model* tastytrade.order.BuyingPowerEffect(*\**, *[change\_in\_margin\_requirement](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.change_in_margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[change\_in\_buying\_power](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.change_in_buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[current\_buying\_power](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.current_buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[new\_buying\_power](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.new_buying_power (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[isolated\_order\_margin\_requirement](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.isolated_order_margin_requirement (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[is\_spread](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.is_spread (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[impact](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.impact (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[effect](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.effect (Python parameter)"): [PriceEffect](utils.html#tastytrade.utils.PriceEffect "tastytrade.utils.PriceEffect (Python enum) — This is an Enum that shows the sign of a price effect, since Tastytrade is apparently against negative numbers.")*)[¶](order.html#tastytrade.order.BuyingPowerEffect "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about the effect of a trade on buying
    power.

    Show JSON schema

    ```
    {
       "title": "BuyingPowerEffect",
       "description": "Dataclass containing information about the effect of a trade on buying\npower.",
       "type": "object",
       "properties": {
          "change-in-margin-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Change-In-Margin-Requirement"
          },
          "change-in-buying-power": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Change-In-Buying-Power"
          },
          "current-buying-power": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Current-Buying-Power"
          },
          "new-buying-power": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "New-Buying-Power"
          },
          "isolated-order-margin-requirement": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Isolated-Order-Margin-Requirement"
          },
          "is-spread": {
             "title": "Is-Spread",
             "type": "boolean"
          },
          "impact": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Impact"
          },
          "effect": {
             "$ref": "#/$defs/PriceEffect"
          }
       },
       "$defs": {
          "PriceEffect": {
             "description": "This is an :class:`~enum.Enum` that shows the sign of a price effect, since\nTastytrade is apparently against negative numbers.",
             "enum": [
                "Credit",
                "Debit",
                "None"
             ],
             "title": "PriceEffect",
             "type": "string"
          }
       },
       "required": [
          "change-in-margin-requirement",
          "change-in-buying-power",
          "current-buying-power",
          "new-buying-power",
          "isolated-order-margin-requirement",
          "is-spread",
          "impact",
          "effect"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.BuyingPowerEffect-fields "Permalink to this headline")
    :   * [`change_in_buying_power (decimal.Decimal)`](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.change_in_buying_power (Python parameter)")
        * [`change_in_margin_requirement (decimal.Decimal)`](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.change_in_margin_requirement (Python parameter)")
        * [`current_buying_power (decimal.Decimal)`](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.current_buying_power (Python parameter)")
        * [`effect (tastytrade.utils.PriceEffect)`](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.effect (Python parameter)")
        * [`impact (decimal.Decimal)`](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.impact (Python parameter)")
        * [`is_spread (bool)`](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.is_spread (Python parameter)")
        * [`isolated_order_margin_requirement (decimal.Decimal)`](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.isolated_order_margin_requirement (Python parameter)")
        * [`new_buying_power (decimal.Decimal)`](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect.new_buying_power (Python parameter)")

    Validators:[¶](order.html#tastytrade.order.BuyingPowerEffect-validators "Permalink to this headline")
    :   * `validate_price_effects` » `all fields`

*enum* tastytrade.order.ComplexOrderType(*[value](order.html#tastytrade.order.ComplexOrderType "tastytrade.order.ComplexOrderType.value (Python parameter)")*)[¶](order.html#tastytrade.order.ComplexOrderType "Link to this definition")
:   Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.13)")

    This is an [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.13)") that contains the valid complex order types.

    Member Type:[¶](order.html#tastytrade.order.ComplexOrderType-member-type "Permalink to this headline")
    :   [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Valid values are as follows:

    OCO = `<ComplexOrderType.OCO: 'OCO'>`[¶](order.html#tastytrade.order.ComplexOrderType.OCO "Link to this definition")

    OTOCO = `<ComplexOrderType.OTOCO: 'OTOCO'>`[¶](order.html#tastytrade.order.ComplexOrderType.OTOCO "Link to this definition")

*pydantic model* tastytrade.order.ComputedData(*\**, *[open](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.open (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[updated\_at](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.updated_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[total\_fees](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.total_fees (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[total\_commissions](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.total_commissions (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[realized\_gain](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.realized_gain (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[realized\_gain\_with\_fees](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.realized_gain_with_fees (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[winner\_realized\_and\_closed](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.winner_realized_and_closed (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[winner\_realized](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.winner_realized (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[winner\_realized\_with\_fees](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.winner_realized_with_fees (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[roll\_count](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.roll_count (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[opened\_at](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.opened_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[last\_occurred\_at](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.last_occurred_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[started\_at\_days\_to\_expiration](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.started_at_days_to_expiration (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[duration](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.duration (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[total\_opening\_cost](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.total_opening_cost (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[total\_closing\_cost](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.total_closing_cost (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[total\_cost](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.total_cost (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[gcd\_open\_quantity](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.gcd_open_quantity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[fees\_missing](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.fees_missing (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[open\_entries](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.open_entries (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[OrderChainEntry](order.html#tastytrade.order.OrderChainEntry "tastytrade.order.OrderChainEntry (Python model) — Bases: TastytradeData")]*, *[total\_cost\_per\_unit](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.total_cost_per_unit (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](order.html#tastytrade.order.ComputedData "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing computed data about an order chain.

    Show JSON schema

    ```
    {
       "title": "ComputedData",
       "description": "Dataclass containing computed data about an order chain.",
       "type": "object",
       "properties": {
          "open": {
             "title": "Open",
             "type": "boolean"
          },
          "updated-at": {
             "format": "date-time",
             "title": "Updated-At",
             "type": "string"
          },
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
          },
          "total-commissions": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Total-Commissions"
          },
          "realized-gain": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Realized-Gain"
          },
          "realized-gain-with-fees": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Realized-Gain-With-Fees"
          },
          "winner-realized-and-closed": {
             "title": "Winner-Realized-And-Closed",
             "type": "boolean"
          },
          "winner-realized": {
             "title": "Winner-Realized",
             "type": "boolean"
          },
          "winner-realized-with-fees": {
             "title": "Winner-Realized-With-Fees",
             "type": "boolean"
          },
          "roll-count": {
             "title": "Roll-Count",
             "type": "integer"
          },
          "opened-at": {
             "format": "date-time",
             "title": "Opened-At",
             "type": "string"
          },
          "last-occurred-at": {
             "format": "date-time",
             "title": "Last-Occurred-At",
             "type": "string"
          },
          "started-at-days-to-expiration": {
             "title": "Started-At-Days-To-Expiration",
             "type": "integer"
          },
          "duration": {
             "title": "Duration",
             "type": "integer"
          },
          "total-opening-cost": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Total-Opening-Cost"
          },
          "total-closing-cost": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Total-Closing-Cost"
          },
          "total-cost": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Total-Cost"
          },
          "gcd-open-quantity": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Gcd-Open-Quantity"
          },
          "fees-missing": {
             "title": "Fees-Missing",
             "type": "boolean"
          },
          "open-entries": {
             "items": {
                "$ref": "#/$defs/OrderChainEntry"
             },
             "title": "Open-Entries",
             "type": "array"
          },
          "total-cost-per-unit": {
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
             "title": "Total-Cost-Per-Unit"
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
          "OrderChainEntry": {
             "description": "Dataclass containing information about a single order in an order chain.",
             "properties": {
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "quantity": {
                   "title": "Quantity",
                   "type": "string"
                },
                "quantity-type": {
                   "title": "Quantity-Type",
                   "type": "string"
                },
                "quantity-numeric": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Quantity-Numeric"
                }
             },
             "required": [
                "symbol",
                "instrument-type",
                "quantity",
                "quantity-type",
                "quantity-numeric"
             ],
             "title": "OrderChainEntry",
             "type": "object"
          }
       },
       "required": [
          "open",
          "updated-at",
          "total-fees",
          "total-commissions",
          "realized-gain",
          "realized-gain-with-fees",
          "winner-realized-and-closed",
          "winner-realized",
          "winner-realized-with-fees",
          "roll-count",
          "opened-at",
          "last-occurred-at",
          "started-at-days-to-expiration",
          "duration",
          "total-opening-cost",
          "total-closing-cost",
          "total-cost",
          "gcd-open-quantity",
          "fees-missing",
          "open-entries"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.ComputedData-fields "Permalink to this headline")
    :   * [`duration (int)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.duration (Python parameter)")
        * [`fees_missing (bool)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.fees_missing (Python parameter)")
        * [`gcd_open_quantity (decimal.Decimal)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.gcd_open_quantity (Python parameter)")
        * [`last_occurred_at (datetime.datetime)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.last_occurred_at (Python parameter)")
        * [`open (bool)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.open (Python parameter)")
        * [`open_entries (list[tastytrade.order.OrderChainEntry])`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.open_entries (Python parameter)")
        * [`opened_at (datetime.datetime)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.opened_at (Python parameter)")
        * [`realized_gain (decimal.Decimal)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.realized_gain (Python parameter)")
        * [`realized_gain_with_fees (decimal.Decimal)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.realized_gain_with_fees (Python parameter)")
        * [`roll_count (int)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.roll_count (Python parameter)")
        * [`started_at_days_to_expiration (int)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.started_at_days_to_expiration (Python parameter)")
        * [`total_closing_cost (decimal.Decimal)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.total_closing_cost (Python parameter)")
        * [`total_commissions (decimal.Decimal)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.total_commissions (Python parameter)")
        * [`total_cost (decimal.Decimal)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.total_cost (Python parameter)")
        * [`total_cost_per_unit (decimal.Decimal | None)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.total_cost_per_unit (Python parameter)")
        * [`total_fees (decimal.Decimal)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.total_fees (Python parameter)")
        * [`total_opening_cost (decimal.Decimal)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.total_opening_cost (Python parameter)")
        * [`updated_at (datetime.datetime)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.updated_at (Python parameter)")
        * [`winner_realized (bool)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.winner_realized (Python parameter)")
        * [`winner_realized_and_closed (bool)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.winner_realized_and_closed (Python parameter)")
        * [`winner_realized_with_fees (bool)`](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData.winner_realized_with_fees (Python parameter)")

    Validators:[¶](order.html#tastytrade.order.ComputedData-validators "Permalink to this headline")
    :   * `validate_price_effects` » `all fields`

*pydantic model* tastytrade.order.FeeCalculation(*\**, *[regulatory\_fees](order.html#tastytrade.order.FeeCalculation "tastytrade.order.FeeCalculation.regulatory_fees (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[clearing\_fees](order.html#tastytrade.order.FeeCalculation "tastytrade.order.FeeCalculation.clearing_fees (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[commission](order.html#tastytrade.order.FeeCalculation "tastytrade.order.FeeCalculation.commission (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[proprietary\_index\_option\_fees](order.html#tastytrade.order.FeeCalculation "tastytrade.order.FeeCalculation.proprietary_index_option_fees (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[total\_fees](order.html#tastytrade.order.FeeCalculation "tastytrade.order.FeeCalculation.total_fees (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*)[¶](order.html#tastytrade.order.FeeCalculation "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about the fees associated with a trade.

    Show JSON schema

    ```
    {
       "title": "FeeCalculation",
       "description": "Dataclass containing information about the fees associated with a trade.",
       "type": "object",
       "properties": {
          "regulatory-fees": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Regulatory-Fees"
          },
          "clearing-fees": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Clearing-Fees"
          },
          "commission": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Commission"
          },
          "proprietary-index-option-fees": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Proprietary-Index-Option-Fees"
          },
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
          "regulatory-fees",
          "clearing-fees",
          "commission",
          "proprietary-index-option-fees",
          "total-fees"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.FeeCalculation-fields "Permalink to this headline")
    :   * [`clearing_fees (decimal.Decimal)`](order.html#tastytrade.order.FeeCalculation "tastytrade.order.FeeCalculation.clearing_fees (Python parameter)")
        * [`commission (decimal.Decimal)`](order.html#tastytrade.order.FeeCalculation "tastytrade.order.FeeCalculation.commission (Python parameter)")
        * [`proprietary_index_option_fees (decimal.Decimal)`](order.html#tastytrade.order.FeeCalculation "tastytrade.order.FeeCalculation.proprietary_index_option_fees (Python parameter)")
        * [`regulatory_fees (decimal.Decimal)`](order.html#tastytrade.order.FeeCalculation "tastytrade.order.FeeCalculation.regulatory_fees (Python parameter)")
        * [`total_fees (decimal.Decimal)`](order.html#tastytrade.order.FeeCalculation "tastytrade.order.FeeCalculation.total_fees (Python parameter)")

    Validators:[¶](order.html#tastytrade.order.FeeCalculation-validators "Permalink to this headline")
    :   * `validate_price_effects` » `all fields`

*pydantic model* tastytrade.order.FillInfo(*\**, *[fill\_id](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo.fill_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[quantity](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo.quantity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[fill\_price](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo.fill_price (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[filled\_at](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo.filled_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[destination\_venue](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo.destination_venue (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[ext\_group\_fill\_id](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo.ext_group_fill_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[ext\_exec\_id](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo.ext_exec_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](order.html#tastytrade.order.FillInfo "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass that contains information about an order fill.

    Show JSON schema

    ```
    {
       "title": "FillInfo",
       "description": "Dataclass that contains information about an order fill.",
       "type": "object",
       "properties": {
          "fill-id": {
             "title": "Fill-Id",
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
          "fill-price": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Fill-Price"
          },
          "filled-at": {
             "format": "date-time",
             "title": "Filled-At",
             "type": "string"
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
          }
       },
       "required": [
          "fill-id",
          "quantity",
          "fill-price",
          "filled-at"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.FillInfo-fields "Permalink to this headline")
    :   * [`destination_venue (str | None)`](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo.destination_venue (Python parameter)")
        * [`ext_exec_id (str | None)`](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo.ext_exec_id (Python parameter)")
        * [`ext_group_fill_id (str | None)`](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo.ext_group_fill_id (Python parameter)")
        * [`fill_id (str)`](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo.fill_id (Python parameter)")
        * [`fill_price (decimal.Decimal)`](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo.fill_price (Python parameter)")
        * [`filled_at (datetime.datetime)`](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo.filled_at (Python parameter)")
        * [`quantity (decimal.Decimal)`](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo.quantity (Python parameter)")

*enum* tastytrade.order.InstrumentType(*[value](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType.value (Python parameter)")*)[¶](order.html#tastytrade.order.InstrumentType "Link to this definition")
:   Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.13)")

    This is an [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.13)") that contains the valid types of instruments
    and their representation in the API.

    Member Type:[¶](order.html#tastytrade.order.InstrumentType-member-type "Permalink to this headline")
    :   [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Valid values are as follows:

    BOND = `<InstrumentType.BOND: 'Bond'>`[¶](order.html#tastytrade.order.InstrumentType.BOND "Link to this definition")

    CRYPTOCURRENCY = `<InstrumentType.CRYPTOCURRENCY: 'Cryptocurrency'>`[¶](order.html#tastytrade.order.InstrumentType.CRYPTOCURRENCY "Link to this definition")

    CURRENCY\_PAIR = `<InstrumentType.CURRENCY_PAIR: 'Currency Pair'>`[¶](order.html#tastytrade.order.InstrumentType.CURRENCY_PAIR "Link to this definition")

    EQUITY = `<InstrumentType.EQUITY: 'Equity'>`[¶](order.html#tastytrade.order.InstrumentType.EQUITY "Link to this definition")

    EQUITY\_OFFERING = `<InstrumentType.EQUITY_OFFERING: 'Equity Offering'>`[¶](order.html#tastytrade.order.InstrumentType.EQUITY_OFFERING "Link to this definition")

    EQUITY\_OPTION = `<InstrumentType.EQUITY_OPTION: 'Equity Option'>`[¶](order.html#tastytrade.order.InstrumentType.EQUITY_OPTION "Link to this definition")

    FIXED\_INCOME = `<InstrumentType.FIXED_INCOME: 'Fixed Income Security'>`[¶](order.html#tastytrade.order.InstrumentType.FIXED_INCOME "Link to this definition")

    FUTURE = `<InstrumentType.FUTURE: 'Future'>`[¶](order.html#tastytrade.order.InstrumentType.FUTURE "Link to this definition")

    FUTURE\_OPTION = `<InstrumentType.FUTURE_OPTION: 'Future Option'>`[¶](order.html#tastytrade.order.InstrumentType.FUTURE_OPTION "Link to this definition")

    INDEX = `<InstrumentType.INDEX: 'Index'>`[¶](order.html#tastytrade.order.InstrumentType.INDEX "Link to this definition")

    LIQUIDITY\_POOL = `<InstrumentType.LIQUIDITY_POOL: 'Liquidity Pool'>`[¶](order.html#tastytrade.order.InstrumentType.LIQUIDITY_POOL "Link to this definition")

    UNKNOWN = `<InstrumentType.UNKNOWN: 'Unknown'>`[¶](order.html#tastytrade.order.InstrumentType.UNKNOWN "Link to this definition")

    WARRANT = `<InstrumentType.WARRANT: 'Warrant'>`[¶](order.html#tastytrade.order.InstrumentType.WARRANT "Link to this definition")

*pydantic model* tastytrade.order.Leg(*\**, *[instrument\_type](order.html#tastytrade.order.Leg "tastytrade.order.Leg.instrument_type (Python parameter)"): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum")*, *[symbol](order.html#tastytrade.order.Leg "tastytrade.order.Leg.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[action](order.html#tastytrade.order.Leg "tastytrade.order.Leg.action (Python parameter)"): [OrderAction](order.html#tastytrade.order.OrderAction "tastytrade.order.OrderAction (Python enum) — Bases: str, Enum")*, *[quantity](order.html#tastytrade.order.Leg "tastytrade.order.Leg.quantity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[remaining\_quantity](order.html#tastytrade.order.Leg "tastytrade.order.Leg.remaining_quantity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[fills](order.html#tastytrade.order.Leg "tastytrade.order.Leg.fills (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[FillInfo](order.html#tastytrade.order.FillInfo "tastytrade.order.FillInfo (Python model) — Bases: TastytradeData")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](order.html#tastytrade.order.Leg "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass that represents an order leg.

    Classes that inherit from [`TradeableTastytradeJsonDataclass`](order.html#tastytrade.order.TradeableTastytradeJsonDataclass "tastytrade.order.TradeableTastytradeJsonDataclass (Python model) — Bases: TastytradeData") can
    call `build_leg()` to build a leg from the dataclass.

    Show JSON schema

    ```
    {
       "title": "Leg",
       "description": "Dataclass that represents an order leg.\n\nClasses that inherit from :class:`TradeableTastytradeJsonDataclass` can\ncall :meth:`build_leg` to build a leg from the dataclass.",
       "type": "object",
       "properties": {
          "instrument-type": {
             "$ref": "#/$defs/InstrumentType"
          },
          "symbol": {
             "title": "Symbol",
             "type": "string"
          },
          "action": {
             "$ref": "#/$defs/OrderAction"
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
          "remaining-quantity": {
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
             "title": "Remaining-Quantity"
          },
          "fills": {
             "anyOf": [
                {
                   "items": {
                      "$ref": "#/$defs/FillInfo"
                   },
                   "type": "array"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Fills"
          }
       },
       "$defs": {
          "FillInfo": {
             "description": "Dataclass that contains information about an order fill.",
             "properties": {
                "fill-id": {
                   "title": "Fill-Id",
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
                "fill-price": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Fill-Price"
                },
                "filled-at": {
                   "format": "date-time",
                   "title": "Filled-At",
                   "type": "string"
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
                }
             },
             "required": [
                "fill-id",
                "quantity",
                "fill-price",
                "filled-at"
             ],
             "title": "FillInfo",
             "type": "object"
          },
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
          "instrument-type",
          "symbol",
          "action"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.Leg-fields "Permalink to this headline")
    :   * [`action (tastytrade.order.OrderAction)`](order.html#tastytrade.order.Leg "tastytrade.order.Leg.action (Python parameter)")
        * [`fills (list[tastytrade.order.FillInfo] | None)`](order.html#tastytrade.order.Leg "tastytrade.order.Leg.fills (Python parameter)")
        * [`instrument_type (tastytrade.order.InstrumentType)`](order.html#tastytrade.order.Leg "tastytrade.order.Leg.instrument_type (Python parameter)")
        * [`quantity (decimal.Decimal | None)`](order.html#tastytrade.order.Leg "tastytrade.order.Leg.quantity (Python parameter)")
        * [`remaining_quantity (decimal.Decimal | None)`](order.html#tastytrade.order.Leg "tastytrade.order.Leg.remaining_quantity (Python parameter)")
        * [`symbol (str)`](order.html#tastytrade.order.Leg "tastytrade.order.Leg.symbol (Python parameter)")

*pydantic model* tastytrade.order.Message(*\**, *[code](order.html#tastytrade.order.Message "tastytrade.order.Message.code (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[message](order.html#tastytrade.order.Message "tastytrade.order.Message.message (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[preflight\_id](order.html#tastytrade.order.Message "tastytrade.order.Message.preflight_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](order.html#tastytrade.order.Message "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass that represents a message from the Tastytrade API, usually
    a warning or an error.

    Show JSON schema

    ```
    {
       "title": "Message",
       "description": "Dataclass that represents a message from the Tastytrade API, usually\na warning or an error.",
       "type": "object",
       "properties": {
          "code": {
             "title": "Code",
             "type": "string"
          },
          "message": {
             "title": "Message",
             "type": "string"
          },
          "preflight-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Preflight-Id"
          }
       },
       "required": [
          "code",
          "message"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.Message-fields "Permalink to this headline")
    :   * [`code (str)`](order.html#tastytrade.order.Message "tastytrade.order.Message.code (Python parameter)")
        * [`message (str)`](order.html#tastytrade.order.Message "tastytrade.order.Message.message (Python parameter)")
        * [`preflight_id (str | None)`](order.html#tastytrade.order.Message "tastytrade.order.Message.preflight_id (Python parameter)")

*pydantic model* tastytrade.order.NewComplexOrder(*\**, *[orders](order.html#tastytrade.order.NewComplexOrder "tastytrade.order.NewComplexOrder.orders (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[NewOrder](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder (Python model) — Bases: TastytradeData")]*, *[source](order.html#tastytrade.order.NewComplexOrder "tastytrade.order.NewComplexOrder.source (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `'tastyware/tastytrade:v10.1.0'`*, *[trigger\_order](order.html#tastytrade.order.NewComplexOrder "tastytrade.order.NewComplexOrder.trigger_order (Python parameter)"): [NewOrder](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder (Python model) — Bases: TastytradeData") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[type](order.html#tastytrade.order.NewComplexOrder "tastytrade.order.NewComplexOrder.type (Python parameter)"): [ComplexOrderType](order.html#tastytrade.order.ComplexOrderType "tastytrade.order.ComplexOrderType (Python enum) — Bases: str, Enum") = `ComplexOrderType.OCO`*)[¶](order.html#tastytrade.order.NewComplexOrder "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about a new OTOCO order.
    Also used for modifying existing orders.

    Show JSON schema

    ```
    {
       "title": "NewComplexOrder",
       "description": "Dataclass containing information about a new OTOCO order.\nAlso used for modifying existing orders.",
       "type": "object",
       "properties": {
          "orders": {
             "items": {
                "$ref": "#/$defs/NewOrder"
             },
             "title": "Orders",
             "type": "array"
          },
          "source": {
             "default": "tastyware/tastytrade:v10.1.0",
             "title": "Source",
             "type": "string"
          },
          "trigger-order": {
             "anyOf": [
                {
                   "$ref": "#/$defs/NewOrder"
                },
                {
                   "type": "null"
                }
             ],
             "default": null
          },
          "type": {
             "$ref": "#/$defs/ComplexOrderType",
             "default": "OCO"
          }
       },
       "$defs": {
          "AdvancedInstructions": {
             "description": "Dataclass containing advanced order rules.",
             "properties": {
                "strict-position-effect-validation": {
                   "default": false,
                   "title": "Strict-Position-Effect-Validation",
                   "type": "boolean"
                }
             },
             "title": "AdvancedInstructions",
             "type": "object"
          },
          "ComplexOrderType": {
             "description": "This is an :class:`~enum.Enum` that contains the valid complex order types.",
             "enum": [
                "OCO",
                "OTOCO"
             ],
             "title": "ComplexOrderType",
             "type": "string"
          },
          "FillInfo": {
             "description": "Dataclass that contains information about an order fill.",
             "properties": {
                "fill-id": {
                   "title": "Fill-Id",
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
                "fill-price": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Fill-Price"
                },
                "filled-at": {
                   "format": "date-time",
                   "title": "Filled-At",
                   "type": "string"
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
                }
             },
             "required": [
                "fill-id",
                "quantity",
                "fill-price",
                "filled-at"
             ],
             "title": "FillInfo",
             "type": "object"
          },
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
          "Leg": {
             "description": "Dataclass that represents an order leg.\n\nClasses that inherit from :class:`TradeableTastytradeJsonDataclass` can\ncall :meth:`build_leg` to build a leg from the dataclass.",
             "properties": {
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "action": {
                   "$ref": "#/$defs/OrderAction"
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
                "remaining-quantity": {
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
                   "title": "Remaining-Quantity"
                },
                "fills": {
                   "anyOf": [
                      {
                         "items": {
                            "$ref": "#/$defs/FillInfo"
                         },
                         "type": "array"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Fills"
                }
             },
             "required": [
                "instrument-type",
                "symbol",
                "action"
             ],
             "title": "Leg",
             "type": "object"
          },
          "NewOrder": {
             "description": "Dataclass containing information about a new order. Also used for\nmodifying existing orders.",
             "properties": {
                "time-in-force": {
                   "$ref": "#/$defs/OrderTimeInForce"
                },
                "order-type": {
                   "$ref": "#/$defs/OrderType"
                },
                "source": {
                   "default": "tastyware/tastytrade:v10.1.0",
                   "title": "Source",
                   "type": "string"
                },
                "legs": {
                   "items": {
                      "$ref": "#/$defs/Leg"
                   },
                   "title": "Legs",
                   "type": "array"
                },
                "gtc-date": {
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
                   "title": "Gtc-Date"
                },
                "stop-trigger": {
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
                   "title": "Stop-Trigger"
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
                "value": {
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
                   "title": "Value"
                },
                "partition-key": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Partition-Key"
                },
                "preflight-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Preflight-Id"
                },
                "rules": {
                   "anyOf": [
                      {
                         "$ref": "#/$defs/OrderRule"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null
                },
                "advanced-instructions": {
                   "anyOf": [
                      {
                         "$ref": "#/$defs/AdvancedInstructions"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null
                }
             },
             "required": [
                "time-in-force",
                "order-type",
                "legs"
             ],
             "title": "NewOrder",
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
          },
          "OrderCondition": {
             "description": "Dataclass that represents an order condition for an order rule.",
             "properties": {
                "id": {
                   "title": "Id",
                   "type": "string"
                },
                "action": {
                   "title": "Action",
                   "type": "string"
                },
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "indicator": {
                   "title": "Indicator",
                   "type": "string"
                },
                "comparator": {
                   "title": "Comparator",
                   "type": "string"
                },
                "threshold": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Threshold"
                },
                "is-threshold-based-on-notional": {
                   "title": "Is-Threshold-Based-On-Notional",
                   "type": "boolean"
                },
                "triggered-at": {
                   "format": "date-time",
                   "title": "Triggered-At",
                   "type": "string"
                },
                "triggered-value": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Triggered-Value"
                },
                "price-components": {
                   "items": {
                      "$ref": "#/$defs/OrderConditionPriceComponent"
                   },
                   "title": "Price-Components",
                   "type": "array"
                }
             },
             "required": [
                "id",
                "action",
                "symbol",
                "instrument-type",
                "indicator",
                "comparator",
                "threshold",
                "is-threshold-based-on-notional",
                "triggered-at",
                "triggered-value",
                "price-components"
             ],
             "title": "OrderCondition",
             "type": "object"
          },
          "OrderConditionPriceComponent": {
             "description": "Dataclass that represents a price component of an order condition.",
             "properties": {
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
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
                }
             },
             "required": [
                "symbol",
                "instrument-type",
                "quantity",
                "quantity-direction"
             ],
             "title": "OrderConditionPriceComponent",
             "type": "object"
          },
          "OrderRule": {
             "description": "Dataclass that represents an order rule for a complex order.",
             "properties": {
                "route-after": {
                   "format": "date-time",
                   "title": "Route-After",
                   "type": "string"
                },
                "routed-at": {
                   "format": "date-time",
                   "title": "Routed-At",
                   "type": "string"
                },
                "cancel-at": {
                   "format": "date-time",
                   "title": "Cancel-At",
                   "type": "string"
                },
                "cancelled-at": {
                   "format": "date-time",
                   "title": "Cancelled-At",
                   "type": "string"
                },
                "order-conditions": {
                   "items": {
                      "$ref": "#/$defs/OrderCondition"
                   },
                   "title": "Order-Conditions",
                   "type": "array"
                }
             },
             "required": [
                "route-after",
                "routed-at",
                "cancel-at",
                "cancelled-at",
                "order-conditions"
             ],
             "title": "OrderRule",
             "type": "object"
          },
          "OrderTimeInForce": {
             "description": "This is an :class:`~enum.Enum` that contains the valid TIFs for orders.",
             "enum": [
                "Day",
                "GTC",
                "GTD",
                "Ext",
                "GTC Ext",
                "IOC"
             ],
             "title": "OrderTimeInForce",
             "type": "string"
          },
          "OrderType": {
             "description": "This is an :class:`~enum.Enum` that contains the valid types of orders.",
             "enum": [
                "Limit",
                "Market",
                "Marketable Limit",
                "Stop",
                "Stop Limit",
                "Notional Market"
             ],
             "title": "OrderType",
             "type": "string"
          }
       },
       "required": [
          "orders"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.NewComplexOrder-fields "Permalink to this headline")
    :   * [`orders (list[tastytrade.order.NewOrder])`](order.html#tastytrade.order.NewComplexOrder "tastytrade.order.NewComplexOrder.orders (Python parameter)")
        * [`source (str)`](order.html#tastytrade.order.NewComplexOrder "tastytrade.order.NewComplexOrder.source (Python parameter)")
        * [`trigger_order (tastytrade.order.NewOrder | None)`](order.html#tastytrade.order.NewComplexOrder "tastytrade.order.NewComplexOrder.trigger_order (Python parameter)")
        * [`type (tastytrade.order.ComplexOrderType)`](order.html#tastytrade.order.NewComplexOrder "tastytrade.order.NewComplexOrder.type (Python parameter)")

*pydantic model* tastytrade.order.NewOrder(*\**, *[time\_in\_force](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.time_in_force (Python parameter)"): [OrderTimeInForce](order.html#tastytrade.order.OrderTimeInForce "tastytrade.order.OrderTimeInForce (Python enum) — Bases: str, Enum")*, *[order\_type](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.order_type (Python parameter)"): [OrderType](order.html#tastytrade.order.OrderType "tastytrade.order.OrderType (Python enum) — Bases: str, Enum")*, *[source](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.source (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `'tastyware/tastytrade:v10.1.0'`*, *[legs](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.legs (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[Leg](order.html#tastytrade.order.Leg "tastytrade.order.Leg (Python model) — Bases: TastytradeData")]*, *[gtc\_date](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.gtc_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[stop\_trigger](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.stop_trigger (Python parameter) — For a stop/stop limit order. If the latter, use price for the limit price"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[price](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.price (Python parameter) — The price of the order; negative = debit, positive = credit"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[value](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.value (Python parameter) — The actual notional value of the order. Only for notional market orders!"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[partition\_key](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.partition_key (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[preflight\_id](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.preflight_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[rules](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.rules (Python parameter)"): [OrderRule](order.html#tastytrade.order.OrderRule "tastytrade.order.OrderRule (Python model) — Bases: TastytradeData") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[advanced\_instructions](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.advanced_instructions (Python parameter)"): [AdvancedInstructions](order.html#tastytrade.order.AdvancedInstructions "tastytrade.order.AdvancedInstructions (Python model) — Bases: TastytradeData") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](order.html#tastytrade.order.NewOrder "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about a new order. Also used for
    modifying existing orders.

    Show JSON schema

    ```
    {
       "title": "NewOrder",
       "description": "Dataclass containing information about a new order. Also used for\nmodifying existing orders.",
       "type": "object",
       "properties": {
          "time-in-force": {
             "$ref": "#/$defs/OrderTimeInForce"
          },
          "order-type": {
             "$ref": "#/$defs/OrderType"
          },
          "source": {
             "default": "tastyware/tastytrade:v10.1.0",
             "title": "Source",
             "type": "string"
          },
          "legs": {
             "items": {
                "$ref": "#/$defs/Leg"
             },
             "title": "Legs",
             "type": "array"
          },
          "gtc-date": {
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
             "title": "Gtc-Date"
          },
          "stop-trigger": {
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
             "title": "Stop-Trigger"
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
          "value": {
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
             "title": "Value"
          },
          "partition-key": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Partition-Key"
          },
          "preflight-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Preflight-Id"
          },
          "rules": {
             "anyOf": [
                {
                   "$ref": "#/$defs/OrderRule"
                },
                {
                   "type": "null"
                }
             ],
             "default": null
          },
          "advanced-instructions": {
             "anyOf": [
                {
                   "$ref": "#/$defs/AdvancedInstructions"
                },
                {
                   "type": "null"
                }
             ],
             "default": null
          }
       },
       "$defs": {
          "AdvancedInstructions": {
             "description": "Dataclass containing advanced order rules.",
             "properties": {
                "strict-position-effect-validation": {
                   "default": false,
                   "title": "Strict-Position-Effect-Validation",
                   "type": "boolean"
                }
             },
             "title": "AdvancedInstructions",
             "type": "object"
          },
          "FillInfo": {
             "description": "Dataclass that contains information about an order fill.",
             "properties": {
                "fill-id": {
                   "title": "Fill-Id",
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
                "fill-price": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Fill-Price"
                },
                "filled-at": {
                   "format": "date-time",
                   "title": "Filled-At",
                   "type": "string"
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
                }
             },
             "required": [
                "fill-id",
                "quantity",
                "fill-price",
                "filled-at"
             ],
             "title": "FillInfo",
             "type": "object"
          },
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
          "Leg": {
             "description": "Dataclass that represents an order leg.\n\nClasses that inherit from :class:`TradeableTastytradeJsonDataclass` can\ncall :meth:`build_leg` to build a leg from the dataclass.",
             "properties": {
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "action": {
                   "$ref": "#/$defs/OrderAction"
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
                "remaining-quantity": {
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
                   "title": "Remaining-Quantity"
                },
                "fills": {
                   "anyOf": [
                      {
                         "items": {
                            "$ref": "#/$defs/FillInfo"
                         },
                         "type": "array"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Fills"
                }
             },
             "required": [
                "instrument-type",
                "symbol",
                "action"
             ],
             "title": "Leg",
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
          },
          "OrderCondition": {
             "description": "Dataclass that represents an order condition for an order rule.",
             "properties": {
                "id": {
                   "title": "Id",
                   "type": "string"
                },
                "action": {
                   "title": "Action",
                   "type": "string"
                },
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "indicator": {
                   "title": "Indicator",
                   "type": "string"
                },
                "comparator": {
                   "title": "Comparator",
                   "type": "string"
                },
                "threshold": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Threshold"
                },
                "is-threshold-based-on-notional": {
                   "title": "Is-Threshold-Based-On-Notional",
                   "type": "boolean"
                },
                "triggered-at": {
                   "format": "date-time",
                   "title": "Triggered-At",
                   "type": "string"
                },
                "triggered-value": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Triggered-Value"
                },
                "price-components": {
                   "items": {
                      "$ref": "#/$defs/OrderConditionPriceComponent"
                   },
                   "title": "Price-Components",
                   "type": "array"
                }
             },
             "required": [
                "id",
                "action",
                "symbol",
                "instrument-type",
                "indicator",
                "comparator",
                "threshold",
                "is-threshold-based-on-notional",
                "triggered-at",
                "triggered-value",
                "price-components"
             ],
             "title": "OrderCondition",
             "type": "object"
          },
          "OrderConditionPriceComponent": {
             "description": "Dataclass that represents a price component of an order condition.",
             "properties": {
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
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
                }
             },
             "required": [
                "symbol",
                "instrument-type",
                "quantity",
                "quantity-direction"
             ],
             "title": "OrderConditionPriceComponent",
             "type": "object"
          },
          "OrderRule": {
             "description": "Dataclass that represents an order rule for a complex order.",
             "properties": {
                "route-after": {
                   "format": "date-time",
                   "title": "Route-After",
                   "type": "string"
                },
                "routed-at": {
                   "format": "date-time",
                   "title": "Routed-At",
                   "type": "string"
                },
                "cancel-at": {
                   "format": "date-time",
                   "title": "Cancel-At",
                   "type": "string"
                },
                "cancelled-at": {
                   "format": "date-time",
                   "title": "Cancelled-At",
                   "type": "string"
                },
                "order-conditions": {
                   "items": {
                      "$ref": "#/$defs/OrderCondition"
                   },
                   "title": "Order-Conditions",
                   "type": "array"
                }
             },
             "required": [
                "route-after",
                "routed-at",
                "cancel-at",
                "cancelled-at",
                "order-conditions"
             ],
             "title": "OrderRule",
             "type": "object"
          },
          "OrderTimeInForce": {
             "description": "This is an :class:`~enum.Enum` that contains the valid TIFs for orders.",
             "enum": [
                "Day",
                "GTC",
                "GTD",
                "Ext",
                "GTC Ext",
                "IOC"
             ],
             "title": "OrderTimeInForce",
             "type": "string"
          },
          "OrderType": {
             "description": "This is an :class:`~enum.Enum` that contains the valid types of orders.",
             "enum": [
                "Limit",
                "Market",
                "Marketable Limit",
                "Stop",
                "Stop Limit",
                "Notional Market"
             ],
             "title": "OrderType",
             "type": "string"
          }
       },
       "required": [
          "time-in-force",
          "order-type",
          "legs"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.NewOrder-fields "Permalink to this headline")
    :   * [`advanced_instructions (tastytrade.order.AdvancedInstructions | None)`](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.advanced_instructions (Python parameter)")
        * [`gtc_date (datetime.date | None)`](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.gtc_date (Python parameter)")
        * [`legs (list[tastytrade.order.Leg])`](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.legs (Python parameter)")
        * [`order_type (tastytrade.order.OrderType)`](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.order_type (Python parameter)")
        * [`partition_key (str | None)`](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.partition_key (Python parameter)")
        * [`preflight_id (str | None)`](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.preflight_id (Python parameter)")
        * [`price (decimal.Decimal | None)`](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.price (Python parameter) — The price of the order; negative = debit, positive = credit")
        * [`rules (tastytrade.order.OrderRule | None)`](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.rules (Python parameter)")
        * [`source (str)`](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.source (Python parameter)")
        * [`stop_trigger (decimal.Decimal | None)`](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.stop_trigger (Python parameter) — For a stop/stop limit order. If the latter, use price for the limit price")
        * [`time_in_force (tastytrade.order.OrderTimeInForce)`](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.time_in_force (Python parameter)")
        * [`value (decimal.Decimal | None)`](order.html#tastytrade.order.NewOrder "tastytrade.order.NewOrder.value (Python parameter) — The actual notional value of the order. Only for notional market orders!")

    *field* price : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](order.html#tastytrade.order.NewOrder.price "Link to this definition")
    :   The price of the order; negative = debit, positive = credit

    *field* stop\_trigger : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None` *(alias 'stop-trigger')*[¶](order.html#tastytrade.order.NewOrder.stop_trigger "Link to this definition")
    :   For a stop/stop limit order. If the latter, use price for the limit price

    *field* value : [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](order.html#tastytrade.order.NewOrder.value "Link to this definition")
    :   The actual notional value of the order. Only for notional market orders!

*enum* tastytrade.order.OrderAction(*[value](order.html#tastytrade.order.OrderAction "tastytrade.order.OrderAction.value (Python parameter)")*)[¶](order.html#tastytrade.order.OrderAction "Link to this definition")
:   Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.13)")

    This is an [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.13)") that contains the valid order actions.

    Member Type:[¶](order.html#tastytrade.order.OrderAction-member-type "Permalink to this headline")
    :   [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Valid values are as follows:

    BUY\_TO\_OPEN = `<OrderAction.BUY_TO_OPEN: 'Buy to Open'>`[¶](order.html#tastytrade.order.OrderAction.BUY_TO_OPEN "Link to this definition")

    BUY\_TO\_CLOSE = `<OrderAction.BUY_TO_CLOSE: 'Buy to Close'>`[¶](order.html#tastytrade.order.OrderAction.BUY_TO_CLOSE "Link to this definition")

    SELL\_TO\_OPEN = `<OrderAction.SELL_TO_OPEN: 'Sell to Open'>`[¶](order.html#tastytrade.order.OrderAction.SELL_TO_OPEN "Link to this definition")

    SELL\_TO\_CLOSE = `<OrderAction.SELL_TO_CLOSE: 'Sell to Close'>`[¶](order.html#tastytrade.order.OrderAction.SELL_TO_CLOSE "Link to this definition")

    BUY = `<OrderAction.BUY: 'Buy'>`[¶](order.html#tastytrade.order.OrderAction.BUY "Link to this definition")

    SELL = `<OrderAction.SELL: 'Sell'>`[¶](order.html#tastytrade.order.OrderAction.SELL "Link to this definition")

*pydantic model* tastytrade.order.OrderChain(*\**, *[id](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.id (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[account\_number](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.account_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[description](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[underlying\_symbol](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.underlying_symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[computed\_data](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.computed_data (Python parameter)"): [ComputedData](order.html#tastytrade.order.ComputedData "tastytrade.order.ComputedData (Python model) — Bases: TastytradeData")*, *[lite\_nodes](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.lite_nodes (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[OrderChainNode](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode (Python model) — Bases: TastytradeData")]*, *[lite\_nodes\_sizes](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.lite_nodes_sizes (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[updated\_at](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.updated_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[created\_at](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.created_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](order.html#tastytrade.order.OrderChain "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about an order chain: a group of orders
    for a specific underlying, such as total P/L, rolls, current P/L in a
    symbol, etc.

    Show JSON schema

    ```
    {
       "title": "OrderChain",
       "description": "Dataclass containing information about an order chain: a group of orders\nfor a specific underlying, such as total P/L, rolls, current P/L in a\nsymbol, etc.",
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
          "description": {
             "title": "Description",
             "type": "string"
          },
          "underlying-symbol": {
             "title": "Underlying-Symbol",
             "type": "string"
          },
          "computed-data": {
             "$ref": "#/$defs/ComputedData"
          },
          "lite-nodes": {
             "items": {
                "$ref": "#/$defs/OrderChainNode"
             },
             "title": "Lite-Nodes",
             "type": "array"
          },
          "lite-nodes-sizes": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Lite-Nodes-Sizes"
          },
          "updated-at": {
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
             "title": "Updated-At"
          },
          "created-at": {
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
             "title": "Created-At"
          }
       },
       "$defs": {
          "ComputedData": {
             "description": "Dataclass containing computed data about an order chain.",
             "properties": {
                "open": {
                   "title": "Open",
                   "type": "boolean"
                },
                "updated-at": {
                   "format": "date-time",
                   "title": "Updated-At",
                   "type": "string"
                },
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
                },
                "total-commissions": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Total-Commissions"
                },
                "realized-gain": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Realized-Gain"
                },
                "realized-gain-with-fees": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Realized-Gain-With-Fees"
                },
                "winner-realized-and-closed": {
                   "title": "Winner-Realized-And-Closed",
                   "type": "boolean"
                },
                "winner-realized": {
                   "title": "Winner-Realized",
                   "type": "boolean"
                },
                "winner-realized-with-fees": {
                   "title": "Winner-Realized-With-Fees",
                   "type": "boolean"
                },
                "roll-count": {
                   "title": "Roll-Count",
                   "type": "integer"
                },
                "opened-at": {
                   "format": "date-time",
                   "title": "Opened-At",
                   "type": "string"
                },
                "last-occurred-at": {
                   "format": "date-time",
                   "title": "Last-Occurred-At",
                   "type": "string"
                },
                "started-at-days-to-expiration": {
                   "title": "Started-At-Days-To-Expiration",
                   "type": "integer"
                },
                "duration": {
                   "title": "Duration",
                   "type": "integer"
                },
                "total-opening-cost": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Total-Opening-Cost"
                },
                "total-closing-cost": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Total-Closing-Cost"
                },
                "total-cost": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Total-Cost"
                },
                "gcd-open-quantity": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Gcd-Open-Quantity"
                },
                "fees-missing": {
                   "title": "Fees-Missing",
                   "type": "boolean"
                },
                "open-entries": {
                   "items": {
                      "$ref": "#/$defs/OrderChainEntry"
                   },
                   "title": "Open-Entries",
                   "type": "array"
                },
                "total-cost-per-unit": {
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
                   "title": "Total-Cost-Per-Unit"
                }
             },
             "required": [
                "open",
                "updated-at",
                "total-fees",
                "total-commissions",
                "realized-gain",
                "realized-gain-with-fees",
                "winner-realized-and-closed",
                "winner-realized",
                "winner-realized-with-fees",
                "roll-count",
                "opened-at",
                "last-occurred-at",
                "started-at-days-to-expiration",
                "duration",
                "total-opening-cost",
                "total-closing-cost",
                "total-cost",
                "gcd-open-quantity",
                "fees-missing",
                "open-entries"
             ],
             "title": "ComputedData",
             "type": "object"
          },
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
          },
          "OrderChainEntry": {
             "description": "Dataclass containing information about a single order in an order chain.",
             "properties": {
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "quantity": {
                   "title": "Quantity",
                   "type": "string"
                },
                "quantity-type": {
                   "title": "Quantity-Type",
                   "type": "string"
                },
                "quantity-numeric": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Quantity-Numeric"
                }
             },
             "required": [
                "symbol",
                "instrument-type",
                "quantity",
                "quantity-type",
                "quantity-numeric"
             ],
             "title": "OrderChainEntry",
             "type": "object"
          },
          "OrderChainLeg": {
             "description": "Dataclass containing information about a single leg in an order\nfrom an order chain.",
             "properties": {
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "action": {
                   "$ref": "#/$defs/OrderAction"
                },
                "fill-quantity": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Fill-Quantity"
                },
                "order-quantity": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Order-Quantity"
                }
             },
             "required": [
                "symbol",
                "instrument-type",
                "action",
                "fill-quantity",
                "order-quantity"
             ],
             "title": "OrderChainLeg",
             "type": "object"
          },
          "OrderChainNode": {
             "description": "Dataclass containing information about a single node in an order chain.",
             "properties": {
                "node-type": {
                   "title": "Node-Type",
                   "type": "string"
                },
                "id": {
                   "title": "Id",
                   "type": "string"
                },
                "description": {
                   "title": "Description",
                   "type": "string"
                },
                "occurred-at": {
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
                   "title": "Occurred-At"
                },
                "total-fees": {
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
                   "title": "Total-Fees"
                },
                "total-fill-cost": {
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
                   "title": "Total-Fill-Cost"
                },
                "gcd-quantity": {
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
                   "title": "Gcd-Quantity"
                },
                "fill-cost-per-quantity": {
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
                   "title": "Fill-Cost-Per-Quantity"
                },
                "order-fill-count": {
                   "anyOf": [
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Order-Fill-Count"
                },
                "roll": {
                   "anyOf": [
                      {
                         "type": "boolean"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Roll"
                },
                "legs": {
                   "anyOf": [
                      {
                         "items": {
                            "$ref": "#/$defs/OrderChainLeg"
                         },
                         "type": "array"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Legs"
                },
                "entries": {
                   "anyOf": [
                      {
                         "items": {
                            "$ref": "#/$defs/OrderChainEntry"
                         },
                         "type": "array"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Entries"
                }
             },
             "required": [
                "node-type",
                "id",
                "description"
             ],
             "title": "OrderChainNode",
             "type": "object"
          }
       },
       "required": [
          "id",
          "account-number",
          "description",
          "underlying-symbol",
          "computed-data",
          "lite-nodes"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.OrderChain-fields "Permalink to this headline")
    :   * [`account_number (str)`](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.account_number (Python parameter)")
        * [`computed_data (tastytrade.order.ComputedData)`](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.computed_data (Python parameter)")
        * [`created_at (datetime.datetime | None)`](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.created_at (Python parameter)")
        * [`description (str)`](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.description (Python parameter)")
        * [`id (int)`](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.id (Python parameter)")
        * [`lite_nodes (list[tastytrade.order.OrderChainNode])`](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.lite_nodes (Python parameter)")
        * [`lite_nodes_sizes (int | None)`](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.lite_nodes_sizes (Python parameter)")
        * [`underlying_symbol (str)`](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.underlying_symbol (Python parameter)")
        * [`updated_at (datetime.datetime | None)`](order.html#tastytrade.order.OrderChain "tastytrade.order.OrderChain.updated_at (Python parameter)")

*pydantic model* tastytrade.order.OrderChainEntry(*\**, *[symbol](order.html#tastytrade.order.OrderChainEntry "tastytrade.order.OrderChainEntry.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[instrument\_type](order.html#tastytrade.order.OrderChainEntry "tastytrade.order.OrderChainEntry.instrument_type (Python parameter)"): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum")*, *[quantity](order.html#tastytrade.order.OrderChainEntry "tastytrade.order.OrderChainEntry.quantity (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[quantity\_type](order.html#tastytrade.order.OrderChainEntry "tastytrade.order.OrderChainEntry.quantity_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[quantity\_numeric](order.html#tastytrade.order.OrderChainEntry "tastytrade.order.OrderChainEntry.quantity_numeric (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*)[¶](order.html#tastytrade.order.OrderChainEntry "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about a single order in an order chain.

    Show JSON schema

    ```
    {
       "title": "OrderChainEntry",
       "description": "Dataclass containing information about a single order in an order chain.",
       "type": "object",
       "properties": {
          "symbol": {
             "title": "Symbol",
             "type": "string"
          },
          "instrument-type": {
             "$ref": "#/$defs/InstrumentType"
          },
          "quantity": {
             "title": "Quantity",
             "type": "string"
          },
          "quantity-type": {
             "title": "Quantity-Type",
             "type": "string"
          },
          "quantity-numeric": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Quantity-Numeric"
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
          "symbol",
          "instrument-type",
          "quantity",
          "quantity-type",
          "quantity-numeric"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.OrderChainEntry-fields "Permalink to this headline")
    :   * [`instrument_type (tastytrade.order.InstrumentType)`](order.html#tastytrade.order.OrderChainEntry "tastytrade.order.OrderChainEntry.instrument_type (Python parameter)")
        * [`quantity (str)`](order.html#tastytrade.order.OrderChainEntry "tastytrade.order.OrderChainEntry.quantity (Python parameter)")
        * [`quantity_numeric (decimal.Decimal)`](order.html#tastytrade.order.OrderChainEntry "tastytrade.order.OrderChainEntry.quantity_numeric (Python parameter)")
        * [`quantity_type (str)`](order.html#tastytrade.order.OrderChainEntry "tastytrade.order.OrderChainEntry.quantity_type (Python parameter)")
        * [`symbol (str)`](order.html#tastytrade.order.OrderChainEntry "tastytrade.order.OrderChainEntry.symbol (Python parameter)")

*pydantic model* tastytrade.order.OrderChainLeg(*\**, *[symbol](order.html#tastytrade.order.OrderChainLeg "tastytrade.order.OrderChainLeg.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[instrument\_type](order.html#tastytrade.order.OrderChainLeg "tastytrade.order.OrderChainLeg.instrument_type (Python parameter)"): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum")*, *[action](order.html#tastytrade.order.OrderChainLeg "tastytrade.order.OrderChainLeg.action (Python parameter)"): [OrderAction](order.html#tastytrade.order.OrderAction "tastytrade.order.OrderAction (Python enum) — Bases: str, Enum")*, *[fill\_quantity](order.html#tastytrade.order.OrderChainLeg "tastytrade.order.OrderChainLeg.fill_quantity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[order\_quantity](order.html#tastytrade.order.OrderChainLeg "tastytrade.order.OrderChainLeg.order_quantity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*)[¶](order.html#tastytrade.order.OrderChainLeg "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about a single leg in an order
    from an order chain.

    Show JSON schema

    ```
    {
       "title": "OrderChainLeg",
       "description": "Dataclass containing information about a single leg in an order\nfrom an order chain.",
       "type": "object",
       "properties": {
          "symbol": {
             "title": "Symbol",
             "type": "string"
          },
          "instrument-type": {
             "$ref": "#/$defs/InstrumentType"
          },
          "action": {
             "$ref": "#/$defs/OrderAction"
          },
          "fill-quantity": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Fill-Quantity"
          },
          "order-quantity": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Order-Quantity"
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
          "symbol",
          "instrument-type",
          "action",
          "fill-quantity",
          "order-quantity"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.OrderChainLeg-fields "Permalink to this headline")
    :   * [`action (tastytrade.order.OrderAction)`](order.html#tastytrade.order.OrderChainLeg "tastytrade.order.OrderChainLeg.action (Python parameter)")
        * [`fill_quantity (decimal.Decimal)`](order.html#tastytrade.order.OrderChainLeg "tastytrade.order.OrderChainLeg.fill_quantity (Python parameter)")
        * [`instrument_type (tastytrade.order.InstrumentType)`](order.html#tastytrade.order.OrderChainLeg "tastytrade.order.OrderChainLeg.instrument_type (Python parameter)")
        * [`order_quantity (decimal.Decimal)`](order.html#tastytrade.order.OrderChainLeg "tastytrade.order.OrderChainLeg.order_quantity (Python parameter)")
        * [`symbol (str)`](order.html#tastytrade.order.OrderChainLeg "tastytrade.order.OrderChainLeg.symbol (Python parameter)")

*pydantic model* tastytrade.order.OrderChainNode(*\**, *[node\_type](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.node_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[id](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[description](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[occurred\_at](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.occurred_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[total\_fees](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.total_fees (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[total\_fill\_cost](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.total_fill_cost (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[gcd\_quantity](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.gcd_quantity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[fill\_cost\_per\_quantity](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.fill_cost_per_quantity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[order\_fill\_count](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.order_fill_count (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[roll](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.roll (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[legs](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.legs (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[OrderChainLeg](order.html#tastytrade.order.OrderChainLeg "tastytrade.order.OrderChainLeg (Python model) — Bases: TastytradeData")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[entries](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.entries (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[OrderChainEntry](order.html#tastytrade.order.OrderChainEntry "tastytrade.order.OrderChainEntry (Python model) — Bases: TastytradeData")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](order.html#tastytrade.order.OrderChainNode "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about a single node in an order chain.

    Show JSON schema

    ```
    {
       "title": "OrderChainNode",
       "description": "Dataclass containing information about a single node in an order chain.",
       "type": "object",
       "properties": {
          "node-type": {
             "title": "Node-Type",
             "type": "string"
          },
          "id": {
             "title": "Id",
             "type": "string"
          },
          "description": {
             "title": "Description",
             "type": "string"
          },
          "occurred-at": {
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
             "title": "Occurred-At"
          },
          "total-fees": {
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
             "title": "Total-Fees"
          },
          "total-fill-cost": {
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
             "title": "Total-Fill-Cost"
          },
          "gcd-quantity": {
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
             "title": "Gcd-Quantity"
          },
          "fill-cost-per-quantity": {
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
             "title": "Fill-Cost-Per-Quantity"
          },
          "order-fill-count": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Order-Fill-Count"
          },
          "roll": {
             "anyOf": [
                {
                   "type": "boolean"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Roll"
          },
          "legs": {
             "anyOf": [
                {
                   "items": {
                      "$ref": "#/$defs/OrderChainLeg"
                   },
                   "type": "array"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Legs"
          },
          "entries": {
             "anyOf": [
                {
                   "items": {
                      "$ref": "#/$defs/OrderChainEntry"
                   },
                   "type": "array"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Entries"
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
          },
          "OrderChainEntry": {
             "description": "Dataclass containing information about a single order in an order chain.",
             "properties": {
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "quantity": {
                   "title": "Quantity",
                   "type": "string"
                },
                "quantity-type": {
                   "title": "Quantity-Type",
                   "type": "string"
                },
                "quantity-numeric": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Quantity-Numeric"
                }
             },
             "required": [
                "symbol",
                "instrument-type",
                "quantity",
                "quantity-type",
                "quantity-numeric"
             ],
             "title": "OrderChainEntry",
             "type": "object"
          },
          "OrderChainLeg": {
             "description": "Dataclass containing information about a single leg in an order\nfrom an order chain.",
             "properties": {
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "action": {
                   "$ref": "#/$defs/OrderAction"
                },
                "fill-quantity": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Fill-Quantity"
                },
                "order-quantity": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Order-Quantity"
                }
             },
             "required": [
                "symbol",
                "instrument-type",
                "action",
                "fill-quantity",
                "order-quantity"
             ],
             "title": "OrderChainLeg",
             "type": "object"
          }
       },
       "required": [
          "node-type",
          "id",
          "description"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.OrderChainNode-fields "Permalink to this headline")
    :   * [`description (str)`](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.description (Python parameter)")
        * [`entries (list[tastytrade.order.OrderChainEntry] | None)`](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.entries (Python parameter)")
        * [`fill_cost_per_quantity (decimal.Decimal | None)`](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.fill_cost_per_quantity (Python parameter)")
        * [`gcd_quantity (decimal.Decimal | None)`](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.gcd_quantity (Python parameter)")
        * [`id (str)`](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.id (Python parameter)")
        * [`legs (list[tastytrade.order.OrderChainLeg] | None)`](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.legs (Python parameter)")
        * [`node_type (str)`](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.node_type (Python parameter)")
        * [`occurred_at (datetime.datetime | None)`](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.occurred_at (Python parameter)")
        * [`order_fill_count (int | None)`](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.order_fill_count (Python parameter)")
        * [`roll (bool | None)`](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.roll (Python parameter)")
        * [`total_fees (decimal.Decimal | None)`](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.total_fees (Python parameter)")
        * [`total_fill_cost (decimal.Decimal | None)`](order.html#tastytrade.order.OrderChainNode "tastytrade.order.OrderChainNode.total_fill_cost (Python parameter)")

    Validators:[¶](order.html#tastytrade.order.OrderChainNode-validators "Permalink to this headline")
    :   * `validate_price_effects` » `all fields`

*pydantic model* tastytrade.order.OrderCondition(*\**, *[id](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[action](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.action (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[symbol](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[instrument\_type](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.instrument_type (Python parameter)"): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum")*, *[indicator](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.indicator (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[comparator](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.comparator (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[threshold](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.threshold (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[is\_threshold\_based\_on\_notional](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.is_threshold_based_on_notional (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[triggered\_at](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.triggered_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[triggered\_value](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.triggered_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[price\_components](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.price_components (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[OrderConditionPriceComponent](order.html#tastytrade.order.OrderConditionPriceComponent "tastytrade.order.OrderConditionPriceComponent (Python model) — Bases: TastytradeData")]*)[¶](order.html#tastytrade.order.OrderCondition "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass that represents an order condition for an order rule.

    Show JSON schema

    ```
    {
       "title": "OrderCondition",
       "description": "Dataclass that represents an order condition for an order rule.",
       "type": "object",
       "properties": {
          "id": {
             "title": "Id",
             "type": "string"
          },
          "action": {
             "title": "Action",
             "type": "string"
          },
          "symbol": {
             "title": "Symbol",
             "type": "string"
          },
          "instrument-type": {
             "$ref": "#/$defs/InstrumentType"
          },
          "indicator": {
             "title": "Indicator",
             "type": "string"
          },
          "comparator": {
             "title": "Comparator",
             "type": "string"
          },
          "threshold": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Threshold"
          },
          "is-threshold-based-on-notional": {
             "title": "Is-Threshold-Based-On-Notional",
             "type": "boolean"
          },
          "triggered-at": {
             "format": "date-time",
             "title": "Triggered-At",
             "type": "string"
          },
          "triggered-value": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Triggered-Value"
          },
          "price-components": {
             "items": {
                "$ref": "#/$defs/OrderConditionPriceComponent"
             },
             "title": "Price-Components",
             "type": "array"
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
          "OrderConditionPriceComponent": {
             "description": "Dataclass that represents a price component of an order condition.",
             "properties": {
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
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
                }
             },
             "required": [
                "symbol",
                "instrument-type",
                "quantity",
                "quantity-direction"
             ],
             "title": "OrderConditionPriceComponent",
             "type": "object"
          }
       },
       "required": [
          "id",
          "action",
          "symbol",
          "instrument-type",
          "indicator",
          "comparator",
          "threshold",
          "is-threshold-based-on-notional",
          "triggered-at",
          "triggered-value",
          "price-components"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.OrderCondition-fields "Permalink to this headline")
    :   * [`action (str)`](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.action (Python parameter)")
        * [`comparator (str)`](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.comparator (Python parameter)")
        * [`id (str)`](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.id (Python parameter)")
        * [`indicator (str)`](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.indicator (Python parameter)")
        * [`instrument_type (tastytrade.order.InstrumentType)`](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.instrument_type (Python parameter)")
        * [`is_threshold_based_on_notional (bool)`](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.is_threshold_based_on_notional (Python parameter)")
        * [`price_components (list[tastytrade.order.OrderConditionPriceComponent])`](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.price_components (Python parameter)")
        * [`symbol (str)`](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.symbol (Python parameter)")
        * [`threshold (decimal.Decimal)`](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.threshold (Python parameter)")
        * [`triggered_at (datetime.datetime)`](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.triggered_at (Python parameter)")
        * [`triggered_value (decimal.Decimal)`](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition.triggered_value (Python parameter)")

*pydantic model* tastytrade.order.OrderConditionPriceComponent(*\**, *[symbol](order.html#tastytrade.order.OrderConditionPriceComponent "tastytrade.order.OrderConditionPriceComponent.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[instrument\_type](order.html#tastytrade.order.OrderConditionPriceComponent "tastytrade.order.OrderConditionPriceComponent.instrument_type (Python parameter)"): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum")*, *[quantity](order.html#tastytrade.order.OrderConditionPriceComponent "tastytrade.order.OrderConditionPriceComponent.quantity (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[quantity\_direction](order.html#tastytrade.order.OrderConditionPriceComponent "tastytrade.order.OrderConditionPriceComponent.quantity_direction (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)[¶](order.html#tastytrade.order.OrderConditionPriceComponent "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass that represents a price component of an order condition.

    Show JSON schema

    ```
    {
       "title": "OrderConditionPriceComponent",
       "description": "Dataclass that represents a price component of an order condition.",
       "type": "object",
       "properties": {
          "symbol": {
             "title": "Symbol",
             "type": "string"
          },
          "instrument-type": {
             "$ref": "#/$defs/InstrumentType"
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
          "symbol",
          "instrument-type",
          "quantity",
          "quantity-direction"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.OrderConditionPriceComponent-fields "Permalink to this headline")
    :   * [`instrument_type (tastytrade.order.InstrumentType)`](order.html#tastytrade.order.OrderConditionPriceComponent "tastytrade.order.OrderConditionPriceComponent.instrument_type (Python parameter)")
        * [`quantity (decimal.Decimal)`](order.html#tastytrade.order.OrderConditionPriceComponent "tastytrade.order.OrderConditionPriceComponent.quantity (Python parameter)")
        * [`quantity_direction (str)`](order.html#tastytrade.order.OrderConditionPriceComponent "tastytrade.order.OrderConditionPriceComponent.quantity_direction (Python parameter)")
        * [`symbol (str)`](order.html#tastytrade.order.OrderConditionPriceComponent "tastytrade.order.OrderConditionPriceComponent.symbol (Python parameter)")

*pydantic model* tastytrade.order.OrderRule(*\**, *[route\_after](order.html#tastytrade.order.OrderRule "tastytrade.order.OrderRule.route_after (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[routed\_at](order.html#tastytrade.order.OrderRule "tastytrade.order.OrderRule.routed_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[cancel\_at](order.html#tastytrade.order.OrderRule "tastytrade.order.OrderRule.cancel_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[cancelled\_at](order.html#tastytrade.order.OrderRule "tastytrade.order.OrderRule.cancelled_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[order\_conditions](order.html#tastytrade.order.OrderRule "tastytrade.order.OrderRule.order_conditions (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[OrderCondition](order.html#tastytrade.order.OrderCondition "tastytrade.order.OrderCondition (Python model) — Bases: TastytradeData")]*)[¶](order.html#tastytrade.order.OrderRule "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass that represents an order rule for a complex order.

    Show JSON schema

    ```
    {
       "title": "OrderRule",
       "description": "Dataclass that represents an order rule for a complex order.",
       "type": "object",
       "properties": {
          "route-after": {
             "format": "date-time",
             "title": "Route-After",
             "type": "string"
          },
          "routed-at": {
             "format": "date-time",
             "title": "Routed-At",
             "type": "string"
          },
          "cancel-at": {
             "format": "date-time",
             "title": "Cancel-At",
             "type": "string"
          },
          "cancelled-at": {
             "format": "date-time",
             "title": "Cancelled-At",
             "type": "string"
          },
          "order-conditions": {
             "items": {
                "$ref": "#/$defs/OrderCondition"
             },
             "title": "Order-Conditions",
             "type": "array"
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
          "OrderCondition": {
             "description": "Dataclass that represents an order condition for an order rule.",
             "properties": {
                "id": {
                   "title": "Id",
                   "type": "string"
                },
                "action": {
                   "title": "Action",
                   "type": "string"
                },
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "indicator": {
                   "title": "Indicator",
                   "type": "string"
                },
                "comparator": {
                   "title": "Comparator",
                   "type": "string"
                },
                "threshold": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Threshold"
                },
                "is-threshold-based-on-notional": {
                   "title": "Is-Threshold-Based-On-Notional",
                   "type": "boolean"
                },
                "triggered-at": {
                   "format": "date-time",
                   "title": "Triggered-At",
                   "type": "string"
                },
                "triggered-value": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Triggered-Value"
                },
                "price-components": {
                   "items": {
                      "$ref": "#/$defs/OrderConditionPriceComponent"
                   },
                   "title": "Price-Components",
                   "type": "array"
                }
             },
             "required": [
                "id",
                "action",
                "symbol",
                "instrument-type",
                "indicator",
                "comparator",
                "threshold",
                "is-threshold-based-on-notional",
                "triggered-at",
                "triggered-value",
                "price-components"
             ],
             "title": "OrderCondition",
             "type": "object"
          },
          "OrderConditionPriceComponent": {
             "description": "Dataclass that represents a price component of an order condition.",
             "properties": {
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
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
                }
             },
             "required": [
                "symbol",
                "instrument-type",
                "quantity",
                "quantity-direction"
             ],
             "title": "OrderConditionPriceComponent",
             "type": "object"
          }
       },
       "required": [
          "route-after",
          "routed-at",
          "cancel-at",
          "cancelled-at",
          "order-conditions"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.OrderRule-fields "Permalink to this headline")
    :   * [`cancel_at (datetime.datetime)`](order.html#tastytrade.order.OrderRule "tastytrade.order.OrderRule.cancel_at (Python parameter)")
        * [`cancelled_at (datetime.datetime)`](order.html#tastytrade.order.OrderRule "tastytrade.order.OrderRule.cancelled_at (Python parameter)")
        * [`order_conditions (list[tastytrade.order.OrderCondition])`](order.html#tastytrade.order.OrderRule "tastytrade.order.OrderRule.order_conditions (Python parameter)")
        * [`route_after (datetime.datetime)`](order.html#tastytrade.order.OrderRule "tastytrade.order.OrderRule.route_after (Python parameter)")
        * [`routed_at (datetime.datetime)`](order.html#tastytrade.order.OrderRule "tastytrade.order.OrderRule.routed_at (Python parameter)")

*enum* tastytrade.order.OrderStatus(*[value](order.html#tastytrade.order.OrderStatus "tastytrade.order.OrderStatus.value (Python parameter)")*)[¶](order.html#tastytrade.order.OrderStatus "Link to this definition")
:   Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.13)")

    This is an [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.13)") that contains different order statuses.
    A typical (successful) order follows a progression:

    RECEIVED -> LIVE -> FILLED

    Member Type:[¶](order.html#tastytrade.order.OrderStatus-member-type "Permalink to this headline")
    :   [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Valid values are as follows:

    RECEIVED = `<OrderStatus.RECEIVED: 'Received'>`[¶](order.html#tastytrade.order.OrderStatus.RECEIVED "Link to this definition")

    CANCELLED = `<OrderStatus.CANCELLED: 'Cancelled'>`[¶](order.html#tastytrade.order.OrderStatus.CANCELLED "Link to this definition")

    FILLED = `<OrderStatus.FILLED: 'Filled'>`[¶](order.html#tastytrade.order.OrderStatus.FILLED "Link to this definition")

    EXPIRED = `<OrderStatus.EXPIRED: 'Expired'>`[¶](order.html#tastytrade.order.OrderStatus.EXPIRED "Link to this definition")

    LIVE = `<OrderStatus.LIVE: 'Live'>`[¶](order.html#tastytrade.order.OrderStatus.LIVE "Link to this definition")

    REJECTED = `<OrderStatus.REJECTED: 'Rejected'>`[¶](order.html#tastytrade.order.OrderStatus.REJECTED "Link to this definition")

    CONTINGENT = `<OrderStatus.CONTINGENT: 'Contingent'>`[¶](order.html#tastytrade.order.OrderStatus.CONTINGENT "Link to this definition")

    ROUTED = `<OrderStatus.ROUTED: 'Routed'>`[¶](order.html#tastytrade.order.OrderStatus.ROUTED "Link to this definition")

    IN\_FLIGHT = `<OrderStatus.IN_FLIGHT: 'In Flight'>`[¶](order.html#tastytrade.order.OrderStatus.IN_FLIGHT "Link to this definition")

    CANCEL\_REQUESTED = `<OrderStatus.CANCEL_REQUESTED: 'Cancel Requested'>`[¶](order.html#tastytrade.order.OrderStatus.CANCEL_REQUESTED "Link to this definition")

    REPLACE\_REQUESTED = `<OrderStatus.REPLACE_REQUESTED: 'Replace Requested'>`[¶](order.html#tastytrade.order.OrderStatus.REPLACE_REQUESTED "Link to this definition")

    REMOVED = `<OrderStatus.REMOVED: 'Removed'>`[¶](order.html#tastytrade.order.OrderStatus.REMOVED "Link to this definition")

    PARTIALLY\_REMOVED = `<OrderStatus.PARTIALLY_REMOVED: 'Partially Removed'>`[¶](order.html#tastytrade.order.OrderStatus.PARTIALLY_REMOVED "Link to this definition")

*enum* tastytrade.order.OrderTimeInForce(*[value](order.html#tastytrade.order.OrderTimeInForce "tastytrade.order.OrderTimeInForce.value (Python parameter)")*)[¶](order.html#tastytrade.order.OrderTimeInForce "Link to this definition")
:   Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.13)")

    This is an [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.13)") that contains the valid TIFs for orders.

    Member Type:[¶](order.html#tastytrade.order.OrderTimeInForce-member-type "Permalink to this headline")
    :   [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Valid values are as follows:

    DAY = `<OrderTimeInForce.DAY: 'Day'>`[¶](order.html#tastytrade.order.OrderTimeInForce.DAY "Link to this definition")

    GTC = `<OrderTimeInForce.GTC: 'GTC'>`[¶](order.html#tastytrade.order.OrderTimeInForce.GTC "Link to this definition")

    GTD = `<OrderTimeInForce.GTD: 'GTD'>`[¶](order.html#tastytrade.order.OrderTimeInForce.GTD "Link to this definition")

    EXT = `<OrderTimeInForce.EXT: 'Ext'>`[¶](order.html#tastytrade.order.OrderTimeInForce.EXT "Link to this definition")

    GTC\_EXT = `<OrderTimeInForce.GTC_EXT: 'GTC Ext'>`[¶](order.html#tastytrade.order.OrderTimeInForce.GTC_EXT "Link to this definition")

    IOC = `<OrderTimeInForce.IOC: 'IOC'>`[¶](order.html#tastytrade.order.OrderTimeInForce.IOC "Link to this definition")

*enum* tastytrade.order.OrderType(*[value](order.html#tastytrade.order.OrderType "tastytrade.order.OrderType.value (Python parameter)")*)[¶](order.html#tastytrade.order.OrderType "Link to this definition")
:   Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.13)")

    This is an [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.13)") that contains the valid types of orders.

    Member Type:[¶](order.html#tastytrade.order.OrderType-member-type "Permalink to this headline")
    :   [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Valid values are as follows:

    LIMIT = `<OrderType.LIMIT: 'Limit'>`[¶](order.html#tastytrade.order.OrderType.LIMIT "Link to this definition")

    MARKET = `<OrderType.MARKET: 'Market'>`[¶](order.html#tastytrade.order.OrderType.MARKET "Link to this definition")

    MARKETABLE\_LIMIT = `<OrderType.MARKETABLE_LIMIT: 'Marketable Limit'>`[¶](order.html#tastytrade.order.OrderType.MARKETABLE_LIMIT "Link to this definition")

    STOP = `<OrderType.STOP: 'Stop'>`[¶](order.html#tastytrade.order.OrderType.STOP "Link to this definition")

    STOP\_LIMIT = `<OrderType.STOP_LIMIT: 'Stop Limit'>`[¶](order.html#tastytrade.order.OrderType.STOP_LIMIT "Link to this definition")

    NOTIONAL\_MARKET = `<OrderType.NOTIONAL_MARKET: 'Notional Market'>`[¶](order.html#tastytrade.order.OrderType.NOTIONAL_MARKET "Link to this definition")

*pydantic model* tastytrade.order.PlacedComplexOrder(*\**, *[account\_number](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.account_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[type](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[orders](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.orders (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[PlacedOrder](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder (Python model) — Bases: TastytradeData")]*, *[id](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.id (Python parameter) — the ID of the order; test orders placed with dry_run don't have an ID"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `-1`*, *[trigger\_order](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.trigger_order (Python parameter)"): [PlacedOrder](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder (Python model) — Bases: TastytradeData") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[terminal\_at](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.terminal_at (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[ratio\_price\_threshold](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.ratio_price_threshold (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[ratio\_price\_comparator](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.ratio_price_comparator (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[ratio\_price\_is\_threshold\_based\_on\_notional](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.ratio_price_is_threshold_based_on_notional (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[related\_orders](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.related_orders (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](order.html#tastytrade.order.PlacedComplexOrder "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about an already placed complex order.

    Show JSON schema

    ```
    {
       "title": "PlacedComplexOrder",
       "description": "Dataclass containing information about an already placed complex order.",
       "type": "object",
       "properties": {
          "account-number": {
             "title": "Account-Number",
             "type": "string"
          },
          "type": {
             "title": "Type",
             "type": "string"
          },
          "orders": {
             "items": {
                "$ref": "#/$defs/PlacedOrder"
             },
             "title": "Orders",
             "type": "array"
          },
          "id": {
             "default": -1,
             "title": "Id",
             "type": "integer"
          },
          "trigger-order": {
             "anyOf": [
                {
                   "$ref": "#/$defs/PlacedOrder"
                },
                {
                   "type": "null"
                }
             ],
             "default": null
          },
          "terminal-at": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Terminal-At"
          },
          "ratio-price-threshold": {
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
             "title": "Ratio-Price-Threshold"
          },
          "ratio-price-comparator": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Ratio-Price-Comparator"
          },
          "ratio-price-is-threshold-based-on-notional": {
             "anyOf": [
                {
                   "type": "boolean"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Ratio-Price-Is-Threshold-Based-On-Notional"
          },
          "related-orders": {
             "anyOf": [
                {
                   "items": {
                      "additionalProperties": {
                         "type": "string"
                      },
                      "type": "object"
                   },
                   "type": "array"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Related-Orders"
          }
       },
       "$defs": {
          "FillInfo": {
             "description": "Dataclass that contains information about an order fill.",
             "properties": {
                "fill-id": {
                   "title": "Fill-Id",
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
                "fill-price": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Fill-Price"
                },
                "filled-at": {
                   "format": "date-time",
                   "title": "Filled-At",
                   "type": "string"
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
                }
             },
             "required": [
                "fill-id",
                "quantity",
                "fill-price",
                "filled-at"
             ],
             "title": "FillInfo",
             "type": "object"
          },
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
          "Leg": {
             "description": "Dataclass that represents an order leg.\n\nClasses that inherit from :class:`TradeableTastytradeJsonDataclass` can\ncall :meth:`build_leg` to build a leg from the dataclass.",
             "properties": {
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "action": {
                   "$ref": "#/$defs/OrderAction"
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
                "remaining-quantity": {
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
                   "title": "Remaining-Quantity"
                },
                "fills": {
                   "anyOf": [
                      {
                         "items": {
                            "$ref": "#/$defs/FillInfo"
                         },
                         "type": "array"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Fills"
                }
             },
             "required": [
                "instrument-type",
                "symbol",
                "action"
             ],
             "title": "Leg",
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
          },
          "OrderCondition": {
             "description": "Dataclass that represents an order condition for an order rule.",
             "properties": {
                "id": {
                   "title": "Id",
                   "type": "string"
                },
                "action": {
                   "title": "Action",
                   "type": "string"
                },
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "indicator": {
                   "title": "Indicator",
                   "type": "string"
                },
                "comparator": {
                   "title": "Comparator",
                   "type": "string"
                },
                "threshold": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Threshold"
                },
                "is-threshold-based-on-notional": {
                   "title": "Is-Threshold-Based-On-Notional",
                   "type": "boolean"
                },
                "triggered-at": {
                   "format": "date-time",
                   "title": "Triggered-At",
                   "type": "string"
                },
                "triggered-value": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Triggered-Value"
                },
                "price-components": {
                   "items": {
                      "$ref": "#/$defs/OrderConditionPriceComponent"
                   },
                   "title": "Price-Components",
                   "type": "array"
                }
             },
             "required": [
                "id",
                "action",
                "symbol",
                "instrument-type",
                "indicator",
                "comparator",
                "threshold",
                "is-threshold-based-on-notional",
                "triggered-at",
                "triggered-value",
                "price-components"
             ],
             "title": "OrderCondition",
             "type": "object"
          },
          "OrderConditionPriceComponent": {
             "description": "Dataclass that represents a price component of an order condition.",
             "properties": {
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
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
                }
             },
             "required": [
                "symbol",
                "instrument-type",
                "quantity",
                "quantity-direction"
             ],
             "title": "OrderConditionPriceComponent",
             "type": "object"
          },
          "OrderRule": {
             "description": "Dataclass that represents an order rule for a complex order.",
             "properties": {
                "route-after": {
                   "format": "date-time",
                   "title": "Route-After",
                   "type": "string"
                },
                "routed-at": {
                   "format": "date-time",
                   "title": "Routed-At",
                   "type": "string"
                },
                "cancel-at": {
                   "format": "date-time",
                   "title": "Cancel-At",
                   "type": "string"
                },
                "cancelled-at": {
                   "format": "date-time",
                   "title": "Cancelled-At",
                   "type": "string"
                },
                "order-conditions": {
                   "items": {
                      "$ref": "#/$defs/OrderCondition"
                   },
                   "title": "Order-Conditions",
                   "type": "array"
                }
             },
             "required": [
                "route-after",
                "routed-at",
                "cancel-at",
                "cancelled-at",
                "order-conditions"
             ],
             "title": "OrderRule",
             "type": "object"
          },
          "OrderStatus": {
             "description": "This is an :class:`~enum.Enum` that contains different order statuses.\nA typical (successful) order follows a progression:\n\nRECEIVED -> LIVE -> FILLED",
             "enum": [
                "Received",
                "Cancelled",
                "Filled",
                "Expired",
                "Live",
                "Rejected",
                "Contingent",
                "Routed",
                "In Flight",
                "Cancel Requested",
                "Replace Requested",
                "Removed",
                "Partially Removed"
             ],
             "title": "OrderStatus",
             "type": "string"
          },
          "OrderTimeInForce": {
             "description": "This is an :class:`~enum.Enum` that contains the valid TIFs for orders.",
             "enum": [
                "Day",
                "GTC",
                "GTD",
                "Ext",
                "GTC Ext",
                "IOC"
             ],
             "title": "OrderTimeInForce",
             "type": "string"
          },
          "OrderType": {
             "description": "This is an :class:`~enum.Enum` that contains the valid types of orders.",
             "enum": [
                "Limit",
                "Market",
                "Marketable Limit",
                "Stop",
                "Stop Limit",
                "Notional Market"
             ],
             "title": "OrderType",
             "type": "string"
          },
          "PlacedOrder": {
             "description": "Dataclass containing information about an existing order, whether it's\nbeen filled or not.",
             "properties": {
                "account-number": {
                   "title": "Account-Number",
                   "type": "string"
                },
                "time-in-force": {
                   "$ref": "#/$defs/OrderTimeInForce"
                },
                "order-type": {
                   "$ref": "#/$defs/OrderType"
                },
                "underlying-symbol": {
                   "title": "Underlying-Symbol",
                   "type": "string"
                },
                "underlying-instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "status": {
                   "$ref": "#/$defs/OrderStatus"
                },
                "cancellable": {
                   "title": "Cancellable",
                   "type": "boolean"
                },
                "editable": {
                   "title": "Editable",
                   "type": "boolean"
                },
                "edited": {
                   "title": "Edited",
                   "type": "boolean"
                },
                "updated-at": {
                   "format": "date-time",
                   "title": "Updated-At",
                   "type": "string"
                },
                "legs": {
                   "items": {
                      "$ref": "#/$defs/Leg"
                   },
                   "title": "Legs",
                   "type": "array"
                },
                "id": {
                   "default": -1,
                   "title": "Id",
                   "type": "integer"
                },
                "size": {
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
                   "title": "Size"
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
                "gtc-date": {
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
                   "title": "Gtc-Date"
                },
                "value": {
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
                   "title": "Value"
                },
                "stop-trigger": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Stop-Trigger"
                },
                "contingent-status": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Contingent-Status"
                },
                "confirmation-status": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Confirmation-Status"
                },
                "cancelled-at": {
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
                   "title": "Cancelled-At"
                },
                "cancel-user-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Cancel-User-Id"
                },
                "cancel-username": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Cancel-Username"
                },
                "replacing-order-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Replacing-Order-Id"
                },
                "replaces-order-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Replaces-Order-Id"
                },
                "in-flight-at": {
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
                   "title": "In-Flight-At"
                },
                "live-at": {
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
                   "title": "Live-At"
                },
                "received-at": {
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
                   "title": "Received-At"
                },
                "reject-reason": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Reject-Reason"
                },
                "user-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "User-Id"
                },
                "username": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Username"
                },
                "terminal-at": {
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
                   "title": "Terminal-At"
                },
                "complex-order-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Complex-Order-Id"
                },
                "complex-order-tag": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Complex-Order-Tag"
                },
                "preflight-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Preflight-Id"
                },
                "order-rule": {
                   "anyOf": [
                      {
                         "$ref": "#/$defs/OrderRule"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null
                },
                "source": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Source"
                }
             },
             "required": [
                "account-number",
                "time-in-force",
                "order-type",
                "underlying-symbol",
                "underlying-instrument-type",
                "status",
                "cancellable",
                "editable",
                "edited",
                "updated-at",
                "legs"
             ],
             "title": "PlacedOrder",
             "type": "object"
          }
       },
       "required": [
          "account-number",
          "type",
          "orders"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.PlacedComplexOrder-fields "Permalink to this headline")
    :   * [`account_number (str)`](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.account_number (Python parameter)")
        * [`id (int)`](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.id (Python parameter) — the ID of the order; test orders placed with dry_run don't have an ID")
        * [`orders (list[tastytrade.order.PlacedOrder])`](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.orders (Python parameter)")
        * [`ratio_price_comparator (str | None)`](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.ratio_price_comparator (Python parameter)")
        * [`ratio_price_is_threshold_based_on_notional (bool | None)`](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.ratio_price_is_threshold_based_on_notional (Python parameter)")
        * [`ratio_price_threshold (decimal.Decimal | None)`](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.ratio_price_threshold (Python parameter)")
        * [`related_orders (list[dict[str, str]] | None)`](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.related_orders (Python parameter)")
        * [`terminal_at (str | None)`](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.terminal_at (Python parameter)")
        * [`trigger_order (tastytrade.order.PlacedOrder | None)`](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.trigger_order (Python parameter)")
        * [`type (str)`](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder.type (Python parameter)")

    *field* id : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `-1`[¶](order.html#tastytrade.order.PlacedComplexOrder.id "Link to this definition")
    :   the ID of the order; test orders placed with dry\_run don’t have an ID

*pydantic model* tastytrade.order.PlacedComplexOrderResponse(*\**, *[buying\_power\_effect](order.html#tastytrade.order.PlacedComplexOrderResponse "tastytrade.order.PlacedComplexOrderResponse.buying_power_effect (Python parameter)"): [BuyingPowerEffect](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect (Python model) — Bases: TastytradeData")*, *[complex\_order](order.html#tastytrade.order.PlacedComplexOrderResponse "tastytrade.order.PlacedComplexOrderResponse.complex_order (Python parameter)"): [PlacedComplexOrder](order.html#tastytrade.order.PlacedComplexOrder "tastytrade.order.PlacedComplexOrder (Python model) — Bases: TastytradeData")*, *[fee\_calculation](order.html#tastytrade.order.PlacedComplexOrderResponse "tastytrade.order.PlacedComplexOrderResponse.fee_calculation (Python parameter)"): [FeeCalculation](order.html#tastytrade.order.FeeCalculation "tastytrade.order.FeeCalculation (Python model) — Bases: TastytradeData") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[warnings](order.html#tastytrade.order.PlacedComplexOrderResponse "tastytrade.order.PlacedComplexOrderResponse.warnings (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[Message](order.html#tastytrade.order.Message "tastytrade.order.Message (Python model) — Bases: TastytradeData")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[errors](order.html#tastytrade.order.PlacedComplexOrderResponse "tastytrade.order.PlacedComplexOrderResponse.errors (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[Message](order.html#tastytrade.order.Message "tastytrade.order.Message (Python model) — Bases: TastytradeData")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](order.html#tastytrade.order.PlacedComplexOrderResponse "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass grouping together information about a placed complex order.

    Show JSON schema

    ```
    {
       "title": "PlacedComplexOrderResponse",
       "description": "Dataclass grouping together information about a placed complex order.",
       "type": "object",
       "properties": {
          "buying-power-effect": {
             "$ref": "#/$defs/BuyingPowerEffect"
          },
          "complex-order": {
             "$ref": "#/$defs/PlacedComplexOrder"
          },
          "fee-calculation": {
             "anyOf": [
                {
                   "$ref": "#/$defs/FeeCalculation"
                },
                {
                   "type": "null"
                }
             ],
             "default": null
          },
          "warnings": {
             "anyOf": [
                {
                   "items": {
                      "$ref": "#/$defs/Message"
                   },
                   "type": "array"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Warnings"
          },
          "errors": {
             "anyOf": [
                {
                   "items": {
                      "$ref": "#/$defs/Message"
                   },
                   "type": "array"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Errors"
          }
       },
       "$defs": {
          "BuyingPowerEffect": {
             "description": "Dataclass containing information about the effect of a trade on buying\npower.",
             "properties": {
                "change-in-margin-requirement": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Change-In-Margin-Requirement"
                },
                "change-in-buying-power": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Change-In-Buying-Power"
                },
                "current-buying-power": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Current-Buying-Power"
                },
                "new-buying-power": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "New-Buying-Power"
                },
                "isolated-order-margin-requirement": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Isolated-Order-Margin-Requirement"
                },
                "is-spread": {
                   "title": "Is-Spread",
                   "type": "boolean"
                },
                "impact": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Impact"
                },
                "effect": {
                   "$ref": "#/$defs/PriceEffect"
                }
             },
             "required": [
                "change-in-margin-requirement",
                "change-in-buying-power",
                "current-buying-power",
                "new-buying-power",
                "isolated-order-margin-requirement",
                "is-spread",
                "impact",
                "effect"
             ],
             "title": "BuyingPowerEffect",
             "type": "object"
          },
          "FeeCalculation": {
             "description": "Dataclass containing information about the fees associated with a trade.",
             "properties": {
                "regulatory-fees": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Regulatory-Fees"
                },
                "clearing-fees": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Clearing-Fees"
                },
                "commission": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Commission"
                },
                "proprietary-index-option-fees": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Proprietary-Index-Option-Fees"
                },
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
                "regulatory-fees",
                "clearing-fees",
                "commission",
                "proprietary-index-option-fees",
                "total-fees"
             ],
             "title": "FeeCalculation",
             "type": "object"
          },
          "FillInfo": {
             "description": "Dataclass that contains information about an order fill.",
             "properties": {
                "fill-id": {
                   "title": "Fill-Id",
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
                "fill-price": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Fill-Price"
                },
                "filled-at": {
                   "format": "date-time",
                   "title": "Filled-At",
                   "type": "string"
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
                }
             },
             "required": [
                "fill-id",
                "quantity",
                "fill-price",
                "filled-at"
             ],
             "title": "FillInfo",
             "type": "object"
          },
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
          "Leg": {
             "description": "Dataclass that represents an order leg.\n\nClasses that inherit from :class:`TradeableTastytradeJsonDataclass` can\ncall :meth:`build_leg` to build a leg from the dataclass.",
             "properties": {
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "action": {
                   "$ref": "#/$defs/OrderAction"
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
                "remaining-quantity": {
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
                   "title": "Remaining-Quantity"
                },
                "fills": {
                   "anyOf": [
                      {
                         "items": {
                            "$ref": "#/$defs/FillInfo"
                         },
                         "type": "array"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Fills"
                }
             },
             "required": [
                "instrument-type",
                "symbol",
                "action"
             ],
             "title": "Leg",
             "type": "object"
          },
          "Message": {
             "description": "Dataclass that represents a message from the Tastytrade API, usually\na warning or an error.",
             "properties": {
                "code": {
                   "title": "Code",
                   "type": "string"
                },
                "message": {
                   "title": "Message",
                   "type": "string"
                },
                "preflight-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Preflight-Id"
                }
             },
             "required": [
                "code",
                "message"
             ],
             "title": "Message",
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
          },
          "OrderCondition": {
             "description": "Dataclass that represents an order condition for an order rule.",
             "properties": {
                "id": {
                   "title": "Id",
                   "type": "string"
                },
                "action": {
                   "title": "Action",
                   "type": "string"
                },
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "indicator": {
                   "title": "Indicator",
                   "type": "string"
                },
                "comparator": {
                   "title": "Comparator",
                   "type": "string"
                },
                "threshold": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Threshold"
                },
                "is-threshold-based-on-notional": {
                   "title": "Is-Threshold-Based-On-Notional",
                   "type": "boolean"
                },
                "triggered-at": {
                   "format": "date-time",
                   "title": "Triggered-At",
                   "type": "string"
                },
                "triggered-value": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Triggered-Value"
                },
                "price-components": {
                   "items": {
                      "$ref": "#/$defs/OrderConditionPriceComponent"
                   },
                   "title": "Price-Components",
                   "type": "array"
                }
             },
             "required": [
                "id",
                "action",
                "symbol",
                "instrument-type",
                "indicator",
                "comparator",
                "threshold",
                "is-threshold-based-on-notional",
                "triggered-at",
                "triggered-value",
                "price-components"
             ],
             "title": "OrderCondition",
             "type": "object"
          },
          "OrderConditionPriceComponent": {
             "description": "Dataclass that represents a price component of an order condition.",
             "properties": {
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
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
                }
             },
             "required": [
                "symbol",
                "instrument-type",
                "quantity",
                "quantity-direction"
             ],
             "title": "OrderConditionPriceComponent",
             "type": "object"
          },
          "OrderRule": {
             "description": "Dataclass that represents an order rule for a complex order.",
             "properties": {
                "route-after": {
                   "format": "date-time",
                   "title": "Route-After",
                   "type": "string"
                },
                "routed-at": {
                   "format": "date-time",
                   "title": "Routed-At",
                   "type": "string"
                },
                "cancel-at": {
                   "format": "date-time",
                   "title": "Cancel-At",
                   "type": "string"
                },
                "cancelled-at": {
                   "format": "date-time",
                   "title": "Cancelled-At",
                   "type": "string"
                },
                "order-conditions": {
                   "items": {
                      "$ref": "#/$defs/OrderCondition"
                   },
                   "title": "Order-Conditions",
                   "type": "array"
                }
             },
             "required": [
                "route-after",
                "routed-at",
                "cancel-at",
                "cancelled-at",
                "order-conditions"
             ],
             "title": "OrderRule",
             "type": "object"
          },
          "OrderStatus": {
             "description": "This is an :class:`~enum.Enum` that contains different order statuses.\nA typical (successful) order follows a progression:\n\nRECEIVED -> LIVE -> FILLED",
             "enum": [
                "Received",
                "Cancelled",
                "Filled",
                "Expired",
                "Live",
                "Rejected",
                "Contingent",
                "Routed",
                "In Flight",
                "Cancel Requested",
                "Replace Requested",
                "Removed",
                "Partially Removed"
             ],
             "title": "OrderStatus",
             "type": "string"
          },
          "OrderTimeInForce": {
             "description": "This is an :class:`~enum.Enum` that contains the valid TIFs for orders.",
             "enum": [
                "Day",
                "GTC",
                "GTD",
                "Ext",
                "GTC Ext",
                "IOC"
             ],
             "title": "OrderTimeInForce",
             "type": "string"
          },
          "OrderType": {
             "description": "This is an :class:`~enum.Enum` that contains the valid types of orders.",
             "enum": [
                "Limit",
                "Market",
                "Marketable Limit",
                "Stop",
                "Stop Limit",
                "Notional Market"
             ],
             "title": "OrderType",
             "type": "string"
          },
          "PlacedComplexOrder": {
             "description": "Dataclass containing information about an already placed complex order.",
             "properties": {
                "account-number": {
                   "title": "Account-Number",
                   "type": "string"
                },
                "type": {
                   "title": "Type",
                   "type": "string"
                },
                "orders": {
                   "items": {
                      "$ref": "#/$defs/PlacedOrder"
                   },
                   "title": "Orders",
                   "type": "array"
                },
                "id": {
                   "default": -1,
                   "title": "Id",
                   "type": "integer"
                },
                "trigger-order": {
                   "anyOf": [
                      {
                         "$ref": "#/$defs/PlacedOrder"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null
                },
                "terminal-at": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Terminal-At"
                },
                "ratio-price-threshold": {
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
                   "title": "Ratio-Price-Threshold"
                },
                "ratio-price-comparator": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Ratio-Price-Comparator"
                },
                "ratio-price-is-threshold-based-on-notional": {
                   "anyOf": [
                      {
                         "type": "boolean"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Ratio-Price-Is-Threshold-Based-On-Notional"
                },
                "related-orders": {
                   "anyOf": [
                      {
                         "items": {
                            "additionalProperties": {
                               "type": "string"
                            },
                            "type": "object"
                         },
                         "type": "array"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Related-Orders"
                }
             },
             "required": [
                "account-number",
                "type",
                "orders"
             ],
             "title": "PlacedComplexOrder",
             "type": "object"
          },
          "PlacedOrder": {
             "description": "Dataclass containing information about an existing order, whether it's\nbeen filled or not.",
             "properties": {
                "account-number": {
                   "title": "Account-Number",
                   "type": "string"
                },
                "time-in-force": {
                   "$ref": "#/$defs/OrderTimeInForce"
                },
                "order-type": {
                   "$ref": "#/$defs/OrderType"
                },
                "underlying-symbol": {
                   "title": "Underlying-Symbol",
                   "type": "string"
                },
                "underlying-instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "status": {
                   "$ref": "#/$defs/OrderStatus"
                },
                "cancellable": {
                   "title": "Cancellable",
                   "type": "boolean"
                },
                "editable": {
                   "title": "Editable",
                   "type": "boolean"
                },
                "edited": {
                   "title": "Edited",
                   "type": "boolean"
                },
                "updated-at": {
                   "format": "date-time",
                   "title": "Updated-At",
                   "type": "string"
                },
                "legs": {
                   "items": {
                      "$ref": "#/$defs/Leg"
                   },
                   "title": "Legs",
                   "type": "array"
                },
                "id": {
                   "default": -1,
                   "title": "Id",
                   "type": "integer"
                },
                "size": {
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
                   "title": "Size"
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
                "gtc-date": {
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
                   "title": "Gtc-Date"
                },
                "value": {
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
                   "title": "Value"
                },
                "stop-trigger": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Stop-Trigger"
                },
                "contingent-status": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Contingent-Status"
                },
                "confirmation-status": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Confirmation-Status"
                },
                "cancelled-at": {
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
                   "title": "Cancelled-At"
                },
                "cancel-user-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Cancel-User-Id"
                },
                "cancel-username": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Cancel-Username"
                },
                "replacing-order-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Replacing-Order-Id"
                },
                "replaces-order-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Replaces-Order-Id"
                },
                "in-flight-at": {
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
                   "title": "In-Flight-At"
                },
                "live-at": {
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
                   "title": "Live-At"
                },
                "received-at": {
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
                   "title": "Received-At"
                },
                "reject-reason": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Reject-Reason"
                },
                "user-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "User-Id"
                },
                "username": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Username"
                },
                "terminal-at": {
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
                   "title": "Terminal-At"
                },
                "complex-order-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Complex-Order-Id"
                },
                "complex-order-tag": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Complex-Order-Tag"
                },
                "preflight-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Preflight-Id"
                },
                "order-rule": {
                   "anyOf": [
                      {
                         "$ref": "#/$defs/OrderRule"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null
                },
                "source": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Source"
                }
             },
             "required": [
                "account-number",
                "time-in-force",
                "order-type",
                "underlying-symbol",
                "underlying-instrument-type",
                "status",
                "cancellable",
                "editable",
                "edited",
                "updated-at",
                "legs"
             ],
             "title": "PlacedOrder",
             "type": "object"
          },
          "PriceEffect": {
             "description": "This is an :class:`~enum.Enum` that shows the sign of a price effect, since\nTastytrade is apparently against negative numbers.",
             "enum": [
                "Credit",
                "Debit",
                "None"
             ],
             "title": "PriceEffect",
             "type": "string"
          }
       },
       "required": [
          "buying-power-effect",
          "complex-order"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.PlacedComplexOrderResponse-fields "Permalink to this headline")
    :   * [`buying_power_effect (tastytrade.order.BuyingPowerEffect)`](order.html#tastytrade.order.PlacedComplexOrderResponse "tastytrade.order.PlacedComplexOrderResponse.buying_power_effect (Python parameter)")
        * [`complex_order (tastytrade.order.PlacedComplexOrder)`](order.html#tastytrade.order.PlacedComplexOrderResponse "tastytrade.order.PlacedComplexOrderResponse.complex_order (Python parameter)")
        * [`errors (list[tastytrade.order.Message] | None)`](order.html#tastytrade.order.PlacedComplexOrderResponse "tastytrade.order.PlacedComplexOrderResponse.errors (Python parameter)")
        * [`fee_calculation (tastytrade.order.FeeCalculation | None)`](order.html#tastytrade.order.PlacedComplexOrderResponse "tastytrade.order.PlacedComplexOrderResponse.fee_calculation (Python parameter)")
        * [`warnings (list[tastytrade.order.Message] | None)`](order.html#tastytrade.order.PlacedComplexOrderResponse "tastytrade.order.PlacedComplexOrderResponse.warnings (Python parameter)")

*pydantic model* tastytrade.order.PlacedOrder(*\**, *[account\_number](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.account_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[time\_in\_force](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.time_in_force (Python parameter)"): [OrderTimeInForce](order.html#tastytrade.order.OrderTimeInForce "tastytrade.order.OrderTimeInForce (Python enum) — Bases: str, Enum")*, *[order\_type](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.order_type (Python parameter)"): [OrderType](order.html#tastytrade.order.OrderType "tastytrade.order.OrderType (Python enum) — Bases: str, Enum")*, *[underlying\_symbol](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.underlying_symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[underlying\_instrument\_type](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.underlying_instrument_type (Python parameter)"): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum")*, *[status](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.status (Python parameter)"): [OrderStatus](order.html#tastytrade.order.OrderStatus "tastytrade.order.OrderStatus (Python enum) — Bases: str, Enum")*, *[cancellable](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.cancellable (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[editable](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.editable (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[edited](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.edited (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[updated\_at](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.updated_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[legs](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.legs (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[Leg](order.html#tastytrade.order.Leg "tastytrade.order.Leg (Python model) — Bases: TastytradeData")]*, *[id](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.id (Python parameter) — the ID of the order; test orders placed with dry_run don't have an ID"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `-1`*, *[size](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.size (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[price](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.price (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[gtc\_date](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.gtc_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[value](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[stop\_trigger](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.stop_trigger (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[contingent\_status](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.contingent_status (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[confirmation\_status](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.confirmation_status (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[cancelled\_at](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.cancelled_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[cancel\_user\_id](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.cancel_user_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[cancel\_username](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.cancel_username (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[replacing\_order\_id](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.replacing_order_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[replaces\_order\_id](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.replaces_order_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[in\_flight\_at](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.in_flight_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[live\_at](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.live_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[received\_at](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.received_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[reject\_reason](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.reject_reason (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[user\_id](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.user_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[username](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.username (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[terminal\_at](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.terminal_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[complex\_order\_id](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.complex_order_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[complex\_order\_tag](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.complex_order_tag (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[preflight\_id](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.preflight_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[order\_rule](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.order_rule (Python parameter)"): [OrderRule](order.html#tastytrade.order.OrderRule "tastytrade.order.OrderRule (Python model) — Bases: TastytradeData") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[source](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.source (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](order.html#tastytrade.order.PlacedOrder "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about an existing order, whether it’s
    been filled or not.

    Show JSON schema

    ```
    {
       "title": "PlacedOrder",
       "description": "Dataclass containing information about an existing order, whether it's\nbeen filled or not.",
       "type": "object",
       "properties": {
          "account-number": {
             "title": "Account-Number",
             "type": "string"
          },
          "time-in-force": {
             "$ref": "#/$defs/OrderTimeInForce"
          },
          "order-type": {
             "$ref": "#/$defs/OrderType"
          },
          "underlying-symbol": {
             "title": "Underlying-Symbol",
             "type": "string"
          },
          "underlying-instrument-type": {
             "$ref": "#/$defs/InstrumentType"
          },
          "status": {
             "$ref": "#/$defs/OrderStatus"
          },
          "cancellable": {
             "title": "Cancellable",
             "type": "boolean"
          },
          "editable": {
             "title": "Editable",
             "type": "boolean"
          },
          "edited": {
             "title": "Edited",
             "type": "boolean"
          },
          "updated-at": {
             "format": "date-time",
             "title": "Updated-At",
             "type": "string"
          },
          "legs": {
             "items": {
                "$ref": "#/$defs/Leg"
             },
             "title": "Legs",
             "type": "array"
          },
          "id": {
             "default": -1,
             "title": "Id",
             "type": "integer"
          },
          "size": {
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
             "title": "Size"
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
          "gtc-date": {
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
             "title": "Gtc-Date"
          },
          "value": {
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
             "title": "Value"
          },
          "stop-trigger": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Stop-Trigger"
          },
          "contingent-status": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Contingent-Status"
          },
          "confirmation-status": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Confirmation-Status"
          },
          "cancelled-at": {
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
             "title": "Cancelled-At"
          },
          "cancel-user-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Cancel-User-Id"
          },
          "cancel-username": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Cancel-Username"
          },
          "replacing-order-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Replacing-Order-Id"
          },
          "replaces-order-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Replaces-Order-Id"
          },
          "in-flight-at": {
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
             "title": "In-Flight-At"
          },
          "live-at": {
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
             "title": "Live-At"
          },
          "received-at": {
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
             "title": "Received-At"
          },
          "reject-reason": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Reject-Reason"
          },
          "user-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "User-Id"
          },
          "username": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Username"
          },
          "terminal-at": {
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
             "title": "Terminal-At"
          },
          "complex-order-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Complex-Order-Id"
          },
          "complex-order-tag": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Complex-Order-Tag"
          },
          "preflight-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Preflight-Id"
          },
          "order-rule": {
             "anyOf": [
                {
                   "$ref": "#/$defs/OrderRule"
                },
                {
                   "type": "null"
                }
             ],
             "default": null
          },
          "source": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Source"
          }
       },
       "$defs": {
          "FillInfo": {
             "description": "Dataclass that contains information about an order fill.",
             "properties": {
                "fill-id": {
                   "title": "Fill-Id",
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
                "fill-price": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Fill-Price"
                },
                "filled-at": {
                   "format": "date-time",
                   "title": "Filled-At",
                   "type": "string"
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
                }
             },
             "required": [
                "fill-id",
                "quantity",
                "fill-price",
                "filled-at"
             ],
             "title": "FillInfo",
             "type": "object"
          },
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
          "Leg": {
             "description": "Dataclass that represents an order leg.\n\nClasses that inherit from :class:`TradeableTastytradeJsonDataclass` can\ncall :meth:`build_leg` to build a leg from the dataclass.",
             "properties": {
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "action": {
                   "$ref": "#/$defs/OrderAction"
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
                "remaining-quantity": {
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
                   "title": "Remaining-Quantity"
                },
                "fills": {
                   "anyOf": [
                      {
                         "items": {
                            "$ref": "#/$defs/FillInfo"
                         },
                         "type": "array"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Fills"
                }
             },
             "required": [
                "instrument-type",
                "symbol",
                "action"
             ],
             "title": "Leg",
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
          },
          "OrderCondition": {
             "description": "Dataclass that represents an order condition for an order rule.",
             "properties": {
                "id": {
                   "title": "Id",
                   "type": "string"
                },
                "action": {
                   "title": "Action",
                   "type": "string"
                },
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "indicator": {
                   "title": "Indicator",
                   "type": "string"
                },
                "comparator": {
                   "title": "Comparator",
                   "type": "string"
                },
                "threshold": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Threshold"
                },
                "is-threshold-based-on-notional": {
                   "title": "Is-Threshold-Based-On-Notional",
                   "type": "boolean"
                },
                "triggered-at": {
                   "format": "date-time",
                   "title": "Triggered-At",
                   "type": "string"
                },
                "triggered-value": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Triggered-Value"
                },
                "price-components": {
                   "items": {
                      "$ref": "#/$defs/OrderConditionPriceComponent"
                   },
                   "title": "Price-Components",
                   "type": "array"
                }
             },
             "required": [
                "id",
                "action",
                "symbol",
                "instrument-type",
                "indicator",
                "comparator",
                "threshold",
                "is-threshold-based-on-notional",
                "triggered-at",
                "triggered-value",
                "price-components"
             ],
             "title": "OrderCondition",
             "type": "object"
          },
          "OrderConditionPriceComponent": {
             "description": "Dataclass that represents a price component of an order condition.",
             "properties": {
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
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
                }
             },
             "required": [
                "symbol",
                "instrument-type",
                "quantity",
                "quantity-direction"
             ],
             "title": "OrderConditionPriceComponent",
             "type": "object"
          },
          "OrderRule": {
             "description": "Dataclass that represents an order rule for a complex order.",
             "properties": {
                "route-after": {
                   "format": "date-time",
                   "title": "Route-After",
                   "type": "string"
                },
                "routed-at": {
                   "format": "date-time",
                   "title": "Routed-At",
                   "type": "string"
                },
                "cancel-at": {
                   "format": "date-time",
                   "title": "Cancel-At",
                   "type": "string"
                },
                "cancelled-at": {
                   "format": "date-time",
                   "title": "Cancelled-At",
                   "type": "string"
                },
                "order-conditions": {
                   "items": {
                      "$ref": "#/$defs/OrderCondition"
                   },
                   "title": "Order-Conditions",
                   "type": "array"
                }
             },
             "required": [
                "route-after",
                "routed-at",
                "cancel-at",
                "cancelled-at",
                "order-conditions"
             ],
             "title": "OrderRule",
             "type": "object"
          },
          "OrderStatus": {
             "description": "This is an :class:`~enum.Enum` that contains different order statuses.\nA typical (successful) order follows a progression:\n\nRECEIVED -> LIVE -> FILLED",
             "enum": [
                "Received",
                "Cancelled",
                "Filled",
                "Expired",
                "Live",
                "Rejected",
                "Contingent",
                "Routed",
                "In Flight",
                "Cancel Requested",
                "Replace Requested",
                "Removed",
                "Partially Removed"
             ],
             "title": "OrderStatus",
             "type": "string"
          },
          "OrderTimeInForce": {
             "description": "This is an :class:`~enum.Enum` that contains the valid TIFs for orders.",
             "enum": [
                "Day",
                "GTC",
                "GTD",
                "Ext",
                "GTC Ext",
                "IOC"
             ],
             "title": "OrderTimeInForce",
             "type": "string"
          },
          "OrderType": {
             "description": "This is an :class:`~enum.Enum` that contains the valid types of orders.",
             "enum": [
                "Limit",
                "Market",
                "Marketable Limit",
                "Stop",
                "Stop Limit",
                "Notional Market"
             ],
             "title": "OrderType",
             "type": "string"
          }
       },
       "required": [
          "account-number",
          "time-in-force",
          "order-type",
          "underlying-symbol",
          "underlying-instrument-type",
          "status",
          "cancellable",
          "editable",
          "edited",
          "updated-at",
          "legs"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.PlacedOrder-fields "Permalink to this headline")
    :   * [`account_number (str)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.account_number (Python parameter)")
        * [`cancel_user_id (str | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.cancel_user_id (Python parameter)")
        * [`cancel_username (str | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.cancel_username (Python parameter)")
        * [`cancellable (bool)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.cancellable (Python parameter)")
        * [`cancelled_at (datetime.datetime | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.cancelled_at (Python parameter)")
        * [`complex_order_id (str | int | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.complex_order_id (Python parameter)")
        * [`complex_order_tag (str | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.complex_order_tag (Python parameter)")
        * [`confirmation_status (str | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.confirmation_status (Python parameter)")
        * [`contingent_status (str | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.contingent_status (Python parameter)")
        * [`editable (bool)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.editable (Python parameter)")
        * [`edited (bool)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.edited (Python parameter)")
        * [`gtc_date (datetime.date | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.gtc_date (Python parameter)")
        * [`id (int)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.id (Python parameter) — the ID of the order; test orders placed with dry_run don't have an ID")
        * [`in_flight_at (datetime.datetime | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.in_flight_at (Python parameter)")
        * [`legs (list[tastytrade.order.Leg])`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.legs (Python parameter)")
        * [`live_at (datetime.datetime | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.live_at (Python parameter)")
        * [`order_rule (tastytrade.order.OrderRule | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.order_rule (Python parameter)")
        * [`order_type (tastytrade.order.OrderType)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.order_type (Python parameter)")
        * [`preflight_id (str | int | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.preflight_id (Python parameter)")
        * [`price (decimal.Decimal | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.price (Python parameter)")
        * [`received_at (datetime.datetime | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.received_at (Python parameter)")
        * [`reject_reason (str | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.reject_reason (Python parameter)")
        * [`replaces_order_id (str | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.replaces_order_id (Python parameter)")
        * [`replacing_order_id (str | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.replacing_order_id (Python parameter)")
        * [`size (decimal.Decimal | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.size (Python parameter)")
        * [`source (str | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.source (Python parameter)")
        * [`status (tastytrade.order.OrderStatus)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.status (Python parameter)")
        * [`stop_trigger (str | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.stop_trigger (Python parameter)")
        * [`terminal_at (datetime.datetime | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.terminal_at (Python parameter)")
        * [`time_in_force (tastytrade.order.OrderTimeInForce)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.time_in_force (Python parameter)")
        * [`underlying_instrument_type (tastytrade.order.InstrumentType)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.underlying_instrument_type (Python parameter)")
        * [`underlying_symbol (str)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.underlying_symbol (Python parameter)")
        * [`updated_at (datetime.datetime)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.updated_at (Python parameter)")
        * [`user_id (str | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.user_id (Python parameter)")
        * [`username (str | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.username (Python parameter)")
        * [`value (decimal.Decimal | None)`](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder.value (Python parameter)")

    Validators:[¶](order.html#tastytrade.order.PlacedOrder-validators "Permalink to this headline")
    :   * `validate_price_effects` » `all fields`

    *field* id : [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `-1`[¶](order.html#tastytrade.order.PlacedOrder.id "Link to this definition")
    :   the ID of the order; test orders placed with dry\_run don’t have an ID

        Validated by:[¶](order.html#tastytrade.order.PlacedOrder.id-validated-by "Permalink to this headline")
        :   * `validate_price_effects`

*pydantic model* tastytrade.order.PlacedOrderResponse(*\**, *[buying\_power\_effect](order.html#tastytrade.order.PlacedOrderResponse "tastytrade.order.PlacedOrderResponse.buying_power_effect (Python parameter)"): [BuyingPowerEffect](order.html#tastytrade.order.BuyingPowerEffect "tastytrade.order.BuyingPowerEffect (Python model) — Bases: TastytradeData")*, *[order](order.html#tastytrade.order.PlacedOrderResponse "tastytrade.order.PlacedOrderResponse.order (Python parameter)"): [PlacedOrder](order.html#tastytrade.order.PlacedOrder "tastytrade.order.PlacedOrder (Python model) — Bases: TastytradeData")*, *[fee\_calculation](order.html#tastytrade.order.PlacedOrderResponse "tastytrade.order.PlacedOrderResponse.fee_calculation (Python parameter)"): [FeeCalculation](order.html#tastytrade.order.FeeCalculation "tastytrade.order.FeeCalculation (Python model) — Bases: TastytradeData") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[warnings](order.html#tastytrade.order.PlacedOrderResponse "tastytrade.order.PlacedOrderResponse.warnings (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[Message](order.html#tastytrade.order.Message "tastytrade.order.Message (Python model) — Bases: TastytradeData")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[errors](order.html#tastytrade.order.PlacedOrderResponse "tastytrade.order.PlacedOrderResponse.errors (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[Message](order.html#tastytrade.order.Message "tastytrade.order.Message (Python model) — Bases: TastytradeData")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](order.html#tastytrade.order.PlacedOrderResponse "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass grouping together information about a placed order.

    Show JSON schema

    ```
    {
       "title": "PlacedOrderResponse",
       "description": "Dataclass grouping together information about a placed order.",
       "type": "object",
       "properties": {
          "buying-power-effect": {
             "$ref": "#/$defs/BuyingPowerEffect"
          },
          "order": {
             "$ref": "#/$defs/PlacedOrder"
          },
          "fee-calculation": {
             "anyOf": [
                {
                   "$ref": "#/$defs/FeeCalculation"
                },
                {
                   "type": "null"
                }
             ],
             "default": null
          },
          "warnings": {
             "anyOf": [
                {
                   "items": {
                      "$ref": "#/$defs/Message"
                   },
                   "type": "array"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Warnings"
          },
          "errors": {
             "anyOf": [
                {
                   "items": {
                      "$ref": "#/$defs/Message"
                   },
                   "type": "array"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Errors"
          }
       },
       "$defs": {
          "BuyingPowerEffect": {
             "description": "Dataclass containing information about the effect of a trade on buying\npower.",
             "properties": {
                "change-in-margin-requirement": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Change-In-Margin-Requirement"
                },
                "change-in-buying-power": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Change-In-Buying-Power"
                },
                "current-buying-power": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Current-Buying-Power"
                },
                "new-buying-power": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "New-Buying-Power"
                },
                "isolated-order-margin-requirement": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Isolated-Order-Margin-Requirement"
                },
                "is-spread": {
                   "title": "Is-Spread",
                   "type": "boolean"
                },
                "impact": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Impact"
                },
                "effect": {
                   "$ref": "#/$defs/PriceEffect"
                }
             },
             "required": [
                "change-in-margin-requirement",
                "change-in-buying-power",
                "current-buying-power",
                "new-buying-power",
                "isolated-order-margin-requirement",
                "is-spread",
                "impact",
                "effect"
             ],
             "title": "BuyingPowerEffect",
             "type": "object"
          },
          "FeeCalculation": {
             "description": "Dataclass containing information about the fees associated with a trade.",
             "properties": {
                "regulatory-fees": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Regulatory-Fees"
                },
                "clearing-fees": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Clearing-Fees"
                },
                "commission": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Commission"
                },
                "proprietary-index-option-fees": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Proprietary-Index-Option-Fees"
                },
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
                "regulatory-fees",
                "clearing-fees",
                "commission",
                "proprietary-index-option-fees",
                "total-fees"
             ],
             "title": "FeeCalculation",
             "type": "object"
          },
          "FillInfo": {
             "description": "Dataclass that contains information about an order fill.",
             "properties": {
                "fill-id": {
                   "title": "Fill-Id",
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
                "fill-price": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Fill-Price"
                },
                "filled-at": {
                   "format": "date-time",
                   "title": "Filled-At",
                   "type": "string"
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
                }
             },
             "required": [
                "fill-id",
                "quantity",
                "fill-price",
                "filled-at"
             ],
             "title": "FillInfo",
             "type": "object"
          },
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
          "Leg": {
             "description": "Dataclass that represents an order leg.\n\nClasses that inherit from :class:`TradeableTastytradeJsonDataclass` can\ncall :meth:`build_leg` to build a leg from the dataclass.",
             "properties": {
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "action": {
                   "$ref": "#/$defs/OrderAction"
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
                "remaining-quantity": {
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
                   "title": "Remaining-Quantity"
                },
                "fills": {
                   "anyOf": [
                      {
                         "items": {
                            "$ref": "#/$defs/FillInfo"
                         },
                         "type": "array"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Fills"
                }
             },
             "required": [
                "instrument-type",
                "symbol",
                "action"
             ],
             "title": "Leg",
             "type": "object"
          },
          "Message": {
             "description": "Dataclass that represents a message from the Tastytrade API, usually\na warning or an error.",
             "properties": {
                "code": {
                   "title": "Code",
                   "type": "string"
                },
                "message": {
                   "title": "Message",
                   "type": "string"
                },
                "preflight-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Preflight-Id"
                }
             },
             "required": [
                "code",
                "message"
             ],
             "title": "Message",
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
          },
          "OrderCondition": {
             "description": "Dataclass that represents an order condition for an order rule.",
             "properties": {
                "id": {
                   "title": "Id",
                   "type": "string"
                },
                "action": {
                   "title": "Action",
                   "type": "string"
                },
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "indicator": {
                   "title": "Indicator",
                   "type": "string"
                },
                "comparator": {
                   "title": "Comparator",
                   "type": "string"
                },
                "threshold": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Threshold"
                },
                "is-threshold-based-on-notional": {
                   "title": "Is-Threshold-Based-On-Notional",
                   "type": "boolean"
                },
                "triggered-at": {
                   "format": "date-time",
                   "title": "Triggered-At",
                   "type": "string"
                },
                "triggered-value": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Triggered-Value"
                },
                "price-components": {
                   "items": {
                      "$ref": "#/$defs/OrderConditionPriceComponent"
                   },
                   "title": "Price-Components",
                   "type": "array"
                }
             },
             "required": [
                "id",
                "action",
                "symbol",
                "instrument-type",
                "indicator",
                "comparator",
                "threshold",
                "is-threshold-based-on-notional",
                "triggered-at",
                "triggered-value",
                "price-components"
             ],
             "title": "OrderCondition",
             "type": "object"
          },
          "OrderConditionPriceComponent": {
             "description": "Dataclass that represents a price component of an order condition.",
             "properties": {
                "symbol": {
                   "title": "Symbol",
                   "type": "string"
                },
                "instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
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
                }
             },
             "required": [
                "symbol",
                "instrument-type",
                "quantity",
                "quantity-direction"
             ],
             "title": "OrderConditionPriceComponent",
             "type": "object"
          },
          "OrderRule": {
             "description": "Dataclass that represents an order rule for a complex order.",
             "properties": {
                "route-after": {
                   "format": "date-time",
                   "title": "Route-After",
                   "type": "string"
                },
                "routed-at": {
                   "format": "date-time",
                   "title": "Routed-At",
                   "type": "string"
                },
                "cancel-at": {
                   "format": "date-time",
                   "title": "Cancel-At",
                   "type": "string"
                },
                "cancelled-at": {
                   "format": "date-time",
                   "title": "Cancelled-At",
                   "type": "string"
                },
                "order-conditions": {
                   "items": {
                      "$ref": "#/$defs/OrderCondition"
                   },
                   "title": "Order-Conditions",
                   "type": "array"
                }
             },
             "required": [
                "route-after",
                "routed-at",
                "cancel-at",
                "cancelled-at",
                "order-conditions"
             ],
             "title": "OrderRule",
             "type": "object"
          },
          "OrderStatus": {
             "description": "This is an :class:`~enum.Enum` that contains different order statuses.\nA typical (successful) order follows a progression:\n\nRECEIVED -> LIVE -> FILLED",
             "enum": [
                "Received",
                "Cancelled",
                "Filled",
                "Expired",
                "Live",
                "Rejected",
                "Contingent",
                "Routed",
                "In Flight",
                "Cancel Requested",
                "Replace Requested",
                "Removed",
                "Partially Removed"
             ],
             "title": "OrderStatus",
             "type": "string"
          },
          "OrderTimeInForce": {
             "description": "This is an :class:`~enum.Enum` that contains the valid TIFs for orders.",
             "enum": [
                "Day",
                "GTC",
                "GTD",
                "Ext",
                "GTC Ext",
                "IOC"
             ],
             "title": "OrderTimeInForce",
             "type": "string"
          },
          "OrderType": {
             "description": "This is an :class:`~enum.Enum` that contains the valid types of orders.",
             "enum": [
                "Limit",
                "Market",
                "Marketable Limit",
                "Stop",
                "Stop Limit",
                "Notional Market"
             ],
             "title": "OrderType",
             "type": "string"
          },
          "PlacedOrder": {
             "description": "Dataclass containing information about an existing order, whether it's\nbeen filled or not.",
             "properties": {
                "account-number": {
                   "title": "Account-Number",
                   "type": "string"
                },
                "time-in-force": {
                   "$ref": "#/$defs/OrderTimeInForce"
                },
                "order-type": {
                   "$ref": "#/$defs/OrderType"
                },
                "underlying-symbol": {
                   "title": "Underlying-Symbol",
                   "type": "string"
                },
                "underlying-instrument-type": {
                   "$ref": "#/$defs/InstrumentType"
                },
                "status": {
                   "$ref": "#/$defs/OrderStatus"
                },
                "cancellable": {
                   "title": "Cancellable",
                   "type": "boolean"
                },
                "editable": {
                   "title": "Editable",
                   "type": "boolean"
                },
                "edited": {
                   "title": "Edited",
                   "type": "boolean"
                },
                "updated-at": {
                   "format": "date-time",
                   "title": "Updated-At",
                   "type": "string"
                },
                "legs": {
                   "items": {
                      "$ref": "#/$defs/Leg"
                   },
                   "title": "Legs",
                   "type": "array"
                },
                "id": {
                   "default": -1,
                   "title": "Id",
                   "type": "integer"
                },
                "size": {
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
                   "title": "Size"
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
                "gtc-date": {
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
                   "title": "Gtc-Date"
                },
                "value": {
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
                   "title": "Value"
                },
                "stop-trigger": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Stop-Trigger"
                },
                "contingent-status": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Contingent-Status"
                },
                "confirmation-status": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Confirmation-Status"
                },
                "cancelled-at": {
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
                   "title": "Cancelled-At"
                },
                "cancel-user-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Cancel-User-Id"
                },
                "cancel-username": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Cancel-Username"
                },
                "replacing-order-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Replacing-Order-Id"
                },
                "replaces-order-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Replaces-Order-Id"
                },
                "in-flight-at": {
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
                   "title": "In-Flight-At"
                },
                "live-at": {
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
                   "title": "Live-At"
                },
                "received-at": {
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
                   "title": "Received-At"
                },
                "reject-reason": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Reject-Reason"
                },
                "user-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "User-Id"
                },
                "username": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Username"
                },
                "terminal-at": {
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
                   "title": "Terminal-At"
                },
                "complex-order-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Complex-Order-Id"
                },
                "complex-order-tag": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Complex-Order-Tag"
                },
                "preflight-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Preflight-Id"
                },
                "order-rule": {
                   "anyOf": [
                      {
                         "$ref": "#/$defs/OrderRule"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null
                },
                "source": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Source"
                }
             },
             "required": [
                "account-number",
                "time-in-force",
                "order-type",
                "underlying-symbol",
                "underlying-instrument-type",
                "status",
                "cancellable",
                "editable",
                "edited",
                "updated-at",
                "legs"
             ],
             "title": "PlacedOrder",
             "type": "object"
          },
          "PriceEffect": {
             "description": "This is an :class:`~enum.Enum` that shows the sign of a price effect, since\nTastytrade is apparently against negative numbers.",
             "enum": [
                "Credit",
                "Debit",
                "None"
             ],
             "title": "PriceEffect",
             "type": "string"
          }
       },
       "required": [
          "buying-power-effect",
          "order"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.PlacedOrderResponse-fields "Permalink to this headline")
    :   * [`buying_power_effect (tastytrade.order.BuyingPowerEffect)`](order.html#tastytrade.order.PlacedOrderResponse "tastytrade.order.PlacedOrderResponse.buying_power_effect (Python parameter)")
        * [`errors (list[tastytrade.order.Message] | None)`](order.html#tastytrade.order.PlacedOrderResponse "tastytrade.order.PlacedOrderResponse.errors (Python parameter)")
        * [`fee_calculation (tastytrade.order.FeeCalculation | None)`](order.html#tastytrade.order.PlacedOrderResponse "tastytrade.order.PlacedOrderResponse.fee_calculation (Python parameter)")
        * [`order (tastytrade.order.PlacedOrder)`](order.html#tastytrade.order.PlacedOrderResponse "tastytrade.order.PlacedOrderResponse.order (Python parameter)")
        * [`warnings (list[tastytrade.order.Message] | None)`](order.html#tastytrade.order.PlacedOrderResponse "tastytrade.order.PlacedOrderResponse.warnings (Python parameter)")

*pydantic model* tastytrade.order.TradeableTastytradeJsonDataclass(*\**, *[instrument\_type](order.html#tastytrade.order.TradeableTastytradeJsonDataclass "tastytrade.order.TradeableTastytradeJsonDataclass.instrument_type (Python parameter)"): [InstrumentType](order.html#tastytrade.order.InstrumentType "tastytrade.order.InstrumentType (Python enum) — Bases: str, Enum")*, *[symbol](order.html#tastytrade.order.TradeableTastytradeJsonDataclass "tastytrade.order.TradeableTastytradeJsonDataclass.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)[¶](order.html#tastytrade.order.TradeableTastytradeJsonDataclass "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass that represents a tradeable instrument.

    Classes that inherit from this class can call [`build_leg()`](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg "tastytrade.order.TradeableTastytradeJsonDataclass.build_leg (Python method) — Builds an order Leg from the dataclass.") to build a
    leg from the dataclass.

    Show JSON schema

    ```
    {
       "title": "TradeableTastytradeJsonDataclass",
       "description": "Dataclass that represents a tradeable instrument.\n\nClasses that inherit from this class can call :meth:`build_leg` to build a\nleg from the dataclass.",
       "type": "object",
       "properties": {
          "instrument-type": {
             "$ref": "#/$defs/InstrumentType"
          },
          "symbol": {
             "title": "Symbol",
             "type": "string"
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
          "instrument-type",
          "symbol"
       ]
    }

    ```

    Fields:[¶](order.html#tastytrade.order.TradeableTastytradeJsonDataclass-fields "Permalink to this headline")
    :   * [`instrument_type (tastytrade.order.InstrumentType)`](order.html#tastytrade.order.TradeableTastytradeJsonDataclass "tastytrade.order.TradeableTastytradeJsonDataclass.instrument_type (Python parameter)")
        * [`symbol (str)`](order.html#tastytrade.order.TradeableTastytradeJsonDataclass "tastytrade.order.TradeableTastytradeJsonDataclass.symbol (Python parameter)")

    build\_leg(*[quantity](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg.quantity "tastytrade.order.TradeableTastytradeJsonDataclass.build_leg.quantity (Python parameter) — the quantity of the symbol to trade, set this as None for notional orders"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*, *[action](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg.action "tastytrade.order.TradeableTastytradeJsonDataclass.build_leg.action (Python parameter) — OrderAction to perform, e.g."): [OrderAction](order.html#tastytrade.order.OrderAction "tastytrade.order.OrderAction (Python enum) — Bases: str, Enum")*) → [Leg](order.html#tastytrade.order.Leg "tastytrade.order.Leg (Python model) — Bases: TastytradeData")[¶](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg "Link to this definition")
    :   Builds an order [`Leg`](order.html#tastytrade.order.Leg "tastytrade.order.Leg (Python model) — Bases: TastytradeData") from the dataclass.

        Parameters:[¶](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg-parameters "Permalink to this headline")
        :   quantity: [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg.quantity "Permalink to this definition")
            :   the quantity of the symbol to trade, set this as None for notional orders

            action: [OrderAction](order.html#tastytrade.order.OrderAction "tastytrade.order.OrderAction (Python enum) — Bases: str, Enum")[¶](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg.action "Permalink to this definition")
            :   [`OrderAction`](order.html#tastytrade.order.OrderAction "tastytrade.order.OrderAction (Python enum) — Bases: str, Enum") to perform, e.g. BUY\_TO\_OPEN

        Returns:[¶](order.html#tastytrade.order.TradeableTastytradeJsonDataclass.build_leg-returns "Permalink to this headline")
        :   a [`Leg`](order.html#tastytrade.order.Leg "tastytrade.order.Leg (Python model) — Bases: TastytradeData") object

[Back to top](order.html#)


[Previous
tastytrade.metrics](metrics.html)
[Next
tastytrade.search](search.html)

© Copyright 2025, tastyware.

Created using
[Sphinx](https://www.sphinx-doc.org/)
7.4.7.
and
[Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)