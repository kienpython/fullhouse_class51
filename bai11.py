
def print_menu():
    print("="*40)
    print("    QUẢN LÝ KHO HÀNG - GROCERY STORE    ")
    print("="*40)
    print("""
1. Xem danh sách hàng tồn kho
2. Nhập thêm hàng hóa mới
3. Cập nhật số lượng tồn kho theo ID
4. Thoát chương trình
""")
    print("="*40)

def show_inventory(inventory_list):
    # [] = {} = () = 0 = False = "" => False
    if not inventory_list:
        print("Kho hàng hiện đang trống!")
        return
    
    print(f"{'ID':<10} | {'Tên hàng hóa':<20} | {'Số lượng tồn':<6}")
    for inventory in inventory_list:
        print(f"{inventory['id']:10} | {inventory['name']:<20} | {inventory['quantity']:<6}")

    print()
    print()
    print()

def check_none(message):
    while True:
        value = input(f"Nhập {message} hóa: ")
        if value:
            return value
        print(f"{message} không được để trống!")

def check_quantity():
    while True:
        try:
            quantity = int(input("Nhập số lượng tồn kho: "))
            if quantity > 0 :
                return quantity
            print("Số lượng tồn kho phải lớn hơn không!")
        except:
            print("Số lượng tồn kho phải là số nguyên!")

def add_item(inventory_list: list) -> list:
    '''
    Hàm này xử lý việc add hàng tồn kho
    '''
    id = check_none("ID")
    name = check_none("Tên hàng hóa")

    quantity = check_quantity()

    inventory_list.append({
        "id": id,
        "name": name,
        "quantity": quantity 
    })
    print("Thêm hàng hóa vào kho thành công!")
    

def update_quantity(inventory_list:list) -> list:
    """
    Hàm này xử lý việc update quantity
    """
    id = input("Nhập vào mã hàng hóa: ")
    if not inventory_list:
        print("Hàng hóa đang rỗng!")
        return

    # check_exits = False
    for index, inventory in enumerate(inventory_list):
        if inventory['id'] == id:
            quantity = check_quantity()
            inventory['quantity'] = quantity
            inventory_list[index] = inventory
            print(f"Cập nhật số lượng hàng hóa của ID {id} thành công!")
            # check_exits = True
            return
            # break
    # if not check_exits:
    print(f"Không tìm thấy hàng hóa có mã {id}!")



    
def main():
    inventory_list = [
        {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
        {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
    ]
    while True:
        print_menu()
        choice = input("Nhập vào lựa chọn của bạn: ")
        if choice == "1":
            show_inventory(inventory_list)
        elif choice == "2":
            add_item(inventory_list)
        elif choice == "3":
            update_quantity(inventory_list)
        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng phần mềm!")
            print("   [Chương trình đã kết thúc]    ")
            break
        else:
            print("Lựa chọn của bạn không hợp lệ! Vui lòng chọn [1-4]!")

if __name__ == "__main__":
    main()