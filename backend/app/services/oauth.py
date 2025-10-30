"""OAuth service placeholder."""
from sqlalchemy.ext.asyncio import AsyncSession


class OAuthService:
    """Service handling external OAuth providers."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def exchange_code(self, *args, **kwargs):  # noqa: ANN002, ANN003
        raise NotImplementedError
