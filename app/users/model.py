from __future__ import annotations
from sqlalchemy import String, Enum, Integer, DateTime, func, Boolean
from sqlalchemy.orm import mapped_column, Mapped
from typing import Optional  
from database.database import Base 
from datetime import datetime

class UserRole(str, Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"

class UserStatus(str, Enum):
    PENDING_VERIFICATION = "pending_verification"
    ACTIVE = "active"
    SUSPENDED = "suspended"
    DELETED = "deleted"
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)

    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False, index=True)

    email_verified: Mapped[bool] = mapped_column(Boolean, default=False ,nullable=False, index=True)
    email_verified_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    password_hash: Mapped[str] = mapped_column(String(200), nullable=False)

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

    status: Mapped[UserStatus] = mapped_column(Enum(UserStatus), default=UserStatus.PENDING_VERIFICATION ,nullable=False)

    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    # reset_tokens: Mapped[List[PasswordResetToken]]



# class PasswordResetToken(Base):
    # __tablename__ = "password_reset_tokens"


