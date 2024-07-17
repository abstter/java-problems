"""
Worksheet # 3: Python Review
Solutions
Python Level 3

Name: Abhiram
Section: D14
"""

# Uncomment the provided print statements as you complete each problem
# to verify results.


print('\n *** Problem 1 *** ')

# Write a for loop that prints the integers from 0 to 20 but skips
# printing odd numbers by using a continue statement.
for i in range(2, 21):
    if (i % 2 == 0):
        print(i, end=' ')
    


print('\n *** Problem 2 *** ')

# Implement the task in #1 without a continue -- just add an
# argument to range().
for i in range(2, 21, 2):
    print(i, end = ' ')


print('\n *** Problem 3 *** ')

# Write Python code that asks for a positive integer input and prints a
# countdown from that number down to 1, inclusive. If the user inputs a
# non-positive integer, the program should print an error message and ask for
# another input. Use two while loops for this problem — one for the error
# checking and another one for the countdown.
def countdown():
    pos = int(input("Enter a positive integer: "))
    while pos < 0 or pos == 0:
        print("Oops! There is an error. You cannot enter a negative integer.")
        break
    while pos > 0:
        print(pos, end = ' ')
        pos = pos - 1
countdown()
        
    
    


print('\n *** Problem 4 *** ')

# This Python program is meant to calculate the factorial of a given number.
# However, it currently results in an infinite loop due to a bug. Fix the bug
# and add a comment in your code identifying the problem and how your fix
# solved it.

n = int(input("Enter a number: "))
factorial = 1

while n > 1: # With this while loop, n never decreases
    factorial = factorial * n
    n = n -1 # With this piece of code, there is a decrease factor for n
    
     
    
print("The factorial is", factorial)


print('\n *** Problem 5 *** ')
import random
# Write a Python program that randomly chooses a secret number between 1 and 5
# (inclusive), and asks the user to guess the number. The game should continue
# until the user guesses the correct number. Implement this using a while loop
# and a break statement.
number = random.randint(1, 5)
while True:
    guess = int(input("Enter a number (between 1 and 5): "))
    if guess == number:
        print("You guessed it!")
        break
    else:
        print("Wrong guess.")





"""
Challenge Problems
"""

print('\n *** Problem 6 *** ')

# Write a program that builds a sequence of numbers. The program should start
# by printing 1 and then add 2 to the previous number in each subsequent step.
# The program should stop when it reaches or exceeds 100.

import random
num = 1
while num < 100:
    print(num, eND = ' ')
    num += 2


print('\n *** Problem 7 *** ')

# The program is supposed to print all odd numbers from 1 to 20, but it is
# only printing 1 and then hanging/freezing. Fix the bug and add a comment in
# your code identifying the problem and how your fix solved it.

# Buggy code (uncomment to test):

i = 0 # i remains at zero to check that 1 is printed
while i < 20:# This makes sure that 21 isn't printed in this code
    i = i + 1 # By incrementing i by 1 before the if statemnt, you make sure it occurs even with the continue.
    if i % 2 == 0:
        continue
    print(i, end = ' ')
    # Once i becomes 2 (an even number), this line is never reached.
    # The if-condition is always met and the continue statement just
    # keeps executing, continuing the loop indefinitely.
