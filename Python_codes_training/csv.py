import csv
f=open("student.csv","a",newline="")
a=csv.writer(f)
a.writerow(["studentid","roll no","name","mobile"])
studentid=int(input("enter studentid:"))
rollno=int(input("enter roll no:"))
name=input("enter name:")
mobile=int(input("enter number:"))
a.writerow([studentid,rollno,name,mobile])
print("student info")
import pandas
csvFile = pandas.read_csv('student.csv')
print(csvFile)