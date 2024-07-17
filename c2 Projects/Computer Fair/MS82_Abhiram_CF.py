# importing tkinter, fram,label, messagebox, and random
from tkinter import *
from tkinter import Tk, Frame, Label
from tkinter import messagebox
import random


class Board:
    # gives color to each tile(background and foreground)
    bg_color={
        
        '2': '#eee4da',
        '4': '#2B89C6',
        '8': '#22CC7E',
        '16': '#E6358B',
        '32': '#CE5404',
        '64': '#F47070',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#f2b179',
        '1024': '#f59563',
        '2048': '#f9f6f2'
    }
    color={
        '2': '#0045BE',
        '4': '#f9f6f2',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#776e65',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2'
    }

        
    def __init__(self):
        # Sets up the window and frame for the game
        self.n=4
        self.window=Tk()
        self.window.title("2048 Game in Python")
        self.gameArea=Frame(self.window, bg="azure3")
        self.Board=[]
        self.gridCell = [[0]*4 for _ in range(4)]
        self.compress = False
        self.merge = False
        self.moved = False
        self.score = 0
        
        for i in range(4):
            rows=[]
            for j in range(4):
                l = Label(self.gameArea, text='', bg="azure4",
                font = ('arial', 22, 'bold'), width=4, height=2)
                l.grid(row=i, column=j, padx=7, pady=7)
                # creating boxes for rows and columns
                rows.append(l)
            self.Board.append(rows)
        self.gameArea.grid()
        
    def reverse(self):
        for idx in range(4):
            self.gridCell[idx].reverse()
                
    def transpose(self):
        self.gridCell=[list(t)for t in zip(*self.gridCell)]
            
    def compressGrid(self):
        # compresses Grid to one side with arrow press
        self.compress = False
        temp = [[0] * 4 for _ in range(4)]
        for i in range(4):
            cnt=0
            for j in range(4):
                if self.gridCell[i][j] != 0:
                    temp[i][cnt]=self.gridCell[i][j]
                    if cnt != j:
                        self.compress = True
                    cnt+=1
        self.gridCell = temp
        
            
    def mergeGrid(self):
        # Function for merging tiles together
        self.merge=False
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j+1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *=2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge=True
                
                        
    def random_cell(self):
        # Spawning new cell(2) random position
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells) #random position
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]=2
            
    def can_merge(self):
        # merges tiles together 
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j+1]:
                    return True
                    
        for i in range(3):
            for j in range(4):
                if self.gridCell[i+1][j] == self.gridCell[i][j]:
                    return True
        return False
        
    def paintGrid(self):
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j]==0:
                    self.Board[i][j].config(text='', bg='azure4')
                else:
                    self.Board[i][j].config(text=str(self.gridCell[i][j]),
                                            bg=self.bg_color.get(str(self.gridCell[i][j])),
                                            fg=self.color.get(str(self.gridCell[i][j])))
                    

class Game:
    def __init__(self, gamepanel):
        self.gamepanel=gamepanel
        self.end=False
        self.won=False
        
    def start(self):
        self.gamepanel.random_cell()
        self.gamepanel.random_cell()
        self.gamepanel.paintGrid()
        # Binds key press to the movement of tiles
        self.gamepanel.window.bind('<Key>', self.link_keys)
        self.gamepanel.window.mainloop()
    
    def link_keys(self, event):
        if self.end or self.won:
            return
        
        self.gamepanel.compress=False
        self.gamepanel.merge=False
        self.gamepanel.moved=False
        
        pressed_key = event.keysym
        
        if pressed_key in ['Up', 'Down', 'Left', 'Right']:
            self.gamepanel.compress = False
            self.gamepanel.merge = False
        # Game movements user makes with key press
        if pressed_key == "Up":
            self.gamepanel.transpose()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.transpose()
        
        elif pressed_key == "Down":
            self.gamepanel.transpose()
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge    
            self.gamepanel.reverse()
            self.gamepanel.transpose()
            
        elif pressed_key == "Left":
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
        
        elif pressed_key == "Right":
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
        else:
            pass
        # Updates score with each tile combination
        self.gamepanel.paintGrid()
        print("Score: " + str(self.gamepanel.score))
        
        flag=0
        for i in range(4):
            for j in range(4):
                if(self.gamepanel.gridCell[i][j]==2048):
                    flag=1
                    break
        if(flag==1): 
            self.won=True
            # reached 2048
            messagebox.showinfo('2048', message="You Wonnn!!")
            print("Winner!")
            return False
                
        for i in range(4):
            for j in range(4):
                if self.gamepanel.gridCell[i][j]==0:
                    flag=1
                    break
        
        if not(flag or self.gamepanel.can_merge()):
            self.end=True
            # No more movements left - no more tiles can merge
            messagebox.showinfo('2048', 'Game Over!!!')
            print("Better Luck Next Time!")
            
        if self.gamepanel.moved:
            # every movement - new cell.
            self.gamepanel.random_cell()
        self.gamepanel.paintGrid()

enter_game = messagebox.askquestion("2048", "Would u like to play 2048? The objective is to combine tiles to reach 2048. If you fill up all the tiles and can't connect, then you lose!")
# messagebox for entering game
if enter_game == 'yes':
    gamepanel = Board()
    game2048 = Game(gamepanel)
    game2048.start()
if enter_game == 'no':
    exit()
    

