import random

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
def check_horizontal_win():
    for row in board:
        for token in [token for token in row if token != 0]:
            if row.count(token) > 3:    # checking for more than 3 duplicates
                print("Player has won!")
                return False
            return True
        
#def check_vertical_win(column):
    for row in board:
        if board[0][column] == board[:-1][column]:
            pass

#def check_diagonal_left(column, board):
    col = range(len(column))
    for row in board:
        if board[-1][-1] == board[:-1][col]:
            return True
        return False

#def check_diagonal_right(column, board):
    col = range(len(column))    # column is undefinied, maybe row[i] = col?
    for row in board:
        if board[-1][0] == board[-1:][col]:
            return True
        return False     

def player_not_won():
        check_horizontal_win()
        #check_vertical_win()
        #check_diagonal_left()
        #check_diagonal_right()

# the main game:
print_game_board()
while True:
    choose_a_column = input("what column would you like to place your token in? (type: 1/2/3/4) ")
    p1 = int(choose_a_column) - 1
    place_a_token(1, p1)
    print_game_board()
    print()
    player_not_won()
    if not place_a_token(1, p1):
        continue                    # goes to the top of the while loop: asks for an input again
    else:
        input_token = random.randint(board[0][0], len(board[0]))
        p2 = input_token - 1
        place_a_token(2, p2)
        print_game_board()                
        player_not_won()

'''
bugs so far:
- not recognising a win
- computer is putting in 2 tokens every turn, one X and one O
'''
