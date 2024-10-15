#!/usr/bin/python3
"""
This module defines a function that calculates the minimum number of operations
needed to achieve n 'H' characters.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to achieve n
    'H' characters.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required, or 0 if
    n cannot be achieved.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
