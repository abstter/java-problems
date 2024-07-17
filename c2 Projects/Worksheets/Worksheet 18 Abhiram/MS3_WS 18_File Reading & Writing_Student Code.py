"""
Worksheet # 18: File Reading and Writing
Student Code
Python Level 3
"""

print("\n +++ Worksheet 18: Student Code +++ \n")

"""
All file handling problems must be solved using with statements to open and
(automatically) close files. All read/write/append operations must be 
performed within with blocks.

Ensure the files 'data.txt', 'Keats.txt', 'log.txt', 'more_names.txt',
'names.txt', and 'Wilcox.txt', are in the same folder as this script file
when running it.

Unless instructed to do so by your teacher, there is no need to print and
submit your output text files--just this script file.
"""

print('\n *** Problem 1 ***')
print(' Answer in comment.\n')
"""
Why is it important to close a file after opening, once you have
performed the intended file operation? How does the with statement
make this easier/less error-prone?

[Answer below:] Closing a file releases resources back to the operating system
and ensures that all of your data is properly written out to disk. Using a with statement statement automatically takes care
of opening and closing the file, even if an error occurs while processing the file. This is particularly important because leaving files open can consume system resources unnecessarily
and might lead to data being lost or corrupted.  


"""


print('\n *** Problem 2 *** \n')
"""
Using the with statement, open the file 'Keats.txt' for reading.
Read and print the contents of the file to the console.
"""
with open('Keats.txt', 'r') as file:
    content = file.read()
    print(content)



print("\n *** Problem 3 *** \n")
"""
Copy the code from Problem 2 and modify it to print the lines of text
double-spaced. This shouldn't modify the original file but rather just
the output. Use the .readlines() method to read in the file as a list
of strings.
"""
with open('Keats.txt', 'r') as file: 
    content = file.read()
    lines = file.readlines()
    for line in lines:
        print(line, end="\n")
    print(content)


print("\n *** Problem 4 *** ")
print(' See the messages.txt file to see results.\n')
"""
Create a new text file named 'messages.txt' and write the messages
'Hello, World!' and 'Python is fun!' on separate lines in the file.
"""
with open('messages.txt', 'w') as file:
    file.write('Hello, world!\n')
    file.write('Python is fun!')





print("\n *** Problem 5 *** ")
print(' See the data_table.txt file to see results.\n')
"""
Write a program that reads the content of 'data.txt' and writes the content
to a new file 'data_table.txt' with a row of dashes between each row, e.g.:
------------
99 89 92 87
------------
75 84 98 95
...etc.
"""

with open('data.txt', 'r') as source_file, \
     open('data_table.txt', 'w') as destination_file:
    content = source_file.readlines()
    for line in content:
        destination_file.write('------------\n')
        destination_file.write(line)
        



print("\n *** Problem 6 *** ")
print(' See the names.txt file to see results.\n')
"""
Write a program that reads the content of 'more_names.txt' and appends it
to the file 'names.txt'.
"""
with open('more_names.txt', 'r') as source_file, \
     open('names.txt', 'a') as destination_file:
    content = source_file.readlines()
    for line in content:
        destination_file.write(line)

    
print("\n *** Problem 7 *** ")
print(' Answer in comment.')
"""
If you were to revise your zoo simulator program to use data files (instead of
keeping all the data with the code), what could you store in those files? What
would be the benefits of doing that?

[Answer below:] In the zoo simulator program, you could store each of the classes in the data files. This makes the code much more organized,
much more safe to use, and seperates the code into smaller units. This makes the code not only easier to maintain but organized as well. Also using the files
allow sharing information between devices, fostering compatability. 


"""


print('\n *** Problem 8: Challenge Problem ***')
"""
Write a program that counts how many times the word "error" appears in a log 
file named 'log.txt'. The 'log.txt' file can be found in LabCommons along with
this worksheet script. As a simpler alternative to using loops, use the count()
method to count the number of occurrences of a substring in a string.

For example:
    'Mississippi'.count('ss') # returns 2

Ignore letter case. Print the 'error' count in an informative message.
"""



print('\n *** Problem 9: Challenge Problem ***')
"""
Now, write a program that counts how many *lines* contain the word "error"
in the log file 'log.txt'. This time, you will need to use a line-by-line loop
to check for instances of the word in each line.

Ignore letter case. Print the count of lines with the word "error" in an
informative message.
"""



print('\n *** Problem 10: Challenge Problem ***')
print(' See the Wilcox_Numbered.txt file to see results.\n')
"""
Read a file named 'Wilcox.txt' and write the same content but with
line numbers to a new file titled 'Wilcox_Numbered.txt'.
"""
