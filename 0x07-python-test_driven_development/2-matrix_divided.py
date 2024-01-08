#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ Divides elements of a matrix
    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float).

    Returns:
        A new matrix with all elements divide3d by div rounded
        to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats or if
        the rows of the matrix have different sizes, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list)
            for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
