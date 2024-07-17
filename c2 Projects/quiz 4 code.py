"""
Quiz #4: Chapter 10
Problem Code and Solutions
Python Level 2

***
Students: copy this file from LabCommons into your H:\ drive and
replace "Student Code" in the file name with your user name
(e.g., MS2_Quiz4_JohnD.py). Rename a file by selecting it and
pressing F2. The file must be closed to do this.

FILL IN THE FIELDS BELOW AND SUBMIT A PRINTOUT
OF THIS FILE WITH YOUR QUIZ PAPER

Following these instructions is worth 1 point.
***

Name:
Grade/Section:
Date:


"""
print('\n*** Problem 1 ***')           # 15 points

# Add code to the line with a # to finish defining space_out(). This 
# should print each character in string s with an extra space added
# between each of its characters.
# Remove the """ before and after the code to run it.
def space_out(s):
    for ch in s:
        print(ch)
space_out("three")
                    


# Add two test cases to ensure the function works as intended:
space_out("bob")
space_out("call")



print('\n\n*** Problem 2 ***')         # 15 points

# Redefine space_out() below to return the spaced-out string in a
# variable new_string (instead of just printing it).
# You will need to add code on every line with a #.
def space_out(s):
    s = new_string         
    for ch in new_string:
        print(ch)
space_out("orange")

                    


# Copy-paste the same two test cases from #1 below to ensure the
# function still works as intended:
space_out("bob")
space_out("call")



print('\n*** Problem 3 ***')           # 15 points

# Define trim() to return a slice of the string contained in its
# parameter whole. That slice must exclude the first and last 
# characters but keep everything else. (Thus, if whole has 2 or
# fewer characters, trim() should not output anything.)

def trim(whole):
    return whole[1:] + whole[:1]
    

# Add three test cases below with strings of 1, 2, and 4+ characters.



print('\n*** Problem 4 ***')           # 20 points

"""
Some programming languages, such as Java, follow a naming convention
called "camel case," in which words in identifiers are separated by
capitalizing their first letters. The first letter of the first word
may or may not be capitalized, depending on what the name represents.
For example: portOfOrigin or LocationMap. 

Python does not follow camel case; instead it follows 'underscore
case', in which words are separated by an underscore. This is
generally easier to read. For this problem, write a function called
und_case() that accepts a string parameter s containing a group of
words in camel case. The function should convert those words into
underscore case and return the resulting string. Leave the first
letter's case unchanged and don't add an underscore before it. Test
your function with strings of multiple camel case words with both an
upper- and lowercase first letter. 
"""


def und_case(s):
    print(s)
    


# Add two camel case test cases below, one string starting with a
# capital letter and another starting with a lowercase letter.


print('\n*** Problem 5 ***')           # 16 points (4 per bug)

# Debug the code in char_ratios() until it works as intended.
# Find and fix all four bugs.

# char_ratios should print out the percentage of a string's characters
# that are vowels, the percentage that are consonants, and the per-
# centage that are neither, rounded to the nearest tenth of a percent.
def char_ratios(s):
    s_length = len(s)
    vowel_count = 0
    cons_count = 0
    other_count = 0
    for ch in s.lower():
        if ch in 'aeiou':
            vowel_count + 1
        elif ch in 'bcdfghjklmnpqrstvwxyz':
            cons_count + 1
        else:
            other_count + 1
    v_percent = round(vowel_count / s_length, 1)
    c_percent = round(cons_count / s_length, 1)
    o_percent = round(other_count / s_length, 1)
    print('The string "' + s + '" is roughly', v_percent, '% vowels,',
          c_percent, '% consonants, and',
          o_percent, '% non-letter characters.')

# Test cases are provided:
char_ratios('The Warriors are inevitable.')
char_ratios('Beware! The roads are icy this time of year.')
char_ratios('The quick brown fox jumps over the lazy dog.')



print('\n*** Problem 6 ***')           # 18 points (9 per comment)

# Study and test the following functions to figure out how they work.
# Add a comment above each function to explain what each does and how
# it works.

# This function basically allows any character in a string that is from 0 to 9 and returns False if not
def can_int_str(s):
    for ch in s:
        if ch in '0123456789':
            continue
        else:
            return False
    return True

# This function prints the string if it consists of the integers in the frist function
def make_int(s):
    if can_int_str(s):
        return int(s)
    else:
        return False       

# Test cases are provided:
print('can_int_str(\'12334325f\'):', can_int_str('12334325f'))
print('can_int_str(\'12334325\'):', can_int_str('12334325'))
print('make_int(\'12334325f\'):', make_int('12334325f'))
print('make_int(\'12334325\'):', make_int('12334325'))
