from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.course import CourseCreate, CourseRead
from database import Base, engine, get_db
from services.course import get_course as gc, get_courses as gcs, create_course as cc, update_course as uc, delete_course as dc
from models.student import Student
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Course Management API")

@app.post("/courses", response_model=CourseRead, status_code=201)
def create_course(course:CourseCreate ,db: Session=Depends(get_db)):
    return cc(db=db, course=course)

@app.get("/courses", response_model=List[CourseRead])
def get_courses(skip:int =0 ,limit:int = 100 ,db:Session = Depends(get_db)):
    return gcs(skip=skip, limit=limit, db=db)

@app.get("/courses/{course_id}", response_model=CourseRead)
def get_course(course_id:int , db:Session = Depends(get_db)):
    return gc(course_id=course_id, db = db)

@app.put("/courses/{course_id}", response_model=CourseRead)
def update_course(course_id: int, course_update:CourseCreate, db:Session=Depends(get_db)):
    db_course = uc(db=db, course_id=course_id, course_update=course_update)
    if not db_course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Khong tim thay du lieu")
    return db_course

@app.delete("/courses/{course_id}", response_model=CourseRead)
def delete_course(course_id: int, db:Session=Depends(get_db)):
    db_course = dc(db=db, course_id=course_id)
    if not db_course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Khong tim thay du lieu")
    return db_course