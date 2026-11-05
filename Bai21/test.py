class User:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def print_info(self):
        print(f"{self.id}-{self.name}-{self.age}")

class Personal:
    def print_info(self):
        print(f"Đây là Personal!")

class Class:
    def __init__(self, id, teacher_id):
        self.id = id 
        self.teacher_id = teacher_id
        self.students = []

# Nói X là Y => Thấy đúng => Kế thừa

class Student(User):
    pass

# Độ ưu tiên: => thằng con => class từ trái sang phải
class Teacher(User , Personal):
    def __init__(self, id, name, age, stk):
        super().__init__(id, name, age)
        self.__stk = stk
        self.classes = [Class("12121",self.id)]
    # def print_info(self):
    #     super().print_info()
    #     print(f"{self.id}-{self.name}-{self.age}-{self.__stk[-4:-1]}")

kien = Student(1111, "Kiên", 20)
# kien.print_info()
kien_teach = Teacher(1111, "Kiên", 20, "1111111")
kien_teach.print_info()
# print(kien.__name)