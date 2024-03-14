import aiohttp
from typing import Dict
from mono_config.manager import BaseMonoManager


class AsyncMonoManager(BaseMonoManager):
    @classmethod
    async def session(cls) -> aiohttp.client.ClientSession:
        return aiohttp.ClientSession()

    async def async_request(
        self,
        method: str,
        uri: str,
        headers=None,
        data=None,
    ) -> Dict:
        session = await self.session()
        if method == "GET":
            response = await session.get(uri, headers=headers)
        if method == "POST":
            response = await session.post(uri, headers=headers, data=data)
        try:
            code = response.status
            response.raise_for_status()
            detail = await response.json()
            payload = self.mono_response(code, detail)
            return payload
        except aiohttp.ClientResponseError as exc:
            error_response = self.mono_response(code, str(exc.message))
            return error_response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    async def get_currencies(self) -> Dict:
        try:
            uri = self.mono_currencies_uri
            response = await self.async_request(method="GET", uri=uri)
            return response
        except Exception as exc:
            exception = {"datail": str(exc)}
            return exception

    async def get_currency(self, ccy: str) -> Dict:
        try:
            pair = self.mono_currencies.get(ccy)
            if pair is not None:
                currencies = await self.get_currencies()
                response = self.currency(ccy, pair, currencies)
            else:
                response = self.currency_exception()
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    async def get_client_info(self) -> Dict:
        try:
            uri = self.mono_client_info_uri
            token = self.token
            headers = {"X-Token": token}
            response = await self.async_request(method="GET", uri=uri, headers=headers)
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    async def get_balance(self) -> Dict:
        try:
            payload = await self.get_client_info()
            code = payload.get("code")
            data = payload.get("detail")
            balance = {"balance": data["accounts"][0]["balance"] / 100}
            response = self.mono_response(code, balance)
            return response
        except Exception:
            return payload

    async def get_statement(self, period: int) -> Dict:
        try:
            uri = self.mono_statement_uri
            token = self.token
            headers = {"X-Token": token}
            time_delta = self.date(period).get("time_delta")
            response = await self.async_request(
                method="GET", uri=f"{uri}{time_delta}/", headers=headers
            )
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception

    async def create_webhook(self, webhook: str) -> Dict:
        try:
            uri = self.mono_webhook_uri
            token = self.token
            headers = {"X-Token": token}
            response = await self.async_request(
                method="POST",
                uri=uri,
                headers=headers,
                data=webhook,
            )
            return response
        except Exception as exc:
            exception = {"detail": str(exc)}
            return exception
