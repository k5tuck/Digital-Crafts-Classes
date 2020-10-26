username = input("Please input the username that you would like to use:  ")
username_pass = input("Please enter the password you would like to use:  ")

attempts = 2
max_attempts = 0
valid = True

while valid:
    if attempts > max_attempts:
        if username == "Kevin" and username_pass == "Lola":
            print("Welcome Back!")
            valid = False
        elif username != "Kevin" and username_pass != "Lola":
            print("Incorrect username or password. Please try again.")
            username = input("Please input the username that you would like to use:  ")
            username_pass = input("Please enter the password you would like to use:  ")
            attempts -= 1
    else:
        print("You have exhausted your login attempts.")
        valid = False
    
    

