from __future__ import annotations
from sqlalchemy.ext.asyncio import AsyncSession
from app.users.model import User
from app.users.repository import UserRepository
from app.auth import schemas as s
from app import exceptions as exp
from app.core.security import hash_password
from app.core.security import create_token
from app.core.config import settings
from app.core.security import verify_password
from app.core.enums import UserStatus
from datetime import datetime, timezone

class AuthService:
    """Business layer: rules + validations + transformations."""

    def __init__(self, user_repo: UserRepository, session: AsyncSession,):
        self.user_repo = user_repo
        self.session = session

    async def register(self, user_register: s.UserRegister) -> s.RegisterResponse:
        # Normalize identifier first
        username = user_register.username.strip()
        email = user_register.email.lower().strip()
        # 1. Check username uniqueness.
        existing_user = await self.user_repo.find_by_username(username)
        if existing_user:
            raise exp.UsernameAlreadyExistsError("Username already exists.")
        # 2. Check email uniqueness.
        existing_email = await self.user_repo.find_by_email(email)
        if existing_email:
            raise exp.EmailAlreadyExistsError("Email already in use.")
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
        payload = {
            "sub": str(user.id),
            "role": user.role.value,
            }
        access_token = create_token(
            data=payload,
            token_type="access"
            )
        # 9. Generate refresh token.
        refresh_token = create_token(
            data=payload,
            token_type="refresh"
            )
        # 10. Return RegisterResponse.
        return s.RegisterResponse(
            access_token=access_token,
            refresh_token= refresh_token,
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
            )
    
    def _check_account_status(self, user:User)->None:
            if user.status == UserStatus.PENDING_VERIFICATION:
                raise exp.UserVerificationPending()
            
            if user.status == UserStatus.SUSPENDED:
                raise exp.UserAccountSuspended()
            
            if user.status == UserStatus.DELETED:
                raise exp.AccountDeleted()

    async def login(self, user_login: s.LoginRequest) -> s.LoginResponse:
        # Normalize identifier first
        username = user_login.username.strip() if user_login.username else None
        email = user_login.email.lower().strip() if user_login.email else None
        password = user_login.password
        # Find the user and verify password:
        if bool(username) == bool(email):
            raise exp.InvalidCredentialsError()
        
        if username:
            user = await self.user_repo.find_by_username(username)
        elif email:
            user = await self.user_repo.find_by_email(email)

        if not user:
            raise exp.InvalidCredentialsError()
        
        is_valid = verify_password(password, user.password_hash)
        if not is_valid:
            raise exp.InvalidCredentialsError()
        # Check account status
        self._check_account_status(user)

        # Update last login
        user.last_login = datetime.now(timezone.utc)

        # commit
        try:
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise

        # Generate access and refresh token
        payload = {
            "sub": str(user.id),
            "role": user.role.value,
            }
        access_token = create_token(
            data=payload,
            token_type="access"
            )
        refresh_token = create_token(
            data=payload,
            token_type="refresh"
            )

        # Return LoginResponse
        return s.LoginResponse(
            access_token=access_token,
            refresh_token= refresh_token,
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
            )





