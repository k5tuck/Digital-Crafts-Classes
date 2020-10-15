square_dim = int(input("How big is the square?  "))
print("Okay, your square will be %i by %i" %(square_dim, square_dim))

height = 0

while height < square_dim:
    print("*"*square_dim)
    height += 1
