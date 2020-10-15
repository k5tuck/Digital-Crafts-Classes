num1 = 1
#num2 = 1

while num1 <= 10: 
    num2 = 1
    while num2 < 11:
        product = num1 * num2
        print("%i X %i = %i" %(num1, num2, product))
        num2 += 1
    num1 += 1
    print("---")
    
    # while num2 < 11:
    #     product = num1 * num2
    #     print("%i X %i = %i" %(num1, num2, product))
    #     num2 += 1
print("Multiplication Table Complete!")