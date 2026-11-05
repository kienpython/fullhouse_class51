# Các pydantic xử input và output

from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email:str
    age: int | None = Field(None, ge=0, le=120)

class UserRead(UserCreate):
    id: int
    is_active:bool
    class config:
        from_attributes = True