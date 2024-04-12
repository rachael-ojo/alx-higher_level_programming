#!/usr/bin/python3
def add(a, b):
    result = add(a, b)
def sub(a, b):
    result = sub(a, b)
def mul(a, b):
    result = mul(a, b)
def div(a, b):
    result = div(a, b)
if __name__ == "__main__":
    from calculator_1 import calculation
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, result))
    print("{} - {} = {}".format(a, b, result))
    print("{} * {} = {}".format(a, b, result))
    print("{} / {} = {}".format(a, b, result))
