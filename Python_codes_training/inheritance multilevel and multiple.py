# -*- coding: utf-8 -*-
"""
create a class of name placements which has function info
which displays we have ""623 and still counting"".create another class
name department with display which will display the names of
the departments present in the college.create a class pragati
with a function welcome which displayes the msg 
"welcome to pragati engineering clg".pragati cls should also
display the details about departments and placements
"""
#muitlilevel
class placements():
    def info(self):
        print("623 placements")
        
class department(placements):
    def display(self):
        print("welcome to pragati college")
        print("departments")
        print("cse,ece,eee,civil,mech")
        
class pragati(department):
    def welcome(self):
        print("welcome to pragati engineering college\n")


        
obj=pragati()
obj.info()
obj.welcome()
obj.display()

#mutiple
class sat():
    def satt(self):
        print("it's me")
        
class nav():
    def navv(self):
        print("it's them")
        
class hap(sat,nav):
    def happ(self):
        print("it's we")
        
obj=hap()
obj.satt()
obj.navv()
obj.happ()

        
