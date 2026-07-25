from datetime import datetime, timedelta, timezone
from authlib.jose import jwt, JoseError
from app.core.config import settings as s
from typing import Any, Literal
from passlib.context import CryptContext
from app.core.exceptions import InvalidTokenError

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_password(password: str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str)->bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_token( 
        data: dict[str, Any], 
        token_type: Literal["access", "refresh"], 
        expires_delta: timedelta | None = None ) -> str:
    
    payload = data.copy()

    if expires_delta is None:
        if token_type == "access":
            expires_delta = timedelta(
                minutes=s.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        else:
            expires_delta = timedelta(
                days=s.REFRESH_TOKEN_EXPIRE_DAYS
            )
    now = datetime.now(timezone.utc)
    payload.update(
        {
            "exp": now + expires_delta,
            "iat": now,
            "type": token_type
        }
    )

    return jwt.encode(
        {"alg": s.ALGORITHM},
        payload= payload,
        key= s.SECRET_KEY.get_secret_value()
    )

def decode_token(
        token: str, 
        expected_type: Literal["access", "refresh"]) -> dict[str, Any]:
    try:
        claims = jwt.decode(
            token,
            s.SECRET_KEY.get_secret_value()
            )
        claims.validate()
        if claims.get("type") != expected_type:
            raise InvalidTokenError(
                description=f"Expected {expected_type} token"
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
    


