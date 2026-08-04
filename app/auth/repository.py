from sqlalchemy.ext.asyncio import AsyncSession
from app.users.model import RefreshToken

class RefreshTokenRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    def create(self, token: RefreshToken)->RefreshToken:
        self.session.add(token)
        return token

    async def find_by_hash(self, token_hash: str)-> RefreshToken | None:
        pass

    async def revoke(self, token: RefreshToken)-> None:
        pass

    async def revoke_all_for_user(self, user_id: int)-> None:
        pass

    async def find_active_by_user(self, user_id: int)-> list[RefreshToken]:
        pass

    async def delete_one(self, token: RefreshToken)-> None:
        pass

    async def delete_expired():
        pass

    async def delete_all_for_user():
        pass
    