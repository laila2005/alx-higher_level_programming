#!/usr/bin/python3
import sys


def print_usage_and_exit():
    """Print usage instructions and exit with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def print_error_and_exit(message):
    """Print error message and exit with status 1."""
    print(message)
    sys.exit(1)


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens_util(board, col, N, solutions):
    """Utilize backtracking to solve the N queens problem."""
    if col >= N:
        solution = [[r.index(1), r.index(1) + col] for r in board]
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, N, solutions)
            board[i][col] = 0


def solve_n_queens(N):
    """Solve the N queens problem and return all solutions."""
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit()
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")
    if N < 4:
        print_error_and_exit("N must be at least 4")
    solutions = solve_n_queens(N)
    print("OK")
    print(len(solutions))
    for solution in solutions:
        print(solution)
