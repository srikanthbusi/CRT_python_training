#take integer user and check if number is divisible by sum of digits or not
n=int(input("enter n"))
n1=n
a=0
r=0
while n>0:
    r=n%10
    a=a+r
    n=n//10
print("sum is ")
print(a)

if n1%a==0:
    print("divisible")
else:
    print("not divisible")
    