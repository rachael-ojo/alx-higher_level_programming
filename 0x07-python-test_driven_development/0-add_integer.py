#!/usr/bin/python3
"""
This module provides a function to add two integers.

Functions:
    add_integer(a, b=98): Adds two integers or floats.

Usage:
    from add_integer import add_integer
    result = add_integer(5, 3)
    print(result)  # Output: 8
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number. Default is 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    Examples:
        >>> add_integer(5, 3)
        8
        >>> add_integer(5.6, 3)
        8
        >>> add_integer(5, 3.2)
        8
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
