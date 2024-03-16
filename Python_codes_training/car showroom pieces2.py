if self.carcomp1 == "mahendra":
    
    elif self.mahmodel == "veer1" or self.mahmodel == "2":
        if varient_option == "1" or varient_option == "petrol":
            self.veervar = "petrol"
            self.display()
        elif varient_option == "2" or varient_option == "diesel":
            self.veervar = "diesel"
            self.display()
        else:
            print("Invalid choice")

elif self.carcomp1 == "toyota":
    if self.toymodel == "tow" or self.toymodel == "1":
        if varient_option == "1" or varient_option == "petrol":
            self.towvar = "petrol"
            self.display()
        elif varient_option == "2" or varient_option == "diesel":
            self.towvar = "diesel"
            self.display()
        else:
            print("Invalid choice")

    elif self.toymodel == "yot" or self.toymodel == "2":
        if varient_option == "1" or varient_option == "petrol":
            self.yotvar = "petrol"
            self.display()
        elif varient_option == "2" or varient_option == "diesel":
            self.yotvar = "diesel"
            self.display()
        else:
            print("Invalid choice")

elif self.carcomp1 == "mercedes":
    if self.mermodel == "alpha" or self.mermodel == "1":
        if varient_option == "1" or varient_option == "petrol":
            self.alphavar = "petrol"
            self.display()
        elif varient_option == "2" or varient_option == "diesel":
            self.alphavar = "diesel"
            self.display()
        else:
            print("Invalid choice")

    elif self.mermodel == "beta" or self.mermodel == "2":
        if varient_option == "1" or varient_option == "petrol":
            self.betavar = "petrol"
            self.display()
        elif varient_option == "2" or varient_option == "diesel":
            self.betavar = "diesel"
            self.display()
        else:
            print("Invalid choice")

else:
    print("Not available")