class Student:
    uni_name = "NUTS" # Class attribute

    def __init__(self, name, cgpa):
        self.name = name  # instance attribute
        self.cgpa = cgpa

stu1 = Student("usman",3.35)

print(stu1.cgpa)