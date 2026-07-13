from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional, Annotated
from app.core.enums import UserRole, UserStatus

class UserProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username:str = Field(min_length=1, max_length=50)
    email: Annotated[EmailStr, Field(max_length=200)]
    role: UserRole
    status: UserStatus
    created_at: datetime
    last_login: Optional[datetime] = None
    updated_at: datetime

class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=1, max_length=50)
    email: EmailStr | None = Field(default=None, max_length=200)

