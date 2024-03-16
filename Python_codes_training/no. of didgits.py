n=12345
count=0
a=0
r=0
while n>0:
    a=n%10
    a=a+r
    n=n//10
    count+=1
print(count)

