num = int(input("Enter a Number:"))
if num % 2 == 0:
    print("Given number is Even")
else:
    print("Given number is Odd")

num = int(input("Enter a Number:"))

result = "Even" if num % 2 == 0 else "Odd"
print(result)

def isEven(num):

    # n&1 is 1, then odd, else even
    return not(num & 1)


num = int(input("Insert a number:"))
print("Even" if isEven(num) else "Odd")