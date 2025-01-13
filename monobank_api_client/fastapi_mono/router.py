from typing import Dict
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from monobank_api_client.fastapi_mono.database import async_session
from monobank_api_client.fastapi_mono.schemas import MonoSchema, MonoSchemaUpdate
from monobank_api_client.fastapi_mono import crud
from monobank_api_client.async_mono.manager import AsyncMonoManager

router = APIRouter(tags=["Mono"], prefix="/mono")


@router.post("/add")
async def add_monobank(
        schema: MonoSchema, session: AsyncSession = Depends(async_session)
) -> Dict:
    """
    Add a new Monobank account.

    :param schema: Schema containing the Monobank account details.
    :param session: Async database session dependency.
    :return: Response dictionary with operation details.
    """
    try:
        response = await crud.create_mono(schema, session)
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.put("/change")
async def change_monobank(
        user: str,
        schema: MonoSchemaUpdate,
        session: AsyncSession = Depends(async_session),
) -> Dict:
    """
    Update an existing Monobank account.

    :param user: User identifier.
    :param schema: Schema with updated Monobank account details.
    :param session: Async database session dependency.
    :return: Response dictionary with operation details.
    """
    try:
        response = await crud.update_mono(user, schema, session)
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.delete("/delete")
async def delete_monobank(
        user: str, session: AsyncSession = Depends(async_session)
) -> Dict:
    """
    Delete a Monobank account.

    :param user: User identifier.
    :param session: Async database session dependency.
    :return: Response dictionary with operation confirmation.
    """
    try:
        response = await crud.delete_mono(user, session)
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.get("/currencies")
async def currencies() -> Dict:
    """
    Fetch available currency exchange rates from Monobank.

    :return: Response dictionary containing currency data.
    """
    try:
        mng = AsyncMonoManager()
        response = await mng.get_currencies()
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.get("/currency")
async def currency(ccy_pair: str) -> Dict:
    """
    Fetch details for a specific currency pair.

    :param ccy_pair: Currency pair (e.g., "USD/EUR").
    :return: Response dictionary containing currency pair details.
    """
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
    """
    Retrieve client information associated with Monobank.

    :param user_id: User identifier.
    :param session: Async database session dependency.
    :return: Response dictionary containing client information.
    """
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
    """
    Retrieve account balance for a Monobank user.

    :param user_id: User identifier.
    :param session: Async database session dependency.
    :return: Response dictionary containing balance details.
    """
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
    """
    Fetch Monobank account statement for a specific period.

    :param user_id: User identifier.
    :param period: Time period in days for the statements.
    :param session: Async database session dependency.
    :return: Response dictionary with transaction data.
    """
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
    """
    Register a webhook for a Monobank account.

    :param user_id: User identifier.
    :param webhook: Webhook URL to be registered.
    :param session: Async database session dependency.
    :return: Response dictionary confirming webhook registration.
    """
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
