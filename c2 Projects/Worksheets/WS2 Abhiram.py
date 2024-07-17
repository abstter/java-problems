"""
Worksheet # 2: Python Review
Student Code
Python Level 3

Name: Abhiram Avasarala 
Section: D14
"""

# Uncomment the provided print statements as you complete each problem
# to verify results.

"""
Part 1
"""

print('\n *** Problem 1 *** ')

# Given a list num_list = [5, 7, 9, 11, 13], write a statement
# to create a new list containing the second, third, and fourth
# elements from the original list:

num_list = [5, 7, 9, 11, 13]
new_num_list = num_list[1:4]
print(new_num_list)


print('\n *** Problem 2 *** ')

# Write a Python function copy_and_add() that takes a list and
# an element as parameters, makes a copy of the list, adds the
# element to the end of the copied list, and returns the copy.
# Write your own test cases.
def copy_and_add(my_list, element):
    new_list = my_list
    new_list.append(element)
    return new_list
print(copy_and_add([1,5,8,9], 7))

print('\n *** Problems 3*** ')

# Write a function first_and_last(input_list) that takes a list as
# a parameter and returns a new list containing only the first and 
# the last elements of the input list. For example, for the input 
# list [1, 2, 3, 4, 5], the function should return [1, 5].
def first_and_last(input_list):
    new_list = []
    new_list.append(input_list[0])
    new_list.append(input_list[-1])
    return new_list
objects = ['train', 'plane', 'box']
print(first_and_last(objects))

print('\n *** Problems 4*** ')

def first_and_last(input_list):
    new_list = []
    new_list.insert(0, input_list[0])
    new_list.insert(1, input_list[1])
    return new_list
objects = ['train', 'plane', 'box']
print(first_and_last(objects))
"""
Part 1: Challenge Problems
"""

print('\n *** Problem 5 *** ')

# Write a function merge_list_halves(list1, list2) that takes the
# first half of its parameter list1 (rounded down for odd-length
# lists) and the second half of list2 (rounded up for odd-length 
# lists), combines the two halves into a new list, and returns it.
# Create at least test two test cases: one with even-length lists,
# and one with odd-length lists.

    

print('\n *** Problem 6 *** ')

# Write a function called interleave_list_halves(values) to combine the first
# half of list1 with the second half of list2, like merge_list_halves() from
# #5, but with one key difference—it should interleave the two halves. That
# means, the function should take one element from the first half of list1,
# then one from the second half of list2, and so on, repeating this pattern
# until it has used up all elements from one or both halves. If one half runs
# out of elements before the other, append all remaining elements from the
# other half to the end of the new list.

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [9, 10, 11]
#print(interleave_list_halves(list1, list2))



"""
Part 2
"""

print('\n *** Problem 7 *** ')

# Given the list of movies below, where the order of the movies
# represents a child’s rankings, write Python code that asks for
# a movie title and returns that movie’s rank (1 being the highest
# and 5 being the lowest) with an informative message. Make sure
# to check for membership first to avoid an error.
movies = ["Toy Story", "Frozen", "The Incredibles",
              "Finding Nemo", "Moana"]
def movie_titles():
    title = input("Enter a movie title:\n ")
    movie = movies.index(title,0,len(movies))
    print("Informative message: This is a cool game.")
    print("The movies are fun.")
    return (movie+1)
print(movie_titles())
    


print('\n *** Problem 8 *** ')

# Given a list of weekly temperatures below, write Python code that
# asks for a day number (1-7), checks whether it’s within the list’s
# bounds, and prints the temperature for that day if it exists or a
# suitable error message otherwise.
temperatures = [74, 70, 72, 75, 79, 82, 81]
def check_temp():
    days = [1, 2, 3, 4, 5, 6, 7]
    day_user = input("Enter a day number(1-7): ")
    if int(day_user) in days:
        return temperatures[days.index(int(day_user))]
    else:
        return("There is an error.")
print(check_temp())
    

print('\n *** Problem 9 *** ')

# Given a list of students, write Python code that iterates over the
# list and adds "is awesome!" to each name before printing it out.
# For example, the program should print:
#     Ana is awesome!
#     Bob is awesome!
#     etc.

students = ["Ana", "Bob", "Cid", "Dal", "Eva"]
def add_awesome():
    for i in range(len(students)):
        students[i] = str(students[i]) + " is awesome"
        print(students[i])
add_awesome()

print('\n *** Problem 10 *** ')

# Given the two-dimensional list below representing the seats in a
# theater, where "X" means the seat is taken and "O" means the seat
# is available, write code that counts and prints the total number
# of available seats.

seats = [['X', 'O', 'X'], ['O', 'O', 'X'], ['X', 'X', 'O']]
def open_seats():
    number = 0
    for i in seats:
        for j in i:
            if j == "O":
                number = number + 1
            if j == "X":
                number = number
    return number
print(open_seats())
                
    

"""
Part 2: Challenge Problems
"""

print('\n *** Problem 11 *** ')

# Given the two lists below, one with students’ names and one with 
# their test scores, write code that iterates over both lists
# simultaneously, using index-based iteration, and prints each
# student’s name along with their score. Do this in only two
# additional lines of code after the initial list assignments.

students = ["Ana", "Bob", "Cid", "Dal", "Eva"]
scores = [87, 84, 93, 85, 92]

for i in range(len(students)):
    print("The score of", students[i], "is", scores[i],".")
    

print('\n *** Problem 12 *** ')

# The following code is supposed to add up the elements in each row
# of the multiplication table and append the sum to a new list
# called row_sums. However, the program contains two bugs that
# causes some semantic errors. Fix the bugs. Hint: Trace the events
# to see if every action is happening at the correct time, both
# inside and outside the loop.

# Uncomment and fix the buggy code below:
"""
mult_table = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
row_sums = []
row_num = 0
sum_of_row = 0  # The row sum is only initialized to 0 at the start;
                # it should be reset back to 0 for every row

for row in mult_table:
    row_num = row_num + 1
    for num in row:
        sum_of_row = sum_of_row + num
        row_sums.append(sum_of_row)   # The current row sum is being
                                      # appended for every *value*;
                                      # should be for every row
        
print("The list of row sums is", row_sums)

"""
#Output FILE
# *** Problem 1 *** 
#[7, 9, 11]
#
# *** Problem 2 *** 
#[1, 5, 8, 9, 7]
#
# *** Problems 3*** 
#['train', 'box']
#
# *** Problems 4*** 
#['train', 'plane']
#
# *** Problem 5 *** 
#
# *** Problem 6 *** 
#
# *** Problem 7 *** 
#Enter a movie title:
# Moana
#Informative message: This is a cool game.
#The movies are fun.
#5
#
# *** Problem 8 *** 
#Enter a day number(1-7): 3
#72
#
# *** Problem 9 *** 
#Ana is awesome
#Bob is awesome
#Cid is awesome
#Dal is awesome
#Eva is awesome
#
# *** Problem 10 *** 
#4
#
# *** Problem 11 *** 
#The score of Ana is 87 .
#The score of Bob is 84 .
#The score of Cid is 93 .
#The score of Dal is 85 .
#The score of Eva is 92 .

