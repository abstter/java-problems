"""
Quiz # 1: Python Shortcuts
Python Level 3

Fill out your name and section below.

Name: Abhiram
Section: D14
"""

# 1. Given the variables first_name = "Ada" and last_name = "Lovelace",
#    use f-string formatting to print the full name in the format:
#    "Last, First: Lovelace, Ada". [10 points]

print("\n*** Problem 1 ***")
first_name = "Ada"
last_name = "Lovelace"
print(f"Last, First: {last_name}, {first_name}.")


# 2. Use a from-import statement to import pi from the math module. Then, use
#    f-string formatting to print pi rounded to 2 decimal places. [12 points]

print("\n*** Problem 2 ***")
from math import pi
formatted_string = f"{pi:.2f}"
print(formatted_string)


# 3. Given the variables product = "Apple", quantity = 10, and price = 1.2,
#    use f-string formatting to print:
#    "The total price for 10 Apples is $12.00." [12 points]

print("\n*** Problem 3 ***")
product = "Apples"
quantity = 10
price = 1.2
print(f"The total price for {quantity} {product} is ${price*quantity}0.")


# 4. In a geometry application, you're calculating the volume of a cylinder.
#    The radius and the height each are results of different function calls,
#    and the calculation itself involves calls to math.pi, the radius, 
#    and calculate_height(). The formula for the volume of a cylinder is:

#        cylinder_volume = pi * radius squared * height

#    Write the calculation and assign it into the cylinder_volume variable.
#    To ensure the code is readable, use line continuation to split the
#    calculation over multiple lines (each term on its own line). Uncomment
#    the print statement to verify results. [18 points]

print("\n*** Problem 4 ***")

import math

def calculate_radius(circumference):
    # circumference is given in meters (m)
    # returns the radius in meters (m)
    return circumference / (2 * math.pi)

def calculate_height(surface_area, radius):
    # surface_area is given in square meters (m^2)
    # radius is given in meters (m)
    # returns the height in meters (m)
    return ((surface_area - 2 * math.pi * radius ** 2)
            / (2 * math.pi * radius))

# Given values
circumference = 31.4  # meters
surface_area = 314.16  # square meters
radius = calculate_radius(circumference) # meters

# Calculation of cylinder_volume
cylinder_volume = math.pi * \
                  (calculate_radius(circumference))* \
                  (calculate_height(surface_area, radius))
                  
print(round(cylinder_volume, 1), "cubic meters")  # Uncomment when done


# 5. You are calculating the average speed of a journey. The total distance 
#    and the total time are each results of different function calls. Write the
#    calculation and assign it into the variable average_speed. Use implicit
#    line continuation to ensure your formula remains readable. [12 points]

print("\n*** Problem 5 ***")

def calculate_total_distance(start, end):
    # Returns the total distance of the journey
    return end - start

def calculate_total_time(departure, arrival):
    # Returns the total time of the journey
    return arrival - departure

# Given values
start = 0
end = 100  # in km
departure = 9  # in hours
arrival = 11  # in hours

# Calculation of average_speed
average_speed = (calculate_total_distance(start, end) /
                calculate_total_time(departure, arrival))
                 
print(average_speed, "km/hr")    # Uncomment when you are done

# 6. Use multiple assignment to assign the values True, False, and True to the
#    variables p, q, and r respectively. [8 points]

print("\n*** Problem 6 ***")

p, q, r = "True", "False", "True"
print("p is", p, "... q is", q, "... r is", r)   # Uncomment when you are done


# 7. Use multiple assignment to swap the values of variables x and y (between
#    the two print statements). [8 points]

print("\n*** Problem 7 ***")

x = 12
y = 4
print("Before the swap, x is", x, "and y is", y)
x, y = y, x
print("After the swap, x is", x, "and y is", y)

# 8. You are tracking a player's score in a game. On day 1, the player scores
#    150 points, on day 2, they score 200 points, on day 3, they double their
#    current score by finding a bonus, and on day 4, they lose 100 points for 
#    a mistake. Use augmented assignment to perform a separate update to the
#    score for each day (before each comment on the same line). [20 points]

print("\n*** Problem 8 ***")

score = 0
score += 150 # Day 1 
score += 200 # Day 2
score*2 # Day 3
score -= 100 # Day 4
print("After Day 4, the player's score is", score)

# Output Files
'''

*** Problem 1 ***
Last, First: Lovelace, Ada.

*** Problem 2 ***
3.14

*** Problem 3 ***
The total price for 10 Apples is $12.00.

*** Problem 4 ***
78.6 cubic meters

*** Problem 5 ***
50.0 km/hr

*** Problem 6 ***
p is True ... q is False ... r is True

*** Problem 7 ***
Before the swap, x is 12 and y is 4
After the swap, x is 4 and y is 12

*** Problem 8 ***
After Day 4, the player's score is 250
'''
