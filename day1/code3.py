 #write an program  to input from user 
# if the integer that is divisable by 
# 3 and 6 print good number,
# 2 and 7 print average number 
# 4 or 9 print Awesome number
# else bad number
num = int(input("Enter an Number : "))
if num%3==0 and num%6==0:
    print("good number")
elif num%2==0 and num%7==0:
    print("average number")
elif num%4==0 and num%9==0:
    print("Awesome number")
else:
    print("bad number")