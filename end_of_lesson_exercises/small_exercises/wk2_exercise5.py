# Exercise 5
numbers = [-23, -52, 0, -1.6, 56, 231, 86, 20, 11, 17, 9]

for num in numbers:
    if num > 0:
        print(num)

# Exercise 6
new_numbers = []
for num in numbers:
    if num > 0:
        new_numbers.append(num)
print(sorted(new_numbers))

