from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.model import RefreshToken
from sqlalchemy import select, delete, update
from datetime import datetime, timezone

class RefreshTokenRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    def create(self, token: RefreshToken)->RefreshToken:    # A user logs in and you create a new refresh token.
        self.session.add(token)
        return token

    async def find_by_hash(self, token_hash: str)-> RefreshToken | None:    # Finds a refresh token by its hashed value.
        stmt = select(RefreshToken).where(RefreshToken.token_hash == token_hash)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def revoke(self, token: RefreshToken)-> None:     # Marks one loaded refresh token as revoked eg. User logs out from one device.
        token.revoked_at= datetime.now(timezone.utc)

    async def revoke_all_for_user(self, user_id: int)-> None:   # Revokes every active refresh token belonging to a user.
        stmt = (update(RefreshToken).where(
            RefreshToken.user_id == user_id, 
            RefreshToken.revoked_at.is_(None)).values(revoked_at= datetime.now(timezone.utc)))
        await self.session.execute(stmt)

    async def find_active_by_user(self, user_id: int) -> list[RefreshToken]:
        now = datetime.now(timezone.utc)

        stmt = (
            select(RefreshToken)
            .where(
                RefreshToken.user_id == user_id,
                RefreshToken.revoked_at.is_(None),
                RefreshToken.expires_at > now
            )
        )
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def delete_one(self, token: RefreshToken) -> None:
        await self.session.delete(token)

    async def delete_expired(self) -> None:
        stmt = delete(RefreshToken).where(
            RefreshToken.expires_at <= datetime.now(timezone.utc)
        )
        await self.session.execute(stmt)

    async def delete_all_for_user(self, user_id: int) -> None:
        stmt = delete(RefreshToken).where(
            RefreshToken.user_id == user_id
        )
        await self.session.execute(stmt)

    async def find_active_by_hash(
            self,
            token_hash: str,
            ) -> RefreshToken | None:
        stmt = (
        select(RefreshToken)
        .where(
            RefreshToken.token_hash == token_hash,
            RefreshToken.revoked_at.is_(None),
            RefreshToken.expires_at > datetime.now(timezone.utc),
            )
            )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    