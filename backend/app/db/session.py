"""Database session and engine management."""
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from ..config import get_settings

_settings = get_settings()
_engine = create_async_engine(str(_settings.database_url), echo=False, future=True)
_async_session_factory = async_sessionmaker(bind=_engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncSession:
    """Create a new SQLAlchemy AsyncSession."""

    async with _async_session_factory() as session:
        yield session
