class Faculty:
    def __init__(self,f_name,dpart,f_id):
        self.f_name = f_name
        self.dpart = dpart
        self.f_id = f_id
    def print_info(self):
        print("Faculty information :",self.f_name,self.dpart,self.f_id)
obj = Faculty("Sundaram","Computer_Science",18997)
obj.print_info()

# class child_classname(parent_classname):
# child    #parent
class cse(Faculty):
    pass
obj = cse("hailey","computer",34545)
obj.print_info()
        
# create a class of name placements which has a function info 
# which displays the number of placements this year("we have 650 placements and counting")
# create another class named Department with function Display which will disp;aly the names of 
# departments present in the college.
# create a class pragati with a function welcome which displays the message ("welcome to pragati engineering college")
# and this pragati class should also display the details about departments and placements


# ,"\n"self.dep1,"\n"self.dep2,"\n"self.dep3,"\n"self.dep4,"\n"self.dep5,"\n"self.dep6,"\n"self.dep7

# dep1,dep2,dep3,dep4,dep5,dep6,dep7