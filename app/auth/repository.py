from sqlalchemy.ext.asyncio import AsyncSession

class RefreshTokenRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create():
        pass

    async def find_by_hash():
        pass
    async def revoke():
        pass
    async def delete_expired():
        pass