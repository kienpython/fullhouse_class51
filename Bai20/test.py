class Student:
    school = "FullHouseDev"
    def __init__(self, name, age, stk):
        self.name = name
        self.age = age
        self.__stk = stk


    @property
    def stk(self):
        return self.__stk

    @stk.setter
    def stk(self, value):
        self.__stk = value

    # 
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    #
    @staticmethod
    def validate_age(age):
        if age <= 0 or age >=200:
            print("Tuổi không hợp lệ")
    #
    @classmethod
    def update_school(cls, new_school):
        cls.school = new_school

    # def __repr__(self):
    #     # return f"Name:{self.name}, Age: {self.age}"
    #     return f"(Name:{self.name}, Age: {self.age})"

    def __str__(self):
        return f"Tài khoản của bạn là {self.name}"

kien = Student("Kiên", 20, "00000000")
print(kien)
# kien.show_info()
# kien.validate_age(28)
# kien.update_school("PTIT")
# kien.stk = "11111111"
# print(kien.stk)



