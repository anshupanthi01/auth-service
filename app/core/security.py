from datetime import datetime, timedelta, timezone
from authlib.jose import jwt, JoseError
from app.core.config import settings as s
from typing import Any
from passlib.context import CryptContext
from app.core.exceptions import InvalidTokenError
import secrets
import hashlib

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# --------------- Password -------------------

def hash_password(password: str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str)->bool:
    return pwd_context.verify(plain_password, hashed_password)

# --------------- Refresh Token -------------------

def create_refresh_token()-> str:
    return secrets.token_urlsafe(64)

def hash_refresh_token(token: str)-> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()

"""Why SHA-256 instead of bcrypt?
    SHA-256 is a good fit because it is:
    Fast
    Deterministic
    Widely used for hashing opaque tokens"""

# --------------- Access Token -------------------

def create_access_token( 
        data: dict[str, Any], 
        expires_delta: timedelta | None = None ) -> str:
    
    payload = data.copy()

    if expires_delta is None:
        expires_delta = timedelta(
            minutes=s.ACCESS_TOKEN_EXPIRE_MINUTES
            )
    now = datetime.now(timezone.utc)
    payload.update(
        {
            "exp": now + expires_delta,
            "iat": now,
            "type": "access"
        }
    )

    return jwt.encode(
        {"alg": s.ALGORITHM},
        payload= payload,
        key= s.SECRET_KEY.get_secret_value()
    )

def decode_access_token(token: str) -> dict[str, Any]:
    try:
        claims = jwt.decode(
            token,
            s.SECRET_KEY.get_secret_value()
            )
        claims.validate()

        if claims.get("type") != "access":
            raise InvalidTokenError(
                description="Expected access token"
                )
        
        subject = claims.get("sub")
        if subject is None:
            raise InvalidTokenError(
                    description="Token missing subject"
                )
        return dict(claims)
            
    except JoseError:
        raise InvalidTokenError(
            description= "Invalid or expired token"
        )
    


