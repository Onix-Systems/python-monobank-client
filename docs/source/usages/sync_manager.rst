SyncMonoManager Methods
=========================

The ``SyncMonoManager`` provides synchronous methods to interact with MonoBank APIs using an authentication token, including:

- Performing HTTP requests
- Retrieving exchange rates, client information, account balances, transaction statements
- Creating payments

session
-------
**Description:** Creates and returns a session object for making HTTP requests.
This method uses the token provided during the SyncMonoManager instantiation.

.. code-block:: python

   session = SyncMonoManager(token="your_token").session()

**Response:** Returns a ``requests.sessions.Session`` instance.


sync_request
------------
**Description:** Performs an HTTP request using the specified method, URI, headers, and data.
Automatically includes the token if not present in the headers.

.. code-block:: python

   method = "POST"
   uri = "https://api.someurl.com/resource"
   headers = {"Authorization": "Bearer your_token"}
   data = {"key": "value"}

   response = SyncMonoManager(token="your_token").sync_request(method, uri, headers, data)
   print(response)

**Response:** A dictionary containing the server response. For example:

.. code-block:: json

   {
       "code": 200,
       "detail": {
           "key": "value"
       }
   }


get_currencies
--------------
**Description:** Retrieves exchange rates from PrivatBank APIs, utilizing the token provided during SyncMonoManager instantiation.

**Parameters:**
- ``cashe_rate`` (bool): Whether to fetch cash exchange rates.

.. code-block:: python

   cashe_rate = True
   currencies = SyncMonoManager(token="your_token").get_currencies(cashe_rate)
   print(currencies)

**Response:** A dictionary with exchange rate information. Example:

.. code-block:: json

   {
       "code": 200,
       "detail": [
           {
               "currency": "USD",
               "rate": 27.5
           },
           {
               "currency": "EUR",
               "rate": 30.5
           }
       ]
   }

get_client_info
---------------
**Description:** Retrieves client account information such as balances and transactions, using the provided token.

.. code-block:: python

   client_info = SyncMonoManager(token="your_token").get_client_info()
   print(client_info)

**Response:** A dictionary with client information. Example:

.. code-block:: json

   {
       "code": 200,
       "detail": {
           "name": "John Doe",
           "balances": [
               {
                   "account": "123456789",
                   "balanceOutEq": 1000.0
               }
           ]
       }
   }


get_balance
-----------
**Description:** Retrieves the account balance, respecting the provided token.

.. code-block:: python

   balance = SyncMonoManager(token="your_token").get_balance()
   print(balance)

**Response:** A dictionary containing the balance. Example:

.. code-block:: json

   {
       "code": 200,
       "detail": {
           "balance": 1000.0
       }
   }


get_statement
-------------
**Description:** Retrieves the account statement for a specific period and transaction limit, using the token supplied during SyncMonoManager creation.

**Parameters:**
- ``period`` (int): Number of days prior to fetch transactions.
- ``limit`` (int): Maximum number of transactions to retrieve.

.. code-block:: python

   statement = SyncMonoManager(token="your_token").get_statement(period=7, limit=10)
   print(statement)

**Response:** A dictionary containing transaction details. Example:

.. code-block:: json

   {
       "code": 200,
       "detail": [
           {
               "transactionId": "54321",
               "amount": -50.0,
               "date": "2023-10-01"
           },
           {
               "transactionId": "98765",
               "amount": 100.0,
               "date": "2023-09-30"
           }
       ]
   }


create_webhook
--------------

This method allows for creating a webhook that will receive events from the Mono APIs.

**Usage:**

.. code-block:: python

   manager = SyncMonoManager(token="your_token")
   webhook_url = "https://your-domain.com/webhook-endpoint"
   result = manager.create_webhook(webhook=webhook_url)
   print("Webhook Creation Result:", result)

**Expected result:**

.. code-block:: json

    {
        "status": "success",
        "webhook": "https://your-domain.com/webhook-endpoint"
    }

.. tip:: Learn More. To learn more about deposits functionality, refer to: :mod:`mono_api_client.sync_mono.manager`