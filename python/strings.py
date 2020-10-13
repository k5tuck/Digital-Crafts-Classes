greeting = "Hello World! "
today = "This is a really good day!"

todays_greeting = greeting + today
print("\n" + todays_greeting)

haiku = "\nThis is the beginning\nof this bootcamp\nI pray that I continue to\nunderstand everything\n"
print(haiku)

person = "Kevin"
today = "Tuesday"
emotion = "happy"

print(f"Hello {person},")
print(f"I hope that your {today} is going well.")
print(f"I'm personally really {emotion}!\n")

print("Hello %s " %person)
print("I hope that your %s is going well." %today)
print("I'm personally really %s!\n" %emotion)

print(f"Hello " + person + ",")
print(f"I hope that your " + today + " is going well.")
print(f"I'm personally really " + emotion + "!\n")