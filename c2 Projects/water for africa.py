def introduction():
    print('''Fleet Battle is a two-player game where each player tries to sink
all the ships in the other player's fleets by taking virtual "shots"
at the other player's game grid. Each player's game grid contains
his fleet in a secret arrangement that he determines prior to the
start of the game.

Each player must guess and can also use logic to infer the most likely
locations of ships on his opponent's grid. This becomes clearer as

Rules:
1. Each player places six ships of various lengths in a secret
   arrangement on an 8x8 grid.
2. Each player takes turns firing shots at the other player's game
   grid to try to strike his ships.
3. When a shot strikes a space occupied by a ship, the attacking
   player is told that he struck a ship but not which ship he struck.
4. Once every space occupied by a ship has been struck, the ship is
   considered sunk. The attacking player is informed of this AND of
   the type of ship sunk.
5. If a player sinks all his opponent's ships before all his own
   ships are sunk by  his opponent, he wins the game.''')
    
introduction()

def battleship_game():
    print('''--------------------------------------------------------

It is Player 1's turn to fill his grid. Player 2,
please relinquish device control to Player 1 and
look away from the screen.''')
    choice = input("Player 1, press y when ready to place ships. ")
    if choice == "y" or choice == "Y":
        grid = []
        for row_num in range(8):
            row = []
            for col_num in range(8):
                if row_num == 0:
                    row.append(str(col_num))
                if col_num == 0:
                    row.append(str(row_num))
                else:
                    row.append('~')
        grid.append(row)
    
    for row in grid:
        print(' '.join(row))

battleship_game()