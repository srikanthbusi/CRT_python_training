# create a class f15 with functions ligths("colour of the light which is taken as parameter to the functin ")
# ,fan("the speed the regulator speed which is taken as the parameter of the function") 
# and AC("current room temperature and the outside temparature ")
# write the 4 function whose name is display
# which displays the difference in outside temperature and 
# room temp of ac and displays the fan speed
class  F15:
    def __init__(self):
        print("hello guru")

    def lights(self, colour):
        print("The colour of the light is set to :",colour)
    
    def fan(self,speed):
        self.regulatorspeed=speed
        print("The speed of the fan is: ",speed)
    
    def ac(self,room_temp,outside_temp):
        self.rt = room_temp
        self.ot = outside_temp
        print("The room temperature is :",room_temp)
        print("The outside temperature is:",outside_temp,"\n")
    def display(self):
        print("The difference between room temperature and outside temperature is:",self.rt-self.ot)
        print("The room temperature of ac",self.rt)
        
        print("the fan speed:",self.regulatorspeed)

busi= F15()
busi.lights("White")
print("\n")
busi.fan("Medium")
print ("\n")
busi.ac(16,32)

busi.display()
  



#   class start time and end time and display them
# class F15:
#     def __init__(self):
#         print("hello guru")

#     def lights(self, colour):
#         print("The colour of the light is set to :", colour)
    
#     def fan(self, speed):
#         print("The speed of the fan is: ", speed)
    
#     def ac(self, room_temp, outside_temp):
#         self.rt = room_temp
#         self.ot = outside_temp
#         print("The room temperature is :", room_temp)
#         print("The outside temperature is:", outside_temp, "\n")
    
#     def display(self):
#         # Before trying to print attributes, check if they have been set
#         if hasattr(self, 'rt') and hasattr(self, 'ot'):
#             print("The difference between room temperature and outside temperature is:", self.rt - self.ot)
#             print("The room temperature of ac", self.rt)
#         else:
#             print("AC settings not found.")

# # Create a single instance of F15
# busi = F15()

# # Use the same instance for all method calls
# busi.lights("White")
# print("\n")

# # Continue using the same instance
# busi.fan("Medium")
# print("\n")

# # Keep using the same instance
# busi.ac(16, 29)
# print("\n")

# # Now this will work, as it's still the same instance where `ac` was called
# busi.display()
