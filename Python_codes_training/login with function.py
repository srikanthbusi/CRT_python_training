#write login function which accepts the user name and password are same and displays a msg login succesful otherwise it keeps asking the user to enter the credential until they are correct

def login():
    while True:
        name=input("name :")
        password=input("password  :")
    
        if name=="sat" and password=="nav":
            print("accepted")
            break
        else:
            print("not accepted")
            
            
        
login()
        