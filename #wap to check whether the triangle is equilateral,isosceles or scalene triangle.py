x = (input("enter  lengths of triangles sides: "))

a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))

if a==b==c:
    print("triangle is an equilateral triangle")

elif a==b or b==c or c==a:
    print("triangle is an isosceles triangle ")

else:
    print("triangle is an scalene triangle")