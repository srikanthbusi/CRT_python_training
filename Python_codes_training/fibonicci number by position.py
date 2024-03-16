def fact(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fact(n-2) + fact(n-1)
n=int(input("enter  :"))
print(fact(n))