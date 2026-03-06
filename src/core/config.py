"""
core.config
Configuration settings for the application.
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Centralized configuration settings."""

    def __init__(self) -> None:
        self.APP_ENV = os.getenv("APP_ENV", "development")

        self.PORT = self._get_required_int("PORT", min_value=1, max_value=65535)

        self.DB_HOST = self._get_required("DB_HOST")
        self.DB_PORT = self._get_required_int("DB_PORT", min_value=1, max_value=65535)
        self.DB_NAME = self._get_required("DB_NAME")
        self.DB_USER = self._get_required("DB_USER")
        self.DB_PASSWORD = self._get_required("DB_PASSWORD")

        self.JWT_SECRET_KEY = self._get_required("JWT_SECRET_KEY")
        self.JWT_EXPIRES_MINUTES = self._get_required_int(
            "JWT_EXPIRES_MINUTES", min_value=1, max_value=365 * 24 * 60
        )  # in minutes
        self.JWT_ALGORITHM = "HS512"

    @staticmethod
    def _get_required(key: str) -> str:
        value = os.getenv(key)
        if value is None or value.strip() == "":
            raise ValueError(f"Missing required environment variable: {key}")
        return value.strip()

    @staticmethod
    def _get_required_int(key: str, *, min_value: int, max_value: int) -> int:
        value = Settings._get_required(key)
        try:
            parsed = int(value)
        except ValueError as exc:
            raise ValueError(
                f"Environment variable {key} must be an integer, got: {value}"
            ) from exc

        if parsed < min_value or parsed > max_value:
            raise ValueError(
                f"Environment variable {key} must be between {min_value} and {max_value}, got: {parsed}"
            )

        return parsed

    @property
    def database_url(self) -> str:
        """Full database connection URL."""
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
