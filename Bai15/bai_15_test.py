# TODO: Read file CSV dạng List
# import csv
# with open("TestData.csv", 'r', encoding='utf-8') as f:
#     data = csv.reader(f, delimiter=",")
#     next(data)
#     for row in data:
#         print(row)

# TODO: Write file CSV, dạng list
# import csv
# data = [
#     ['Phạm Ngọc Kiên 1', 20, 'Class 51'],
#     ['Phạm Ngọc Kiên 2', 24, 'Class 51'],
#     ['Phạm Ngọc Kiên 3', '25', 'Class 51'],
#     ['Phạm Ngọc Kiên 4', '21', 'Class 51']
# ]
# with open("TestData1.csv", 'w', encoding="utf-8", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(['Name','Age','Class'])
#     writer.writerows(data)

#TODO: Read file csv by Dict
# import csv
# with open("TestData.csv", 'r', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     # => Lấy row 1 làm key
#     # => Cột có value không header => key = None
#     for row in reader:
#         # print(row)
#         print(row['Name'])

#TODO: Write file csv by Dict
# import csv
# data = [
#     {'Name': 'Phạm Ngọc Kiên 1', 'Age': '20', 'Class': 'Class 51'},
#     {'Name': 'Phạm Ngọc Kiên 2', 'Age': '24', 'Class': 'Class 51'},
#     {'Name': 'Phạm Ngọc Kiên 3', 'Age': '25', 'Class': 'Class 51'},
#     {'Name': 'Phạm Ngọc Kiên 4', 'Age': '21', 'Class': 'Class 51'},
# ]
# with open("TestDataDict.csv", "w", encoding="utf-8", newline="") as f :
#     fields = ['Name', "Age", "Class"]
#     writer = csv.DictWriter(f, fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(data)


"""
Đọc file TestData.csv, 
Tạo menu:

1. Hiển thị danh sách sinh viên
=> dictRead => fstring :<10

2. Hiển thị danh sách sinh viên theo lớp
if class 
[Danh sách sinh viên Class 51]
1. Phạm Ngọ    ....
[Danh sách sinh viên Class 52]
1. Phạm Ngọ    ....

3. Tìm bạn có tuổi cao nhất.
4. Xóa toàn bộ sinh viên của lớp Class 55
5. Thêm sinh viên mới vào class 51: Nhập tên, tuổi
0. Thoát

"""

import csv

def get_datas(path) -> list:
    """
    Get data from TestData.csv, return list[dict]
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = []
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
        return data

def save_data(data, path):
    """
    Nhận một data là một dict
    """
    with open(path, 'a', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Name',"Age", "Class"])
        writer.writerow(data)

def display_students_by_class(path):
    # TODO: Get all datas
    data = get_datas(path) # [{},{}]

    # # TODO Handle title collum
    headers = []
    for key in data[0].keys():
        headers.append(key)
    chuoi_header = ""
    for header in headers:
        chuoi_header+= f"| {header:20}"
    print(chuoi_header)


    classes = []
    for row in data:
        for key, value in row.items():
            if key == "Class":
                classes.append(value)

    class_dict = {}
    # TODO Phân loại
    for row in data:
        # print(row['Class'])
        if row['Class'] not in class_dict:
            class_dict[row['Class']] = []
            class_dict[row['Class']].append(row)
        else:
            class_dict[row['Class']].append(row)

    # TODO: Print by class
    for key, value in class_dict.items():
        print(f"[Danh sách sinh viên của class {key}]")
        for row in value:
            string_print = ""
            for key, value in row.items():
                string_print += f"| {value:<20}"
            print(string_print)
        print()



def display_students(path):
    # TODO: Get all datas
    data = get_datas(path) # [{},{}]

    # TODO Handle title collum
    headers = []
    for key in data[0].keys():
        headers.append(key)
    chuoi_header = ""
    for header in headers:
        chuoi_header+= f"| {header:20}"
    print(chuoi_header)

    # TODO Print row
    for row in data:
        string_print = ""
        for key, value in row.items():
            string_print += f"| {value:<20}"
        print(string_print)

def create_students(path):
    name = input("Tên sinh viên là: ")
    age = input("Tuổi sinh viên là: ")

    data = {
        "Name": name,
        "Age": age,
        "Class": "Class 51"
    }
    save_data(data, path)

def main():
    while True:
        path = "TestData.csv"
        choice = input("""
====================================
1. Hiển thị danh sách sinh viên
2. Hiển thị danh sách sinh viên theo lớp
3. Tìm bạn có tuổi cao nhất.
4. Xóa toàn bộ sinh viên của lớp Class 55
5. Thêm sinh viên mới vào class 51: Nhập tên, tuổi
0. Thoát
Lựa chọn của bạn là: """)
        
        if choice == "1":
            display_students(path)
        elif choice == "2":
            display_students_by_class(path)
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            create_students(path)
        elif choice == "0":
            break
        else:
            print("Vui lòng chọn chức năng từ [0-5]!")

if __name__ == "__main__":
    main()