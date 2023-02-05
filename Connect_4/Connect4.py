import random

board = [[1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0]]

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


# checking if a player has won:
def check_horizontal_win(board):
    for row in board:
        for token in [token for token in row if token != 0]:
            if row.count(token) > 3:    # checking for more than 3 duplicates
                print("Player has won!")
                return True
    return False

# if board is bigger, it will return True - need to think of a way that will recognise that the counters are next to each other, not: [0,1,1,1,2,1,0,0]
        
def check_vertical_win(board):
    columns = list(zip(*board))
    for column in columns:
            if column[0] != 0 and column[0]==column[1] and column[0]==column[2] and column[0]==column[3]:
                print("Player has won!")
                return True
    return False
check_vertical_win(board)

#def check_diagonal_left(board):
    # col = range(len(column))
    # for row in board:
    #     if board[-1][-1] == board[:-1][col]:
    #         return True
    #     return False

#def check_diagonal_right(board):
    # col = range(len(column))    # column is undefinied, maybe row[i] = col?
    # for row in board:
    #     if board[-1][0] == board[-1:][col]:
    #         return True
    #     return False     

def player_won():
        return check_horizontal_win(board)
        #check_vertical_win(board)
        #check_diagonal_left(board)
        #check_diagonal_right(board)

# the main game:
if __name__ == "__main__":
    
    while not player_won():
        print_game_board()
        choose_a_column = input("what column would you like to place your token in? (type: 1/2/3/4) ")
        p1 = int(choose_a_column) - 1
        if not place_a_token(1, p1):
            print()
            continue
        else:
            input_token = random.randint(1, len(board[0]))
            p2 = input_token - 1
            while not place_a_token(2, p2):
                input_token = random.randint(1, len(board[0]))
                p2 = input_token - 1
    print_game_board()              
