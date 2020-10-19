
try:
    num1 = int(input("Please enter your first number:  "))
    num2 = int(input("Please enter your second number:  "))
    num_sum = num1 + num2
    print("This is the sum of your two numbers:  %i" %num_sum)
    product = num1 * num2
    print("This is the product of your two numbers:  %i" %product)
    quotient = num2 / num1
    print("This is the quotient of your two numbers:  %i" %quotient)
except ValueError:
    print("You must enter a number.")
except ZeroDivisionError:
    print("Please enter another number. You cannot divide by zero.")
