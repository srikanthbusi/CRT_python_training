#write a program to check the on road price of a bike under the conditions 
# if the price is greater than 72000 then income taxes will  be 10% of original price and insurance will be 15% of the actual price
# if the price is greater than 150000 and less than 200000 the tax woiuld be 25% and the insurance will be 20%
# price is above 200000 then tax will be 35% and insurance will be 28%
# otherwise minimum bike price starts from 75000
# on road price of the bike whose formula is actual price +tax+insurance       # 
actual_price= int(input("enter the actual price"))
income_tax = 0
insurance  = 0
if actual_price>72000 and actual_price<150000:
    income_tax = (10/100)*actual_price
    insurance = (15/100)*actual_price
elif actual_price>=150000 and actual_price<200000:
    income_tax = (25/100)*actual_price
    insurance = (20/100)*actual_price
elif actual_price>=200000:
    income_tax = (35/100)*actual_price
    insurance = (28/100)*actual_price
else:
    print("bike price starts from 75000")
    exit()

Onroad_price = actual_price +income_tax + insurance
print("the onroad price", Onroad_price)


# Write a program to check the onroad price of a bike under the conditions if the price is grater than
# 72,000 then income tax is 10% of orginal price insurance will be 15% of the orginal price
# greather than 1,50,000 and less than 2 lakhs then income tax is 25% of orginal price 
#insurance will be 20% of the orginal price
# above 2 lakhs tax = 35% and insurance will be 28%
#Otherwise min price 720000

# Print ONRoad Price

# Orginal_Price = int(input("Enter the Orginal Price of the Bike : ₹"))
# def OnRoadPrice(o,t,i):
  
#     tax = t/100 * o
#     print("Tax Amount: ₹",tax)
 
#     insurance = i/100 * o
#     print("Insurance Amount : ₹",insurance)
#     onroadprice = o + tax +insurance

#     print("The OnRoad Price : ₹",onroadprice )


# insurance =0
# if(Orginal_Price > 72000):
#    OnRoadPrice(Orginal_Price,10,15)
# elif(Orginal_Price > 150000 and Orginal_Price<200000):
#     OnRoadPrice(Orginal_Price,25,20)
# elif(Orginal_Price>200000):
#     OnRoadPrice(Orginal_Price,35,28)
# else:
#     print("Starting Price will be Min of ₹72,000")