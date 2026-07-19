from datetime import datetime, timedelta, timezone
from authlib.jose import jwt, JoseError
from app.core.config import settings as s
from typing import Any
from passlib.context import CryptContext
from exceptions import InvalidTokenError

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_password(password: str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str)->bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token( data: dict[str, Any], expires_delta: timedelta | None = None ) -> str:
    payload = data.copy()

    expire = datetime.now(timezone.utc) + (
        expires_delta
        if expires_delta
        else timedelta(minutes= s.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    payload.update(
        {
            "exp": expire,
            "iat": datetime.now(timezone.utc),
        }
    )

    return jwt.encode(
        algorithm= s.algorithm,
        payload= payload,
        key= s.SECRET_KEY.get_secret_value()
    )


def decode_token(token: str) -> dict[str, Any]:
    try:
        claims = jwt.decode(
        token, 
        s.SECRET_KEY.get_secret_value())
        claims.validate()
        return claims
    except JoseError:
        raise InvalidTokenError(
            description= "Invalid or expired token"
        )


