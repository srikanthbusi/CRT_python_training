#hierarachy
class placements():
    def info(self):
        print("623 placements")
        
class department(placements):
    def display(self):
        print("welcome to pragati college")
        print("departments")
        print("cse,ece,eee,civil,mech")
        
class pragati(placements):
    def welcome(self):
        print("welcome to pragati engineering college\n")
obj=pragati()
obj1=department()
obj.info()
obj.welcome()
obj1.display()