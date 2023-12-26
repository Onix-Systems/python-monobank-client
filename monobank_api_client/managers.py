import requests
from typing import Dict
from datetime import datetime

from .config import (
    MONOBANK_CLIENT_INFO_URI,
    MONOBANK_CURRENCY_URI,
    MONOBANK_STATEMENT_URI,
    MONOBANK_WEBHOOK_URI,
    MONOBANK_CURRENCIES,
    MONOBANK_CURRENCY_CODE_A,
    MONOBANK_CURRENCY_CODE_B,
)


class MonoManager:
    def __init__(self, token=None):
        self._token = token

    _mono_currency_uri = MONOBANK_CURRENCY_URI
    _mono_client_info_uri = MONOBANK_CLIENT_INFO_URI
    _mono_statement_uri = MONOBANK_STATEMENT_URI
    _mono_webhook_uri = MONOBANK_WEBHOOK_URI
    _mono_currencies = MONOBANK_CURRENCIES
    _mono_currency_code_a = MONOBANK_CURRENCY_CODE_A
    _mono_currency_code_b = MONOBANK_CURRENCY_CODE_B

    @property
    def token(self) -> str:
        return self._token

    @token.setter
    def token(self, new_token: str):
        self._token = new_token

    @property
    def mono_currency_uri(self) -> str:
        return self._mono_currency_uri

    @mono_currency_uri.setter
    def mono_currency_uri(self, new_uri: str):
        self._mono_currency_uri = new_uri

    @property
    def mono_client_info_uri(self) -> str:
        return self._mono_client_info_uri

    @mono_client_info_uri.setter
    def mono_client_info_uri(self, new_uri: str):
        self._mono_client_info_uri = new_uri

    @property
    def mono_statement_uri(self) -> str:
        return self._mono_statement_uri

    @mono_statement_uri.setter
    def mono_statement_uri(self, new_uri: str):
        self._mono_statement_uri = new_uri

    @property
    def mono_webhook_uri(self) -> str:
        return self._mono_webhook_uri

    @mono_webhook_uri.setter
    def mono_webhook_uri(self, new_uri: str):
        self._mono_webhook_uri = new_uri

    @property
    def mono_currency_code_a(self) -> str:
        return self._mono_currency_code_a

    @mono_currency_code_a.setter
    def mono_currency_code_a(self, new_code: str):
        self._mono_currency_code_a = new_code

    @property
    def mono_currency_code_b(self) -> str:
        return self._mono_currency_code_b

    @mono_currency_code_b.setter
    def mono_currency_code_b(self, new_code: str):
        self._mono_currency_code_b = new_code

    @property
    def mono_currencies(self) -> Dict:
        return self._mono_currencies

    @mono_currencies.setter
    def mono_currencies(self, new_currencies: Dict):
        self._mono_currencies = new_currencies

    @classmethod
    def session(cls) -> requests.sessions.Session:
        return requests.Session()

    @staticmethod
    def __date(period: int) -> Dict:
        _day = 86400  # 1 day (UNIX)
        try:
            delta = int(datetime.now().timestamp()) - (period * _day)
            time_delta = {"time_delta": delta}
            return time_delta
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def get_currencies(self) -> Dict:
        try:
            session = self.session()
            uri = self.mono_currency_uri
            response = session.get(uri)
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

    def get_currency(self, ccy_pair: str) -> Dict:
        try:
            pair = self.mono_currencies.get(ccy_pair)
            currencies = self.get_currencies()
            code = currencies.get("code")
            payload = currencies.get("detail")
            if isinstance(payload, list):
                codeA = self.mono_currency_code_a
                codeB = self.mono_currency_code_b
                for ccy in payload:
                    if ccy.get(codeB) == pair.get(codeB):
                        for key, value in ccy.items():
                            if key == codeA and value == pair.get(codeA):
                                buy = ccy.get("rateBuy")
                                sale = ccy.get("rateSell")
                                if buy is not None and sale is not None:
                                    currency = {ccy_pair: {"Buy": buy, "Sale": sale}}
                                else:
                                    cross = ccy.get("rateCross")
                                    currency = {ccy_pair: {"Cross": cross}}
                                response = {"code": code, "detail": currency}
                                return response
            else:
                response = {"code": code, "detail": payload}
                return response
        except AttributeError:
            error_response = {
                "code": 400,
                "detail": "Incorrect currency pair",
                "list of acceptable currency pairs": self.mono_currencies.keys(),
            }
            return error_response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def get_client_info(self) -> Dict:
        try:
            session = self.session()
            token = self.token
            uri = self.mono_client_info_uri
            headers = {"X-Token": token}
            response = session.get(uri, headers=headers)
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
            session = self.session()
            token = self.token
            uri = self.mono_statement_uri
            headers = {"X-Token": token}
            time_delta = self.__date(period).get("time_delta")
            response = session.get(f"{uri}{time_delta}/", headers=headers)
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

    def create_webhook(self, webhook: str) -> Dict:
        try:
            session = self.session()
            token = self.token
            uri = self.mono_webhook_uri
            headers = {"X-Token": token}
            response = session.post(uri, headers=headers, data=webhook)
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
