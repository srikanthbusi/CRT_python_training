#####sum of the digits
# sum = 0
# num  = int(input("enter the number"))
# while(num>0):
#     sum = sum + num%10
#     num = num//10 
# print("ok the sum of the digits : ",sum)

# ###counting no of digits
# c = 0
# num  = int(input("Enter karo"))
# while(num>0):
#     digit=  num%10
#     num = num//10 
#     c = c+1
    
# print("ok Bhaiyya: ",c)

# multiplication of digits of a number
# sum = 1
# num1 = num  = int(input("enter the number"))
# num1 = num
# while(num>0):
#     digit = num%10
#     sum = sum*digit
#     num = num//10 
# print("the multiplication of the ",num1,"is: ",sum)


# take an integer as an input from the user
#  and check whether if the number is divisible 
# by sum of digits or not

'''
sum = 0
num  = int(input("enter a number"))
n1 = num
while(num>0):
    sum = sum + num%10
    num = num//10
print("the of the digits of an number is:",sum)
if n1%sum==0:
        print("it is divisible") 
else:
        print("it is not divisible")'''

    
# take an number input from user check 
# if the sum of factors of that number 
# is greater than the original number or not
# if yes print yes else no
# sum = 0
# n = int(input("enter a number"))
# for i in range(1,n/2 +1):
#     if n%i==0:
#         sum+=i
# if sum>0:
#     print("yes")  


# calcualate the difference of sum of numbers that are divisible by 6 and not divisible by 6 in the range of first 30 numbers
# sum = sum1 = 0
# for i in range(1,31):
#     if i%6==0:
#         sum = sum+i
   
#     else:
#         sum1+=i
# print(-(sum-sum1))

 

# n1 = int(input("Enter a number: "))
# rev = 0
# n = n1  # Assign the input number to another variable to keep the original number unchanged

# while(n > 0):
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# if rev == n1:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# nod= 0
# n = 153
# while(n>0):
#   nod = nod+1
#   n = n//10
# sod = 0

# n2 = n
# org = n2
# while(n2>0):
#   digit = n2%10
#   sod =sod +digit**nod
#   n2 = n2//10

# print(sod)

# if sod == org:
#   print("armstrong")
# else:
#   ("none")


# This program is designed to find and 
# print all the factors of a given number 
# and then calculate the sum of those factors.
# num = int(input("Enter an Number : "))
# i=1
# sum=0
# while(i<=num/2):
#     if(num%i==0):
#         print(i,"",end=" ")
#         sum=sum+i
#     i+=1
    
# print("\nSum of ",sum)
  

  











