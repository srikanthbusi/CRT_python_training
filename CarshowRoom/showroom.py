# in a show room there are 3 car companies toyota mahindra and mercedes
# take  the input from user for the car model company name and in the input message give the 
# user the three options of these three companies that user input company name goes as the 
# input//Argument to model name function,which welcomes the user accordingly to the company name(print company).
# the first function ask the user to enter the specific model name for that company("please select the model")
# the second function whose name is variant according to the car company name and car model the user should 
# be asked to enter the varaint he would like to choose from petrol and dieseal
# the last function display must be display according to  the car company, car model name,car variant first 
# it's ex showroom price must be displayed and then it's onroad price must be displayed,which is calculated as 
# ex showroom price + cgst +sgst +insurance.  The sgst,cgst  and insurance must have a common value trouhout the car showroom
# then car price.
from Honda import *
from Mahindra import *
from Toyota import *


class Showroom:
    def __init__(self):
        # self.model = None
        # self.variant = None
        # self.cgst="5%"
        # self.cal_cgst=5/100
        # self.sgst="12%"
        # self.cal_sgst=12/100
        # self.ins="50%"
        # self.cal_ins=50/100
        print("###### --Welcome to BUSI's Car Showroom-- #########\nPlease select the car Company from the above:")
        print("\n1.Mahindra\n2.Honda\n3.Toyota")

    def choose(self):
        while True:
            chosecae = input()
            if chosecae == "1" or chosecae.lower() == "mahindra":
                Mahindra()
                break  # Call the Mahindra function as an instance method
            elif chosecae == "2" or chosecae.lower() == "honda":
                Honda()
                break 
            elif chosecae == "3" or chosecae.lower() == "toyota":
                Toyota() 
                break
            else:
                print("Invalid option!!!!!!!!\nPlease checkout the available companies from the above")
                continue
            
cars = Showroom()
cars.choose()



# cars = Showroom()
# cars.choose()

# from Honda import *
# from Mahindra import *
# from Toyota import *

# class Showroom:
#     def __init__(self):
#         self.model = None
#         self.variant = None
#         self.chosen_car = None  # To store the chosen car details
#         print("###### --Welcome to BUSI's Car Showroom-- #########\nPlease select the car Company from the above:")
#         print("\n1.Mahindra\n2.Honda\n3.Toyota")

#     def choose(self):
#         while True:
#             chosecae = input()
#             if chosecae == "1" or chosecae.lower() == "mahindra":
#                 self.chosen_car = Mahindra()  # Store the instance of the chosen car
#                 break
#             elif chosecae == "2" or chosecae.lower() == "honda":
#                 self.chosen_car = Honda()
#                 break 
#             elif chosecae == "3" or chosecae.lower() == "toyota":
#                 self.chosen_car = Toyota() 
#                 break
#             else:
#                 print("Invalid option!!!!!!!!\nPlease checkout the available companies from the above")
#                 continue 
    
#     def display_chosen_car(self):
#         if self.chosen_car is not None:
#             print("Chosen Car Details:")
#             print("Model:", self.chosen_car.model)
#             print("Variant:", self.chosen_car.variant)
#         else:
#             print("No car chosen yet")

    # def Toyota(self,fortuner,crysta,glanza):
    #     print("Thanks for choosing Toyota Company\nWhich type  of models do you want")
    #     print("The models for Toyota are:\n1.Fortuner | Starting ₹30.99 Lakh\n2. Innova Crysta | Starting ₹19.99 Lakh\n3.Glanza | Starting ₹6.81 Lakh")
    #     while True:
    #         models = input()
    #         if models =="1" or models.lower()=="fortuner":
    #             self.fortuner = self.fortuner
    #             print("Thanks for choosing Fortuner :")
    #             variant()
    #             return "Fortuner"
    #         elif models =="2" or models.lower()=="innova crysta":
    #             self.crysta = self.crysta
    #             print("Thanks for choosing Innova Crysta :")
    #             variant()
    #             return "Innova Crysta"
    #         elif models =="3" or models.lower()=="glanza":
    #             self.glanza = self.glanza
    #             print("Thanks for choosing Glanza :")
    #             variant()
    #             return "Glanza"
    #         else:
    #             print("Sorry we have only this limited Models") 
    #             continue 

    # def variant(self,):
    #     print("Please select your variant:\n1.Petrol\n2.Diesel")
    #     while True:
    #         vari = input()
    #         if vari == "1" or vari=="petrol":
    #             print("Thanks for choosing Petrol Variant which can occupy 30 liters ")
    #             return "Petrol"
    #         elif vari == "2" or vari=="diesel":
    #             print("Thanks for choosing Diesel Variant which can occupy 40 liters ")
    #             return "Diesel"
    #         else:
    #             print("Sorry presently we are maintaining these two variants only")
    #             continue
    # def Mahindra():
    #     print("Thank you for choosing Mahindra Company\nWhich type  of models do you want")
    #     print("\n1.Thar price (Rs. 11.25 - 17.60 Lakh)\n2.Scorpio price (Rs. 13.59 - 17.35 Lakh)\n3.XUV700 price (Rs. 13.99 - 26.99 Lakh)")
    #     while(True):
    #         models = input()
    #         if models =="1" or models.lower() =="thar":
    #             print("Thanks for choosing *Thar*:")
    #             variant()
    #             break
    #         elif models =="2"or models.lower() =="scorpio":
    #             print("Thanks for choosing *Scorpio* :")
    #             variant()
    #             break
    #         elif models =="3" or models.lower() =="XUV700":
    #             print("Thanks for choosing *XUV700* :")
    #             variant()
    #             break
    #         else:
    #             print("Sorry we have only this limited Models")
    #             continue

    # def variant():
    #     print("Please select your variant:\n1.Petrol\n2.Diesel")
    #     while True:
    #         vari = input()
    #         if vari == "1" or vari=="petrol":
    #             print("Thanks for choosing Petrol Variant which can occupy 30 liters ")
    #             break
    #         elif vari == "2" or vari=="diesel":
    #             print("Thanks for choosing dieasel Variant which can occupy 40 liters ")
    #             break
    #         else:
    #             ("Sorry presently we are maintaing these two variants only")
    #             continue
    # def Honda():
    #     print("\nThank you for choosing Honda Company\nWhich type  of models do you want")
    #     print("\n1.Amaze price (Rs. 11.25 - 17.60 Lakh)\n2.City price (Rs. 13.59 - 17.35 Lakh)\n3.Elevate price (Rs. 13.99 - 26.99 Lakh)")
    #     while True:
    #         models = input()
    #         if models =="1" or models.lower()=="amaze":
    #             print("Thanks for choosing *Amaze* please select your variant :")
    #             variant()
    #             break
    #         elif models =="2" or models.lower()=="city ":
    #             print("Thanks for choosing *City * please select your variant :")
    #             variant()
    #             break
    #         elif models =="3" or models.lower()=="elevate":
    #             print("Thanks for choosing *Elevate* please select your variant :")
    #             variant()
    #             break
    #         else:
    #             print("Sorry we have only this limited Models") 
    #             continue 
    # def variant():
    #     print("Please select your variant:\n1.Petrol\n2.Diesel")
    #     while True:
    #         vari = input()
    #         if vari == "1" or vari=="petrol":
    #             print("Thanks for choosing Petrol Variant which can occupy 30 liters ")
    #             break
    #         elif vari == "2" or vari=="diesel":
    #             print("Thanks for choosing dieasel Variant which can occupy 40 liters ")
    #             break
    #         else:
    #             ("Sorry presently we are maintaing these two variants only")
    #             continue


# display()
# cars.display_chosen_car()  # Display the chosen car details

# cars.Toyota()
# cars.variant()
# cars.Mahindra()
# cars.variant()
# cars.Honda()
# cars.variant()




              