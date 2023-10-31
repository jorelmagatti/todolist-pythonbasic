
from contextlib import asynccontextmanager
from sqlite3 import OperationalError
from typing import AsyncIterator, cast

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from todo_list.config import settings

Base = declarative_base()
engine = create_async_engine(str(settings.database_uri))

async_session_factory = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
)


@asynccontextmanager
async def get_db() -> AsyncIterator[AsyncSession]:
    db = cast(AsyncSession, async_session_factory())
    try:
        yield db
    finally:
        await db.close()


async def check_database():
    try:
        async with engine.connect():
            return True
    except OperationalError:
        return False
