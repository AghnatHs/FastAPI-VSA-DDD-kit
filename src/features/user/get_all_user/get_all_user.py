from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import get_async_db_session
from src.core.http import HTTPDataResponse
from src.infrastructure.repositories.user_repository import UserRepository

get_all_user_router = APIRouter(prefix="/users", tags=["users"])


class UserResponseDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    email: str
    created_at: datetime
    updated_at: datetime


@get_all_user_router.get("", response_model=HTTPDataResponse[list[UserResponseDto]])
async def get_all_user(
    db: AsyncSession = Depends(get_async_db_session),
) -> HTTPDataResponse[list[UserResponseDto]]:
    users = await UserRepository(db).findAll()
    return HTTPDataResponse[list[UserResponseDto]](
        status="success",
        data=[UserResponseDto.model_validate(user) for user in users],
        message="Users fetched successfully",
    )
