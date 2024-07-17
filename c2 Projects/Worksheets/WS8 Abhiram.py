# WS 8 Abhiram Avasarala
# Problem Number 1
# I chose a dictionary as they are mutable and easy to change
print('Question 1')
animals = {'Cat': 1, 'Cheetah' : 2, 'Tiger' : 3}
del animals['Tiger']
animal = {'Eagle' : 3}
animals.update(animal)
print(animals)
# Problem Number 2
print('Question 2')
first, second, third = animals.values()
print(first, second, third)
# Problem Number 3
# I chose a list as they are useful for storing tabular data
print('Question 3')
chess = [0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0]
print(chess)

# Problem Number 4
# I chose a tuple as they are useful in collections of elements and data is not changed
print('Question 4')
pos = (6, 5)
print(pos)

# Problem Number 5
print('Question 5')
text = "cat dog cat bird dog cat bird bird"
words = text.split()
word_count = {}

for word in words:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1
print("Word count:", word_count)

# Problem Number 6
print('Question 6')
matrix = [
        [0, 7, 0, 0, 0],
        [0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
        ]
sparse_matrix = { (0, 1): 7, (2, 3): 6, (4, 0): 8 }
print(sparse_matrix)

# Problem Number 7
print('Question 7')
nba_players = {
    ('Curry', 'Stephen') : {'team':'Warriors', 'rings':4},
    ('Thompson', 'Klay') : {'team':'Warriors', 'rings':4},
    ('Brooks', 'Dillon') : {'team':'Rockets', 'rings':0}
    }
nba_players[('Lebron', 'James')] = {'team' : 'Lakers', 'rings':4}
for player in nba_players:
    print(player, nba_players[player])
# Problem Number 8
print('Question 8')
movies = {'Spiderman No-Way Home' : 7.9, 'Encanto' : 8.1, 'Jumanji' : 10}
print('Adding movie')
movies['Blue Beetle']= 10
for movie in movies:
    print(movie, movies[movie])
print('Changing movie')
movies['Blue Beetle'] = 5
print(movies)
print('Removing movie')
del movies['Encanto']
print(movies)





