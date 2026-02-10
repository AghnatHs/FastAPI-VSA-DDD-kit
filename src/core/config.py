"""
core.config
Configuration settings for the application.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Centralized configuration settings."""

    PORT = os.getenv("PORT")

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    @property
    def database_url(self) -> str:
        """Full database connection URL."""
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
