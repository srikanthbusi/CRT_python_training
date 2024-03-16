# calculate the sum of digits of a number which is taken as input from the user
sum = 0
num = int(input("enter the sequence of numbers"))
while num>0:
    sum = sum +(num%10)
    num = num/10
print(int(sum))   


''' Calc the sum of digits of a number '''

n = int(input("Enter a Number : "))
sum=0
while n != 0 :
    temp = n%10
    sum =sum+ temp

    n= int((n/10))

print(sum)
231.21222


 