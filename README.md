# monobank-api-client
This module is designed for quick interaction with the monobank API

## Name
monobank_api_client

## Installation
This framework is published at the TestPyPI, install it with pip:

    py -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ monobank-api-client

## Usage

1. Request your token at https://api.monobank.ua/
2. Use that token to initialize client:

    from monobank_api_client.managers import MonoManager

    token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    mng = MonoManager(token)

### Methods

Get currencies

```python
>>> mng.get_currency()
[
  200,
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
]
```

Get client info

```python
>>> mng.get_client_info()
[
  200,
  {
    "clientId": "xxxxxxxxxx",
    "name": "Lastname Firstname",
    "webHookUrl": "",
    "permissions": "psfj",
    "accounts": [
      {
        "id": "xxxxxxxxxxxxxxxxxxxxxx",
        "sendId": "xxxxxxxxxx",
        "currencyCode": 980,
        "cashbackType": "UAH",
        "balance": 1341,
        "creditLimit": 0,
        "maskedPan": [
          "xxxxxx******xxxx"
        ],
        "type": "black",
        "iban": "UAxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      }
    ]
  }
]

```

Get statement
```python
>>> period = 31
>>> mng.get_statement(period)
[
  200,
  [
    {
      "id": "xxxxxxxxxxxxxxxxxx",
      "time": 1702464077,
      "description": "Файно Маркет",
      "mcc": 5499,
      "originalMcc": 5499,
      "amount": -46030,
      "operationAmount": -46030,
      "currencyCode": 980,
      "commissionRate": 0,
      "cashbackAmount": 460,
      "balance": 1341,
      "hold": false,
      "receiptId": "xxxx-xxxx-xxxx-xxxx"
    },
  ...
  ]
]
```

Create a Webhook
```python
>>> mng.create_webhook('https://myserver.com/hookpath')
```
