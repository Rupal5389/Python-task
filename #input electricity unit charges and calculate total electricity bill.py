a = float(input("enter electricity unit charges :"))

a = 50

if a<=50:
    price=a*0.50
elif a>50 and a<=150:
    price=a*0.75
elif a>150 and a<=250:
    price= a*1.20
else:
    print=a*1.50

print("price")