"""
Domain model for user
"""

from datetime import datetime
from typing import Self
from uuid import UUID, uuid4


class User:
    """User domain model"""

    @classmethod
    def register(
        cls,
        email: str,
        hashed_password: str,
        created_at: datetime,
        updated_at: datetime,
    ) -> Self:
        """Register a new user with validation"""
        if "@" not in email:
            raise ValueError("Invalid email")

        return cls(uuid4(), email, hashed_password, created_at, updated_at)

    def __init__(
        self,
        id: UUID,
        email: str,
        hashed_password: str,
        created_at: datetime,
        updated_at: datetime,
    ) -> None:
        self.id = id
        self.email = email
        self.hashed_password = hashed_password
        self.created_at = created_at
        self.updated_at = updated_at
