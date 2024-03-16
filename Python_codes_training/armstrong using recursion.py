n=int(input("enter the value :"))
def cou(n):

    if n==0:
        return 0
    
    else:
        return 1+cou(n//10)
print(cou(n))
c=cou(n)
def arm(n,c):
    
    if n==0:
        return 0
    else:
        return (n%10)**c + arm(n//10,c)  
print(arm(n,c))
dec=arm(n,c)
if dec==n:
    print("armstrong")
else :
    print("not armstrong")
