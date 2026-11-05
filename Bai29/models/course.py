from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from database import Base
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    price = Column(Integer, nullable=False)
    is_published = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    students = relationship("Student", back_populates="course")
