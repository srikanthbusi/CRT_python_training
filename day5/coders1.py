# create a class of name placements which has a function info 
# which displays the number of placements this year("we have 650 placements and counting")
# create another class named Department with function Display which will disp;aly the names of 
# departments present in the college.
# create a class pragati with a function welcome which displays the message ("welcome to pragati engineering college")
# and this pragati class should also display the details about departments and placements

class placements:
    def __init__(self,a):
        self.a = a
    def info(self):
        print("We have",self.a,"placements and still counting!!")
class depart():
    def __init__(self,dep1,dep2,dep3,dep4,dep5,dep6,dep7):

        self.dep1 = dep1
        self.dep2 = dep2
        self.dep3 = dep3
        self.dep4 = dep4
        self.dep5 = dep5
        self.dep6 = dep6
        self.dep7 = dep7
    def display(self):
        print("The departments in our college are:",self.dep1,self.dep2,self.dep3,self.dep4,self.dep5,self.dep6,self.dep7)
class pragati(depart,placements):
    def welcome(self):
        print("Welcome to pragati Engineering")

ob=pragati("cse","ece","EEE","AI","DS","CMD","CIVIL")
ob.welcome()
ob.display()
ob1 = pragati(890)


