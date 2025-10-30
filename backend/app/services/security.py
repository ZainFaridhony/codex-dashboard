"""Security utilities for token handling (placeholders)."""
from datetime import datetime, timedelta
from typing import Any

import jwt

from ..config import get_settings

_settings = get_settings()


def create_access_token(subject: str, expires_delta: timedelta | None = None) -> str:
    """Generate a signed JWT access token."""

    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=_settings.access_token_exp_minutes))
    payload: dict[str, Any] = {"sub": subject, "exp": expire}
    return jwt.encode(payload, _settings.jwt_private_key, algorithm=_settings.jwt_algorithm)
