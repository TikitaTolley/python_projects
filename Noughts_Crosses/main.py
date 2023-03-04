import random

board = [[0,0,0],[0,0,0],[0,0,0]]

#PLAYER = O, 1
#COMPUTER = X , 2

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
    

def check_horizontal():
    pass

def check_vertical():
    pass

def diagonal_left():
    pass

def diagonal_right():
    pass

def placing_counter(counter, col, board):
    if board[2][col] == 0:
        board[2][col] = counter
    elif board[2][col] != 0 and board[1][col] == 0 and board[0][col] == 0:
        board[1][col] = counter
    elif board[2][col] != 0 and board[1][col] != 0 and board[0][col] == 0:
        board[0][col] = counter
    else:
        print("Column is full!")
        return False


print_board(board)

#if __main__ == True:
def play():
    while True:
        place_counter = input("Where would you like to place your counter? (column 1, 2 or 3?) ")   # indexed + 1 : column position
        player_1 = int(place_counter) - 1
        if placing_counter(1, player_1, board) == False:
            print_board(board)
            continue
        else:
            player_2 = random.randint(len(board)-1)
            if placing_counter(2, player_2, board) == False:
                print_board(board)
                continue

play()

print("Player has won!")

