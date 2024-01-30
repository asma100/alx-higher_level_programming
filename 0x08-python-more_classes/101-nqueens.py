#!/usr/bin/python3
import sys

def is_valid(board, row, col):

    for i in range(row):
        if board[i] == col:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i] == j:
            return False
    return True

def solve(board, row):
    if row == len(board):
        print(board)
    else:
        for col in range(len(board)):
            if is_valid(board, row, col):
                board[row] = col
                solve(board, row+1)

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [-1] * N
solve(board, 0)
