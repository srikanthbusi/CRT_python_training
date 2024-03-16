a=0
re=0
n=int(input("enter the number : "))
n1=n
while n>=1:
    a=n%10
    re=re+a**3
    n=n//10
print("sum",re)
if n1==re:
    print("armstrong number")
else:
    print("not armstrong number")
