# w , a ,program to find the smallest negative number and second smallest number from the list without using min max keywords or sort function
m1 = 999
m2 = 999
list1 = [22,-1,42,65,1,-4,6]
for i in range(len(list1)):
    if list1[i] < m1:
        m1 = list1[i]
print("Minimum value is:",m1)
# seperate for loop for second minimum
for  i in range(len(list1)):
    if list1[i]<m2 and list1[i]!=m1:
        m2 = list1[i] 
print("minimum second value is:",m2)



# another method
m1 = 999
m2 = 999
list1 = [22,-1,42,65,1,-4,6]
for i in range(len(list1)):
    if list1[i] < m1:
        m1 = list1[i]
    elif m2>a[i]
print("Minimum value is:",m1)
# seperate for loop for second minimum
for  i in range(len(list1)):
    if list1[i]<m2 and list1[i]!=m1:
        m2 = list1[i] 
print("minimum second value is:",m2)
