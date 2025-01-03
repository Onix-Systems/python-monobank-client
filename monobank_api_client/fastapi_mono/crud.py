from typing import Dict
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from monobank_api_client.fastapi_mono.models import MonoModel as mdl
from monobank_api_client.fastapi_mono.schemas import MonoSchema, MonoSchemaUpdate
from monobank_api_client.async_mono.manager import AsyncMonoManager


async def create_mono(schema: MonoSchema, session: AsyncSession) -> Dict:
    try:
        mng = AsyncMonoManager()
        query = await session.execute(select(mdl).where(mdl.user_id == schema.user_id))
        if query.first() is not None:
            return mng.exists_exception()
        new_obj = insert(mdl).values(**schema.model_dump())
        await session.execute(new_obj)
        await session.commit()
        return mng.create_success()
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


async def read_mono(user_id: str, session: AsyncSession) -> Dict:
    try:
        query = await session.execute(select(mdl).where(mdl.user_id == user_id))
        return query.first()
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


async def update_mono(
    user_id: str, schema: MonoSchemaUpdate, session: AsyncSession
) -> Dict:
    try:
        mng = AsyncMonoManager()
        query = await session.execute(select(mdl).where(mdl.user_id == user_id))
        if query.first() is not None:
            query = await session.execute(
                update(mdl).values(**schema.model_dump()).where(mdl.user_id == user_id)
            )
            await session.commit()
            return mng.update_success()
        return mng.does_not_exsists_exception()
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


async def delete_mono(user_id: str, session: AsyncSession) -> Dict:
    try:
        mng = AsyncMonoManager()
        query = await session.execute(select(mdl).where(mdl.user_id == user_id))
        if query.first() is not None:
            query = await session.execute(delete(mdl).where(mdl.user_id == user_id))
            await session.commit()
            return mng.delete_success()
        return mng.does_not_exsists_exception()
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception
