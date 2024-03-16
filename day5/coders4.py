# create an Atm System 
# task 1: display the remaining amount in the Atm
# task 2: Authentication of user (userbane and password) if the user is authenticated 
# then give him following options to choose
# 1. check Balance
# 2.Cash Withdrawal  and also see remaining balance
# 3.Cash Deposit     and also see remaining balance
# 4.mini Statement of the last three transactions
# 5.card renewal providing 
# rupay,vissa,mastercard
#create an atm system
#displaying the reaming amount in atm
#select the card rupay-2k limit,visa-5k limit,mastercard-8klimit
#authenticate the user if the user is authenticated then
#giving the following option1 1.(check balance)
                            #2.(cash deposite)
                            #3.(cashwithdraw)
#mini statement of the last three transaction

# class Car:
#     def __init__(self):
#         self.cgst = 0.12  # Assuming common CGST rate
#         self.sgst = 0.12  # Assuming common SGST rate
#         self.insurance = 15000  # Assuming common insurance cost

#     def welcome(self, company):
#         print(f"Welcome to the {company} Showroom")
#         print("###############################")

#     def choose_model(self, company):
#         print(f"Please select the model for {company}:")
#         if company.lower() == "toyota":
#             print("1. Fortuner\n2. Innova Crysta\n3. Glanza")
#         elif company.lower() == "mahindra":
#             print("1. Thar\n2. Scorpio\n3. XUV700")
#         elif company.lower() == "mercedes":
#             print("1. Benz E-Class\n2. Benz AMG GT 4 Door Coupe\n3. Benz G-Class")
#         else:
#             print("Invalid company name")

#     def choose_variant(self):
#         print("Please select the variant:\n1. Petrol\n2. Diesel")
#         variant_choice = input()
#         if variant_choice == "1":
#             return "Petrol"
#         elif variant_choice == "2":
#             return "Diesel"
#         else:
#             print("Invalid variant choice")

#     def calculate_on_road_price(self, ex_showroom_price):
#         cgst_amount = ex_showroom_price * self.cgst
#         sgst_amount = ex_showroom_price * self.sgst
#         insurance_amount = self.insurance
#         return ex_showroom_price + cgst_amount + sgst_amount + insurance_amount

#     def display(self, company, model, variant, ex_showroom_price):
#         print("###############################")
#         print("Car Company:", company)
#         print("Car Model:", model)
#         print("Car Variant:", variant)
#         print("Ex-showroom Price: ₹", ex_showroom_price)
#         on_road_price = self.calculate_on_road_price(ex_showroom_price)
#         print("On-road Price: ₹", on_road_price)

#     def brands(self):
#         print("###############################")
#         print("Choose from the above brands: \n1. Toyota\n2. Mahindra\n3. Mercedes ")
#         company = input("Enter the company name (Toyota/Mahindra/Mercedes): ")
#         self.welcome(company)
#         self.choose_model(company)
#         model_choice = input()
#         if company.lower() == "toyota":
#             if model_choice == "1":
#                 self.variant()
#                 self.display("Toyota", "Fortuner", "variant", 3099000)
#             elif model_choice == "2":
#                 self.variant()
#                 # Display other models and proceed similarly
#             elif model_choice == "3":
#                 self.variant()
#                 # Display other models and proceed similarly
#             else:
#                 print("Invalid model choice")
#         elif company.lower() == "mahindra":
#             if model_choice == "1":
#                 self.variant()
#                 # Display other models and proceed similarly
#             elif model_choice == "2":
#                 self.variant()
#                 # Display other models and proceed similarly
#             elif model_choice == "3":
#                 self.variant()
#                 # Display other models and proceed similarly
#             else:
#                 print("Invalid model choice")
#         elif company.lower() == "mercedes":
#             if model_choice == "1":
#                 self.variant()
#                 # Display other models and proceed similarly
#             elif model_choice == "2":
#                 self.variant()
#                 # Display other models and proceed similarly
#             elif model_choice == "3":
#                 self.variant()
#                 # Display other models and proceed similarly
#             else:
#                 print("Invalid model choice")
#         else:
#             print("Invalid company choice")

#     def variant(self):
#         variant = self.choose_variant()
#         if variant:
#             if variant == "Petrol":
#                 print("Thanks for choosing Petrol Variant")
#             elif variant == "Diesel":
#                 print("Thanks for choosing Diesel Variant")


# car1 = Car()
# car1.brands()
# car1.display()
# from abc import ABC, abstractmethod

# class Ticket(ABC):
#     @abstractmethod
#     def book_ticket(self):
#         pass

# class MakeMyTrip(Ticket):
#     def book_ticket(self):
#         name = input("Enter your name: ")
#         phone_no = input("Enter your phone number: ")
#         email_id = input("Enter your email address: ")
#         journey_date = input("Enter the journey date: ")
#         print(f"Thank you for booking with MakeMyTrip, {name}!")

# class IRCTC(Ticket):
#     def book_ticket(self):
#         name = input("Enter your name: ")
#         phone_no = input("Enter your phone number: ")
#         email_id = input("Enter your email address: ")
#         journey_date = input("Enter the journey date: ")
#         trip_type = input("Select trip type (one-way/round-trip): ").lower()
#         if trip_type == "round-trip":
#             return_date = input("Enter the return date: ")
#             print(f"Thank you for choosing IRCTC! Your round-trip is booked from {journey_date} to {return_date}.")
#         else:
#             print("Thank you for choosing IRCTC!")

# class Indigo:
#     def _init_(self, irctc):
#         self.irctc = irctc

#     def choose_transport_mode(self):
#         print("Select mode of transport: Flight, Bus, or Train")
#         mode = input("Enter your choice: ")
#         print(f"You have chosen {mode} with IRCTC.")

# # Example usage
# # if _name_ == "_main_":
#     mmtrip = MakeMyTrip()
#     mmtrip.book_ticket()

#     irctc = IRCTC()
#     irctc.book_ticket()

#     indigo = Indigo(irctc)
#     indigo.choose_transport_mode()


