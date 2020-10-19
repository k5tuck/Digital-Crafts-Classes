# Exercise 1
# names = ["Jahnette", "Kevin", "Ivory"]
# names.append("Tezrah")
# names = names + ["Annalise"]
# print(names)

# Exercise 2
# names[2] = "Foo"
# names[4] = "Bar"
# print(names)

# # Exercise 3
# names = ['Jahnette', 'Kevin', 'Ivory', 'Tezrah', 'Annalise']
# i = 0
# for name in range(len(names)):
#     print(names[0])
#     del names[0]
# print(names)

# # Exercise 4
# first_food_list = ['Corn','Potatoes','Tomatoes']
# second_food_list = ['milk','eggs','cheese','yogurt']
# third_food_list = ['frozen pizza','popsicle']
# shopping_lists = [first_food_list, second_food_list, third_food_list]

# for food in shopping_lists:
#     print(food)

# Exercise 5
shopping_names = ["Veggies", "Cold Items", "Junk Food"]
shopping_lists = [
    ['Corn','Potatoes','Tomatoes'],
    ['milk','eggs','cheese','yogurt'],
    ['frozen pizza','popsicle']]

i = 0
for name in shopping_names:
    j = 0
    print("%i. %s" %(i+1, name))
    for food in shopping_lists[i]:
        print("   %i. %s" %(j+1, food))
        j += 1
    i += 1