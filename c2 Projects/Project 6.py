# Abhiram Avasarala Project 6 Phase 1
ttt_board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ',]]

def print_board(bd):# This function makes the board
    print("   a     b     c   ")  
    print("      |     |")
    print("1  "+bd[0][0]+"  |  "+bd[0][1]+"  |  "+bd[0][2])
    print(" _____|_____|_____")
    print("      |     |        ")
    print("2  "+bd[1][0]+"  |  "+bd[1][1]+"  |  "+bd[1][2])
    print(" _____|_____|_____")
    print("      |     |        ")
    print("3  "+bd[2][0]+"  |  "+bd[2][1]+"  |  "+bd[2][2])     
    print("      |     |")
    
def check_win(bd, ch):# This function checks if you win or the AI wins
    if ch == bd[0][0]==bd[0][1]==bd[0][2]:
        return True
    elif ch==bd[1][2]==bd[1][1]==bd==[1][2]:
        return True
    elif ch==bd[2][2]==bd[2][1]==bd[2][0]:
        return True
    elif ch==bd[0][0]==bd[1][0]==bd==[2][0]:
        return True
    elif ch==bd[0][1]==bd[1][1]==bd==[2][1]:
        return True
    elif ch==bd[0][2]==bd[1][2]==bd[2][2]:
       return True
    elif ch==bd[0][0]==bd[1][1]==bd==[2][2]:
        return True
    elif ch==bd[0][2]==bd[1][1]==bd==[2][0]:
        return True
    


def check_draw(bd):# This function checks if it is a draw
    for i in range(3):
        for j in range(3):
            if bd[i][j] == ' ':
                return False
    return True

'''
Output

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
Enter the location of your move (e.g., B3): c2

 You have made your move: 

   a     b     c   
      |     |
1     |     |   
 _____|_____|_____
      |     |        
2     |     |  X
 _____|_____|_____
      |     |        
3     |     |   
      |     |


 Please wait while the AI calculates its move...


 The AI has made its move: 

   a     b     c   
      |     |
1  O  |     |   
 _____|_____|_____
      |     |        
2     |     |  X
 _____|_____|_____
      |     |        
3     |     |   
      |     |

Enter the location of your move (e.g., B3): b1

 You have made your move: 

   a     b     c   
      |     |
1  O  |  X  |   
 _____|_____|_____
      |     |        
2     |     |  X
 _____|_____|_____
      |     |        
3     |     |   
      |     |


 Please wait while the AI calculates its move...


 The AI has made its move: 

   a     b     c   
      |     |
1  O  |  X  |   
 _____|_____|_____
      |     |        
2  O  |     |  X
 _____|_____|_____
      |     |        
3     |     |   
      |     |

Enter the location of your move (e.g., B3): a3

 You have made your move: 

   a     b     c   
      |     |
1  O  |  X  |   
 _____|_____|_____
      |     |        
2  O  |     |  X
 _____|_____|_____
      |     |        
3  X  |     |   
      |     |


 Please wait while the AI calculates its move...


 The AI has made its move: 

   a     b     c   
      |     |
1  O  |  X  |   
 _____|_____|_____
      |     |        
2  O  |     |  X
 _____|_____|_____
      |     |        
3  X  |  O  |   
      |     |

Enter the location of your move (e.g., B3): b2

 You have made your move: 

   a     b     c   
      |     |
1  O  |  X  |   
 _____|_____|_____
      |     |        
2  O  |  X  |  X
 _____|_____|_____
      |     |        
3  X  |  O  |   
      |     |


 Please wait while the AI calculates its move...


 The AI has made its move: 

   a     b     c   
      |     |
1  O  |  X  |  O
 _____|_____|_____
      |     |        
2  O  |  X  |  X
 _____|_____|_____
      |     |        
3  X  |  O  |   
      |     |

Enter the location of your move (e.g., B3): c3

 You have made your move: 

   a     b     c   
      |     |
1  O  |  X  |  O
 _____|_____|_____
      |     |        
2  O  |  X  |  X
 _____|_____|_____
      |     |        
3  X  |  O  |  X
      |     |


It's a draw!! Game over.
'''
