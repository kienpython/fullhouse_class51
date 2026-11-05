from sqlalchemy.orm import Session
from models import User
from schemas import UserRead, UserCreate

def get_user(db:Session, user_id:int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db:Session, user:UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    # print(db_user.id)
    db.refresh(db_user)
    # print(db_user.id)
    return db_user

def delete_user(db:Session, user_id:int):
    user = get_user(user_id)
    if user:
        db.delete(user)
        db.commit()
    return user
