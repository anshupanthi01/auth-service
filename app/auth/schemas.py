from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional, Annotated

class UserRegister(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email:  Annotated[EmailStr, Field(max_length=254)]
    password: str = Field(min_length=8)

class LoginRequest(BaseModel):
    username: str | None = Field(default=None, min_length=1, max_length=50) 
    email: Annotated[EmailStr, Field(max_length=254)]  | None = None
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type:str = "bearer"
 
class RefreshTokenRequest(BaseModel):
    refresh_token: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(min_length=8)

class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str = Field(min_length=8)

class EmailVerificationRequest(BaseModel):
    token: str

class UserRegisterResponse(TokenResponse):
    message: str = "User registered successfully!!"