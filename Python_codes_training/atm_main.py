import atm_crt as atm
class login:
    def cardinfo(self):
        self.cardtype=input("Which type of card do you use: \n1.Rupay \n2.Visa \n3.MasterCard: ")
        if self.cardtype!="1" and self.cardtype!="2" and self.cardtype!="3" and self.cardtype!="rupay" and self.cardtype!="visa" and self.cardtype!="mastercard":
            print("Invalid Response")
            self.cardinfo()
        

    def authenticate(self):
        username=input("Enter the Username:")
        password=input("Enter the Password:")
        if username=="sat" and password=="nav":
            print("Select the option you wanna perform:")
            print("1.Check Balance\n2.Cash Withdrawl \n3.Cash Deposit \n4.Mini Statement")
            self.option=input()
        else:
            print("Invalid")
            self.authenticate()

        self.userbal=75000

        if self.option=="1" or self.option=="check balance":
            print("Your account Balance is:",self.userbal)
            
        if self.option=="2" or self.option=="cash withdrawl":
            print("Enter the amount you want to withdraw:")
            self.wda=int(input())
            if self.cardtype=="1" or self.cardtype=="rupay":
                limit=2000
                
            elif self.cardtype=="2" or self.cardtype=="visa":
                limit=5000
                
            else:
                limit=8499
           
            if self.wda > atm.atmbal:
                print("Sorry for the inconvinience \n The ATM is out of funds")
            elif(self.wda>limit):
                print("widthdrawl amount exceeds the transaction limit")
            elif (self.wda)>(self.userbal):
                print("Insufficent funds in the account!!!")
            else:
                print(self.wda,",is Withdrawn")
                rem=(self.userbal)-(self.wda)
                print("Your remaining Balance is:",rem)
                
        if self.option=="3" or self.option=="cash deposit":
            print("Enter the amount you want to Deposit:")
            self.dpa=int(input())
            print("Amount Deposited: ",self.dpa)
            print("Your total Balance is:",self.dpa+self.userbal)

    
        if self.option=="4" or self.option=="mini statement":
            print("The last Three Trasactions are:")
            print("TO: amp funds \t Amount:1000 \t Balance:",self.userbal)
            print("TO: ap electicity bill \t Amount:1200 \t Balance:75000")
            print("TO: kfc \t\t Amount:2000 \t Balance:73000")


        
    



obj2=login()
obj2.cardinfo()
obj2.authenticate()