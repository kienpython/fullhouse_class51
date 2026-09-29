# f = open("C:/Users/kienp/Downloads/Used/FullHouseDev/Class_51/testdata.txt", 'r', encoding="utf-8")

# data = f.read()
# print(data)
# f.close()

# with open("testdata.txt", 'a', encoding='utf-8') as f, \
#     open("testdata.txt", 'r', encoding='utf-8') as fa:
#     f.writelines([
#         "\nPham Ngọc Kiên 8\n",
#         "Phạm Ngọc Kiên 9"
#     ])

#     data = fa.read()
#     print(data)

# count=0
# with open('../testdata.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         if line=='ka\n':
#             count+=1
# print(count)

new_data = []
with open("Class_51/testdata.txt","r",encoding='utf-8') as f, \
open("Class_51/new_data.txt","w",encoding='utf-8') as fa:
    for line in f:
        new_data.append(f"{line.upper().strip()}\n")
    fa.writelines(new_data)
