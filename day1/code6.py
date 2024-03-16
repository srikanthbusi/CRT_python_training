# 
a = int(input("enter the first side"))
b = int(input("enter the second side"))
c = int(input("enter the third side"))
if a==b==c:
    print("Equilateral Triangle")
elif a==b or b==c or c==a:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")