from typing import Any, Dict, Tuple
import requests
from datetime import datetime


class MonoManager:

    def __init__(self, request):
        self.request = request
    
    session = requests.Session()
    
    _currency_uri = 'https://api.monobank.ua/bank/currency'
    _client_info_uri = 'https://api.monobank.ua/personal/client-info'
    _statement_uri = 'https://api.monobank.ua/personal/statement/0/'
    _webhook_uri = 'https://api.monobank.ua/personal/webhook'
    _day_utc = 86400   # 1 day (UNIX)

    @classmethod
    def get_currency(cls) -> Tuple[int, Dict[str, Any]]:
        try:
            response = cls.session.get(cls._currency_uri)
            response.raise_for_status()
            return response.status_code, response.json()
        except requests.exceptions.HTTPError as exc:
            error_response = {
                "detail": str(exc),
                "code": response.status_code,
            }
            return error_response
        except Exception as exc:
            return {
                "detail": str(exc)
            }

    def get_client_info(self, token: str) -> Tuple[int, Dict[str, Any]]:
        try:
            headers = {"X-Token": token}
            response = self.session.get(
                self._client_info_uri,
                headers=headers
            )
            response.raise_for_status()
            return response.status_code, response.json()
        except requests.exceptions.HTTPError as exc:
            error_response = {
                "detail": str(exc),
                "code": response.status_code,
            }
            return error_response
        except Exception as exc:
            return {
                "detail": str(exc)
            }

    def get_balance(self, token: str) -> Tuple[int, Dict[str, Any]]:
        try:
            headers = {"X-Token": token}
            response = self.session.get(
                self._client_info_uri,
                headers=headers
            )
            response.raise_for_status()
            balance = {
                'balance': response.json()["accounts"][0]["balance"] / 100
            }
            return response.status_code, balance
        except requests.exceptions.HTTPError as exc:
            error_response = {
                "detail": str(exc),
                "code": response.status_code,
            }
            return error_response
        except Exception as exc:
            return {
                "detail": str(exc)
            }

    def get_statement(self, token: str, period: int) -> Tuple[int, Dict[str, Any]]:
        try:
            time_delta = int(datetime.now().timestamp()) - (period * self._day_utc)
            headers = {"X-Token": token}
            response = self.session.get(
                f"{self._statement_uri}{time_delta}/",
                headers=headers
            )
            response.raise_for_status()
            return response.status_code, response.json()
        except requests.exceptions.HTTPError as exc:
            error_response = {
                "detail": str(exc),
                "code": response.status_code,
            }
            return error_response
        except Exception as exc:
            return {
                "detail": str(exc)
            }

    def create_webhook(self, token: str, webHookUrl: str) -> Tuple[int, Dict[str, Any]]:
        try:
            headers = {"X-Token": token}
            response = self.session.post(
                self._webhook_uri,
                data=webHookUrl,
                headers=headers
            )
            response.raise_for_status()
            return response.status_code, response.json()
        except requests.exceptions.HTTPError as exc:
            error_response = {
                "detail": str(exc),
                "code": response.status_code,
            }
            return error_response
        except Exception as exc:
            return {
                "detail": str(exc)
            }
