"""
Worksheet # 9: Object-Oriented Programming
Student Code
Python Level 3

Name: 
Class Section (if more than one G8 class): 
"""

print('\n *** Problem 1 *** ')

"""
In the comment below, define Object-Oriented Programming (OOP) 
using your own words.
"""

print("Answer in the comment.")

""" 
# Object-oriented programming (OOP) is a programming model that organizes code objects, which are members of classes.

"""


print('\n *** Problem 2 *** ')

# Given the functional programming approach below, re-write it using 
# the OOP approach. Run your own test cases for the OOP version.

def get_description(name, age):
    return f"{name} is {age} years old"

# Test cases
student1_name = "Alice"
student1_age = 15

student2_name = "Bob"
student2_age = 16

print(get_description(student1_name, student1_age))
print(get_description(student2_name, student2_age))

# Write the OOP version and its test cases below:
class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print(f"{self.name} is ", f"{self.age} years old.")
    
student1 = Students("Alice", 15)
student2 = Students("Bob", 16)
print("\n")
student1.description()
student2.description()


print('\n *** Problem 3 *** ')

"""
Explain in your own words the benefits of using the OOP approach. Use your code
from Problem 2 as an example. Identify a scenario where it would be more
beneficial to use the OOP approach.
"""

print("Answer in the comment.")

"""
# Problems can be solved easily through OOPS because a program can be broken down into bit-sized codes or problems that can be easily solved.
With the development of technology, the maintenance cost of the programs is reduced, and there is increased productivity.
In Problem 2, the code is broken down into classes and objects which makes it much more efficient to print out the age and name of the two kids.
A specific scenario  is a car where since it has a model name, a colour, a year in which it was manufactured, an engine size and so on.
We would therefore create a Car object with the name, colour, engine size and year as attributes.

"""


print('\n *** Problem 4 *** ')

# Identify and fix the errors in the following code (uncomment to test):

class Elephant:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(f"The elephant's name is {self.name} and",
              f"it is {self.age} years old")

# Provided test case:
elephant1 = Elephant("Dumbo", 5)
elephant1.description()



print('\n *** Problem 5 *** ')

# Create a class called Circle. The class should have an attribute radius
# initialized during object creation and a method area() that calculates the
# area of the circle. Run your own test case to verify that it works.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        area = math.pi*(self.radius*2)
        print(f"The area of the circle with radius {self.radius} is {area}.")
circle1 = Circle(5)
circle1.area()
        

print('\n *** Problem 6: Challenge Problem *** ')

# Create a class called Library. This class should have an attribute books that 
# is a list. It should have methods to add a book, remove a book, and list the 
# books. Run your own test cases.
