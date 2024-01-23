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
        error = {"detail": str(exc)}
        return error


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
        error = {"detail": str(exc)}
        return error


@router.delete("/delete-mono")
async def delete_monobank(
    user: str, session: AsyncSession = Depends(async_session)
) -> Dict:
    try:
        response = await crud.delete_mono(user, session)
        return response
    except Exception as exc:
        error = {"detail": str(exc)}
        return error


@router.get("/currencies")
async def currencies() -> Dict:
    mng = AsyncMonoManager()
    response = await mng.get_currencies()
    return response


@router.get("/currency")
async def currency(ccy_pair: str) -> Dict:
    mng = AsyncMonoManager()
    response = await mng.get_currency(ccy_pair)
    return response


@router.get("/client_info")
async def client_info(
    user: str, session: AsyncSession = Depends(async_session)
) -> Dict:
    token = await crud.read_mono(user, session)
    mng = AsyncMonoManager(token.get("token"))
    response = await mng.get_client_info()
    return response


@router.get("/balance")
async def balance(user: str, session: AsyncSession = Depends(async_session)) -> Dict:
    token = await crud.read_mono(user, session)
    mng = AsyncMonoManager(token.get("token"))
    response = await mng.get_balance()
    return response


@router.get("/statement")
async def statement(
    user: str, period: int, session: AsyncSession = Depends(async_session)
) -> Dict:
    token = await crud.read_mono(user, session)
    mng = AsyncMonoManager(token.get("token"))
    response = await mng.get_statement(period)
    return response


@router.post("/webhook")
async def webhook(
    user: str, webhook: str, session: AsyncSession = Depends(async_session)
) -> Dict:
    token = await crud.read_mono(user, session)
    mng = AsyncMonoManager(token.get("token"))
    response = await mng.create_webhook(webhook)
    return response
