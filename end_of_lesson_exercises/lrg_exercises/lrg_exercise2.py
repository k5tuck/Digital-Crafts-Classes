
num = int(input("What number would you like to factor?:  "))

if num % 2 == 0:
    print("%i is a positive number" %num)
    even_list = []
    p = 1
    while p <= num:
        if num % p == 0:
            q = num / p
            even_list.append(p)
            even_list.append(int(q))
            p += 1
        else:
            p += 1
    print("These are the factors for %i:" %num)
    dup_list = set(even_list)
    even_sorted = sorted(dup_list)
    for i in range(len(even_sorted)):
        print(even_sorted[i])
else:
    print("%i is a negative number" %num)
    odd_list = []
    p = 1
    while p <= num:
        if num % p == 0:
            q = num / p
            odd_list.append(p)
            odd_list.append(int(q))
            p += 1
        else:
            p += 1
    print("These are the factors for %i:" %num)
    odd_dup_list = set(odd_list)
    odd_sorted = sorted(odd_dup_list)
    for i in range(len(odd_sorted)):
        print(odd_sorted[i])