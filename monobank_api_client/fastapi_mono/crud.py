from typing import Dict, Tuple

from fastapi import Response, status
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_mono.models import MonoModel as mdl
from fastapi_mono.schemas import MonoSchema, MonoSchemaUpdate
from fastapi_mono.exceptions import MonoException


async def create_mono(schema: MonoSchema, session: AsyncSession) -> Dict:
    try:
        query = await session.execute(select(mdl).where(mdl.user_id == schema.user_id))
        if query.first() is not None:
            return MonoException.exists_error()
        else:
            new_obj = insert(mdl).values(**schema.model_dump())
            await session.execute(new_obj)
            await session.commit()
            response = Response(
                status_code=status.HTTP_201_CREATED,
                content="Mono-token added successfully.",
            )
        return response
    except Exception as exc:
        error = {"detail": str(exc)}
        return error


async def read_mono(user: str, session: AsyncSession) -> Tuple:
    try:
        query = await session.execute(select(mdl).where(mdl.user_id == user))
        token = query.first()[0].mono_token
        return token
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


async def update_mono(
    user: str, schema: MonoSchemaUpdate, session: AsyncSession
) -> Dict:
    try:
        query = await session.execute(select(mdl).where(mdl.user_id == user))
        if query.first() is not None:
            query = await session.execute(
                update(mdl).values(**schema.model_dump()).where(mdl.user_id == user)
            )
            await session.commit()
            response = {
                "code": status.HTTP_200_OK,
                "detail": "Mono-token chanched successfully.",
            }
        else:
            return MonoException.does_not_exsists()
        return response
    except Exception as exc:
        error = {"detail": str(exc)}
        return error


async def delete_mono(user: str, session: AsyncSession) -> Dict:
    try:
        query = await session.execute(select(mdl).where(mdl.user_id == user))
        if query.first() is not None:
            query = await session.execute(delete(mdl).where(mdl.user_id == user))
            await session.commit()
            response = {
                "code": status.HTTP_204_NO_CONTENT,
                "detail": "Mono-token deleted successfully.",
            }
        else:
            return MonoException.does_not_exsists()
        return response
    except Exception as exc:
        error = {"detail": str(exc)}
        return error
