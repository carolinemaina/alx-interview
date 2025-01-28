#!/usr/bin/python3
import sys


def print_solutions(board):
    """Helper function to print the board"""
    print(board)


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at (row, col)"""
    for i in range(row):
        # Check if the column or diagonal is attacked
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row, board):
    """Solve the N queens problem using backtracking"""
    if row == N:
        print_solutions(board)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(N, row + 1, board)
            board[row] = -1  # Backtrack


def nqueens(N):
    """Main function to solve the N queens problem"""
    if N < 4:
        print(f"{N} must be at least 4")
        sys.exit(1)

    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(N, 0, board)


def main():
    """Main function to handle input arguments"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)


if __name__ == "__main__":
    main()

