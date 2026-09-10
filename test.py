# TODO Khai báo
# number = [] # Mảng rỗng
# number = [1,"python",3,4, [12,3,21]] #Mảng có giá trị

# number = (1,2,3)
# print(type(number))
# print(number)
# number_1 = list(number)
# print(number_1)
# print(type(number_1))

# number = "123"
# print(type(number))
# print(int(number))

# TODO Duyệt phần tử
# numbers = [1,23,4,5,6]
# # for number in numbers:
# #     print(number)
# # for index in range(len(numbers)):
# #     print(numbers[index])

# for index, value in enumerate(numbers):
#     print(f"{index}:{value}")

# TODO: Insert value
# numbers = [1,2,3,4,5,6]
# Append
# numbers.append(7)
# print(numbers)
# Insert
# Index nằm trong list sẽ thêm vào vị trí index
# Index mà nằm ngoài phạm vi của list, thì sẽ mặc định thêm vào cuối
# numbers.insert(8, 5)
# print(numbers)

# # TODO: Xóa phần tử
# numbers = [1,2,3,4,5,6]
# # Muốn xóa 1 phần tử trong list theo index và muốn giữ lại value
# # numbers.pop()
# # Khi dùng pop cần đảm bảo index nằm trong phạm vi của list
# number_deleted = numbers.pop(1)

# # Khi dùng remove, cần đảm bảo value có trong list
# # numbers.remove(9)

# # Mình sẽ xóa và không lấy giá trị
# del numbers[3]
# print(number_deleted)


# TODO: Các phương thức thao tác với list
# 1. Sort
"""
1. Các phần từ bên trong list cần là số
2. Nếu không thêm reverse sẽ sort theo thứ tự tăng dần và ngược lại
"""
# numbers = [1,2,3,3,5,6]
# numbers.sort(reverse=True)
# print(numbers)

# 2. reverse()
# numbers.reverse()
# print(numbers)

# 3. count()
# print(numbers.count(3)) => Đếm số phần tử trong một list
# print(len(numbers)) #=> Đếm xem list có bao nhiêu phần tử

#4. index() => Trả về vị trí đầu tiên mà nó tìm thấy
# numbers = [1,2,3,3,5,6]
# print(numbers.index(3))

# # 5. copy()
# num = 1
# num1 = num

# numbers = [1,2,3,3,5,6]
# number_copy = numbers.copy()
# number_copy.append(7)
# print(number_copy)
# print(numbers)

# #6. extend()
# numbers = [1,2,3,3,5,6]
# ext_number = [4,5,6,7]
# numbers.extend(ext_number)
# # numbers += ext_number
# print(numbers)

# # TODO: List comprehension
# #1. len()
# numbers = [1,2,4,3,5,0]
# # print(len(numbers))
# # print(sum(numbers))
# # print(max(numbers))
# # print(min(numbers))
# # print(sorted(numbers))
# # print(all(numbers)) => and, 1 => True, 2 => True.... 0=> False
# # print(any(numbers)) => or => False, 2 => True.... 0=> True



# TODO Tuple
# number = (1,2,3,3)
# print(type(number))
# Nếu tuple có 1 phần tử, thì cần thêm 1 dấu , ở cuối
# number = (1,2,3)
# number = tuple(number)
# print(number[:1])
# => Tuble có mọi đặc điểm của list ngoại trừ ko sửa được

# unpacking của tuble
# z, *y, x = (1,2,3,4,5,6)
# print(x, y, z)

# TODO: Set => Giống list nhưng không có index và giá trị giống nhau
# set_number = {1,2,3,5,4,3,4,3}
# list_number = [1,2,1,21,21,212,2,2,1]
# list_number = set(list_number)
# print(list_number)
# print(set_number)

# # 1. Thêm phần từ 
# set_number = {1,2,3,5,4,3,4,3}
# # set_number.add(["9",'9'])
# set_number.update(["10",'9'])
# print(set_number) # => Set là mutable


#  TODO Example
"""
QUẢN LÝ SINH VIÊN
Giả sử các em là người quản lý hệ thống hồ sơ của trường!
Giờ các em muốn quản lý điểm học sinh trên một app (quản lý toán lý hóa)

Đầu tiên các em cần tạo cho thầy một menu dạng như sau:
-----------------------------------------------
  Chào mừng bạn đến với app quản lý sinh viên!
-----------------------------------------------
Vui lòng chọn chức năng mà bạn mong muốn:
1. Thêm sinh viên mới
2. Xem thông tin sinh viên
3. Xóa sinh viên
4. Tạo bảng xếp hạng sinh viên
0. Thoát chương trình

Giải thích:
=> Khi các em nhập 1, càng em cần nhập các thông tin, MSSV, tên, tuổi, điểm toán, điểm lý, điểm hóa
=> Khi các em chọn 2, sẽ đổ ra toàn bộ thông tin của sinh viên 
----------------------------- > 8 : giỏi, 6-8 là khá , dưới 6 là trung bình
MSSV Họ và tên       Tuổi   Toán  Lý  Hóa Phân loại
1111 Phạm Ngọc Kiên  25     10    9   8   Giỏi
...
=> Khi các em chọn 3, sẽ yêu cầu nhập vào tên của sinh viên => Yêu cầu người dùng nhập vào MSSV, => xóa
=> Khi các em nhập 4 hiển thị lại sinh viên theo tổng điểm toán lý hóa, từ cao xuống thấp
=> Chỉ thoát chương trình khi bạn nhập số 0 => Xin chào, và hẹn gặp lại.

"""
[["Nguyễn văn a", 21],["Nguyễn Văn B",22]]
