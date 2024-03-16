n=int(input("enter number  "))
n1=n
a=0
while n>0:
    r=n%10
    a=a*10+r
    n=n//10
if n1==a:
    print("pallindrone")
else:
    print("not pallindrone")