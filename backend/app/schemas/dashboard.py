"""Dashboard API response schemas."""
from uuid import UUID

from pydantic import BaseModel, Field

from .user import UserProfile


class DashboardStats(BaseModel):
    logins_30d: int = Field(ge=0)
    tasks_completed: int = Field(ge=0)


class DashboardWidgetPayload(BaseModel):
    id: UUID
    type: str
    data: dict


class DashboardOverviewResponse(BaseModel):
    user: UserProfile
    stats: DashboardStats
    widgets: list[DashboardWidgetPayload]
