from sqlalchemy import Column, Integer, String
from core.database import Base
class Book(Base):
    __tablename__ = "Books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    quantity = Column(Integer, default=0)

    # class config:
    #     from_attributes = True
