# Week 1

## Topics Basics Covered
### Developer Fundamentals
1. Command Line
2. File System
3. Git Basics
5. Markdown

### Python
1. print()
2. variables
3. types
5. comparisons
6. input

## Explanation
### Print() Function
This week so far we have gone over the basics of beginning basics of python. To recap a little:
* The print function can be very helpful in debugging and will display content in the output terminal

```Python
print("This is a great way to debug")
#This will print out "This is a great way to debug"
```
### Variables
Variable are names that you can assign different types too. Example:
```Python
first_var = "Random Name" # Here the String "Random Name" is assigned to first_var
first_int = 38 # Here the integer 38 is assigned to the variable first_int
last_float = 69.123 # A float has been assigned to the variable last_float
```

### Types
* There a different *types* in Python
    * Strings
    * Integers
    * Floats
    * Booleans

#### Strings
String can be de defined by the following:
```Python
string1 = 'This is a string'
string2 = "This is also a string"
string3 = 'Ya\'ll this will also be a string too'
string4 = '''
This will become a block of strings. 
This can become useful for long strings of text 
that are too long for a single line.
'''
```
#### Numbers - Integers / Floats

Integers and Floats can differ.

Integers can be considered whole numbers, either positive or negative.
Example: 
```
a = 1
b = 1003
c = -390
```

Floats can be considered decimals. They are similar to doubles and floats in C++.
Example:
```
a = 3.9
b = -1.9404
c = 8274.928794
```

#### Booleans
Booleans are either True or False values.

```Python
0 = False
1 = True
"a" == "a" # Evaluates to True
40 >= "a" # Evaluates to False
```

### Comparisons

These are methods that will allow us to compare different values against each other.

```Python
1 == 1 # The == operator compares whether these two numbers equal each other or not
1 >= 2 # The >= compares whether 1 is greater than or equal to 2
1 <= 2 # The <= compares whether 1 is less than or equal to 2
1 > 2 # This will compare whether 1 is greater than 2 or not
1 < 2 # This will compare whether 1 is less than 2 or not
```

### If, Elif, and Else

If and Else statements can be used to create "branches" that will direct the flow of your code.
```Python
if 1 >= 2:
    print("This shouldn't be printing.")
elif 1 == 2:
    print("This also should not work.")
else:
    print("This was the only option left.")
```

### Input

Input allows you to receive data from a user
```Python
name = input("Please enter your name: ")
print("Hello %s!" %name)

```

### Nested Blocks

It's possible for blocks of code to be nested inside other code. For example:
```Python
name = "Wilema"
if len(name) > 5:
    print("Hello %s !" %name)
    if name == "Wilema"
        print("Your name is the absolute greatest!")
    else:
        print("Your name is cool too!")
else:
    print("Your name is too short.")
```

### Loops

Loops can be used to iterate through blocks of code multiple times without having to copy and paste previous code.

```Python

```

### Error Handling

