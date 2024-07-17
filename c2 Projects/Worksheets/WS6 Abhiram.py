"""
Worksheet # 6: Dictionaries
Student Code
Python Level 3

Name:
Section:
"""

# Uncomment any provided print statements as needed to verify results.


print('\n *** Problem 1 - Creating and Accessing Dictionaries *** ')

# 1a. Create an empty dictionary named book_record and print it.

print('\n(1-a)')
book_record = {}
print(book_record)
# 1b. Now add the following title and author to the book_record dictionary:
#     'Title': 'To Kill a Mockingbird', 'Author': 'Harper Lee'.
#     Print the book_record dictionary.

print('\n(1-b)')
book_record['Title'] = 'To Kill a Mockingbird'
book_record['Author'] = 'Harper Lee'
print(book_record)
# 1c. Create a dictionary named class_students with the following keys and
#     values: 'John': 12, 'Emily': 13, 'Alex': 14.

print('\n(1-c)')
class_students = { 'John': 12,
                   'Emily': 13,
                   'Alex': 14,
                   }
print(class_students)  # Output: {'John': 12, 'Emily': 13, 'Alex': 14}


print('\n *** Problem 2 - Dictionary Methods *** ')

# 2a. Use the get() method to retrieve the age of 'Daniel' from the
#     class_students dictionary. If 'Daniel' is not present, it should return
#     'Student not found.'
print('\n(2-a)')
age = dict(Tom=5, Bob=23, Ross=100)
age = age.get("Daniel", "Student not found")
print(age)  # Output: 'Student not found.'


# 2b. Remove 'Emily' from the class_students dictionary using the pop() method.
#     Print the returned value and the updated dictionary.

print('\n(2-b)')
Emily_student = class_students.pop("Emily")
print(Emily_student)
print(class_students) 

# 2c. Create another dictionary named new_students with the following keys and
#     values: 'Michael': 14, 'Sarah': 13. Print it.

print('\n(2-c)')
new_students = dict(Michael=14, Sarah=13)
print(new_students)
# 2d. Merge new_students into the class_students dictionary using the update()
#     method and print both new_students and the updated class_students.

print('\n(2-d)')
class_students.update(new_students)
print(new_students)
print(class_students)

# 2e. Clear all entries in the class_students dictionary using the clear()
#     method and print the updated dictionary.

print('\n(2-e)')
new_students.clear()
print(new_students)

print('\n *** Problem 3 - Dictionary View Objects *** ')

# You are given the following dictionary:
fruit_colors = {'Apple': 'Red', 'Banana': 'Yellow', 'Grapes': 'Purple'}

# 3a. Get a view object of all keys in fruit_colors and print it.

print('\n(3-a)')
keys1 = fruit_colors.keys()
print(keys1)
# 3b. Get a view object of all values in fruit_colors and print it.

print('\n(3-b)')
values1 = fruit_colors.values()
print(values1)

# 3c. Get a view object of all items (key-value pairs) in fruit_colors and
#     print it.

print('\n(3-c)')
items1 = fruit_colors.items()
print(items1)

# 3d. Add a new key-value pair 'Orange': 'Orange' to fruit_colors and print
#     the updated view objects of keys, values, and items.

print('\n(3-d)')
fruit_colors['Orange'] = 'Orange'
print(keys1)
print(values1)
print(items1)
# 3e. Check if 'Apple' is in the keys of fruit_colors using a view object.

print('\n(3-e)')
if "Apple" in keys1:
    print("Apple is in key of fruit_colors")
else:
    print("Apple is not there")

# 3f. Check if 'Green' is in the values of fruit_colors using a view object.

print('\n(3-f)')
if "Green" in values1:
    print("Green is in key of fruit_colors")
else:
    print("Green is not there.")

# 3g. Check if the key-value pair ('Banana', 'Yellow') is present in
#     fruit_colors using a view object.

print('\n(3-g)')
if ('Banana','Yellow') in items1:
    print("It is in key of fruit_colors")
else:
    print("Nothing there.")

"""
Challenge Problem
"""

print('\n *** Problem 4 - Dictionary View Objects *** ')

# 4a. Convert the view object of keys in fruit_colors to a list and remove
#     'Apple' from the list. Print the updated list and also check if 'Apple'
#     still exists in the fruit_colors dictionary.

print('\n(4-a)')
keys = list(fruit_colors.keys())
keys.pop(keys.index('Apple'))
print(keys)
print(fruit_colors.keys())
# 4b. Create a function that takes a dictionary and a color as arguments. This
#     function should return all fruits (keys) that have this color, utilizing
#     a view object of the dictionary.

print('\n(4-b)')


#print(get_fruits_of_color(fruit_colors, 'Red'))  # Output: ['Apple']