#!/usr/bin/python3
class MyList(list):
    def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: An object to check.
        a_class: The class to compare with.

    Returns:
        True if the object is exactly an instance of the specified class, otherwise False.
"""
    return type(obj) is a_class

if __name__ == "__main__":
    print(is_same_class(5, int))  
    print(is_same_class(5, float))
    print(is_same_class([], list))
    print(is_same_class([], dict))
