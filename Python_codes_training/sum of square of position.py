"1578"

a=0
re=0
it=0
n=int(input("enter the number : "))
n1=n
while n>0:
    n=n//10
    it+=1
print(it)
while n1>0:
    a=n1%10
    re=re+a**it
    it-=1
    n1=n1//10
print("sum",re)
