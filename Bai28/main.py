# Chua cac endpoint
from database import Base, engine
from fastapi import FastAPI
from routers import home_router, users_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(home_router)
app.include_router(users_router)

