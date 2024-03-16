"""calculate the difference of sum of numbers that  are divisible by six and 
not divisible by six in the range of first 30 natural number"""


n=int(input("enter number "))
a=0
b=0
for i in range(1,n+1):
    if i%6==0:
        a=a+i
    else:
        b=b+i
print(a)
print(b)
if a>b:
    print("difference")
    print(a-b)
else:
    print("difference")
    print(b-a)
        
        