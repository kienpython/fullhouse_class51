from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from core.database import Base, engine, get_db
from sqlalchemy.orm import Session
from services import sv_get_books, sv_create_book, sv_get_book
from schemas import sm_bookwrite, sm_bookread
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Quản lý thư viện cá nhân")

@app.get("/")
def welcome():
    return {
        "Message": "Chào mừng bạn đến với ứng dụng quản lý thư viện cá nhân của mình"
    }
@app.get("/books", response_model=List[sm_bookread])
def get_book(db:Session = Depends(get_db)):
    return sv_get_books(db)

@app.post("/books", response_model=sm_bookread, status_code=201)
def create_book(book_data:sm_bookwrite , db:Session=Depends(get_db)):
    book = sv_create_book(book_data=book_data, db=db )
    if not book:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Thêm thất bại!")
    return book

@app.get("/books/{book_id}", response_model=sm_bookread)
def get_book(book_id:int, db:Session=Depends(get_db)):
    book = sv_get_book(db=db, book_id=book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy quyển sách bạn muốn!")
    return book