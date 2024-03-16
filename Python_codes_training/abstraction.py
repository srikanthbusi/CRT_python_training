""" create a class ticket which will be the absract inside that
create a function bookticket which will be the abstract method
 and has nothing in it.create a class makemytrip which
will use the bookticket function from ticket class to
take the details such as name,phone number,email id,journey date
and displays a msg saying thank u for booking from bookmytrip.
create a class irctc which uses te book ticket of ticket class
and takes the same details as makemytrip but in the end 
it will given option to user to select whether it is
oneway or round trip.if the user option is round trip
it again asks the user to enter the return date as well
and then print the msg thanku for choosing irctc else
print the msg thanku for choosing irctc.create a class indigo
which takes alla the details as irctc and just asks
which mode transport who want to go with:train,flight or bus
and displays thanku fro choosing indigo"""

from abc import ABC,abstractmethod
class ticket(ABC):
     @abstractmethod
     def bookticket(self,name,phone,email,jd):
         
         
         
                         
         pass
class makemytrip(ticket):
    def bookticket(self,name,phone,email,jd):
        print("thank you for choosing")
        
        
class irctc(ticket):
    def bookticket(self,name,phone,email,jd):
        
        print("Thank you for booking from MakeMyTrip.")
        triptype = input("Enter trip type (oneway / round): ").lower()
        if triptype == "round":
            returndate = input("Enter return date: ")
            print("Thank you for choosing IRCTC for a round trip.")
        else:
            print("Thank you for choosing IRCTC for a one way trip.")

class indigo(ticket):
    def bookticket(self,name,phone,email,jd):
        modeoftransport = input("Enter mode of transport (train/flight/bus): ")
        print("Thank you for choosing Indigo.")
        
obj1=makemytrip()
obj1.bookticket("sat","5756767678","sat@gmail.com","21-22-2024")

obj2=irctc()
obj2.bookticket("nav","787","nav@gmail.com","21-22-2024")

obj3=indigo()
obj3.bookticket("nav",'546',"nav@gmail.com","21-22-2024")
    