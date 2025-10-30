"""Placeholder tests for auth endpoints."""
import pytest


@pytest.mark.asyncio
async def test_register_not_implemented(async_client):
    with pytest.raises(RuntimeError):
        await async_client.post("/api/auth/register", json={})
