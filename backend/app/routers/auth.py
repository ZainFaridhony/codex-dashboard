"""Authentication related API routes."""
from __future__ import annotations

from datetime import datetime, timedelta
from uuid import uuid4

from fastapi import APIRouter, Depends, Header, HTTPException, Response, status

from ..dependencies import get_db
from ..schemas import auth as schemas

router = APIRouter()


@router.post("/register", response_model=schemas.RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(payload: schemas.RegisterRequest, db=Depends(get_db)) -> schemas.RegisterResponse:  # noqa: B008
    """Stub endpoint for registering a user."""

    _ = db  # placeholder usage
    return schemas.RegisterResponse(user_id=uuid4(), email=payload.email, profile_completed=False)


@router.post("/login", response_model=schemas.TokenResponse)
async def login(payload: schemas.LoginRequest, db=Depends(get_db)) -> schemas.TokenResponse:  # noqa: B008
    """Stub endpoint for logging in a user."""

    _ = db
    return schemas.TokenResponse(access_token="fake-access-token", expires_in=900, refresh_token="fake-refresh-token")


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(response: Response, db=Depends(get_db)) -> Response:  # noqa: B008
    """Stub endpoint clearing refresh token cookie."""

    _ = db
    response.delete_cookie("refresh_token")
    return response


@router.post("/token/refresh", response_model=schemas.TokenResponse)
async def refresh_token(
    payload: schemas.RefreshRequest,
    db=Depends(get_db),  # noqa: B008
    refresh_token_cookie: str | None = Header(default=None, alias="X-Refresh-Token"),
) -> schemas.TokenResponse:
    """Stub endpoint issuing new access tokens."""

    _ = db
    token = payload.refresh_token or refresh_token_cookie
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing refresh token")
    return schemas.TokenResponse(access_token="fake-access-token", expires_in=900, refresh_token="fake-refresh-token")


@router.get("/me", response_model=schemas.UserSession)
async def get_current_user(db=Depends(get_db)) -> schemas.UserSession:  # noqa: B008
    """Return a placeholder current user profile."""

    _ = db
    return schemas.UserSession(
        user_id=uuid4(),
        email="user@example.com",
        first_name="Example",
        last_name="User",
        roles=["user"],
        last_login=datetime.utcnow() - timedelta(days=1),
    )


@router.get("/google/authorize")
async def google_authorize() -> dict[str, str]:
    """Return placeholder Google authorization URL."""

    return {"redirect": "https://accounts.google.com/o/oauth2/v2/auth"}


@router.get("/google/callback")
async def google_callback() -> dict[str, str]:
    """Simulate Google OAuth callback completion."""

    return {"message": "Google OAuth successful"}


@router.post("/password/forgot", status_code=status.HTTP_202_ACCEPTED)
async def password_forgot(payload: schemas.PasswordForgotRequest, db=Depends(get_db)) -> dict[str, str]:  # noqa: B008
    """Request password reset email."""

    _ = db
    return {"message": "If the account exists, a reset email has been sent."}


@router.post("/password/reset")
async def password_reset(payload: schemas.PasswordResetRequest, db=Depends(get_db)) -> dict[str, str]:  # noqa: B008
    """Reset account password using provided token."""

    _ = db
    if payload.token == "invalid":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token")
    return {"message": "Password updated"}
