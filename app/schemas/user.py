from pydantic import BaseModel, EmailStr, Field
import uuid
from datetime import datetime
from typing import Optional

# Shared properties
class UserBase(BaseModel):
    email: EmailStr = Field(..., example="user@example.com")
    is_active: Optional[bool] = True
    is_superuser: bool = False # Optional

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str = Field(..., min_length=8, example="strongpassword")

# Properties to receive via API on update (optional)
class UserUpdate(UserBase):
    password: Optional[str] = Field(None, min_length=8, example="newstrongpassword")
    email: Optional[EmailStr] = None # Allow email update? Consider implications
    is_active: Optional[bool] = None

# Properties stored in DB (never expose password)
class UserInDBBase(UserBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str

# Properties to return to client
class User(UserInDBBase):
    pass # Excludes hashed_password by default