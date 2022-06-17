#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    Return the Pascal's triangle of size n
    """
    triangle = []
    for i in range(n):
        row = [1]
        for j in range(i):
            row.append(triangle[i-1][j] + triangle[i-1][j+1])
        row.append(1)
        triangle.append(row)
    return triangle
