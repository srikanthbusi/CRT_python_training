# write an function to see when the user name and password are same as mentioned in the above
def login():
    while True:
        username = input("Enter the username: ")
        password = input("Enter the password: ")

        if username == password:
            print("The credentials are the same.")
            break  # Exit the loop if credentials match
        else:
            print("The credentials are not the same.")
            # Optionally, you can add a break here to exit after the first attempt
            # Or continue looping for more attempts

login()  # Call the function to execute the login process










