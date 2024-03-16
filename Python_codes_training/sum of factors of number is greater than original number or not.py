"""take a num input from user check
 if sum of factors of number is greater than original number or not"""
n=int(input("enter number "))
n1=n
a=0
print("factors")
for i in range(1,(n//2)+1):
    if n%i==0:
        a=a+i
        print(i)
print("sum",a)
if a>n:
    print("greater")
else:
    print("less")
