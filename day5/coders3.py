# create an class "ticket" which will be the abstract class inside that
# create an function Book ticket which will be in abstract method
# and has nothing in it.
# create a class "make my trip" which will use the book ticket function 
# from ticket class to take the details such as "name","phno","emailid"
# "journey date" and displays an message saying "thankyou for booking from "make 
# my trip.  create an Class "IRCTC" which uses the "book ticket" of ntticket class
# and takes the same details as "make my trip" but in the end it will give an option to
# user to select whether it is an one way or round trip if the user option is round trip
# it again asks the user to enter the return data as well and then print the message"
# "thank you for choosing" else:thank you for choosing irctc
# create an class indigo which takes all the details as irctc and just asks which mode \
# of transportation do you want to go in train,flight,bus and display ("thanks for choosing Indigo")


# create the class ticket which will be the abstract class inside that create a function book ticket which will be the abstract 
#  method and has nothing in it.create a class make my trip which will use the book ticket fun()
# from ticket class to take the details such as name ,phoneno.,emailid,journey date and displays 
# a msg saying thank u for bookin from makemytrip.create a class irctc which uses the book ticket of ticket class 
# and take the same details as makemytrip but in the end  it will give an option to user to select whether it is one way or round trip.
# if the user option is round trip it again ask the user to enter the return date as well and then prints the msg thank u for
#  choosing irctcc else print the msg thank u for choosing irctcc.create a class indigo which takes all the details as irctc and 
#  just asks which mode of transport u want to go  in train ,flight,bus and displays thank u for choosing indigo

from abc import ABC,abstractmethod
class ticket (ABC):
    @abstractmethod
    def book_ticket(self):
        pass
class make_my_trip(ticket):
    def book_ticket(self):
        print("The Applicant name is:",input())
        print("The  phone number is",input())
        print("The Email_id is :",input())
        print("The journey date : ",input())
        print("Thank you for bookiing from Make My Trip")
class IRCTC(ticket):
    def book_ticket(self):
        print("The Applicant name is:",input())
        print("The  phone number is",input())
        print("The Email_id is :",input())
        print("The journey date : ",input())
        print("Thank you for bookiing from IRCTC Portal")
        print("choose from from the above")
        option  =  input("\n1.One Way \n2.Round way")
        if option == "One Way" or option ==1:
            print("Thank you for choosing Make My Trip!!!")
        elif option == "Round Way" or option ==2:
            print("Enter the return date of your Journey:",input())
            print("Thank you for choosing Make My Trip!!!")
        else:
            print("Thank you for bookiing from IRCTC Portal")







ob2 = IRCTC()
print(ob2.book_ticket())

    