# Exercise 1
# new_dict = {
#     "kids": ["Tezrah", "Ivory"],
#     "age": [3, 2],
#     "offspring": True
# }

# print(new_dict)

# new_dict["spouse"] = "Jahnette"
# print(new_dict)

#Exercise 2
person = {
    "first_name": "John",
    "last_name": "Smith",
    "age": 39,
    "hair_color": "Silver"
}
for key in person:
    print(f"{key}:", person[key])
print("Hello %s %s. You are %i years old and have some cool %s hair!" 
%(person["first_name"], person["last_name"], person["age"], person["hair_color"]))

# Exercise 3
# person1 = {
# "name": "Susan", 
# "phone": "202-555-3938", 
# "email": "Susanthegreat@mail.com"}
# person2 = {
# "name": "Mike", 
# "phone": "332-555-3128", 
# "email": "Grasshopper@mail.com"}
# person3 = {
# "name": "Nika", 
# "phone": "923-555-9237", 
# "email": "Garz0348@mail.com"}
# list_of_people = [person1, person2, person3]

# for people in list_of_people:
#     for details in people:
#         print(details, details[key])
        