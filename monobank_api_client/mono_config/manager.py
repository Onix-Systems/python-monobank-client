from typing import Dict, List
from datetime import datetime
from .config import (
    MONOBANK_CURRENCIES_URI,
    MONOBANK_CURRENCIES,
    MONOBANK_CURRENCY_CODE_A,
    MONOBANK_CURRENCY_CODE_B,
    MONOBANK_CLIENT_INFO_URI,
    MONOBANK_STATEMENT_URI,
    MONOBANK_WEBHOOK_URI,
    MONO_CREATE_SUCCESS_CODE,
    MONO_CREATE_SUCCESS_DETAIL,
    MONO_UPDATE_SUCCESS_CODE,
    MONO_UPDATE_SUCCESS_DETAIL,
    MONO_DELETE_SUCCESS_CODE,
    MONO_DELETE_SUCCESS_DETAIL,
    MONO_CURRENCY_EXCEPTION_CODE,
    MONO_CURRENCY_EXCEPTION_DETAIL,
    MONO_EXISTS_EXCEPTION_CODE,
    MONO_EXISTS_EXCEPTION_DETAIL,
    MONO_DOES_NOT_EXISTS_EXCEPTION_CODE,
    MONO_DOES_NOT_EXISTS_EXCEPTION_DETAIL,
)


