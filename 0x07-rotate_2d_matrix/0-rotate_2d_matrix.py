#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """ Rotate 2D Matrix 90 degrees clockwise"""

    n = len(matrix)

    for x in range(0, int(n / 2)):
        for y in range(x, n-x-1):
            temp = matrix[x][y]

            matrix[x][y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = matrix[y][n-1-x]
            matrix[y][n-1-x] = temp
