string = "Given a string, print the string reversed."
new_string = []
last_string = []

i = -1 
for letter in range(len(string)):
    new_string.append(string[i])
    i -= 1
    # print(new_string)
print(new_string)
