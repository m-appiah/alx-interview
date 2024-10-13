#!/usr/bin/python3
"""
This module defines a function that
generates Pascal's triangle up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Parameters:
    n (int): The number of rows in Pascal's triangle to generate.

    Returns:
    list: A list of lists, where each inner list
    represents a row in Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
