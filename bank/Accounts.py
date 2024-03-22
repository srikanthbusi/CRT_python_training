class HDFC:
    def __init__(self,Name,Balance):
        self.account = Name
        self.balance = Balance
        print("Thankyou for choosing HDFC Bank")
        print("*********************************")
        print(f"\n The account named as : {self.account} created : \n The present balance is :{self.balance:.2f}")
        print("*********************************")


    def getBal(self):
        print(f"The Account Name is {self.account} and the present balance are :{self.balance:.2f}")
        
    def deposit(self):
        dep = int(input("Please enter your requied amount to deposit:"))
        self.balance = self.balance + dep
        print(f"**Hence Rupees{dep} are deposited to your {self.account}**")