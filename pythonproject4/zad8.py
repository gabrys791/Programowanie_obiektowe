

class Student:
    pass

class Marks:
    pass


instancja=Student()
inna_instancja=Marks()

print(isinstance(instancja, Student))
print(issubclass(Student, object))
print()