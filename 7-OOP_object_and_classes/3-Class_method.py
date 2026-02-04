class Student:
    uni_name = "NUTS" # Class attribute

    def __init__(self, name, cgpa):
        self.name = name  # instance attribute
        self.cgpa = cgpa

    @classmethod
    def get_uni_name(cls): #class method
        print(cls.uni_name)

    def get_name(self): # instance method
        print(self.name) 

    @staticmethod
    def fees_discount(fees,discount): #static method
        final_fees = fees - (discount*fees/100)
        print(f"discounted fees is: {final_fees}")


stu1 = Student("usman",3.35)

stu1.get_uni_name()
stu1.fees_discount(100,50)