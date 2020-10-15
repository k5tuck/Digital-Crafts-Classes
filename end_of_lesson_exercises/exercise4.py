day = int(input("Day (0-6)?:  "))
valid = True

while valid:
    if day == 0:
        print("Sunday")
        valid = False
    elif day == 1:
        print("Monday")
        valid = False
    elif day == 2:
        print("Tuesday")
        valid = False
    elif day == 3:
        print("Wednesday")
        valid = False
    elif day == 4:
        print("Thursday")
        valid = False
    elif day == 5:
        print("Friday")
        valid = False
    elif day == 6:
        print("Saturday")
        valid = False
    else:
        print("You have entered a number outside of the range. Please try again.")
        break
        # valid = False