# Abhiram Avasarala C5
import random
people = ["elon musk", "tom brady", "lionel messi", "cristiano ronaldo", "mr beast", "stephen curry", "anthony davis", "justin jefferson", "kyle walker", "kevin deBruyne"]
sports = ["football", "soccer", "bowling", "basketball", "tennis", "track and field", "swimming", "handball", "volleyball", "raquetball"]

def intro():
    print('''___________________________________________________________________________ 

Welcome to the Dadman Game!

This game is similar to hangman but without all the
gratuitous hanging. Instead, you are in an even scarier
situation. You did Something Very Bad and have been sent
to your room. Your dad is slowly making his way up the
stairs to give you a Talk. You are trying to come up with
a good explanation for why you did the thing you did
before your dad makes it to the top of the stairs.

Because this is a game, the only way to come up with such
an excuse is to first solve a word puzzle, and quickly.
Solve away...
___________________________________________________________________________''')
    
intro()

def game():
    print("Please select one of the following puzzle categories: ")
    print("\n")
    game = input("Please select one of the following puzzle categories:\n 1.Famous People \n 2.Sports\n")
    if game == "1." or game == "1" or game == "Famous People" or game == "famous people":
        thing = random.choice(people)
    elif game == "2." or game == "2" or game == "sports" or game == "Sports":
        thing = random.choice(sports)
    else:
        print("That is not a valid option. Please enter another one.")
        game()
        
    user = ' '
    for i in range(len(thing)):
        user += ' _'
    print(user)
    guesses = 6
    
    while guesses > 0:
        z = input("Guess a letter: ")
        z = z.lower()
        if z not in thing:
            guesses = guesses-1
        for i in range(len(thing)-1):
            if thing[i] == z:
                ind = i
                user = user[:ind]+z+user[ind+1:]
                print(user)
        print("Lives left: " + str(guesses))
    print(user)
    print("You have finished the game!!!")
        
game()        
    
# Output
'''___________________________________________________________________________ 

Welcome to the Dadman Game!

This game is similar to hangman but without all the
gratuitous hanging. Instead, you are in an even scarier
situation. You did Something Very Bad and have been sent
to your room. Your dad is slowly making his way up the
stairs to give you a Talk. You are trying to come up with
a good explanation for why you did the thing you did
before your dad makes it to the top of the stairs.

Because this is a game, the only way to come up with such
an excuse is to first solve a word puzzle, and quickly.
Solve away...
___________________________________________________________________________
Please select one of the following puzzle categories:
 1.Famous People 
 2.Sports
1
  _ _ _ _ _ _ _ _
Guess a letter: a
  _ _a_ _ _ _ _ _
Lives left: 6
Guess a letter: b
  _b_a_ _ _ _ _ _
Lives left: 6
Guess a letter: n
Lives left: 5
Guess a letter: m
m _b_a_ _ _ _ _ _
Lives left: 5
Guess a letter: p
Lives left: 4
Guess a letter: e
m _bea_ _ _ _ _ _
Lives left: 4
Guess a letter: s
m _beas _ _ _ _ _
Lives left: 4
Guess a letter: i
Lives left: 3
Guess a letter: o
Lives left: 2
Guess a letter: p
Lives left: 1
Guess a letter: z
Lives left: 0
m _beas _ _ _ _ _
You have finished the game!!!
'''


