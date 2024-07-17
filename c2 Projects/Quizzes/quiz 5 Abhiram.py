"""
Quiz 5: Chapter 18
File Reading and Writing
Abhiram Avasarala D14
Python Level 3
"""

"""
All file handling problems must be solved using with statements to open and
automatically close files. All read/write/append operations must be 
performed within with blocks.

Ensure the files 'hello.txt', 'journal.txt', and 'numbers.txt' are in the same 
folder as this script file. All other files will be created using code.

Unless instructed to do so by your teacher, there is no need to print and
submit your output text files--just this script file.
"""

print("+++ Quiz 5: Student Code +++ \n")

print(" *** Problem 1 ***")
print(" See the 'greeting.txt' file to see results.\n")
"""
Debugging: The code below is meant to write "Hello, World!" to a file named
greeting.txt, but it contains an error.

<4 points> In a comment, identify the error.
<4 points> Correct the error.
"""
# The error is that it was in read mode and needs to be in write mode
with open('greeting.txt', 'w') as f:
    f.write("Hello, World!")


print(" *** Problem 2 ***")
print(" See the 'hello_reversed.txt' file to see results.\n")
"""
<16 points> Fill in the missing code. The program should read each line from
file 'hello.txt', call the provided function reverse() to reverse that line,
and write each reversed line to hello_reversed.txt. The reversed output file
will naturally start with a blank line, the result of the first line's ending
newline character being moved to the start.
"""
def reverse(string):
    return string[::-1]

# <8 points> Open 'hello.txt' for reading and 'hello_reversed.txt' for writing
# in the same with statement. Use appropriate file variable names:
with open('hello.txt', 'r') as source_file, \
     open('hello_reversed.txt', 'w') as destination_file:
# <8 points> Loop over each line in 'hello.txt' and write the reversed
# version of each line (using the provided reverse() function) to
# 'hello_reversed.txt':
    content = source_file.read()
    destination_file.write(reverse(content))
    


print(" *** Problem 3 ***")
print(" Answer in comment.\n")
"""
<10 points> Compare and contrast the 'a' (append) mode and the 'w' (write) mode
in file operations with Python.

[Answer below:]
# Write mode is used when you want to write data to a file. If the file exists, it will be overwritten.
If the file doesn’t exist, Python will create it.

# Append mode is used when you want used to add data to the end of the file. It won’t delete the existing data.
If the file doesn’t exist, Python will create it.

"""


print(" *** Problem 4 *** ")
print(" See the 'sums.txt' file to see results.\n")
"""
<24 points total> Fill in the missing code in the following Python program that 
calculates the sum of numbers in 'numbers.txt' and appends the sum to 'sums.txt' 
(which doesn't exist yet).
"""
total_sum = 0
# <4 points> Open 'numbers.txt' for reading. Use the file variable num_file:
with open('numbers.txt', 'r') as num_file: 
    # <4 points> Loop over each line in num_file. Use a for loop:
    for line in num_file:
        # <4 points> Remove any leading/trailing whitespace from the line:
        line = num_file.readline().strip()  
        # Check if the line contains only digits:
        if line.isdigit():
            # <4 points> Convert the line to an integer and add it to total_sum:
            total_sum = total_sum + int(line)

# <4 points> Open 'sums.txt' for appending. Use file variable sums_file.
# (Opening the file for appending will create the file.)
with open('sums.txt', 'a') as sums_file:
    # <4 points> Convert the sum to a string and write it in sums_file:
    sums_file.write(str(total_sum))


print(" *** Problem 5 *** ")
print(" See the 'hello_allcaps.txt' file to see results.\n")
"""
<16 points total> Fill in the missing code to complete the following program, 
which should read the content of 'hello.txt', convert all the content to 
uppercase, and write it to the file 'hello_allcaps.txt'.
"""
# <8 points> Open 'hello.txt' for reading and 'hello_allcaps.txt' for writing
# in the same with statement. Use appropriate file variable names:
with open('hello.txt', 'r') as source_file, \
     open('hello_allcaps.txt', 'w') as destination_file:
    # <4 points> Read the entire content of the file into a single string:
    content = source_file.read()
    # <4 points> Write that string in uppercase to the output file:
    destination_file.write(content.upper())


print(" *** Problem 6 ***")
"""
<16 points total> Fill in the missing code to complete the following program. 
The program will read and output the contents of the 'journal.txt' file, adding
'Day 1:', 'Day 2:', etc. when printing each line read from the file.
"""
# <4 points> Open a file named 'journal.txt' for reading.
with open('journal.txt', 'r') as file:
    i = 0  # Initialize i for counting lines
    for line in file:
        # <4 points> Increment i to continue the line count.
        i = i + 1
        # <4 points> Remove leading and trailing whitespace from line:
        clean_line = file.readline().strip()  
        # <4 points> Print clean_line preceded by the day number. The output
        # should look like 'Day 1: Touched down at JFK...'
        print(f"Day {i}: {clean_line}")
        


print("\n *** Problem 7 *** ")
print(" Answer in comment.\n")
"""
<10 points total - 5 points per benefit>
Consider a recipe builder app that assists in creating recipes, scaling
servings, and more. Describe two benefits of using files (such as text files)
to save and load recipes and ingredients, as opposed to hard-coding them
into the program or entering all the data each time you use the program.

[Answer below:]
# Persistant Data Storage: Files keep information safe and ready for you when you return. 
# Scalability: the ability to save information to files means your recipe can handle more data over time.
# files are capable of storing much more information than data structures created purely in memory/RAM,
which has a much smaller capacity
"""
