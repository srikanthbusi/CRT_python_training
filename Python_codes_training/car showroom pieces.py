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
        if carcomp == "mahendra":
            print("Mahendra")
            print("1) Mah1")
            print("2) Veer1")
            mahmodel = input("")
            self.mahmodel = mahmodel
            self.varient()

        elif carcomp == "toyota":
            print("Toyota")
            print("1) Tow")
            print("2) Yot")
            toymodel = input("")
            self.toymodel = toymodel
            self.varient()

        elif carcomp == "mercedes":
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

        if self.carcomp1 == "mahendra":
            if self.mahmodel == "mah1" or self.mahmodel == "1":
                if varient_option == "1":
                    self.mahvar = "petrol"
                    self.display()
                elif varient_option == "2":
                    self.mahvar = "diesel"
                    self.display()
                else:
                    print("Invalid choice")

            elif self.mahmodel == "veer1" or self.mahmodel == "2":
                if varient_option == "1":
                    self.veervar = "petrol"
                    self.display()
                elif varient_option == "2":
                    self.veervar = "diesel"
                    self.display()
                else:
                    print("Invalid choice")

        elif self.carcomp1 == "toyota":
            if self.toymodel == "tow" or self.toymodel == "1":
                if varient_option == "1":
                    self.towvar = "petrol"
                    self.display()
                elif varient_option == "2":
                    self.towvar = "diesel"
                    self.display()
                else:
                    print("Invalid choice")

            elif self.toymodel == "yot" or self.toymodel == "2":
                if varient_option == "1":
                    self.yotvar = "petrol"
                    self.display()
                elif varient_option == "2":
                    self.yotvar = "diesel"
                    self.display()
                else:
                    print("Invalid choice")

        elif self.carcomp1 == "mercedes":
            if self.mermodel == "alpha" or self.mermodel == "1":
                if varient_option == "1":
                    self.alphavar = "petrol"
                    self.display()
                elif varient_option == "2":
                    self.alphavar = "diesel"
                    self.display()
                else:
                    print("Invalid choice")

            elif self.mermodel == "beta" or self.mermodel == "2":
                if varient_option == "1":
                    self.betavar = "petrol"
                    self.display()
                elif varient_option == "2":
                    self.betavar = "diesel"
                    self.display()
                else:
                    print("Invalid choice")

        else:
            print("Not available")

    def display(self):
        exprice1 = 0
        if self.carcomp1 == "mahendra":
            if self.mahvar == "petrol":
                exprice1 = 540000
            elif self.mahvar == "diesel":
                exprice1 = 520000

        elif self.carcomp1 == "toyota":
            if self.towvar == "petrol":
                exprice1 = 600000
            elif self.towvar == "diesel":
                exprice1 = 620000
            elif self.yotvar == "petrol":
                exprice1 = 640000
            elif self.yotvar == "diesel":
                exprice1 = 650000

        elif self.carcomp1 == "mercedes":
            if self.alphavar == "petrol":
                exprice1 = 800000
            elif self.alphavar == "diesel":
                exprice1 = 820000
            elif self.betavar == "petrol":
                exprice1 = 900000
            elif self.betavar == "diesel":
                exprice1 = 1000000

        sgst1 = exprice1 * 0.15
        cgst1 = exprice1 * 0.15
        insurance1 = exprice1 * 0.20
        onroad1 = exprice1 + sgst1 + cgst1 + insurance1
        print("Ex showroom price :", exprice1)
        print("On road price :", onroad1)


sat = showroom()
