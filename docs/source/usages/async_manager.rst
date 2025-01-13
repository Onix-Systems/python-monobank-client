AsyncMonoManager
================

The `AsyncMonoManager` class provides a simple and efficient way to interact asynchronously with Mono APIs.

The `AsyncMonoManager` class provides a simple and efficient way to interact asynchronously with Mono APIs.
Designed for modern Python applications, it allows developers to fetch currency rates, retrieve client information,
check balances, download statements, and create payments, all in a non-blocking manner.

Methods

get_currencies
--------------

This method retrieves the exchange rates for different currencies. Supports fetching rates for both cash and non-cash operations.

**Usage:**

.. code-block:: python

    import asyncio

    async def main():
        manager = AsyncMonoManager(token="your_token_here")

        # Get cash currency rates
        cash_rates = await manager.get_currencies(type='cash')
        print("Cash rates:", cash_rates)

        # Get non-cash currency rates
        non_cash_rates = await manager.get_currencies(type='non-cash')
        print("Non-cash rates:", non_cash_rates)

    asyncio.run(main())

**Expected result:**

.. code-block:: json

    {
        "USD": {"buy": 38.50, "sell": 38.90},
        "EUR": {"buy": 40.10, "sell": 40.50}
    }

get_client_info
---------------

This method retrieves account details of the client.

**Usage:**

.. code-block:: python

    async def main():
        manager = AsyncMonoManager(token="your_token_here")
        client_info = await manager.get_client_info()
        print("Client Info:", client_info)

    asyncio.run(main())

**Expected result:**

.. code-block:: json

    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+380XXXXXXXXX"
    }

get_balance
-----------

This method fetches the current balances of all linked accounts.

**Usage:**

.. code-block:: python

    async def main():
        manager = AsyncMonoManager(token="your_token_here")
        balance = await manager.get_balance()
        print("Account Balance:", balance)

    asyncio.run(main())

**Expected result:**

.. code-block:: json

    [
        {"account": "UA1234567890", "currency": "UAH", "balance": 5000.75},
        {"account": "UA0987654321", "currency": "USD", "balance": 200.00}
    ]

get_statement
-------------

This method retrieves transaction statements for a specific account over a given time period or limit.

**Usage:**

.. code-block:: python

    async def main():
        manager = AsyncMonoManager(token="your_token_here")
        statement = await manager.get_statement(account="UA1234567890", period="7d", limit=10)
        print("Statements:", statement)

    asyncio.run(main())

**Expected result:**

.. code-block:: json

    [
        {"date": "2023-10-10", "amount": -100.50, "description": "Payment to XYZ"},
        {"date": "2023-10-09", "amount": 500.00, "description": "Salary Deposit"}
    ]

create_webhook
--------------

This method allows for creating a webhook that will receive events from the Mono APIs.

**Usage:**

.. code-block:: python

    async def main():
        manager = AsyncMonoManager(token="your_token_here")
        webhook_url = "https://your-domain.com/webhook-endpoint"

        result = await manager.create_webhook(webhook=webhook_url)
        print("Webhook Creation Result:", result)

    asyncio.run(main())

**Expected result:**

.. code-block:: json

    {
        "status": "success",
        "webhook": "https://your-domain.com/webhook-endpoint"
    }

Method Details
--------------

1. **get_currencies**:

   - **Purpose**: Fetches currency exchange rates.
   - **Parameters**:
      - `type` (str): Type of rate, either `'cash'` or `'non-cash'`. Default is `'non-cash'`.

2. **get_client_info**:

   - **Purpose**: Retrieves the information details of the client.

3. **get_balance**:
   - **Purpose**: Gets the current balance for the client's accounts.

4. **get_statement**:

   - **Purpose**: Retrieves transaction statements.

   - **Parameters**:

   - `account` (str): The account ID to fetch data for.
   - `period` (str): Time period for the statements (e.g., `'7d'` for last 7 days).
   - `limit` (int): Maximum number of transactions to retrieve.

5. **create_webhook**:

   - **Purpose**: Creates a webhook to receive events from the Mono APIs.
   - **Parameters**:    - `webhook` (str): The URL of the webhook endpoint.

.. tip:: Learn More. To learn more about deposits functionality, refer to: :mod:`monobank_api_client.fastapi_mono.router`