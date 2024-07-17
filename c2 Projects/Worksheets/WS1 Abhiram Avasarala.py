"""
Worksheet # 1: Python Review
Student Code
Python Level 3

Name: Abhiram Avasarala
Section: Grade 8
"""

# Uncomment the provided print statements as you complete each problem
# to verify results.

"""
Part 1
"""

print('\n *** Problem 1 *** ')

def subtotal(price, qty):
    total = price * qty
    rounded = round(total,2)
    return rounded

print(subtotal(3.68, 12))


print('\n *** Problem 2 *** ')

def total_with_tax(subtotal_amt, tax_rate):
    tax = round(subtotal_amt * tax_rate/100, 2)
    return subtotal_amt + tax

print(total_with_tax(75, 8.25))


print('\n *** Problem 3 *** ')

item_total = total_with_tax(subtotal(3.68, 12), 8.25)
print(item_total)


print('\n *** Problem 4 *** ')
def concat_str(str1, str2, seperator = ' '):
    return str1 + seperator + str2

#print(concat_str('Hello', 'world!'))
print(concat_str('Hello', 'world!', ', '))
#print(concat_str('Hello', 'world!', sep = '...'))


print('\n *** Problem 5 *** ')

# The following function is supposed to calculate and return the area of a
# circle given the radius, but it’s not producing the correct result. Identify
# and fix the problem(s).
import math
def circle_area(r):
    area = math.pi * r**2
    return area

print(circle_area(5))
print(circle_area(99.9))


"""
Part 2
"""

print('\n *** Problem 6 *** ')

# Define a function find_max() that takes three numbers as parameters and  
# returns the maximum of the three.
def find_max(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        print("Cant find greatest number.")


print(find_max(3, 9, 6))



print('\n *** Problem 7 *** ')

# Write a Python function eval_temp(temp) that takes a temperature
# as a parameter and returns 'Hot' if the temperature is above 85
# degrees, 'Warm' if the temperature is between 70 and 85 degrees
# inclusive, 'Cool' if the temperature is between 50 and 70 degrees
# (including 50 but excluding 70), and 'Cold' if the temperature
# is below 50.
def eval_temp(temp):
    if temp > 85:
        return "Hot"
    if temp >= 70 and temp <= 85:
        return "Warm"
    if temp >= 50 and temp < 70:
        return "Cool"
    if temp < 50:
        return "Cold"
    else:
        print("Incorrect input.")
print(eval_temp(71))
print(eval_temp(89))
print(eval_temp(51))
print(eval_temp(40))
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
    for i in list:
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
def move_player(coord, action):
    if action == "up":
        coord[1] = coord[1]-1
    if action == "down":
        coord[1] = coord[1]+1
    if action == "left":
        coord[0] = coord[0]-1
    if action == "right":
        coord[0] = coord[0]+1
    return coord

# Test the function. Call move_player() to move the player up, down, left, 
# and right. Print player_coord after each move to verify the results.
player_coord = [0, 0]
print(move_player(player_coord, "up"))
print(move_player(player_coord, "down"))
print(move_player(player_coord, "right"))
print(move_player(player_coord, "left"))

'''
Output:

 *** Problem 1 *** 
44.16

 *** Problem 2 *** 
81.19

 *** Problem 3 *** 
47.8

 *** Problem 4 *** 
Hello, world!

 *** Problem 5 *** 
78.53981633974483
31353.126098752677

 *** Problem 6 *** 
9

 *** Problem 7 *** 
Warm
Hot
Cool
Cold

 *** Problem 8 *** 
True
False

 *** Problem 9 *** 
[0, -1]
[0, 0]
[1, 0]
[0, 0]
'''