#!/usr/bin/python3
import sys

def printSolution(board):
    """Print the positions of the queens"""
    solution = []
    for i in range(len(board)):
        solution.append([i, board[i]])
    print(solution)


def isSafe(board, row, col, N):
    """Check if placing a queen at (row, col) is safe"""
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solveNQUtil(board, col, N):
    """Use backtracking to solve the N queens problem"""
    if col == N:
        printSolution(board)
        return True

    res = False
    for i in range(N):
        if isSafe(board, i, col, N):
            board[col] = i
            res = solveNQUtil(board, col + 1, N) or res
            board[col] = -1  # backtrack
    return res


def solveNQ(N):
    """Initialize the board and start solving"""
    if N < 4:
        print(f"{N} must be at least 4")
        sys.exit(1)

    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    board = [-1] * N  # Board initialized with -1 (no queens placed)
    if not solveNQUtil(board, 0, N):
        print("Solution does not exist")
        sys.exit(1)


def main():
    """Main function to handle input and run the solution"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solveNQ(N)


if __name__ == '__main__':
    main()
