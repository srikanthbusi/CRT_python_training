# finding a number is prime or not
num = int(input("enter an number"))
flag = 0
for i in range(2,num):
    if num%i == 0:
        flag = 1
        break
if flag==1:
    print("not a prime numbe")
else:
    print(" prime number")

# n = int(input("Enter an Number : "))

# for i in range(2,n//2):  
#     if(n%i==0):
#         print('"Not a Prime Number"')  
#         break
#     else:
#         print('Prime number"')
# print("Completed")