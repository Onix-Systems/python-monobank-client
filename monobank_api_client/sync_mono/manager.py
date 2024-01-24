import requests
from typing import Dict
from mono_config.manager import BaseMonoManager


class SyncMonoManager(BaseMonoManager):
    @classmethod
    def session(cls) -> requests.sessions.Session:
        return requests.Session()

    def sync_request(
        self,
        method: str,
        uri: str,
        headers=None,
        data=None,
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
            response = self.sync_request(method="GET", uri=uri)
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
            else:
                list_ccy = [key for key in self.mono_currencies.keys()]
                response = self.currency_exception(list_ccy)
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def get_client_info(self) -> Dict:
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
        try:
            client_info = self.get_client_info()
            code = client_info.get("code")
            data = client_info.get("detail")
            balance = {"balance": data["accounts"][0]["balance"] / 100}
            response = {"code": code, "detail": balance}
            return response
        except Exception:
            return client_info

    def get_statement(self, period: int) -> Dict:
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
