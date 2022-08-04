#!/usr/bin/python3
"""
Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    reverses the  2d matrix rows and columns
    """
    newmatrics = matrix
    for i in range(len(matrix)):
        for j in range(i):
            temp1 = matrix[i][j]
            temp2 = matrix[j][i]
            newmatrics[i][j] = temp2
            newmatrics[j][i] = temp1
    # print(newmatrics)
    for i in matrix:
        i.reverse()
