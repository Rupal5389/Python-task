basic_salary = float(input("enter basic salary of an employee :"))
HRA = float(input("enter HRA :"))
DA = float(input("enter DA :")) 

gross_salary = basic_salary+HRA+DA

gross_salary = basic_salary+(HRA*basic_salary/100)+(DA*basic_salary/100)
print(" gross salary is :",gross_salary) 