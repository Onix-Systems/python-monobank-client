from typing import Dict
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_mono.models import MonoModel as mdl
from fastapi_mono.schemas import MonoSchema, MonoSchemaUpdate
from async_mono.manager import AsyncMonoManager


async def create_mono(schema: MonoSchema, session: AsyncSession) -> Dict:
    try:
        mng = AsyncMonoManager()
        query = await session.execute(select(mdl).where(mdl.user_id == schema.user_id))
        if query.first() is not None:
            return mng.exists_exception()
        else:
            new_obj = insert(mdl).values(**schema.model_dump())
            await session.execute(new_obj)
            await session.commit()
            response = mng.create_success()
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


async def read_mono(user: str, session: AsyncSession) -> Dict:
    try:
        query = await session.execute(select(mdl).where(mdl.user_id == user))
        token = query.first()[0].mono_token
        response = {"token": token}
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


async def update_mono(
    user: str, schema: MonoSchemaUpdate, session: AsyncSession
) -> Dict:
    try:
        mng = AsyncMonoManager()
        query = await session.execute(select(mdl).where(mdl.user_id == user))
        if query.first() is not None:
            query = await session.execute(
                update(mdl).values(**schema.model_dump()).where(mdl.user_id == user)
            )
            await session.commit()
            response = mng.update_success()
        else:
            return mng.does_not_exsists_exception()
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


async def delete_mono(user: str, session: AsyncSession) -> Dict:
    try:
        mng = AsyncMonoManager()
        query = await session.execute(select(mdl).where(mdl.user_id == user))
        if query.first() is not None:
            query = await session.execute(delete(mdl).where(mdl.user_id == user))
            await session.commit()
            response = mng.delete_success()
        else:
            return mng.does_not_exsists_exception()
        return response
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception
