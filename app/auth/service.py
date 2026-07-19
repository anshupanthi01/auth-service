from __future__ import annotations
from sqlalchemy.ext.asyncio import AsyncSession
from app.users.model import User
from app.users.repository import UserRepository
from app.auth import schemas as s
from app.exceptions import UsernameAlreadyExistsError, EmailAlreadyExistsError
from app.core.security import hash_password
from app.core.security import create_token

class AuthService:
    """Business layer: rules + validations + transformations."""

    def __init__(self, user_repo: UserRepository, session: AsyncSession,):
        self.user_repo = user_repo
        self.session = session

    async def register(self, user_register: s.UserRegister) -> s.RegisterResponse:
        username = user_register.username.strip()
        email = user_register.email.lower().strip()

        # 1. Check username uniqueness.
        existing_user = await self.user_repo.find_by_username(username)
        if existing_user:
            raise UsernameAlreadyExistsError()
        # 2. Check email uniqueness.
        existing_email = await self.user_repo.find_by_email(email)
        if existing_email:
            raise EmailAlreadyExistsError()
        # 3. Hash password. 
        password_hash = hash_password(user_register.password)
        # 4. Create User ORM object.
        user = User(
            username = username,
            email = email,
            password_hash = password_hash
        )
        # 5. Save through repository.
        self.user_repo.create(user)           
        # 6. Commit transaction.
        try:
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise

        # 7. Refresh user.
        await self.session.refresh(user)     

        # 8. Generate access token.
        access_token = create_token(
            data={"sub": str(user.id)},
            token_type="access",
            
            )
        # 9. Generate refresh token.
        refresh_token = create_token(
            data={"sub": str(user.id)},
            token_type="refresh"
            )

        # 10. Return RegisterResponse.
        return s.RegisterResponse(
            access_token=access_token,
            refresh_token= refresh_token,
            )
        