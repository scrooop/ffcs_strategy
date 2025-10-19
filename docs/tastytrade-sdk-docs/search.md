tastytrade.search - tastytrade 10.1.0 documentation







[Skip to content](search.html#tastytrade.search.SymbolData)

tastytrade 10.1.0 documentation

tastytrade.search






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
  + tastytrade.search

    [tastytrade.search](search.html#)



    tastytrade.search
    - [tastytrade.search.SymbolData](search.html#tastytrade.search.SymbolData)

      * [Fields](search.html#tastytrade.search.SymbolData-fields)
    - [Ftastytrade.search.a\_symbol\_search](search.html#tastytrade.search.a_symbol_search)

      * [Parameters](search.html#tastytrade.search.a_symbol_search-parameters)

        + [psession](search.html#tastytrade.search.a_symbol_search.session)
        + [psymbol](search.html#tastytrade.search.a_symbol_search.symbol)
    - [Ftastytrade.search.symbol\_search](search.html#tastytrade.search.symbol_search)

      * [Parameters](search.html#tastytrade.search.symbol_search-parameters)

        + [psession](search.html#tastytrade.search.symbol_search.session)
        + [psymbol](search.html#tastytrade.search.symbol_search.symbol)
  + [tastytrade.session](session.html)
  + [tastytrade.streamer](streamer.html)
  + [tastytrade.utils](utils.html)
  + [tastytrade.watchlists](watchlists.html)

tastytrade.search

* [tastytrade.search.SymbolData](search.html#tastytrade.search.SymbolData)

  + [Fields](search.html#tastytrade.search.SymbolData-fields)
* [Ftastytrade.search.a\_symbol\_search](search.html#tastytrade.search.a_symbol_search)

  + [Parameters](search.html#tastytrade.search.a_symbol_search-parameters)

    - [psession](search.html#tastytrade.search.a_symbol_search.session)
    - [psymbol](search.html#tastytrade.search.a_symbol_search.symbol)
* [Ftastytrade.search.symbol\_search](search.html#tastytrade.search.symbol_search)

  + [Parameters](search.html#tastytrade.search.symbol_search-parameters)

    - [psession](search.html#tastytrade.search.symbol_search.session)
    - [psymbol](search.html#tastytrade.search.symbol_search.symbol)

# tastytrade.search[¶](search.html#module-tastytrade.search "Link to this heading")

*pydantic model* tastytrade.search.SymbolData(*\**, *[symbol](search.html#tastytrade.search.SymbolData "tastytrade.search.SymbolData.symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[description](search.html#tastytrade.search.SymbolData "tastytrade.search.SymbolData.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)[¶](search.html#tastytrade.search.SymbolData "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass holding search results for an individual item.

    Show JSON schema

    ```
    {
       "title": "SymbolData",
       "description": "Dataclass holding search results for an individual item.",
       "type": "object",
       "properties": {
          "symbol": {
             "title": "Symbol",
             "type": "string"
          },
          "description": {
             "title": "Description",
             "type": "string"
          }
       },
       "required": [
          "symbol",
          "description"
       ]
    }

    ```

    Fields:[¶](search.html#tastytrade.search.SymbolData-fields "Permalink to this headline")
    :   * [`description (str)`](search.html#tastytrade.search.SymbolData "tastytrade.search.SymbolData.description (Python parameter)")
        * [`symbol (str)`](search.html#tastytrade.search.SymbolData "tastytrade.search.SymbolData.symbol (Python parameter)")

*async* tastytrade.search.a\_symbol\_search(*[session](search.html#tastytrade.search.a_symbol_search.session "tastytrade.search.a_symbol_search.session (Python parameter) — active user session to use"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[symbol](search.html#tastytrade.search.a_symbol_search.symbol "tastytrade.search.a_symbol_search.symbol (Python parameter) — search phrase"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[SymbolData](search.html#tastytrade.search.SymbolData "tastytrade.search.SymbolData (Python model) — Bases: TastytradeData")][¶](search.html#tastytrade.search.a_symbol_search "Link to this definition")
:   Performs a symbol search using the Tastytrade API and returns a
    list of symbols that are similar to the given search phrase.

    Parameters:[¶](search.html#tastytrade.search.a_symbol_search-parameters "Permalink to this headline")
    :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](search.html#tastytrade.search.a_symbol_search.session "Permalink to this definition")
        :   active user session to use

        symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](search.html#tastytrade.search.a_symbol_search.symbol "Permalink to this definition")
        :   search phrase

tastytrade.search.symbol\_search(*[session](search.html#tastytrade.search.symbol_search.session "tastytrade.search.symbol_search.session (Python parameter) — active user session to use"): [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")*, *[symbol](search.html#tastytrade.search.symbol_search.symbol "tastytrade.search.symbol_search.symbol (Python parameter) — search phrase"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[SymbolData](search.html#tastytrade.search.SymbolData "tastytrade.search.SymbolData (Python model) — Bases: TastytradeData")][¶](search.html#tastytrade.search.symbol_search "Link to this definition")
:   Performs a symbol search using the Tastytrade API and returns a
    list of symbols that are similar to the given search phrase.

    Parameters:[¶](search.html#tastytrade.search.symbol_search-parameters "Permalink to this headline")
    :   session: [Session](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")[¶](search.html#tastytrade.search.symbol_search.session "Permalink to this definition")
        :   active user session to use

        symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](search.html#tastytrade.search.symbol_search.symbol "Permalink to this definition")
        :   search phrase

[Back to top](search.html#)


[Previous
tastytrade.order](order.html)
[Next
tastytrade.session](session.html)

© Copyright 2025, tastyware.

Created using
[Sphinx](https://www.sphinx-doc.org/)
7.4.7.
and
[Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)