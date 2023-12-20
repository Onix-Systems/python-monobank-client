import requests
from typing import Dict, List
from datetime import datetime

from .config import (
    MONOBANK_CLIENT_INFO_URI,
    MONOBANK_CURRENCY_URI,
    MONOBANK_STATEMENT_URI,
    MONOBANK_WEBHOOK_URI,
)


class MonoManager:

    def __init__(self, token=None):
        self._token = token
    
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
    def session(cls) -> requests.sessions.Session:
        return requests.Session()
    
    @staticmethod
    def __date(period: int) -> int|Dict:
        _day = 86400   # 1 day (UNIX)
        try:
            time_delta = int(datetime.now().timestamp()) - (period * _day)
            return time_delta
        except Exception as exc:
            exception = {
                'detail': str(exc)
            }
            return exception

    def get_currency(self) -> List[Dict]|Dict:
        try:
            session = self.session()
            uri = self.mono_currency_uri
            response = session.get(uri)
            code = response.status_code
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as exc:
            error_response = {
                "code": code,
                "detail": str(exc)
            }
            return error_response
        except Exception as exc:
            exception = {
                "detail": str(exc)
            }
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
            return response.json()
        except requests.exceptions.HTTPError as exc:
            error_response = {
                "code": code,
                "detail": str(exc)
            }
            return error_response
        except Exception as exc:
            exception = {
                "detail": str(exc)
            }
            return exception

    def get_balance(self) -> Dict:
        try:
            response = self.get_client_info()
            balance = {
                'balance': response["accounts"][0]["balance"] / 100
            }
            return balance
        except Exception:
            return response

    def get_statement(self, period: int) -> List[Dict]|Dict:
        try:
            session = self.session()
            token = self.token
            uri = self.mono_statement_uri
            headers = {"X-Token": token}
            time_delta = self.__date(period)
            response = session.get(
                f"{uri}{time_delta}/", headers=headers
            )
            code = response.status_code
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as exc:
            error_response = {
                "code": code,
                "detail": str(exc)
            }
            return error_response
        except Exception as exc:
            exception = {
                "detail": str(exc)
            }
            return exception

    def create_webhook(self, webhook: str) -> Dict:
        try:            
            session = self.session()
            token = self.token
            uri = self.mono_webhook_uri
            headers = {"X-Token": token}
            response = session.post(
                uri, headers=headers, data=webhook
            )
            code = response.status_code
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as exc:
            error_response = {
                "code": code,
                "detail": str(exc)
            }
            return error_response
        except Exception as exc:
            exception = {
                "detail": str(exc)
            }
            return exception
