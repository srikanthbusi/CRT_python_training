def Honda():
    print("\nThank you for choosing Honda Company\nWhich type  of models do you want")
    print("\n1.Amaze price (Rs. 11.25 - 17.60 Lakh)\n2.City price (Rs. 13.59 - 17.35 Lakh)\n3.Elevate price (Rs. 13.99 - 26.99 Lakh)")
    while True:
        models = input()
        if models =="1" or models.lower()=="amaze":
            print("Thanks for choosing *Amaze* please select your variant :")
            variant()
            break
        elif models =="2" or models.lower()=="city ":
            print("Thanks for choosing *City * please select your variant :")
            variant()
            break
        elif models =="3" or models.lower()=="elevate":
            print("Thanks for choosing *Elevate* please select your variant :")
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
# def DisplayHonda():