from typing import AsyncGenerator, Generator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from .models.users import User
from .repository.users import UserManager
from .session import async_session


async def get_async_session() -> Generator:
    """Database session generator."""
    session: AsyncSession = async_session()
    try:
        yield session
    finally:
        await session.close()


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    """User CRUD manager."""
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    """DI for UserManager."""
    yield UserManager(user_db)
