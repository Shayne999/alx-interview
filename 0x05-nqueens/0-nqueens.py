#!/usr/bin/python3
"""N Queens Problem"""


import sys


def is_safe(board, row, col, N):
    """Checks if it is safe to place a queen at board"""
    for i in range(row):
        if board[i][col] == 1:
            return False

    """Check upper diagonal on left side"""
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    """Check lower diagonal on left side"""
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, row, N, solutions):
    """Converts the board to a list of lists"""
    if row == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, N, solutions)
            board[row][col] = 0


def solve_n_queens(N):
    """Solves the N Queens problem"""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for i in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_n_queens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
