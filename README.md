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
```

Get client info
```python
>>> mng.get_client_info()
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
```

Get balance
```python
>>> mng.get_balance()
{
  "balance": x.xx
}
```

Get statement
```python
>>> period = 31
>>> mng.get_statement(period)
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
```

Create a Webhook
```python
>>> mng.create_webhook('https://myserver.com/hookpath')
```
