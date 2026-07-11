from __future__ import annotations
from sqlalchemy import String, Enum, Integer, DateTime, func, Boolean
from sqlalchemy.orm import mapped_column, Mapped
# from typing import List  
from database.database import Base 
from datetime import datetime

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False, index=True)

    email: Mapped[str] = mapped_column(String(20), unique=True, nullable=False, index=True)

    password_hash: Mapped[str] = mapped_column(String(30), nullable=False, index=True)

    role: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False, index=True)

    created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True), 
    server_default=func.now(), 
    nullable=False)

    updated_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True), 
    server_default=func.now(), 
    onupdate=func.now(), 
    nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, index=True)

    # reset_tokens: Mapped[List[PasswordResetToken]]



# class PasswordResetToken(Base):
    # __tablename__ = "password_reset_tokens"


