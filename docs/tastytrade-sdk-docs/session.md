tastytrade.session - tastytrade 10.1.0 documentation







[Skip to content](session.html#tastytrade.session.Address)

tastytrade 10.1.0 documentation

tastytrade.session






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
  + tastytrade.session

    [tastytrade.session](session.html#)



    tastytrade.session
    - [tastytrade.session.Address](session.html#tastytrade.session.Address)

      * [Fields](session.html#tastytrade.session.Address-fields)
    - [tastytrade.session.Customer](session.html#tastytrade.session.Customer)

      * [Fields](session.html#tastytrade.session.Customer-fields)
    - [tastytrade.session.CustomerAccountMarginType](session.html#tastytrade.session.CustomerAccountMarginType)

      * [Fields](session.html#tastytrade.session.CustomerAccountMarginType-fields)
    - [tastytrade.session.CustomerAccountType](session.html#tastytrade.session.CustomerAccountType)

      * [Fields](session.html#tastytrade.session.CustomerAccountType-fields)
    - [tastytrade.session.CustomerEntity](session.html#tastytrade.session.CustomerEntity)

      * [Fields](session.html#tastytrade.session.CustomerEntity-fields)
    - [tastytrade.session.CustomerPerson](session.html#tastytrade.session.CustomerPerson)

      * [Fields](session.html#tastytrade.session.CustomerPerson-fields)
    - [tastytrade.session.CustomerSuitability](session.html#tastytrade.session.CustomerSuitability)

      * [Fields](session.html#tastytrade.session.CustomerSuitability-fields)
    - [tastytrade.session.EntityOfficer](session.html#tastytrade.session.EntityOfficer)

      * [Fields](session.html#tastytrade.session.EntityOfficer-fields)
    - [tastytrade.session.EntitySuitability](session.html#tastytrade.session.EntitySuitability)

      * [Fields](session.html#tastytrade.session.EntitySuitability-fields)
    - [Ctastytrade.session.OAuthSession](session.html#tastytrade.session.OAuthSession)

      * [Parameters](session.html#tastytrade.session.OAuthSession-parameters)

        + [pprovider\_secret](session.html#tastytrade.session.OAuthSession.__init__.provider_secret)
        + [prefresh\_token](session.html#tastytrade.session.OAuthSession.__init__.refresh_token)
        + [pis\_test](session.html#tastytrade.session.OAuthSession.__init__.is_test)
        + [pproxy](session.html#tastytrade.session.OAuthSession.__init__.proxy)
      * [Ma\_refresh](session.html#tastytrade.session.OAuthSession.a_refresh)
      * [Aasync\_client](session.html#tastytrade.session.OAuthSession.async_client)
      * [Mdeserialize](session.html#tastytrade.session.OAuthSession.deserialize)
      * [Aexpires\_at](session.html#tastytrade.session.OAuthSession.expires_at)
      * [Ais\_test](session.html#tastytrade.session.OAuthSession.is_test)
      * [Aprovider\_secret](session.html#tastytrade.session.OAuthSession.provider_secret)
      * [Aproxy](session.html#tastytrade.session.OAuthSession.proxy)
      * [Mrefresh](session.html#tastytrade.session.OAuthSession.refresh)
      * [Arefresh\_token](session.html#tastytrade.session.OAuthSession.refresh_token)
      * [Mserialize](session.html#tastytrade.session.OAuthSession.serialize)
      * [Async\_client](session.html#tastytrade.session.OAuthSession.sync_client)
    - [Ctastytrade.session.Session](session.html#tastytrade.session.Session)

      * [Parameters](session.html#tastytrade.session.Session-parameters)

        + [plogin](session.html#tastytrade.session.Session.__init__.login)
        + [premember\_me](session.html#tastytrade.session.Session.__init__.remember_me)
        + [ppassword](session.html#tastytrade.session.Session.__init__.password)
        + [premember\_token](session.html#tastytrade.session.Session.__init__.remember_token)
        + [pis\_test](session.html#tastytrade.session.Session.__init__.is_test)
        + [ptwo\_factor\_authentication](session.html#tastytrade.session.Session.__init__.two_factor_authentication)
        + [pdxfeed\_tos\_compliant](session.html#tastytrade.session.Session.__init__.dxfeed_tos_compliant)
        + [pproxy](session.html#tastytrade.session.Session.__init__.proxy)
      * [Ma\_destroy](session.html#tastytrade.session.Session.a_destroy)
      * [Ma\_get\_2fa\_info](session.html#tastytrade.session.Session.a_get_2fa_info)
      * [Ma\_get\_customer](session.html#tastytrade.session.Session.a_get_customer)

        + [Returns](session.html#tastytrade.session.Session.a_get_customer-returns)
      * [Ma\_validate](session.html#tastytrade.session.Session.a_validate)

        + [Returns](session.html#tastytrade.session.Session.a_validate-returns)
      * [Aasync\_client](session.html#tastytrade.session.Session.async_client)
      * [Mdeserialize](session.html#tastytrade.session.Session.deserialize)
      * [Mdestroy](session.html#tastytrade.session.Session.destroy)
      * [Adxlink\_url](session.html#tastytrade.session.Session.dxlink_url)
      * [Mget\_2fa\_info](session.html#tastytrade.session.Session.get_2fa_info)
      * [Mget\_customer](session.html#tastytrade.session.Session.get_customer)

        + [Returns](session.html#tastytrade.session.Session.get_customer-returns)
      * [Ais\_test](session.html#tastytrade.session.Session.is_test)
      * [Aproxy](session.html#tastytrade.session.Session.proxy)
      * [Aremember\_token](session.html#tastytrade.session.Session.remember_token)
      * [Mserialize](session.html#tastytrade.session.Session.serialize)
      * [Asession\_expiration](session.html#tastytrade.session.Session.session_expiration)
      * [Asession\_token](session.html#tastytrade.session.Session.session_token)
      * [Astreamer\_token](session.html#tastytrade.session.Session.streamer_token)
      * [Async\_client](session.html#tastytrade.session.Session.sync_client)
      * [Auser](session.html#tastytrade.session.Session.user)
      * [Mvalidate](session.html#tastytrade.session.Session.validate)

        + [Returns](session.html#tastytrade.session.Session.validate-returns)
    - [tastytrade.session.TwoFactorInfo](session.html#tastytrade.session.TwoFactorInfo)

      * [Fields](session.html#tastytrade.session.TwoFactorInfo-fields)
    - [tastytrade.session.User](session.html#tastytrade.session.User)

      * [Fields](session.html#tastytrade.session.User-fields)
  + [tastytrade.streamer](streamer.html)
  + [tastytrade.utils](utils.html)
  + [tastytrade.watchlists](watchlists.html)

tastytrade.session

* [tastytrade.session.Address](session.html#tastytrade.session.Address)

  + [Fields](session.html#tastytrade.session.Address-fields)
* [tastytrade.session.Customer](session.html#tastytrade.session.Customer)

  + [Fields](session.html#tastytrade.session.Customer-fields)
* [tastytrade.session.CustomerAccountMarginType](session.html#tastytrade.session.CustomerAccountMarginType)

  + [Fields](session.html#tastytrade.session.CustomerAccountMarginType-fields)
* [tastytrade.session.CustomerAccountType](session.html#tastytrade.session.CustomerAccountType)

  + [Fields](session.html#tastytrade.session.CustomerAccountType-fields)
* [tastytrade.session.CustomerEntity](session.html#tastytrade.session.CustomerEntity)

  + [Fields](session.html#tastytrade.session.CustomerEntity-fields)
* [tastytrade.session.CustomerPerson](session.html#tastytrade.session.CustomerPerson)

  + [Fields](session.html#tastytrade.session.CustomerPerson-fields)
* [tastytrade.session.CustomerSuitability](session.html#tastytrade.session.CustomerSuitability)

  + [Fields](session.html#tastytrade.session.CustomerSuitability-fields)
* [tastytrade.session.EntityOfficer](session.html#tastytrade.session.EntityOfficer)

  + [Fields](session.html#tastytrade.session.EntityOfficer-fields)
* [tastytrade.session.EntitySuitability](session.html#tastytrade.session.EntitySuitability)

  + [Fields](session.html#tastytrade.session.EntitySuitability-fields)
* [Ctastytrade.session.OAuthSession](session.html#tastytrade.session.OAuthSession)

  + [Parameters](session.html#tastytrade.session.OAuthSession-parameters)

    - [pprovider\_secret](session.html#tastytrade.session.OAuthSession.__init__.provider_secret)
    - [prefresh\_token](session.html#tastytrade.session.OAuthSession.__init__.refresh_token)
    - [pis\_test](session.html#tastytrade.session.OAuthSession.__init__.is_test)
    - [pproxy](session.html#tastytrade.session.OAuthSession.__init__.proxy)
  + [Ma\_refresh](session.html#tastytrade.session.OAuthSession.a_refresh)
  + [Aasync\_client](session.html#tastytrade.session.OAuthSession.async_client)
  + [Mdeserialize](session.html#tastytrade.session.OAuthSession.deserialize)
  + [Aexpires\_at](session.html#tastytrade.session.OAuthSession.expires_at)
  + [Ais\_test](session.html#tastytrade.session.OAuthSession.is_test)
  + [Aprovider\_secret](session.html#tastytrade.session.OAuthSession.provider_secret)
  + [Aproxy](session.html#tastytrade.session.OAuthSession.proxy)
  + [Mrefresh](session.html#tastytrade.session.OAuthSession.refresh)
  + [Arefresh\_token](session.html#tastytrade.session.OAuthSession.refresh_token)
  + [Mserialize](session.html#tastytrade.session.OAuthSession.serialize)
  + [Async\_client](session.html#tastytrade.session.OAuthSession.sync_client)
* [Ctastytrade.session.Session](session.html#tastytrade.session.Session)

  + [Parameters](session.html#tastytrade.session.Session-parameters)

    - [plogin](session.html#tastytrade.session.Session.__init__.login)
    - [premember\_me](session.html#tastytrade.session.Session.__init__.remember_me)
    - [ppassword](session.html#tastytrade.session.Session.__init__.password)
    - [premember\_token](session.html#tastytrade.session.Session.__init__.remember_token)
    - [pis\_test](session.html#tastytrade.session.Session.__init__.is_test)
    - [ptwo\_factor\_authentication](session.html#tastytrade.session.Session.__init__.two_factor_authentication)
    - [pdxfeed\_tos\_compliant](session.html#tastytrade.session.Session.__init__.dxfeed_tos_compliant)
    - [pproxy](session.html#tastytrade.session.Session.__init__.proxy)
  + [Ma\_destroy](session.html#tastytrade.session.Session.a_destroy)
  + [Ma\_get\_2fa\_info](session.html#tastytrade.session.Session.a_get_2fa_info)
  + [Ma\_get\_customer](session.html#tastytrade.session.Session.a_get_customer)

    - [Returns](session.html#tastytrade.session.Session.a_get_customer-returns)
  + [Ma\_validate](session.html#tastytrade.session.Session.a_validate)

    - [Returns](session.html#tastytrade.session.Session.a_validate-returns)
  + [Aasync\_client](session.html#tastytrade.session.Session.async_client)
  + [Mdeserialize](session.html#tastytrade.session.Session.deserialize)
  + [Mdestroy](session.html#tastytrade.session.Session.destroy)
  + [Adxlink\_url](session.html#tastytrade.session.Session.dxlink_url)
  + [Mget\_2fa\_info](session.html#tastytrade.session.Session.get_2fa_info)
  + [Mget\_customer](session.html#tastytrade.session.Session.get_customer)

    - [Returns](session.html#tastytrade.session.Session.get_customer-returns)
  + [Ais\_test](session.html#tastytrade.session.Session.is_test)
  + [Aproxy](session.html#tastytrade.session.Session.proxy)
  + [Aremember\_token](session.html#tastytrade.session.Session.remember_token)
  + [Mserialize](session.html#tastytrade.session.Session.serialize)
  + [Asession\_expiration](session.html#tastytrade.session.Session.session_expiration)
  + [Asession\_token](session.html#tastytrade.session.Session.session_token)
  + [Astreamer\_token](session.html#tastytrade.session.Session.streamer_token)
  + [Async\_client](session.html#tastytrade.session.Session.sync_client)
  + [Auser](session.html#tastytrade.session.Session.user)
  + [Mvalidate](session.html#tastytrade.session.Session.validate)

    - [Returns](session.html#tastytrade.session.Session.validate-returns)
* [tastytrade.session.TwoFactorInfo](session.html#tastytrade.session.TwoFactorInfo)

  + [Fields](session.html#tastytrade.session.TwoFactorInfo-fields)
* [tastytrade.session.User](session.html#tastytrade.session.User)

  + [Fields](session.html#tastytrade.session.User-fields)

# tastytrade.session[¶](session.html#module-tastytrade.session "Link to this heading")

*pydantic model* tastytrade.session.Address(*\**, *[city](session.html#tastytrade.session.Address "tastytrade.session.Address.city (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[country](session.html#tastytrade.session.Address "tastytrade.session.Address.country (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[is\_domestic](session.html#tastytrade.session.Address "tastytrade.session.Address.is_domestic (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_foreign](session.html#tastytrade.session.Address "tastytrade.session.Address.is_foreign (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[postal\_code](session.html#tastytrade.session.Address "tastytrade.session.Address.postal_code (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[state\_region](session.html#tastytrade.session.Address "tastytrade.session.Address.state_region (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[street\_one](session.html#tastytrade.session.Address "tastytrade.session.Address.street_one (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[street\_two](session.html#tastytrade.session.Address "tastytrade.session.Address.street_two (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[street\_three](session.html#tastytrade.session.Address "tastytrade.session.Address.street_three (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](session.html#tastytrade.session.Address "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing customer address information.

    Show JSON schema

    ```
    {
       "title": "Address",
       "description": "Dataclass containing customer address information.",
       "type": "object",
       "properties": {
          "city": {
             "title": "City",
             "type": "string"
          },
          "country": {
             "title": "Country",
             "type": "string"
          },
          "is-domestic": {
             "title": "Is-Domestic",
             "type": "boolean"
          },
          "is-foreign": {
             "title": "Is-Foreign",
             "type": "boolean"
          },
          "postal-code": {
             "title": "Postal-Code",
             "type": "string"
          },
          "state-region": {
             "title": "State-Region",
             "type": "string"
          },
          "street-one": {
             "title": "Street-One",
             "type": "string"
          },
          "street-two": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Street-Two"
          },
          "street-three": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Street-Three"
          }
       },
       "required": [
          "city",
          "country",
          "is-domestic",
          "is-foreign",
          "postal-code",
          "state-region",
          "street-one"
       ]
    }

    ```

    Fields:[¶](session.html#tastytrade.session.Address-fields "Permalink to this headline")
    :   * [`city (str)`](session.html#tastytrade.session.Address "tastytrade.session.Address.city (Python parameter)")
        * [`country (str)`](session.html#tastytrade.session.Address "tastytrade.session.Address.country (Python parameter)")
        * [`is_domestic (bool)`](session.html#tastytrade.session.Address "tastytrade.session.Address.is_domestic (Python parameter)")
        * [`is_foreign (bool)`](session.html#tastytrade.session.Address "tastytrade.session.Address.is_foreign (Python parameter)")
        * [`postal_code (str)`](session.html#tastytrade.session.Address "tastytrade.session.Address.postal_code (Python parameter)")
        * [`state_region (str)`](session.html#tastytrade.session.Address "tastytrade.session.Address.state_region (Python parameter)")
        * [`street_one (str)`](session.html#tastytrade.session.Address "tastytrade.session.Address.street_one (Python parameter)")
        * [`street_three (str | None)`](session.html#tastytrade.session.Address "tastytrade.session.Address.street_three (Python parameter)")
        * [`street_two (str | None)`](session.html#tastytrade.session.Address "tastytrade.session.Address.street_two (Python parameter)")

*pydantic model* tastytrade.session.Customer(*\**, *[id](session.html#tastytrade.session.Customer "tastytrade.session.Customer.id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[first\_name](session.html#tastytrade.session.Customer "tastytrade.session.Customer.first_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[first\_surname](session.html#tastytrade.session.Customer "tastytrade.session.Customer.first_surname (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[last\_name](session.html#tastytrade.session.Customer "tastytrade.session.Customer.last_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[address](session.html#tastytrade.session.Customer "tastytrade.session.Customer.address (Python parameter)"): [Address](session.html#tastytrade.session.Address "tastytrade.session.Address (Python model) — Bases: TastytradeData")*, *[customer\_suitability](session.html#tastytrade.session.Customer "tastytrade.session.Customer.customer_suitability (Python parameter)"): [CustomerSuitability](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability (Python model) — Bases: TastytradeData")*, *[mailing\_address](session.html#tastytrade.session.Customer "tastytrade.session.Customer.mailing_address (Python parameter)"): [Address](session.html#tastytrade.session.Address "tastytrade.session.Address (Python model) — Bases: TastytradeData")*, *[is\_foreign](session.html#tastytrade.session.Customer "tastytrade.session.Customer.is_foreign (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[regulatory\_domain](session.html#tastytrade.session.Customer "tastytrade.session.Customer.regulatory_domain (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[usa\_citizenship\_type](session.html#tastytrade.session.Customer "tastytrade.session.Customer.usa_citizenship_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[home\_phone\_number](session.html#tastytrade.session.Customer "tastytrade.session.Customer.home_phone_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[mobile\_phone\_number](session.html#tastytrade.session.Customer "tastytrade.session.Customer.mobile_phone_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[work\_phone\_number](session.html#tastytrade.session.Customer "tastytrade.session.Customer.work_phone_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[birth\_date](session.html#tastytrade.session.Customer "tastytrade.session.Customer.birth_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*, *[email](session.html#tastytrade.session.Customer "tastytrade.session.Customer.email (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[external\_id](session.html#tastytrade.session.Customer "tastytrade.session.Customer.external_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[tax\_number](session.html#tastytrade.session.Customer "tastytrade.session.Customer.tax_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[tax\_number\_type](session.html#tastytrade.session.Customer "tastytrade.session.Customer.tax_number_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[citizenship\_country](session.html#tastytrade.session.Customer "tastytrade.session.Customer.citizenship_country (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[agreed\_to\_margining](session.html#tastytrade.session.Customer "tastytrade.session.Customer.agreed_to_margining (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[subject\_to\_tax\_withholding](session.html#tastytrade.session.Customer "tastytrade.session.Customer.subject_to_tax_withholding (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[agreed\_to\_terms](session.html#tastytrade.session.Customer "tastytrade.session.Customer.agreed_to_terms (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[ext\_crm\_id](session.html#tastytrade.session.Customer "tastytrade.session.Customer.ext_crm_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[has\_industry\_affiliation](session.html#tastytrade.session.Customer "tastytrade.session.Customer.has_industry_affiliation (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[has\_listed\_affiliation](session.html#tastytrade.session.Customer "tastytrade.session.Customer.has_listed_affiliation (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[has\_political\_affiliation](session.html#tastytrade.session.Customer "tastytrade.session.Customer.has_political_affiliation (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[has\_delayed\_quotes](session.html#tastytrade.session.Customer "tastytrade.session.Customer.has_delayed_quotes (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[has\_pending\_or\_approved\_application](session.html#tastytrade.session.Customer "tastytrade.session.Customer.has_pending_or_approved_application (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_professional](session.html#tastytrade.session.Customer "tastytrade.session.Customer.is_professional (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[permitted\_account\_types](session.html#tastytrade.session.Customer "tastytrade.session.Customer.permitted_account_types (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[CustomerAccountType](session.html#tastytrade.session.CustomerAccountType "tastytrade.session.CustomerAccountType (Python model) — Bases: TastytradeData")]*, *[created\_at](session.html#tastytrade.session.Customer "tastytrade.session.Customer.created_at (Python parameter)"): [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.13)")*, *[identifiable\_type](session.html#tastytrade.session.Customer "tastytrade.session.Customer.identifiable_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[person](session.html#tastytrade.session.Customer "tastytrade.session.Customer.person (Python parameter)"): [CustomerPerson](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson (Python model) — Bases: TastytradeData")*, *[gender](session.html#tastytrade.session.Customer "tastytrade.session.Customer.gender (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[middle\_name](session.html#tastytrade.session.Customer "tastytrade.session.Customer.middle_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[prefix\_name](session.html#tastytrade.session.Customer "tastytrade.session.Customer.prefix_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[second\_surname](session.html#tastytrade.session.Customer "tastytrade.session.Customer.second_surname (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[suffix\_name](session.html#tastytrade.session.Customer "tastytrade.session.Customer.suffix_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[foreign\_tax\_number](session.html#tastytrade.session.Customer "tastytrade.session.Customer.foreign_tax_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[birth\_country](session.html#tastytrade.session.Customer "tastytrade.session.Customer.birth_country (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[visa\_expiration\_date](session.html#tastytrade.session.Customer "tastytrade.session.Customer.visa_expiration_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[visa\_type](session.html#tastytrade.session.Customer "tastytrade.session.Customer.visa_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[signature\_of\_agreement](session.html#tastytrade.session.Customer "tastytrade.session.Customer.signature_of_agreement (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[desk\_customer\_id](session.html#tastytrade.session.Customer "tastytrade.session.Customer.desk_customer_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[entity](session.html#tastytrade.session.Customer "tastytrade.session.Customer.entity (Python parameter)"): [CustomerEntity](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity (Python model) — Bases: TastytradeData") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[family\_member\_names](session.html#tastytrade.session.Customer "tastytrade.session.Customer.family_member_names (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[has\_institutional\_assets](session.html#tastytrade.session.Customer "tastytrade.session.Customer.has_institutional_assets (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[industry\_affiliation\_firm](session.html#tastytrade.session.Customer "tastytrade.session.Customer.industry_affiliation_firm (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[is\_investment\_adviser](session.html#tastytrade.session.Customer "tastytrade.session.Customer.is_investment_adviser (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[listed\_affiliation\_symbol](session.html#tastytrade.session.Customer "tastytrade.session.Customer.listed_affiliation_symbol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[political\_organization](session.html#tastytrade.session.Customer "tastytrade.session.Customer.political_organization (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[user\_id](session.html#tastytrade.session.Customer "tastytrade.session.Customer.user_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](session.html#tastytrade.session.Customer "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing customer information.

    Show JSON schema

    ```
    {
       "title": "Customer",
       "description": "Dataclass containing customer information.",
       "type": "object",
       "properties": {
          "id": {
             "title": "Id",
             "type": "string"
          },
          "first-name": {
             "title": "First-Name",
             "type": "string"
          },
          "first-surname": {
             "title": "First-Surname",
             "type": "string"
          },
          "last-name": {
             "title": "Last-Name",
             "type": "string"
          },
          "address": {
             "$ref": "#/$defs/Address"
          },
          "customer-suitability": {
             "$ref": "#/$defs/CustomerSuitability"
          },
          "mailing-address": {
             "$ref": "#/$defs/Address"
          },
          "is-foreign": {
             "title": "Is-Foreign",
             "type": "boolean"
          },
          "regulatory-domain": {
             "title": "Regulatory-Domain",
             "type": "string"
          },
          "usa-citizenship-type": {
             "title": "Usa-Citizenship-Type",
             "type": "string"
          },
          "home-phone-number": {
             "title": "Home-Phone-Number",
             "type": "string"
          },
          "mobile-phone-number": {
             "title": "Mobile-Phone-Number",
             "type": "string"
          },
          "work-phone-number": {
             "title": "Work-Phone-Number",
             "type": "string"
          },
          "birth-date": {
             "format": "date",
             "title": "Birth-Date",
             "type": "string"
          },
          "email": {
             "title": "Email",
             "type": "string"
          },
          "external-id": {
             "title": "External-Id",
             "type": "string"
          },
          "tax-number": {
             "title": "Tax-Number",
             "type": "string"
          },
          "tax-number-type": {
             "title": "Tax-Number-Type",
             "type": "string"
          },
          "citizenship-country": {
             "title": "Citizenship-Country",
             "type": "string"
          },
          "agreed-to-margining": {
             "title": "Agreed-To-Margining",
             "type": "boolean"
          },
          "subject-to-tax-withholding": {
             "title": "Subject-To-Tax-Withholding",
             "type": "boolean"
          },
          "agreed-to-terms": {
             "title": "Agreed-To-Terms",
             "type": "boolean"
          },
          "ext-crm-id": {
             "title": "Ext-Crm-Id",
             "type": "string"
          },
          "has-industry-affiliation": {
             "title": "Has-Industry-Affiliation",
             "type": "boolean"
          },
          "has-listed-affiliation": {
             "title": "Has-Listed-Affiliation",
             "type": "boolean"
          },
          "has-political-affiliation": {
             "title": "Has-Political-Affiliation",
             "type": "boolean"
          },
          "has-delayed-quotes": {
             "title": "Has-Delayed-Quotes",
             "type": "boolean"
          },
          "has-pending-or-approved-application": {
             "title": "Has-Pending-Or-Approved-Application",
             "type": "boolean"
          },
          "is-professional": {
             "title": "Is-Professional",
             "type": "boolean"
          },
          "permitted-account-types": {
             "items": {
                "$ref": "#/$defs/CustomerAccountType"
             },
             "title": "Permitted-Account-Types",
             "type": "array"
          },
          "created-at": {
             "format": "date-time",
             "title": "Created-At",
             "type": "string"
          },
          "identifiable-type": {
             "title": "Identifiable-Type",
             "type": "string"
          },
          "person": {
             "$ref": "#/$defs/CustomerPerson"
          },
          "gender": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Gender"
          },
          "middle-name": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Middle-Name"
          },
          "prefix-name": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Prefix-Name"
          },
          "second-surname": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Second-Surname"
          },
          "suffix-name": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Suffix-Name"
          },
          "foreign-tax-number": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Foreign-Tax-Number"
          },
          "birth-country": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Birth-Country"
          },
          "visa-expiration-date": {
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
             "title": "Visa-Expiration-Date"
          },
          "visa-type": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Visa-Type"
          },
          "signature-of-agreement": {
             "anyOf": [
                {
                   "type": "boolean"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Signature-Of-Agreement"
          },
          "desk-customer-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Desk-Customer-Id"
          },
          "entity": {
             "anyOf": [
                {
                   "$ref": "#/$defs/CustomerEntity"
                },
                {
                   "type": "null"
                }
             ],
             "default": null
          },
          "family-member-names": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Family-Member-Names"
          },
          "has-institutional-assets": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Has-Institutional-Assets"
          },
          "industry-affiliation-firm": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Industry-Affiliation-Firm"
          },
          "is-investment-adviser": {
             "anyOf": [
                {
                   "type": "boolean"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Is-Investment-Adviser"
          },
          "listed-affiliation-symbol": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Listed-Affiliation-Symbol"
          },
          "political-organization": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Political-Organization"
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
          }
       },
       "$defs": {
          "Address": {
             "description": "Dataclass containing customer address information.",
             "properties": {
                "city": {
                   "title": "City",
                   "type": "string"
                },
                "country": {
                   "title": "Country",
                   "type": "string"
                },
                "is-domestic": {
                   "title": "Is-Domestic",
                   "type": "boolean"
                },
                "is-foreign": {
                   "title": "Is-Foreign",
                   "type": "boolean"
                },
                "postal-code": {
                   "title": "Postal-Code",
                   "type": "string"
                },
                "state-region": {
                   "title": "State-Region",
                   "type": "string"
                },
                "street-one": {
                   "title": "Street-One",
                   "type": "string"
                },
                "street-two": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Street-Two"
                },
                "street-three": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Street-Three"
                }
             },
             "required": [
                "city",
                "country",
                "is-domestic",
                "is-foreign",
                "postal-code",
                "state-region",
                "street-one"
             ],
             "title": "Address",
             "type": "object"
          },
          "CustomerAccountMarginType": {
             "description": "Dataclass containing margin information for a customer account type.",
             "properties": {
                "name": {
                   "title": "Name",
                   "type": "string"
                },
                "is-margin": {
                   "title": "Is-Margin",
                   "type": "boolean"
                }
             },
             "required": [
                "name",
                "is-margin"
             ],
             "title": "CustomerAccountMarginType",
             "type": "object"
          },
          "CustomerAccountType": {
             "description": "Dataclass containing information for a type of customer account.",
             "properties": {
                "name": {
                   "title": "Name",
                   "type": "string"
                },
                "description": {
                   "title": "Description",
                   "type": "string"
                },
                "is-tax-advantaged": {
                   "title": "Is-Tax-Advantaged",
                   "type": "boolean"
                },
                "is-publicly-available": {
                   "title": "Is-Publicly-Available",
                   "type": "boolean"
                },
                "has-multiple-owners": {
                   "title": "Has-Multiple-Owners",
                   "type": "boolean"
                },
                "margin-types": {
                   "items": {
                      "$ref": "#/$defs/CustomerAccountMarginType"
                   },
                   "title": "Margin-Types",
                   "type": "array"
                }
             },
             "required": [
                "name",
                "description",
                "is-tax-advantaged",
                "is-publicly-available",
                "has-multiple-owners",
                "margin-types"
             ],
             "title": "CustomerAccountType",
             "type": "object"
          },
          "CustomerEntity": {
             "description": "Dataclass containing customer entity information.",
             "properties": {
                "id": {
                   "title": "Id",
                   "type": "string"
                },
                "address": {
                   "$ref": "#/$defs/Address"
                },
                "business-nature": {
                   "title": "Business-Nature",
                   "type": "string"
                },
                "email": {
                   "title": "Email",
                   "type": "string"
                },
                "entity-officers": {
                   "items": {
                      "$ref": "#/$defs/EntityOfficer"
                   },
                   "title": "Entity-Officers",
                   "type": "array"
                },
                "entity-suitability": {
                   "$ref": "#/$defs/EntitySuitability"
                },
                "entity-type": {
                   "title": "Entity-Type",
                   "type": "string"
                },
                "foreign-institution": {
                   "title": "Foreign-Institution",
                   "type": "string"
                },
                "grantor-birth-date": {
                   "title": "Grantor-Birth-Date",
                   "type": "string"
                },
                "grantor-email": {
                   "title": "Grantor-Email",
                   "type": "string"
                },
                "grantor-first-name": {
                   "title": "Grantor-First-Name",
                   "type": "string"
                },
                "grantor-last-name": {
                   "title": "Grantor-Last-Name",
                   "type": "string"
                },
                "grantor-middle-name": {
                   "title": "Grantor-Middle-Name",
                   "type": "string"
                },
                "grantor-tax-number": {
                   "title": "Grantor-Tax-Number",
                   "type": "string"
                },
                "has-foreign-bank-affiliation": {
                   "title": "Has-Foreign-Bank-Affiliation",
                   "type": "string"
                },
                "has-foreign-institution-affiliation": {
                   "title": "Has-Foreign-Institution-Affiliation",
                   "type": "string"
                },
                "is-domestic": {
                   "title": "Is-Domestic",
                   "type": "boolean"
                },
                "legal-name": {
                   "title": "Legal-Name",
                   "type": "string"
                },
                "phone-number": {
                   "title": "Phone-Number",
                   "type": "string"
                },
                "tax-number": {
                   "title": "Tax-Number",
                   "type": "string"
                }
             },
             "required": [
                "id",
                "address",
                "business-nature",
                "email",
                "entity-officers",
                "entity-suitability",
                "entity-type",
                "foreign-institution",
                "grantor-birth-date",
                "grantor-email",
                "grantor-first-name",
                "grantor-last-name",
                "grantor-middle-name",
                "grantor-tax-number",
                "has-foreign-bank-affiliation",
                "has-foreign-institution-affiliation",
                "is-domestic",
                "legal-name",
                "phone-number",
                "tax-number"
             ],
             "title": "CustomerEntity",
             "type": "object"
          },
          "CustomerPerson": {
             "description": "Dataclass containing customer person information.",
             "properties": {
                "external-id": {
                   "title": "External-Id",
                   "type": "string"
                },
                "first-name": {
                   "title": "First-Name",
                   "type": "string"
                },
                "last-name": {
                   "title": "Last-Name",
                   "type": "string"
                },
                "citizenship-country": {
                   "title": "Citizenship-Country",
                   "type": "string"
                },
                "usa-citizenship-type": {
                   "title": "Usa-Citizenship-Type",
                   "type": "string"
                },
                "employment-status": {
                   "title": "Employment-Status",
                   "type": "string"
                },
                "marital-status": {
                   "title": "Marital-Status",
                   "type": "string"
                },
                "number-of-dependents": {
                   "title": "Number-Of-Dependents",
                   "type": "integer"
                },
                "occupation": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Occupation"
                },
                "middle-name": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Middle-Name"
                },
                "prefix-name": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Prefix-Name"
                },
                "suffix-name": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Suffix-Name"
                },
                "birth-country": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Birth-Country"
                },
                "birth-date": {
                   "anyOf": [
                      {
                         "format": "date",
                         "type": "string"
                      },
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Birth-Date"
                },
                "visa-expiration-date": {
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
                   "title": "Visa-Expiration-Date"
                },
                "visa-type": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Visa-Type"
                },
                "employer-name": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Employer-Name"
                },
                "job-title": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Job-Title"
                }
             },
             "required": [
                "external-id",
                "first-name",
                "last-name",
                "citizenship-country",
                "usa-citizenship-type",
                "employment-status",
                "marital-status",
                "number-of-dependents"
             ],
             "title": "CustomerPerson",
             "type": "object"
          },
          "CustomerSuitability": {
             "description": "Dataclass containing customer suitability information.",
             "properties": {
                "id": {
                   "title": "Id",
                   "type": "integer"
                },
                "annual-net-income": {
                   "title": "Annual-Net-Income",
                   "type": "integer"
                },
                "covered-options-trading-experience": {
                   "title": "Covered-Options-Trading-Experience",
                   "type": "string"
                },
                "employment-status": {
                   "title": "Employment-Status",
                   "type": "string"
                },
                "futures-trading-experience": {
                   "title": "Futures-Trading-Experience",
                   "type": "string"
                },
                "liquid-net-worth": {
                   "title": "Liquid-Net-Worth",
                   "type": "integer"
                },
                "marital-status": {
                   "title": "Marital-Status",
                   "type": "string"
                },
                "net-worth": {
                   "title": "Net-Worth",
                   "type": "integer"
                },
                "number-of-dependents": {
                   "title": "Number-Of-Dependents",
                   "type": "integer"
                },
                "stock-trading-experience": {
                   "title": "Stock-Trading-Experience",
                   "type": "string"
                },
                "uncovered-options-trading-experience": {
                   "title": "Uncovered-Options-Trading-Experience",
                   "type": "string"
                },
                "customer-id": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Customer-Id"
                },
                "employer-name": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Employer-Name"
                },
                "job-title": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Job-Title"
                },
                "occupation": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Occupation"
                },
                "tax-bracket": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Tax-Bracket"
                }
             },
             "required": [
                "id",
                "annual-net-income",
                "covered-options-trading-experience",
                "employment-status",
                "futures-trading-experience",
                "liquid-net-worth",
                "marital-status",
                "net-worth",
                "number-of-dependents",
                "stock-trading-experience",
                "uncovered-options-trading-experience"
             ],
             "title": "CustomerSuitability",
             "type": "object"
          },
          "EntityOfficer": {
             "description": "Dataclass containing entity officer information.",
             "properties": {
                "id": {
                   "title": "Id",
                   "type": "string"
                },
                "external-id": {
                   "title": "External-Id",
                   "type": "string"
                },
                "first-name": {
                   "title": "First-Name",
                   "type": "string"
                },
                "last-name": {
                   "title": "Last-Name",
                   "type": "string"
                },
                "middle-name": {
                   "title": "Middle-Name",
                   "type": "string"
                },
                "prefix-name": {
                   "title": "Prefix-Name",
                   "type": "string"
                },
                "suffix-name": {
                   "title": "Suffix-Name",
                   "type": "string"
                },
                "address": {
                   "$ref": "#/$defs/Address"
                },
                "birth-country": {
                   "title": "Birth-Country",
                   "type": "string"
                },
                "birth-date": {
                   "format": "date",
                   "title": "Birth-Date",
                   "type": "string"
                },
                "citizenship-country": {
                   "title": "Citizenship-Country",
                   "type": "string"
                },
                "email": {
                   "title": "Email",
                   "type": "string"
                },
                "employer-name": {
                   "title": "Employer-Name",
                   "type": "string"
                },
                "employment-status": {
                   "title": "Employment-Status",
                   "type": "string"
                },
                "home-phone-number": {
                   "title": "Home-Phone-Number",
                   "type": "string"
                },
                "is-foreign": {
                   "title": "Is-Foreign",
                   "type": "boolean"
                },
                "job-title": {
                   "title": "Job-Title",
                   "type": "string"
                },
                "marital-status": {
                   "title": "Marital-Status",
                   "type": "string"
                },
                "mobile-phone-number": {
                   "title": "Mobile-Phone-Number",
                   "type": "string"
                },
                "number-of-dependents": {
                   "title": "Number-Of-Dependents",
                   "type": "integer"
                },
                "occupation": {
                   "title": "Occupation",
                   "type": "string"
                },
                "owner-of-record": {
                   "title": "Owner-Of-Record",
                   "type": "boolean"
                },
                "relationship-to-entity": {
                   "title": "Relationship-To-Entity",
                   "type": "string"
                },
                "tax-number": {
                   "title": "Tax-Number",
                   "type": "string"
                },
                "tax-number-type": {
                   "title": "Tax-Number-Type",
                   "type": "string"
                },
                "usa-citizenship-type": {
                   "title": "Usa-Citizenship-Type",
                   "type": "string"
                },
                "visa-expiration-date": {
                   "format": "date",
                   "title": "Visa-Expiration-Date",
                   "type": "string"
                },
                "visa-type": {
                   "title": "Visa-Type",
                   "type": "string"
                },
                "work-phone-number": {
                   "title": "Work-Phone-Number",
                   "type": "string"
                }
             },
             "required": [
                "id",
                "external-id",
                "first-name",
                "last-name",
                "middle-name",
                "prefix-name",
                "suffix-name",
                "address",
                "birth-country",
                "birth-date",
                "citizenship-country",
                "email",
                "employer-name",
                "employment-status",
                "home-phone-number",
                "is-foreign",
                "job-title",
                "marital-status",
                "mobile-phone-number",
                "number-of-dependents",
                "occupation",
                "owner-of-record",
                "relationship-to-entity",
                "tax-number",
                "tax-number-type",
                "usa-citizenship-type",
                "visa-expiration-date",
                "visa-type",
                "work-phone-number"
             ],
             "title": "EntityOfficer",
             "type": "object"
          },
          "EntitySuitability": {
             "description": "Dataclass containing entity suitability information.",
             "properties": {
                "id": {
                   "title": "Id",
                   "type": "string"
                },
                "annual-net-income": {
                   "title": "Annual-Net-Income",
                   "type": "integer"
                },
                "covered-options-trading-experience": {
                   "title": "Covered-Options-Trading-Experience",
                   "type": "string"
                },
                "entity-id": {
                   "title": "Entity-Id",
                   "type": "integer"
                },
                "futures-trading-experience": {
                   "title": "Futures-Trading-Experience",
                   "type": "string"
                },
                "liquid-net-worth": {
                   "title": "Liquid-Net-Worth",
                   "type": "integer"
                },
                "net-worth": {
                   "title": "Net-Worth",
                   "type": "integer"
                },
                "stock-trading-experience": {
                   "title": "Stock-Trading-Experience",
                   "type": "string"
                },
                "tax-bracket": {
                   "title": "Tax-Bracket",
                   "type": "string"
                },
                "uncovered-options-trading-experience": {
                   "title": "Uncovered-Options-Trading-Experience",
                   "type": "string"
                }
             },
             "required": [
                "id",
                "annual-net-income",
                "covered-options-trading-experience",
                "entity-id",
                "futures-trading-experience",
                "liquid-net-worth",
                "net-worth",
                "stock-trading-experience",
                "tax-bracket",
                "uncovered-options-trading-experience"
             ],
             "title": "EntitySuitability",
             "type": "object"
          }
       },
       "required": [
          "id",
          "first-name",
          "first-surname",
          "last-name",
          "address",
          "customer-suitability",
          "mailing-address",
          "is-foreign",
          "regulatory-domain",
          "usa-citizenship-type",
          "home-phone-number",
          "mobile-phone-number",
          "work-phone-number",
          "birth-date",
          "email",
          "external-id",
          "tax-number",
          "tax-number-type",
          "citizenship-country",
          "agreed-to-margining",
          "subject-to-tax-withholding",
          "agreed-to-terms",
          "ext-crm-id",
          "has-industry-affiliation",
          "has-listed-affiliation",
          "has-political-affiliation",
          "has-delayed-quotes",
          "has-pending-or-approved-application",
          "is-professional",
          "permitted-account-types",
          "created-at",
          "identifiable-type",
          "person"
       ]
    }

    ```

    Fields:[¶](session.html#tastytrade.session.Customer-fields "Permalink to this headline")
    :   * [`address (tastytrade.session.Address)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.address (Python parameter)")
        * [`agreed_to_margining (bool)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.agreed_to_margining (Python parameter)")
        * [`agreed_to_terms (bool)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.agreed_to_terms (Python parameter)")
        * [`birth_country (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.birth_country (Python parameter)")
        * [`birth_date (datetime.date)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.birth_date (Python parameter)")
        * [`citizenship_country (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.citizenship_country (Python parameter)")
        * [`created_at (datetime.datetime)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.created_at (Python parameter)")
        * [`customer_suitability (tastytrade.session.CustomerSuitability)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.customer_suitability (Python parameter)")
        * [`desk_customer_id (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.desk_customer_id (Python parameter)")
        * [`email (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.email (Python parameter)")
        * [`entity (tastytrade.session.CustomerEntity | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.entity (Python parameter)")
        * [`ext_crm_id (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.ext_crm_id (Python parameter)")
        * [`external_id (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.external_id (Python parameter)")
        * [`family_member_names (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.family_member_names (Python parameter)")
        * [`first_name (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.first_name (Python parameter)")
        * [`first_surname (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.first_surname (Python parameter)")
        * [`foreign_tax_number (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.foreign_tax_number (Python parameter)")
        * [`gender (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.gender (Python parameter)")
        * [`has_delayed_quotes (bool)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.has_delayed_quotes (Python parameter)")
        * [`has_industry_affiliation (bool)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.has_industry_affiliation (Python parameter)")
        * [`has_institutional_assets (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.has_institutional_assets (Python parameter)")
        * [`has_listed_affiliation (bool)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.has_listed_affiliation (Python parameter)")
        * [`has_pending_or_approved_application (bool)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.has_pending_or_approved_application (Python parameter)")
        * [`has_political_affiliation (bool)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.has_political_affiliation (Python parameter)")
        * [`home_phone_number (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.home_phone_number (Python parameter)")
        * [`id (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.id (Python parameter)")
        * [`identifiable_type (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.identifiable_type (Python parameter)")
        * [`industry_affiliation_firm (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.industry_affiliation_firm (Python parameter)")
        * [`is_foreign (bool)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.is_foreign (Python parameter)")
        * [`is_investment_adviser (bool | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.is_investment_adviser (Python parameter)")
        * [`is_professional (bool)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.is_professional (Python parameter)")
        * [`last_name (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.last_name (Python parameter)")
        * [`listed_affiliation_symbol (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.listed_affiliation_symbol (Python parameter)")
        * [`mailing_address (tastytrade.session.Address)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.mailing_address (Python parameter)")
        * [`middle_name (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.middle_name (Python parameter)")
        * [`mobile_phone_number (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.mobile_phone_number (Python parameter)")
        * [`permitted_account_types (list[tastytrade.session.CustomerAccountType])`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.permitted_account_types (Python parameter)")
        * [`person (tastytrade.session.CustomerPerson)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.person (Python parameter)")
        * [`political_organization (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.political_organization (Python parameter)")
        * [`prefix_name (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.prefix_name (Python parameter)")
        * [`regulatory_domain (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.regulatory_domain (Python parameter)")
        * [`second_surname (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.second_surname (Python parameter)")
        * [`signature_of_agreement (bool | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.signature_of_agreement (Python parameter)")
        * [`subject_to_tax_withholding (bool)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.subject_to_tax_withholding (Python parameter)")
        * [`suffix_name (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.suffix_name (Python parameter)")
        * [`tax_number (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.tax_number (Python parameter)")
        * [`tax_number_type (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.tax_number_type (Python parameter)")
        * [`usa_citizenship_type (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.usa_citizenship_type (Python parameter)")
        * [`user_id (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.user_id (Python parameter)")
        * [`visa_expiration_date (datetime.date | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.visa_expiration_date (Python parameter)")
        * [`visa_type (str | None)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.visa_type (Python parameter)")
        * [`work_phone_number (str)`](session.html#tastytrade.session.Customer "tastytrade.session.Customer.work_phone_number (Python parameter)")

*pydantic model* tastytrade.session.CustomerAccountMarginType(*\**, *[name](session.html#tastytrade.session.CustomerAccountMarginType "tastytrade.session.CustomerAccountMarginType.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[is\_margin](session.html#tastytrade.session.CustomerAccountMarginType "tastytrade.session.CustomerAccountMarginType.is_margin (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*)[¶](session.html#tastytrade.session.CustomerAccountMarginType "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing margin information for a customer account type.

    Show JSON schema

    ```
    {
       "title": "CustomerAccountMarginType",
       "description": "Dataclass containing margin information for a customer account type.",
       "type": "object",
       "properties": {
          "name": {
             "title": "Name",
             "type": "string"
          },
          "is-margin": {
             "title": "Is-Margin",
             "type": "boolean"
          }
       },
       "required": [
          "name",
          "is-margin"
       ]
    }

    ```

    Fields:[¶](session.html#tastytrade.session.CustomerAccountMarginType-fields "Permalink to this headline")
    :   * [`is_margin (bool)`](session.html#tastytrade.session.CustomerAccountMarginType "tastytrade.session.CustomerAccountMarginType.is_margin (Python parameter)")
        * [`name (str)`](session.html#tastytrade.session.CustomerAccountMarginType "tastytrade.session.CustomerAccountMarginType.name (Python parameter)")

*pydantic model* tastytrade.session.CustomerAccountType(*\**, *[name](session.html#tastytrade.session.CustomerAccountType "tastytrade.session.CustomerAccountType.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[description](session.html#tastytrade.session.CustomerAccountType "tastytrade.session.CustomerAccountType.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[is\_tax\_advantaged](session.html#tastytrade.session.CustomerAccountType "tastytrade.session.CustomerAccountType.is_tax_advantaged (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[is\_publicly\_available](session.html#tastytrade.session.CustomerAccountType "tastytrade.session.CustomerAccountType.is_publicly_available (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[has\_multiple\_owners](session.html#tastytrade.session.CustomerAccountType "tastytrade.session.CustomerAccountType.has_multiple_owners (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[margin\_types](session.html#tastytrade.session.CustomerAccountType "tastytrade.session.CustomerAccountType.margin_types (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[CustomerAccountMarginType](session.html#tastytrade.session.CustomerAccountMarginType "tastytrade.session.CustomerAccountMarginType (Python model) — Bases: TastytradeData")]*)[¶](session.html#tastytrade.session.CustomerAccountType "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information for a type of customer account.

    Show JSON schema

    ```
    {
       "title": "CustomerAccountType",
       "description": "Dataclass containing information for a type of customer account.",
       "type": "object",
       "properties": {
          "name": {
             "title": "Name",
             "type": "string"
          },
          "description": {
             "title": "Description",
             "type": "string"
          },
          "is-tax-advantaged": {
             "title": "Is-Tax-Advantaged",
             "type": "boolean"
          },
          "is-publicly-available": {
             "title": "Is-Publicly-Available",
             "type": "boolean"
          },
          "has-multiple-owners": {
             "title": "Has-Multiple-Owners",
             "type": "boolean"
          },
          "margin-types": {
             "items": {
                "$ref": "#/$defs/CustomerAccountMarginType"
             },
             "title": "Margin-Types",
             "type": "array"
          }
       },
       "$defs": {
          "CustomerAccountMarginType": {
             "description": "Dataclass containing margin information for a customer account type.",
             "properties": {
                "name": {
                   "title": "Name",
                   "type": "string"
                },
                "is-margin": {
                   "title": "Is-Margin",
                   "type": "boolean"
                }
             },
             "required": [
                "name",
                "is-margin"
             ],
             "title": "CustomerAccountMarginType",
             "type": "object"
          }
       },
       "required": [
          "name",
          "description",
          "is-tax-advantaged",
          "is-publicly-available",
          "has-multiple-owners",
          "margin-types"
       ]
    }

    ```

    Fields:[¶](session.html#tastytrade.session.CustomerAccountType-fields "Permalink to this headline")
    :   * [`description (str)`](session.html#tastytrade.session.CustomerAccountType "tastytrade.session.CustomerAccountType.description (Python parameter)")
        * [`has_multiple_owners (bool)`](session.html#tastytrade.session.CustomerAccountType "tastytrade.session.CustomerAccountType.has_multiple_owners (Python parameter)")
        * [`is_publicly_available (bool)`](session.html#tastytrade.session.CustomerAccountType "tastytrade.session.CustomerAccountType.is_publicly_available (Python parameter)")
        * [`is_tax_advantaged (bool)`](session.html#tastytrade.session.CustomerAccountType "tastytrade.session.CustomerAccountType.is_tax_advantaged (Python parameter)")
        * [`margin_types (list[tastytrade.session.CustomerAccountMarginType])`](session.html#tastytrade.session.CustomerAccountType "tastytrade.session.CustomerAccountType.margin_types (Python parameter)")
        * [`name (str)`](session.html#tastytrade.session.CustomerAccountType "tastytrade.session.CustomerAccountType.name (Python parameter)")

*pydantic model* tastytrade.session.CustomerEntity(*\**, *[id](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[address](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.address (Python parameter)"): [Address](session.html#tastytrade.session.Address "tastytrade.session.Address (Python model) — Bases: TastytradeData")*, *[business\_nature](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.business_nature (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[email](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.email (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[entity\_officers](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.entity_officers (Python parameter)"): [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)")[[EntityOfficer](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer (Python model) — Bases: TastytradeData")]*, *[entity\_suitability](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.entity_suitability (Python parameter)"): [EntitySuitability](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability (Python model) — Bases: TastytradeData")*, *[entity\_type](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.entity_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[foreign\_institution](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.foreign_institution (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[grantor\_birth\_date](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.grantor_birth_date (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[grantor\_email](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.grantor_email (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[grantor\_first\_name](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.grantor_first_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[grantor\_last\_name](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.grantor_last_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[grantor\_middle\_name](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.grantor_middle_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[grantor\_tax\_number](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.grantor_tax_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[has\_foreign\_bank\_affiliation](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.has_foreign_bank_affiliation (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[has\_foreign\_institution\_affiliation](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.has_foreign_institution_affiliation (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[is\_domestic](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.is_domestic (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[legal\_name](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.legal_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[phone\_number](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.phone_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[tax\_number](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.tax_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)[¶](session.html#tastytrade.session.CustomerEntity "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing customer entity information.

    Show JSON schema

    ```
    {
       "title": "CustomerEntity",
       "description": "Dataclass containing customer entity information.",
       "type": "object",
       "properties": {
          "id": {
             "title": "Id",
             "type": "string"
          },
          "address": {
             "$ref": "#/$defs/Address"
          },
          "business-nature": {
             "title": "Business-Nature",
             "type": "string"
          },
          "email": {
             "title": "Email",
             "type": "string"
          },
          "entity-officers": {
             "items": {
                "$ref": "#/$defs/EntityOfficer"
             },
             "title": "Entity-Officers",
             "type": "array"
          },
          "entity-suitability": {
             "$ref": "#/$defs/EntitySuitability"
          },
          "entity-type": {
             "title": "Entity-Type",
             "type": "string"
          },
          "foreign-institution": {
             "title": "Foreign-Institution",
             "type": "string"
          },
          "grantor-birth-date": {
             "title": "Grantor-Birth-Date",
             "type": "string"
          },
          "grantor-email": {
             "title": "Grantor-Email",
             "type": "string"
          },
          "grantor-first-name": {
             "title": "Grantor-First-Name",
             "type": "string"
          },
          "grantor-last-name": {
             "title": "Grantor-Last-Name",
             "type": "string"
          },
          "grantor-middle-name": {
             "title": "Grantor-Middle-Name",
             "type": "string"
          },
          "grantor-tax-number": {
             "title": "Grantor-Tax-Number",
             "type": "string"
          },
          "has-foreign-bank-affiliation": {
             "title": "Has-Foreign-Bank-Affiliation",
             "type": "string"
          },
          "has-foreign-institution-affiliation": {
             "title": "Has-Foreign-Institution-Affiliation",
             "type": "string"
          },
          "is-domestic": {
             "title": "Is-Domestic",
             "type": "boolean"
          },
          "legal-name": {
             "title": "Legal-Name",
             "type": "string"
          },
          "phone-number": {
             "title": "Phone-Number",
             "type": "string"
          },
          "tax-number": {
             "title": "Tax-Number",
             "type": "string"
          }
       },
       "$defs": {
          "Address": {
             "description": "Dataclass containing customer address information.",
             "properties": {
                "city": {
                   "title": "City",
                   "type": "string"
                },
                "country": {
                   "title": "Country",
                   "type": "string"
                },
                "is-domestic": {
                   "title": "Is-Domestic",
                   "type": "boolean"
                },
                "is-foreign": {
                   "title": "Is-Foreign",
                   "type": "boolean"
                },
                "postal-code": {
                   "title": "Postal-Code",
                   "type": "string"
                },
                "state-region": {
                   "title": "State-Region",
                   "type": "string"
                },
                "street-one": {
                   "title": "Street-One",
                   "type": "string"
                },
                "street-two": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Street-Two"
                },
                "street-three": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Street-Three"
                }
             },
             "required": [
                "city",
                "country",
                "is-domestic",
                "is-foreign",
                "postal-code",
                "state-region",
                "street-one"
             ],
             "title": "Address",
             "type": "object"
          },
          "EntityOfficer": {
             "description": "Dataclass containing entity officer information.",
             "properties": {
                "id": {
                   "title": "Id",
                   "type": "string"
                },
                "external-id": {
                   "title": "External-Id",
                   "type": "string"
                },
                "first-name": {
                   "title": "First-Name",
                   "type": "string"
                },
                "last-name": {
                   "title": "Last-Name",
                   "type": "string"
                },
                "middle-name": {
                   "title": "Middle-Name",
                   "type": "string"
                },
                "prefix-name": {
                   "title": "Prefix-Name",
                   "type": "string"
                },
                "suffix-name": {
                   "title": "Suffix-Name",
                   "type": "string"
                },
                "address": {
                   "$ref": "#/$defs/Address"
                },
                "birth-country": {
                   "title": "Birth-Country",
                   "type": "string"
                },
                "birth-date": {
                   "format": "date",
                   "title": "Birth-Date",
                   "type": "string"
                },
                "citizenship-country": {
                   "title": "Citizenship-Country",
                   "type": "string"
                },
                "email": {
                   "title": "Email",
                   "type": "string"
                },
                "employer-name": {
                   "title": "Employer-Name",
                   "type": "string"
                },
                "employment-status": {
                   "title": "Employment-Status",
                   "type": "string"
                },
                "home-phone-number": {
                   "title": "Home-Phone-Number",
                   "type": "string"
                },
                "is-foreign": {
                   "title": "Is-Foreign",
                   "type": "boolean"
                },
                "job-title": {
                   "title": "Job-Title",
                   "type": "string"
                },
                "marital-status": {
                   "title": "Marital-Status",
                   "type": "string"
                },
                "mobile-phone-number": {
                   "title": "Mobile-Phone-Number",
                   "type": "string"
                },
                "number-of-dependents": {
                   "title": "Number-Of-Dependents",
                   "type": "integer"
                },
                "occupation": {
                   "title": "Occupation",
                   "type": "string"
                },
                "owner-of-record": {
                   "title": "Owner-Of-Record",
                   "type": "boolean"
                },
                "relationship-to-entity": {
                   "title": "Relationship-To-Entity",
                   "type": "string"
                },
                "tax-number": {
                   "title": "Tax-Number",
                   "type": "string"
                },
                "tax-number-type": {
                   "title": "Tax-Number-Type",
                   "type": "string"
                },
                "usa-citizenship-type": {
                   "title": "Usa-Citizenship-Type",
                   "type": "string"
                },
                "visa-expiration-date": {
                   "format": "date",
                   "title": "Visa-Expiration-Date",
                   "type": "string"
                },
                "visa-type": {
                   "title": "Visa-Type",
                   "type": "string"
                },
                "work-phone-number": {
                   "title": "Work-Phone-Number",
                   "type": "string"
                }
             },
             "required": [
                "id",
                "external-id",
                "first-name",
                "last-name",
                "middle-name",
                "prefix-name",
                "suffix-name",
                "address",
                "birth-country",
                "birth-date",
                "citizenship-country",
                "email",
                "employer-name",
                "employment-status",
                "home-phone-number",
                "is-foreign",
                "job-title",
                "marital-status",
                "mobile-phone-number",
                "number-of-dependents",
                "occupation",
                "owner-of-record",
                "relationship-to-entity",
                "tax-number",
                "tax-number-type",
                "usa-citizenship-type",
                "visa-expiration-date",
                "visa-type",
                "work-phone-number"
             ],
             "title": "EntityOfficer",
             "type": "object"
          },
          "EntitySuitability": {
             "description": "Dataclass containing entity suitability information.",
             "properties": {
                "id": {
                   "title": "Id",
                   "type": "string"
                },
                "annual-net-income": {
                   "title": "Annual-Net-Income",
                   "type": "integer"
                },
                "covered-options-trading-experience": {
                   "title": "Covered-Options-Trading-Experience",
                   "type": "string"
                },
                "entity-id": {
                   "title": "Entity-Id",
                   "type": "integer"
                },
                "futures-trading-experience": {
                   "title": "Futures-Trading-Experience",
                   "type": "string"
                },
                "liquid-net-worth": {
                   "title": "Liquid-Net-Worth",
                   "type": "integer"
                },
                "net-worth": {
                   "title": "Net-Worth",
                   "type": "integer"
                },
                "stock-trading-experience": {
                   "title": "Stock-Trading-Experience",
                   "type": "string"
                },
                "tax-bracket": {
                   "title": "Tax-Bracket",
                   "type": "string"
                },
                "uncovered-options-trading-experience": {
                   "title": "Uncovered-Options-Trading-Experience",
                   "type": "string"
                }
             },
             "required": [
                "id",
                "annual-net-income",
                "covered-options-trading-experience",
                "entity-id",
                "futures-trading-experience",
                "liquid-net-worth",
                "net-worth",
                "stock-trading-experience",
                "tax-bracket",
                "uncovered-options-trading-experience"
             ],
             "title": "EntitySuitability",
             "type": "object"
          }
       },
       "required": [
          "id",
          "address",
          "business-nature",
          "email",
          "entity-officers",
          "entity-suitability",
          "entity-type",
          "foreign-institution",
          "grantor-birth-date",
          "grantor-email",
          "grantor-first-name",
          "grantor-last-name",
          "grantor-middle-name",
          "grantor-tax-number",
          "has-foreign-bank-affiliation",
          "has-foreign-institution-affiliation",
          "is-domestic",
          "legal-name",
          "phone-number",
          "tax-number"
       ]
    }

    ```

    Fields:[¶](session.html#tastytrade.session.CustomerEntity-fields "Permalink to this headline")
    :   * [`address (tastytrade.session.Address)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.address (Python parameter)")
        * [`business_nature (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.business_nature (Python parameter)")
        * [`email (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.email (Python parameter)")
        * [`entity_officers (list[tastytrade.session.EntityOfficer])`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.entity_officers (Python parameter)")
        * [`entity_suitability (tastytrade.session.EntitySuitability)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.entity_suitability (Python parameter)")
        * [`entity_type (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.entity_type (Python parameter)")
        * [`foreign_institution (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.foreign_institution (Python parameter)")
        * [`grantor_birth_date (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.grantor_birth_date (Python parameter)")
        * [`grantor_email (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.grantor_email (Python parameter)")
        * [`grantor_first_name (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.grantor_first_name (Python parameter)")
        * [`grantor_last_name (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.grantor_last_name (Python parameter)")
        * [`grantor_middle_name (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.grantor_middle_name (Python parameter)")
        * [`grantor_tax_number (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.grantor_tax_number (Python parameter)")
        * [`has_foreign_bank_affiliation (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.has_foreign_bank_affiliation (Python parameter)")
        * [`has_foreign_institution_affiliation (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.has_foreign_institution_affiliation (Python parameter)")
        * [`id (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.id (Python parameter)")
        * [`is_domestic (bool)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.is_domestic (Python parameter)")
        * [`legal_name (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.legal_name (Python parameter)")
        * [`phone_number (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.phone_number (Python parameter)")
        * [`tax_number (str)`](session.html#tastytrade.session.CustomerEntity "tastytrade.session.CustomerEntity.tax_number (Python parameter)")

*pydantic model* tastytrade.session.CustomerPerson(*\**, *[external\_id](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.external_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[first\_name](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.first_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[last\_name](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.last_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[citizenship\_country](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.citizenship_country (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[usa\_citizenship\_type](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.usa_citizenship_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[employment\_status](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.employment_status (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[marital\_status](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.marital_status (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[number\_of\_dependents](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.number_of_dependents (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[occupation](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.occupation (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[middle\_name](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.middle_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[prefix\_name](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.prefix_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[suffix\_name](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.suffix_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[birth\_country](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.birth_country (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[birth\_date](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.birth_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[visa\_expiration\_date](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.visa_expiration_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[visa\_type](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.visa_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[employer\_name](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.employer_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[job\_title](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.job_title (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](session.html#tastytrade.session.CustomerPerson "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing customer person information.

    Show JSON schema

    ```
    {
       "title": "CustomerPerson",
       "description": "Dataclass containing customer person information.",
       "type": "object",
       "properties": {
          "external-id": {
             "title": "External-Id",
             "type": "string"
          },
          "first-name": {
             "title": "First-Name",
             "type": "string"
          },
          "last-name": {
             "title": "Last-Name",
             "type": "string"
          },
          "citizenship-country": {
             "title": "Citizenship-Country",
             "type": "string"
          },
          "usa-citizenship-type": {
             "title": "Usa-Citizenship-Type",
             "type": "string"
          },
          "employment-status": {
             "title": "Employment-Status",
             "type": "string"
          },
          "marital-status": {
             "title": "Marital-Status",
             "type": "string"
          },
          "number-of-dependents": {
             "title": "Number-Of-Dependents",
             "type": "integer"
          },
          "occupation": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Occupation"
          },
          "middle-name": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Middle-Name"
          },
          "prefix-name": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Prefix-Name"
          },
          "suffix-name": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Suffix-Name"
          },
          "birth-country": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Birth-Country"
          },
          "birth-date": {
             "anyOf": [
                {
                   "format": "date",
                   "type": "string"
                },
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Birth-Date"
          },
          "visa-expiration-date": {
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
             "title": "Visa-Expiration-Date"
          },
          "visa-type": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Visa-Type"
          },
          "employer-name": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Employer-Name"
          },
          "job-title": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Job-Title"
          }
       },
       "required": [
          "external-id",
          "first-name",
          "last-name",
          "citizenship-country",
          "usa-citizenship-type",
          "employment-status",
          "marital-status",
          "number-of-dependents"
       ]
    }

    ```

    Fields:[¶](session.html#tastytrade.session.CustomerPerson-fields "Permalink to this headline")
    :   * [`birth_country (str | None)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.birth_country (Python parameter)")
        * [`birth_date (datetime.date | str | None)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.birth_date (Python parameter)")
        * [`citizenship_country (str)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.citizenship_country (Python parameter)")
        * [`employer_name (str | None)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.employer_name (Python parameter)")
        * [`employment_status (str)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.employment_status (Python parameter)")
        * [`external_id (str)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.external_id (Python parameter)")
        * [`first_name (str)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.first_name (Python parameter)")
        * [`job_title (str | None)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.job_title (Python parameter)")
        * [`last_name (str)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.last_name (Python parameter)")
        * [`marital_status (str)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.marital_status (Python parameter)")
        * [`middle_name (str | None)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.middle_name (Python parameter)")
        * [`number_of_dependents (int)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.number_of_dependents (Python parameter)")
        * [`occupation (str | None)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.occupation (Python parameter)")
        * [`prefix_name (str | None)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.prefix_name (Python parameter)")
        * [`suffix_name (str | None)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.suffix_name (Python parameter)")
        * [`usa_citizenship_type (str)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.usa_citizenship_type (Python parameter)")
        * [`visa_expiration_date (datetime.date | None)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.visa_expiration_date (Python parameter)")
        * [`visa_type (str | None)`](session.html#tastytrade.session.CustomerPerson "tastytrade.session.CustomerPerson.visa_type (Python parameter)")

*pydantic model* tastytrade.session.CustomerSuitability(*\**, *[id](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.id (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[annual\_net\_income](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.annual_net_income (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[covered\_options\_trading\_experience](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.covered_options_trading_experience (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[employment\_status](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.employment_status (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[futures\_trading\_experience](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.futures_trading_experience (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[liquid\_net\_worth](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.liquid_net_worth (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[marital\_status](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.marital_status (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[net\_worth](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.net_worth (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[number\_of\_dependents](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.number_of_dependents (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[stock\_trading\_experience](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.stock_trading_experience (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[uncovered\_options\_trading\_experience](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.uncovered_options_trading_experience (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[customer\_id](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.customer_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[employer\_name](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.employer_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[job\_title](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.job_title (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[occupation](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.occupation (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[tax\_bracket](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.tax_bracket (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](session.html#tastytrade.session.CustomerSuitability "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing customer suitability information.

    Show JSON schema

    ```
    {
       "title": "CustomerSuitability",
       "description": "Dataclass containing customer suitability information.",
       "type": "object",
       "properties": {
          "id": {
             "title": "Id",
             "type": "integer"
          },
          "annual-net-income": {
             "title": "Annual-Net-Income",
             "type": "integer"
          },
          "covered-options-trading-experience": {
             "title": "Covered-Options-Trading-Experience",
             "type": "string"
          },
          "employment-status": {
             "title": "Employment-Status",
             "type": "string"
          },
          "futures-trading-experience": {
             "title": "Futures-Trading-Experience",
             "type": "string"
          },
          "liquid-net-worth": {
             "title": "Liquid-Net-Worth",
             "type": "integer"
          },
          "marital-status": {
             "title": "Marital-Status",
             "type": "string"
          },
          "net-worth": {
             "title": "Net-Worth",
             "type": "integer"
          },
          "number-of-dependents": {
             "title": "Number-Of-Dependents",
             "type": "integer"
          },
          "stock-trading-experience": {
             "title": "Stock-Trading-Experience",
             "type": "string"
          },
          "uncovered-options-trading-experience": {
             "title": "Uncovered-Options-Trading-Experience",
             "type": "string"
          },
          "customer-id": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Customer-Id"
          },
          "employer-name": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Employer-Name"
          },
          "job-title": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Job-Title"
          },
          "occupation": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Occupation"
          },
          "tax-bracket": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Tax-Bracket"
          }
       },
       "required": [
          "id",
          "annual-net-income",
          "covered-options-trading-experience",
          "employment-status",
          "futures-trading-experience",
          "liquid-net-worth",
          "marital-status",
          "net-worth",
          "number-of-dependents",
          "stock-trading-experience",
          "uncovered-options-trading-experience"
       ]
    }

    ```

    Fields:[¶](session.html#tastytrade.session.CustomerSuitability-fields "Permalink to this headline")
    :   * [`annual_net_income (int)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.annual_net_income (Python parameter)")
        * [`covered_options_trading_experience (str)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.covered_options_trading_experience (Python parameter)")
        * [`customer_id (str | None)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.customer_id (Python parameter)")
        * [`employer_name (str | None)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.employer_name (Python parameter)")
        * [`employment_status (str)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.employment_status (Python parameter)")
        * [`futures_trading_experience (str)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.futures_trading_experience (Python parameter)")
        * [`id (int)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.id (Python parameter)")
        * [`job_title (str | None)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.job_title (Python parameter)")
        * [`liquid_net_worth (int)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.liquid_net_worth (Python parameter)")
        * [`marital_status (str)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.marital_status (Python parameter)")
        * [`net_worth (int)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.net_worth (Python parameter)")
        * [`number_of_dependents (int)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.number_of_dependents (Python parameter)")
        * [`occupation (str | None)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.occupation (Python parameter)")
        * [`stock_trading_experience (str)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.stock_trading_experience (Python parameter)")
        * [`tax_bracket (str | None)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.tax_bracket (Python parameter)")
        * [`uncovered_options_trading_experience (str)`](session.html#tastytrade.session.CustomerSuitability "tastytrade.session.CustomerSuitability.uncovered_options_trading_experience (Python parameter)")

*pydantic model* tastytrade.session.EntityOfficer(*\**, *[id](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[external\_id](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.external_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[first\_name](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.first_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[last\_name](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.last_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[middle\_name](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.middle_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[prefix\_name](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.prefix_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[suffix\_name](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.suffix_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[address](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.address (Python parameter)"): [Address](session.html#tastytrade.session.Address "tastytrade.session.Address (Python model) — Bases: TastytradeData")*, *[birth\_country](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.birth_country (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[birth\_date](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.birth_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*, *[citizenship\_country](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.citizenship_country (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[email](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.email (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[employer\_name](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.employer_name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[employment\_status](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.employment_status (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[home\_phone\_number](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.home_phone_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[is\_foreign](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.is_foreign (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[job\_title](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.job_title (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[marital\_status](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.marital_status (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[mobile\_phone\_number](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.mobile_phone_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[number\_of\_dependents](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.number_of_dependents (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[occupation](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.occupation (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[owner\_of\_record](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.owner_of_record (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[relationship\_to\_entity](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.relationship_to_entity (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[tax\_number](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.tax_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[tax\_number\_type](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.tax_number_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[usa\_citizenship\_type](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.usa_citizenship_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[visa\_expiration\_date](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.visa_expiration_date (Python parameter)"): [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)")*, *[visa\_type](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.visa_type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[work\_phone\_number](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.work_phone_number (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)[¶](session.html#tastytrade.session.EntityOfficer "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing entity officer information.

    Show JSON schema

    ```
    {
       "title": "EntityOfficer",
       "description": "Dataclass containing entity officer information.",
       "type": "object",
       "properties": {
          "id": {
             "title": "Id",
             "type": "string"
          },
          "external-id": {
             "title": "External-Id",
             "type": "string"
          },
          "first-name": {
             "title": "First-Name",
             "type": "string"
          },
          "last-name": {
             "title": "Last-Name",
             "type": "string"
          },
          "middle-name": {
             "title": "Middle-Name",
             "type": "string"
          },
          "prefix-name": {
             "title": "Prefix-Name",
             "type": "string"
          },
          "suffix-name": {
             "title": "Suffix-Name",
             "type": "string"
          },
          "address": {
             "$ref": "#/$defs/Address"
          },
          "birth-country": {
             "title": "Birth-Country",
             "type": "string"
          },
          "birth-date": {
             "format": "date",
             "title": "Birth-Date",
             "type": "string"
          },
          "citizenship-country": {
             "title": "Citizenship-Country",
             "type": "string"
          },
          "email": {
             "title": "Email",
             "type": "string"
          },
          "employer-name": {
             "title": "Employer-Name",
             "type": "string"
          },
          "employment-status": {
             "title": "Employment-Status",
             "type": "string"
          },
          "home-phone-number": {
             "title": "Home-Phone-Number",
             "type": "string"
          },
          "is-foreign": {
             "title": "Is-Foreign",
             "type": "boolean"
          },
          "job-title": {
             "title": "Job-Title",
             "type": "string"
          },
          "marital-status": {
             "title": "Marital-Status",
             "type": "string"
          },
          "mobile-phone-number": {
             "title": "Mobile-Phone-Number",
             "type": "string"
          },
          "number-of-dependents": {
             "title": "Number-Of-Dependents",
             "type": "integer"
          },
          "occupation": {
             "title": "Occupation",
             "type": "string"
          },
          "owner-of-record": {
             "title": "Owner-Of-Record",
             "type": "boolean"
          },
          "relationship-to-entity": {
             "title": "Relationship-To-Entity",
             "type": "string"
          },
          "tax-number": {
             "title": "Tax-Number",
             "type": "string"
          },
          "tax-number-type": {
             "title": "Tax-Number-Type",
             "type": "string"
          },
          "usa-citizenship-type": {
             "title": "Usa-Citizenship-Type",
             "type": "string"
          },
          "visa-expiration-date": {
             "format": "date",
             "title": "Visa-Expiration-Date",
             "type": "string"
          },
          "visa-type": {
             "title": "Visa-Type",
             "type": "string"
          },
          "work-phone-number": {
             "title": "Work-Phone-Number",
             "type": "string"
          }
       },
       "$defs": {
          "Address": {
             "description": "Dataclass containing customer address information.",
             "properties": {
                "city": {
                   "title": "City",
                   "type": "string"
                },
                "country": {
                   "title": "Country",
                   "type": "string"
                },
                "is-domestic": {
                   "title": "Is-Domestic",
                   "type": "boolean"
                },
                "is-foreign": {
                   "title": "Is-Foreign",
                   "type": "boolean"
                },
                "postal-code": {
                   "title": "Postal-Code",
                   "type": "string"
                },
                "state-region": {
                   "title": "State-Region",
                   "type": "string"
                },
                "street-one": {
                   "title": "Street-One",
                   "type": "string"
                },
                "street-two": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Street-Two"
                },
                "street-three": {
                   "anyOf": [
                      {
                         "type": "string"
                      },
                      {
                         "type": "null"
                      }
                   ],
                   "default": null,
                   "title": "Street-Three"
                }
             },
             "required": [
                "city",
                "country",
                "is-domestic",
                "is-foreign",
                "postal-code",
                "state-region",
                "street-one"
             ],
             "title": "Address",
             "type": "object"
          }
       },
       "required": [
          "id",
          "external-id",
          "first-name",
          "last-name",
          "middle-name",
          "prefix-name",
          "suffix-name",
          "address",
          "birth-country",
          "birth-date",
          "citizenship-country",
          "email",
          "employer-name",
          "employment-status",
          "home-phone-number",
          "is-foreign",
          "job-title",
          "marital-status",
          "mobile-phone-number",
          "number-of-dependents",
          "occupation",
          "owner-of-record",
          "relationship-to-entity",
          "tax-number",
          "tax-number-type",
          "usa-citizenship-type",
          "visa-expiration-date",
          "visa-type",
          "work-phone-number"
       ]
    }

    ```

    Fields:[¶](session.html#tastytrade.session.EntityOfficer-fields "Permalink to this headline")
    :   * [`address (tastytrade.session.Address)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.address (Python parameter)")
        * [`birth_country (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.birth_country (Python parameter)")
        * [`birth_date (datetime.date)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.birth_date (Python parameter)")
        * [`citizenship_country (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.citizenship_country (Python parameter)")
        * [`email (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.email (Python parameter)")
        * [`employer_name (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.employer_name (Python parameter)")
        * [`employment_status (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.employment_status (Python parameter)")
        * [`external_id (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.external_id (Python parameter)")
        * [`first_name (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.first_name (Python parameter)")
        * [`home_phone_number (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.home_phone_number (Python parameter)")
        * [`id (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.id (Python parameter)")
        * [`is_foreign (bool)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.is_foreign (Python parameter)")
        * [`job_title (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.job_title (Python parameter)")
        * [`last_name (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.last_name (Python parameter)")
        * [`marital_status (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.marital_status (Python parameter)")
        * [`middle_name (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.middle_name (Python parameter)")
        * [`mobile_phone_number (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.mobile_phone_number (Python parameter)")
        * [`number_of_dependents (int)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.number_of_dependents (Python parameter)")
        * [`occupation (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.occupation (Python parameter)")
        * [`owner_of_record (bool)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.owner_of_record (Python parameter)")
        * [`prefix_name (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.prefix_name (Python parameter)")
        * [`relationship_to_entity (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.relationship_to_entity (Python parameter)")
        * [`suffix_name (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.suffix_name (Python parameter)")
        * [`tax_number (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.tax_number (Python parameter)")
        * [`tax_number_type (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.tax_number_type (Python parameter)")
        * [`usa_citizenship_type (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.usa_citizenship_type (Python parameter)")
        * [`visa_expiration_date (datetime.date)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.visa_expiration_date (Python parameter)")
        * [`visa_type (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.visa_type (Python parameter)")
        * [`work_phone_number (str)`](session.html#tastytrade.session.EntityOfficer "tastytrade.session.EntityOfficer.work_phone_number (Python parameter)")

*pydantic model* tastytrade.session.EntitySuitability(*\**, *[id](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[annual\_net\_income](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.annual_net_income (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[covered\_options\_trading\_experience](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.covered_options_trading_experience (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[entity\_id](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.entity_id (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[futures\_trading\_experience](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.futures_trading_experience (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[liquid\_net\_worth](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.liquid_net_worth (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[net\_worth](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.net_worth (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[stock\_trading\_experience](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.stock_trading_experience (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[tax\_bracket](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.tax_bracket (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[uncovered\_options\_trading\_experience](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.uncovered_options_trading_experience (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)[¶](session.html#tastytrade.session.EntitySuitability "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing entity suitability information.

    Show JSON schema

    ```
    {
       "title": "EntitySuitability",
       "description": "Dataclass containing entity suitability information.",
       "type": "object",
       "properties": {
          "id": {
             "title": "Id",
             "type": "string"
          },
          "annual-net-income": {
             "title": "Annual-Net-Income",
             "type": "integer"
          },
          "covered-options-trading-experience": {
             "title": "Covered-Options-Trading-Experience",
             "type": "string"
          },
          "entity-id": {
             "title": "Entity-Id",
             "type": "integer"
          },
          "futures-trading-experience": {
             "title": "Futures-Trading-Experience",
             "type": "string"
          },
          "liquid-net-worth": {
             "title": "Liquid-Net-Worth",
             "type": "integer"
          },
          "net-worth": {
             "title": "Net-Worth",
             "type": "integer"
          },
          "stock-trading-experience": {
             "title": "Stock-Trading-Experience",
             "type": "string"
          },
          "tax-bracket": {
             "title": "Tax-Bracket",
             "type": "string"
          },
          "uncovered-options-trading-experience": {
             "title": "Uncovered-Options-Trading-Experience",
             "type": "string"
          }
       },
       "required": [
          "id",
          "annual-net-income",
          "covered-options-trading-experience",
          "entity-id",
          "futures-trading-experience",
          "liquid-net-worth",
          "net-worth",
          "stock-trading-experience",
          "tax-bracket",
          "uncovered-options-trading-experience"
       ]
    }

    ```

    Fields:[¶](session.html#tastytrade.session.EntitySuitability-fields "Permalink to this headline")
    :   * [`annual_net_income (int)`](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.annual_net_income (Python parameter)")
        * [`covered_options_trading_experience (str)`](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.covered_options_trading_experience (Python parameter)")
        * [`entity_id (int)`](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.entity_id (Python parameter)")
        * [`futures_trading_experience (str)`](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.futures_trading_experience (Python parameter)")
        * [`id (str)`](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.id (Python parameter)")
        * [`liquid_net_worth (int)`](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.liquid_net_worth (Python parameter)")
        * [`net_worth (int)`](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.net_worth (Python parameter)")
        * [`stock_trading_experience (str)`](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.stock_trading_experience (Python parameter)")
        * [`tax_bracket (str)`](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.tax_bracket (Python parameter)")
        * [`uncovered_options_trading_experience (str)`](session.html#tastytrade.session.EntitySuitability "tastytrade.session.EntitySuitability.uncovered_options_trading_experience (Python parameter)")

*class* tastytrade.session.OAuthSession(*[provider\_secret](session.html#tastytrade.session.OAuthSession.__init__.provider_secret "tastytrade.session.OAuthSession.__init__.provider_secret (Python parameter) — OAuth secret for your provider"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[refresh\_token](session.html#tastytrade.session.OAuthSession.__init__.refresh_token "tastytrade.session.OAuthSession.__init__.refresh_token (Python parameter) — refresh token for the user"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[is\_test](session.html#tastytrade.session.OAuthSession.__init__.is_test "tastytrade.session.OAuthSession.__init__.is_test (Python parameter) — whether to use the test API endpoints, default False"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`*, *[proxy](session.html#tastytrade.session.OAuthSession.__init__.proxy "tastytrade.session.OAuthSession.__init__.proxy (Python parameter) — if provided, all requests will be made through this proxy, as well as web socket connections for streamers."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](session.html#tastytrade.session.OAuthSession "Link to this definition")
:   Bases: [`Session`](session.html#tastytrade.session.Session "tastytrade.session.Session (Python class) — Bases: object")

    Contains a managed user login which can then be used to interact with the
    remote API.

    Note that OAuth sessions can’t be used to create streamers!

    Parameters:[¶](session.html#tastytrade.session.OAuthSession-parameters "Permalink to this headline")
    :   provider\_secret: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](session.html#tastytrade.session.OAuthSession.__init__.provider_secret "Permalink to this definition")
        :   OAuth secret for your provider

        refresh\_token: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](session.html#tastytrade.session.OAuthSession.__init__.refresh_token "Permalink to this definition")
        :   refresh token for the user

        is\_test: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`[¶](session.html#tastytrade.session.OAuthSession.__init__.is_test "Permalink to this definition")
        :   whether to use the test API endpoints, default False

        proxy: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](session.html#tastytrade.session.OAuthSession.__init__.proxy "Permalink to this definition")
        :   if provided, all requests will be made through this proxy, as well as
            web socket connections for streamers.

    *async* a\_refresh() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](session.html#tastytrade.session.OAuthSession.a_refresh "Link to this definition")
    :   Refreshes the acccess token using the stored refresh token.

    async\_client[¶](session.html#tastytrade.session.OAuthSession.async_client "Link to this definition")
    :   httpx client for async requests

    *classmethod* deserialize(*[serialized](session.html#tastytrade.session.OAuthSession.deserialize "tastytrade.session.OAuthSession.deserialize.serialized (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.13)")[¶](session.html#tastytrade.session.OAuthSession.deserialize "Link to this definition")
    :   Create a new Session object from a serialized string.

    expires\_at[¶](session.html#tastytrade.session.OAuthSession.expires_at "Link to this definition")
    :   Unix timestamp for when the session token expires

    is\_test[¶](session.html#tastytrade.session.OAuthSession.is_test "Link to this definition")
    :   Whether this is a cert or real session

    provider\_secret[¶](session.html#tastytrade.session.OAuthSession.provider_secret "Link to this definition")
    :   OAuth secret for your provider

    proxy[¶](session.html#tastytrade.session.OAuthSession.proxy "Link to this definition")
    :   Proxy URL to use for requests and web sockets

    refresh() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](session.html#tastytrade.session.OAuthSession.refresh "Link to this definition")
    :   Refreshes the acccess token using the stored refresh token.

    refresh\_token[¶](session.html#tastytrade.session.OAuthSession.refresh_token "Link to this definition")
    :   Refresh token for the user

    serialize() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](session.html#tastytrade.session.OAuthSession.serialize "Link to this definition")
    :   Serializes the session to a string, useful for storing
        a session for later use.
        Could be used with pickle, Redis, etc.

    sync\_client[¶](session.html#tastytrade.session.OAuthSession.sync_client "Link to this definition")
    :   httpx client for sync requests

*class* tastytrade.session.Session(*[login](session.html#tastytrade.session.Session.__init__.login "tastytrade.session.Session.__init__.login (Python parameter) — Tastytrade username or email"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[password](session.html#tastytrade.session.Session.__init__.password "tastytrade.session.Session.__init__.password (Python parameter) — tastytrade password to login; if absent, remember token is required"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[remember\_me](session.html#tastytrade.session.Session.__init__.remember_me "tastytrade.session.Session.__init__.remember_me (Python parameter) — whether or not to create a remember token to use instead of a password"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`*, *[remember\_token](session.html#tastytrade.session.Session.__init__.remember_token "tastytrade.session.Session.__init__.remember_token (Python parameter) — previously generated token; if absent, password is required"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[is\_test](session.html#tastytrade.session.Session.__init__.is_test "tastytrade.session.Session.__init__.is_test (Python parameter) — whether to use the test API endpoints, default False"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`*, *[two\_factor\_authentication](session.html#tastytrade.session.Session.__init__.two_factor_authentication "tastytrade.session.Session.__init__.two_factor_authentication (Python parameter) — if two factor authentication is enabled, this is the code sent to the user's device"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[dxfeed\_tos\_compliant](session.html#tastytrade.session.Session.__init__.dxfeed_tos_compliant "tastytrade.session.Session.__init__.dxfeed_tos_compliant (Python parameter) — whether to use the dxfeed TOS-compliant API endpoint for the streamer"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`*, *[proxy](session.html#tastytrade.session.Session.__init__.proxy "tastytrade.session.Session.__init__.proxy (Python parameter) — if provided, all requests will be made through this proxy, as well as web socket connections for streamers."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](session.html#tastytrade.session.Session "Link to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    Contains a local user login which can then be used to interact with the
    remote API.

    Parameters:[¶](session.html#tastytrade.session.Session-parameters "Permalink to this headline")
    :   login: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](session.html#tastytrade.session.Session.__init__.login "Permalink to this definition")
        :   Tastytrade username or email

        remember\_me: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`[¶](session.html#tastytrade.session.Session.__init__.remember_me "Permalink to this definition")
        :   whether or not to create a remember token to use instead of a password

        password: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](session.html#tastytrade.session.Session.__init__.password "Permalink to this definition")
        :   tastytrade password to login; if absent, remember token is required

        remember\_token: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](session.html#tastytrade.session.Session.__init__.remember_token "Permalink to this definition")
        :   previously generated token; if absent, password is required

        is\_test: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`[¶](session.html#tastytrade.session.Session.__init__.is_test "Permalink to this definition")
        :   whether to use the test API endpoints, default False

        two\_factor\_authentication: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](session.html#tastytrade.session.Session.__init__.two_factor_authentication "Permalink to this definition")
        :   if two factor authentication is enabled, this is the code sent to the
            user’s device

        dxfeed\_tos\_compliant: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `False`[¶](session.html#tastytrade.session.Session.__init__.dxfeed_tos_compliant "Permalink to this definition")
        :   whether to use the dxfeed TOS-compliant API endpoint for the streamer

        proxy: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`[¶](session.html#tastytrade.session.Session.__init__.proxy "Permalink to this definition")
        :   if provided, all requests will be made through this proxy, as well as
            web socket connections for streamers.

    *async* a\_destroy() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](session.html#tastytrade.session.Session.a_destroy "Link to this definition")
    :   Sends a API request to log out of the existing session. This will
        invalidate the current session token and login.

    *async* a\_get\_2fa\_info() → [TwoFactorInfo](session.html#tastytrade.session.TwoFactorInfo "tastytrade.session.TwoFactorInfo (Python model) — Bases: TastytradeData")[¶](session.html#tastytrade.session.Session.a_get_2fa_info "Link to this definition")
    :   Gets the 2FA info for the current user.

    *async* a\_get\_customer() → [Customer](session.html#tastytrade.session.Customer "tastytrade.session.Customer (Python model) — Bases: TastytradeData")[¶](session.html#tastytrade.session.Session.a_get_customer "Link to this definition")
    :   Gets the customer dict from the API.

        Returns:[¶](session.html#tastytrade.session.Session.a_get_customer-returns "Permalink to this headline")
        :   a Tastytrade ‘Customer’ object in JSON format.

    *async* a\_validate() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[¶](session.html#tastytrade.session.Session.a_validate "Link to this definition")
    :   Validates the current session by sending a request to the API.

        Returns:[¶](session.html#tastytrade.session.Session.a_validate-returns "Permalink to this headline")
        :   True if the session is valid and False otherwise.

    async\_client[¶](session.html#tastytrade.session.Session.async_client "Link to this definition")
    :   httpx client for async requests

    *classmethod* deserialize(*[serialized](session.html#tastytrade.session.Session.deserialize "tastytrade.session.Session.deserialize.serialized (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.13)")[¶](session.html#tastytrade.session.Session.deserialize "Link to this definition")
    :   Create a new Session object from a serialized string.

    destroy() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[¶](session.html#tastytrade.session.Session.destroy "Link to this definition")
    :   Sends a API request to log out of the existing session. This will
        invalidate the current session token and login.

    dxlink\_url[¶](session.html#tastytrade.session.Session.dxlink_url "Link to this definition")
    :   URL for dxfeed websocket

    get\_2fa\_info() → [TwoFactorInfo](session.html#tastytrade.session.TwoFactorInfo "tastytrade.session.TwoFactorInfo (Python model) — Bases: TastytradeData")[¶](session.html#tastytrade.session.Session.get_2fa_info "Link to this definition")
    :   Gets the 2FA info for the current user.

    get\_customer() → [Customer](session.html#tastytrade.session.Customer "tastytrade.session.Customer (Python model) — Bases: TastytradeData")[¶](session.html#tastytrade.session.Session.get_customer "Link to this definition")
    :   Gets the customer dict from the API.

        Returns:[¶](session.html#tastytrade.session.Session.get_customer-returns "Permalink to this headline")
        :   a Tastytrade ‘Customer’ object in JSON format.

    is\_test[¶](session.html#tastytrade.session.Session.is_test "Link to this definition")
    :   Whether this is a cert or real session

    proxy[¶](session.html#tastytrade.session.Session.proxy "Link to this definition")
    :   Proxy URL to use for requests and web sockets

    remember\_token[¶](session.html#tastytrade.session.Session.remember_token "Link to this definition")
    :   A single-use token which can be used to login without a password

    serialize() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](session.html#tastytrade.session.Session.serialize "Link to this definition")
    :   Serializes the session to a string, useful for storing
        a session for later use.
        Could be used with pickle, Redis, etc.

    session\_expiration[¶](session.html#tastytrade.session.Session.session_expiration "Link to this definition")
    :   expiration for session token

    session\_token[¶](session.html#tastytrade.session.Session.session_token "Link to this definition")
    :   The session token used to authenticate requests

    streamer\_token[¶](session.html#tastytrade.session.Session.streamer_token "Link to this definition")
    :   Auth token for dxfeed websocket

    sync\_client[¶](session.html#tastytrade.session.Session.sync_client "Link to this definition")
    :   httpx client for sync requests

    user[¶](session.html#tastytrade.session.Session.user "Link to this definition")
    :   The user dict returned by the API; contains basic user information

    validate() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[¶](session.html#tastytrade.session.Session.validate "Link to this definition")
    :   Validates the current session by sending a request to the API.

        Returns:[¶](session.html#tastytrade.session.Session.validate-returns "Permalink to this headline")
        :   True if the session is valid and False otherwise.

*pydantic model* tastytrade.session.TwoFactorInfo(*\**, *[is\_active](session.html#tastytrade.session.TwoFactorInfo "tastytrade.session.TwoFactorInfo.is_active (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[type](session.html#tastytrade.session.TwoFactorInfo "tastytrade.session.TwoFactorInfo.type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](session.html#tastytrade.session.TwoFactorInfo "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about two-factor authentication.

    Show JSON schema

    ```
    {
       "title": "TwoFactorInfo",
       "description": "Dataclass containing information about two-factor authentication.",
       "type": "object",
       "properties": {
          "is-active": {
             "title": "Is-Active",
             "type": "boolean"
          },
          "type": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Type"
          }
       },
       "required": [
          "is-active"
       ]
    }

    ```

    Fields:[¶](session.html#tastytrade.session.TwoFactorInfo-fields "Permalink to this headline")
    :   * [`is_active (bool)`](session.html#tastytrade.session.TwoFactorInfo "tastytrade.session.TwoFactorInfo.is_active (Python parameter)")
        * [`type (str | None)`](session.html#tastytrade.session.TwoFactorInfo "tastytrade.session.TwoFactorInfo.type (Python parameter)")

*pydantic model* tastytrade.session.User(*\**, *[email](session.html#tastytrade.session.User "tastytrade.session.User.email (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[external\_id](session.html#tastytrade.session.User "tastytrade.session.User.external_id (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[is\_confirmed](session.html#tastytrade.session.User "tastytrade.session.User.is_confirmed (Python parameter)"): [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*, *[username](session.html#tastytrade.session.User "tastytrade.session.User.username (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[name](session.html#tastytrade.session.User "tastytrade.session.User.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[nickname](session.html#tastytrade.session.User "tastytrade.session.User.nickname (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[¶](session.html#tastytrade.session.User "Link to this definition")
:   Bases: [`TastytradeData`](utils.html#tastytrade.utils.TastytradeData "tastytrade.utils.TastytradeData (Python model) — A pydantic dataclass that converts keys from snake case to dasherized and performs type validation and coercion.")

    Dataclass containing information about a Tastytrade user.

    Show JSON schema

    ```
    {
       "title": "User",
       "description": "Dataclass containing information about a Tastytrade user.",
       "type": "object",
       "properties": {
          "email": {
             "title": "Email",
             "type": "string"
          },
          "external-id": {
             "title": "External-Id",
             "type": "string"
          },
          "is-confirmed": {
             "title": "Is-Confirmed",
             "type": "boolean"
          },
          "username": {
             "title": "Username",
             "type": "string"
          },
          "name": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Name"
          },
          "nickname": {
             "anyOf": [
                {
                   "type": "string"
                },
                {
                   "type": "null"
                }
             ],
             "default": null,
             "title": "Nickname"
          }
       },
       "required": [
          "email",
          "external-id",
          "is-confirmed",
          "username"
       ]
    }

    ```

    Fields:[¶](session.html#tastytrade.session.User-fields "Permalink to this headline")
    :   * [`email (str)`](session.html#tastytrade.session.User "tastytrade.session.User.email (Python parameter)")
        * [`external_id (str)`](session.html#tastytrade.session.User "tastytrade.session.User.external_id (Python parameter)")
        * [`is_confirmed (bool)`](session.html#tastytrade.session.User "tastytrade.session.User.is_confirmed (Python parameter)")
        * [`name (str | None)`](session.html#tastytrade.session.User "tastytrade.session.User.name (Python parameter)")
        * [`nickname (str | None)`](session.html#tastytrade.session.User "tastytrade.session.User.nickname (Python parameter)")
        * [`username (str)`](session.html#tastytrade.session.User "tastytrade.session.User.username (Python parameter)")

[Back to top](session.html#)


[Previous
tastytrade.search](search.html)
[Next
tastytrade.streamer](streamer.html)

© Copyright 2025, tastyware.

Created using
[Sphinx](https://www.sphinx-doc.org/)
7.4.7.
and
[Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)