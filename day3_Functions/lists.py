# creation of lists
list = [1,"56,","L","Yoyo",36.55,True]  #initialization
print(list)     #accessing      
print(list[1:3])  #slicing
print(list[5])
for i in list:
    print(i,end =" //")      #looping
list1 = [1,45.36,"hello","guru"]
(list.append(list1))      #appending
print(list)
list1.insert(1,"mowayoyo")   #insertion
print(list1)
list[5]=False   #mutability
print(list[::-2])

list3 = [["hello","guru","mowa"],["bagunnava","tinam","tellarinda"],["podukora","rey"]]
for acces in list3:
    print(acces)
    
