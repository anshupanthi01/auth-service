from app.users.repository import UserRepository as Repo
from app.users.model import User
from app.users.schema import UserProfileResponse, UserUpdate
from sqlalchemy.ext.asyncio import AsyncSession

class UserAlreadyExistsError(Exception):
    pass

class UserService:
    def __init__(self, user_repo: Repo, session: AsyncSession):
        self.user_repo = user_repo
        self.session = session
