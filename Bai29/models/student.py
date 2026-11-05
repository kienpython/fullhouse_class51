from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(200), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    course = relationship("Course", back_populates="students")