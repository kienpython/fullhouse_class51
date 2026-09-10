while True:
    ten_khach_hang = input("Tên khách hàng: ")
    so_luong_sp = int(input("Số lượng sản phẩm cần mua: "))
    tong_tien = 0
    list_san_pham = ""
    # TODO: Xử lý nhập sản phẩm
    for so_luong in range(so_luong_sp):
        ten_san_pham = input("Tên sản phẩm: ")
        don_gia = int(input("Đơn giá: "))
        so_luong_mua = int(input("Số lượng mua: "))
        thanh_tien = don_gia * so_luong_mua
        tong_tien += thanh_tien
        list_san_pham += f"{ten_san_pham} - {so_luong_mua}: {thanh_tien}\n"

    # TODO: Tính tiền
    giam_gia = 0
    if tong_tien >= 500_000:
        giam_gia = tong_tien * 10 / 100
    elif tong_tien >= 300_000 :
        giam_gia = tong_tien * 5 / 100
    tien_thanh_toan = tong_tien - giam_gia

    # TODO: Check dừng chương trình
    while True:
        check = input("Bạn có muốn tiếp tục tạo đơn hàng không?(Y/N)")
        if check == "N":
            break
        elif check == "Y":
            continue
        else:
            print("Lựa chọn này không hợp lệ, mời bạn chọn lại")

    # TODO: print hóa đơn
    print(f"Tên khách hàng {ten_khach_hang}")
    print("*"*15)
    print("Thông tin sản phẩm bạn đã chọn là:")
    print("*"*15)
    print(list_san_pham)
    print("*"*15)
    print(f"Tổng tiền trước giảm giá: {tong_tien}")
    print(f"Số tiền được giảm: {giam_gia}")
    print('*'*15)
    print(f"Số tiền cần thành toán: {tien_thanh_toan}")
    break