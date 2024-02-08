#!/usr/bin/python3
# Print all possible combinations of two digits
for i in range(10):
    for j in range(i + 1, 10):
        print('{:02d}, '.format(i * 10 + j), end='')

print()  # Print a newline after the loop
