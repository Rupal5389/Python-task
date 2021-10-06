'''class Faculty: #parent class
    def __init__(self, f_name, department, f_id):
        self.f_name = f_name
        self.department = department
        self.f_id = f_id

    def print_info(self):
        print('faculty information=',self.f_name, self.department, self.f_id)

class Cse(Faculty): #child class
    pass #no statement

obj = Cse("jyoti Mam","computer science","1002")
obj.print_info()'''

class School: #parent class
    def School_name(self):
        print("St. Joseph's Convent")

class Student(School): #child class 
    def Student_info(self):
        print("Name: Rupal Manwatkar")
        print("Roll No: 20")

obj = Student()
obj.School_name()
obj.Student_info()
