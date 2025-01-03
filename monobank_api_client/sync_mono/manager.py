import requests
from typing import Dict
from monobank_api_client.mono_config.manager import BaseMonoManager


class SyncMonoManager(BaseMonoManager):
    """
    SyncMonoManager handles synchronous interactions with Mono's APIs.

    This class provides methods for making HTTP requests to the Mono API,
    fetching currencies, account balance, client information, and more.
    """

    @classmethod
    def session(cls) -> requests.sessions.Session:
        """
        Create and return a new session for API requests.

        :return: A requests session instance.
        :rtype: requests.sessions.Session
        """
        return requests.Session()

    def sync_request(
        self,
        method: str,
        uri: str,
        headers=None,
        data=None,
    ) -> Dict:
        """
        Make a synchronous HTTP request.

        :param method: HTTP method to use, e.g., "GET" or "POST".
        :type method: str
        :param uri: API endpoint to send the request to.
        :type uri: str
        :param headers: Headers to include in the request.
        :type headers: dict or None
        :param data: Data payload for POST requests.
        :type data: dict or None
        :return: Parsed API response or error message.
        :rtype: dict
        """
        session = self.session()
        if method == "GET":
            response = session.get(uri, headers=headers)
        if method == "POST":
            response = session.post(uri, headers=headers, data=data)
        try:
            code = response.status_code
            response.raise_for_status()
            detail = response.json()
            payload = self.mono_response(code, detail)
            return payload
        except requests.exceptions.HTTPError as exc:
            error_response = self.mono_response(code, str(exc))
            return error_response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def get_currencies(self) -> Dict:
        """
        Retrieve the list of supported currencies from Mono API.

        :return: API response containing currency details.
        :rtype: dict
        """
        try:
            uri = self.mono_currencies_uri
            response = self.sync_request(method="GET", uri=uri)
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def get_currency(self, ccy: str) -> Dict:
        """
        Retrieve specific currency details based on the given currency code.

        :param ccy: Currency code, e.g., "USD", "EUR".
        :type ccy: str
        :return: Currency details or error message.
        :rtype: dict
        """
        try:
            pair = self.mono_currencies.get(ccy)
            if pair is not None:
                currencies = self.get_currencies()
                response = self.currency(ccy, pair, currencies)
            else:
                response = self.currency_exception()
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def get_client_info(self) -> Dict:
        """
        Fetch client information using the auth token.

        :return: API response containing client details.
        :rtype: dict
        """
        try:
            token = self.token
            uri = self.mono_client_info_uri
            headers = {"X-Token": token}
            response = self.sync_request(method="GET", uri=uri, headers=headers)
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def get_balance(self) -> Dict:
        """
        Retrieve the account balance from Mono API.

        The balance is calculated by accessing the first account in the client data.

        :return: API response containing the account balance.
        :rtype: dict
        """
        try:
            payload = self.get_client_info()
            code = payload.get("code")
            data = payload.get("detail")
            balance = {"balance": data["accounts"][0]["balance"] / 100}
            response = self.mono_response(code, balance)
            return response
        except Exception:
            return payload

    def get_statement(self, period: int) -> Dict:
        """
        Fetch a statement for a specified time period.

        :param period: Number of days for which the statement is fetched.
        :type period: int
        :return: API response containing the statement data.
        :rtype: dict
        """
        try:
            token = self.token
            uri = self.mono_statement_uri
            headers = {"X-Token": token}
            time_delta = self.date(period).get("time_delta")
            response = self.sync_request(
                method="GET", uri=f"{uri}{time_delta}/", headers=headers
            )
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def create_webhook(self, webhook: str) -> Dict:
        """
        Register a new webhook URL with Mono API.

        :param webhook: The URL to register as the webhook.
        :type webhook: str
        :return: API response confirming registration or an error.
        :rtype: dict
        """
        try:
            token = self.token
            uri = self.mono_webhook_uri
            headers = {"X-Token": token}
            response = self.sync_request(
                method="POST", uri=uri, headers=headers, data=webhook
            )
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception
