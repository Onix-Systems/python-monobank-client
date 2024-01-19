import requests
from typing import Dict
from mono_config.manager import BaseMonoManager


class SyncMonoManager(BaseMonoManager):
    @classmethod
    def session(cls) -> requests.sessions.Session:
        return requests.Session()

    def get_currencies(self) -> Dict:
        try:
            session = self.session()
            uri = self.mono_currencies_uri
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
            list_ccy = self.mono_currencies.keys()
            error_response = {
                "code": 400,
                "detail": "Incorrect currency pair",
                "list of acceptable currency pairs": list_ccy,
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