class BaseMonoManager:
    def __init__(self, token=None) -> None:
        self._token = token

    _mono_currencies_uri = MONOBANK_CURRENCIES_URI
    _mono_currencies = MONOBANK_CURRENCIES
    _mono_currency_code_a = MONOBANK_CURRENCY_CODE_A
    _mono_currency_code_b = MONOBANK_CURRENCY_CODE_B
    _mono_client_info_uri = MONOBANK_CLIENT_INFO_URI
    _mono_statement_uri = MONOBANK_STATEMENT_URI
    _mono_webhook_uri = MONOBANK_WEBHOOK_URI
    _mono_create_success_code = MONO_CREATE_SUCCESS_CODE
    _mono_create_success_detail = MONO_CREATE_SUCCESS_DETAIL
    _mono_update_success_code = MONO_UPDATE_SUCCESS_CODE
    _mono_update_success_detail = MONO_UPDATE_SUCCESS_DETAIL
    _mono_delete_success_code = MONO_DELETE_SUCCESS_CODE
    _mono_delete_success_detail = MONO_DELETE_SUCCESS_DETAIL
    _mono_currency_exception_code = MONO_CURRENCY_EXCEPTION_CODE
    _mono_currency_exception_detail = MONO_CURRENCY_EXCEPTION_DETAIL
    _mono_exsists_exception_code = MONO_EXISTS_EXCEPTION_CODE
    _mono_exsists_exception_detail = MONO_EXISTS_EXCEPTION_DETAIL
    _mono_does_not_exsists_exception_code = MONO_DOES_NOT_EXISTS_EXCEPTION_CODE
    _mono_does_not_exsists_exception_detail = MONO_DOES_NOT_EXISTS_EXCEPTION_DETAIL

    @property
    def token(self) -> str:
        return self._token

    @token.setter
    def token(self, new_token: str) -> None:
        self._token = new_token

    @property
    def mono_currencies_uri(self) -> str:
        return self._mono_currencies_uri

    @mono_currencies_uri.setter
    def mono_currencies_uri(self, new_uri: str) -> None:
        self._mono_currencies_uri = new_uri

    @property
    def mono_currency_code_a(self) -> str:
        return self._mono_currency_code_a

    @mono_currency_code_a.setter
    def mono_currency_code_a(self, new_code: str) -> None:
        self._mono_currency_code_a = new_code

    @property
    def mono_currency_code_b(self) -> str:
        return self._mono_currency_code_b

    @mono_currency_code_b.setter
    def mono_currency_code_b(self, new_code: str) -> None:
        self._mono_currency_code_b = new_code

    @property
    def mono_currencies(self) -> Dict:
        return self._mono_currencies

    @mono_currencies.setter
    def mono_currencies(self, new_currencies: Dict) -> None:
        self._mono_currencies = new_currencies

    @property
    def mono_client_info_uri(self) -> str:
        return self._mono_client_info_uri

    @mono_client_info_uri.setter
    def mono_client_info_uri(self, new_uri: str) -> None:
        self._mono_client_info_uri = new_uri

    @property
    def mono_statement_uri(self) -> str:
        return self._mono_statement_uri

    @mono_statement_uri.setter
    def mono_statement_uri(self, new_uri: str) -> None:
        self._mono_statement_uri = new_uri

    @property
    def mono_webhook_uri(self) -> str:
        return self._mono_webhook_uri

    @mono_webhook_uri.setter
    def mono_webhook_uri(self, new_uri: str) -> None:
        self._mono_webhook_uri = new_uri

    @property
    def mono_create_success_code(self) -> int:
        return self._mono_create_success_code

    @mono_create_success_code.setter
    def mono_create_success_code(self, new_code: int) -> None:
        self._mono_create_success_code = new_code

    @property
    def mono_create_success_detail(self) -> str:
        return self._mono_create_success_detail

    @mono_create_success_detail.setter
    def mono_create_success_detail(self, new_detail: str) -> None:
        self._mono_create_success_detail = new_detail

    @property
    def mono_update_success_code(self) -> int:
        return self._mono_update_success_code

    @mono_update_success_code.setter
    def mono_update_success_code(self, new_code: int) -> None:
        self._mono_update_success_code = new_code

    @property
    def mono_update_success_detail(self) -> str:
        return self._mono_update_success_detail

    @mono_update_success_detail.setter
    def mono_update_success_detail(self, new_detail: str) -> None:
        self._mono_update_success_detail = new_detail

    @property
    def mono_delete_success_code(self) -> int:
        return self._mono_delete_success_code

    @mono_delete_success_code.setter
    def mono_delete_success_code(self, new_code: int) -> None:
        self._mono_delete_success_code = new_code

    @property
    def mono_delete_success_detail(self) -> str:
        return self._mono_delete_success_detail

    @mono_delete_success_detail.setter
    def mono_delete_success_detail(self, new_detail: str) -> None:
        self._mono_delete_success_detail = new_detail

    @property
    def mono_currency_exception_code(self) -> int:
        return self._mono_currency_exception_code

    @mono_currency_exception_code.setter
    def mono_currency_exception_code(self, new_code: int) -> None:
        self._mono_currency_exception_code = new_code

    @property
    def mono_currency_exception_detail(self) -> str:
        return self._mono_currency_exception_detail

    @mono_currency_exception_detail.setter
    def mono_currency_exception_detail(self, new_detail: str) -> None:
        self._mono_currency_exception_detail = new_detail

    @property
    def mono_exsists_exception_code(self) -> int:
        return self._mono_exsists_exception_code

    @mono_exsists_exception_code.setter
    def mono_exsists_exception_code(self, new_code: int) -> None:
        self._mono_exsists_exception_code = new_code

    @property
    def mono_exsists_exception_detail(self) -> str:
        return self._mono_exsists_exception_detail

    @mono_exsists_exception_detail.setter
    def mono_exsists_exception_detail(self, new_detail: str) -> None:
        self._mono_exsists_exception_detail = new_detail

    @property
    def mono_does_not_exsists_exception_code(self) -> int:
        return self._mono_does_not_exsists_exception_code

    @mono_does_not_exsists_exception_code.setter
    def mono_does_not_exsists_exception_code(self, new_code: int) -> None:
        self._mono_does_not_exsists_exception_code = new_code

    @property
    def mono_does_not_exsists_exception_detail(self) -> str:
        return self._mono_does_not_exsists_exception_detail

    @mono_does_not_exsists_exception_detail.setter
    def mono_does_not_exsists_exception_detail(self, new_detail: str) -> None:
        self._mono_does_not_exsists_exception_detail = new_detail

    @staticmethod
    def date(period: int) -> Dict:
        _day = 86400  # 1 day (UNIX)
        try:
            delta = int(datetime.now().timestamp()) - (period * _day)
            time_delta = {"time_delta": delta}
            return time_delta
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def currency(self, ccy_pair: str, pair: Dict, currencies: Dict) -> Dict:
        try:
            code_a = self.mono_currency_code_a
            code_b = self.mono_currency_code_b
            code = currencies.get("code")
            payload = currencies.get("detail")
            for ccy in payload:
                if ccy.get(code_a) == pair.get(code_a) and ccy.get(code_b) == pair.get(
                    code_b
                ):
                    cross = ccy.get("rateCross")
                    if cross is not None:
                        currency = {ccy_pair: {"Cross": cross}}
                    else:
                        buy = ccy.get("rateBuy")
                        sale = ccy.get("rateSell")
                        currency = {ccy_pair: {"Buy": buy, "Sale": sale}}
                    response = {"code": code, "detail": currency}
            return response
        except AttributeError:
            error_response = {"code": code, "detail": payload}
            return error_response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def create_success(self) -> Dict:
        try:
            response = {
                "code": self.mono_create_success_code,
                "detail": self.mono_create_success_detail,
            }
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def update_success(self) -> Dict:
        try:
            response = {
                "code": self.mono_update_success_code,
                "detail": self.mono_update_success_detail,
            }
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def delete_success(self) -> Dict:
        try:
            response = {
                "code": self.mono_delete_success_code,
                "detail": self.mono_delete_success_detail,
            }
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def currency_exception(self, list_ccy: List) -> Dict:
        try:
            response = {
                "code": self.mono_currency_exception_code,
                "detail": self.mono_currency_exception_detail,
                "list of acceptable currency pairs": list_ccy,
            }
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def exists_exception(self) -> Dict:
        try:
            response = {
                "code": self.mono_exsists_exception_code,
                "detail": self.mono_exsists_exception_detail,
            }
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    def does_not_exsists_exception(self) -> Dict:
        try:
            response = {
                "code": self.mono_does_not_exsists_exception_code,
                "detail": self.mono_does_not_exsists_exception_detail,
            }
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception
