from login_and_reg import *
print('#**WELCOME TO SRK PRODUCTS**#')
p=eccom()

#REGITRATION CHECK
while(True):
    o=int(input('Select the option given below\n1.Signin\n2.Login\n3.Exit\n'))
    if o==1:
        username=input('Enter the user name :')
        password=input('Please set your password :')
        phoneno=int(input('Enter your phone number :'))
        pincode=int(input('Enter the  pincode :'))
        city=input('Enter your City :')
        p.registration(self,username,password,phoneno,pincode,city)
        print('Registration Successfully completed')
        break

    elif o==2:
        username=input('Enter the user name :')
        password=input('Please set your password :')
        a=p.login(username,password)
        if a==1:
            break
        else:
            pass

    elif o==3:
        quit()

    else:
        print('Invalid Option!')
