base = int(input("Enter the base number: "))
expo = int(input("Enter the exponential number: "))
res = 1
# i = 0
# while i < expo:
#     res *= base
#     i+=1
# print(res)
# for i in range(expo):
#     res *= base
# print(res)


while expo !=0:
    res *= base
    expo -= 1
print(res)
# for i in range(1, expo+1):
#     result = result * base

# for i in range(expo, 0, -1):
#     result *= base

# for expo in range(expo, 0, -1):
#     result *= base

