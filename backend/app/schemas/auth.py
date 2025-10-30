"""Pydantic schemas for authentication flows."""
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=12)
    first_name: str | None = None
    last_name: str | None = None


class RegisterResponse(BaseModel):
    user_id: UUID
    email: EmailStr
    profile_completed: bool


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    expires_in: int
    refresh_token: str | None = None


class RefreshRequest(BaseModel):
    refresh_token: str | None = None


class PasswordForgotRequest(BaseModel):
    email: EmailStr


class PasswordResetRequest(BaseModel):
    token: str
    password: str = Field(min_length=12)


class UserSession(BaseModel):
    user_id: UUID
    email: EmailStr
    first_name: str | None
    last_name: str | None
    roles: list[str]
    last_login: datetime | None
