#with user input
n1=int(input("enter number"))
def cal(n):
    a1=n%10
    while n>10:
        n=n//10
    
    a=a1+n
    print(n)
    print(a1)
    print(a)
cal(n1)

#without user input

def cal(n):
    a1=n%10
    
    while n>10:
        n=n//10
    
    a=a1+n
    print(n)
    print(a1)
    print(a)
cal(12)
