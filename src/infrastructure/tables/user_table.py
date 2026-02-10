"""
Table that map to User domain model.
"""

import uuid

from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from src.core.db import Base
from src.domain.user import User


class UserTable(Base):
    """
    Table that map to User domain model.
    """

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    def to_domain(self) -> User:
        """Convert table model to domain model"""
        return User(
            nid=self.id,
            email=self.email,
            password=self.password,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @classmethod
    def from_domain(cls, user: User) -> "UserTable":
        """Convert domain model to table model"""
        return cls(
            id=user.id,
            email=user.email,
            password=user.password,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
