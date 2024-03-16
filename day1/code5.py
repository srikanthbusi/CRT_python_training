# check if the year is leap year or not
# 1. if the t=year is divisible by 4 and not divisible by 100  or if it is diivisible by 400 then it is called as leap year

year = int(input("enter the year"))
if year%4==0 and (year%100!=0) or year%400==0:
    print("leap year")
else:
    print("not leap year")