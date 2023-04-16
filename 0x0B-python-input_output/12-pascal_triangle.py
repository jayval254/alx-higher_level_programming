#!/usr/bin/python3
"""PascalTriangle module"""


def pascal_triangle(n):
    """Pascal triangle
    Args:
        n (int): the size of the triangle
    Returns:
        (list[list]): list of lists of integers representing the pascal's triangle
        an empty list if n<=0
    """
    if n <= 0:
        return []
    result = []
    last = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(last[j] + last[j - 1])
        last = row
        result.append(row)
    return 
