class showroom:
    # Constructor executes automatically when object is created without function call
    def __init__(self):
        print("Welcome to Vice Car Showroom")
        print("Select the car company")
        print("1. Toyota  2. Mahendra  3. Mercedes")
        carcomp = input("")
        self.carcomp1 = carcomp
        self.model(self.carcomp1)

    # Constructor ends
    def model(self, carcomp):
        if self.carcomp1 == "mahendra" or self.carcomp1=="1":
            print("Mahendra")
            print("1) Mah1")
            print("2) Veer1")
            mahmodel = input("")
            self.mahmodel = mahmodel
            self.varient()

        elif self.carcomp1 == "toyota" or self.carcomp1=="2":
            print("Toyota")
            print("1) Tow")
            print("2) Yot")
            toymodel = input("")
            self.toymodel = toymodel
            self.varient()

        elif self.carcomp1 == "mercedes" or self.carcomp1=="3":
            print("Mercedes")
            print("1) Alpha")
            print("2) Beta")
            mermodel = input("")
            self.mermodel = mermodel
            self.varient()

        else:
            print("Not available")

    def varient(self):
        print("Variant")
        print("1) Petrol")
        print("2) Diesel")

        varient_option = input("Enter your choice: ")

        
        if self.mahmodel == "mah1" or self.mahmodel == "1":
            if varient_option == "1" or varient_option == "petrol":
                self.mahvar = "petrol"
                self.display()
            elif varient_option == "2" or varient_option == "diesel":
                self.mahvar = "diesel"
                self.display()
            else:
                print("Invalid choice")

            

    def display(self):
        exprice1 = 0
        if self.carcomp1 == "mahendra":
            if self.mahvar == "petrol" or self.mahvar == "1":
                exprice1 = 540000
            elif self.mahvar == "diesel" or self.mahvar == "2":
                exprice1 = 520000
            elif self.veervar == "petrol" or self.veervar == "1":
                exprice1 = 520000
            elif self.veervar == "diesel" or self.veervar == "2":
                exprice1 = 520000
            else:
                print("invalid")

        elif self.carcomp1 == "toyota":
            if self.towvar == "petrol" or self.towvar == "1":
                exprice1 = 600000
            elif self.towvar == "diesel" or self.towvar == "2":
                exprice1 = 620000
            elif self.yotvar == "petrol" or self.yotvar == "1":
                exprice1 = 640000
            elif self.yotvar == "diesel" or self.yotvar == "2":
                exprice1 = 650000
            else:
                print("invalid")

        elif self.carcomp1 == "mercedes":
            if self.alphavar == "petrol" or self.alphavar == "1":
                exprice1 = 800000
            elif self.alphavar == "diesel" or self.alphavar == "2":
                exprice1 = 820000
            elif self.betavar == "petrol" or self.betavar == "1":
                exprice1 = 900000
            elif self.betavar == "diesel" or self.betaavar == "2":
                exprice1 = 1000000
            else:
                print("invalid")

        sgst1 = exprice1 * 0.15
        cgst1 = exprice1 * 0.15
        insurance1 = exprice1 * 0.20
        onroad1 = exprice1 + sgst1 + cgst1 + insurance1
        print("Ex showroom price :", exprice1)
        print("On road price :", onroad1)


sat = showroom()
