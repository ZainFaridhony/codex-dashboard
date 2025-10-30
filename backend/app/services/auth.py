"""Authentication service layer placeholders."""
from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession


class AuthService:
    """Service encapsulating authentication workflows."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def register_user(self, *args, **kwargs):  # noqa: ANN002, ANN003
        raise NotImplementedError

    async def authenticate_user(self, *args, **kwargs):  # noqa: ANN002, ANN003
        raise NotImplementedError
