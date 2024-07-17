"""
Worksheet # 11: Class Design in Python
Student Code
Python Level 3

Name: 
Class Section (if more than one G8 class): 
"""

print('\n *** Problem 1 *** ')

"""
In your own words, what does polymorphism allow us to do in object-oriented
programming?
"""



"""
# Polymorphism is a feature of object-oriented programming languages that allows a specific routine to use variables of different types at different times.

"""


print('\n *** Problem 2 *** ')

"""
Given a Bird class with a stub method called lay_eggs(), describe how you 
would implement polymorphism to allow any subclass of Bird to lay eggs without
knowing whether that subclass builds a nest first, lays eggs in a scrape
in the ground, lays them in another bird's nest, etc.
"""



"""
# 

"""


print('\n *** Problem 3 *** ')

# You are given the Bird class below. First, note that you DON'T need to
# explicitly define an __init__() constructor for a class if you don't have 
# any attributes that need to be assigned or methods that need to be run
# at object creation.

class Bird:
    def __init__(self,name):
        self.self = self
        self.name = name
    
    def lay(self):
        print("f{self.name} is laying eggs.")
        
class Sparrow(Bird):
    def lay(self):
        print(f"{self.name} builds a nest in a tree and lays its eggs there.")
class Plover(Bird):
    def lay(self):
        print(f"{self.name} lays eggs in a scrape on the ground.")
class Cuckoo(Bird):
    def lay(self):
        print(f"{self.name} lays its eggs in another bird's nest.")
    
# Your task is to implement polymorphism in the manner you described in 
# Problem 2. Create three subclasses for Bird using the following
# information about different birds' egg-laying methods:

# a. Sparrow - builds a nest in a tree and lays its eggs there
# b. Plover - lays eggs in a scrape on the ground
# c. Cuckoo - lays its eggs in another bird's nest
B1 = Sparrow("Sparrow")
B2 = Plover("Plover")
B3 = Cuckoo("Cuckoo")

# Run your own test cases demonstrating the polymorphism at work.
for x in (B1, B2, B3):
    print(x.self)
    x.lay()


print('\n *** Problem 4 *** ')

"""
Define 'instance attribute' and 'class attribute' in your own words. Provide
examples of each.
"""

"""
# class attributes remain the same for every object and are defined outside the __init__() function.
Instance attributes are somewhat dynamic because they can have different values in each object.
Instance attributes are defined in the __init__() function. For instance, list is a class in Python.
When we create a list, we have an instance of the list class.


"""


print('\n *** Problem 5 *** ')

# Debugging:
# The following code should print the name and age of a specific Dog instance
# and the kind of diet all dogs need. Explain and fix the bug(s) or mistake(s),
# if any.

class Dog:
    diet = "mainly carnivorous"

    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Coco", 10)
print(my_dog.name)
print(my_dog.age)


print(my_dog.diet)

print("Explanation part of answer in the comment.")

"""
# Line 110 was unecessary as it talked about ur dog. The code should print out the kind of diet that all dogs need so the line was not needed.

"""


print('\n *** Problem 6 *** ')

# You're developing a game where players can create magic potions. Each potion
# can have one primary effect (like "Healing", "Invisibility", etc.). Players
# have a limited inventory space for potions, so the total number of potions
# must be tracked.

# You are given the following Potion class and need to modify it to add:
#     a. a class attribute to track the number of potions created
#     b. a class attribute representing the potion inventory space;
#        set this to 10
#     c. a class method to report the available potion inventory space
#     d. code in the constructor to update the potion count, report how 
#        many potions have been made, and report how much inventory space
#        remains for potions

class Potion:
    def __init__(self, primary_effect):
        self.primary_effect = primary_effect

# Provided test cases:
potion1 = Potion("Healing")
potion2 = Potion("Invisibility")
potion3 = Potion("Haste")


print('\n *** Problem 7: Challenge Problem *** ')

"""
Suppose we wanted to create an even more universal interface than the lay_eggs()
method in the Bird class from Problem 2--a method that will work for all
animals. Obviously, not all animals lay eggs.

Assuming you had an Animal superclass, how would you go about applying
polymorphism in this case? In the Bird class, would you remove the lay_eggs()
method? Why or why not? Explain and provide code to demonstrate your answer.
"""

print("Explanation part of answer in the comment.")

"""
[Answer]

"""
