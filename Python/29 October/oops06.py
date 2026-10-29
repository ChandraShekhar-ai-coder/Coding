from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, description="Password must be at least 8 characters long")
    full_name: str = Field(..., min_length=2, max_length=100)
    phone_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = Field(None, description="e.g. female, male, other, prefer_not_to_say")
    height_cm: Optional[float] = Field(None, ge=50, le=280)
class UserLogin(BaseModel):
    email: EmailStr
    password: str
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    refresh_token: Optional[str] = None
class RefreshTokenRequest(BaseModel):
    refresh_token: str
class TokenPayload(BaseModel):
    sub: str
    email: str
    exp: Optional[int] = None
class UserAuthResponse(BaseModel):
    id: str
    email: str
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    height_cm: Optional[float] = None
    is_active: bool = True
    created_at: datetime
    updated_at: datetime
    model_config = {"from_attributes": True}