# TODO: Convert file json to dict
# import json

# with open("../test_json_data.json","r", encoding="utf-8") as f:
#     data = json.load(f)
# print(data['name'])
# print(type(data))

# TODO: Convert dict to json
# import json
# student = {
#     "id": 1111,
#     "name": "Phạm Ngọc Kiên",
#     "class": "Class 51"
# }

# with open("json_data.json", 'w', encoding='utf-8') as f:
#     json.dump(student, f, ensure_ascii=False, indent=7, sort_keys=True, separators=(",",": "))

# # TODO: Try except
# import json
# try:
#     pass
# except FileNotFoundError as fnf:
#     pass
# except json.JSONDecodeError as jde:
#     pass
# except Exception as e:
#     pass


# TODO: Example
import json

def check_empty(path):
    try:
        with open(path,'r',encoding='utf-8') as user:
            if not user.read(1):
                return True
    except:
        print("Hệ thông đang gặp chút sự cố, vui lòng thử lại sau!")
        return 1
def load_users(path):
    is_empty = check_empty(path)
    if is_empty == 1:
        return None
    if is_empty:
        with open(path, 'w', encoding="utf-8") as user:
            json.dump({"users": []}, user, ensure_ascii=False)
            return {"users": []}
    else: 
        with open(path,'r',encoding='utf-8') as user:
            return json.load(user)

def save_users(data, path):
    with open(path, 'w', encoding="utf-8") as user:
        json.dump(data, user, ensure_ascii=False)
        print("Tài khoản của bạn đã được đăng ký")

def check_exits(users, username):
    for user in users:
        if user['username'] == username:
            print("Username đã tồn tại!")
            return True
    return False
def register(path):
    username = input("Nhập vào username: ")
    password = input("Nhập vào password: ")
    full_name = input("Nhập vào fullname: ")
    login_count = 0
    old_data = load_users(path)
    if not old_data:
        return
    # TODO: Xử lý username tồn tại
    if check_exits(old_data['users'], username):
        return
    # TODO: Password phải lớn hơn 6 ký tự
    if len(password) < 6:
        print("Password phải có ít nhất 6 ký tự")
        return

    # TODO: Không được để trường nào trống
    if not username or not full_name:
        print("Không trường nào được để trống!")

    new_account = {
        "username": username, 
        "password": password,
        "fullname": full_name, 
        "login_count": login_count
    }
    old_data['users'].append(new_account)
    save_users(old_data, path)

path = 'users.json'
# print(load_users(path))
register(path)
