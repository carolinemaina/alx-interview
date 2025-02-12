#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


def print_solution(board):
    """Print the solution in the required format"""
    print([[i, board[i]] for i in range(len(board))])


def is_valid(board, row, col):
    """Check if placing a queen at (row, col) is valid"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, board, row):
    """Use backtracking to find all solutions for the N Queens problem"""
    if row == N:
        print_solution(board)
        return
    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, board, row + 1)
            board[row] = -1


def nqueens(N):
    """Solve the N Queens problem"""
    if N < 4:
        print(f"N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(N, board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
