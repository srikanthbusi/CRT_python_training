n=int(input("enter width"))

for i in range(1,n):
    for s in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print(" ")
#in j loop 2*i is used rather than 2*i-1 coz 
#calculation
#for i=1 in 2*i-1 range will be (1,1) means loop will not executed