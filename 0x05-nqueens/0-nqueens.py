
#!/usr/bin/python3
'''
N Queen Puzzle
    Description:
        The N queens puzzle is the challenge of
        placing N non-attacking queens on an N×N chessboard.

    Usage:
        If the user called the program with the wrong
        number of arguments, print Usage:
        nqueens N, followed by a new line, and exit with the status 1
        where N must be an integer greater or equal to 4
        If N is not an integer, print N must be a number,
        followed by a new line,
        and exit with the status 1
        If N is smaller than 4, print N must be at least 4,
        followed by a new line,
        and exit with the status 1
        The program should print every possible solution to the problem
        One solution per line
        Format: see example
        You don’t have to print the solutions in a specific order

'''

import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]

    def solve(row):
        if row == N:
            for i in range(N):
                for j in range(N):
                    print(board[i][j], end=' ')
                print()
            print()
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

