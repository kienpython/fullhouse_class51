# phần chưa các models trong database
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy.sql import func
from database import Base
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True)
    age = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    create_at = Column(DateTime, server_default=func.now())