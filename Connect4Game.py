'''
The Connect 4 Game:

two modes:
- player1 vs player 2
- player vs computer

how to play:
4 x 4 grid

the 1st player to connect four of their discs horizontally, vertically 
or diagonally winds the game!
- only 1 piece can be played at a time on each players go


how to code it!
1st player will have discs = 1
2nd player will have discs = 2
make a matrix of 0 that change to either 1 or 2 
[y, x]?
Example:
0000
1122
2222
0010

so player 2 would win!
draw out grid? using pygame ? of end result...
'''
import random
import matplotlib.pyplot as plt
import numpy as np
import math
import pygame


#global values
PLAYER_1 = 1
PLAYER_2 = 2
COMPUTER = 3
'''
ROWS = 4
COLUMNS = 4
'''

# introduction:
def intro():
    while True:    
        playing = input("Would you like to play a game of Connect 4? (type: yes or q to quit) ").lower()
        if playing == "yes":
            choice_of_game = input("How many players are there? (type: 1 or 2) ")
            if choice_of_game == "2":
                print("You have chosen the 2 player game!")
                print_empty_grid()
            else:
                print("You have chosen to play against the computer!")
        else:
            print("See you another time!")
            quit()

def print_empty_grid():
    d = np.zeros((4,4))
    return d

print_empty_grid()

























































'''
# matrix: dictionary: rows: A,B,C,D | columns: array of 4 zeros - so you can index them: e.g. 1 disc could go to empty_discs[D][0]
empty_discs = {
    "A": [0,0,0,0],
    "B": [0,0,0,0],
    "C": [0,0,0,0],
    "D": [0,0,0,0]
}

def print_discs():
    x = empty_discs.values()
    y = empty_discs.keys()
    plt.plot([x,y])
    plt.show()


def play2players():
    while True:
        player1()
        print_discs()
        check_horizontal()
        check_vertical()
        check_diagonally_left()
        check_diagonally_right()
        player2()
        print_discs()
        check_horizontal()
        check_vertical()
        check_diagonally_left()
        check_diagonally_right()

def play1players():
    pass


# run through each array and check if every element is all 1, all 2 or all 3
def check_horizontal():
    while True:
        for x in empty_discs.values():
            if x == 0:
                continue
            elif x == 1:
                pass

        return False

def check_vertical():
    pass

def check_diagonally_right():
    pass

def check_diagonally_left():
    pass
# player chooses a column
def player1():
    while True:
        turn = input("Where would you like your disc to go? (columns: 1, 2, 3 or 4?) ")
        for i in empty_discs[D][x]:
            if turn == "1":
                empty_discs["D"][0] = PLAYER_1
            pass
    

def player2():
    pass

def computer():
    pass

def win():
    pass
    
print_discs()
intro()
'''

