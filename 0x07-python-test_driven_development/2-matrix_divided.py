#!/usr/bin/python3
""" This module divides each element in matrix by div"""


def matrix_divided(matrix, div):
    """
    Takes a list as input and divisor and performs division

    Args:
        matrix(list): a list of integers/floats
        div(int): divisor

    Returns:
        list: a new matrix
    """
    if matrix_checker(matrix) is False:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if matrix_length(matrix) is False:
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) or isinstance(div, float):
        raise TypeError("div must be a number")
    result = []
    for row in matrix:
        result_row = []
        for element in row:
            result_row.append(round(element / div, 2))
        result.append(result_row)
    print(result)
    return matrix


def matrix_checker(matrix):
    """
    Checks if matrix is a list of lists of int/float

    Args:
        matrix(list): a list of int/float

    Returns:
        True on success
        raises a TypeError on failure
    """
    if not isinstance(matrix, list):
        return False
    for sublist in matrix:
        if not isinstance(sublist, list):
            return False
        if not all(isinstance(item, (int, float)) for item in sublist):
            return False
    return True


def matrix_length(matrix):
    """
    Checks if each row have an equal size

    Args:
        matrix(list): a list of integers/floats

    Returns:
        True if they have the same size
    """
    first_row_length = len(matrix[0])
    if not isinstance(matrix, list):
        return False
    if len(matrix) == 0:
        return True
    for row in matrix:
        if not isinstance(row, list) or len(row) != first_row_length:
            return False
    return True
