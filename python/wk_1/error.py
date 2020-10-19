
try:
    num = int(input("Please enter a number:  "))
    while num > 0:
        print(num)
        num -= 1
except ValueError:
    print("You did not enter a number. Please enter a number.")

