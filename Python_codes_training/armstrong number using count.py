a=0
re=0
n=int(input("enter the number : "))
n1=n
n2=n
count=0
while n>=1:
    n=n//10
    count+=1
print(count)
for i in range(count+1):
    a=n1%10
    re=re+a**3
    n1=n1//10
print("sum",re)
if n2==re:
    print("armstrong number")
else:
    print("not armstrong number")
