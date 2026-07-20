from __future__ import annotations
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta, UTC
from typing import Annotated, List
from fastapi import APIRouter, Depends, status
from app.auth.service import AuthService
from app.core.security import create_token, decode_token, hash_password, verify_password
from app.auth.schemas import UserRegister, RegisterResponse
from app.database.database import get_db
from app.users.repository import UserRepository

router = APIRouter(prefix="/users")

# ============= REGISTER / CREATE USER =============
@router.post('/register', response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(user_register = UserRegister, session = Annotated[AsyncSession, Depends(get_db)]):
    pass