class Student:
    def __init__(self,student_name,marks):
        self.student_name=student_name
        self.marks=marks

    def set_marks(self, m):
        self.marks = m
    def set_name(self,imie):
        self.student_name=imie

student=Student('Gabryś',[5,5,5])
print(student.__dict__)
student.set_marks([5, 5, 7])
print(student.__dict__)