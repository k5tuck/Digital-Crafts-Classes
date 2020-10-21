# Exercise 1
# def name ():
#     name = input("What is your name?  ")
#     i = 0
#     while i <3:
#         print("Hello my name: %s" %name)
#         i+=1
# name()

# Exercise 2
# num1 = int(input("First Number:  "))
# num2 = int(input("Second number:  "))
# def mulitply (a, b):
#     valid = True
#     while valid:
#         try:
#             result = int(a) * int(b)
#             valid = False
#         except TypeError:
#             print("Oops! Looks like you forgot to put in a number!")
#     print(result)

# mulitply(num1, num2)
# mulitply(num1, num2)
# mulitply(num1, num2)

# Exercise 2
# diff_movies = {
#     "Title":"Star Wars - A New Hope",
#     "Genre":"Sci-Fi",
#     "Year": "1977"
# }
# def movie (title, genre, year):
#     movies = [title, genre, year]
#     for movie in movies:
#         print(movie)

# movie(diff_movies["Title"], diff_movies["Genre"], diff_movies["Year"])

# Exercise 3
# diff_movies = {
#     "Title":"Star Wars - A New Hope",
#     "Genre":"Sci-Fi",
#     "Year": "1977"
#     # ["Title":"Ready Player",
#     # "Genre":"Sci-Fi",
#     # "Year": "2019"]
# }
# def movie_dict (dictionary):
#     movies = dictionary
#     idx = 1
#     for key in movies:
#         print("%i %s: %s"%(idx, key, movies[key]))
#         idx += 1

# movie_dict(diff_movies)

# Exercise 4
# def random (a, b):
#     #print(a + b) #Checking value of result
#     return a + b

# random("Kevin ", "Tucker")

# Exercise 5
# def total_count(a):
#     new = []
#     for i in a:
#         for j in i:
#             new.append(j)
#     list_dict = {
#         "list_length": len(a),
#         "total_chars": len(new)
#     }
#     for key in list_dict:
#         return("%s: %i" %(key, list_dict[key]))

# total1 = total_count(["I", 'hope', 'this', 'this', 'is', 'right...'])
# print("-------------")
# print(total1)
# total2 = total_count(['I', 'Am', 'Awesome'])
# print("-------------")
# print(total2)
# total3 = total_count(["It\'s", 'a', 'beautiful', 'morning!'])
# print("-------------")
# print(total3)


# Exercise 6
# name = "Kevin"
# def holla(message):
#     print("%s, %s" %(name, message))

# holla("my name is.")
# holla("wishes he could be like Yoda.")
# holla("just doesn't want to be short and green.")

# Exercise 7
# name = "Kevin"
# def name_alter(a):
#     name = a
#     return name

# name1 = name_alter("Jeff")
# print(name1)
# name2 = name_alter("Tiota")
# print(name2)
# name3 = name_alter("Natalie")
# print(name3)