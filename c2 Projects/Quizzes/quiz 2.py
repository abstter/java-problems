"""
Quiz # 2: Data Structures
Student Code
Python Level 3

Fill out your name and section below.

Name:
Section:
"""

# Uncomment any provided print statements or function calls as needed
# to verify results.


print("\n*** Problem 1 ***")    # 10 points
planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
print(planets)
# Create a tuple called planets that contains the following planets:
# 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'
# (Copy-paste the planet names above to save time.) Print the tuple.


print("\n*** Problem 2 ***")    # 10 points
gas_giants = planets[4:6]
# Write code to get a slice of the elements including only Jupiter and Saturn
# and assign it into the variable gas_giants.

print(gas_giants)


print("\n*** Problem 3 ***")    # 10 points
landmark_coordinates = (3, 4), (6, 1), (2, 7)

# You are given the coordinates of three landmarks on a map as tuples
# representing (x, y) coordinates: (3, 4), (6, 1), and (2, 7). Create a tuple
# called landmark_coordinates to store these coordinates.

print(landmark_coordinates)


print("\n*** Problem 4 ***")    # 15 points
# You have been provided with the tuple book_data which contains information
# about a book in the following order:
#
#     'Title', 'Author', 'Publication Year', 'Genre'
#
# Unpack book_data into individual variables and print out the information 
# in an informative message of the form
#
#      The Hobbit was written by J.R.R. Tolkien and published in 1937.

book_data = ('The Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasy')
x, y, z = 'The Hobbit', 'J.R.R. Tolkien', 1937
print(f"{x} was written by {y} and published in {z}.")

print("\n*** Problem 5 ***")    # 15 points
country_capitals = {
"USA": "Washington, D.C",
"Japan": "Tokyo",
"Philippines": "Manila",
}
for key, value in country_capitals.items():
    print(key, value)
# Create a dictionary named country_capitals with countries as keys and 
# their capitals as values. Include entries for the USA (Washington, D.C.),
# Japan (Tokyo) and the Philippines (Manila). Using the items() method,  
# print each country and capital (key-value pair) on its own line.


print("\n*** Problem 6 ***")    # 15 points       
# Write a function get_capital() to accept a country parameter and return the
# capital if the country is in the country_capitals dictionary. Otherwise, 
# print "not found in the data set". Test your function with the countries
# and print the results in an informative message in the following format:
#
#     Morocco: The capital is not found in the data set.
#     Philippines: The capital is Manila.

test_country_1 = "Morocco"
test_country_2 = "Philippines"

def get_capital(country):
    capital = country_capitals.get(country, "not found in the data set")
    print(f"The capital is {capital}.")
get_capital(test_country_1)
get_capital(test_country_2) 


print("\n*** Problem 7 ***")    # 15 points
# Write a function remove_country() that accepts a country as parameter and
# checks if it is present in the dictionary.
# > If so, it should remove its entry and print the entry being removed with
#   a helpful message such as "Removing Greenland, Nuuk from data set."
# > If not, print a message such as "Iceland not found in data set."

# Test the function with the following countries:

def remove_country(country):
    capital = country_capitals.pop(country, "not found in data set.")
    print(f"Removing {capital} from data set.")
test_country_3 = "Iceland"
test_country_4 = "Greenland"

remove_country(test_country_3)
remove_country(test_country_4)




print("\n*** Problem 8 ***")    # 10 points

# The following code is intended to create a dictionary of city temperatures
# (in Celsius) and convert them to Fahrenheit. However, there is an error
# in the code. Your task is to debug the code. Briefly explain the bug with
# a comment and then fix it.

# Hint: The problem isn't with the math. What tool have you learned about that
# allows you to access a dictionary's key-value pairs?

city_temperatures_C = {'New York': 22, 'London': 18, 'Tokyo': 26, 'Delhi': 34}

city_temperatures_F = {}
# items method would iterate over the key value pair
for city, temperature in city_temperatures_C.items():
    city_temperatures_F[city] = (temperature * 9 / 5) + 32

'''
Output:

*** Problem 1 ***
('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')

*** Problem 2 ***
('Jupiter', 'Saturn')

*** Problem 3 ***
((3, 4), (6, 1), (2, 7))

*** Problem 4 ***
The Hobbit was written by J.R.R. Tolkien and published in 1937.

*** Problem 5 ***
USA Washington, D.C
Japan Tokyo
Philippines Manila

*** Problem 6 ***
The capital is not found in the data set.
The capital is Manila.

*** Problem 7 ***
Removing not found in data set. from data set.
Removing not found in data set. from data set.

*** Problem 8 ***
'''