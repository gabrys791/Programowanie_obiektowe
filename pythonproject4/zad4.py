class Student:
    nazwa_ucznia =""
    klasa_ucznia =""
    student_id =""
    def __init__(self,nazwa_ucznia, klasa_ucznia, student_id=None):
        self.nazwa_ucznia=nazwa_ucznia
        self.klasa_ucznia=klasa_ucznia
        self.student_id=student_id
    def student_data(self):
        if self.student_id == None:
            return self.nazwa_ucznia,self.klasa_ucznia
        else:
            return self.student_id


student=Student('Gabriel','IO 3',166292)
print(Student.__dict__)
# print(student.nazwa_ucznia)
# print(student.student_data())
# print(Student.__dict__)
# print(Student.__module__)