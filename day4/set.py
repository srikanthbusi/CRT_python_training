myself= {1,3,"srikanth","teja","prudhvi","nandan","455.645"}
print(myself[0]) # prints 1
print(len(myself)) # prints the length of list i.e., 6
print("Element at index 2 is :",myself[2]) # prints "Element at index 2 is : srikanth"</s>
myself.update()

fs = frozenset(myself)
print("\nFrozen Set:")
print(fs)
# Adding an element to a FrozenSet raises TypeError


# class car:
#     def __init__(self):
#         print("Welcome to/\ **BSK** /\Showroom")
#         print("###############################")
#         print("Please Choose your Car brands")
#     def brands(self,toyota,mahindra,mercedes,other):
#                 print("###############################")
#                 print("Choose from the above brands: \n1.Toyota\n2.Mahindra\n3.Mercedes ")
#                 brand  = int(input())
#                 if brand ==1:
#                        print("Thanks for choosing Toyota Company",toyota)
#                        self.Fortuner = toyota
#                        car1.Model_toyota(Fortuner=1,Innova_Crysta=2,Glanza=3,others=4)

#                 elif brand ==2:
#                        print("Thanks for choosing Mahindra Company",mahindra)
#                        self.thar = mahindra
#                        car1.Model_Mahndra(Thar=1,Scorpio=2,XUV700=3,othermodel=4)
#                 elif brand ==3:
#                        print("Thanks for choosing Mercedes Company",mercedes)
#                        self.Benz_E_Class = mercedes
#                        car1.Model_Mercedes(Benz_E_Class=1,Benz_AMG_GT_4_Door_Coupe=2,Benz_G_Class=3 ,othermodels=4)
#                 else:
#                        print("Sorry we have only this limited companies",other)
#     def Model_toyota(self,Fortuner,Innova_Crysta,Glanza,others):
#                         print("The models for Toyota are:\n1.Fortuner | Starting ₹30.99 Lakh\n2. Innova Crysta | Starting ₹19.99 Lakh\n3.Glanza | Starting ₹6.81 Lakh",Fortuner,Innova_Crysta,Glanza)
#                         models = int(input())
#                         if models ==1:
#                           print("Thanks for choosing **Fortuner** please select your variant :")
#                           self.petrol = Fortuner
#                           car1.variant(petrol=40,diesel=55)
#                         elif models ==2:
#                           print("Thanks for choosing **Innova Crysta** please select your variant :")
#                           self.petrol = Innova_Crysta
#                           car1.variant(petrol=40,diesel=55)
#                         elif models ==2:
#                           print("Thanks for choosing **Glanza** please select your variant :")
#                           self.petrol = Glanza
#                           car1.variant(petrol=40,diesel=55)
#                         else:
#                           print("Sorry we have only this limited Models",others)  
    
#     def Model_Mahndra(self,Thar,Scorpio,XUV700,othermodel):
#                         print("The models for Toyota are:\n1.Thar price (Rs. 11.25 - 17.60 Lakh)\n2. Scorpio price (Rs. 13.59 - 17.35 Lakh)\n3.XUV700 price (Rs. 13.99 - 26.99 Lakh)",Thar,Scorpio,XUV700,othermodel)
#                         models = int(input())
#                         if models ==1:
#                           print("Thanks for choosing **Thar** please select your variant :")
#                           self.petrol = Thar
#                           car1.variant(petrol=40,diesel=55)
#                         elif models ==2:
#                           print("Thanks for choosing **Scorpio** please select your variant :")
#                           self.petrol = Scorpio
#                           car1.variant(petrol=40,diesel=55)
#                         elif models ==3:
#                           print("Thanks for choosing **XUV700** please select your variant :")
#                           self.petrol = XUV700
#                           car1.variant(petrol=40,diesel=55)
#                         else:
#                           print("Sorry we have only this limited Models",othermodel)
#     def Model_Mercedes(self,Benz_E_Class,Benz_AMG_GT_4_Door_Coupe,Benz_G_Class ,othermodels):
#                         print("The models for Toyota are:\n1.Benz E-Class price (₹75 Lakh - ₹88 Lakh)\n2.Benz AMG GT 4 Door Coupe price (₹3.3 Crore)\n3.Benz G-Class price (₹2.6 Crore)",Benz_E_Class,Benz_AMG_GT_4_Door_Coupe,Benz_G_Class ,othermodels)
#                         models = int(input())
#                         if models ==1:
#                           print("Thanks for choosing **Benz E-Class price** please select your variant :")
#                           self.petrol = Benz_E_Class
#                           car1.variant(petrol=40,diesel=55,othervari=2)
#                         elif models ==2:
#                           print("Thanks for choosing **Benz AMG GT 4 Door Coupe** please select your variant :")
#                           self.petrol = Benz_AMG_GT_4_Door_Coupe
#                           car1.variant(petrol=40,diesel=55,othervari=2)
#                         elif models ==3:
#                           print("Thanks for choosing **Benz G-Clas** please select your variant :")
#                           self.petrol = Benz_G_Class
#                           car1.variant(petrol=40,diesel=55,othervari=2)
#                         else:
#                           print("Sorry we have only this limited Models",othermodels)                      
                        
#     def variant(self,petrol,diesel,othervari):
#             print("Please select your variant:\n1.Petrol\n2.Diesel")
#             vari = int(input())
#             if vari == 1:
#              print("Thanks for choosing Petrol Variant which can occupy",petrol,"liters ")
#             elif vari == 2:
#              print("Thanks for choosing dieasel Variant which can occupy",diesel,"liters ")
#             else:
#                     ("Sorry presently we are maintaing these two variants",othervari," only")

#     def display(self):
#           print("the car company",self.toyota)
#           print("car model name,car variant,ex showroom price:",self.mahindra)
        
#         # print("the fan speed:",self.regulatorspeed)
          
          
               
# # class toyota
# # class 



# car1 = car()
# car1.brands(toyota=1,mahindra=2,mercedes=3,other=4)
# print(car1.display)

 # in a show room there are 3 car companies toyota mahindra and mercedes
# take  the input from user for the car model company name and in the input message give the 
# user the three options of these three companies that user input company name goes as the 
# input//Argument to model name function,which welcomes the user accordingly to the company name(print company).
# the first function ask the user to enter the specific model name for that company("please select the model")
# the second function whose name is variant according to the car company name and car model the user should 
# be asked to enter the varaint he would like to choose from petrol and dieseal
# the last function display must be display according to  the car company, car model name,car var…
#######################################################################################################