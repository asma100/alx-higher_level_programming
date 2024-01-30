#!/usr/bin/python3
import sys

def as_is_valid(as_board, as_row, as_col):
    """Checks if placing a queen at (as_row, as_col) is valid."""
    for as_i in range(as_row):
        if as_board[as_i] == as_col or abs(as_row - as_i) == abs(as_col - as_board[as_i]):
            return False
    return True

def as_solve_n_queens(as_n, as_board, as_row):
    """Solve the N queens problem using backtracking."""
    if as_row == as_n:
        # Found a solution, print it
        print(" ".join(map(str, as_board)))
        return

    for as_col in range(as_n):
        if as_is_valid(as_board, as_row, as_col):
            as_board[as_row] = as_col
            as_solve_n_queens(as_n, as_board, as_row + 1)

def as_main():
    """Main function to handle arguments and call the solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        as_n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if as_n < 4:
        print("N must be at least 4")
        sys.exit(1)

    as_board = [-1] * as_n  # Initialize board with -1 to represent empty cells
    as_solve_n_queens(as_n, as_board, 0)

if __name__ == "__main__":
    as_main()
