"""
Worksheet #8: String Slicing, Searching, and Counting
Student Code
Python Level 2
"""

""" Problem 1 """
orig_str = 'The King\'s actions quelled the rebellion.'
def change_char(s, i, new_char):
   string1 = s[:i - 1]
   string2 = s[i:]
   return   
   
   
    

print('_Problem 1_\n')

'''
word0 = 'luck'
word1 = change_char(word0, 2, 'r')
word2 = change_char(word1, 0, 'm')
word3 = change_char(word2, 1, 'a')
word4 = change_char(word3, 3, 'e')
word5 = change_char(word4, 2, 'n')
print('Printing word0 through word5, after 5 consecutive calls to')
print('change_char():')
print(word0, word1, word2, word3, word4, word5)

print('\nAnother example of change_char():\n')
print('Original string:', orig_str)
print('Running: new_str = change_char(orig_str, 19, \'f\')...')
new_str = change_char(orig_str, 19, 'f')
print('New string:', new_str)
'''

""" Problem 2 """
def change_slice(s, b, e, new_slice):
    s1 = s[:b]
    s2 = s[e:]
    return s1 + new_slice + s2

print('\n_Problem 2_\n')


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

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print('\n_Problem 3_\n')
'''
book_title = 'The Lion, the Witch, and the Wardrobe'
print("book_title is 'The Lion, the Witch, and the Wardrobe'")
print("Running index_of_e = find(book_title, 'e', 6)...")
index_of_e = find(book_title, 'e', 6)
print("index_of_e =", index_of_e)
'''

""" Problem 4 """

string = 'banana'
count = 0
for char in string:
    if char == 'a':
        count = count + 1
    print(count)

print('\n_Problem 4_\n')
'''
print("book_title is 'The Lion, the Witch, and the Wardrobe'")
print("Running e_count = count_char(book_title, 'e')")
e_count = count_char(book_title, 'e')
print("e_count =", e_count)
'''

""" Problem 5 """


print('\n_Problem 5_\n')
'''
word = 'SuperCaliFragilisticExpialidocious'
print("word is 'SuperCaliFragilisticExpialidocious'\n")
print("Calling find_letters(word)...\n")
find_letters(word)
'''

""" Problem 6 """

print('\n_Problem 6_\n')
'''
print("Calling: alphabetize('bear', 'snake')...")
alphabetize('bear', 'snake')
print("\nCalling: alphabetize('hello', 'goodbye')...")
alphabetize('hello', 'goodbye')
print("\nCalling: alphabetize('autonomous', 'autonomic')...")
alphabetize('autonomous', 'autonomic')
'''