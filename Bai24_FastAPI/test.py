from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = [
    {
        "name": "123",
        "classes": 51,
        'subjects': ["Toán", "Lý", "Hóa"]
    },
    {
            "name": "Phạm Ngọc Kiên2",
            "classes": 52,
            'subjects': ["Toán"]
    }
    ,
    {
        "name": "Phạm Ngọc Kiên4",
        "classes": 53,
        'subjects': ["Toán"]
        }

]

class UserCreate(BaseModel):
    name:str
    classes:int
    subject:object

#TODO: POST 
@app.post("/user")
def create_user(user:UserCreate):
    users.append(user) 
    return users[0]

# TODO: GET
@app.get("/user/{user_name}")
def get_user(user_name:str):
    for user in users:
        if user['name'] == user_name:
            return user

#TODO: DELETE
@app.delete("/user/{user_name}")
def delete_user(user_name:str):
    for user in users:
        if user['name'] == user_name:
            users.remove(user)
    return users
#TODO: Handle get

@app.get('/home')
def hello_world():
    return {
        "message":"Hello World!"
    }

@app.get('/class/{user_id}')
def get_class(user_id:int):
    # print(user_id)
    # print(type(user_id))
    class_user = []
    for user in users:
        if user['class'] == user_id:
            class_user.append(user)
    return class_user

# Tìm học sinh theo môn học
@app.get('/subject/{sj_id}')
def get_class(sj_id:str):
    sj_user = []
    for user in users:
        if sj_id.title() in user['subjects']:
            sj_user.append(user)
    return sj_user
