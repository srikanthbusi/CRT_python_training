list= [12,42,23,96,7,18,10,133]
# addition of minimum and maximum
min = list[0]
max = list[0]
mini = 0
maxi= 0

for i in range(len(list)):
    if min>list[i]: 
        # min  12>12  12>42 12>7
        min =list[i]   # 7 is strored
        mini = i      
    if max<list[i]:
        max =list[i]
        maxi = i 
s = min + max
d = maxi - min
list[mini] = d
list[maxi] = s
print(d)
print(s)

