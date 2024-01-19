from typing import Dict
from datetime import datetime

from .config import (
    MONOBANK_CURRENCIES_URI,
    MONOBANK_CURRENCIES,
    MONOBANK_CURRENCY_CODE_A,
    MONOBANK_CURRENCY_CODE_B,
    MONOBANK_CLIENT_INFO_URI,
    MONOBANK_STATEMENT_URI,
    MONOBANK_WEBHOOK_URI,
)


class BaseMonoManager:
    def __init__(self, token=None):
        self._token = token

    _mono_currencies_uri = MONOBANK_CURRENCIES_URI
    _mono_currencies = MONOBANK_CURRENCIES
    _mono_currency_code_a = MONOBANK_CURRENCY_CODE_A
    _mono_currency_code_b = MONOBANK_CURRENCY_CODE_B
    _mono_client_info_uri = MONOBANK_CLIENT_INFO_URI
    _mono_statement_uri = MONOBANK_STATEMENT_URI
    _mono_webhook_uri = MONOBANK_WEBHOOK_URI

    @property
    def token(self) -> str:
        return self._token

    @token.setter
    def token(self, new_token: str):
        self._token = new_token

    @property
    def mono_currencies_uri(self) -> str:
        return self._mono_currencies_uri

    @mono_currencies_uri.setter
    def mono_currencies_uri(self, new_uri: str):
        self._mono_currencies_uri = new_uri

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
