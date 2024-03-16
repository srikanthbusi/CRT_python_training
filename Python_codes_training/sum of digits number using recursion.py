n=int(input("enter the value :"))
def sum(n):

    if n<10 and n>=0:
        return n
    elif n<0:
        print("Invalid")
        
    else:
        a=n%10
        return a+sum(n//10)
print(sum(n))