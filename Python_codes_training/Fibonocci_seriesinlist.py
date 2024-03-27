n = int(input())
i =0
j = 1
list1 = [0,1]
for num in range(2,n):
    k = i+j
    list1.append(k)
    i=j
    j=k
print(list1)    
    