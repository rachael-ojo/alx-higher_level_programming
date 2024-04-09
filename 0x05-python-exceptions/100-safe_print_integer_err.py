#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
        print()  # New line after printing the integer
        return True
    except ValueError:
        print("Exception: ValueError", file=sys.stderr)
        return False
