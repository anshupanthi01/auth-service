from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from app.users.model import User
from app.users.repository import UserRepository
from app.users.schema import UserUpdate


class UserNotFoundError(Exception):
    pass


class UserService:
    def __init__(self, user_repo: UserRepository, session: AsyncSession):
        self.user_repo = user_repo
        self.session = session

    async def get_my_profile(self, current_user_id: int) -> User:
        user = await self.user_repo.find_by_id(current_user_id)

        if user is None:
            raise UserNotFoundError("User not found.")

        return user

    async def update_profile(
        self,
        current_user_id: int,
        user_update: UserUpdate,
    ) -> User:
        # 1. Load the current user
        user = await self.user_repo.find_by_id(current_user_id)

        if user is None:
            raise UserNotFoundError("User not found.")

        # 2. Check username duplication (if username is being changed)

        # 3. Check email duplication (if email is being changed)

        # 4. Update only the provided fields

        # 5. Commit the transaction

        # 6. Refresh the ORM object

        # 7. Return the updated user
        return user