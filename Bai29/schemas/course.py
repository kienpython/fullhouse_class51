from pydantic import BaseModel, Field

class CourseCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)
    price: int = Field(..., ge=0)

class CourseRead(CourseCreate):
    id: int
    is_published: bool
    class Config:
        from_attributes = True

