# Abhiram Avasarala C5 WS 6
import random
def num_guess():
    num = random.randint(1, 50)
    chance = 3
    while chance <= 3:
        print("Guess a number between 1 and 50! You have ", chance,"tries!")
        chance = chance - 1
        guess = input()
        i = int(guess)
        if i < 1 or i > 50:
            print("Sorry, that is an invalid guess. It has to be between 1 and 50.")
            continue
        if i == num:
            print("You guessed right!")
            break
        elif i < num:
            print("Try higher!")
        elif i > num:
            print("Try lower!")
        if (chance <= 0):
            print("Uh oh! You are out of tries! The number was",num,"!")
            break
num_guess()