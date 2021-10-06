# write a program using CSV file

import csv
f = open("student.csv","w",newline="")
a= csv.writer(f)
a.writerow(["name","rollno","email","mobileno","adress","p1","p2","p3","p4","p5","total","percentage","result"])

name="rupal"
rollno=2905
email="abc@gmail.com"
mobileno=123456789
adress="nagpur"
p1=int(input("enter the paper1 marks"))
p2=int(input("enter the paper2 marks"))
p3=int(input("enter the paper3 marks"))
p4=int(input("enter the paper4 marks"))
p5=int(input("enter the paper5 marks"))
if p1>35 and p2>35 and p3>35 and p4>35 and p5>35:
    result="pass"
    print("you are pass")
else:
    result="fail"
    print("you are fail")
total=p1+p2+p3+p4+p5
percentage = total/5

a.writerow(["name","rollno","gmail","mobileno","adresss","p1","p2","p3","p4","p5","total","percentage","result"])
print("record are save")