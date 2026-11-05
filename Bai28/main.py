# Chua cac endpoint
from database import Base, engine, get_db
from models import User, Subject
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from services.user import create_user as cu, get_user
from schemas import UserCreate, UserRead
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/home")
def home():
    return {
        "Message": 'Home'
    }

@app.post("/users")
def create_user(user:UserCreate, db:Session=Depends(get_db)):
    return cu(db=db, user=user)