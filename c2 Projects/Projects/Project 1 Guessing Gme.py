# This code will run a guessing game with a target and a bomb
import random


import time

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    time.sleep(1)
    print("A number has been selected between 1 and 100")
    time.sleep(1)
    print("You have 10 attempts to guess the number.")
    print("Try to guess the number but beware the bomb.")
    print(target)
    print(bomb)
# These are the variables to hold target, bomb, losses, wins, attempts, and games
target = random.randrange(1, 100)
bomb = random.randrange(1, 100)
losses = 0
wins = 0
attempts = 10
games = 0
global user_guess



# This function will show how close or far the target is
def target_close():
    global user_guess, attempts, wins, losses
    if target - user_guess <= 5:
        print("Your guess is very close(5 or less) to the target.")
    elif target - user_guess >= 11 and target - user_guess <= 31:
        print("Your guess is somewhat close (11 to 30 away) to the target.")
    elif target - user_guess >= 31 and target - user_guess <= 51:
        print("Your guess is neither close nor far (31 to 51 away) to the target.")
    elif target - user_guess >= 51 and target - user_guess <= 71:
        print("Your guess is far (51 to 71 away) to the target.")
    elif target - user_guess >= 71:
        print("Your guess is very far (71 or more) to the target.")

# This function will show how close or far the bomb is
def bomb_close():
    global user_guess, attempts, wins, losses
    if bomb - user_guess <= 5:
        print("Your guess is very close(5 or less) to the bomb.")
    elif bomb - user_guess >= 11 and bomb- user_guess <= 31:
        print("Your guess is somewhat close (11 to 30 away) to the bomb.")
    elif bomb - user_guess >= 31 and bomb - user_guess <= 51:
        print("Your guess is neither close nor far (31 to 51 away) to the bomb.")
    elif bomb - user_guess >= 51 and bomb - user_guess <= 71:
        print("Your guess is far (51 to 71 away) to the bomb.")
    elif bomb - user_guess >= 71:
        print("Your guess is very far (71 or more) to the bomb.")
# This function shows whether there is a win or loss
def win_loss():
    global user_guess, attempts, wins, losses, games
    if user_guess == target:
        print("Congratulations! You have guessed the target.")
        print(f"Target was {target}.")
        print(f"Bomb was {bomb}.")
        wins += 1
        games += 1
        game = input("Do you want to play again? (y/n)")
        attempts = 0
        if game == 'n':
            exit()
        elif game == 'y':
            guesses1()
    elif user_guess == bomb:
        print("Oh no! You have guessed the bomb.")
        print(f"Target was {target}.")
        print(f"Bomb was {bomb}.")
        games += 1
        losses += 1
        attemps = 0
        if game == 'n':
            exit()
        elif game == 'y':
            guesses1()
    elif attempts == 0:
        print("Oh no! You have run out of attempts.")
        print(f"Target was {target}.")
        print(f"Bomb was {bomb}.")
        guesses = 0
        games += 1
        losses += 1
# This is the input function  
def guesses():
    global user_guess, attempts, wins, losses
    user_guess = int(input("Enter your guess. \n"))

def guesses1():
    global user_guess, attempts, wins, losses
    guessing_game()
    while attempts > 0:
        attempts = attempts - 1
        print('You have ',attempts+1,'guesses left.')
        guesses()
        target_close()
        bomb_close()
        win_loss()
guesses1()
# This function is the scorecard for the game
def scorecard():
    global games, losses, wins
    print("Games: ", games)
    print("Losses: ", losses)
    print("Wins: ", wins)

scorecard()
 
# Output File
'''
1)Welcome to the Number Guessing Game!
A number has been selected between 1 and 100
You have 10 attempts to guess the number.
Try to guess the number but beware the bomb.
You have  10 guesses left.
Enter your guess. 
45
Your guess is somewhat close (11 to 30 away) to the target.
Your guess is neither close nor far (31 to 51 away) to the bomb.
You have  9 guesses left.
Enter your guess. 
55
Your guess is somewhat close (11 to 30 away) to the target.
Your guess is somewhat close (11 to 30 away) to the bomb.
You have  8 guesses left.
Enter your guess. 
44
Your guess is somewhat close (11 to 30 away) to the target.
Your guess is neither close nor far (31 to 51 away) to the bomb.
You have  7 guesses left.
Enter your guess. 
88
Your guess is very close(5 or less) to the target.
Your guess is very close(5 or less) to the bomb.
You have  6 guesses left.
Enter your guess. 
89
Your guess is very close(5 or less) to the target.
Your guess is very close(5 or less) to the bomb.
You have  5 guesses left.
Enter your guess. 
90
Your guess is very close(5 or less) to the target.
Your guess is very close(5 or less) to the bomb.
You have  4 guesses left.
Enter your guess. 
91
Your guess is very close(5 or less) to the target.
Your guess is very close(5 or less) to the bomb.
You have  3 guesses left.
Enter your guess. 
92
Your guess is very close(5 or less) to the target.
Your guess is very close(5 or less) to the bomb.
You have  2 guesses left.
Enter your guess. 
93
Your guess is very close(5 or less) to the target.
Your guess is very close(5 or less) to the bomb.
You have  1 guesses left.
Enter your guess. 
87
Your guess is very close(5 or less) to the target.
Your guess is very close(5 or less) to the bomb.
Oh no! You have run out of attempts.
Target was 73.
Bomb was 80.
Games:  1
Losses:  1
Wins:  0

2)Welcome to the Number Guessing Game!
A number has been selected between 1 and 100
You have 10 attempts to guess the number.
Try to guess the number but beware the bomb.
88
You have  10 guesses left.
Enter your guess. 
88
Your guess is very close(5 or less) to the target.
Your guess is very close(5 or less) to the bomb.
Congratulations! You have guessed the target.
Target was 88.
Bomb was 13.
Do you want to play again? (y/n)y
'''
    

        
        
        
