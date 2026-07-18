from datetime import datetime, timedelta, timezone
from authlib.jose import jwt
from app.core.config import settings as s
from typing import Any

def create_access_token(
    data: dict[str, Any],
    expires_delta: timedelta | None = None,
) -> str:
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + (
        expires_delta
        if expires_delta
        else timedelta(minutes= s.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    to_encode.update(
        {
            "exp": expire,
            "iat": datetime.now(timezone.utc),
        }
    )

    return jwt.encode(
        to_encode,
        s.SECRET_KEY.get_secret_value(),
        algorithm= s.algorithm,
    )


def decode_access_token(token: str) -> dict[str, Any]:
    return jwt.decode(
        token,
        s.SECRET_KEY.get_secret_value(),
        algorithms=[s.algorithm],
    )

