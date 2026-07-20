from __future__ import annotations
from sqlalchemy import String, Enum, Integer, DateTime, func, Boolean
from sqlalchemy.orm import mapped_column, Mapped
from typing import Optional  
from database.database import Base 
from datetime import datetime
from app.core.enums import UserRole, UserStatus

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)

    email: Mapped[str] = mapped_column(String(300), unique=True, nullable=False, index=True)

    password_hash: Mapped[str] = mapped_column(String(200), nullable=False)
    
    email_verified: Mapped[bool] = mapped_column(Boolean, default=False ,nullable=False, index=True)
    email_verified_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.USER,nullable=False, index=True)

    created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True), 
    server_default=func.now(), 
    nullable=False)

    updated_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True), 
    server_default=func.now(), 
    onupdate=func.now(), 
    nullable=False)

    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    
    status: Mapped[UserStatus] = mapped_column(Enum(UserStatus), default=UserStatus.PENDING_VERIFICATION ,nullable=False)
    
    deletion_requested_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True, default=None)
    # reset_tokens: Mapped[List[PasswordResetToken]]



# class PasswordResetToken(Base):
    # __tablename__ = "password_reset_tokens"


