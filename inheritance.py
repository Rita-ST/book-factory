
class Student:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Student :", self.name)

class Computer_eng_student(Student):
    def __init__(self, name, year):
        super().__init__(name)  
        self.year = year

    def details(self):
        print(self.name, "is a", self.year)

d = Computer_eng_student("Brady", 36174)
d.info()      
d.details()  