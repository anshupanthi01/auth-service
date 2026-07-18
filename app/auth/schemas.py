from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Annotated, Literal

class UserRegister(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email:  Annotated[EmailStr, Field(max_length=254)]
    password: str = Field(min_length=8, max_length=128)


class LoginRequest(BaseModel):
    username: str | None = Field(default=None, min_length=3, max_length=50) 
    email: Annotated[EmailStr, Field(max_length=254)]  | None = None
    password: str = Field(min_length=8, max_length=128)

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type:Literal["Bearer"] = "bearer"
    expires_in: int

class RegisterResponse(TokenResponse):
    pass

class LoginResponse(TokenResponse):
    pass

class RefreshTokenRequest(BaseModel):
    refresh_token: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    reset_token: str
    new_password: str = Field(min_length=8, max_length=128)

class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str = Field(min_length=8, max_length=128)

class EmailVerificationRequest(BaseModel):
    verification_token: str

class LogoutRequest(BaseModel):
    refresh_token: str