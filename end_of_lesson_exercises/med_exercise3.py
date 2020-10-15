print("You have 0 coins.")
amount = int(input("How many coins would you like?  "))

print("You have %i coins." %amount)
valid = True

while valid:
    answer = input("Do you want another coin? (yes or no) ")
    if answer == "yes" or answer == "y":
        amount += 1
        print("You have %i coins." %amount)
    elif answer == "no" or answer == "n":
        print("Goodbye")
        valid = False