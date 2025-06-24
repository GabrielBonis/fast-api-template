from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    hashed_password: str

class UserCreate(UserBase):
    hashed_password: str

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True
