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


class car:
    def _init_(self):
        self.cgst = 0.12  # Assuming common CGST rate
        self.sgst = 0.12  # Assuming common SGST rate
        self.insurance = 15000  # Assuming common insurance cost

        print("Welcome to/\ *BSK* /\Showroom")
        print("###############################")
        print("Please Choose your Car brands")
    def brands(self):
                print("###############################")
                print("Choose from the above brands: \n1.Toyota\n2.Mahindra\n3.Mercedes ")
                brand  = input()
                if brand =="1"or brand.lower() =="toyota":
                       print("Thanks for choosing Toyota Company")
                       car1.Model_toyota()
                elif brand =="2"or brand.lower()=="mahindra":
                       print("Thanks for choosing Mahindra Company")
                       car1.Model_Mahndra()
                    
                elif brand =="3" or brand.lower() =="mercedes":
                       print("Thanks for choosing Mercedes Company")
                       car1.Model_Mercedes()
                    
                else:
                    print("Sorry we have only this limited companies")
                  
                      
    def Model_toyota(self):
                   print("###############################")
                   print("The models for Toyota are:\n1.Fortuner | Starting ₹30.99 Lakh\n2. Innova Crysta | Starting ₹19.99 Lakh\n3.Glanza | Starting ₹6.81 Lakh")                         
                   models = input()
                   if models =="1" or models=="fortuner":
                    print("Thanks for choosing *Fortuner* please select your variant :")
                    car1.variant(petrol=40,diesel=55)
                    self.display("Toyota", "Fortuner", "Petrol", 3099000)
                   elif models =="2" or models=="innova crysta":
                     print("Thanks for choosing *Innova Crysta* please select your variant :")
                     car1.variant(petrol=40,diesel=55)
                   elif models =="3" or models=="glanza":
                          print("Thanks for choosing *Glanza* please select your variant :")
                          car1.variant(petrol=40,diesel=55)
                   else:
                          print("Sorry we have only this limited Models")  
    
    def Model_Mahndra(self):
                        print("The models for Toyota are:\n1.Thar price (Rs. 11.25 - 17.60 Lakh)\n2. Scorpio price (Rs. 13.59 - 17.35 Lakh)\n3.XUV700 price (Rs. 13.99 - 26.99 Lakh)")
                        models = input()
                        if models =="1" or models =="thar":
                          print("Thanks for choosing *Thar* please select your variant :")
                          car1.variant(petrol=40,diesel=55)
                        elif models =="2"or models =="scorpio":
                          print("Thanks for choosing *Scorpio* please select your variant :")
                          car1.variant(petrol=40,diesel=55)
                        elif models =="3" or models =="XUV700":
                          print("Thanks for choosing *XUV700* please select your variant :")
                          car1.variant(petrol=40,diesel=55)
                        else:
                          print("Sorry we have only this limited Models")
    def Model_Mercedes(self):
                        print("The models for Toyota are:\n1.Benz E-Class price (₹75 Lakh - ₹88 Lakh)\n2.Benz AMG GT 4 Door Coupe price (₹3.3 Crore)\n3.Benz G-Class price (₹2.6 Crore)")
                        models = input()
                        if models =="1" or models=="Benz E-Class price":
                          print("Thanks for choosing *Benz E-Class price* please select your variant :")
                          car1.variant(petrol=40,diesel=55,othervari=2)
                        elif models =="2" or models =="Benz AMG GT 4 Door Coupe":
                          print("Thanks for choosing *Benz AMG GT 4 Door Coupe* please select your variant :")
                          car1.variant(petrol=40,diesel=55,othervari=2)
                        elif models =="3" or models =="Benz G-Class":
                          print("Thanks for choosing *Benz G-Clas* please select your variant :")
                          car1.variant(petrol=40,diesel=55,othervari=2)
                        else:
                          print("Sorry we have only this limited Models")
    def variant(self,petrol,diesel,othervari):
            print("Please select your variant:\n1.Petrol\n2.Diesel")
            vari = input()
            if vari == "1" or vari=="petrol":
             print("Thanks for choosing Petrol Variant which can occupy",petrol,"liters ")
            elif vari == "2" or vari=="diesel":
             print("Thanks for choosing dieasel Variant which can occupy",diesel,"liters ")
            else:
                    ("Sorry presently we are maintaing these two variants",othervari," only")  
    def display(self):
          print("\tCar Details \nMake : ",car1.make(),"\nModel : ",car1.model(),"\nVariant : ",car1.vari())                  
                          
                                                
                        
    
    def calculate_on_road_price(self, ex_showroom_price):
        cgst_amount = ex_showroom_price * self.cgst
        sgst_amount = ex_showroom_price * self.sgst
        insurance_amount = self.insurance
        return ex_showroom_price + cgst_amount + sgst_amount + insurance_amount
    def display(self, company, model, variant, ex_showroom_price):
        print("###############################")
        print("Car Company:", company)
        print("Car Model:", model)
        print("Car Variant:", variant)
        print("Ex-showroom Price: ₹", ex_showroom_price)
        on_road_price = self.calculate_on_road_price(ex_showroom_price)
        print("On-road Price: ₹", on_road_price)
                 

 



# # Driver code
# if __name__ == '__main__':
#     # Create object of the class
#     mycar = car()
#     # Call methods of the class
#     mycar.brands()
#     mycar.Model_Mahndra()
#     mycar.display()
    #       if (brand =="1"or brand =="toyota") or brand =="2"or brand=="mahindra" and brand =="3" or brand =="mercedes":
    #       print("the car company",self.toyota)
    #       print("car model name,car variant,ex showroom price:",self.mahindra)
                   
                        
                        
        
          
          
                



car()
car1 = car()
car1.brands()
# print(car1.display)
    
        