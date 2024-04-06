def Honda():
    print("\nThank you for choosing Honda Company\nWhich type  of models do you want")
    print("\n1.Amaze price (Rs. 11.25 - 17.60 Lakh)\n2.City price (Rs. 13.59 - 17.35 Lakh)\n3.Elevate price (Rs. 13.99 - 26.99 Lakh)")
    while True:
        models = input()
        if models =="1" or models.lower()=="amaze":
            print("Thanks for choosing *Amaze* please select your variant :")
            print("Please select your variant:\n1.Petrol\n2.Diesel")
            while True:
                vari = input()
                if vari == "1" or vari.lower()=="petrol":
                    print("Thanks for choosing Petrol Variant which can occupy 40 liters ")
                    prs=1023900
                    print("The Ex-Showroom price of Your selected Car --Amaza-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(1023900,15,18,14)
                    break
                elif vari == "2" or vari.lower()=="diesel":
                    print("Thanks for choosing Diesel Variant which can occupy 40 liters ")
                    prs=1123599
                    print("The Ex-Showroom price of Your selected Car --Amaze-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(1123599,15,18,14)
                    break
                else:
                    print("Sorry presently we are maintaining these two variants only")
                    continue
            break
        elif models =="2" or models.lower()=="city ":
            print("Thanks for choosing *City * please select your variant :")
            print("Please select your variant:\n1.Petrol\n2.Diesel")
            while True:
                vari = input()
                if vari == "1" or vari.lower()=="petrol":
                    print("Thanks for choosing Petrol Variant which can occupy 40 liters ")
                    prs=1223900
                    print("The Ex-Showroom price of Your selected Car --City-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(1223900,15,18,14)
                    break
                elif vari == "2" or vari.lower()=="diesel":
                    print("Thanks for choosing Diesel Variant which can occupy 40 liters ")
                    prs=1423599
                    print("The Ex-Showroom price of Your selected Car --City-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(1423599,15,18,14)
                    break
                else:
                    print("Sorry presently we are maintaining these two variants only")
                    continue
            break
        elif models =="3" or models.lower()=="elevate":
            print("Thanks for choosing *Elevate* please select your variant :")
            print("Please select your variant:\n1.Petrol\n2.Diesel")
            while True:
                vari = input()
                if vari == "1" or vari.lower()=="petrol":
                    print("Thanks for choosing Petrol Variant which can occupy 40 liters ")
                    prs=823900
                    print("The Ex-Showroom price of Your selected Car --Elevate-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(823900,15,18,14)
                    break
                elif vari == "2" or vari.lower()=="diesel":
                    print("Thanks for choosing Diesel Variant which can occupy 40 liters ")
                    prs=1023599
                    print("The Ex-Showroom price of Your selected Car --Elevate-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(1023599,15,18,14)
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
