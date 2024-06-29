#!/usr/bin/python3

"""
Rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2D matrix 90 degree clockwise
    """

    copy_matrix = matrix.copy()
    reversed_matrix = copy_matrix[::-1]

    for elements in range(len(matrix)):
        new_matrix = []
        for row in reversed_matrix:
            new_matrix.append(row[elements])
            matrix[elements] = new_matrix
)
