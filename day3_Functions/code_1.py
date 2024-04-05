# write an function which takes two parmeters(arguments)
#  A and B type cast the value of second arguement into integer
# then multiply both the arguments and print the last digit of the result
# def check(a,b):
#     b = int(b)
#     print(a*b)
#     print((a*b)%10)

# check(4,6.56)  #postion argument 
# check(b=4,a=6.56)   #keyword args



# # default args
# def city(name="srikanth",city="mandapeta"):
#     print("my name is",name "and the city is",city)

# city()
# city("justin","carlifornia")


def identity(area,pincode,rating,place="none",domicile="karachi",):
    area = pincode*(rating)
    # print("my name is",place "and the city is",domicile)

    print(area)
identity(4556,5,56)
identity()
identity(fname = "srikanth",lname = "beiber")

def identity(**name):  #unkown parameters
    print("My name is::",name["fname"])

identity(fname = "srikanth",lname = "beiber")
