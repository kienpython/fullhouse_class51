# string_value = 'python fullhouse dev' # => 'dev python fullhome'
# Thầy có một chuỗi string_value 
# Viết code làm sao cho ra dc kết quả là 'dev python fullhome' 
# value = (string_value[-3:] + " " + string_value[:16]).replace("house", 'home')
# value = f"{string_value[-3:]} {string_value[:16].replace('house', 'home')}"
# print(value)
string_value = 'python fullhouse dev ' #=> 'dev python fullhome'
list_value = string_value.split()
new_list = ""
for value in list_value:
    if value == "fullhouse":
        value = value.replace("house","home")
    new_list += value
print(new_list)

# TODO find(), in
# # check_exits = True if "pyton" in string_value else False
# # print(check_exits)

# print(string_value.find("fullhouse1"))

# TODO: upper(), lower(), title(), swapcase(), capitalize()
# print(string_value.upper()) #=> IN HOA
# print(string_value.lower()) #=> in thường
# print(string_value.title()) #=> Viết Hoa Chữ Cái Đầu
# print(string_value.swapcase()) #=> Đảo chữ hoa <=> thường
# print(string_value.capitalize()) #=> Viết hoa chữ cái đầu

#TODO: split()
# Sử dụng split + join + a[index] để chuyển 'python fullhouse dev' => 'dev python fullhome'

# word = string_value.split() # => ['python', 'fullhouse', 'dev']
# print(word[1])
# print(word[1].split('house'))
# word[1]= 'home'.join(word[1].split('house'))
# result = " ".join([word[2], word[0],word[1]])
# print(result)


# value_split = string_value.split("fullhouse")
# list_data = ['python', 'dev','home']
# data_join = "-".join(list_data)
# print(value_split)

# TODO: Replace()
# value_rep = string_value.replace("h", "k")
# print(value_rep)
# TODO: Nối chuỗi
# string_value_1 = "FullHouse"

# # full_value = string_value +" "+ string_value_1
# full_value = f"{string_value} {string_value_1}"
# # print(full_value)

# TODO: Slicing
# ------------------
# string_value_1 = '@' + string_value[1:]
# print(string_value)

# print(type(string_value))
# 'p y t h o n'
# '0 1 2 3 4 5'
# '-6 -5 -4 -3 -2 -1'
# start => ko viết => df = 0
# end => ko viết => df = 6
# print(string_value[:5:2])
# print(string_value[-4::-1])

