start_num = int(input("What number do you want to start on?  "))
end_num = int(input("What number would you like to end on?  "))

print("Starting number: %i" %start_num)
print("Ending number: %i" %end_num)

while start_num <= end_num:
    print(start_num)
    start_num += 1