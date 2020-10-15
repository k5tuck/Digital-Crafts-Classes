total_bill = float(input("What is the total bill amount?  "))
service = input("Was your service: good, fair, or bad?  ")

if service == "good":
    tip_amount = (total_bill * .20)
    print("Tip amount: %.2f" %tip_amount)
    total = total_bill + tip_amount
    print("Total amount: %.2f" %total)
elif service == "fair":
    tip_amount = (total_bill * .15)
    print("Tip amount: %.2f" %tip_amount)
    total = total_bill + tip_amount
    print("Total amount: %.2f" %total)
elif service == "bad":
    tip_amount = (total_bill * .10)
    print("Tip amount: %.2f" %tip_amount)
    total = total_bill + tip_amount
    print("Total amount: %.2f" %total)
else:
    print("I mean you can still give them Something...")