from fastapi import FastAPI
from database import Base, engine
from routers import courses

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Course Management API")

app.include_router(courses.router)