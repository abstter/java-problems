"""
Worksheet # 5: Tuples
Student Code
Python Level 3

Name:
Section:
"""

# Uncomment any provided print statements as needed to verify results.

"""
Part 1
"""

print('\n *** Problem 1 - Creating Tuples *** ')

# 1a. Write code to create and print a tuple named "cities" with the elements
#     'New York', 'Paris', 'Tokyo', 'London'.

print('\n(1-a)')
cities = 'New York', 'Paris', 'Tokyo', 'London'
print(cities)

# 1b. Write code to create a single-element tuple named "single" with the 
#     element 100 (add a trailing comma). What will happen if you don't  
#     include a trailing comma? Try this as well to test your hypothesis.

print('\n(1-b)')
single = (100,)
print(single)


print('\n *** Problem 2 - Accessing Tuple Elements *** ')

# 2a. Write code that creates a tuple named "days" with the elements 
#     'M', 'Tu', 'W', 'Th', 'F'. Then, print the element for 'Tu' using
#     the index number.
print('\n(2-a)')
days = 'M', 'Tu', 'W', 'Th', 'F'
print(days[1])

# 2b. Write code to slice the days tuple to print the weekday abbreviations
#     from Tu to F.

print('\n(2-b)')
days = 'M', 'Tu', 'W', 'Th', 'F'
print(days[1:5])

print('\n *** Problem 3 - Tuple Immutability *** \n')

# 3.  Write code to try to change the third element of the "cities" tuple to
#     'Berlin'. What happens and why? Type your answer as a comment.
cities = 'New York', 'Paris', 'Tokyo', 'London'
#cities[2] = "Berlin"
#print(cites[2])
# Output
#TypeError: 'tuple' object does not support item assignment



print('\n *** Problem 4 - Tuple Packing and Unpacking *** ')

# 4a. Write code to create a tuple named "student_scores" by
#     packing the following scores: 85, 90, 78, 92 (no parentheses).

print('\n(4-a)')
student_scores = 85, 90, 78, 92
print(student_scores)  # Output: (85, 90, 78, 92)

# 4b. Write code to unpack the "student_scores" tuple into variables named
#     "math", "science", "english", "history" using multiple assignment. 
#     Then, print the score for English.

print('\n(4-b)')
student_scores = 85, 90, 78, 92
math, science, english, history = 85, 90, 78, 92
print(english)  # Output: 78

# 4c. What will happen if you try to unpack "student_scores" into three
#     variables instead of four? Write code to test your hypothesis.

print('\n(4-c)')
print("Code commented to prevent error. Uncomment to see what happens.")
#math, science, english = student_scores
# Output
#ValueError: too many values to unpack (expected 3)

"""
Part 1: Challenge Problem
"""

print('\n *** Problem 5 - Tuple Unpacking, Formatted Output *** \n')

# You are given a student name, their grade, and their average score as a 
# tuple. You need to print this information in a formatted way. Use tuple
# unpacking to get the information from the tuple, then print the information
# in a user-friendly format. Here is an example tuple that you might be given:

student_info = ("John Smith", "8th grade", 92.5)
name, grade, score = "John Smith", "8th grade", 92.5
print(f"{name}, who is in {grade}, has an average score of {score}.")
# Here is what the output of your code should look like:
# John Smith, who is in 8th grade, has an average score of 92.5.



"""
Part 2
"""

print('\n *** Problem 6 - Tuple Concatenation *** \n')

# Each class in a school's 8th grade (“8A”, “8B”, “8C”) forms teams for a
# science competition. Class “8A” has formed two teams (“Neutrons”, “Protons”),
# class “8B” has formed two teams (“Electrons”, “Photons”), and class “8C” has
# formed two teams (“Quarks” and “Leptons”).

# To track this information, declare variables teams_8A, teams_8B, and teams_8C
# and assign each to a tuple containing the class and team names. Then, write
# code to combine these tuples into a single tuple called all_teams.
teams_8A = "Neutrons", "Protons" 
teams_8B = "Electrons", "Photons"
teams_8C = "Quarks", "Leptons"
all_teams = teams_8A, teams_8B, teams_8C 
print(all_teams)


