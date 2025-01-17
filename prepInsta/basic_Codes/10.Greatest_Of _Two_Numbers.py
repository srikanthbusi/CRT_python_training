first = int(input("Enter first number:"))
second = int(input("Enter second number:"))

# if first == second:
#     print("Both are Equal")
# elif first > second:
#     print(str(first) + " is Greater")
# else:
#     print(str(second) + " is Greater")


# if first == second:
#     print("Both are same")
# else:
#     print(str(first) + " is greater than "+str(second) if first>second else str(second)+ " is greater than " + str(first))



if first == second:
    print("Both are same")
else:
    result = (max(first,second))
    print(f"{result} is the greatest number among them")