#!/usr/bin/python3
# Print numbers from 0 to 98 in decimal and hexadecimal using format string
for i in range(99):
    print('{} {}'.format(i, hex(i)), end=' ')
