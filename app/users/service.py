from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from app.users.model import User
from app.users.repository import UserRepository
from app.users.schema import UserUpdate
from app.users.exceptions import UserNotFoundError, UsernameAlreadyExists, EmailAlreadyInUse

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
        if user_update.username is not None and user_update.username != user.username:
            existing_username = await self.user_repo.find_by_username(user_update.username)
            if existing_username is not None:
                raise UsernameAlreadyExists("Username already exist.")

        # 3. Check email duplication (if email is being changed)
        email_changed = False
        if user_update.email is not None and user_update.email != user.email:
            existing_email = await self.user_repo.find_by_email(user_update.email)
            if existing_email is not None:
                raise EmailAlreadyInUse("Email already in use.")
            email_changed = True

        # 4. Update only the provided fields
        if user_update.username is not None:
            user.username = user_update.username
        if user_update.email is not None:
            user.email = user_update.email

        if email_changed:
            user.email_verified = False
            user.email_verified_at = None

        await self.session.commit()
        await self.session.refresh(user)
        return user