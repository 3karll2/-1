from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=1, le=120)

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=1, le=120)

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    age: int

    class Config:
        from_attributes = True