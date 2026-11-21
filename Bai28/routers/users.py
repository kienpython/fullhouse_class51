from services.user import create_user as cu
from schemas import UserCreate
from sqlalchemy.orm import Session
from database import get_db
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/users", tags=["Users"])
@router.post("/")
def create_user(user:UserCreate, db:Session=Depends(get_db)):
    return cu(db=db, user=user)