# # calculate the sum of digits of a number which is taken as input from the user
# sum = 0
# num = int(input("enter the sequence of numbers"))
# while num>0:
#     sum = sum +(num%10)
#     num = num/10
# print(int(sum))   


# ''' Calc the sum of digits of a number '''

# n = int(input("Enter a Number : "))
# sum=0
# while n != 0 :
#     temp = n%10
#     sum =sum+ temp

#     n= int((n/10))

# print(sum)
# 231.21222

# Read a line of space-separated integers from the user
input_string = input("Enter integers separated by spaces: ")

# Split the string into a list where each element is a substring between spaces
input_list = input_string.split()
# print(max(input_list))

# # Convert each list element to an integer
# int(item)
integers = [int(item)for item in input_list]
print(max(integers))

# print(integers)  # Outputs the list of integers

 