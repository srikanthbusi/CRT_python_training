from DisplayToyota import*
def Toyota()):
    print("Thanks for choosing Toyota Company\nWhich type  of models do you want")
    print("The models for Toyota are:\n1.Fortuner | Starting ₹30.99 Lakh\n2. Innova Crysta | Starting ₹19.99 Lakh\n3.Glanza | Starting ₹6.81 Lakh")
    while True:
        models = input()
        if models =="1" or models.lower()=="fortuner":
            print("Thanks for choosing Fortuner :")
            variant()
            return "Fortuner"
        elif models =="2" or models.lower()=="innova crysta":
            self.crysta = self.crysta
            print("Thanks for choosing Innova Crysta :")
            variant()
            return "Innova Crysta"
        elif models =="3" or models.lower()=="glanza":
            self.glanza = self.glanza
            print("Thanks for choosing Glanza :")
            variant()
            return "Glanza"
        else:
            print("Sorry we have only this limited Models") 
            continue 

def variant(self,):
    print("Please select your variant:\n1.Petrol\n2.Diesel")
    while True:
        vari = input()
        if vari == "1" or vari=="petrol":
            print("Thanks for choosing Petrol Variant which can occupy 30 liters ")
            return "Petrol"
        elif vari == "2" or vari=="diesel":
            print("Thanks for choosing Diesel Variant which can occupy 40 liters ")
            return "Diesel"
        else:
            print("Sorry presently we are maintaining these two variants only")
            continue

def display():
        exprice1 =1
        print(f"The Exshowroom price of {Toyota()} is",exprice1)
        sgst1 = exprice1 * 0.15
        cgst1 = exprice1 * 0.15
        insurance1 = exprice1 * 0.20
        onroad1 = exprice1 + sgst1 + cgst1 + insurance1
        print("Ex showroom price :", exprice1)
        print("On road price :", onroad1)



display()
