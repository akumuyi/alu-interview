#!/usr/bin/python3

def rain(walls):
    """
    Calculate the total amount of rainwater retained after rain.

    Args:
        walls (list): A list of non-negative integers representing wall heights.

    Returns:
        int: Total amount of rainwater retained in square units.

    Assumptions:
        - The ends of the list (before index 0 and after index walls[-1]) are not walls,
          meaning they will not retain water.
        - If the list is empty, the function returns 0.
    """
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i])

    right_max[n-1] = walls[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])

    water_retained = 0
    for i in range(n):
        water_retained += max(0, min(left_max[i], right_max[i]) - walls[i])

    return water_retained

