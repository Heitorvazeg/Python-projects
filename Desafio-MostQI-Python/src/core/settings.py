from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from .env file."""

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # API Configuration
    WORKFLOW_API: str = ""

    # Site URL
    SITE_URL: str = ""

    # Header Auth Configuration
    AUTH_TOKEN: str = ""

    # Application Configuration
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"


settings = Settings()
