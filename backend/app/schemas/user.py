"""User related response schemas."""
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserProfile(BaseModel):
    user_id: UUID
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None
    is_email_verified: bool
    last_login: datetime | None = None
