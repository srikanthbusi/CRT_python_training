# write an function which takes two parmeters(arguments)
#  A and B type cast the value of second arguement into integer
# then multiply both the arguments and print the last digit of the result
# def check(a,b):
#     b = int(b)
#     print("Multiplication of two numbers after typecasting b: ",a*b)
#     print("The last number is",(a*b)%10)

# check(4,6.56)  #postion argument 
# check(b=4,a=6.56)   #keyword args



# # # default arguments
# def city(name="srikanth",city="mandapeta"):
#     print(f"My name is {name} and the city is {city}")


# city()
# city("justin","carlifornia")


# def identity(area,pincode,rating,place="none",domicile="karachi",):
#     area = pincode*(rating)
    # print("my name is",place "and the city is",domicile)

#     print(area)
# identity(4556,5,56)
# identity()
# identity(fname = "srikanth",lname = "beiber")

# def identity(**name):  #unkown parameters
#     print("My name is::",name["fname"])

# identity(fname = "srikanth",lname = "beiber")


# Arbitrary Arguments/ Variable Length arguments
# def webseries(*series):
#     print("\nThe recommended Web series are:",end=" ")
#     for i in series:
#         print(i,end =",")

# webseries("Dark","Modernfamily","FamilyMan","Save The Tigers")

# Arbitrary keyword Arguments
# def sports(**persons):
#     print("\nName: " +persons["name"])
#     print("Sports category: "+persons["category"])
#     print("Level of Execelence in Career: " +persons["Level"])

# sports(name = "Sachin Tendulkar",category = "Cricket", Level = "Legend")
# sports(name = "MS Dhoni",category = "Cricket", Level = "Legend")
# sports(name = "Mary kom",category = "Boxing", Level = "Legend")
# sports(name = "Bajrang punia",category = "Boxing", Level = "Novice")

