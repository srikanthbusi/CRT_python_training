l=[22,-1,42,55,1,-4,6]
#write a program to find the second smallest negative number from list
m1=l[0]
m2=l[0]
m3=l[0]
for i in range (len(l)):
    if l[i]<m1:
        m2=m1
        m1=l[i]
print(m1)
print(m2)



