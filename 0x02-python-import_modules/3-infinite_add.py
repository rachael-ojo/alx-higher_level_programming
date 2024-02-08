#!/usr/bin/python3
import sys

def sum_arguments():
    total = sum(int(arg) for arg in sys.argv[1:])
    print(total)

if __name__ == "__main__":
    sum_arguments()
