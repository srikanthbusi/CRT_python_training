class showroom:
    #constructor executes automatically when object is created without function call
    def __init__(self):
        print("welcome to vice car showroom")
        print("select the car company")
        print("1.toyota 2.mahendra 3.mercedes")
        carcomp=input("")
        self.carcomp1=carcomp
        sat.model()
    #constructor ends
    def model(self,carcomp1):
        if self.carcomp=="mahendra":
            print("mahendra")
            print("1)mah1")
            print("2)veer1")
            mahmodel=input("")
            self.mahmodel=mahmodel
            
            sat.varient()
                
        elif self.carcomp=="toyota":
            print("toyota")
            print("1)tow")
            print("2)yot")
            toymodel=input("")
            self.toymodel=toymodel
            
            sat.varient()
                
        elif self.carcomp=="mercedes":
            print("mercedes")
            print("1)alpha")
            print("2)beta")
            mermodel=input("")
            self.mermodel=mermodel
            
            sat.varient()

        else:
            print("not available")
            
                    
            
    def varient(self):
        print("varient")
        print("1)petrol")
        print("2)diesel")
        
        if self.mahmodel=="mah1" or self.mahmodel=="1":
            mahvar=input("")
            self.mahvar=mahvar
            sat.display()
            
        elif self.mahmodel=="veer1" or self.mahmodel=="2":
            veervar=input("")
            self.veervar=veervar
            sat.display()
            
        elif self.toymodel=="tow" or self.toymodel=="1":
            towvar=input("")
            self.towvar=towvar
            sat.display()
            
        elif self.toymodel=="yot" or self.toymodel=="2":
            yotvar=input("")
            self.yotvar=yotvar
            sat.display()
            
        elif self.mermodel=="alpha" or self.alphamodel=="1":
            alphavar=input("")
            self.alphavar=alphavar
            sat.display()
            
        elif self.mermodel=="beta" or self.betamodel=="2":
            betavar=input("")
            self.betavar=betavar
            sat.display()
            
        else:
            print("not available")

        
        
    def display(self):
        if self.mahvar=="petrol":
            exprice1=540000
            sgst1=exprice1*0.15
            cgst1=exprice1*0.15
            insurance1=exprice1*0.20
            onroad1=exprice1+sgst1+cgst1+insurance1
            print("ex showroom price :",exprice1)
            print("on road price :",onroad1)
            
            
        elif self.mahvar=="diesel":
            exprice1=520000
            sgst1=exprice1*0.15
            cgst1=exprice1*0.15
            insurance1=exprice1*0.20
            onroad1=exprice1+sgst1+cgst1+insurance1
            print("ex showroom price :",exprice1)
            print("on road price :",onroad1)
            
        elif self.veervar=="petrol":
            exprice1=500000
            sgst1=exprice1*0.15
            cgst1=exprice1*0.15
            insurance1=exprice1*0.20
            onroad1=exprice1+sgst1+cgst1+insurance1
            print("ex showroom price :",exprice1)
            print("on road price :",onroad1)
            
        elif self.veervar=="diesel":
            exprice1=560000
            sgst1=exprice1*0.15
            cgst1=exprice1*0.15
            insurance1=exprice1*0.20
            onroad1=exprice1+sgst1+cgst1+insurance1
            print("ex showroom price :",exprice1)
            print("on road price :",onroad1)
            
        elif self.towvar=="petrol":
            exprice1=600000
            sgst1=exprice1*0.15
            cgst1=exprice1*0.15
            insurance1=exprice1*0.20
            onroad1=exprice1+sgst1+cgst1+insurance1
            print("ex showroom price :",exprice1)
            print("on road price :",onroad1)
            
        elif self.towvar=="diesel":
            exprice1=620000
            sgst1=exprice1*0.15
            cgst1=exprice1*0.15
            insurance1=exprice1*0.20
            onroad1=exprice1+sgst1+cgst1+insurance1
            print("ex showroom price :",exprice1)
            print("on road price :",onroad1)
            
        elif self.yotvar=="petrol":
            exprice1=640000
            sgst1=exprice1*0.15
            cgst1=exprice1*0.15
            insurance1=exprice1*0.20
            onroad1=exprice1+sgst1+cgst1+insurance1
            print("ex showroom price :",exprice1)
            print("on road price :",onroad1)
            
        elif self.yotvar=="diesel":
            exprice1=650000
            sgst1=exprice1*0.15
            cgst1=exprice1*0.15
            insurance1=exprice1*0.20
            onroad1=exprice1+sgst1+cgst1+insurance1
            print("ex showroom price :",exprice1)
            print("on road price :",onroad1)
            
        elif self.alphavar=="petrol":
            exprice1=800000
            sgst1=exprice1*0.15
            cgst1=exprice1*0.15
            insurance1=exprice1*0.20
            onroad1=exprice1+sgst1+cgst1+insurance1
            print("ex showroom price :",exprice1)
            print("on road price :",onroad1)
            
        elif self.alphavar=="diesel":
            exprice1=820000
            sgst1=exprice1*0.15
            cgst1=exprice1*0.15
            insurance1=exprice1*0.20
            onroad1=exprice1+sgst1+cgst1+insurance1
            print("ex showroom price :",exprice1)
            print("on road price :",onroad1)
            
        elif self.betavar=="petrol":
            exprice1=900000
            sgst1=exprice1*0.15
            cgst1=exprice1*0.15
            insurance1=exprice1*0.20
            onroad1=exprice1+sgst1+cgst1+insurance1
            print("ex showroom price :",exprice1)
            print("on road price :",onroad1)
            
        elif self.betavar=="diesel":
            exprice1=1000000
            sgst1=exprice1*0.15
            cgst1=exprice1*0.15
            insurance1=exprice1*0.20
            onroad1=exprice1+sgst1+cgst1+insurance1
            print("ex showroom price :",exprice1)
            print("on road price :",onroad1)
            
        else:
            print("invalid")
            

sat=showroom()
