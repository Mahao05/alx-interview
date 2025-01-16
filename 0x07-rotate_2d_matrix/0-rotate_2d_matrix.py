#!/usr/bin/python3
""" 2D rotation """


def rotate_2d_matrix(matrix):
    """function that takes a matrix
    and rotates it 90 degrees
    clockwise
    Instructions:
        - Do not return anything.
        - The matrix must be edited in-place.
    Assumptions:
        - matrix is a 2D array (n x n)
        - matrix is not empty
    """
    n = len(matrix)
    # We will iterate the matrix from the outermost layer moving inwards
    # n // 2 is the number of times we will iterate the matrix based on its
    # size
    for row in range(n // 2):
        # n - row - 1 is the last column
        for column in range(row, n - row - 1):
            curr_value = matrix[row][column]
            # left -> top
            matrix[row][column] = matrix[n - 1 - column][row]
            # bottom -> left
            matrix[n - 1 - column][row] = matrix[n - 1 - row][n - 1 - column]
            # right -> bottom
            matrix[n - 1 - row][n - 1 - column] = matrix[column][n - 1 - row]
            # top -> right
            matrix[column][n - 1 - row] = curr_value
