from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional, Annotated

class UserRegister(BaseModel):
    username: str
    email: EmailStr 
    password: str 

class LoginRequest(BaseModel):
    # username: str 
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    acess_token: str
    refresh_token: str
    token_type:str = "bearer"
 
class RefreshTokenRequest(BaseModel):
    refresh_token: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    token: str
    new_pasword: str

class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str

class EmailVerificationRequest(BaseModel):
    token: str