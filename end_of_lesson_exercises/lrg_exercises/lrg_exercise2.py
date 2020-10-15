num = int(input("What number would you like to factor?:  "))

if num % 2 == 0:
    print("%i is a positive number" %num)
    even_num = 2
    even = [even_num]
    result = num / even_num
    while result != num:
        result = num / even_num
        even.append(result)
        even_num += 2     
else:
    print("%i is a negative number" %num)
    odd_num = 1
    odd = [odd_num]
    odd_result = num / odd_num
    while odd_result != num:
        odd_result = num / odd_num
        odd.append(odd_result)
        odd_num += 2

print("These are the factors for %i: \n" %num)
for i in range(len(even)):
    print(even[i])
