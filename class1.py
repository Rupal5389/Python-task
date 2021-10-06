'''class student:
    roll_number = 100
    num1 = 50
    num2 = 80 #data member

    def add(self): #member function
        print(self.num1+self.num2)

obj = student()
obj.add()
print(obj.roll_number)'''

from os import name


'''class Hod:
    def __init__(self):#constructor
        self.name = 'rupal'
        self.age = 21
        self.empid = 1000

    def info(self): #instance method
        print("my name is:", self.name)
        print("my age is:", self.age)
        print("my emp id is:",self.empid)

obj = Hod()#object create
obj.info()'''

'''class Student:
    def __init__(self):
        self.s_name = "rupal"
        self.l_name = "manwatkar" #instance
        self.s_roll.no = 20
        self.s_branch = "CSE"
        self.s_mb = 00000000

obj = Student()
print(obj.__dict__)'''

'''class family:
    def __init__(self):
        self.mother_name = "vandana"
        self.father_name = "manoj"
        self.brother_name = "manthan"
        self.objedu = self.qualification()

    def display(self):
        print("mother_name=",self.mother_name)
        print("father_name=",self.father_name)
        print("brother_name=",self.brother_name)

    class qualification:
      def __init__(self):
        self.mother_name = "graduate"
        self.father_name = "graduate"
        self.brother_name = "post graduate"

      def show(self):
        print("mother_name=",self.mother_name)
        print("father_name=",self.father_name)
        print("brother_name=",self.brother_name)

obj = family()
obj.display()
temp = obj.objedu
temp.show()'''

'''class flower:
    def __init__(self):
        self.flower_name1 = "Rose"
        self.flower_name2 = "Sunflower"
        self.flower_name3 = "lily"
        self.flower_name4 = "mogra"
        self.objcolor = self.coloridentification()

    def display(self):
        print("flower_name1=",self.flower_name1)
        print("flower_name2=",self.flower_name2)
        print("flower_name3=",self.flower_name3)
        print("flower_name4=",self.flower_name4)

    class coloridentification:
        def __init__(self):
            self.flower_name1= "red"
            self.flower_name2= "yellow"
            self.flower_name3= "white"
            self.flower_name4= "orange"

        def show(self):
            print("flower_name1=",self.flower_name1)
            print("flower_name2=",self.flower_name2)
            print("flower_name3=",self.flower_name3)
            print("flower_name4=",self.flower_name4)

obj = flower()
obj.display()
obj.objcolor.show()'''





