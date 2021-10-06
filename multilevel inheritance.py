class Grandfather:
    def __init__(self, Grandfather_name):
        self.Grandfather_name = Grandfather_name

class Father(Grandfather):
    def __init__(self, Father_name, Grandfather_name):
        self.Father_name = Father_name

        Grandfather.__init__(self,Grandfather_name)

class Son(Father):
    def __init__(self, Sonname, father_name, Grandfather_name):
        self.Sonname = Sonname

        Father.__init__(self, father_name, Grandfather_name)

    def print_name(self):
        print("Grandfather name :", self.Grandfather_name)
        print("Father_name:", self.Father_name )
        print("sonname:", self.Sonname)

s1 = Son("Manthan","Nayan","Mahendra")
print(s1.Grandfather_name)
s1.print_name()