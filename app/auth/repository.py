from sqlalchemy.ext.asyncio import AsyncSession
from app.users.model import RefreshToken

class RefreshTokenRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, refresh_token: RefreshToken)->RefreshToken:
        self.session.add(refresh_token)
        return refresh_token

    async def find_by_hash():
        pass

    async def revoke():
        pass

    async def delete_expired():
        pass

    async def delete_all_for_user():
        pass
    
    async def delete_one():
        pass