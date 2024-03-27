# # Fibanocci series
# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(3,11):
#     c = a+b
#     print(c)
#     a = b
#     b = c


# n = int(input("Enter N value : "))
# i=0
# j=1
# print("0 1",end=" ")
# sum = i+j

# for i in range(2,n):
   
#     print(sum, end=" ")
#     i=j
#     j=sum
#     sum=i+j


# printing the Fibanocci  series in list
n = int(input())
i =0
j=1
list1 = [0,1]
for num in range(2,n):
    k = i+j
    list1.append(k)
    i=j
    j=k
print(list1)    
    