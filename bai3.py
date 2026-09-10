# if elif else....

a = 500
b = 100

"""
1. Cấu trúc điều kiện đầy đủ:
if điều_kiện:
    ....
elif điều_kiện:
    ....
else:
    ....

2. Mk có thể sử dụng từng phần
Vd: 
number = 500
# Kiểm tra xem số vừa nhập có lớn hơn 200 không, nếu có thì in ra, nếu không thì không xử lý gì.
if number > 200:
    print(number)
# Kiểm tra xem số vừa nhập có lớn hơn 200 không, nếu có thì in ra, nếu không thì báo là không lớn hơn 200
if number > 200:
    print(number)
else:
    print("Không lớn hơn 200!")
# Kiểm tra xem số vừa nhập và kiểm tra, nếu lớn 200 thì in ra lớn hơn, nhỏ hơn 200 thì in ra nhỏ hơn, còn không thì bằng

"""
# if a > 200: 
#     print("a lớn hơn 200!")

# if a > 300:
#     print("a lớn hơn 300!")

# elif a == b:
#     print("a bằng b!")
# elif a > b :
#     print("a lớn hơn b!")
# else:
#     print("a lớn hơn b===!")


# Kiểm tra chẵn lẻ
# a = 200
# if a % 2 == 0:
#     print("Đây là số chẵn!")
# else:
#     print("Đây là số lẻ!")


"""
Lớp mk có tổng cộng là 10 sinh viên, hôm nay số lượng sinh viên tham gia học là 8. Gửi thông báo về cho giáo viên biết là nay lớp có đủ sinh viên đi học không? nếu thiếu thì thiếu mấy người.
"""

""
# number = 500
# check = True if a > 200 else False
# if a > 200:
#     check = True
# else:
#     check = False

"Kiểm tra xem 1 số mk nhập vào có lớn hơn 200 và nhỏ hơn 500 không"
a = 300
# if a >= 200 and a <= 500:
#     print(a)
"""Kiểm tra tính năng đăng nhập:

Nhập vào username + password
check username có tồn tại trong CSDL: []
check password nó có đúng username đó không?
check active có == True không
"""

# usernames = ['kien', 'vy', 'quang']
# passwords = ['123', '456', '789']
# username = input("Nhập vào username: ")
# password = input("Nhập vào password: ")
# status = True
# if not (username in usernames):
#     pass
# if not(password in passwords):
#     pass

# status = True
# if status: 
#     print("Login thành công!")
# status = 1
# if status: 
#     print("Login thành công!")
# status = 2
# if status: 
#     print("Login thành công!")
# status = -1
# if status: 
#     print("Login thành công!")
# status = 0
# if status: 
#     print("Login thành công!")
# status = []
# if status: 
#     print("Login thành công!")
# => 0 = [] = False khi kiểm tra điều kiện

number = 500
if number < 400:
    print("Lớn hơn")
print("Bé hơn")
