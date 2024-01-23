# monobank-api-client
This module provides quick integration of the Monobank API for developing applications based on synchronous and asynchronous frameworks.

## Name
monobank_api_client

## Installation
This framework is published at the PyPI, install it with pip:

  1.This package makes it possible to use module methods in synchronous frameworks:

    pip install monobank-api-client[http]

  2.This package makes it possible to use module methods in asynchronous frameworks:

    pip install monobank-api-client[aio]

  3.This package makes it possible to use ready-made views with a synchronous script based on the Django Rest framework:

    pip install monobank-api-client[drf]

  To get started, add the following packages to INSTALLED_APPS:

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'drf_mono',
    ]

  Include drf_mono urls to your urls.py:

      urlpatterns = [
          ...
          path('mono/', include('drf_mono.urls', namespace='drf_mono')),
      ]
  
  4.This package makes it possible to use ready-made routers with an asynchronous script based on the FastAPI framework:

    pip install monobank-api-client[fastapi]

  5.To install all packages at once:

    pip install monobank-api-client[all]

## Usage

1. Request your token at https://api.monobank.ua/
2. For a synchronous request use that token to initialize client:

    from sync_mono.manager import SyncMonoManager

    token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    mng = SyncMonoManager(token)

3. For an asynchronous request, use this token to initialize the client:

    from async_mono.manager import AsyncMonoManager

    token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    mng = AsyncMonoManager(token)

### Methods

Get currencies
```python
>>> mng.get_currencies()
{
  "code": 200,
  "detail":
    [
      {
        "currencyCodeA": 840,
        "currencyCodeB": 980,
        "date": 1702591273,
        "rateBuy": 36.95,
        "rateSell": 37.4406
      },
      {
        "currencyCodeA": 978,
        "currencyCodeB": 980,
        "date": 1702623973,
        "rateBuy": 40.35,
        "rateSell": 41.1404
      },
      {
        "currencyCodeA": 978,
        "currencyCodeB": 840,
        "date": 1702623973,
        "rateBuy": 1.086,
        "rateSell": 1.1025
      },
      ...
    ]
}
```

Get currency
```python
>>> mng.get_currency('USDUAH')
{
  "code": 200,
  "detail": {
    "USDUAH": {
      "Buy": 37.5,
      "Sale": 37.8702
    }
  }
}
```

Get client info
```python
>>> mng.get_client_info()
{
  "code": 200,
  "detail":
    {
      "clientId": "xxxxxxxxxx",
      "name": "Last name First name",
      "webHookUrl": "",
      "permissions": "psfj",
      "accounts": [
        {
          "id": "xxxxxxxxxxxxxxxxxxx",
          "sendId": "xxxxxxxxxx",
          "currencyCode": 980,
          "cashbackType": "UAH",
          "balance": xxxxx,
          "creditLimit": 0,
          "maskedPan": [
            "xxxxxx******xxxx"
          ],
          "type": "black",
          "iban": "UAxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        }
      ]
    }
}
```

Get balance
```python
>>> mng.get_balance()
{
  "code": 200,
  "detail":
    {
      "balance": x.xx
    }
}
```

Get statement
```python
>>> period = 31
>>> mng.get_statement(period)
{
  "code": 200,
  "detail":
    [
      {
        "id": "xxxxxxxxxxxxxxxxxx",
        "time": xxxxxxxxxx,
        "description": "xxxx xxxxx",
        "mcc": xxxx,
        "originalMcc": xxxx,
        "amount": -xxxxx,
        "operationAmount": -xxxxx,
        "currencyCode": xxx,
        "commissionRate": x,
        "cashbackAmount": xxx,
        "balance": xxxx,
        "hold": false,
        "receiptId": "xxxx-xxxx-xxxx-xxxx"
      },
      ...
    ]
}
```

Create a Webhook
```python
>>> mng.create_webhook('https://myserver.com/hookpath')
```
