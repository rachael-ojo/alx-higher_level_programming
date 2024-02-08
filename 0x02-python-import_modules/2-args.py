#!/usr/bin/python3
import sys

def print_arguments():
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("Number of argument(s): .")
    elif num_args == 1:
        print("Number of argument(s): argument:")
        print("1:", sys.argv[1])
    else:
        print("Number of argument(s): arguments:")
        for i in range(1, num_args + 1):
            print(i, ":", sys.argv[i])

if __name__ == "__main__":
    print_arguments()
