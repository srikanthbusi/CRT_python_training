def Toyota():
    print("Thanks for choosing Toyota Company\nWhich type  of models do you want")
    print("The models for Toyota are:\n1.Fortuner | Starting ₹30.99 Lakh\n2. Innova Crysta | Starting ₹19.99 Lakh\n3.Glanza | Starting ₹6.81 Lakh")
    while True:
        models = input()
        if models =="1" or models.lower()=="fortuner":
            print("Thanks for choosing Fortuner :")
            print("Please select your variant:\n1.Petrol\n2.Diesel")
            while True:
                vari = input()
                if vari == "1" or vari.lower()=="petrol":
                    print("Thanks for choosing Petrol Variant which can occupy 30 liters ")
                    prs=3023000
                    print("The Ex-Showroom price of Your selected Car --Fortuner-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(3023000,15,18,14)
                    break
                elif vari == "2" or vari.lower()=="diesel":
                    print("Thanks for choosing Diesel Variant which can occupy 40 liters ")
                    prs=3523590
                    print("The Ex-Showroom price of Your selected Car --Fortuner-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(3523590,15,18,14)
                    break
                else:
                    print("Sorry presently we are maintaining these two variants only")
                    continue
            break
        elif models =="2" or models.lower()=="innova crysta":
            print("Thanks for choosing Innova Crysta :")
            print("Please select your variant:\n1.Petrol\n2.Diesel")
            while True:
                vari = input()
                if vari == "1" or vari.lower()=="petrol":
                    print("Thanks for choosing Petrol Variant which can occupy 40 liters ")
                    prs=3423900
                    print("The Ex-Showroom price of Your selected Car --Innova Crysta-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(3423900,15,18,14)
                    break
                elif vari == "2" or vari.lower()=="diesel":
                    print("Thanks for choosing Diesel Variant which can occupy 40 liters ")
                    prs=3723599
                    print("The Ex-Showroom price of Your selected Car --Innova Crysta-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(3723599,15,18,14)
                    break
                else:
                    print("Sorry presently we are maintaining these two variants only")
                    continue
            break
  
        elif models =="3" or models.lower()=="glanza":
            print("Thanks for choosing Glanza :")
            print("Please select your variant:\n1.Petrol\n2.Diesel")
            while True:
                vari = input()
                if vari == "1" or vari.lower()=="petrol":
                    print("Thanks for choosing Petrol Variant which can occupy 40 liters ")
                    prs=623900
                    print("The Ex-Showroom price of Your selected Car --Glanza-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(623900,15,18,14)
                    break
                elif vari == "2" or vari.lower()=="diesel":
                    print("Thanks for choosing Diesel Variant which can occupy 40 liters ")
                    prs=823599
                    print("The Ex-Showroom price of Your selected Car --Glanza-- is:",prs)
                    print("The onroad price must be conisdered with the following factors\nCentral GST= 15%\nState GST=18%\nInsurance Policy=14%")
                    calculate_percentage_increase(823599,15,18,14)
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

