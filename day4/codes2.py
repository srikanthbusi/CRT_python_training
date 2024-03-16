# lamda and map

def car_company():
    print("The available car companies are Toyota, Mahindra and Mercedes.")
    company = input("Please Enter The Car Company Name: ").capitalize()
    if company == 'T':
        return company_toyota()

# class car:
#  def showroom(self):
#     print("Welcome to our  Car Show Room")
#     print("Select your car")
#     c = input("Enter our car model:")
#     if self.c == "toyota":
#         print("you selected toyota as your car")
    

# busi = car()
# print(busi.showroom())

class car_showroom :
     def brands(self):
          







# class car:
#     def __init__(self,a):
#         print("Welcome sir!!!  Choose  Car Company")
#         car_name = input()
#         if(car_name == "Toyota" or car_name=="Mahindra"or car_name=="Mercedes"):
#             self.company=car_name
#             self.model_variant(car_name)
#         else:
#             print("Invalid Input Please Enter Again ")
            
#     def model_variant(self,c):
#         print("Choose Variant Petrol/Diesel :")
#         variant=input().lower()
#         if(variant=="petrol" or variant=="diesel"):
#             self.variants(c,variant)
#         else:
#             print("Invalid Input Please Enter Again ")
    
#     def variants(self,co,va):
#         print("\nYour Car Details Are As Follows \nCar Company : ",co,"\nVariant : ",va)
        
# def main():
#     c1 = car("Toyota")
#     c2 = car("Mahindra")
#     c3 = car("Mercedes")

# if __name__=='__main__':
#     main()
#         elif car_name.equals(a):
#                  self.mahindra(car_name)
#                  print("your choosen Car Company is Mahindra")
#         elif  car_name == "Mercedes":
#                 self.CarCompany=car_name
#                 self.model(self.CarCompany)
#         else :
#                print("Your entered wrong choice please try again ")
    
    
#     def model(self,company  ):
    


#       def toyota(self):
#          print("Car Models Available In Toyota Are : Petrol & Diesel")
#          model=input("Enter The Model You Want To Choose : ")   
#          self.variants(model,"Toyota")
# cars = car("Toyota")

# class Car:
#     def __init__(self, company, cgst, sgst, insurance):
#         self.company = company
#         self.cgst = cgst
#         self.sgst = sgst
#         self.insurance = insurance

#     def model_name(self, model):
#         print(f"Welcome to {self.company} showroom!")
#         print("Please select the model:")
#         return model

#     def variant(self, model, variant):
#         print(f"You have selected {model} {variant} variant.")
#         return variant

#     def display(self, model, variant, price_ex_showroom):
#         print(f"{model} {variant} variant ex showroom price: Rs. {price_ex_showroom}")
#         price_onroad = price_ex_showroom + self.cgst + self.sgst + self.insurance
#         print(f"{model} {variant} variant onroad price: Rs. {price_onroad}")

# toyota = Car("Toyota", 9, 9, 20000)
# mahindra = Car("Mahindra", 9, 9, 15000)
# mercedes = Car("Mercedes", 12, 12, 50000)

# company = input("Enter the car company (Toyota, Mahindra, Mercedes): ")
# if company.lower() == "toyota":
#     model = input("Please select the model: ")
#     variant = input("Please select the variant (Petrol, Diesel): ")
#     toyota.display(model, variant, 1000000)
# elif company.lower() == "mahindra":
#     model = input("Please select the model: ")
#     variant = input("Please select the variant (Petrol, Diesel): ")
#     mahindra.display(model, variant, 800000)
# elif company.lower() == "mercedes":
#     model = input("Please select the model: ")
#     variant = input("Please select the variant (Petrol, Diesel): ")
#     mercedes.display(model, variant, 2000000)
# else:
#     print("Invalid company selected")

