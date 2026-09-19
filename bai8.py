# TODO: Khởi tạo
# def function_name(parameter):
#     return parameter

# function_name nó thường sẽ được cấu trúc là động từ + danh từ, snake_case
# Hàm => Xử lý một tác vụ (hành động), giúp mình dễ bảo trì code và tái sử dụng
# def tinh_tong(a, b):
#     return a+1, b+1, "str", 'abc', 123

# a = 5
# b = 6 
# c, d = tinh_tong(a, b)
# print(c, d) # => print(11)
# print(tinh_tong(a+1, b))
# print(tinh_tong(a+2, b))
# print(tinh_tong(a+3, b))

# Không dùng return, in ra giá trị
# Biến ở trong hàm => pare: tham số
# Biến ở truyền vào => agr: đối số

# --------------------------------------------------------
# => Số lượng đối số truyền vào phải bằng số tham số
# TH1. Các e truyền thẳng vào giá trị => các e cần chắc chắn là mk truyền đúng thứ tự và truyền đủ giá trị
# def in_tong(toan, ly):
#     print(toan)
#     print(ly)
#     print(toan+ly)
# toan = 5 
# ly = 6
# in_tong(toan, ly)

# TH2: Truyền vào thông qua key=> Cần đảm bảo truyền vào đủ giá trị
# def in_tong(toan, ly):
#     print(toan)
#     print(ly)
#     print(toan+ly)
# toan = 5 
# ly = 6
# in_tong(toan=toan, ly=ly)

# TH3: Truyền vào thông qua key, param có giá trị default
# => Xử lý được trường hợp mk truyền vào thiếu đối số (agr)
# => Nếu param có gtri default ở trước thì toàn bộ các param đằng sau cũng cần đảm bảo có giá trị default
# hoa = 9
# def in_tong(toan, ly = 9):
#     hoa = 10
#     global gdcd
#     gdcd = 10
#     print(toan)
#     print(ly)
#     print(toan+ly + hoa)


# toan = 5 
# ly = 6
# in_tong(toan , ly=10)
# print(gdcd)

# # TH4: Không biết có bao nhiêu giá trị cần truyền vào => Muốn trả về một tuple
# def in_tong(*args):
#     print(args)
# # in_tong(1,2,3,4,5,6,7,8,9)
# in_tong(dict)

# TH5: Không biết có bao nhiêu giá trị cần truyền vào => Muốn trả về là một dict
# def in_info(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# in_info(name = "Phạm Ngọc Kiên", Password = "123")

# TODO: Lambda => Xử lý với hàm ngắn gọn và không quá phức tạp
# def square(x) -> int:
#     '''
#     Hàm nhận vào 1 giá trị và tính lũy thừa của nó
#     '''
#     return int(x ** 2)
# square = lambda x : x ** 2
# print(square(5.5))
# a = input()

# items = [(1,"b"), (3, "a"), (2, "c")]
# items.sort(key=lambda x : x[1])
# print(items)


#TODO: Lưu ý
# 1. Tên hàm dạng (in thường , các chuỗi cách nhau bằng _)=> snake_case, và cấu tạo từ v_n => in_tong_gia_tri 
# 2. Cố gắng viết docstring và typehint cho hàm
# 3. Không bao giờ sử dụng mutable là một default agr
# 4. Biến khởi tạo ở phạm vi nào thì chỉ sử dụng trong phạm vi đó