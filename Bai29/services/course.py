from sqlalchemy.orm import Session
from models.course import Course
from schemas.course import CourseCreate
from typing import Optional

def create_course(db:Session, course:CourseCreate) -> Course:
    db_course = Course(title = course.title, price = course.price)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_courses(db:Session, skip:int = 0, limit: int = 100) -> list[Course]:
    return db.query(Course).offset(skip).limit(limit).all()

def get_course(db:Session, course_id:int) -> Optional[Course]:
    return db.query(Course).filter(Course.id == course_id).first()

def update_course(db:Session, course_id:int, course_update: CourseCreate) -> Optional[Course]:
    db_course = get_course(db, course_id)
    if not db_course:
        return None
    db_course.title = course_update.title
    db_course.price = course_update.price
    db.commit()
    db.refresh(db_course)
    return db_course

def delete_course(db:Session, course_id:int) -> Optional[Course]:
    db_course = get_course(db, course_id)
    if not db_course:
        return None
    db.delete(db_course)
    db.commit()
    return db_course
    
