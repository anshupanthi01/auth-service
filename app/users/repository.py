from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.users.model import User

# Repository returns ORM entities.
class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session=session

    async def find_by_id(self, user_id: int)->Optional[User]:
        result = await self.session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
    
    async def find_by_username(self, username: str)-> Optional[User]:
        result = await self.session.execute(select(User).where(User.username == username))
        return result.scalar_one_or_none()
    
    async def find_by_email(self, email: str)->Optional[User]:
        result = await self.session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()
    
    def create(self, user: User)-> User:
        self.session.add(user)
        return user