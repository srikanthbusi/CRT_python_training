marks = int(input())
if marks < 0 or marks > 100:
    print("Invalid")
elif marks < 50:
    print("F")
elif marks >= 50 and marks<60:
    print("D")
elif marks >= 60 and marks<70:
    print("c")
elif marks >= 70 and marks<80:
    print("B") 
elif marks >=80 and marks<90:
    print("A")
else:
    print("A+")



marks=int(input("Enter your marks: "))
if marks<0 or marks>100:
  print("invalid")
elif marks<50:
  print("Grade F")
elif marks<60:
  print("Grade D")
elif marks<70:
  print("Grade C")
elif marks<80:
  print("Grade B")
elif marks<90:
  print("Grade A")
else:
  print("Grade A+")