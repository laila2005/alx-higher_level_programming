#!/usr/bin/python3
"""
divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix and round
    it two decimals
    """
    #check if div = zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    #check for the size for each row
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    #check if div is an int
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    #check for each num in row is int
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    #check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = []

    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div,2))
        new_matrix.append(new_row)
    return new_matrix
