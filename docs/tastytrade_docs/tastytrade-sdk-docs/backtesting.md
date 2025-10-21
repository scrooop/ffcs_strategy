tastytrade.backtest - tastytrade 10.1.0 documentation







[Skip to content](backtesting.html#tastytrade.backtest.Backtest)

tastytrade 10.1.0 documentation

tastytrade.backtest






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
  + tastytrade.backtest

    [tastytrade.backtest](backtesting.html#)



    tastytrade.backtest
    - [tastytrade.backtest.Backtest](backtesting.html#tastytrade.backtest.Backtest)

      * [Fields](backtesting.html#tastytrade.backtest.Backtest-fields)
    - [tastytrade.backtest.BacktestData](backtesting.html#tastytrade.backtest.BacktestData)
    - [tastytrade.backtest.BacktestEntry](backtesting.html#tastytrade.backtest.BacktestEntry)

      * [Fields](backtesting.html#tastytrade.backtest.BacktestEntry-fields)
    - [tastytrade.backtest.BacktestExit](backtesting.html#tastytrade.backtest.BacktestExit)

      * [Fields](backtesting.html#tastytrade.backtest.BacktestExit-fields)
    - [tastytrade.backtest.BacktestLeg](backtesting.html#tastytrade.backtest.BacktestLeg)

      * [Fields](backtesting.html#tastytrade.backtest.BacktestLeg-fields)
    - [tastytrade.backtest.BacktestParameters](backtesting.html#tastytrade.backtest.BacktestParameters)

      * [Fields](backtesting.html#tastytrade.backtest.BacktestParameters-fields)
    - [tastytrade.backtest.BacktestResponse](backtesting.html#tastytrade.backtest.BacktestResponse)

      * [Fields](backtesting.html#tastytrade.backtest.BacktestResponse-fields)
    - [tastytrade.backtest.BacktestResults](backtesting.html#tastytrade.backtest.BacktestResults)

      * [Fields](backtesting.html#tastytrade.backtest.BacktestResults-fields)
    - [Ctastytrade.backtest.BacktestSession](backtesting.html#tastytrade.backtest.BacktestSession)

      * [Mavailable\_parameters](backtesting.html#tastytrade.backtest.BacktestSession.available_parameters)
      * [Mcancel](backtesting.html#tastytrade.backtest.BacktestSession.cancel)

        + [Parameters](backtesting.html#tastytrade.backtest.BacktestSession.cancel-parameters)

          - [pbacktest\_id](backtesting.html#tastytrade.backtest.BacktestSession.cancel.backtest_id)
      * [Mdelete](backtesting.html#tastytrade.backtest.BacktestSession.delete)
      * [Mget](backtesting.html#tastytrade.backtest.BacktestSession.get)
      * [Mrun](backtesting.html#tastytrade.backtest.BacktestSession.run)

        + [Parameters](backtesting.html#tastytrade.backtest.BacktestSession.run-parameters)

          - [pbacktest](backtesting.html#tastytrade.backtest.BacktestSession.run.backtest)
    - [tastytrade.backtest.BacktestSnapshot](backtesting.html#tastytrade.backtest.BacktestSnapshot)

      * [Fields](backtesting.html#tastytrade.backtest.BacktestSnapshot-fields)
    - [tastytrade.backtest.BacktestStatistics](backtesting.html#tastytrade.backtest.BacktestStatistics)

      * [Fields](backtesting.html#tastytrade.backtest.BacktestStatistics-fields)
    - [tastytrade.backtest.BacktestTrial](backtesting.html#tastytrade.backtest.BacktestTrial)

      * [Fields](backtesting.html#tastytrade.backtest.BacktestTrial-fields)
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

tastytrade.backtest

* [tastytrade.backtest.Backtest](backtesting.html#tastytrade.backtest.Backtest)

  + [Fields](backtesting.html#tastytrade.backtest.Backtest-fields)
* [tastytrade.backtest.BacktestData](backtesting.html#tastytrade.backtest.BacktestData)
* [tastytrade.backtest.BacktestEntry](backtesting.html#tastytrade.backtest.BacktestEntry)

  + [Fields](backtesting.html#tastytrade.backtest.BacktestEntry-fields)
* [tastytrade.backtest.BacktestExit](backtesting.html#tastytrade.backtest.BacktestExit)

  + [Fields](backtesting.html#tastytrade.backtest.BacktestExit-fields)
* [tastytrade.backtest.BacktestLeg](backtesting.html#tastytrade.backtest.BacktestLeg)

  + [Fields](backtesting.html#tastytrade.backtest.BacktestLeg-fields)
* [tastytrade.backtest.BacktestParameters](backtesting.html#tastytrade.backtest.BacktestParameters)

  + [Fields](backtesting.html#tastytrade.backtest.BacktestParameters-fields)
* [tastytrade.backtest.BacktestResponse](backtesting.html#tastytrade.backtest.BacktestResponse)

  + [Fields](backtesting.html#tastytrade.backtest.BacktestResponse-fields)
* [tastytrade.backtest.BacktestResults](backtesting.html#tastytrade.backtest.BacktestResults)

  + [Fields](backtesting.html#tastytrade.backtest.BacktestResults-fields)
* [Ctastytrade.backtest.BacktestSession](backtesting.html#tastytrade.backtest.BacktestSession)

  + [Mavailable\_parameters](backtesting.html#tastytrade.backtest.BacktestSession.available_parameters)
  + [Mcancel](backtesting.html#tastytrade.backtest.BacktestSession.cancel)

    - [Parameters](backtesting.html#tastytrade.backtest.BacktestSession.cancel-parameters)

      * [pbacktest\_id](backtesting.html#tastytrade.backtest.BacktestSession.cancel.backtest_id)
  + [Mdelete](backtesting.html#tastytrade.backtest.BacktestSession.delete)
  + [Mget](backtesting.html#tastytrade.backtest.BacktestSession.get)
  + [Mrun](backtesting.html#tastytrade.backtest.BacktestSession.run)

    - [Parameters](backtesting.html#tastytrade.backtest.BacktestSession.run-parameters)

      * [pbacktest](backtesting.html#tastytrade.backtest.BacktestSession.run.backtest)
* [tastytrade.backtest.BacktestSnapshot](backtesting.html#tastytrade.backtest.BacktestSnapshot)

  + [Fields](backtesting.html#tastytrade.backtest.BacktestSnapshot-fields)
* [tastytrade.backtest.BacktestStatistics](backtesting.html#tastytrade.backtest.BacktestStatistics)

  + [Fields](backtesting.html#tastytrade.backtest.BacktestStatistics-fields)
* [tastytrade.backtest.BacktestTrial](backtesting.html#tastytrade.backtest.BacktestTrial)

  + [Fields](backtesting.html#tastytrade.backtest.BacktestTrial-fields)

# tastytrade.backtest[¶](backtesting.html#module-tastytrade.backtest "Link to this heading")

*pydantic model* tastytrade.backtest.Backtest(*\**, *[symbol](backtesting.html#tastytrade.backtest.Backtest "tastytrade.backtest.Backtest.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[entryConditions](backtesting.html#tastytrade.backtest.Backtest "tastytrade.backtest.Backtest.entryConditions (Python parameter)"): [BacktestEntry](backtesting.html#tastytrade.backtest.BacktestEntry "tastytrade.backtest.BacktestEntry (Python model) — Bases: BacktestData")*, *[exitConditions](backtesting.html#tastytrade.backtest.Backtest "tastytrade.backtest.Backtest.exitConditions (Python parameter)"): [BacktestExit](backtesting.html#tastytrade.backtest.BacktestExit "tastytrade.backtest.BacktestExit (Python model) — Bases: BacktestData")*, *[legs](backtesting.html#tastytrade.backtest.Backtest "tastytrade.backtest.Backtest.legs (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[BacktestLeg](backtesting.html#tastytrade.backtest.BacktestLeg "tastytrade.backtest.BacktestLeg (Python model) — Bases: BacktestData")]*, *[startDate](backtesting.html#tastytrade.backtest.Backtest "tastytrade.backtest.Backtest.startDate (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*, *[endDate](backtesting.html#tastytrade.backtest.Backtest "tastytrade.backtest.Backtest.endDate (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") = `datetime.date(2024, 7, 31)`*, *[status](backtesting.html#tastytrade.backtest.Backtest "tastytrade.backtest.Backtest.status (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `'pending'`*)[¶](backtesting.html#tastytrade.backtest.Backtest "Link to this definition")
:   Bases: [`BacktestData`](backtesting.html#tastytrade.backtest.BacktestData "tastytrade.backtest.BacktestData (Python model) — Bases: BaseModel")

    Dataclass of configuration options for a backtest.

    Show JSON schema

    ```
    {
       "title": "Backtest",
       "description": "Dataclass of configuration options for a backtest.",
       "type": "object",
       "properties": {
          "symbol": {
             "title": "Symbol",
             "type": "string"
          },
          "entryConditions": {
             "$ref": "#/$defs/BacktestEntry"
          },
          "exitConditions": {
             "$ref": "#/$defs/BacktestExit"
          },
          "legs": {
             "items": {
                "$ref": "#/$defs/BacktestLeg"
             },
             "title": "Legs",
             "type": "array"
          },
          "startDate": {
             "format": "date",
             "title": "Startdate",
             "type": "string"
          },
          "endDate": {
             "default": "2024-07-31",
             "format": "date",
             "title": "Enddate",
             "type": "string"
          },
          "status": {
             "default": "pending",
             "title": "Status",
             "type": "string"
          }
       },
       "$defs": {
          "BacktestEntry": {
             "description": "Dataclass of parameters for backtest trade entry.",
             "properties": {
                "useExactDte": {
                   "default": true,
                   "title": "Useexactdte",
                   "type": "boolean"
                },
                "maximumActiveTrials": {
                   "anyOf": [
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Maximumactivetrials"
                },
                "maximumActiveTrialsBehavior": {
                   "anyOf": [
                      {
                         "enum": [
                            "close oldest",
                            "don't enter"
                         ],
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Maximumactivetrialsbehavior"
                },
                "frequency": {
                   "default": "every day",
                   "title": "Frequency",
                   "type": "string"
                }
             },
             "title": "BacktestEntry",
             "type": "object"
          },
          "BacktestExit": {
             "description": "Dataclass of parameters for backtest trade exit.",
             "properties": {
                "afterDaysInTrade": {
                   "anyOf": [
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Afterdaysintrade"
                },
                "stopLossPercentage": {
                   "anyOf": [
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Stoplosspercentage"
                },
                "takeProfitPercentage": {
                   "anyOf": [
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Takeprofitpercentage"
                },
                "atDaysToExpiration": {
                   "anyOf": [
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Atdaystoexpiration"
                }
             },
             "title": "BacktestExit",
             "type": "object"
          },
          "BacktestLeg": {
             "description": "Dataclass of parameters for placing legs of backtest trades.\nLeg delta must be a multiple of 5.",
             "properties": {
                "daysUntilExpiration": {
                   "default": 45,
                   "title": "Daysuntilexpiration",
                   "type": "integer"
                },
                "delta": {
                   "default": 15,
                   "title": "Delta",
                   "type": "integer"
                },
                "direction": {
                   "default": "sell",
                   "enum": [
                      "buy",
                      "sell"
                   ],
                   "title": "Direction",
                   "type": "string"
                },
                "quantity": {
                   "default": 1,
                   "title": "Quantity",
                   "type": "integer"
                },
                "side": {
                   "default": "call",
                   "enum": [
                      "call",
                      "put"
                   ],
                   "title": "Side",
                   "type": "string"
                }
             },
             "title": "BacktestLeg",
             "type": "object"
          }
       },
       "required": [
          "symbol",
          "entryConditions",
          "exitConditions",
          "legs",
          "startDate"
       ]
    }

    ```

    Fields:[¶](backtesting.html#tastytrade.backtest.Backtest-fields "Permalink to this headline")
    :   * `end_date (datetime.date)`
        * `entry_conditions (tastytrade.backtest.BacktestEntry)`
        * `exit_conditions (tastytrade.backtest.BacktestExit)`
        * [`legs (list[tastytrade.backtest.BacktestLeg])`](backtesting.html#tastytrade.backtest.Backtest "tastytrade.backtest.Backtest.legs (Python parameter)")
        * `start_date (datetime.date)`
        * [`status (str)`](backtesting.html#tastytrade.backtest.Backtest "tastytrade.backtest.Backtest.status (Python parameter)")
        * [`symbol (str)`](backtesting.html#tastytrade.backtest.Backtest "tastytrade.backtest.Backtest.symbol (Python parameter)")

*pydantic model* tastytrade.backtest.BacktestData[¶](backtesting.html#tastytrade.backtest.BacktestData "Link to this definition")
:   Bases: `BaseModel`

    Dataclass for converting backtest JSON naming conventions to snake case.

    Show JSON schema

    ```
    {
       "title": "BacktestData",
       "description": "Dataclass for converting backtest JSON naming conventions to snake case.",
       "type": "object",
       "properties": {}
    }

    ```

*pydantic model* tastytrade.backtest.BacktestEntry(*\**, *[useExactDte](backtesting.html#tastytrade.backtest.BacktestEntry "tastytrade.backtest.BacktestEntry.useExactDte (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `True`*, *[maximumActiveTrials](backtesting.html#tastytrade.backtest.BacktestEntry "tastytrade.backtest.BacktestEntry.maximumActiveTrials (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[maximumActiveTrialsBehavior](backtesting.html#tastytrade.backtest.BacktestEntry "tastytrade.backtest.BacktestEntry.maximumActiveTrialsBehavior (Python parameter)"): 'close oldest' | "don't enter" | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[frequency](backtesting.html#tastytrade.backtest.BacktestEntry "tastytrade.backtest.BacktestEntry.frequency (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `'every day'`*)[¶](backtesting.html#tastytrade.backtest.BacktestEntry "Link to this definition")
:   Bases: [`BacktestData`](backtesting.html#tastytrade.backtest.BacktestData "tastytrade.backtest.BacktestData (Python model) — Bases: BaseModel")

    Dataclass of parameters for backtest trade entry.

    Show JSON schema

    ```
    {
       "title": "BacktestEntry",
       "description": "Dataclass of parameters for backtest trade entry.",
       "type": "object",
       "properties": {
          "useExactDte": {
             "default": true,
             "title": "Useexactdte",
             "type": "boolean"
          },
          "maximumActiveTrials": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Maximumactivetrials"
          },
          "maximumActiveTrialsBehavior": {
             "anyOf": [
                {
                   "enum": [
                      "close oldest",
                      "don't enter"
                   ],
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Maximumactivetrialsbehavior"
          },
          "frequency": {
             "default": "every day",
             "title": "Frequency",
             "type": "string"
          }
       }
    }

    ```

    Fields:[¶](backtesting.html#tastytrade.backtest.BacktestEntry-fields "Permalink to this headline")
    :   * [`frequency (str)`](backtesting.html#tastytrade.backtest.BacktestEntry "tastytrade.backtest.BacktestEntry.frequency (Python parameter)")
        * `maximum_active_trials (int | None)`
        * `maximum_active_trials_behavior (Literal['close oldest', "don't enter"] | None)`
        * `use_exact_DTE (bool)`

*pydantic model* tastytrade.backtest.BacktestExit(*\**, *[afterDaysInTrade](backtesting.html#tastytrade.backtest.BacktestExit "tastytrade.backtest.BacktestExit.afterDaysInTrade (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[stopLossPercentage](backtesting.html#tastytrade.backtest.BacktestExit "tastytrade.backtest.BacktestExit.stopLossPercentage (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[takeProfitPercentage](backtesting.html#tastytrade.backtest.BacktestExit "tastytrade.backtest.BacktestExit.takeProfitPercentage (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[atDaysToExpiration](backtesting.html#tastytrade.backtest.BacktestExit "tastytrade.backtest.BacktestExit.atDaysToExpiration (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](backtesting.html#tastytrade.backtest.BacktestExit "Link to this definition")
:   Bases: [`BacktestData`](backtesting.html#tastytrade.backtest.BacktestData "tastytrade.backtest.BacktestData (Python model) — Bases: BaseModel")

    Dataclass of parameters for backtest trade exit.

    Show JSON schema

    ```
    {
       "title": "BacktestExit",
       "description": "Dataclass of parameters for backtest trade exit.",
       "type": "object",
       "properties": {
          "afterDaysInTrade": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Afterdaysintrade"
          },
          "stopLossPercentage": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Stoplosspercentage"
          },
          "takeProfitPercentage": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Takeprofitpercentage"
          },
          "atDaysToExpiration": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Atdaystoexpiration"
          }
       }
    }

    ```

    Fields:[¶](backtesting.html#tastytrade.backtest.BacktestExit-fields "Permalink to this headline")
    :   * `after_days_in_trade (int | None)`
        * `at_days_to_expiration (int | None)`
        * `stop_loss_percentage (int | None)`
        * `take_profit_percentage (int | None)`

*pydantic model* tastytrade.backtest.BacktestLeg(*\**, *[daysUntilExpiration](backtesting.html#tastytrade.backtest.BacktestLeg "tastytrade.backtest.BacktestLeg.daysUntilExpiration (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `45`*, *[delta](backtesting.html#tastytrade.backtest.BacktestLeg "tastytrade.backtest.BacktestLeg.delta (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `15`*, *[direction](backtesting.html#tastytrade.backtest.BacktestLeg "tastytrade.backtest.BacktestLeg.direction (Python parameter)"): 'buy' | 'sell' = `'sell'`*, *[quantity](backtesting.html#tastytrade.backtest.BacktestLeg "tastytrade.backtest.BacktestLeg.quantity (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `1`*, *[side](backtesting.html#tastytrade.backtest.BacktestLeg "tastytrade.backtest.BacktestLeg.side (Python parameter)"): 'call' | 'put' = `'call'`*)[¶](backtesting.html#tastytrade.backtest.BacktestLeg "Link to this definition")
:   Bases: [`BacktestData`](backtesting.html#tastytrade.backtest.BacktestData "tastytrade.backtest.BacktestData (Python model) — Bases: BaseModel")

    Dataclass of parameters for placing legs of backtest trades.
    Leg delta must be a multiple of 5.

    Show JSON schema

    ```
    {
       "title": "BacktestLeg",
       "description": "Dataclass of parameters for placing legs of backtest trades.\nLeg delta must be a multiple of 5.",
       "type": "object",
       "properties": {
          "daysUntilExpiration": {
             "default": 45,
             "title": "Daysuntilexpiration",
             "type": "integer"
          },
          "delta": {
             "default": 15,
             "title": "Delta",
             "type": "integer"
          },
          "direction": {
             "default": "sell",
             "enum": [
                "buy",
                "sell"
             ],
             "title": "Direction",
             "type": "string"
          },
          "quantity": {
             "default": 1,
             "title": "Quantity",
             "type": "integer"
          },
          "side": {
             "default": "call",
             "enum": [
                "call",
                "put"
             ],
             "title": "Side",
             "type": "string"
          }
       }
    }

    ```

    Fields:[¶](backtesting.html#tastytrade.backtest.BacktestLeg-fields "Permalink to this headline")
    :   * `days_until_expiration (int)`
        * [`delta (int)`](backtesting.html#tastytrade.backtest.BacktestLeg "tastytrade.backtest.BacktestLeg.delta (Python parameter)")
        * [`direction (Literal['buy', 'sell'])`](backtesting.html#tastytrade.backtest.BacktestLeg "tastytrade.backtest.BacktestLeg.direction (Python parameter)")
        * [`quantity (int)`](backtesting.html#tastytrade.backtest.BacktestLeg "tastytrade.backtest.BacktestLeg.quantity (Python parameter)")
        * [`side (Literal['call', 'put'])`](backtesting.html#tastytrade.backtest.BacktestLeg "tastytrade.backtest.BacktestLeg.side (Python parameter)")

*pydantic model* tastytrade.backtest.BacktestParameters(*\**, *[symbol](backtesting.html#tastytrade.backtest.BacktestParameters "tastytrade.backtest.BacktestParameters.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[startDate](backtesting.html#tastytrade.backtest.BacktestParameters "tastytrade.backtest.BacktestParameters.startDate (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*, *[endDate](backtesting.html#tastytrade.backtest.BacktestParameters "tastytrade.backtest.BacktestParameters.endDate (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*)[¶](backtesting.html#tastytrade.backtest.BacktestParameters "Link to this definition")
:   Bases: [`BacktestData`](backtesting.html#tastytrade.backtest.BacktestData "tastytrade.backtest.BacktestData (Python model) — Bases: BaseModel")

    Dataclass containing valid start/end dates for a symbol.

    Show JSON schema

    ```
    {
       "title": "BacktestParameters",
       "description": "Dataclass containing valid start/end dates for a symbol.",
       "type": "object",
       "properties": {
          "symbol": {
             "title": "Symbol",
             "type": "string"
          },
          "startDate": {
             "format": "date",
             "title": "Startdate",
             "type": "string"
          },
          "endDate": {
             "format": "date",
             "title": "Enddate",
             "type": "string"
          }
       },
       "required": [
          "symbol",
          "startDate",
          "endDate"
       ]
    }

    ```

    Fields:[¶](backtesting.html#tastytrade.backtest.BacktestParameters-fields "Permalink to this headline")
    :   * `end_date (datetime.date)`
        * `start_date (datetime.date)`
        * [`symbol (str)`](backtesting.html#tastytrade.backtest.BacktestParameters "tastytrade.backtest.BacktestParameters.symbol (Python parameter)")

*pydantic model* tastytrade.backtest.BacktestResponse(*\**, *[symbol](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[entryConditions](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.entryConditions (Python parameter)"): [BacktestEntry](backtesting.html#tastytrade.backtest.BacktestEntry "tastytrade.backtest.BacktestEntry (Python model) — Bases: BacktestData")*, *[exitConditions](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.exitConditions (Python parameter)"): [BacktestExit](backtesting.html#tastytrade.backtest.BacktestExit "tastytrade.backtest.BacktestExit (Python model) — Bases: BacktestData")*, *[legs](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.legs (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[BacktestLeg](backtesting.html#tastytrade.backtest.BacktestLeg "tastytrade.backtest.BacktestLeg (Python model) — Bases: BacktestData")]*, *[startDate](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.startDate (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*, *[endDate](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.endDate (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") = `datetime.date(2024, 7, 31)`*, *[status](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.status (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `'pending'`*, *[createdAt](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.createdAt (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[id](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[results](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.results (Python parameter)"): [BacktestResults](backtesting.html#tastytrade.backtest.BacktestResults "tastytrade.backtest.BacktestResults (Python model) — Bases: BacktestData")*, *[eta](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.eta (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[progress](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.progress (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](backtesting.html#tastytrade.backtest.BacktestResponse "Link to this definition")
:   Bases: [`Backtest`](backtesting.html#tastytrade.backtest.Backtest "tastytrade.backtest.Backtest (Python model) — Bases: BacktestData")

    Dataclass containing a backtest and associated information.

    Show JSON schema

    ```
    {
       "title": "BacktestResponse",
       "description": "Dataclass containing a backtest and associated information.",
       "type": "object",
       "properties": {
          "symbol": {
             "title": "Symbol",
             "type": "string"
          },
          "entryConditions": {
             "$ref": "#/$defs/BacktestEntry"
          },
          "exitConditions": {
             "$ref": "#/$defs/BacktestExit"
          },
          "legs": {
             "items": {
                "$ref": "#/$defs/BacktestLeg"
             },
             "title": "Legs",
             "type": "array"
          },
          "startDate": {
             "format": "date",
             "title": "Startdate",
             "type": "string"
          },
          "endDate": {
             "default": "2024-07-31",
             "format": "date",
             "title": "Enddate",
             "type": "string"
          },
          "status": {
             "default": "pending",
             "title": "Status",
             "type": "string"
          },
          "createdAt": {
             "format": "date-time",
             "title": "Createdat",
             "type": "string"
          },
          "id": {
             "title": "Id",
             "type": "string"
          },
          "results": {
             "$ref": "#/$defs/BacktestResults"
          },
          "eta": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Eta"
          },
          "progress": {
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
             "title": "Progress"
          }
       },
       "$defs": {
          "BacktestEntry": {
             "description": "Dataclass of parameters for backtest trade entry.",
             "properties": {
                "useExactDte": {
                   "default": true,
                   "title": "Useexactdte",
                   "type": "boolean"
                },
                "maximumActiveTrials": {
                   "anyOf": [
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Maximumactivetrials"
                },
                "maximumActiveTrialsBehavior": {
                   "anyOf": [
                      {
                         "enum": [
                            "close oldest",
                            "don't enter"
                         ],
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Maximumactivetrialsbehavior"
                },
                "frequency": {
                   "default": "every day",
                   "title": "Frequency",
                   "type": "string"
                }
             },
             "title": "BacktestEntry",
             "type": "object"
          },
          "BacktestExit": {
             "description": "Dataclass of parameters for backtest trade exit.",
             "properties": {
                "afterDaysInTrade": {
                   "anyOf": [
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Afterdaysintrade"
                },
                "stopLossPercentage": {
                   "anyOf": [
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Stoplosspercentage"
                },
                "takeProfitPercentage": {
                   "anyOf": [
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Takeprofitpercentage"
                },
                "atDaysToExpiration": {
                   "anyOf": [
                      {
                         "type": "integer"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Atdaystoexpiration"
                }
             },
             "title": "BacktestExit",
             "type": "object"
          },
          "BacktestLeg": {
             "description": "Dataclass of parameters for placing legs of backtest trades.\nLeg delta must be a multiple of 5.",
             "properties": {
                "daysUntilExpiration": {
                   "default": 45,
                   "title": "Daysuntilexpiration",
                   "type": "integer"
                },
                "delta": {
                   "default": 15,
                   "title": "Delta",
                   "type": "integer"
                },
                "direction": {
                   "default": "sell",
                   "enum": [
                      "buy",
                      "sell"
                   ],
                   "title": "Direction",
                   "type": "string"
                },
                "quantity": {
                   "default": 1,
                   "title": "Quantity",
                   "type": "integer"
                },
                "side": {
                   "default": "call",
                   "enum": [
                      "call",
                      "put"
                   ],
                   "title": "Side",
                   "type": "string"
                }
             },
             "title": "BacktestLeg",
             "type": "object"
          },
          "BacktestResults": {
             "description": "Dataclass containing partial or finished results of a backtest.",
             "properties": {
                "snapshots": {
                   "anyOf": [
                      {
                         "items": {
                            "$ref": "#/$defs/BacktestSnapshot"
                         },
                         "type": "array"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "title": "Snapshots"
                },
                "statistics": {
                   "anyOf": [
                      {
                         "$ref": "#/$defs/BacktestStatistics"
                      },
                      {
                         "type": "null"
                      }
                   ]
                },
                "trials": {
                   "anyOf": [
                      {
                         "items": {
                            "$ref": "#/$defs/BacktestTrial"
                         },
                         "type": "array"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "title": "Trials"
                }
             },
             "required": [
                "snapshots",
                "statistics",
                "trials"
             ],
             "title": "BacktestResults",
             "type": "object"
          },
          "BacktestSnapshot": {
             "description": "Dataclass containing a snapshot in time during the backtest.",
             "properties": {
                "dateTime": {
                   "format": "date-time",
                   "title": "Datetime",
                   "type": "string"
                },
                "profitLoss": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Profitloss"
                },
                "normalizedUnderlyingPrice": {
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
                   "title": "Normalizedunderlyingprice"
                },
                "underlyingPrice": {
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
                   "title": "Underlyingprice"
                }
             },
             "required": [
                "dateTime",
                "profitLoss"
             ],
             "title": "BacktestSnapshot",
             "type": "object"
          },
          "BacktestStatistics": {
             "description": "Dataclass containing statistics on the overall performance of a backtest.",
             "properties": {
                "Avg. BPR per trade": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Avg. Bpr Per Trade"
                },
                "Avg. daily change in PNL": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Avg. Daily Change In Pnl"
                },
                "Avg. daily change in net liq": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Avg. Daily Change In Net Liq"
                },
                "Avg. days in trade": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Avg. Days In Trade"
                },
                "Avg. premium": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Avg. Premium"
                },
                "Avg. profit/loss per trade": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Avg. Profit/Loss Per Trade"
                },
                "Avg. return per trade": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Avg. Return Per Trade"
                },
                "Highest profit": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Highest Profit"
                },
                "Loss percentage": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Loss Percentage"
                },
                "Losses": {
                   "title": "Losses",
                   "type": "integer"
                },
                "Max drawdown": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Max Drawdown"
                },
                "Number of trades": {
                   "title": "Number Of Trades",
                   "type": "integer"
                },
                "Premium capture rate": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Premium Capture Rate"
                },
                "Return on used capital": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Return On Used Capital"
                },
                "Total fees": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Total Fees"
                },
                "Total premium": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Total Premium"
                },
                "Total profit/loss": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Total Profit/Loss"
                },
                "Used capital": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Used Capital"
                },
                "Win percentage": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Win Percentage"
                },
                "Wins": {
                   "title": "Wins",
                   "type": "integer"
                },
                "Worst loss": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Worst Loss"
                }
             },
             "required": [
                "Avg. BPR per trade",
                "Avg. daily change in PNL",
                "Avg. daily change in net liq",
                "Avg. days in trade",
                "Avg. premium",
                "Avg. profit/loss per trade",
                "Avg. return per trade",
                "Highest profit",
                "Loss percentage",
                "Losses",
                "Max drawdown",
                "Number of trades",
                "Premium capture rate",
                "Return on used capital",
                "Total fees",
                "Total premium",
                "Total profit/loss",
                "Used capital",
                "Win percentage",
                "Wins",
                "Worst loss"
             ],
             "title": "BacktestStatistics",
             "type": "object"
          },
          "BacktestTrial": {
             "description": "Dataclass containing information on trades placed during the backtest.",
             "properties": {
                "closeDateTime": {
                   "format": "date-time",
                   "title": "Closedatetime",
                   "type": "string"
                },
                "openDateTime": {
                   "format": "date-time",
                   "title": "Opendatetime",
                   "type": "string"
                },
                "profitLoss": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Profitloss"
                }
             },
             "required": [
                "closeDateTime",
                "openDateTime",
                "profitLoss"
             ],
             "title": "BacktestTrial",
             "type": "object"
          }
       },
       "required": [
          "symbol",
          "entryConditions",
          "exitConditions",
          "legs",
          "startDate",
          "createdAt",
          "id",
          "results"
       ]
    }

    ```

    Fields:[¶](backtesting.html#tastytrade.backtest.BacktestResponse-fields "Permalink to this headline")
    :   * `created_at (datetime.datetime)`
        * [`eta (int | None)`](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.eta (Python parameter)")
        * [`id (str)`](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.id (Python parameter)")
        * [`progress (decimal.Decimal | None)`](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.progress (Python parameter)")
        * [`results (tastytrade.backtest.BacktestResults)`](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse.results (Python parameter)")

*pydantic model* tastytrade.backtest.BacktestResults(*\**, *[snapshots](backtesting.html#tastytrade.backtest.BacktestResults "tastytrade.backtest.BacktestResults.snapshots (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[BacktestSnapshot](backtesting.html#tastytrade.backtest.BacktestSnapshot "tastytrade.backtest.BacktestSnapshot (Python model) — Bases: BacktestData")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*, *[statistics](backtesting.html#tastytrade.backtest.BacktestResults "tastytrade.backtest.BacktestResults.statistics (Python parameter)"): [BacktestStatistics](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics (Python model) — Bases: BaseModel") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*, *[trials](backtesting.html#tastytrade.backtest.BacktestResults "tastytrade.backtest.BacktestResults.trials (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[BacktestTrial](backtesting.html#tastytrade.backtest.BacktestTrial "tastytrade.backtest.BacktestTrial (Python model) — Bases: BacktestData")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*)[¶](backtesting.html#tastytrade.backtest.BacktestResults "Link to this definition")
:   Bases: [`BacktestData`](backtesting.html#tastytrade.backtest.BacktestData "tastytrade.backtest.BacktestData (Python model) — Bases: BaseModel")

    Dataclass containing partial or finished results of a backtest.

    Show JSON schema

    ```
    {
       "title": "BacktestResults",
       "description": "Dataclass containing partial or finished results of a backtest.",
       "type": "object",
       "properties": {
          "snapshots": {
             "anyOf": [
                {
                   "items": {
                      "$ref": "#/$defs/BacktestSnapshot"
                   },
                   "type": "array"
                },
                {
                   "type": "null"
                }
             ],
             "title": "Snapshots"
          },
          "statistics": {
             "anyOf": [
                {
                   "$ref": "#/$defs/BacktestStatistics"
                },
                {
                   "type": "null"
                }
             ]
          },
          "trials": {
             "anyOf": [
                {
                   "items": {
                      "$ref": "#/$defs/BacktestTrial"
                   },
                   "type": "array"
                },
                {
                   "type": "null"
                }
             ],
             "title": "Trials"
          }
       },
       "$defs": {
          "BacktestSnapshot": {
             "description": "Dataclass containing a snapshot in time during the backtest.",
             "properties": {
                "dateTime": {
                   "format": "date-time",
                   "title": "Datetime",
                   "type": "string"
                },
                "profitLoss": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Profitloss"
                },
                "normalizedUnderlyingPrice": {
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
                   "title": "Normalizedunderlyingprice"
                },
                "underlyingPrice": {
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
                   "title": "Underlyingprice"
                }
             },
             "required": [
                "dateTime",
                "profitLoss"
             ],
             "title": "BacktestSnapshot",
             "type": "object"
          },
          "BacktestStatistics": {
             "description": "Dataclass containing statistics on the overall performance of a backtest.",
             "properties": {
                "Avg. BPR per trade": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Avg. Bpr Per Trade"
                },
                "Avg. daily change in PNL": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Avg. Daily Change In Pnl"
                },
                "Avg. daily change in net liq": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Avg. Daily Change In Net Liq"
                },
                "Avg. days in trade": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Avg. Days In Trade"
                },
                "Avg. premium": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Avg. Premium"
                },
                "Avg. profit/loss per trade": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Avg. Profit/Loss Per Trade"
                },
                "Avg. return per trade": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Avg. Return Per Trade"
                },
                "Highest profit": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Highest Profit"
                },
                "Loss percentage": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Loss Percentage"
                },
                "Losses": {
                   "title": "Losses",
                   "type": "integer"
                },
                "Max drawdown": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Max Drawdown"
                },
                "Number of trades": {
                   "title": "Number Of Trades",
                   "type": "integer"
                },
                "Premium capture rate": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Premium Capture Rate"
                },
                "Return on used capital": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Return On Used Capital"
                },
                "Total fees": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Total Fees"
                },
                "Total premium": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Total Premium"
                },
                "Total profit/loss": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Total Profit/Loss"
                },
                "Used capital": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Used Capital"
                },
                "Win percentage": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Win Percentage"
                },
                "Wins": {
                   "title": "Wins",
                   "type": "integer"
                },
                "Worst loss": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Worst Loss"
                }
             },
             "required": [
                "Avg. BPR per trade",
                "Avg. daily change in PNL",
                "Avg. daily change in net liq",
                "Avg. days in trade",
                "Avg. premium",
                "Avg. profit/loss per trade",
                "Avg. return per trade",
                "Highest profit",
                "Loss percentage",
                "Losses",
                "Max drawdown",
                "Number of trades",
                "Premium capture rate",
                "Return on used capital",
                "Total fees",
                "Total premium",
                "Total profit/loss",
                "Used capital",
                "Win percentage",
                "Wins",
                "Worst loss"
             ],
             "title": "BacktestStatistics",
             "type": "object"
          },
          "BacktestTrial": {
             "description": "Dataclass containing information on trades placed during the backtest.",
             "properties": {
                "closeDateTime": {
                   "format": "date-time",
                   "title": "Closedatetime",
                   "type": "string"
                },
                "openDateTime": {
                   "format": "date-time",
                   "title": "Opendatetime",
                   "type": "string"
                },
                "profitLoss": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Profitloss"
                }
             },
             "required": [
                "closeDateTime",
                "openDateTime",
                "profitLoss"
             ],
             "title": "BacktestTrial",
             "type": "object"
          }
       },
       "required": [
          "snapshots",
          "statistics",
          "trials"
       ]
    }

    ```

    Fields:[¶](backtesting.html#tastytrade.backtest.BacktestResults-fields "Permalink to this headline")
    :   * [`snapshots (list[tastytrade.backtest.BacktestSnapshot] | None)`](backtesting.html#tastytrade.backtest.BacktestResults "tastytrade.backtest.BacktestResults.snapshots (Python parameter)")
        * [`statistics (tastytrade.backtest.BacktestStatistics | None)`](backtesting.html#tastytrade.backtest.BacktestResults "tastytrade.backtest.BacktestResults.statistics (Python parameter)")
        * [`trials (list[tastytrade.backtest.BacktestTrial] | None)`](backtesting.html#tastytrade.backtest.BacktestResults "tastytrade.backtest.BacktestResults.trials (Python parameter)")

*class* tastytrade.backtest.BacktestSession(*[session](backtesting.html#tastytrade.backtest.BacktestSession "tastytrade.backtest.BacktestSession.__init__.session (Python parameter)"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*)[¶](backtesting.html#tastytrade.backtest.BacktestSession "Link to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    Class for creating a backtesting session which can be reused for multiple backtests.

    Example usage:

    ```
    from tastytrade import BacktestSession, Backtest
    from tqdm.asyncio import tqdm  # progress bar

    backtest = Backtest(...)
    backtest_session = BacktestSession(session)
    results = [r async for r in tqdm(backtest_session.run(backtest))]
    print(results[-1])

    ```

    *async* available\_parameters() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[BacktestParameters](backtesting.html#tastytrade.backtest.BacktestParameters "tastytrade.backtest.BacktestParameters (Python model) — Bases: BacktestData")][¶](backtesting.html#tastytrade.backtest.BacktestSession.available_parameters "Link to this definition")
    :   Get a list of available symbols for backtesting, as well as valid testing dates
        for each symbol.

    *async* cancel(*[backtest\_id](backtesting.html#tastytrade.backtest.BacktestSession.cancel.backtest_id "tastytrade.backtest.BacktestSession.cancel.backtest_id (Python parameter) — ID of the backtest to cancel"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[¶](backtesting.html#tastytrade.backtest.BacktestSession.cancel "Link to this definition")
    :   Cancel the running backtest with the given ID.

        Parameters:[¶](backtesting.html#tastytrade.backtest.BacktestSession.cancel-parameters "Permalink to this headline")
        :   backtest\_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](backtesting.html#tastytrade.backtest.BacktestSession.cancel.backtest_id "Permalink to this definition")
            :   ID of the backtest to cancel

    *async* delete() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[¶](backtesting.html#tastytrade.backtest.BacktestSession.delete "Link to this definition")
    :   Delete the active backtesting session.

    *async* get(*[backtest\_id](backtesting.html#tastytrade.backtest.BacktestSession.get "tastytrade.backtest.BacktestSession.get.backtest_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*) → [BacktestResponse](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse (Python model) — Bases: Backtest")[¶](backtesting.html#tastytrade.backtest.BacktestSession.get "Link to this definition")
    :   Fetch a specific past backtest by ID.

    *async* run(*[backtest](backtesting.html#tastytrade.backtest.BacktestSession.run.backtest "tastytrade.backtest.BacktestSession.run.backtest (Python parameter) — configuration for the backtest"): [Backtest](backtesting.html#tastytrade.backtest.Backtest "tastytrade.backtest.Backtest (Python model) — Bases: BacktestData")*) → [AsyncGenerator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncGenerator "(in Python v3.13)")[[BacktestResponse](backtesting.html#tastytrade.backtest.BacktestResponse "tastytrade.backtest.BacktestResponse (Python model) — Bases: Backtest"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][¶](backtesting.html#tastytrade.backtest.BacktestSession.run "Link to this definition")
    :   Run the given backtest and yield results progresively.

        Parameters:[¶](backtesting.html#tastytrade.backtest.BacktestSession.run-parameters "Permalink to this headline")
        :   backtest: [Backtest](backtesting.html#tastytrade.backtest.Backtest "tastytrade.backtest.Backtest (Python model) — Bases: BacktestData")[¶](backtesting.html#tastytrade.backtest.BacktestSession.run.backtest "Permalink to this definition")
            :   configuration for the backtest

*pydantic model* tastytrade.backtest.BacktestSnapshot(*\**, *[dateTime](backtesting.html#tastytrade.backtest.BacktestSnapshot "tastytrade.backtest.BacktestSnapshot.dateTime (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[profitLoss](backtesting.html#tastytrade.backtest.BacktestSnapshot "tastytrade.backtest.BacktestSnapshot.profitLoss (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[normalizedUnderlyingPrice](backtesting.html#tastytrade.backtest.BacktestSnapshot "tastytrade.backtest.BacktestSnapshot.normalizedUnderlyingPrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[underlyingPrice](backtesting.html#tastytrade.backtest.BacktestSnapshot "tastytrade.backtest.BacktestSnapshot.underlyingPrice (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](backtesting.html#tastytrade.backtest.BacktestSnapshot "Link to this definition")
:   Bases: [`BacktestData`](backtesting.html#tastytrade.backtest.BacktestData "tastytrade.backtest.BacktestData (Python model) — Bases: BaseModel")

    Dataclass containing a snapshot in time during the backtest.

    Show JSON schema

    ```
    {
       "title": "BacktestSnapshot",
       "description": "Dataclass containing a snapshot in time during the backtest.",
       "type": "object",
       "properties": {
          "dateTime": {
             "format": "date-time",
             "title": "Datetime",
             "type": "string"
          },
          "profitLoss": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Profitloss"
          },
          "normalizedUnderlyingPrice": {
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
             "title": "Normalizedunderlyingprice"
          },
          "underlyingPrice": {
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
             "title": "Underlyingprice"
          }
       },
       "required": [
          "dateTime",
          "profitLoss"
       ]
    }

    ```

    Fields:[¶](backtesting.html#tastytrade.backtest.BacktestSnapshot-fields "Permalink to this headline")
    :   * `date_time (datetime.datetime)`
        * `normalized_underlying_price (decimal.Decimal | None)`
        * `profit_loss (decimal.Decimal)`
        * `underlying_price (decimal.Decimal | None)`

*pydantic model* tastytrade.backtest.BacktestStatistics(*\**, *[avg\_bp\_per\_trade](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.avg_bp_per_trade (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[avg\_daily\_pnl\_change](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.avg_daily_pnl_change (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[avg\_daily\_net\_liq\_change](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.avg_daily_net_liq_change (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[avg\_days\_in\_trade](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.avg_days_in_trade (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[avg\_premium](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.avg_premium (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[avg\_profit\_loss\_per\_trade](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.avg_profit_loss_per_trade (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[avg\_return\_per\_trade](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.avg_return_per_trade (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[highest\_profit](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.highest_profit (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[loss\_percentage](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.loss_percentage (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[Losses](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.Losses (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[max\_drawdown](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.max_drawdown (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[number\_of\_trades](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.number_of_trades (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[premium\_capture\_rate](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.premium_capture_rate (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[return\_on\_used\_capital](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.return_on_used_capital (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[total\_fees](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.total_fees (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[total\_premium](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.total_premium (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[total\_profit\_loss](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.total_profit_loss (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[used\_capital](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.used_capital (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[win\_percentage](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.win_percentage (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[Wins](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.Wins (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[worst\_loss](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.worst_loss (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*)[¶](backtesting.html#tastytrade.backtest.BacktestStatistics "Link to this definition")
:   Bases: `BaseModel`

    Dataclass containing statistics on the overall performance of a backtest.

    Show JSON schema

    ```
    {
       "title": "BacktestStatistics",
       "description": "Dataclass containing statistics on the overall performance of a backtest.",
       "type": "object",
       "properties": {
          "Avg. BPR per trade": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Avg. Bpr Per Trade"
          },
          "Avg. daily change in PNL": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Avg. Daily Change In Pnl"
          },
          "Avg. daily change in net liq": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Avg. Daily Change In Net Liq"
          },
          "Avg. days in trade": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Avg. Days In Trade"
          },
          "Avg. premium": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Avg. Premium"
          },
          "Avg. profit/loss per trade": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Avg. Profit/Loss Per Trade"
          },
          "Avg. return per trade": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Avg. Return Per Trade"
          },
          "Highest profit": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Highest Profit"
          },
          "Loss percentage": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Loss Percentage"
          },
          "Losses": {
             "title": "Losses",
             "type": "integer"
          },
          "Max drawdown": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Max Drawdown"
          },
          "Number of trades": {
             "title": "Number Of Trades",
             "type": "integer"
          },
          "Premium capture rate": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Premium Capture Rate"
          },
          "Return on used capital": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Return On Used Capital"
          },
          "Total fees": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Total Fees"
          },
          "Total premium": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Total Premium"
          },
          "Total profit/loss": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Total Profit/Loss"
          },
          "Used capital": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Used Capital"
          },
          "Win percentage": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Win Percentage"
          },
          "Wins": {
             "title": "Wins",
             "type": "integer"
          },
          "Worst loss": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Worst Loss"
          }
       },
       "required": [
          "Avg. BPR per trade",
          "Avg. daily change in PNL",
          "Avg. daily change in net liq",
          "Avg. days in trade",
          "Avg. premium",
          "Avg. profit/loss per trade",
          "Avg. return per trade",
          "Highest profit",
          "Loss percentage",
          "Losses",
          "Max drawdown",
          "Number of trades",
          "Premium capture rate",
          "Return on used capital",
          "Total fees",
          "Total premium",
          "Total profit/loss",
          "Used capital",
          "Win percentage",
          "Wins",
          "Worst loss"
       ]
    }

    ```

    Fields:[¶](backtesting.html#tastytrade.backtest.BacktestStatistics-fields "Permalink to this headline")
    :   * [`avg_bp_per_trade (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.avg_bp_per_trade (Python parameter)")
        * [`avg_daily_net_liq_change (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.avg_daily_net_liq_change (Python parameter)")
        * [`avg_daily_pnl_change (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.avg_daily_pnl_change (Python parameter)")
        * [`avg_days_in_trade (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.avg_days_in_trade (Python parameter)")
        * [`avg_premium (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.avg_premium (Python parameter)")
        * [`avg_profit_loss_per_trade (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.avg_profit_loss_per_trade (Python parameter)")
        * [`avg_return_per_trade (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.avg_return_per_trade (Python parameter)")
        * [`highest_profit (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.highest_profit (Python parameter)")
        * [`loss_percentage (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.loss_percentage (Python parameter)")
        * `losses (int)`
        * [`max_drawdown (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.max_drawdown (Python parameter)")
        * [`number_of_trades (int)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.number_of_trades (Python parameter)")
        * [`premium_capture_rate (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.premium_capture_rate (Python parameter)")
        * [`return_on_used_capital (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.return_on_used_capital (Python parameter)")
        * [`total_fees (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.total_fees (Python parameter)")
        * [`total_premium (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.total_premium (Python parameter)")
        * [`total_profit_loss (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.total_profit_loss (Python parameter)")
        * [`used_capital (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.used_capital (Python parameter)")
        * [`win_percentage (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.win_percentage (Python parameter)")
        * `wins (int)`
        * [`worst_loss (decimal.Decimal)`](backtesting.html#tastytrade.backtest.BacktestStatistics "tastytrade.backtest.BacktestStatistics.worst_loss (Python parameter)")

*pydantic model* tastytrade.backtest.BacktestTrial(*\**, *[closeDateTime](backtesting.html#tastytrade.backtest.BacktestTrial "tastytrade.backtest.BacktestTrial.closeDateTime (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[openDateTime](backtesting.html#tastytrade.backtest.BacktestTrial "tastytrade.backtest.BacktestTrial.openDateTime (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[profitLoss](backtesting.html#tastytrade.backtest.BacktestTrial "tastytrade.backtest.BacktestTrial.profitLoss (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*)[¶](backtesting.html#tastytrade.backtest.BacktestTrial "Link to this definition")
:   Bases: [`BacktestData`](backtesting.html#tastytrade.backtest.BacktestData "tastytrade.backtest.BacktestData (Python model) — Bases: BaseModel")

    Dataclass containing information on trades placed during the backtest.

    Show JSON schema

    ```
    {
       "title": "BacktestTrial",
       "description": "Dataclass containing information on trades placed during the backtest.",
       "type": "object",
       "properties": {
          "closeDateTime": {
             "format": "date-time",
             "title": "Closedatetime",
             "type": "string"
          },
          "openDateTime": {
             "format": "date-time",
             "title": "Opendatetime",
             "type": "string"
          },
          "profitLoss": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Profitloss"
          }
       },
       "required": [
          "closeDateTime",
          "openDateTime",
          "profitLoss"
       ]
    }

    ```

    Fields:[¶](backtesting.html#tastytrade.backtest.BacktestTrial-fields "Permalink to this headline")
    :   * `close_date_time (datetime.datetime)`
        * `open_date_time (datetime.datetime)`
        * `profit_loss (decimal.Decimal)`

[Back to top](backtesting.html#)


[Previous
tastytrade.account](account.html)
[Next
tastytrade.dxfeed](dxfeed.html)

© Copyright 2025, tastyware.

Created using
[Sphinx](https://www.sphinx-doc.org/)
7.4.7.
and
[Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)