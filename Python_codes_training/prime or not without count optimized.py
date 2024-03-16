n = int(input("enter n  "))
flag = 0
# after n/2(half) no number will divide n
# floor division used to not considering decimal values of n/2 
for i in range(2, n//2):
    if n % i == 0:
        flag = 1
        break
if flag == 1:
    print("not prime")
else:
    print("prime")
