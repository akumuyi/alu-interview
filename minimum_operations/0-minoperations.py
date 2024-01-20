#!/usr/bin/python3
"""
This script contains a function, minOperations, that calculates
the fewest number of operations needed to result in exactly n
characters 'H' in a text file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n characters 'H' in a text file.

    Parameters:
    - n (int): The desired number of 'H' characters in the file.

    Returns:
    int: The minimum number of operations required. If n is
    impossible to achieve, returns 0.
    """

    # Base case: If n is 0 or 1, no operations are needed
    if n <= 1:
        return 0

    # Initialize variables
    operations = 0
    current_length = 1
    clipboard = 1

    # Continue until the current length reaches or exceeds n
    while current_length < n:
        # Check if n is divisible by the current length
        if n % current_length == 0:
            clipboard = current_length  # Update clipboard to the current length
            operations += 1

        operations += 1
        current_length += clipboard

    return operations
