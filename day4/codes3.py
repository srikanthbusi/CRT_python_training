# # [2,0,1024,0,40,230,0]  shift all the zeroes to the right side

list1 = [2,0,1024,0,40,230,0]
for i in range(len(list1)):
    if list1[i] == 0:
        j=i+1
        while j < len(list1) and list1[j]==0:
            j+=1
        if j < len(list1):
            k=i
            list1.insert(k,list1.pop(j))
print(' '.join(map(str,list1)))


list1 = [2,0,1024,0,40,230,0]
for i in range(len(list1)):
    if list1[i] == 0:
        j=i+1
        while j < len(list1) and list1[j]==0:
            j+=1

list  = [2,0,4,0,34,553,0,34444,3454,0,45555]



print(len(list))

list2 = []

list1 = [2,0,1024,0,40,230,0]
for i in list1:
    if i!= 0:
        list2.append(i)
for i in list1:
    if i==0:
        list2.append(i)