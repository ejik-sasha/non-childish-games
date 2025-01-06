from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text
import asyncio
from config import settings

# Синхронное подключение
sync_engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

# Асинхронное подключение
async_engine = create_async_engine(
    settings.DATABASE_URL_ASYNC,
    echo=False,
    # pool_size=5,
    # max_overflow=10,
)

session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

class Base(DeclarativeBase):
    pass