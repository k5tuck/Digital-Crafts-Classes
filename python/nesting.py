pet_name = input("what is the pet's name?:  ")
pet_length = len(pet_name)

if pet_name == "Shadow":
    print("El Gat Diablo!")
elif pet_name == "Daisy":
    print("Good Dog!")
elif pet_length < 3:
    print("This name is too short")
elif pet_length > 3:
    print("AWWW sweet %s" %pet_name)
else:
    print("%s is an awesome name!" %pet_name)