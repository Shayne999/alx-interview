#!/usr/bin/python3

""" Returns pascals triangle"""

def pascal_triangle(n):

    p_triangle = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            p_triangle.append(level)
    return p_triangle