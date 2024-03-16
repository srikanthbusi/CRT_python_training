t=(1,2,3,"hi","hlo")
print(t)
print(t[2])
print(t[2::])

t=t+("sn",)
print(t)

for i in range(5):
    n=int(input("enter"))
    t=t+(n,)
print(t)