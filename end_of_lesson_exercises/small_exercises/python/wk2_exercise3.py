numbers = [6, 7, 8, 64, 2, 3, 312, 109, 878]
smallest = len(numbers)

for num in numbers:
    if smallest < num:
        pass
    else:
        smallest = num
print(smallest)

#Alternative using sort method
numbers.sort()
print(numbers[0])

#Alternative
print(min(numbers))