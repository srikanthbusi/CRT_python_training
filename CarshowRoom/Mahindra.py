def Mahindra():
    print("Thank you for choosing Mahindra Company\nWhich type  of models do you want")
    print("\n1.Thar price (Rs. 11.25 - 17.60 Lakh)\n2.Scorpio price (Rs. 13.59 - 17.35 Lakh)\n3.XUV700 price (Rs. 13.99 - 26.99 Lakh)")
    while(True):
        models = input()
        if models =="1" or models.lower() =="thar":
            print("Thanks for choosing *Thar*:")
            variant()
            break
        elif models =="2"or models.lower() =="scorpio":
            print("Thanks for choosing *Scorpio* :")
            variant()
            break
        elif models =="3" or models.lower() =="XUV700":
            print("Thanks for choosing *XUV700* :")
            variant()
            break
        else:
            print("Sorry we have only this limited Models")
            continue

def variant():
    print("Please select your variant:\n1.Petrol\n2.Diesel")
    while True:
        vari = input()
        if vari == "1" or vari=="petrol":
            print("Thanks for choosing Petrol Variant which can occupy 30 liters ")
            break
        elif vari == "2" or vari=="diesel":
            print("Thanks for choosing dieasel Variant which can occupy 40 liters ")
            break
        else:
            ("Sorry presently we are maintaing these two variants only")
            continue
