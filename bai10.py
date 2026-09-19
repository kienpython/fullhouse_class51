
def print_menu():
    print("="*60)
    print("QUAN LÝ BÃI XE - SMART PAKKING")
    print("="*60)
    print("""
1. Check-in (Đăng ký xe vào)
2. Báo cáo tồn kho (Hiển thị danh sách)
3. Tìm kiếm xe (Theo biển số)
4. Check-out (Xử lý xe ra & Tính phí)
5. Thoát chương trình
""")
    print("="*60)


def get_stt_id(list_xe):
    if not list_xe:
        return 1  
    return list_xe[-1]['ID']

def check_exits_xe(list_xe , bien_so:str):
    if not list_xe:
        return False
    for xe in list_xe:
        if xe['bien_so'] == bien_so:
            return xe
    return False

def nhap_type_int(message):
    while True:
        try:
            gio_vao = int(input(f"Nhập vào {message}: "))
            return gio_vao
        except:
            print(f"{message} phải là một số!")
    

def nhap_data_xe():
    while True:
        bien_so = input("Nhập vào biển số xe: ")
        # TODO: Check tồn tại biển số xe chưa
        if check_exits_xe(list_xe, bien_so):
            print("Biển số xe đã tồn tại!")
        else:
            break
    loai_xe = input("Nhập vào loại xe: ")

    # Giờ vào nằm trong khoảng từ 0-23, và nếu nhập vòa một số thực, làm tròn 
    while True:
        gio_vao = nhap_type_int("Giờ vào")
        # TODO: Check phạm vi giờ
        if not (int(gio_vao) >= 0 or int(gio_vao) <= 23):
            print("Giờ vào không hợp lệ!")
        else:
            break
    return bien_so, loai_xe, gio_vao

def check_in(list_xe:list) -> list:
    """
    Hàm này xử lý việc check in biển số xe
    """

    bien_so, loai_xe, gio_vao = nhap_data_xe()

    # TODO: Add xe vào list xe
    list_xe.append({
        "ID": get_stt_id(list_xe)+1,
        "bien_so": bien_so,
        "loai_xe": loai_xe,
        "gio_vao": gio_vao
    })
    print("Nhập vào thành công!")
    

def check_list_xe(list_xe):
    '''
    Check xem list xe có rỗng không!
    '''
    if not list_xe:
        print("[Thông báo: Bãi xe hiện đang trống!]")
        return True
    
def display_list_xe(list_xe):
    if check_list_xe(list_xe):
        return
    print(f"{'ID':<4} | {'Biển số xe':<20} | {'Loại xe':<14} | {'Giờ vào':<10}")
    for xe in list_xe:
        print(f"{xe['ID']:<4} | {xe['bien_so']:<20} | {xe['loai_xe']:<14} | {xe['gio_vao']:<10}")

def search_xe(list_xe:list):
    if check_list_xe(list_xe):
        return
    bien_so = input("Nhập vào biển số xe: ")
    xe_finded = check_exits_xe(list_xe, bien_so)
    if not xe_finded:
        print(f"[Lỗi]: Không tìm thấy biển số {bien_so} trong hệ thống!")
    print(f"Thông tin chi tiết: {xe_finded}")


def check_out(list_xe:list):
    bien_so = input("Nhập vào biển số xe: ")
    gio_ra = nhap_type_int("Giờ ra: ")
    xe = check_exits_xe(list_xe, bien_so)
    if not xe:
        print(f"[Lỗi]: Không tim thấy biển số {bien_so} trong hệ thống!")
        return
    if gio_ra < xe['gio_vao'] or gio_ra > 23:
        print("[Lỗi]: Giờ ra phải sau hoặc bằng giờ vào!")
        return
    phi_gui_xe = 5000
    tong_phi = phi_gui_xe*(gio_ra - xe['gio_vao'])
    print(f"Tổng phí phải trả: {tong_phi}")

    #TODO: Xóa xe sau khi thanh toán
    list_xe.remove(xe)
    print(f"[Thành công]: Đã xóa xe ID {xe['ID']} thành công!")
    


list_xe = [{
    "ID":1,
    "bien_so": "AB-88844",
    "loai_xe": "Xe Máy",
    "gio_vao": 3
}]
def main():
    print_menu()
    while True:
        try:
            choice = int(input("Nhập vào lựa chọn của bạn (1-5):"))
        except:
            print("Phải nhập vào là một số!")
            break

        if choice == 1:
            check_in(list_xe)
        elif choice == 2:
            display_list_xe(list_xe)
        elif choice == 3:
            search_xe(list_xe)
        elif choice == 4:
            check_out(list_xe)
        elif choice == 5:
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Vui lòng chọn chức năng từ 1-5!")

if __name__ == "__main__":
    main()