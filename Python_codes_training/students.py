"""create a e commerce website where user can login after login where we can see all the products and the 
products contain the name price category stockinfo . the user can add the product,from these products user
can place an order just by the product name and the quantity he want to purchase,once he enters this a bill
should be gernrated with a total amount ,and message should be given as order is placed,complete the payment
of the delivery the change of stock should be reflected on the list of stocks"""
import csv
f=open("students.csv","a",newline="")
a=csv.writer(f)
a.writerow(["studentid","roll no","name","mobile"])
studentid=int(input("enter studentid:"))
rollno=int(input("enter roll no:"))
name=input("enter name:")
mobile=int(input("enter number:"))
a.writerow([studentid,rollno,name,mobile])
print("student info")

file2=open("students.csv","r")
print(file2.readlines())

