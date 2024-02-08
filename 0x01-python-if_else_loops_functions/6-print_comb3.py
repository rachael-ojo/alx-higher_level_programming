#!/usr/bin/python3
# Print all possible combinations of two digits
for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        print('{:02d}, '.format(1 * 10 + 2), end='')

print()  # Print a newline after the loop
