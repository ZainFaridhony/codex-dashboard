"""Dashboard API routes."""
from __future__ import annotations

from datetime import datetime, timedelta
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Query, status

from ..dependencies import get_db
from ..schemas import dashboard as schemas

router = APIRouter()


@router.get("/overview", response_model=schemas.DashboardOverviewResponse)
async def dashboard_overview(
    date_range: str = Query("30d"),
    db=Depends(get_db),  # noqa: B008
) -> schemas.DashboardOverviewResponse:
    """Return a placeholder dashboard overview payload."""

    _ = db
    if date_range not in {"7d", "30d", "90d"}:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unsupported date range")

    return schemas.DashboardOverviewResponse(
        user={
            "user_id": uuid4(),
            "email": "user@example.com",
            "first_name": "Example",
            "last_name": "User",
            "is_email_verified": True,
            "last_login": datetime.utcnow() - timedelta(days=1),
        },
        stats=schemas.DashboardStats(logins_30d=5, tasks_completed=12),
        widgets=[
            schemas.DashboardWidgetPayload(
                id=uuid4(),
                type="tasks",
                data={"completed": 12, "pending": 3},
            )
        ],
    )


@router.patch("/widgets/{widget_id}", response_model=schemas.DashboardWidgetPayload)
async def update_widget(
    widget_id: uuid4,
    payload: schemas.DashboardWidgetPayload,
    db=Depends(get_db),  # noqa: B008
) -> schemas.DashboardWidgetPayload:
    """Update a dashboard widget configuration (stub)."""

    _ = db
    if widget_id != payload.id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Widget ID mismatch")
    return payload
