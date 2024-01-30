#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    """Checks if placing a queen at (row, col) is valid."""
    for i in range(row):
        if board[i] == col or abs(row - i) == abs(col - board[i]):
            return False
    return True

def solve_n_queens(n, board, row):
    """Solve the N queens problem using backtracking."""
    if row == n:
        # Found a solution, print it
        print(" ".join(map(str, board)))
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_n_queens(n, board, row + 1)

def main():
    """Main function to handle arguments and call the solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n  # Initialize board with -1 to represent empty cells
    solve_n_queens(n, board, 0)

if __name__ == "__main__":
    main()
