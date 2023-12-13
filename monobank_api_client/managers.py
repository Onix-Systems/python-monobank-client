from typing import Any, Dict, Tuple
import requests
from datetime import datetime

from .config import (
    MONOBANK_CLIENT_INFO_URI,
    MONOBANK_CURRENCY_URI,
    MONOBANK_STATEMENT_URI,
    MONOBANK_WEBHOOK_URI,
)


class MonoManager:

    def __init__(self, request, token=None):
        self.request = request
        self._token = token
    
    _session = requests.Session()

    _day_unix = 86400   # 1 day (UNIX)
    
    _mono_currency_uri = MONOBANK_CURRENCY_URI
    _mono_client_info_uri = MONOBANK_CLIENT_INFO_URI
    _mono_statement_uri = MONOBANK_STATEMENT_URI
    _mono_webhook_uri = MONOBANK_WEBHOOK_URI

    @property
    def token(self):
        return self._token
    
    @token.setter
    def token(self, new_token):
        self._token = new_token

    @property
    def mono_currency_uri(self):
        return self._mono_currency_uri
    
    @mono_currency_uri.setter
    def mono_currency_uri(self, new_uri):
        self._mono_currency_uri = new_uri

    @property
    def mono_client_info_uri(self):
        return self._mono_client_info_uri
    
    @mono_client_info_uri.setter
    def mono_client_info_uri(self, new_uri):
        self._mono_client_info_uri = new_uri

    @property
    def mono_statement_uri(self):
        return self._mono_statement_uri
    
    @mono_statement_uri.setter
    def mono_statement_uri(self, new_uri):
        self._mono_statement_uri = new_uri

    @property
    def mono_webhook_uri(self):
        return self._mono_webhook_uri
    
    @mono_webhook_uri.setter
    def mono_webhook_uri(self, new_uri):
        self._mono_webhook_uri = new_uri

    @classmethod
    @property
    def get_currency(cls) -> Tuple[int, Dict[str, Any]]:
        try:
            session = cls._session
            uri = cls._mono_currency_uri
            response = session.get(uri)
            response.raise_for_status()
            return response.status_code, response.json()
        except requests.exceptions.HTTPError as exc:
            error_response = {
                "code": response.status_code,
                "detail": str(exc),
            }
            return error_response
        except Exception as exc:
            exception = {
                "detail": str(exc)
            }
            return exception

    def get_client_info(self) -> Tuple[int, Dict[str, Any]]:
        try:
            session = self._session
            token = self._token
            uri = self._mono_client_info_uri
            headers = {"X-Token": token}
            response = session.get(uri, headers=headers)
            response.raise_for_status()
            return response.status_code, response.json()
        except requests.exceptions.HTTPError as exc:
            error_response = {
                "code": response.status_code,
                "detail": str(exc),
            }
            return error_response
        except Exception as exc:
            exception = {
                "detail": str(exc)
            }
            return exception

    def get_balance(self) -> Tuple[int, Dict[str, Any]]:
        try:
            response = self.get_client_info()
            code = response[0]
            payload = response[1]
            balance = {
                'balance': payload["accounts"][0]["balance"] / 100
            }
            return code, balance
        except Exception:
            return response

    def get_statement(self, period: int) -> Tuple[int, Dict[str, Any]]:
        try:
            session = self._session
            token = self._token
            uri = self._mono_statement_uri
            headers = {"X-Token": token}
            time_delta = int(datetime.now().timestamp()) - (period * self._day_unix)
            response = session.get(f"{uri}{time_delta}/", headers=headers)
            response.raise_for_status()
            return response.status_code, response.json()
        except requests.exceptions.HTTPError as exc:
            error_response = {
                "code": response.status_code,
                "detail": str(exc),
            }
            return error_response
        except Exception as exc:
            exception = {
                "detail": str(exc)
            }
            return exception

    def create_webhook(self, webHookUrl: str) -> Tuple[int, Dict[str, Any]]:
        try:            
            session = self._session
            token = self._token
            uri = self._mono_webhook_uri
            headers = {"X-Token": token}
            response = session.post(uri, headers=headers, data=webHookUrl)
            response.raise_for_status()
            return response.status_code, response.json()
        except requests.exceptions.HTTPError as exc:
            error_response = {
                "code": response.status_code,
                "detail": str(exc)
            }
            return error_response
        except Exception as exc:
            exception = {
                "detail": str(exc)
            }
            return exception
