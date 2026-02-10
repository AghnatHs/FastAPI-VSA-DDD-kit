"""
Domain model for user
"""

from datetime import datetime
from typing import Self
from uuid import UUID, uuid4


class User:
    """User domain model"""

    @classmethod
    def register(cls, email: str, password: str) -> Self:
        """Register a new user with validation"""
        if "@" not in email:
            raise ValueError("Invalid email")
        if len(password) < 8:
            raise ValueError("Password too short")

        return cls(uuid4(), email, password)

    def __init__(
        self,
        nid: UUID,
        email: str,
        password: str,
        created_at: datetime = None,
        updated_at: datetime = None,
    ) -> None:
        self.id = nid
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at
