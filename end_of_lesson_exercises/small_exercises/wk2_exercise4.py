numbers = [2,56, 231, 5346, 86, 20, 11, 17, 9]
for num in numbers:
    if num % 2 == 0:
        print(num)

#Alternative - Returns list
print([num for num in numbers if num % 2 == 0])