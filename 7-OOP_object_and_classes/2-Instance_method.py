class Student:
    uni_name = "NUTS" # Class attribute

    def __init__(self, name, cgpa):
        self.name = name  # instance attribute
        self.cgpa = cgpa

    def get_name(self): # instance method
        print(self.name) 

stu1 = Student("usman",3.35)

stu1.get_name()