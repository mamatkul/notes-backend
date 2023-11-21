from datetime import datetime, timedelta
from functools import wraps
from typing import Optional

from fastapi import Depends, HTTPException
from fastapi_users.authentication.strategy import jwt
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.core.config import settings
from app.api.core.crud import CRUDBase
from app.api.core.dependencies import get_async_session
from app.api.core.models.notes import Note
from app.api.core.models.users import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
notes_crud = CRUDBase(Note)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def check_note_ownership(func):
    @wraps(func)
    async def wrapper(id: int, db: AsyncSession = Depends(get_async_session), user: User = Depends()):
        if func.__name__ == "get_all_notes":
            return await func(db, user_id=user.id)

        note = await notes_crud.get(db, id)
        if note is None or note.user_id != user.id:
            raise HTTPException(status_code=404, detail="Note not found or you don't have access")
        return await func(id, db, user)

    return wrapper
