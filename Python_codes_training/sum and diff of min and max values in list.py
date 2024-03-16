l=[12,42,23,96,7,18,10,133]
min=0
max=0
mini=l[0]
maxi=l[0]
for i in range (len(l)):
    if mini>l[i]:
        mini=l[i]
        min=i
    if maxi<l[i]:
        maxi=l[i]
        max=i
print(mini)
print(maxi)
a=mini+maxi
d=maxi-mini
print(a)
print(d)

            
