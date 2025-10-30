"""Configuration settings for the Codex Dashboard backend."""
from functools import lru_cache

from pydantic import BaseSettings, Field, PostgresDsn, RedisDsn


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    environment: str = Field("development", env="APP_ENV")
    database_url: PostgresDsn = Field(..., env="DATABASE_URL")
    redis_url: RedisDsn = Field(..., env="REDIS_URL")
    jwt_private_key: str = Field(..., env="JWT_PRIVATE_KEY")
    jwt_public_key: str = Field(..., env="JWT_PUBLIC_KEY")
    jwt_algorithm: str = Field("RS256", env="JWT_ALGORITHM")
    access_token_exp_minutes: int = Field(15, env="ACCESS_TOKEN_EXP_MINUTES")
    refresh_token_exp_days: int = Field(30, env="REFRESH_TOKEN_EXP_DAYS")
    brevo_api_key: str = Field(..., env="BREVO_API_KEY")
    google_client_id: str = Field(..., env="GOOGLE_CLIENT_ID")
    google_client_secret: str = Field(..., env="GOOGLE_CLIENT_SECRET")
    google_redirect_uri: str = Field(..., env="GOOGLE_REDIRECT_URI")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings instance."""

    return Settings()
