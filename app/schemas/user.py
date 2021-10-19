from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = True


class UserCreate(UserBase):
    first_name: str
    last_name: str


class User(UserBase):
    first_name: str
    last_name: str
    email: str
    is_active: bool
