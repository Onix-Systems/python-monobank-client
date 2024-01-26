from typing import Dict
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_mono.database import async_session
from fastapi_mono.schemas import MonoSchema, MonoSchemaUpdate
from fastapi_mono import crud
from async_mono.manager import AsyncMonoManager


router = APIRouter(tags=["Mono"])


@router.post("/add-mono")
async def add_monobank(
    schema: MonoSchema, session: AsyncSession = Depends(async_session)
) -> Dict:
    try:
        response = await crud.create_mono(schema, session)
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.put("/change-mono")
async def change_monobank(
    user: str,
    schema: MonoSchemaUpdate,
    session: AsyncSession = Depends(async_session),
) -> Dict:
    try:
        response = await crud.update_mono(user, schema, session)
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.delete("/delete-mono")
async def delete_monobank(
    user: str, session: AsyncSession = Depends(async_session)
) -> Dict:
    try:
        response = await crud.delete_mono(user, session)
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.get("/currencies")
async def currencies() -> Dict:
    try:
        mng = AsyncMonoManager()
        response = await mng.get_currencies()
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.get("/currency")
async def currency(ccy_pair: str) -> Dict:
    try:
        mng = AsyncMonoManager()
        response = await mng.get_currency(ccy_pair)
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.get("/client_info")
async def client_info(
    user_id: str, session: AsyncSession = Depends(async_session)
) -> Dict:
    try:
        mng = AsyncMonoManager()
        payload = await crud.read_mono(user_id, session)
        if payload is not None:
            mng.token = payload[0].mono_token
            response = await mng.get_client_info()
        else:
            response = mng.does_not_exsists_exception()
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.get("/balance")
async def balance(user_id: str, session: AsyncSession = Depends(async_session)) -> Dict:
    try:
        mng = AsyncMonoManager()
        payload = await crud.read_mono(user_id, session)
        if payload is not None:
            mng.token = payload[0].mono_token
            response = await mng.get_balance()
        else:
            response = mng.does_not_exsists_exception()
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.get("/statement")
async def statement(
    user_id: str, period: int, session: AsyncSession = Depends(async_session)
) -> Dict:
    try:
        mng = AsyncMonoManager()
        payload = await crud.read_mono(user_id, session)
        if payload is not None:
            mng.token = payload[0].mono_token
            response = await mng.get_statement(period)
        else:
            response = mng.does_not_exsists_exception()
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.post("/webhook")
async def webhook(
    user_id: str, webhook: str, session: AsyncSession = Depends(async_session)
) -> Dict:
    try:
        mng = AsyncMonoManager()
        payload = await crud.read_mono(user_id, session)
        if payload is not None:
            mng.token = payload[0].mono_token
            response = await mng.create_webhook(webhook)
        else:
            response = mng.does_not_exsists_exception()
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception
