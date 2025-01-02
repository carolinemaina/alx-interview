#!/usr/bin/python3
"""
Pascal triangle representation
"""

def pascal_triangle(n):
    '''
    Returns an empty list if n <= 0
    '''
    if n <= 0:
        return []        

    triangle = [[1]]

    for row_index in range(1, n):
        row = [1]

        for i in range(1, row_index):
            row.append(triangle[row_index - 1][i - 1] + triangle[row_index - 1][i])

        row.append(1)
    triangle.append(row)
    return triangle
