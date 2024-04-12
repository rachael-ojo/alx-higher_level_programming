#!/usr/bin/python3
"""Defines an inherited list class Mylist"""

class MyList(list):
    """Implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """Prints the list in sorted order (ascending)"""
        print(Sorted(self))
