board = [[0 for x in range(4)] for y in range(6)]

print(board)

def print_board():
    for row in board:
        for token in row:
            if token == 1:
                print('X', end=" ")
            elif token == 2:
                print('O', end=" ")
            else:
                print("-", end=" ")

print_board()
