
req_tri = int(input("What triangle do you want to print out?:  "))

i = 1
while i <= req_tri: #Comment out to loop through just one triangle

    dots = i * ((i + 1) / 2) #change "i" back to req_tri to loop through one triangle
    print("Dots in triangle:  %i" %dots)
    t = 1
    d = 1
    print("*" * d)
    while t < i:  #change "i" back to req_tri to loop through one triangle
        t += 1
        d += 1
        print("*" * d)
    i += 1  #Comment out to loop through just one triangle
