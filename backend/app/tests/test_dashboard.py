"""Placeholder dashboard tests."""
import pytest


@pytest.mark.asyncio
async def test_dashboard_overview_not_implemented(async_client):
    with pytest.raises(RuntimeError):
        await async_client.get("/api/dashboard/overview")
