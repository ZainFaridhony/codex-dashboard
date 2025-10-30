"""Application entrypoint for the Codex Dashboard backend."""
from fastapi import FastAPI

from .routers import auth, dashboard


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""
    application = FastAPI(title="Codex Dashboard API", version="0.1.0")

    application.include_router(auth.router, prefix="/api/auth", tags=["auth"])
    application.include_router(dashboard.router, prefix="/api/dashboard", tags=["dashboard"])

    @application.get("/health", tags=["health"])
    async def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return application


app = create_app()
