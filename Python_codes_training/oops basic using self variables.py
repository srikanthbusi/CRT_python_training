"""create a class f15 with functions lights,fan,ac 
lights:prints color of light which is taken as parameter to func
fan: prints the regulators speed,taken as parameter
ac:room temperature and outside temperature parameter
display:which displays the deference in outside and room temperature and fan"""

class f15:
    #constructor executes automatically when object is created without function call
    def __init__(self):
        print("place where phase 1 training happening")
        a=10
        b=2
        print(a+b)
    #constructor ends
    def lights(satish,c):
        print("color is",c)
    def fan(satish,d):
        print("speed is",d)
        satish.sp=d
    def ac(satish,a,b):
        print("room temp is",a)
        print("out temp :",b)
        satish.a=a
        satish.b=b
    def display(self):
        print("difference is",self.a-self.b)
        print(self.sp)
        
           
        
sat=f15()
sat.lights("blue")
sat.fan(25)
sat.ac(28,24)
sat.display()
    
        