print('\n *** Problem 7 - Tuple Repetition *** \n')

# Each round of the science competition has the same order of subjects for its
# questions: (“Physics”, “Chemistry”, “Biology”, “Astronomy”, “Geology”). There
# are four rounds in the contest. Create a new tuple based on the one below to
# create a continuous subject pattern for the questions in all four rounds.
# Assign the tuple into all_questions.

round_questions = ('Physics', 'Chemistry', 'Biology', 'Astronomy', 'Geology')
all_questions = round_questions*4
print(all_questions)

print('\n *** Problem 8 - Membership Checking *** ')

# 8a. You have a tuple with the collection of books below. Write code to check
#     whether “Hunger Games” is in this collection.

print('\n(8-a)')
books = ('Harry Potter', 'Lord of the Rings', 
         'Hunger Games', 'Percy Jackson', 'Narnia')
print('Hunger Games' not in books)
# 8b. Given the same collection of books in the previous question, write a
#     program that checks if “Maze Runner” is not in the collection.

print('\n(8-b)')
print('Maze Runner' not in books)

print('\n *** Problem 9 - Tuple Iteration *** ')

# 9a. Using the books tuple, write a loop that prints each book title on a 
#     new line.

print('\n(9-a)')
for book in books:
    print(book)
# 9b. Now, let’s assume the books tuple represents the books’ arrangement on a
#     shelf. Write a for loop that prints the index and title of each book in
#     the books tuple (e.g., “Book 1: Harry Potter”) on a new line.

print('\n(9-b)')
for i in range(len(books)):
    print("Book",i+1,":",books[i])
# 9c. Your school is hosting a trivia competition and you’ve been asked to help
#     keep track of the teams and their scores. The data is stored as a tuple
#     (given below), where each element is another tuple that contains a team’s
#     name and their score.

scores = (("Eagles", 150), ("Falcons", 165),
          ("Cardinals", 140), ("Blue Jays", 170))

# Write code to print out each team’s name and their corresponding score on a
# new line, as shown below:
#
#     The team Eagles has a score of 150.
#     The team Falcons has a score of 165. ...etc.

print('\n(9-c)')
for score in scores:
    print("The team",score[0], "has a score of", score[1])
"""
Part 2: Challenge Problems
"""
print('\n *** Problem 10 - Nested Tuple Conversion *** \n')

# Python's built-in tuple() function accepts another data structure such as a
# list as an argument and converts it to a tuple, if it can. However, it only
# converts the outermost layer of the data structure; a list of lists would
# just be converted into a tuple of lists. Try this in the interactive Shell:
#     tuple([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Write a function nested_list_to_tuple() that accepts a list of lists, where 
# each inner list should be converted to a tuple using the tuple() function.
# Your function should return a list of these tuples.
def nested_list_to_tuple():
    tuple([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
nested_list_to_tuple()
    

print('\n *** Problem 11 - Nested Tuple Iteration *** \n')

# You are given a tuple that contains weather data for a week. Each element
# in the tuple is another tuple with two elements: the first is the day of the
# week and the second is that day's average temperature in Fahrenheit.

# Write a function hottest_day(data) to accept that tuple of day-temp tuples
# and find the day with the highest average temperature. It should return a
# tuple consisting of that day and its temperature.

weather_data = (("Monday", 85), ("Tuesday", 80), ("Wednesday", 90),
                ("Thursday", 88), ("Friday", 83),
                ("Saturday", 79), ("Sunday", 85))

#print(hottest_day(weather_data))
# Output: ('Wednesday', 90)


print('\n *** Problem 12 - Tuple Reversal *** \n')

# Write a Python function reverse_tuple() that takes a tuple as its argument 
# and returns a new tuple that is the reverse of the input. Note: tuples may 
# be immutable, but you can form new tuples by slicing existing ones or 
# combining them using concatenation (+). Test your function on tuple_n:
def reverse_tuple(my_tuple):
    l = []
    for i in range(len(my_tuple)):
        l.append(my_tuple[len(my_tuple - (i+1))])
    print("tuple_n =", reversed_tuple, "\n") 
    