import random

board = [[0 for x in range(4)] for y in range(6)]

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
    first_token_check = range(len(board[0])-3)
    for row in board:
        for token in first_token_check:
            if row[token] != 0 and row[token]==row[token+1] and row[token]==row[token+2] and row[token]==row[token+3]:
                if row[token] == 1:
                    print("Player has won!")
                else:
                    print("Computer has won!")  
                return True
    return False
        
        
def check_vertical_win(board):
    columns = list(zip(*board))
    first_token_check = range(len(columns[0])-3)
    for column in columns:
        for token in first_token_check:
            if column[token] != 0 and column[token]==column[token+1] and column[token]==column[token+2] and column[token]==column[token+3]:
                if column[token] == 1:
                    print("Player has won!")
                else:
                    print("Computer has won!")    
                return True
    return False

def check_diagonal_left(board):
    rows = range(len(board) - 3)
    cols = range(3, len(board[0]))
    checkable_tokens = [(r, c) for r in rows for c in cols]  # [(0, 3)] [(0,3),(0,4),(1,3),(1,4)]
    for r, c in checkable_tokens:
        if board[r][c] != 0 and board[r][c]==board[r+1][c-1] and board[r][c]==board[r+2][c-2] and board[r][c]==board[r+3][c-3]:
            if board[r][c] == 1:
                print("Player has won!")
            else:
                print("Computer has won!")
            return True
    return False

def check_diagonal_right(board):
    rows = range(len(board) - 3)
    cols = range(len(board[0]) - 3)
    checkable_tokens = [(r, c) for r in rows for c in cols]
    for r, c in checkable_tokens:
        if board[r][c] != 0 and board[r][c]==board[r+1][c+1] and board[r][c]==board[r+2][c+2] and board[r][c]==board[r+3][c+3]:
            if board[r][c] == 1:
                print("Player has won!")
            else:
                print("Computer has won!")
            return True
    return False

def player_won():
        if check_horizontal_win(board) or check_vertical_win(board) or check_diagonal_left(board) or check_diagonal_right(board):
            return True
        return False

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
