n=int(input("enter the value :"))
def cou(n):

    if n==0:
        return 0
    
    else:
        return 1+cou(n//10)
print(cou(n))