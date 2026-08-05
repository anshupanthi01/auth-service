from __future__ import annotations
from sqlalchemy import String, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship 
from app.database.database import Base 
from datetime import datetime
from app.users.model import User

class RefreshToken(Base):
    __tablename__ = "refresh_token"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable= False)
    token_hash: Mapped[str] = mapped_column(String(200), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now, nullable= False)
    last_used_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable= False)
    revoked_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable= False)
    user: Mapped[User] = relationship(back_populates="users")