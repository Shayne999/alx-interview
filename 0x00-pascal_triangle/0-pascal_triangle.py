#!/usr/bin/python3

""" Returns pascals triangle"""

def pascal_triangle(n):
    # prints out pascals triangle

    # returns an empty list if n <= 0
    if n <= 0:
        return []
    
    p_triangle = []

    # creates triangle rows, each one starting with 1
    for row_count in range(n):
        row = [1] * (row_count + 1)

        # fills in each row's values based on the previous row
        for j in range(1, row_count):
            row[j] = p_triangle[row_count - 1][j - 1] + p_triangle[row_count - 1][j]

        #append rows to the triangle
        p_triangle.append(row)

    return p_triangle