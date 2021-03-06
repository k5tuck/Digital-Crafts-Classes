# 1. Fizz Buzz
# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the 
# number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and 
# five print "FizzBuzz".

# i = 1
# while i <= 100:
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#     i += 1

# 2. Sum of All Multiples of 3 or 5 below 1000
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# i = 1
# result = 0
# while i <= 1000:
#     if i % 3 == 0 or i % 5 == 0:
#         result += i
#     i += 1    
# print(result)

# 3. Fibonacci Sequence
# Each new term in the Fibonacci sequence is generated by adding the 
# previous two terms. By starting with 1 and 2, the first 10 terms 
# will be:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do
#  not exceed four million, find the sum of the even-valued terms.

fib1 = 0
fib2 = 1
total = 0

