"""
Abhiram Avasarala
Computer Fair Project
"""
import time
def welcome():
    print("Lights......")
    time.sleep(1)
    print("Camera.......")
    time.sleep(1)
    print("Action!")
    time.sleep(1)
    print("Welcome to the Arcade of Madness, presented by the Master of Fun.....Abhiram!!!!")
    time.sleep(1)
    print("Today, I'll be taking you through a series of mind-twisting and fun games so hold on tight and enjoy!!")
    time.sleep(2)
    print("____________________________________________________")
    print("The games available to play are: Crazy Libs, Soccer Simulator, Hangman and Tic-Tac-Toe!")
    time.sleep(1)
    
def games():
    choices = input("Enter one of the games you would like to play: ")
    if choices == "Crazy Libs" or choices == "crazy libs":
        import Abhiramlib
    else:
        print("I did not understand your message. Please enter a more understandable choice.")
        input("Enter one of the choices: ")

welcome()
games()