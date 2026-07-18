from __future__ import annotations
from sqlalchemy.ext.asyncio import AsyncSession
from app.users.model import User
from app.users.repository import UserRepository
from app.auth import schemas as s


class AuthService:
    """Business layer: rules + validations + transformations."""

    def __init__(self, user_repo: UserRepository, session: AsyncSession,):
        self.user_repo = user_repo
        self.session = session

    async def register(self, user_register: s.UserRegister) -> s.TokenResponse:
        pass
        # 1. Check username uniqueness.
        # 2. Check email uniqueness.
        # 3. Hash password. 
        # 4. Create User ORM object.
        # 5. Save through repository.
        # 6. Commit transaction.
        # 7. Refresh user.
        # 8. Generate access token.
        # 9. Generate refresh token.
        # 10. Return TokenResponse.
        