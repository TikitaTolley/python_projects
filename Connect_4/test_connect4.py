
from Connect_4.Connect4 import *

def test_demo():
    assert 3 != 2

def test_horizontal_win_on_empty_board():
    board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    assert not check_horizontal_win(board)

def test_horizontal_win_on_non_win():
    board = [[0,1,1,0], [1,0,0,1], [1,0,1,1], [0,1,0,0]]
    assert not check_horizontal_win(board)

def test_horizontal_win_on_non_win_mix():
    board = [[0,1,1,0], [1,0,0,1], [1,2,1,1], [0,1,0,0]]
    assert not check_horizontal_win(board)

def test_horizontal_win_on_win():
    board = [[0,0,0,0], [1,1,1,1], [0,0,0,0], [0,0,0,0]]
    assert check_horizontal_win(board)

def test_horizontal_win_on_win_p2():
    board = [[0,0,0,0], [1,1,0,1], [2,2,2,2], [0,0,0,0]]
    assert check_horizontal_win(board)