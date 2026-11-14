from pydantic import BaseModel, ConfigDict
from app.models.user import UserRole

class UserBase(BaseModel):
    email: str
    is_active: bool = True

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.USER

class UserRead(UserBase):
    id: int
    role: UserRole

    model_config= ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: str |None=None
    role: str |None=None
    
