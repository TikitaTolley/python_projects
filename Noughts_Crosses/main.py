import random

board = [[0,0,0],[0,0,0],[0,0,0]]

def print_board(board):
    for row in board:
        print()
        for col in row:
            if col == 1:
                print('O', end=" ")
            elif col == 2:
                print('X', end=" ")
            else:
                print("-", end=" ")
    

def check_horizontal(board):
    for row in board:
        if row[0] == 1:
            if row[0] == row[1] == row[2]:
                print("Player 1 has won!")
                return False
        if row[0] == 2:
            if row[0] == row[1] == row[2]:
                print("Player 2 has won!")
                return False


def check_vertical(board):
    column_lists = [list(x) for x in zip(*board)]   # list comprehension to make tuples into lists of columns
    for column in column_lists:
        if column[0] == 1:
            if column[0] == column[1] == column[2]:
                print("Player 1 has won!")
                return False
        if column[0] == 2:
            if column[0] == column[1] == column[2]:
                print("Player 2 has won!")
                return False


def diagonal_right(board):
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 1:
            print("Player 1 has won")
            return False
        elif board[0][0] == 2:
            print("Player 2 has won!")
            return False


def diagonal_left(board):
    if board[2][2] == board[1][1] == board[2][0]:
        if board[0][0] == 1:
            print("Player 1 has won")
            return False
        elif board[0][0] == 2:
            print("Player 2 has won!")
            return False


def check_if_winner():
    if check_horizontal(board) == False or check_vertical(board) == False or diagonal_left(board) == False or diagonal_right(board) == False:
        return True
    return False


def placing_counter(counter, col, board):
    while True:    
        if board[2][col] == 0 and board[1][col] == 0 and board[0][col] == 0:
            board[2][col] = counter
            return True
        elif board[2][col] != 0 and board[1][col] == 0 and board[0][col] == 0:
            board[1][col] = counter
            return True
        elif board[2][col] != 0 and board[1][col] != 0 and board[0][col] == 0:
            board[0][col] = counter
            return True
        elif board[2][col] != 0 and board[1][col] != 0 and board[0][col] != 0:
            print()
            print("Column is full!")
            return False
        elif col < 0 or col > 2:
            print()
            print("This isn't a column in the board!")
            return False
        for row in board:
            for space in row:
                if space != 0:
                    print()
                    print("The board is full, you have drawn!")
                    return False


def play():
    while True:
        print()
        print_board(board)
        place_counter = input("Where would you like to place your counter? (column 1, 2 or 3?) ")   # indexed + 1 : column position
        player_1 = int(place_counter) - 1
        if placing_counter(1, player_1, board):
            if check_if_winner():
                print_board(board)
                break
                                              # player 2's turn
            player_2 = random.randint(0, 2)
            while not placing_counter(2, player_2, board):
                player_2 = random.randint(0, 2)
                if check_if_winner():
                    print_board(board)
                    break


play()


