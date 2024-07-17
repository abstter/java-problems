"""
Quiz # 3: Object-Oriented Programming
Student Code
Python Level 3

Name: Abhiram A
Class Section (if more than one G8 class):  D14
"""


print('\n *** Problem 1 *** ')  # 15 points

# Define a class Rectangle with attributes length and width. Implement a method
# area() that returns the area of the rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return (self.length*self.width)
        

# Test case for Rectangle class (uncomment to test)

rect = Rectangle(10, 5)
print(f"Area of rectangle with length 10 and width 5: {rect.area()}")

# Expected output: 50



print('\n *** Problem 2 *** ')  # 10 points

# The following code is supposed to create a Circle class and calculate its
# area. Uncomment it, and then identify and fix the issues.

class Circle:
    
    def __init__(self, radius):        
        self.radius = radius  # Assign the radius instance attribute to the
                         # parameter of the same name

    def area(self,pi=3.14):
        return pi * self.radius**2  # Calculate the area using the class
                                    # attribute pi and the radius

# Test case for Circle class
circle = Circle(7)
print(f"Area of circle with radius 7: {circle.area()}")
# Expected output: 153.86



print('\n *** Problem 3 *** ')  # 15 points

"""
What is inheritance in object-oriented programming? Identify at least one
benefit it provides.
"""

print("Answer in the comment.")

"""
# What is inheritance in object-oriented programing?
In object-oriented programming (OOP), inheritance is a mechanism that allows a class
to inherit properties and behaviors from another class. One benefit it provides is that
it encourages code reuse, lessens duplication, and organizes code logically to make it easier to use and update.

"""



print('\n *** Problem 4 *** ')  # 10 points

# Given the class Appliance with an attribute power_source (like "electricity" or
# "gas"):

class Appliance:
    def __init__(self, power_source):
        self.power_source = power_source
class Oven(Appliance):
    def __init__(self,power_source,capacity):
        super().__init__(power_source)
        self.capacity = capacity
        

# Create a subclass Oven that inherits from Appliance and introduces a new
# attribute capacity (i.e. an internal volume in liters). A value for capacity
# must be provided when an Oven object is created, so this must be handled
# by Oven's constructor method __init__().


# Test case for Oven subclass (uncomment to test)   

oven = Oven("electricity", 50)
print(f"Oven with power source {oven.power_source} and",
      f"capacity {oven.capacity} liters.")

# Expected output: Oven with power source electricity and capacity 50 liters.



print('\n *** Problem 5 *** ')  # 15 points

# Create a class Bird with a stub method sound(). Then, create two subclasses:
# Sparrow and Owl. Override the sound() method in each subclass to print their
# respective sounds. Sparrows say "chirp chirp!" and owls say "Hoot hoot!"
class Bird:
    def sound():
        pass
class Sparrow(Bird):
    def sound(self):
        print("Chirp Chirp!")
class Owl(Bird):
    def sound(self):
        print("Hoot Hoot!")

# Test cases for Bird subclasses (uncomment to test)

sparrow = Sparrow()
owl = Owl()

print("Sparrow sound: ", end="")
sparrow.sound()  # Expected output: Chirp chirp!

print("Owl sound: ", end="")
owl.sound()  # Expected output: Hoot hoot!



print('\n *** Problem 6 *** ')   # 15 points

"""
What is polymorphism in OOP? Describe at least one advantage it offers.
"""

print("Answer in the comment.")

"""
# Polymorphism is an object-oriented programming (OOP) concept that refers to the ability of a variable, function or object to take on multiple forms.
Polymorphism in Python allows us to use a single connection to represent different types of objects. It makes our
code more flexible and easier to maintain as there are functions which can handle various object types without the need of specific
class of each object.

"""


print('\n *** Problem 7 *** ')  # 20 points

# Given the class Polygon with an attribute sides representing the number of
# sides:

class Polygon:
    def __init__(self, sides):
        self.sides = sides

# Create a subclass Rectangle that inherits from Polygon and introduces
# attributes length and width: 
class Rectangle(Polygon):
    def __init__(self,length,width,sides=4):
        super().__init__(sides=4)
        self.length = length
        self.width = width

# Finally, create a subclass Square that inherits from Rectangle but only
# requires one side length since all sides are equal:
class Square(Rectangle):
    def __init__(self,width,sides=4):
        super().__init__(width,sides)

# Test cases for Polygon and its subclasses (uncomment to test)

rectangle = Rectangle(10, 5)
square = Square(4)

print(f"Rectangle with {rectangle.sides} sides, length {rectangle.length},",
      f"and width {rectangle.width}.")
# Expected output: Rectangle with 4 sides, length 10, and width 5.

print(f"Square with {square.sides} sides and side length {square.length}.")
# Expected output: Square with 4 sides and side length 4.
"""
 *** Problem 1 *** 
Area of rectangle with length 10 and width 5: 50

 *** Problem 2 *** 
Area of circle with radius 7: 153.86

 *** Problem 3 *** 
Answer in the comment.

 *** Problem 4 *** 
Oven with power source electricity and capacity 50 liters.

 *** Problem 5 *** 
Sparrow sound: Chirp Chirp!
Owl sound: Hoot Hoot!

 *** Problem 6 *** 
Answer in the comment.

 *** Problem 7 *** 
Rectangle with 4 sides, length 10, and width 5.
Square with 4 sides and side length 4.
"""