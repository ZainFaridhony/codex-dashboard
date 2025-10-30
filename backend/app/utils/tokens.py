"""Utility helpers for tokens."""
from secrets import token_urlsafe


def generate_token(length: int = 32) -> str:
    """Generate a URL-safe random token."""

    return token_urlsafe(length)
