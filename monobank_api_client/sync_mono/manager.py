import requests
from typing import Dict
from mono_config.manager import BaseMonoManager
from mono_config.exceptions import MonoException


class SyncMonoManager(BaseMonoManager, MonoException):
    @classmethod
    def session(cls) -> requests.sessions.Session:
        return requests.Session()

    def sync_request(
        self, uri: str, headers: Dict | None, data: Dict | None, method: str
    ) -> Dict:
        session = self.session()
        if method == "GET":
            response = session.get(uri, headers=headers)
        if method == "POST":
            response = session.post(uri, headers=headers, data=data)
        try:
            code = response.status_code
            response.raise_for_status()
            payload = {"code": code, "detail": response.json()}
            return payload
        except requests.exceptions.HTTPError as exc:
            error_response = {"code": code, "detail": str(exc)}
            return error_response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def get_currencies(self) -> Dict:
        try:
            uri = self.mono_currencies_uri
            response = self.sync_request(uri=uri, headers=None, data=None, method="GET")
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def get_currency(self, ccy_pair: str) -> Dict:
        try:
            pair = self.mono_currencies.get(ccy_pair)
            if pair is not None:
                currencies = self.get_currencies()
                response = self.currency(ccy_pair, pair, currencies)
                return response
            list_ccy = [key for key in self.mono_currencies.keys()]
            error_response = self.currency_error(list_ccy)
            return error_response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def get_client_info(self) -> Dict:
        try:
            token = self.token
            uri = self.mono_client_info_uri
            headers = {"X-Token": token}
            response = self.sync_request(
                uri=uri, headers=headers, data=None, method="GET"
            )
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def get_balance(self) -> Dict:
        try:
            client_info = self.get_client_info()
            code = client_info.get("code")
            data = client_info.get("detail")
            balance = {"balance": data["accounts"][0]["balance"] / 100}
            payload = {"code": code, "detail": balance}
            return payload
        except Exception:
            return client_info

    def get_statement(self, period: int) -> Dict:
        try:
            token = self.token
            uri = self.mono_statement_uri
            headers = {"X-Token": token}
            time_delta = self.date(period).get("time_delta")
            response = self.sync_request(
                uri=f"{uri}{time_delta}/", headers=headers, data=None, method="GET"
            )
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def create_webhook(self, webhook: str) -> Dict:
        try:
            token = self.token
            uri = self.mono_webhook_uri
            headers = {"X-Token": token}
            response = self.sync_request(
                uri=uri, headers=headers, data=webhook, method="POST"
            )
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception
