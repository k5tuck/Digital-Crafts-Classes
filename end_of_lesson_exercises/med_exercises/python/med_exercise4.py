width = int(input("Width?  (__) units  "))
height = int(input("Height? (__) units  "))
h = 2

print("*"*width)
while h != height:
    print("*", " " * (width-4), "*")
    h += 1
print("*"*width)