#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_numbers = []  # array to hold squared values
    for row in matrix:
        row_values = []
        for num in row:
            row_values.append(num ** 2)
        squared_numbers.append(row_values)
    return squared_numbers
