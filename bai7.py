# TODO: Create dict

# 1. Khai báo trực tiếp
# number = [1,2,34,5]
# print(number[0])
# number_dict = {
#     "ten": "Phạm Ngọc Kiên",
#     "lop":'class 51'
# }

# 2. Thông qua hàm zip
# keys = ['ten', 'class']
# values = ["Phạm Ngọc Kiên", "class_51"]
# dict_data = dict(zip(keys, values))
# print(dict_data)

#3 Chuyển từ list sang dict
# value_1 = ["ten", "Phạm Ngọc Kiên"]
# value_2 = ["class", "class_51"]
# d = dict([value_1,value_2])
# print(d)

# # 4. fromkeys
# keys = ['ten','class']
# d = dict.fromkeys(keys, "test")
# print(d)

# TODO Get Values
# number_dict = {
#     "ten": "Phạm Ngọc Kiên",
#     "lop":'class 51'
# }
# # 1. Dựa vào key
# # print(number_dict['ten'])
# # print(number_dict['ten1'])
# # 2. Sử dụng hàm get()
# print(number_dict.get("ten1", "Phạm Ngọc Kiên 1"))

# TODO: Duyệt qua dict
# List có mấy cách duyệt
# 1. Duyệt qua values: for value in values:
# 2. Duyệt qua index: for index in range(len(list)):
# 3. Duyệt qua cả index và value : for index, value in enumerate(list)

# Dict có 3 cách duyệt tương ứng
# 1. Duyệt qua values: for value in dict_data.values():
# 2. Duyệt qua keys: for key in dict_data.keys():
# 3. Duyệt qua cặp key, value: for key, value in dict_data.items():

# dict_data = {
#     "ten": "Phạm Ngọc Kiên",
#     "lop":'class 51'
# }

# 1.
# for value in dict_data.values():
#     print(value)

# 2.
# for key in dict_data.keys():
#     print(f"{key}-{dict_data[key]}")

# 3.
# for key, value in dict_data.items():
#     print(f"{key}-{value}")


# TODO: Thêm, sửa dict
# dict_data = {
#     "ten": "Phạm Ngọc Kiên",
#     "lop":'class 51'
# }
# 1. Thêm data vào dict
# dict_data["tuoi"] = 25
# print(dict_data)

# # 2. Update data 
# dict_data['ten'] = "Phạm Ngọc Kiên 1"
# print(dict_data)

# TODO: Xóa data
# dict_data = {
#     "ten": "Phạm Ngọc Kiên",
#     "lop":'class 51'
# }

# 1. pop() => Xóa data và trả về value của data đó
# ten = dict_data.pop("ten") 
# print(dict_data)
# print(ten)

# 2. del() => Xóa data nhưng không trả về giá trị
# del dict_data["ten"]
# print(dict_data)

# 3. popitem() => Xóa phần tử cuối cùng trong dict
# key, value = dict_data.popitem()
# print(dict_data)
# print(key, value)

# 4. clear()
# dict_data.clear()
# print(dict_data)

# TODO: Kiểm tra key và values, trộn dictionary
dict_data = {
    "ten": "Phạm Ngọc Kiên",
    "lop":'class 51'
}
# 1. Kiểm tra key có tồn tại trong dict
# print("lop1" in dict_data)

# 2. Kiêm tra value có tồn tại trong dict không
# print("class 51" in dict_data.values())

# 3. Trộn 2 dictionary
# dict_data = {
#     "ten": "Phạm Ngọc Kiên",
#     "lop":'class 51'
# }
# dict_data_add = {
#     "tuoi": 25
# }
# dict_data.update(dict_data_add)
# print(dict_data)

# TODO: Kiến thức bổ sung: key => bắt buộc phải là một immutable , value là kiểu dữ liệu gì cũng được
# dict_data = {
#     "ten": {
#         "first_name":"Pham",
#         "last_name":"Kien"
#     },
#     "tuoi": [1,2,3,4],
#     "lop": ("class 51", "class 52")
# }

#--------------
# dict_data => dict => lấy value thông qua key
# dict_data['lop] => tuple => lay value thong qua index
# lop_data = dict_data["lop"]
# dict_data["lop"] = ("class 51", "class 53")
# print(lop_data)


# dict_data = {
#     "tuoi": 25
# }
# dict_data["tuoi"] = dict_data['tuoi'] + 1
# print(dict_data)


# # TODO: Comprehension
# numbers = [1,2,3,4,5]
# dict_numbers = {}
# # for number in numbers:
# #     dict_numbers[number] = number**2
# # print(dict_numbers)

# dict_numbers = {number:number**2 for number in numbers}
# print(dict_numbers)

# TODO Example
# dict_data = {
#     1: "abc",
#     True: "bcd"
# }
# print(len(dict_data))
# print(dict_data)

d = {'a':1, "b":2}
print(d['c'])

