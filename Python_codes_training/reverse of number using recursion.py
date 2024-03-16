#recursion to reverse the number
n=int(input("enter the value :"))
def rev(n):
    if n<10 and n>=0:
        return n
    elif n<0:
        print("Invalid")
        
    else:
        a=n%10
        
        print(a,end="")
        return rev(n//10)
print(rev(n))
