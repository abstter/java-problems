"""
Abhiram Avasarala
Computer Fair Project
"""
import time
import random
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
    
def games():
    print("The games available to play are: Crazy Libs, Soccer Simulator, Rock Paper Scissors, and Tic-Tac-Toe!")
    time.sleep(1)
    choices = input("Enter one of the games you would like to play: ")
    # Crazy Libs
    if choices == "Crazy Libs" or choices == "crazy libs":
        time.sleep(2)
        print("___________________________________________")
        import Abhiramlib
        continue1 = input("Press y if you would like to play again or press q to exit: ")
        if continue1 == "y":
            games()
        else:
            exit()
    # Soccer Simulator
    elif choices == "Tic Tac Toe" or choices == "Tic-Tac-Toe" or choices == "tic tac toe" or choices == "tic-tac-toe":
        time.sleep(1)
        print("________________________________________________")
        time.sleep(1)
        import tic_tac_toe_p6
        continue1 = input("Press y if you would like to play again or press q to exit: ")
        if continue1 == "y":
            games()
        else:
            exit()
    # Rock Paper Scissors
    elif choices == "rock paper scissors" or choices == "Rock Paper Scissors":
        print("Welcome to rock paper scissors!")
        time.sleep(1)
        print("Let's begin, shall we?")
        time.sleep(1)
        rps = ["bob", "mr. beast", "gorilla", "blob", "gecko", "Hulk"]
        choice = random.choice(rps)
        print("Selecting an opponent for you....")
        time.sleep(2)
        print("Your opponent will be......")
        time.sleep(1)
        print("..",choice,"!!!!")
        choice1 = input("Enter rock, paper, or scissors:")
        options = ["rock", "paper", "scissors"]
        two = random.choice(options)

        if choice1 == "rock" and two == "rock":
            print("Your opponent selected rock!")
            continue1 = input("It's a tie!! Press y if you would like to play again or press q to exit: ")
            if continue1 == "y":
                games()
            else:
                exit()
        if choice1 == "paper" and two == "rock":
            print("Your opponent selected rock!")
            continue1 = input("You win!! Press y if you would like to play again or press q to exit: ")
            if continue1 == "y":
                games()
            else:
                exit()
        if choice1 == "scissors" and two == "rock":
            print("Your opponent selected rock!")
            continue1 = input("You lose!! Press y if you would like to play again or press q to exit: ")
            if continue1 == "y":
                games()
            else:
                exit()
        if choice1 == "paper" and two == "scissors":
            print("Your opponent selected scissors!")
            continue1 = input("You lose!! Press y if you would like to play again or press q to exit: ")
            if continue1 == "y":
                games()
            else:
                exit()
        if choice1 == "rock" and two == "scissors":
            print("Your opponent selected scissors!")
            continue1 = input("You win!! Press y if you would like to play again or press q to exit: ")
            if continue1 == "y":
                games()
            else:
                exit()
        if choice1 == "paper" and two == "paper":
            print("Your opponent selected paper!")
            continue1 = input("It's a tie!! Press y if you would like to play again or press q to exit: ")
            if continue1 == "y":
                games()
            else:
                exit()
        if choice1 == "scissors" and two == "scissors":
            print("Your opponent selected scissors!")
            continue1 = input("It's a tie!! Press y if you would like to play again or press q to exit: ")
            if continue1 == "y":
                games()
            else:
                exit()
        if choice1 == "rock" and two == "paper":
            print("Your opponent selected paper!")
            continue1 = input("You lose!! Press y if you would like to play again or press q to exit: ")
            if continue1 == "y":
                games()
            else:
                exit()
        if choice1 == "scissors" and two == "paper":
            print("Your opponent selected paper!")
            continue1 = input("You win!! Press y if you would like to play again or press q to exit: ")
            if continue1 == "y":
                games()
            else:
                exit()
    elif choices == "Soccer Simulator" or choices == "soccer simulator" or choices == "Soccer simulator":
        time.sleep(2)
        print("_________________________________________")
        import soccer_sim
        continue1 = input("You win!! Press y if you would like to play again or press any other letter to exit: ")
        if continue1 == "y":
            games()
        else:
            exit()
    else:
        print("I did not understand your message. Please enter a more understandable choice.")
        games()
    
    

welcome()
games()

# Output
"""
Lights......
Camera.......
Action!
Welcome to the Arcade of Madness, presented by the Master of Fun.....Abhiram!!!!
Today, I'll be taking you through a series of mind-twisting and fun games so hold on tight and enjoy!!
The games available to play are: Crazy Libs, Soccer Simulator, Rock Paper Scissors, and Tic-Tac-Toe!
Enter one of the games you would like to play: Tic Tac Toe
________________________________________________
Welcome to the Tic Tac Toe game.
The AI has the character O. You have the character X.
You go first. Good luck!

   a     b     c   
      |     |
1     |     |   
 _____|_____|_____
      |     |        
2     |     |   
 _____|_____|_____
      |     |        
3     |     |   
      |     |
Enter the location of your move (e.g., B3): b2

 You have made your move: 

   a     b     c   
      |     |
1     |     |   
 _____|_____|_____
      |     |        
2     |  X  |   
 _____|_____|_____
      |     |        
3     |     |   
      |     |


 Please wait while the AI calculates its move...


 The AI has made its move: 

   a     b     c   
      |     |
1     |     |  O
 _____|_____|_____
      |     |        
2     |  X  |   
 _____|_____|_____
      |     |        
3     |     |   
      |     |

Enter the location of your move (e.g., B3): a1

 You have made your move: 

   a     b     c   
      |     |
1  X  |     |  O
 _____|_____|_____
      |     |        
2     |  X  |   
 _____|_____|_____
      |     |        
3     |     |   
      |     |


 Please wait while the AI calculates its move...


 The AI has made its move: 

   a     b     c   
      |     |
1  X  |     |  O
 _____|_____|_____
      |     |        
2     |  X  |   
 _____|_____|_____
      |     |        
3     |     |  O
      |     |

Enter the location of your move (e.g., B3): a2

 You have made your move: 

   a     b     c   
      |     |
1  X  |     |  O
 _____|_____|_____
      |     |        
2  X  |  X  |   
 _____|_____|_____
      |     |        
3     |     |  O
      |     |


 Please wait while the AI calculates its move...


 The AI has made its move: 

   a     b     c   
      |     |
1  X  |     |  O
 _____|_____|_____
      |     |        
2  X  |  X  |  O
 _____|_____|_____
      |     |        
3     |     |  O
      |     |


The AI has won!! You have lost!! Game Over.
Press y if you would like to play again or press q to exit: q
"""