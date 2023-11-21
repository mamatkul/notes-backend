from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .config import settings

engine = create_async_engine(
    f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}",
    future=True,
    echo=True,
    execution_options={"isolation_level": "AUTOCOMMIT"},
)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
