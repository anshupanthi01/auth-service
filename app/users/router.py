from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, APIRouter
from app.users.service import UserService
from app.users.schema import UserProfileResponse, UserUpdate
from app.database.database import get_db
from app.users.repository import UserRepository

router = APIRouter(prefix="/users", tags=["Users"])

# 1. This function is the "injector"
async def get_user_service(
        session: AsyncSession = Depends(get_db)
        ) -> UserService:
    user_repo = UserRepository(session)
    return UserService(user_repo, session)

@router.get("/me")
async def read_current_user():
    pass