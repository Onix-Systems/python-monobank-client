from typing import Dict
import aiohttp
from mono_config.manager import BaseMonoManager


class AsyncMonoManager(BaseMonoManager):
    @classmethod
    async def session(cls) -> aiohttp.client.ClientSession:
        return aiohttp.ClientSession()

    async def get_currencies(self) -> Dict:
        try:
            session = await self.session()
            async with session:
                uri = self.mono_currencies_uri
                async with session.get(uri) as response:
                    try:
                        code = response.status
                        response.raise_for_status()
                        detail = await response.json()
                        payload = {"code": code, "detail": detail}
                        return payload
                    except aiohttp.ClientResponseError as exc:
                        error_response = {"code": code, "detail": str(exc.message)}
                        return error_response
        except Exception as exc:
            error = {"datail": str(exc)}
            return error

    async def get_currency(self, ccy_pair: str) -> Dict:
        try:
            pair = self.mono_currencies.get(ccy_pair)
            if pair is not None:
                currencies = await self.get_currencies()
                code = currencies.get("code")
                payload = currencies.get("detail")
                if isinstance(payload, list):
                    code_a = self.mono_currency_code_a
                    code_b = self.mono_currency_code_b
                    for ccy in payload:
                        if ccy.get(code_b) == pair.get(code_b):
                            for key, value in ccy.items():
                                if key == code_a and value == pair.get(code_a):
                                    buy = ccy.get("rateBuy")
                                    sale = ccy.get("rateSell")
                                    if buy is not None and sale is not None:
                                        currency = {
                                            ccy_pair: {"Buy": buy, "Sale": sale}
                                        }
                                    else:
                                        cross = ccy.get("rateCross")
                                        currency = {ccy_pair: {"Cross": cross}}
                                    response = {"code": code, "detail": currency}
                                    return response
                else:
                    response = {"code": code, "detail": payload}
                    return response
            list_ccy = [key for key in self.mono_currencies.keys()]
            error_response = {
                "code": 400,
                "detail": "Incorrect currency pair",
                "list of acceptable currency pairs": list_ccy,
            }
            return error_response
        except Exception as exc:
            error = {"detail": str(exc)}
            return error

    async def get_client_info(self) -> Dict:
        try:
            session = await self.session()
            async with session:
                uri = self.mono_client_info_uri
                token = self.token
                headers = {"X-Token": token}
                async with session.get(uri, headers=headers) as response:
                    try:
                        code = response.status
                        response.raise_for_status()
                        detail = await response.json()
                        payload = {"code": code, "detail": detail}
                        return payload
                    except aiohttp.ClientResponseError as exc:
                        error_response = {"code": code, "detail": str(exc.message)}
                        return error_response
        except Exception as exc:
            error = {"detail": str(exc)}
            return error

    async def get_balance(self) -> Dict:
        try:
            info = await self.get_client_info()
            code = info.get("code")
            data = info.get("detail")
            balance = {"balance": data["accounts"][0]["balance"] / 100}
            payload = {"code": code, "detail": balance}
            return payload
        except Exception:
            return info

    async def get_statement(self, period: int) -> Dict:
        if period > 31:
            error = {
                "code": 400,
                "detail": "The period should not be more than 31 days",
            }
            return error
        try:
            session = await self.session()
            async with session:
                token = self.token
                uri = self.mono_statement_uri
                headers = {"X-Token": token}
                time_delta = self.__date(period).get("time_delta")
                async with session.get(
                    f"{uri}{time_delta}/", headers=headers
                ) as response:
                    try:
                        code = response.status
                        response.raise_for_status()
                        detail = await response.json()
                        payload = {"code": code, "detail": detail}
                        return payload
                    except aiohttp.ClientResponseError as exc:
                        error_response = {"code": code, "detail": str(exc.message)}
                        return error_response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    async def create_webhook(self, webhook: str) -> Dict:
        try:
            session = await self.session()
            async with session:
                token = self.token
                uri = self.mono_webhook_uri
                headers = {"X-Token": token}
                async with session.post(uri, headers=headers, data=webhook) as response:
                    try:
                        code = response.status
                        response.raise_for_status()
                        detail = await response.json()
                        payload = {"code": code, "detail": detail}
                        return payload
                    except aiohttp.ClientResponseError as exc:
                        error_response = {"code": code, "detail": str(exc.message)}
                        return error_response
        except Exception as exc:
            error = {"detail": str(exc)}
            return error
