numbers = [6, 7, 8, 64, 2, 3, 312, 109, 878]
smallest = len(numbers)
for num in numbers:
    if smallest < num:
        pass
    else:
        smallest = num
print(smallest)