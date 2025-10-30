"""Common dependency utilities for FastAPI routes."""
from collections.abc import AsyncIterator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .db.session import get_async_session


async def get_db(session: AsyncSession = Depends(get_async_session)) -> AsyncIterator[AsyncSession]:
    """Provide a database session to request handlers."""

    try:
        yield session
    finally:
        await session.close()
