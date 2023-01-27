'''Better version of the game connect 4'''

board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

def print_game_board():
    for row in board:
        for token in row:
            if token == 1:
                print("X", end=" ")
            elif token == 2:
                print("O", end=" ")
            else:
                print("-", end=" ")
        print()        


# allows a player to place a token in the board:
def place_a_token(token, column):
    if board[0][column] > 0:
        print("That column has already been filled!")
        return False
    
    for row in range(len(board)):
        if board[row][column] > 0:
            board[row -1][column] = token
            return True
    board[-1][column] = token
    return True



# checks whether a player has won:

def check_if_won():
    pass

# the main game:
print_game_board()
while True:
    choose_a_column = input("what column would you like to place your token in? (type: 1/2/3/4) ")
    p = int(choose_a_column) - 1
    place_a_token(1, p)
    print_game_board()

'''
p1 = 1
p2 (computer) = 2
'''



'''
import random

if != place_a_token():
    continue
else:
    input_token = random.randint(board[0][0], len(board[row]))
    p2 = input_token -1
    place_a_token(2, p2)
    print_game_board()                # goes to the top of the while loop: asks for an input again
'''



'''
def check_horizontal_win():
    for row in board:
        if board.count(row) > 3:    # checking for more than 3 duplicates
            return True
        return False

def check_vertical_win():
    for row in board:
        for board[row][column]:
            if board[]

def check_diagonal_left():


check_diagonal_right()
    col = range(len(column))    # column is undefinied, maybe row[i] = col?
    for row in board:
        if board[-1][0] = board[-1:][col]:
            return True
        return False       
(board[-1][0] = board[-2][1] = board[-3][2] = board[-4][3])



def player_has_won?(token):
    while != player_has_won?() -> False
        check_horizontal_win()
        check_vertical_win()
        check_diagonal_left()
        check_diagonal_right()
    print(f"Player {token} has won!")

'''
