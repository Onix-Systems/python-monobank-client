import aiohttp
from typing import Dict
from monobank_api_client.mono_config.manager import BaseMonoManager


class AsyncMonoManager(BaseMonoManager):
    """
    An asynchronous manager class for interacting with Mono API.

    This class provides various asynchronous methods for performing operations
    like retrieving currencies, client information, balance, statements, and
    setting up webhooks.
    """

    @classmethod
    async def session(cls) -> aiohttp.client.ClientSession:
        """
        Creates an asynchronous ClientSession instance.

        :returns: ClientSession instance for making HTTP requests.
        :rtype: aiohttp.client.ClientSession
        """
        return aiohttp.ClientSession()

    async def async_request(
            self,
            method: str,
            uri: str,
            headers=None,
            data=None,
    ) -> Dict:
        """
        Makes an asynchronous HTTP request using the provided method, URI, headers, and data.

        :param method: The HTTP method ("GET", "POST", etc.) to use in the request.
        :type method: str
        :param uri: The target URI for the HTTP request.
        :type uri: str
        :param headers: Optional headers to include in the request.
        :type headers: dict or None
        :param data: Optional data to include in the request.
        :type data: dict or None
        :returns: Response payload including status code and details.
        :rtype: dict
        :raises aiohttp.ClientResponseError: Raised if the HTTP request fails with an HTTP error.
        :raises Exception: Raised if another error occurs during the request.
        """
        session = await self.session()
        if method == "GET":
            response = await session.get(uri, headers=headers)
        if method == "POST":
            response = await session.post(uri, headers=headers, data=data)
        try:
            code = response.status
            response.raise_for_status()
            detail = await response.json()
            payload = self.mono_response(code, detail)
            return payload
        except aiohttp.ClientResponseError as exc:
            error_response = self.mono_response(code, str(exc.message))
            return error_response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    async def get_currencies(self) -> Dict:
        """
        Retrieves the latest currency rates from Mono API.

        :returns: A dictionary containing the response payload with currency data.
        :rtype: dict
        :raises Exception: Raised if an error occurs during the request.
        """
        try:
            uri = self.mono_currencies_uri
            response = await self.async_request(method="GET", uri=uri)
            return response
        except Exception as exc:
            exception = {"datail": str(exc)}
            return exception

    async def get_currency(self, ccy: str) -> Dict:
        """
        Retrieves detailed currency exchange information for a given currency code.

        :param ccy: The currency code to retrieve exchange information for.
        :type ccy: str
        :returns: A dictionary containing the response payload with currency details.
        :rtype: dict
        :raises Exception: Raised if an error occurs during the request.
        """
        try:
            pair = self.mono_currencies.get(ccy)
            if pair is not None:
                currencies = await self.get_currencies()
                response = self.currency(ccy, pair, currencies)
            else:
                response = self.currency_exception()
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    async def get_client_info(self) -> Dict:
        """
        Retrieves client information from Mono API.

        :returns: A dictionary containing the client's information.
        :rtype: dict
        :raises Exception: Raised if an error occurs during the request.
        """
        try:
            uri = self.mono_client_info_uri
            token = self.token
            headers = {"X-Token": token}
            response = await self.async_request(method="GET", uri=uri, headers=headers)
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    async def get_balance(self) -> Dict:
        """
        Retrieves the balance details of the client from Mono API.

        :returns: A dictionary containing the client's balance data.
        :rtype: dict
        :raises Exception: Raised if an error occurs while retrieving the balance details.
        """
        try:
            payload = await self.get_client_info()
            code = payload.get("code")
            data = payload.get("detail")
            balance = {"balance": data["accounts"][0]["balance"] / 100}
            response = self.mono_response(code, balance)
            return response
        except Exception:
            return payload

    async def get_statement(self, period: int) -> Dict:
        """
        Retrieves the account statement for a specified period from Mono API.

        :param period: The number of months or the period for which the statement is requested.
        :type period: int
        :returns: A dictionary containing the statement details.
        :rtype: dict
        :raises Exception: Raised if an error occurs during the request.
        """
        try:
            uri = self.mono_statement_uri
            token = self.token
            headers = {"X-Token": token}
            time_delta = self.date(period).get("time_delta")
            response = await self.async_request(
                method="GET", uri=f"{uri}{time_delta}/", headers=headers
            )
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    async def create_webhook(self, webhook: str) -> Dict:
        """
        Creates and registers a webhook for receiving client account updates.

        :param webhook: The webhook URL to be registered.
        :type webhook: str
        :returns: A dictionary containing the webhook creation response.
        :rtype: dict
        :raises Exception: Raised if an error occurs during webhook creation.
        """
        try:
            uri = self.mono_webhook_uri
            token = self.token
            headers = {"X-Token": token}
            response = await self.async_request(
                method="POST",
                uri=uri,
                headers=headers,
                data=webhook,
            )
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception
