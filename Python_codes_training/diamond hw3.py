n=int(input("Enter diamond length:"))
for i in range(1,n+1):
    for s in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print(" ")

for i in range(n-1,0,-1):
    for s in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    
    
    print(" ")
    