from pydantic import BaseModel, EmailStr
from typing import Optional

class EmergencyContact(BaseModel):
    name: str
    phone: str

class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int
    religion: Optional[str] = None
    emergency_contact: EmergencyContact

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None