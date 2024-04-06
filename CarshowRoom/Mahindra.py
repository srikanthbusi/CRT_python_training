def Mahindra():
    print("Thank you for choosing Mahindra Company\nWhich type  of models do you want")
    print("\n1.Thar price (Rs. 11.25 - 17.60 Lakh)\n2.Scorpio price (Rs. 13.59 - 17.35 Lakh)\n3.XUV700 price (Rs. 13.99 - 26.99 Lakh)")
    while(True):
        models = input()
        if models =="1" or models.lower() =="thar":
            print("Thanks for choosing *Thar*:")
            print("Please select your variant:\n1.Petrol\n2.Diesel")
            while True:
                vari = input()
                if vari == "1" or vari.lower()=="petrol":
                    print("Thanks for choosing Petrol Variant which can occupy 30 liters ")
                    prs=1323000
                    print("The Ex-Showroom price of Your selected Car --Thar-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(1323000,15,18,14)
                    break
                elif vari == "2" or vari.lower()=="diesel":
                    print("Thanks for choosing Diesel Variant which can occupy 40 liters ")
                    prs=1523590
                    print("The Ex-Showroom price of Your selected Car --Thar-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(1523590,15,18,14)
                    break
                else:
                    print("Sorry presently we are maintaining these two variants only")
                    continue
            break
        elif models =="2"or models.lower() =="scorpio":
            print("Thanks for choosing *Scorpio* :")
            print("Please select your variant:\n1.Petrol\n2.Diesel")
            while True:
                vari = input()
                if vari == "1" or vari.lower()=="petrol":
                    print("Thanks for choosing Petrol Variant which can occupy 40 liters ")
                    prs=1423900
                    print("The Ex-Showroom price of Your selected Car --Scorpio-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(1423900,15,18,14)
                    break
                elif vari == "2" or vari.lower()=="diesel":
                    print("Thanks for choosing Diesel Variant which can occupy 40 liters ")
                    prs=1623599
                    print("The Ex-Showroom price of Your selected Car --Scorpio-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(1623599,15,18,14)
                    break
                else:
                    print("Sorry presently we are maintaining these two variants only")
                    continue
            break
        elif models =="3" or models.lower() =="XUV700":
            print("Thanks for choosing *XUV700* :")
            print("Please select your variant:\n1.Petrol\n2.Diesel")
            while True:
                vari = input()
                if vari == "1" or vari.lower()=="petrol":
                    print("Thanks for choosing Petrol Variant which can occupy 40 liters ")
                    prs=1523900
                    print("The Ex-Showroom price of Your selected Car --Scorpio-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(1523900,15,18,14)
                    break
                elif vari == "2" or vari.lower()=="diesel":
                    print("Thanks for choosing Diesel Variant which can occupy 45 liters ")
                    prs=1723599
                    print("The Ex-Showroom price of Your selected Car --Scorpio-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(1723599,15,18,14)
                    break
                else:
                    print("Sorry presently we are maintaining these two variants only")
                    continue
            break
        else:
            print("Sorry we have only this limited Models")
            continue

def calculate_percentage_increase(prs, cgst,sgst,insurance):
    print("The onroad Price inclusive with Taxes and Insurance is : ",((prs * cgst / 100)+(prs * sgst / 100)+(prs * insurance / 100))+prs)



