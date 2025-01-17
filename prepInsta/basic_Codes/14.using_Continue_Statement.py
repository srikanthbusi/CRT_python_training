# Problem Statement
# Write a program to print all numbers between two intervals, namely low and high. But, with a special condition that numbers divisible by 5 must not be printed and skipped. (Do this using continue Statement)

# Sample Input

# 1 10

# Sample Output

# 1 2 3 4 6 7 8 9

 

# Sample Input

# 10 20

# Sample Output

# 11 12 13 14 16 17 18 19

 

 

# low, high = input("Enter the two numbers: ").split()

# for i in range(int(low), int(high)+1):
#     if i % 5 == 0:
#         continue
#     print(i, end=" ")


low,high = map(int,input("Enter the two numbers:").split())
for i in range(low,high+1):
    if i%5==0:
        continue
    print(i,end= " ")