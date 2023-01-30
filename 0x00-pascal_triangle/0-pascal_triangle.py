#!/usr/bin/python3
"""
This file contains the pascal_triangle function
"""


def pascal_triangle(n):
    """This function returns a list of lists of
    integers representing the Pascal’s triangle of n
    """
    # if n <= 0:
    #     return []
    # result = [[1]]
    # for i in range(1, n):
    #     current_row = [1]
    #     for j in range(1, i):
    #         current_row.append(result[i-1][j-1] + result[i-1][j])
    #     current_row.append(1)
    #     result.append(current_row)
    result = []
    for i in range(n):
        currentRow = []
        for j in range(i+1):
            if j == 0 or j == i:
                currentRow.append(1)
            else:
                currentRow.append(result[i-1][j] + result[i-1][j-1])
        result.append(currentRow)
    return result
