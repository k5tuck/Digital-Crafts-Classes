
numbers = [6,7,8,4,312,109,878]
biggest = 0
for num in numbers:
    if biggest < num:
        biggest = num
    else:
        pass
print(biggest)

#Alternative using sort method
numbers.sort()
print(numbers[-1])

#Alternative
print(max(numbers))