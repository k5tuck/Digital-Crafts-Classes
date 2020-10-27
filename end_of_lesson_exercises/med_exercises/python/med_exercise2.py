total_bill = float(input("What is the total bill amount?  "))
service = input("Was your service: good, fair, or bad?  ")
split = int(input("How many ways will the check be split, if any?  "))

if service == "good":
    tip_amount = (total_bill * .20)
    print("Tip amount: %.2f" %tip_amount)
    total = total_bill + tip_amount
    print("Total amount: %.2f" %total)
    split_amount = total / split
    print("Amount per person: %.2f" %split_amount)
elif service == "fair":
    tip_amount = (total_bill * .15)
    print("Tip amount: %.2f" %tip_amount)
    total = total_bill + tip_amount
    print("Total amount: %.2f" %total)
    split_amount = total / split
    print("Amount per person: %.2f" %split_amount)
elif service == "bad":
    tip_amount = (total_bill * .10)
    print("Tip amount: %.2f" %tip_amount)
    total = total_bill + tip_amount
    print("Total amount: %.2f" %total)
    split_amount = total / split
    print("Amount per person: %.2f" %split_amount)
else:
    print("I mean you can still give them Something...")