"""
Worksheet # 1: Python Review
Student Code
Python Level 3

Name:
Section:
"""

# Uncomment the provided print statements as you complete each problem
# to verify results.

"""
Part 1
"""

print('\n *** Problem 1 *** ')

def subtotal(price, qty):
    total = price * qty
    roun = round(total,2)
    return roun
    
print(subtotal(3.68, 12))


print('\n *** Problem 2 *** ')

def total_with_tax(s_amt, tax_rate):
    thing = tax_rate/100
    tax = round(s_amt * thing, 2)
    return s_amt + tax

print(total_with_tax(75, 8.25))


print('\n *** Problem 3 *** ')

item_total = 
print(item_total)


print('\n *** Problem 4 *** ')

# Define a function concat_str() that concatenates two strings together with
# an optional separator, returning the result. The default separator should be
# a single space. Test your function with two strings and no separator provided,
# and again with two strings and a separator of your choice.

#print(concat_str('Hello', 'world!'))
#print(concat_str('Hello', 'world!', ', '))
#print(concat_str('Hello', 'world!', sep = '...'))


print('\n *** Problem 5 *** ')

# The following function is supposed to calculate and return the area of a
# circle given the radius, but it’s not producing the correct result. Identify
# and fix the problem(s).

def circle_area(r):
    area = (math.pi * radius) * 2
    print(area)

print(circle_area(5))
print(circle_area(99.9))


"""
Part 2
"""

print('\n *** Problem 6 *** ')

# Define a function find_max() that takes three numbers as parameters and  
# returns the maximum of the three.

# Write your own test cases to test your function.


print('\n *** Problem 7 *** ')

# Write a Python function eval_temp(temp) that takes a temperature
# as a parameter and returns 'Hot' if the temperature is above 85
# degrees, 'Warm' if the temperature is between 70 and 85 degrees
# inclusive, 'Cool' if the temperature is between 50 and 70 degrees
# (including 50 but excluding 70), and 'Cold' if the temperature
# is below 50.

# Write your own test cases to check every branch of your conditional,
# including edge cases.


print('\n *** Problem 8 *** ')

# The following code is supposed to check whether a list is sorted
# in ascending order or not, but it’s not working correctly.
# Identify and fix the problem(s). 
#   a.  First, determine when the expected output matches the actual
#       output and when it doesn’t, identify why that happens. 
#   b.  Once you fix that bug, you will likely encounter an error.
#       Fix it if/when it arises. Remember that fixing a bug can
#       reveal other bugs that had previously been hidden.

def is_sorted(list):
    for i in range(len(list)):
        if list[i] > list[i + 1]:
            return False
        else:
            return True

print(is_sorted([1, 2, 3, 4, 5]))  
# Expected output: True

print(is_sorted([1, 3, 2, 5, 4]))  
# Expected output: False


print('\n *** Problem 9 *** ')

# You’re programming a simple game where the player is located in a 2D grid at
# a position with coordinates stored in a list coord = [x, y]. The player has
# three possible actions: 'up', 'down', 'left', 'right'. Each action changes
# the player's position: 'up' decreases the y-coordinate by 1, 'down' increases
# the y-coordinate by 1, 'left' decreases the x-coordinate by 1, and 'right'
# increases the x-coordinate by 1.

# Write a Python function move_player(coord, action) that takes the player’s
# current coordinates in a list and an action (a string) as parameters, and
# returns a new list with the updated coordinates after the action is performed.
# You can assume that the action will always be one of the four valid actions.
# Then, reassign the player’s global coordinate list to the function’s return
# value.


# Test the function. Call move_player() to move the player up, down, left, 
# and right. Print player_coord after each move to verify the results.

player_coord = [0, 0]
