# Create an ecommerce product where the user can register 
# and login himself,he can see that all the products are 
# present.The products contain name,price,category and 
# stockleft.From these products user can place an order 
# just by the product name and the quantity you want to purchase.
# Once he enters this,a bill should be generated with the
# total amount and the message return,a bill should be generated 
# that order is placed showing order is place.The change of stock
# should be reflected on the change of total products.


from registration import *
import csv
class eccom:
    def  registration(self,username,password,phoneno,pincode,city):
        self.username=username
        self.password = password
        self.phoneno = phoneno
        self.pincode = pincode
        self.city = city
        ob1.registration("username","password","phoneno","pincode","city")
        username = input("Enter the User Name: ")
        password = input("Enter the required password : ")
        phoneno = int(input("Enter your phone Number : "))
        pincode = int(input("Enter the pincode"))
        city = input("Enter your City name:")
        print("Thank You for your Patience for Registering!!!!!")
        
        with open("registration.csv","a",newline="") as file:
          file = csv.writer(file)
          file.writerow([self.username,self.password,self.phoneno,self.pincode,self.city])
        

    def  login(self,username,password):
        # self.username=username
        # self.password = password
        
        # ob1.login("username","password")
        print("*******Please Enter Login to your Account*******")
        username = input("User_Name:")
        password = input("password:")
        with open("registration.csv","a",newline="") as file2:
           file2 = csv.DictReader(file2)
           for logins in file2:
            if logins["User_Name"] == username and logins["password:"] == password:
              print("The user Credentials are Correct")
              break
            else:
              print("Invalid Credentials")
           
        
        
        # for row in file :
        #   if row[username] == "Srikanth" and row[password] == 7981751544 and row[phoneno] == 7981751544 and row[pincode] and[city]:
            
        # return False

             
        
ob1 = eccom()

        