# board = [[0 for x in range(4)] for y in range(6)]
board = [[0,2,0,0],[2,0,0,0],[1,0,2,0],[2,1,2,0]]
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
        print()

print_board()


def checking_computer_tokens(board):
    l = []
    rows = list()
    cols =
    for row in board:
        for token in row:
            if row[token]==2:
                l.append(board[row-1][token])
                l.append(board[row-1][token+1])
                l.append(board[row][token+1])
                l.append(board[row+1][token+1])
                l.append(board[row+1][token])
                l.append(board[row][token-1])
                l.append(board[row-1][token-1])
                # l = list([board[row-1][token],
                #  board[row-1][token+1], 
                # board[row][token+1], 
                # board[row+1][token+1], 
                # board[row+1][token], 
                # board[row+1][token-1], 
                # board[row][token-1], 
                # board[row-1][token-1]])
            

print(checking_computer_tokens(board))

    

                    



