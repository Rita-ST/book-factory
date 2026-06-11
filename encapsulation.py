class Students:
    def __init__(self,name, id, tuition_fee):
        self.nam = name
        self.id = id
        self.__tuition_fee = tuition_fee

    def student_info(self):
        return f" {self.name} of id number {self.id}"
student1 = Students("Anne Godlewski",35117,26438)
print(student1.student_info)
student1.__tuition_fee
