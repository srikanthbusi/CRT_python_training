#calculate the sum of digits of number taken from user
n=int(input("enter n"))
res=0
while n>0:
    r=n%10
    res=res+r

    n=n//10
print(res)
    