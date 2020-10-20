# Week 2

## Topics Basics Covered
1. Lists
2. Dicitonaries
3. Functions
4. Classes

## Explanation
### Lists
```Python
numbers = [6,7,8,4,878,312,109]
num = 0
for k in numbers:
   num += k
print(num)
```

### Dictionaries
```Python
person = {
    "first_name": "John",
    "last_name": "Smith",
    "age": 39,
    "hair_color": "Silver"
}
for key in person:
    print(f"{key}:", person[key])
```

### Functions
```Python
diff_movies = {
    "Title":"Star Wars - A New Hope",
    "Genre":"Sci-Fi",
    "Year": "1977"
}
def movie_dict (dictionary):
    movies = dictionary
    for key in movies:
        print("%s: "%key, movies[key])

movie_dict(diff_movies)
```

### Classes
```Python

```