first = int(input("Enter first number:"))
second = int(input("Enter second number:"))
third = int(input("Enter second number:"))

if first>=second and first>=third:
    print(f"{first} is the greatest number")

elif second>=first and second>=third:
    print(f"{second} is the greatest number")
else:
    print(f"{third} is the greatest number")

temp = first if first > second else second
result = temp if temp > third else third
print(f"{result} is the greatest number")

print(max(first,second,third))

result = max(first, max(second, third))
print(str(result) + " is greatest")


first = int(input("Enter first number:"))
second = int(input("Enter second number:"))
third = int(input("Enter third number:"))

if first > second and first > third:
    print(str(first) + " is greatest")
elif second > first and second > third:
    print(str(second) + " is greatest")
else:
    print(str(third) + " is greatest")


