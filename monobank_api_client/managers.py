from typing import Any, Dict, Tuple
import requests
from datetime import datetime
from .config import (
    MONO_CURRENCY_URI,
    MONO_CLIENT_INFO_URI,
    MONO_STATEMENT_URI,
    MONO_WEBHOOK_URI,
    DAY_UTC,
)


class MonoManager:

    def __init__(self, request):
        self.request = request

    session = requests.Session()

    @classmethod
    @property
    def get_currency(cls) -> Tuple[int, Dict[str, Any]]:
        try:
            _ = cls.session.get(MONO_CURRENCY_URI)
            _.raise_for_status()
            return _.json()
        except Exception as exc:
            raise exc

    def get_client_info(self, token: str):
        try:
            headers = {"X-Token": token}
            _ = self.session.get(
                MONO_CLIENT_INFO_URI, headers=headers
            )
            _.raise_for_status()
            return _.json()
        except Exception as exc:
            raise exc

    def get_balance(self, token: str):
        try:
            payload = self.get_client_info(self, token)
            balance = {
                'balance': payload["accounts"][0]["balance"] / 100
            }
            return balance
        except Exception as exc:
            raise exc
        
    def get_statement(self, token: str, period: int):
        try:
            time_delta = int(datetime.now().timestamp()) - (period * DAY_UTC)
            headers = {"X-Token": token}
            _ = self.session.get(
                f"{MONO_STATEMENT_URI}{time_delta}/",
                headers=headers
            )
            _.raise_for_status()
            return _.json()
        except Exception as exc:
            raise exc

    def create_webhook(self, token: str, webHookUrl: str):
        try:
            headers = {"X-Token": token}
            _ = self.session.post(
                MONO_WEBHOOK_URI, data=webHookUrl, headers=headers
            )
            _.raise_for_status()
            return _.json()
        except Exception as exc:
            raise exc
