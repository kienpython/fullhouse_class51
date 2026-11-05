import pandas as pd

# TODO:: Khái niệm
# TODO: Series
# series = pd.Series(
#     [10,20,30],
#     # index = ['a','b','c']
# )
# print(series)

# TODO: Data Frame
# df = pd.DataFrame({
#     "Name":["Phạm Ngọc Kiên", "Phạm Ngọc Kiên 1"],
#     "Age":[22, 23],
# })
# print(df)

# TODO: Cách khai báo Data Frame
#1 Cách 1 - Phổ biến nhất
# df = pd.DataFrame({
#     "Name":["Phạm Ngọc Kiên", "Phạm Ngọc Kiên 1"],
#     "Age":[22, 23],
# })
# print(df)

# 2 Cách 2 : Tạo từ một list của dict
# df = pd.DataFrame(
#     [
#         {"Name":"Phạm Ngọc Kiên", "Age":22},
#         {"Name": "Phạm Ngọc Kiên 1", "Age": 23}
#     ]
# )
# print(df)

# 3. Cách 3 Tạo từ list của list 
# df = pd.DataFrame(
#     [
#         ["Phạm Ngọc Kiên", 22],
#         ["Phạm Ngọc Kiên 1", 23],
#     ]
# )
# print(df)

# 4. Tạo từ một numpy array
# import numpy as np
# df = pd.DataFrame(
#     np.zeros((3,4)),
#     columns=['A','B','C','D']
# )
# print(df)

# 5. Đọc từ file CSV
# df = pd.read_csv('TestData.csv')
# print(df)

# 6. Đọc từ file Excel
# df = pd.read_excel("CN HN-KS26-CNTT3.xlsx", sheet_name='Trang tính1')
# print(df)

#TODO: cách hàm xử lý với dataframe
# df = pd.read_csv('TestData.csv')
# print(df)
# print(df.head()) #=> Lấy 5 row đầu tiên
# print(df.head(8)) #=> Lấy 8 row đầu tiên
# print(df.tail(5)) # => Lấy 5 dòng cuôi
# print(df.shape) #=> Lấy được thông tin về dim (15,3)
# print(df.columns) # => Lấy tên của cột
# print(df.dtypes) #=> Lấy kiểu dữ liệu của mỗi cột
# print(df.info()) # => Xem tổng quan data
# print(df.describe()) # => stats cột số
# print(df.isna().sum()) #=> kiểm tra rỗng

# TODO: Truy cập cột
# df = pd.read_csv('TestData.csv')
# print(df)

#1. Bracket - chuẩn nhất
# print(df['Name']) #=> lấy giá trị của 1 cột
# print(df[["Name","Age"]]) #=> lấy giá trị của nhiều cột

#2. Dot - Nhanh hơn, nhưng có nhiều giới hạn: class, chứa dấu cũng báo lôi
# print(df.Name)

#3. loc - xử lý cả hàng và cột
# print(df.loc[3::2,'Name']) #=> Lấy hàng 3-5 (cả index = 5), của cột Name
# print(df.loc[3:5,['Name', 'Age']]) #=> Lấy hàng 3-5 (cả index = 5) của cột Name và Age

#TODO: Truy cập hàng
# df = pd.DataFrame({
#     "Name":["Phạm Ngọc Kiên", "Phạm Ngọc Kiên 1", "Phạm Ngọc Kiên 2"],
#     "Age":[22, 23, 24],
# }, index=['a','b','c'])
# print(df)

# 1. Chưa setup lại index
# print(df.iloc[0]) #=> Lấy row đầu tiền
# print(df.iloc[0,0]) # => Lấy value theo tọa độ
# print(df.iloc[0:2]) # => Lấy 2 hàng đầu của data (Không lấy index tại 2)
# print(df.iloc[:,0:2]) # => Lấy hàng và cột theo điều kiện
# print(df.iloc[-1]) # => Lấy hàng cuối cùng

#2. Đã setup index
# print(df.loc['a']) # => Lấy hàng a
# print(df.loc['b','Name']) # => Lấy hàng b, và cột Name
# print(df.loc[['b','c'],'Name'])


# TODO: Lọc data với boolean mask
# df = pd.read_csv("TestData.csv")
# # Lọc trực tiếp từ điều kiện, 1 điều kiện
# # print(df[df['Class'] != "Class 51"])

# # Lọc từ nhiều điều kiện
# # print(df[(df['Class'] == "Class 51") & (df['Age'] >= 24)])
# # &, |, ~, isin
# print(df[df['Class'].isin(['Class 51', "Class 52"])])

#TODO: Sắp xếp và query()
# # 1. Sắp xếp theo thứ tự tăng dần
# df = pd.read_csv("TestData.csv")
# # print(df.sort_values('Class')) # => Sắp xếp theo thứ tự tăng 
# # print(df.sort_values("Age", ascending=False)) #=> Sắp xếp age theo thứ tự giảm dần
# # print(df.sort_values(['Age',"Class"], ascending=[True, True])) #=> Sắp xếp theo 2 cột, độ ưu tiên từ trái sang phải

# # => Đảm bảo giá trị so sánh cùng kiểu dữ liệu với giá trị so 
# # => df.query => Copy df, thay đổi và in ra
# age = int(input("Nhập vào tên class: "))
# print(df.query('Age > @age'))

#TODO: Groupby 
# df = pd.read_csv("TestData.csv")

# Tính tổng giá trị theo Class
# print(df.groupby('Class')['Age'].agg(['sum','mean','count']))

#TODO: Xử lý số giá trị thiếu
df = pd.read_csv("TestData.csv")
# # Đếm số dòng trống của mỗi cột
# print(df.isna().sum())

# # Xóa hàng có giá trị NaN
# print(df.dropna())

# Xóa cột có nhiều NaN
# print(df.dropna(axis=1, thresh=100))
# print(df.fillna(0))
# print(df.fillna(df["Age"].mean()))



