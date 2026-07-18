from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional, Annotated

class UserRegister(BaseModel):
    pass

class LoginRequest(BaseModel):
    pass

class TokenResponse(BaseModel):
    pass
 
class RefreshTokenRequest(BaseModel):
    pass

class ForgotPasswordRequest(BaseModel):
    pass

class ResetPasswordRequest(BaseModel):
    pass

class ChangePasswordRequest(BaseModel):
    pass

class EmailVerificationRequest(BaseModel):
    pass