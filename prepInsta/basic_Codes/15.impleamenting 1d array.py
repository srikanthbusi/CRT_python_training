# num = int(input("Enter the size of the array: "))
# arr = []
# print("Please enter the required numbers: ")
# for  i in range(num):
#     arr.append(int(input()))

# print("Hence the final numbers are: ")
# for i in range(num):
#     print(arr[i],end=", ")

num = int(input("Enter the Size of Array :"))
arr = [int(x) for x in input("Enter the Elements : ").split()]


print("The elements are : ")

for i in range(num):
    print(arr[i], end=" ")


num = int(input("Enter the Size of Array :"))
arr = []

print("Enter the numbers")
while num > 0:
    arr.append(int(input()))
    num -= 1

print("The elements are : ")

for item in arr:
    print(item, end=" ")
