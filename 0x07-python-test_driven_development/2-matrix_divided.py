#!/usr/bin/python3
"""
Divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix and rounds the result to two decimals.
    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int/float): The divisor.
    Returns:
        list: A new matrix with the divided and rounded results.
    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)
    return new_matrix
