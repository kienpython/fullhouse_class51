
students = [["1111","Phạm Ngọc Kiên", 25, 7, 7, 7]]

thong_bao = " "*4 + "Chào mừng bạn đến với app quản lý sinh viên!" + " "*4
gach = "-" * len(thong_bao) 
print(gach)
print(thong_bao)
print(gach)
while True:
    choice = input("""
Vui lòng chọn chức năng mà bạn mong muốn:
1. Thêm sinh viên mới
2. Xem thông tin sinh viên
3. Xóa sinh viên
4. Tạo bảng xếp hạng sinh viên
0. Thoát chương trình
Lựa chọn của bạn là: 
""")
    if choice == "1":
        mssv = input("Nhập vào MSSV: ")
        if not mssv:
            print("Mssv không được bỏ trống!")
            continue
            
        name = input("Nhập vào name: ")
        if not name:
            print("Tuổi không được bỏ trống!")
            continue

        try:
            age = int(input("Nhập vào age: "))
            if not age:
                print("Tuổi không được bỏ trống!")
                continue
        except:
            print("Tuổi không hợp lệ!")

        try:
            phys = float(input("Nhập vào phys: "))
        except:
            print("Điểm lý không hợp lệ!")
        try:
            chemis = float(input("Nhập vào chemis: "))
        except:
            print("Điểm hóa không hợp lệ!")
        try:
            math = float(input("Nhập vào math: "))
        except:
            print("Điểm toán không hợp lê!")

        students.append([mssv, name, age, phys, chemis, math])
    elif choice == "2":
        print("--------------------")
        print("Danh sách sinh viên:")
        for student in students:
            print(f"{'MSSV':<12} | {'Họ và tên':<20} | {'Tuổi':<12} | {'Điểm lý':<12} | {'Điểm Hóa':<12} | {'Điểm Lý':<12}")
            print(f"{student[0]:<12} | {student[1]:<20} | {student[2]:<12} | {student[3]:<12} | {student[4]:<12} | {student[5]:<12}")

    elif choice == "3":
        mssv = input("Vui lòng nhập vào MSSV mà bạn muốn xóa: ")
        check = False
        for student in students:
            if student[0] == mssv:
                students.remove(student)
                print("Đã xóa thành công!")
                check = True
                break
        if not check:
            print("Không tìm thấy sinh viên cần xóa!")

    elif choice == "0":
        break
    else:
        print("Lựa chọn của bạn không hợp lệ!")
    