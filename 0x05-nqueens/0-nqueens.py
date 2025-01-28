#!/usr/bin/python3
""" 0-nqueens Module """

import sys


def solve_nqueens(N):
    """
    Solves the N Queens problem and prints all possible solutions.
    Args:
    N: The number of queens and the size of the chessboard.
    """

    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    queens = []
    solutions = []

    def is_safe(queens, row, col):
        """
        Checks if queen can be placed at
        given position without attacking any other queen.
        """

        for queen in queens:
            if queen[
                    0
                    ] == row or queen[
                            1
                            ] == col or abs(
                                    queen[0] - row
                                    ) == abs(queen[1] - col):
                            return False
        return True


    def backtrack(queens):
        """
        Recursive function to solve the N Queens problem.
        """
        if len(queens) == N:
            solutions.append(queens.copy())
            return

        for row in range(N):
            if is_safe(queens, row, len(queens)):
                queens.append([row, len(queens)])

                backtrack(queens)
                queens.pop()

            backtrack(queens)

            for solution in solutions:
                print(solution)
            return solutions


    if __name__ == '__main__':
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)

        try:
            num_queens = int(sys.argv[1])
            solve_nqueens(num_queens)
        except ValueError:
            print("N must be a number")
            sys.exit(1)
