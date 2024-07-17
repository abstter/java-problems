"""
Worksheet #8: String Slicing, Searching, and Counting
Student Code
Python Level 2
"""

""" Problem 1 """

orig_str = 'The King\'s actions quelled the rebellion.'

print('_Problem 1_\n')

def change_char(s, i, new_char):
    global new_string
    new_string = ' '
    new_string = s[:i] + new_char + s[i+1:]
    return new_string

word0 = 'luck'
word1 = change_char(word0, 2, 'r')
word2 = change_char(word1, 0, 'm')
word3 = change_char(word2, 1, 'a')
word4 = change_char(word3, 3, 'e')
word5 = change_char(word4, 2, 'n')
#print('Printing word0 through word5, after 5 consecutive calls to')
#print('change_char():')
print(word0, word1, word2, word3, word4, word5)



""" Problem 2 """


print('\n_Problem 2_\n')

def change_slice(s, b, e, new_slice):
    global new
    new = s[:b] + new_slice + s[e:]
    return new
    
string0 = 'neural elasticity'
print('string0 =', string0)
print("Running string1 = change_slice(string0, 4, 8, 'op')...")
string1 = change_slice(string0, 4, 8, 'op')
print('string1 =', string1)

print('\nAnother example of change_slice():\n')
orig_str = 'The King\'s actions fuelled the rebellion.'
print('Original string:', orig_str)
print("Running: new_str = change_slice(orig_str, -8, -4, 'volut')...")
new_str = change_slice(orig_str, -8, -4, 'volut')
print('New string:', new_str)


""" Problem 3 """

def find(word, letter, starting_index):
    index = starting_index
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print('\n_Problem 3_\n')

book_title = 'The Lion, the Witch, and the Wardrobe'
print("book_title is 'The Lion, the Witch, and the Wardrobe'")
print("Running index_of_e = find(book_title, 'e', 6)...")
index_of_e = find(book_title, 'e', 6)
print("index_of_e =", index_of_e)


""" Problem 4 """

def count_char(string, char):
    count = 0
    for char in string:
        if char == 'a':
            count = count + 1
        print(count)

print('\n_Problem 4_\n')
count_char('banana', 'a')
W
# Output Files
'''
_Problem 1_

luck lurk murk mark mare mane

_Problem 2_

string0 = neural elasticity
Running string1 = change_slice(string0, 4, 8, 'op')...
string1 = neuroplasticity

Another example of change_slice():

Original string: The King's actions fuelled the rebellion.
Running: new_str = change_slice(orig_str, -8, -4, 'volut')...
New string: The King's actions fuelled the revolution.

_Problem 3_

book_title is 'The Lion, the Witch, and the Wardrobe'
Running index_of_e = find(book_title, 'e', 6)...
index_of_e = 12

_Problem 4_

0
1
1
2
2
3
'''
