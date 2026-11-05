# ----------------------Module
from fastapi import FastAPI, HTTPException, status, Path, Query
from typing import Optional
from datetime import datetime
from enum import Enum

# a = datetime.utcnow()

#----------------------Class
class CategoryEnum(str, Enum):
    tra_sua = "tra-sua"
    tra_trai_cay = "Trà Trái Cây"

# ----------------------Def

def find_item(menu , item_id):
    items = [item for item in menu if item['id'] == item_id]
    if not items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy món")
    return items[0]

# --------------------Data
app = FastAPI()
menu = [
    {"id": 1, "name": "Trà sữa trân châu", "price": 30000, "category": "tra-sua"},
    {"id": 2, "name": "Trà đào cam sả", "price": 35000, "category": "tra-trai-cay"},
    {"id": 3, "name": "Matcha latte", "price": 40000, "category": "tra-sua"},
]

#------------------Endpoint
@app.get("/home/{item_id}/category/{category_name}")
def get_item(item_id:int = Path(..., title="Item ID", description="Item ID lơn hơn hoặc bằng 10" , ge=1, le=100), category_name:str|None=None):
    return {
        "message": f"{item_id}-{category_name}"
    }



@app.get("/")
def home():
    return {
        "message": "Chào mừng các bạn đến quán trà sữa mini!"
    }

@app.get("/about")
def about_store():
    return {
        "name": "FullhouseDev",
        "address": "Online",
        "open": "19h"
    }



@app.get("/menu")
def get_menu(max_price: int = Query(100000, alias="mp", deprecated=True), category:CategoryEnum|None=None):
    result = menu
    if max_price:
        result = [item for item in result if item['price'] <= max_price]
    if category:
        result = [item for item in result if item['category'] == category.replace("_","-")]
    return result

@app.get("/menu/count")
def count_menu():
    return {
        "total": len(menu)
    }

@app.get("/menu/{item_id}")
def get_item_by_id(item_id:int):
    item = find_item(menu, item_id)
    return item

# @app.put("/menu/{item_id}")
# def update_item(item_id:int):
#     item = find_item(item_id)

@app.delete("/menu/{item_id}")
def delete_item(item_id:int):
    item = find_item(menu, item_id)
    menu.remove(item)
    return {
        "Message": f"Bạn đã xóa thành công món {item['name']}"
    }