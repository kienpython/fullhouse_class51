# database -> models -> schemas -> serviecs -> main
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:Kientkls01@localhost:3306/bai2_database"

engine = create_engine(DATABASE_URL)

SesionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()