n = int(input("enter n  "))
flag = 0
for i in range(2, n):
    if n % i == 0:
        flag = 1
        break
if flag == 1:
    print("not prime")
else:
    print("prime")
