"""Dashboard related persistence models."""
from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, Integer, JSON, String
from sqlalchemy.dialects.postgresql import INET, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .user import User


class DashboardWidget(Base):
    """Dashboard widget configuration for a user."""

    id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    config: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    position: Mapped[int] = mapped_column(Integer, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

    user: Mapped[User] = relationship("User")


class AuditLog(Base):
    """Audit log entries for sensitive user actions."""

    id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[uuid4 | None] = mapped_column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="SET NULL"), nullable=True)
    action: Mapped[str] = mapped_column(String, nullable=False)
    ip: Mapped[str | None] = mapped_column(INET, nullable=True)
    metadata: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    user: Mapped[User | None] = relationship("User")
