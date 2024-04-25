#!/usr/bin/python3
"""
This module contains a function to find a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of integers.

    Returns:
        int: A peak value from the list.

    Complexity:
        The algorithm has a complexity of O(log(n)), achieved by utilizing a binary search approach.
    """
    if not list_of_integers:
        return None
    
    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]

# Example usage:
# if __name__ == "__main__":
#     result = find_peak([1, 2, 3, 4, 5])
#     print(result)
