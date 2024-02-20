#!/usr/bin/python3

def raise_exception_msg(message=""):
    try:
        # Attempting to raise a NameError with the provided message
        raise NameError(message)
    except NameError as e:
        # Catching the exception and printing the error message
        print("Name Error:", e)
