class School:
    def School_name(self):
        print("st.joseph's convent")

class Faculty(School):
    def faculty_name(self):
        print("Riya Mam")

class Student(School):
    def Student_info(self):
        print("Name: Rupal Manwatkar")
        print("Roll No: 20")

class Principle(Faculty, Student):
    pass

obj = Principle()
obj.School_name()
obj.faculty_name()
obj.Student_info()