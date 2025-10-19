tastytrade.metrics - tastytrade 10.1.0 documentation







[Skip to content](metrics.html#tastytrade.metrics.DividendInfo)

tastytrade 10.1.0 documentation

tastytrade.metrics






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
  + tastytrade.metrics

    [tastytrade.metrics](metrics.html#)



    tastytrade.metrics
    - [tastytrade.metrics.DividendInfo](metrics.html#tastytrade.metrics.DividendInfo)

      * [Fields](metrics.html#tastytrade.metrics.DividendInfo-fields)
    - [tastytrade.metrics.EarningsInfo](metrics.html#tastytrade.metrics.EarningsInfo)

      * [Fields](metrics.html#tastytrade.metrics.EarningsInfo-fields)
    - [tastytrade.metrics.EarningsReport](metrics.html#tastytrade.metrics.EarningsReport)

      * [Fields](metrics.html#tastytrade.metrics.EarningsReport-fields)
    - [tastytrade.metrics.Liquidity](metrics.html#tastytrade.metrics.Liquidity)

      * [Fields](metrics.html#tastytrade.metrics.Liquidity-fields)
    - [tastytrade.metrics.MarketMetricInfo](metrics.html#tastytrade.metrics.MarketMetricInfo)

      * [Fields](metrics.html#tastytrade.metrics.MarketMetricInfo-fields)
    - [tastytrade.metrics.OptionExpirationImpliedVolatility](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility)

      * [Fields](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility-fields)
    - [Ftastytrade.metrics.a\_get\_dividends](metrics.html#tastytrade.metrics.a_get_dividends)

      * [Parameters](metrics.html#tastytrade.metrics.a_get_dividends-parameters)

        + [psession](metrics.html#tastytrade.metrics.a_get_dividends.session)
        + [psymbol](metrics.html#tastytrade.metrics.a_get_dividends.symbol)
    - [Ftastytrade.metrics.a\_get\_earnings](metrics.html#tastytrade.metrics.a_get_earnings)

      * [Parameters](metrics.html#tastytrade.metrics.a_get_earnings-parameters)

        + [psession](metrics.html#tastytrade.metrics.a_get_earnings.session)
        + [psymbol](metrics.html#tastytrade.metrics.a_get_earnings.symbol)
        + [pstart\_date](metrics.html#tastytrade.metrics.a_get_earnings.start_date)
    - [Ftastytrade.metrics.a\_get\_market\_metrics](metrics.html#tastytrade.metrics.a_get_market_metrics)

      * [Parameters](metrics.html#tastytrade.metrics.a_get_market_metrics-parameters)

        + [psession](metrics.html#tastytrade.metrics.a_get_market_metrics.session)
        + [psymbols](metrics.html#tastytrade.metrics.a_get_market_metrics.symbols)
    - [Ftastytrade.metrics.a\_get\_risk\_free\_rate](metrics.html#tastytrade.metrics.a_get_risk_free_rate)

      * [Parameters](metrics.html#tastytrade.metrics.a_get_risk_free_rate-parameters)

        + [psession](metrics.html#tastytrade.metrics.a_get_risk_free_rate.session)
    - [Ftastytrade.metrics.get\_dividends](metrics.html#tastytrade.metrics.get_dividends)

      * [Parameters](metrics.html#tastytrade.metrics.get_dividends-parameters)

        + [psession](metrics.html#tastytrade.metrics.get_dividends.session)
        + [psymbol](metrics.html#tastytrade.metrics.get_dividends.symbol)
    - [Ftastytrade.metrics.get\_earnings](metrics.html#tastytrade.metrics.get_earnings)

      * [Parameters](metrics.html#tastytrade.metrics.get_earnings-parameters)

        + [psession](metrics.html#tastytrade.metrics.get_earnings.session)
        + [psymbol](metrics.html#tastytrade.metrics.get_earnings.symbol)
        + [pstart\_date](metrics.html#tastytrade.metrics.get_earnings.start_date)
    - [Ftastytrade.metrics.get\_market\_metrics](metrics.html#tastytrade.metrics.get_market_metrics)

      * [Parameters](metrics.html#tastytrade.metrics.get_market_metrics-parameters)

        + [psession](metrics.html#tastytrade.metrics.get_market_metrics.session)
        + [psymbols](metrics.html#tastytrade.metrics.get_market_metrics.symbols)
    - [Ftastytrade.metrics.get\_risk\_free\_rate](metrics.html#tastytrade.metrics.get_risk_free_rate)

      * [Parameters](metrics.html#tastytrade.metrics.get_risk_free_rate-parameters)

        + [psession](metrics.html#tastytrade.metrics.get_risk_free_rate.session)
  + [tastytrade.order](order.html)
  + [tastytrade.search](search.html)
  + [tastytrade.session](session.html)
  + [tastytrade.streamer](streamer.html)
  + [tastytrade.utils](utils.html)
  + [tastytrade.watchlists](watchlists.html)

tastytrade.metrics

* [tastytrade.metrics.DividendInfo](metrics.html#tastytrade.metrics.DividendInfo)

  + [Fields](metrics.html#tastytrade.metrics.DividendInfo-fields)
* [tastytrade.metrics.EarningsInfo](metrics.html#tastytrade.metrics.EarningsInfo)

  + [Fields](metrics.html#tastytrade.metrics.EarningsInfo-fields)
* [tastytrade.metrics.EarningsReport](metrics.html#tastytrade.metrics.EarningsReport)

  + [Fields](metrics.html#tastytrade.metrics.EarningsReport-fields)
* [tastytrade.metrics.Liquidity](metrics.html#tastytrade.metrics.Liquidity)

  + [Fields](metrics.html#tastytrade.metrics.Liquidity-fields)
* [tastytrade.metrics.MarketMetricInfo](metrics.html#tastytrade.metrics.MarketMetricInfo)

  + [Fields](metrics.html#tastytrade.metrics.MarketMetricInfo-fields)
* [tastytrade.metrics.OptionExpirationImpliedVolatility](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility)

  + [Fields](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility-fields)
* [Ftastytrade.metrics.a\_get\_dividends](metrics.html#tastytrade.metrics.a_get_dividends)

  + [Parameters](metrics.html#tastytrade.metrics.a_get_dividends-parameters)

    - [psession](metrics.html#tastytrade.metrics.a_get_dividends.session)
    - [psymbol](metrics.html#tastytrade.metrics.a_get_dividends.symbol)
* [Ftastytrade.metrics.a\_get\_earnings](metrics.html#tastytrade.metrics.a_get_earnings)

  + [Parameters](metrics.html#tastytrade.metrics.a_get_earnings-parameters)

    - [psession](metrics.html#tastytrade.metrics.a_get_earnings.session)
    - [psymbol](metrics.html#tastytrade.metrics.a_get_earnings.symbol)
    - [pstart\_date](metrics.html#tastytrade.metrics.a_get_earnings.start_date)
* [Ftastytrade.metrics.a\_get\_market\_metrics](metrics.html#tastytrade.metrics.a_get_market_metrics)

  + [Parameters](metrics.html#tastytrade.metrics.a_get_market_metrics-parameters)

    - [psession](metrics.html#tastytrade.metrics.a_get_market_metrics.session)
    - [psymbols](metrics.html#tastytrade.metrics.a_get_market_metrics.symbols)
* [Ftastytrade.metrics.a\_get\_risk\_free\_rate](metrics.html#tastytrade.metrics.a_get_risk_free_rate)

  + [Parameters](metrics.html#tastytrade.metrics.a_get_risk_free_rate-parameters)

    - [psession](metrics.html#tastytrade.metrics.a_get_risk_free_rate.session)
* [Ftastytrade.metrics.get\_dividends](metrics.html#tastytrade.metrics.get_dividends)

  + [Parameters](metrics.html#tastytrade.metrics.get_dividends-parameters)

    - [psession](metrics.html#tastytrade.metrics.get_dividends.session)
    - [psymbol](metrics.html#tastytrade.metrics.get_dividends.symbol)
* [Ftastytrade.metrics.get\_earnings](metrics.html#tastytrade.metrics.get_earnings)

  + [Parameters](metrics.html#tastytrade.metrics.get_earnings-parameters)

    - [psession](metrics.html#tastytrade.metrics.get_earnings.session)
    - [psymbol](metrics.html#tastytrade.metrics.get_earnings.symbol)
    - [pstart\_date](metrics.html#tastytrade.metrics.get_earnings.start_date)
* [Ftastytrade.metrics.get\_market\_metrics](metrics.html#tastytrade.metrics.get_market_metrics)

  + [Parameters](metrics.html#tastytrade.metrics.get_market_metrics-parameters)

    - [psession](metrics.html#tastytrade.metrics.get_market_metrics.session)
    - [psymbols](metrics.html#tastytrade.metrics.get_market_metrics.symbols)
* [Ftastytrade.metrics.get\_risk\_free\_rate](metrics.html#tastytrade.metrics.get_risk_free_rate)

  + [Parameters](metrics.html#tastytrade.metrics.get_risk_free_rate-parameters)

    - [psession](metrics.html#tastytrade.metrics.get_risk_free_rate.session)

# tastytrade.metrics[¶](metrics.html#module-tastytrade.metrics "Link to this heading")

*pydantic model* tastytrade.metrics.DividendInfo(*\**, *[occurred\_date](metrics.html#tastytrade.metrics.DividendInfo "tastytrade.metrics.DividendInfo.occurred_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*, *[amount](metrics.html#tastytrade.metrics.DividendInfo "tastytrade.metrics.DividendInfo.amount (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*)[¶](metrics.html#tastytrade.metrics.DividendInfo "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass representing dividend information for a given symbol.

    Show JSON schema

    ```
    {
       "title": "DividendInfo",
       "description": "Dataclass representing dividend information for a given symbol.",
       "type": "object",
       "properties": {
          "occurred-date": {
             "format": "date",
             "title": "Occurred-Date",
             "type": "string"
          },
          "amount": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Amount"
          }
       },
       "required": [
          "occurred-date",
          "amount"
       ]
    }

    ```

    Fields:[¶](metrics.html#tastytrade.metrics.DividendInfo-fields "Permalink to this headline")
    :   * [`amount (decimal.Decimal)`](metrics.html#tastytrade.metrics.DividendInfo "tastytrade.metrics.DividendInfo.amount (Python parameter)")
        * [`occurred_date (datetime.date)`](metrics.html#tastytrade.metrics.DividendInfo "tastytrade.metrics.DividendInfo.occurred_date (Python parameter)")

*pydantic model* tastytrade.metrics.EarningsInfo(*\**, *[occurred\_date](metrics.html#tastytrade.metrics.EarningsInfo "tastytrade.metrics.EarningsInfo.occurred_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*, *[eps](metrics.html#tastytrade.metrics.EarningsInfo "tastytrade.metrics.EarningsInfo.eps (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*)[¶](metrics.html#tastytrade.metrics.EarningsInfo "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass representing earnings information for a given symbol.

    Show JSON schema

    ```
    {
       "title": "EarningsInfo",
       "description": "Dataclass representing earnings information for a given symbol.",
       "type": "object",
       "properties": {
          "occurred-date": {
             "format": "date",
             "title": "Occurred-Date",
             "type": "string"
          },
          "eps": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Eps"
          }
       },
       "required": [
          "occurred-date",
          "eps"
       ]
    }

    ```

    Fields:[¶](metrics.html#tastytrade.metrics.EarningsInfo-fields "Permalink to this headline")
    :   * [`eps (decimal.Decimal)`](metrics.html#tastytrade.metrics.EarningsInfo "tastytrade.metrics.EarningsInfo.eps (Python parameter)")
        * [`occurred_date (datetime.date)`](metrics.html#tastytrade.metrics.EarningsInfo "tastytrade.metrics.EarningsInfo.occurred_date (Python parameter)")

*pydantic model* tastytrade.metrics.EarningsReport(*\**, *[estimated](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.estimated (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[late\_flag](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.late_flag (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[visible](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.visible (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[actual\_eps](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.actual_eps (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[consensus\_estimate](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.consensus_estimate (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[expected\_report\_date](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.expected_report_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[quarter\_end\_date](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.quarter_end_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[time\_of\_day](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.time_of_day (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[updated\_at](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.updated_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](metrics.html#tastytrade.metrics.EarningsReport "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about a recent earnings report, or the
    expected date of the next one.

    Show JSON schema

    ```
    {
       "title": "EarningsReport",
       "description": "Dataclass containing information about a recent earnings report, or the\nexpected date of the next one.",
       "type": "object",
       "properties": {
          "estimated": {
             "title": "Estimated",
             "type": "boolean"
          },
          "late-flag": {
             "title": "Late-Flag",
             "type": "integer"
          },
          "visible": {
             "title": "Visible",
             "type": "boolean"
          },
          "actual-eps": {
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
             "title": "Actual-Eps"
          },
          "consensus-estimate": {
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
             "title": "Consensus-Estimate"
          },
          "expected-report-date": {
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
             "title": "Expected-Report-Date"
          },
          "quarter-end-date": {
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
             "title": "Quarter-End-Date"
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
          }
       },
       "required": [
          "estimated",
          "late-flag",
          "visible"
       ]
    }

    ```

    Fields:[¶](metrics.html#tastytrade.metrics.EarningsReport-fields "Permalink to this headline")
    :   * [`actual_eps (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.actual_eps (Python parameter)")
        * [`consensus_estimate (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.consensus_estimate (Python parameter)")
        * [`estimated (bool)`](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.estimated (Python parameter)")
        * [`expected_report_date (datetime.date | None)`](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.expected_report_date (Python parameter)")
        * [`late_flag (int)`](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.late_flag (Python parameter)")
        * [`quarter_end_date (datetime.date | None)`](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.quarter_end_date (Python parameter)")
        * [`time_of_day (str | None)`](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.time_of_day (Python parameter)")
        * [`updated_at (datetime.datetime | None)`](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.updated_at (Python parameter)")
        * [`visible (bool)`](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport.visible (Python parameter)")

*pydantic model* tastytrade.metrics.Liquidity(*\**, *[sum](metrics.html#tastytrade.metrics.Liquidity "tastytrade.metrics.Liquidity.sum (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[count](metrics.html#tastytrade.metrics.Liquidity "tastytrade.metrics.Liquidity.count (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[started\_at](metrics.html#tastytrade.metrics.Liquidity "tastytrade.metrics.Liquidity.started_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[updated\_at](metrics.html#tastytrade.metrics.Liquidity "tastytrade.metrics.Liquidity.updated_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](metrics.html#tastytrade.metrics.Liquidity "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass representing liquidity information for a given symbol.

    Show JSON schema

    ```
    {
       "title": "Liquidity",
       "description": "Dataclass representing liquidity information for a given symbol.",
       "type": "object",
       "properties": {
          "sum": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Sum"
          },
          "count": {
             "title": "Count",
             "type": "integer"
          },
          "started-at": {
             "format": "date-time",
             "title": "Started-At",
             "type": "string"
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
          }
       },
       "required": [
          "sum",
          "count",
          "started-at"
       ]
    }

    ```

    Fields:[¶](metrics.html#tastytrade.metrics.Liquidity-fields "Permalink to this headline")
    :   * [`count (int)`](metrics.html#tastytrade.metrics.Liquidity "tastytrade.metrics.Liquidity.count (Python parameter)")
        * [`started_at (datetime.datetime)`](metrics.html#tastytrade.metrics.Liquidity "tastytrade.metrics.Liquidity.started_at (Python parameter)")
        * [`sum (decimal.Decimal)`](metrics.html#tastytrade.metrics.Liquidity "tastytrade.metrics.Liquidity.sum (Python parameter)")
        * [`updated_at (datetime.datetime | None)`](metrics.html#tastytrade.metrics.Liquidity "tastytrade.metrics.Liquidity.updated_at (Python parameter)")

*pydantic model* tastytrade.metrics.MarketMetricInfo(*\**, *[symbol](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[implied\_volatility\_index](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.implied_volatility_index (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[implied\_volatility\_index\_5\_day\_change](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.implied_volatility_index_5_day_change (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[implied\_volatility\_index\_rank](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.implied_volatility_index_rank (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[tos\_implied\_volatility\_index\_rank](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.tos_implied_volatility_index_rank (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[tw\_implied\_volatility\_index\_rank](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.tw_implied_volatility_index_rank (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[tos\_implied\_volatility\_index\_rank\_updated\_at](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.tos_implied_volatility_index_rank_updated_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[implied\_volatility\_index\_rank\_source](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.implied_volatility_index_rank_source (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[implied\_volatility\_percentile](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.implied_volatility_percentile (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[implied\_volatility\_updated\_at](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.implied_volatility_updated_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[liquidity\_rating](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.liquidity_rating (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[updated\_at](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.updated_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[option\_expiration\_implied\_volatilities](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.option_expiration_implied_volatilities (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[OptionExpirationImpliedVolatility](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility "tastytrade.metrics.OptionExpirationImpliedVolatility (Python model) — Bases: TastytradeData")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[beta](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.beta (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[corr\_spy\_3month](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.corr_spy_3month (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[market\_cap](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.market_cap (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")*, *[earnings](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.earnings (Python parameter)"): [EarningsReport](metrics.html#tastytrade.metrics.EarningsReport "tastytrade.metrics.EarningsReport (Python model) — Bases: TastytradeData") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[price\_earnings\_ratio](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.price_earnings_ratio (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[earnings\_per\_share](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.earnings_per_share (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[dividend\_rate\_per\_share](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.dividend_rate_per_share (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[implied\_volatility\_30\_day](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.implied_volatility_30_day (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[historical\_volatility\_30\_day](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.historical_volatility_30_day (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[historical\_volatility\_60\_day](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.historical_volatility_60_day (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[historical\_volatility\_90\_day](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.historical_volatility_90_day (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[iv\_hv\_30\_day\_difference](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.iv_hv_30_day_difference (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[beta\_updated\_at](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.beta_updated_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[created\_at](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.created_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[dividend\_ex\_date](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.dividend_ex_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[dividend\_next\_date](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.dividend_next_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[dividend\_pay\_date](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.dividend_pay_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[dividend\_updated\_at](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.dividend_updated_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[liquidity\_value](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.liquidity_value (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[liquidity\_rank](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.liquidity_rank (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[liquidity\_running\_state](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.liquidity_running_state (Python parameter)"): [Liquidity](metrics.html#tastytrade.metrics.Liquidity "tastytrade.metrics.Liquidity (Python model) — Bases: TastytradeData") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[dividend\_yield](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.dividend_yield (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[listed\_market](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.listed_market (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[lendability](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.lendability (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[borrow\_rate](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.borrow_rate (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](metrics.html#tastytrade.metrics.MarketMetricInfo "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass representing market metrics for a given symbol.

    Contains lots of useful information, like IV rank, IV percentile and beta.

    Show JSON schema

    ```
    {
       "title": "MarketMetricInfo",
       "description": "Dataclass representing market metrics for a given symbol.\n\nContains lots of useful information, like IV rank, IV percentile and beta.",
       "type": "object",
       "properties": {
          "symbol": {
             "title": "Symbol",
             "type": "string"
          },
          "implied-volatility-index": {
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
             "title": "Implied-Volatility-Index"
          },
          "implied-volatility-index-5-day-change": {
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
             "title": "Implied-Volatility-Index-5-Day-Change"
          },
          "implied-volatility-index-rank": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Implied-Volatility-Index-Rank"
          },
          "tos-implied-volatility-index-rank": {
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
             "title": "Tos-Implied-Volatility-Index-Rank"
          },
          "tw-implied-volatility-index-rank": {
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
             "title": "Tw-Implied-Volatility-Index-Rank"
          },
          "tos-implied-volatility-index-rank-updated-at": {
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
             "title": "Tos-Implied-Volatility-Index-Rank-Updated-At"
          },
          "implied-volatility-index-rank-source": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Implied-Volatility-Index-Rank-Source"
          },
          "implied-volatility-percentile": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Implied-Volatility-Percentile"
          },
          "implied-volatility-updated-at": {
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
             "title": "Implied-Volatility-Updated-At"
          },
          "liquidity-rating": {
             "anyOf": [
                {
                   "type": "integer"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Liquidity-Rating"
          },
          "updated-at": {
             "format": "date-time",
             "title": "Updated-At",
             "type": "string"
          },
          "option-expiration-implied-volatilities": {
             "anyOf": [
                {
                   "items": {
                      "$ref": "#/$defs/OptionExpirationImpliedVolatility"
                   },
                   "type": "array"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Option-Expiration-Implied-Volatilities"
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
          "corr-spy-3month": {
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
             "title": "Corr-Spy-3Month"
          },
          "market-cap": {
             "anyOf": [
                {
                   "type": "number"
                },
                {
                   "type": "string"
                }
             ],
             "title": "Market-Cap"
          },
          "earnings": {
             "anyOf": [
                {
                   "$ref": "#/$defs/EarningsReport"
                },
                {
                   "type": "null"
                }
             ],
             "default": null
          },
          "price-earnings-ratio": {
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
             "title": "Price-Earnings-Ratio"
          },
          "earnings-per-share": {
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
             "title": "Earnings-Per-Share"
          },
          "dividend-rate-per-share": {
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
             "title": "Dividend-Rate-Per-Share"
          },
          "implied-volatility-30-day": {
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
             "title": "Implied-Volatility-30-Day"
          },
          "historical-volatility-30-day": {
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
             "title": "Historical-Volatility-30-Day"
          },
          "historical-volatility-60-day": {
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
             "title": "Historical-Volatility-60-Day"
          },
          "historical-volatility-90-day": {
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
             "title": "Historical-Volatility-90-Day"
          },
          "iv-hv-30-day-difference": {
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
             "title": "Iv-Hv-30-Day-Difference"
          },
          "beta-updated-at": {
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
             "title": "Beta-Updated-At"
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
          },
          "dividend-ex-date": {
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
             "title": "Dividend-Ex-Date"
          },
          "dividend-next-date": {
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
             "title": "Dividend-Next-Date"
          },
          "dividend-pay-date": {
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
             "title": "Dividend-Pay-Date"
          },
          "dividend-updated-at": {
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
             "title": "Dividend-Updated-At"
          },
          "liquidity-value": {
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
             "title": "Liquidity-Value"
          },
          "liquidity-rank": {
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
             "title": "Liquidity-Rank"
          },
          "liquidity-running-state": {
             "anyOf": [
                {
                   "$ref": "#/$defs/Liquidity"
                },
                {
                   "type": "null"
                }
             ],
             "default": null
          },
          "dividend-yield": {
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
             "title": "Dividend-Yield"
          },
          "listed-market": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Listed-Market"
          },
          "lendability": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Lendability"
          },
          "borrow-rate": {
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
             "title": "Borrow-Rate"
          }
       },
       "$defs": {
          "EarningsReport": {
             "description": "Dataclass containing information about a recent earnings report, or the\nexpected date of the next one.",
             "properties": {
                "estimated": {
                   "title": "Estimated",
                   "type": "boolean"
                },
                "late-flag": {
                   "title": "Late-Flag",
                   "type": "integer"
                },
                "visible": {
                   "title": "Visible",
                   "type": "boolean"
                },
                "actual-eps": {
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
                   "title": "Actual-Eps"
                },
                "consensus-estimate": {
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
                   "title": "Consensus-Estimate"
                },
                "expected-report-date": {
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
                   "title": "Expected-Report-Date"
                },
                "quarter-end-date": {
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
                   "title": "Quarter-End-Date"
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
                }
             },
             "required": [
                "estimated",
                "late-flag",
                "visible"
             ],
             "title": "EarningsReport",
             "type": "object"
          },
          "Liquidity": {
             "description": "Dataclass representing liquidity information for a given symbol.",
             "properties": {
                "sum": {
                   "anyOf": [
                      {
                         "type": "number"
                      },
                      {
                         "type": "string"
                      }
                   ],
                   "title": "Sum"
                },
                "count": {
                   "title": "Count",
                   "type": "integer"
                },
                "started-at": {
                   "format": "date-time",
                   "title": "Started-At",
                   "type": "string"
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
                }
             },
             "required": [
                "sum",
                "count",
                "started-at"
             ],
             "title": "Liquidity",
             "type": "object"
          },
          "OptionExpirationImpliedVolatility": {
             "description": "Dataclass containing implied volatility information for a given symbol\nand expiration date.",
             "properties": {
                "expiration-date": {
                   "format": "date",
                   "title": "Expiration-Date",
                   "type": "string"
                },
                "settlement-type": {
                   "title": "Settlement-Type",
                   "type": "string"
                },
                "option-chain-type": {
                   "title": "Option-Chain-Type",
                   "type": "string"
                },
                "implied-volatility": {
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
                   "title": "Implied-Volatility"
                }
             },
             "required": [
                "expiration-date",
                "settlement-type",
                "option-chain-type"
             ],
             "title": "OptionExpirationImpliedVolatility",
             "type": "object"
          }
       },
       "required": [
          "symbol",
          "updated-at",
          "market-cap"
       ]
    }

    ```

    Fields:[¶](metrics.html#tastytrade.metrics.MarketMetricInfo-fields "Permalink to this headline")
    :   * [`beta (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.beta (Python parameter)")
        * [`beta_updated_at (datetime.datetime | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.beta_updated_at (Python parameter)")
        * [`borrow_rate (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.borrow_rate (Python parameter)")
        * [`corr_spy_3month (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.corr_spy_3month (Python parameter)")
        * [`created_at (datetime.datetime | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.created_at (Python parameter)")
        * [`dividend_ex_date (datetime.date | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.dividend_ex_date (Python parameter)")
        * [`dividend_next_date (datetime.date | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.dividend_next_date (Python parameter)")
        * [`dividend_pay_date (datetime.date | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.dividend_pay_date (Python parameter)")
        * [`dividend_rate_per_share (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.dividend_rate_per_share (Python parameter)")
        * [`dividend_updated_at (datetime.datetime | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.dividend_updated_at (Python parameter)")
        * [`dividend_yield (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.dividend_yield (Python parameter)")
        * [`earnings (tastytrade.metrics.EarningsReport | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.earnings (Python parameter)")
        * [`earnings_per_share (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.earnings_per_share (Python parameter)")
        * [`historical_volatility_30_day (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.historical_volatility_30_day (Python parameter)")
        * [`historical_volatility_60_day (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.historical_volatility_60_day (Python parameter)")
        * [`historical_volatility_90_day (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.historical_volatility_90_day (Python parameter)")
        * [`implied_volatility_30_day (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.implied_volatility_30_day (Python parameter)")
        * [`implied_volatility_index (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.implied_volatility_index (Python parameter)")
        * [`implied_volatility_index_5_day_change (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.implied_volatility_index_5_day_change (Python parameter)")
        * [`implied_volatility_index_rank (str | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.implied_volatility_index_rank (Python parameter)")
        * [`implied_volatility_index_rank_source (str | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.implied_volatility_index_rank_source (Python parameter)")
        * [`implied_volatility_percentile (str | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.implied_volatility_percentile (Python parameter)")
        * [`implied_volatility_updated_at (datetime.datetime | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.implied_volatility_updated_at (Python parameter)")
        * [`iv_hv_30_day_difference (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.iv_hv_30_day_difference (Python parameter)")
        * [`lendability (str | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.lendability (Python parameter)")
        * [`liquidity_rank (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.liquidity_rank (Python parameter)")
        * [`liquidity_rating (int | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.liquidity_rating (Python parameter)")
        * [`liquidity_running_state (tastytrade.metrics.Liquidity | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.liquidity_running_state (Python parameter)")
        * [`liquidity_value (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.liquidity_value (Python parameter)")
        * [`listed_market (str | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.listed_market (Python parameter)")
        * [`market_cap (decimal.Decimal)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.market_cap (Python parameter)")
        * [`option_expiration_implied_volatilities (list[tastytrade.metrics.OptionExpirationImpliedVolatility] | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.option_expiration_implied_volatilities (Python parameter)")
        * [`price_earnings_ratio (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.price_earnings_ratio (Python parameter)")
        * [`symbol (str)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.symbol (Python parameter)")
        * [`tos_implied_volatility_index_rank (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.tos_implied_volatility_index_rank (Python parameter)")
        * [`tos_implied_volatility_index_rank_updated_at (datetime.datetime | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.tos_implied_volatility_index_rank_updated_at (Python parameter)")
        * [`tw_implied_volatility_index_rank (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.tw_implied_volatility_index_rank (Python parameter)")
        * [`updated_at (datetime.datetime)`](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo.updated_at (Python parameter)")

*pydantic model* tastytrade.metrics.OptionExpirationImpliedVolatility(*\**, *[expiration\_date](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility "tastytrade.metrics.OptionExpirationImpliedVolatility.expiration_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*, *[settlement\_type](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility "tastytrade.metrics.OptionExpirationImpliedVolatility.settlement_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[option\_chain\_type](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility "tastytrade.metrics.OptionExpirationImpliedVolatility.option_chain_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[implied\_volatility](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility "tastytrade.metrics.OptionExpirationImpliedVolatility.implied_volatility (Python parameter)"): [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing implied volatility information for a given symbol
    and expiration date.

    Show JSON schema

    ```
    {
       "title": "OptionExpirationImpliedVolatility",
       "description": "Dataclass containing implied volatility information for a given symbol\nand expiration date.",
       "type": "object",
       "properties": {
          "expiration-date": {
             "format": "date",
             "title": "Expiration-Date",
             "type": "string"
          },
          "settlement-type": {
             "title": "Settlement-Type",
             "type": "string"
          },
          "option-chain-type": {
             "title": "Option-Chain-Type",
             "type": "string"
          },
          "implied-volatility": {
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
             "title": "Implied-Volatility"
          }
       },
       "required": [
          "expiration-date",
          "settlement-type",
          "option-chain-type"
       ]
    }

    ```

    Fields:[¶](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility-fields "Permalink to this headline")
    :   * [`expiration_date (datetime.date)`](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility "tastytrade.metrics.OptionExpirationImpliedVolatility.expiration_date (Python parameter)")
        * [`implied_volatility (decimal.Decimal | None)`](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility "tastytrade.metrics.OptionExpirationImpliedVolatility.implied_volatility (Python parameter)")
        * [`option_chain_type (str)`](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility "tastytrade.metrics.OptionExpirationImpliedVolatility.option_chain_type (Python parameter)")
        * [`settlement_type (str)`](metrics.html#tastytrade.metrics.OptionExpirationImpliedVolatility "tastytrade.metrics.OptionExpirationImpliedVolatility.settlement_type (Python parameter)")

*async* tastytrade.metrics.a\_get\_dividends(*[session](metrics.html#tastytrade.metrics.a_get_dividends.session "tastytrade.metrics.a_get_dividends.session (Python parameter) — active user session to use"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[symbol](metrics.html#tastytrade.metrics.a_get_dividends.symbol "tastytrade.metrics.a_get_dividends.symbol (Python parameter) — symbol to retrieve dividend information for"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[DividendInfo](metrics.html#tastytrade.metrics.DividendInfo "tastytrade.metrics.DividendInfo (Python model) — Bases: TastytradeData")][¶](metrics.html#tastytrade.metrics.a_get_dividends "Link to this definition")
:   Retrieves dividend information for the given symbol.

    Parameters:[¶](metrics.html#tastytrade.metrics.a_get_dividends-parameters "Permalink to this headline")
    :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](metrics.html#tastytrade.metrics.a_get_dividends.session "Permalink to this definition")
        :   active user session to use

        symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](metrics.html#tastytrade.metrics.a_get_dividends.symbol "Permalink to this definition")
        :   symbol to retrieve dividend information for

*async* tastytrade.metrics.a\_get\_earnings(*[session](metrics.html#tastytrade.metrics.a_get_earnings.session "tastytrade.metrics.a_get_earnings.session (Python parameter) — active user session to use"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[symbol](metrics.html#tastytrade.metrics.a_get_earnings.symbol "tastytrade.metrics.a_get_earnings.symbol (Python parameter) — symbol to retrieve earnings information for"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[start\_date](metrics.html#tastytrade.metrics.a_get_earnings.start_date "tastytrade.metrics.a_get_earnings.start_date (Python parameter) — limits earnings to those on or after the given date"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[EarningsInfo](metrics.html#tastytrade.metrics.EarningsInfo "tastytrade.metrics.EarningsInfo (Python model) — Bases: TastytradeData")][¶](metrics.html#tastytrade.metrics.a_get_earnings "Link to this definition")
:   Retrieves earnings information for the given symbol.

    Parameters:[¶](metrics.html#tastytrade.metrics.a_get_earnings-parameters "Permalink to this headline")
    :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](metrics.html#tastytrade.metrics.a_get_earnings.session "Permalink to this definition")
        :   active user session to use

        symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](metrics.html#tastytrade.metrics.a_get_earnings.symbol "Permalink to this definition")
        :   symbol to retrieve earnings information for

        start\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")[¶](metrics.html#tastytrade.metrics.a_get_earnings.start_date "Permalink to this definition")
        :   limits earnings to those on or after the given date

*async* tastytrade.metrics.a\_get\_market\_metrics(*[session](metrics.html#tastytrade.metrics.a_get_market_metrics.session "tastytrade.metrics.a_get_market_metrics.session (Python parameter) — active user session to use"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[symbols](metrics.html#tastytrade.metrics.a_get_market_metrics.symbols "tastytrade.metrics.a_get_market_metrics.symbols (Python parameter) — list of symbols to retrieve metrics for"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[MarketMetricInfo](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo (Python model) — Bases: TastytradeData")][¶](metrics.html#tastytrade.metrics.a_get_market_metrics "Link to this definition")
:   Retrieves market metrics for the given symbols.

    Parameters:[¶](metrics.html#tastytrade.metrics.a_get_market_metrics-parameters "Permalink to this headline")
    :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](metrics.html#tastytrade.metrics.a_get_market_metrics.session "Permalink to this definition")
        :   active user session to use

        symbols: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")][¶](metrics.html#tastytrade.metrics.a_get_market_metrics.symbols "Permalink to this definition")
        :   list of symbols to retrieve metrics for

*async* tastytrade.metrics.a\_get\_risk\_free\_rate(*[session](metrics.html#tastytrade.metrics.a_get_risk_free_rate.session "tastytrade.metrics.a_get_risk_free_rate.session (Python parameter) — active user session to use"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")[¶](metrics.html#tastytrade.metrics.a_get_risk_free_rate "Link to this definition")
:   Retrieves the current risk-free rate.

    Parameters:[¶](metrics.html#tastytrade.metrics.a_get_risk_free_rate-parameters "Permalink to this headline")
    :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](metrics.html#tastytrade.metrics.a_get_risk_free_rate.session "Permalink to this definition")
        :   active user session to use

tastytrade.metrics.get\_dividends(*[session](metrics.html#tastytrade.metrics.get_dividends.session "tastytrade.metrics.get_dividends.session (Python parameter) — active user session to use"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[symbol](metrics.html#tastytrade.metrics.get_dividends.symbol "tastytrade.metrics.get_dividends.symbol (Python parameter) — symbol to retrieve dividend information for"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[DividendInfo](metrics.html#tastytrade.metrics.DividendInfo "tastytrade.metrics.DividendInfo (Python model) — Bases: TastytradeData")][¶](metrics.html#tastytrade.metrics.get_dividends "Link to this definition")
:   Retrieves dividend information for the given symbol.

    Parameters:[¶](metrics.html#tastytrade.metrics.get_dividends-parameters "Permalink to this headline")
    :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](metrics.html#tastytrade.metrics.get_dividends.session "Permalink to this definition")
        :   active user session to use

        symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](metrics.html#tastytrade.metrics.get_dividends.symbol "Permalink to this definition")
        :   symbol to retrieve dividend information for

tastytrade.metrics.get\_earnings(*[session](metrics.html#tastytrade.metrics.get_earnings.session "tastytrade.metrics.get_earnings.session (Python parameter) — active user session to use"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[symbol](metrics.html#tastytrade.metrics.get_earnings.symbol "tastytrade.metrics.get_earnings.symbol (Python parameter) — symbol to retrieve earnings information for"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[start\_date](metrics.html#tastytrade.metrics.get_earnings.start_date "tastytrade.metrics.get_earnings.start_date (Python parameter) — limits earnings to those on or after the given date"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[EarningsInfo](metrics.html#tastytrade.metrics.EarningsInfo "tastytrade.metrics.EarningsInfo (Python model) — Bases: TastytradeData")][¶](metrics.html#tastytrade.metrics.get_earnings "Link to this definition")
:   Retrieves earnings information for the given symbol.

    Parameters:[¶](metrics.html#tastytrade.metrics.get_earnings-parameters "Permalink to this headline")
    :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](metrics.html#tastytrade.metrics.get_earnings.session "Permalink to this definition")
        :   active user session to use

        symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](metrics.html#tastytrade.metrics.get_earnings.symbol "Permalink to this definition")
        :   symbol to retrieve earnings information for

        start\_date: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")[¶](metrics.html#tastytrade.metrics.get_earnings.start_date "Permalink to this definition")
        :   limits earnings to those on or after the given date

tastytrade.metrics.get\_market\_metrics(*[session](metrics.html#tastytrade.metrics.get_market_metrics.session "tastytrade.metrics.get_market_metrics.session (Python parameter) — active user session to use"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[symbols](metrics.html#tastytrade.metrics.get_market_metrics.symbols "tastytrade.metrics.get_market_metrics.symbols (Python parameter) — list of symbols to retrieve metrics for"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[MarketMetricInfo](metrics.html#tastytrade.metrics.MarketMetricInfo "tastytrade.metrics.MarketMetricInfo (Python model) — Bases: TastytradeData")][¶](metrics.html#tastytrade.metrics.get_market_metrics "Link to this definition")
:   Retrieves market metrics for the given symbols.

    Parameters:[¶](metrics.html#tastytrade.metrics.get_market_metrics-parameters "Permalink to this headline")
    :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](metrics.html#tastytrade.metrics.get_market_metrics.session "Permalink to this definition")
        :   active user session to use

        symbols: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")][¶](metrics.html#tastytrade.metrics.get_market_metrics.symbols "Permalink to this definition")
        :   list of symbols to retrieve metrics for

tastytrade.metrics.get\_risk\_free\_rate(*[session](metrics.html#tastytrade.metrics.get_risk_free_rate.session "tastytrade.metrics.get_risk_free_rate.session (Python parameter) — active user session to use"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*) → [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.13)")[¶](metrics.html#tastytrade.metrics.get_risk_free_rate "Link to this definition")
:   Retrieves the current risk-free rate.

    Parameters:[¶](metrics.html#tastytrade.metrics.get_risk_free_rate-parameters "Permalink to this headline")
    :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](metrics.html#tastytrade.metrics.get_risk_free_rate.session "Permalink to this definition")
        :   active user session to use

[Back to top](metrics.html#)


[Previous
tastytrade.market\_sessions](market-sessions.html)
[Next
tastytrade.order](order.html)

© Copyright 2025, tastyware.

Created using
[Sphinx](https://www.sphinx-doc.org/)
7.4.7.
and
[Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)