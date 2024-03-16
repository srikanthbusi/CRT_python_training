"""create a class f15 with functions lights,fan,ac 
lights:prints color of light which is taken as parameter to func
fan: prints the regulators speed,taken as parameter
ac:room temperature and outside temperature parameter
display:which displays the deference in outside and room temperature and fan"""

class f15:
    def lights(self,c):
        print("color is",c)
    def fan(self,d):
        print("speed is",d)
    def ac(self,a,b):
        print("room temp is",a)
        print("out temp :",b)
    def display(self,a,b):
        print("difference is")
        if a>b:
            print(a-b)
        else:
            print(b-a)
sat=f15()
sat.lights("blue")
sat.fan(25)
sat.ac(28,24)
sat.display(28,24)
    
        