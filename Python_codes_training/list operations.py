#craetion of list
l=[1,2,3,"sat","nav"]
print(l)

#accesing
print(l[4])

#slicing
print(l[2::])
print(l[2:4])
print(l[::-1])
print(l[0:5:2])


#loop acess
for i in l:
    print(i)

#appending
l.append(4)
print(l)

#removing
l.remove("hi")
print(l)

#inserting
l.insert(2,"sss")
print(l)

#deleting
l.clear()
print(l)

#regaining
l=[1,2,3,"sat","nav"]

#multidimensional list
l1=[[1,2,3,"sat"],["sss","nav"]]
print(l1)

#multidimensional list accesing
print(l1[1][0])

#updating list
l1[1][0]="sn"
l[1]="ns"
print(l1)
print(l)

