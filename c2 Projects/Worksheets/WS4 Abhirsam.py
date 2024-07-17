"""
Worksheet # 4: Python Shortcuts
Student Code
Python Level 3
"""

# Uncomment the provided print statements as you complete each problem
# to verify results.

"""
Part 1
"""

print('\n*** Problem 1: Multiple Assignment *** ')

# 1a. Assign values 5, 10, and 15 to variables a, b, and c respectively in a
#     single line.

print('\n(1-a)')


a, b, c = 15, 10, 5
print('a is', a, '\nb is', b, '\nc is', c, )
# 1b. Now swap the values between variables a and c using the 
#     multiple assignment feature of Python.


print('\n(1-b)')
print("\nBefore swap, a is", a, "and c is", c)
a, c = c, a
print("After swap, a is", a, "and c is", c)

# 1c. You can also use multiple assignment to assign individual variables
#     to elements of a list. Declare four variables w, x, y, z, and assign 
#     them values from the list [2, 4, 6, 8] using a single line of code.

print('\n(1-c)')
w,x,y,z = 2,4,6,8
print("\nThe values of w, x, y, z are, respectively,", w, x, y, z)



print('\n\n*** Problem 2: Augmented Assignment *** ')

# 2a. Given a = 5 and b = 10, use the -= operator to subtract b from a.

print('\n(2-a)')

a = 5
b = 10
print("Before augmented assignment, a is", a,
      "and b is", b)
a -= b
print("After augmented assignment, a is", a,
      "and b is", b)

# 2b. Given list1 = [1, 2, 3] and list2 = [4, 5, 6], use
#     augmented assignment to concatenate list2 to list1.

print('\n(2-b)')

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("\nBefore augmented assignment, list1 is", list1,
      "and list2 is", list2)
list1 += list2
print("After augmented assignment, list1 is", list1,
      "and list2 is", list2)

# 2c. Define a variable c = 20. Use an augmented assignment operator to
#     multiply c by 3.

print('\n(2-c)')

c = 20
print("\nBefore augmented assignment, c is", c)
c *= 3
print("After augmented assignment, c is", c)


print('\n\n*** Problem 3: From-Import Statement *** ')

# 3a. Import the math module and use it to print the square root of 81.

print('\n(3-a)')
import math
print(math.sqrt(81))
# 3b. Now use the from-import statement to import the sqrt function
#     from the math module and calculate the square root of 64.

print('\n(3-b)')
from math import sqrt
print(math.sqrt(64))
# 3c. Use the from-import statement to import the date object from the 
#     datetime module. The date object has a method called today() that
#     returns today's date. Sample call: date.today(). Print today's date.

print('\n(3-c)')
from datetime import date
print(date.today())

print('\n\n*** Problem 4: Line Continuation *** ')

# 4a. Given that a, b, c, d, e, f = 2, 3, 5, 7, 11, 13, write an if statement
#     to check the following condition using implicit line continuation:
#   (a < b and c > d) or (e < f and b + c > d) or (d - e > f and a * c < b * d)
#     Your if statement should output "condition met" if the condition is true.

print('\n(4-a)')

a, b, c, d, e, f = 2, 3, 5, 7, 11, 13
if (a < b and c > d or e < f and b + c > d or d - e > f and a * c < b * d):
    print("Condition met")

# 4b. Write the same conditional using explicit line continuation.

print('\n(4-b)')

a, b, c, d, e, f = 2, 3, 5, 7, 11, 13
if a < b and c > d \
   or e < f and b + c > d \
   or d - e > f and a * c < b * d:
    print("Condition met")

# 4c.  Imagine you're trying to calculate the distance between two points in
#      3D space. The formula for this is
#
#          sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
#
#      Your points are p1 = (2, 4, 6) and p2 = (5, 9, 3). Write the calculation
#      in one line, then split the statement using implicit line continuation 
#      to improve readability.

print('\n(4-c)')

p1 = [2, 4, 6]
p2 = [5, 9, 3]

# Calculate in one line
print(sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2))

# Using line continuation for better readability
distance = (sqrt((p2[0] - p1[0])**2 \
           + (p2[1] - p1[1])**2 \
           + (p2[2] - p1[2])**2))

print ("\nDistance between", p1, "and", p2, "is", distance)


"""
Part 2
"""

print('\n\n*** Problem 5: F-string Formatting *** ')

# 5a.  You are given the variables price = 9.99, qty = 3, item = "burger",
#      and restaurant = "Joe's Diner". Using F-string formatting with 
#      those variables, create and output a string that says:
#
#          3 burgers at Joe's diner costs $29.97.

print('\n(5-a)')

price = 9.99
qty = 3
item = "burger"
restaurant = "Joe's Diner"

print(f"{qty} {item} at {restaurant} costs ${price * qty}") 

# 5b.  Import pi from the math module. hen, print pi to 2 decimal places, 
#      T4 decimal places, and in scientific notation with 2 decimal places
#      using F-string formatting.

print('\n(5-b)')
from math import pi
formatted_string = f"{pi:.2f} {pi:.4f} {pi:.2e}"
print(formatted_string)  # Output: 3.14, 3.1416, 3.14e+00

# 5c.  You're given a variable day = 1. Use F-string formatting to print the
#      day with a leading zero if the day is a single digit.

print('\n(5-c)')
day = 1
formatted_day = f"{day:02}"
print(formatted_day)  # Output: 01

"""
Part 2: Challenge Problems
"""

print('\n\n*** Problem 6: Conditional (Ternary) Expressions *** ')

# 6a. Given a variable temperature = 85, write a one-line conditional (ternary)
#     expression to print "It's hot" if temperature is above 79, otherwise 
#     print "It's cold".

print('\n(6-a)')

temperature = 85
max_value = "It's hot" if  temperature > 79 else "It's cold"
print(max_value) # Output: 10
# 6b. Using a conditional expression, assign the value "positive" to a variable
#     called sign if a given number num is greater than zero, "negative" if
#     it's less than zero, and "zero" if it's equal to zero.

print('\n(6-b)')

num = 10  # you can change this value to test with different numbers
sign = "positive" if  num > 0 else ("negative" if num < 0 else "zero")
print(sign)  # Output: positive


print('\n\n*** Problem 7: List Comprehensions *** ')

# 7a. Using a list comprehension, generate a list of the cubes of all integers
#     from 0 to 10, but only if the cube is less than 500.

print('\n(7-a)')
cubes = [i ** 3 for i in range(0,11) if i < 8]
print(cubes)  # Output: [0, 1, 8, 27, 64, 125, 216, 343]

# 7b. Given a list of names, use a list comprehension to create a new list
#     that contains only those names that start with the letter 'A'.

print('\n(7-b)')
print(a_names)  # Output: ['Adi', 'Andrew']

# 7c. Given a list of numbers, use a list comprehension with a conditional
#     expression to create a new list called parity that contains the string 
#     "even" for every even number and "odd" for every odd number in the
#     original list.

print('\n(7-c)')

numbers = [11, 42, 23, 84, 110]

#print(parity)  # Output: ['odd', 'even', 'odd', 'even', 'even']
print()