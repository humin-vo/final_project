from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    phone_number: str

class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True
