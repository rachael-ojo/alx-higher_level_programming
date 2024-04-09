#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        print()  # New line after printing the integer
        return True
    except:
        return False
