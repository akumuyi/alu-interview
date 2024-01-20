#!/usr/bin/python3

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n characters 'H' in a text file.

    Parameters:
    - n (int): The desired number of 'H' characters in the file.

    Returns:
    int: The minimum number of operations required. If n is impossible to achieve, returns 0.
    """

    # Base case: If n is 0 or 1, no operations are needed
    if n <= 1:
        return 0

    # Initialize variables
    operations = 0        # Total number of operations
    current_length = 1    # Current length of the sequence of characters in the file
    clipboard = 1        # Number of characters currently stored in the clipboard

    # Continue until the current length reaches or exceeds n
    while current_length < n:
        # Check if n is divisible by the current length
        if n % current_length == 0:
            clipboard = current_length  # Update clipboard to the current length
            operations += 1

        operations += 1
        current_length += clipboard

    return operations

if __name__ == "__main__":
    # Example usage
    n1 = 14
    result1 = minOperations(n1)
    print(f"Min number of operations to reach {n1} characters: {result1}")

    n2 = 100
    result2 = minOperations(n2)
    print(f"Min number of operations to reach {n2} characters: {result2}")

