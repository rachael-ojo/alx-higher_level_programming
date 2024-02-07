#!/usr/bin/python3
# Print the ASCII alphabet in lowercase without newline, excluding 'q' and 'e'
print(''.join(chr(i) for i in range(97, 123) if chr(i) not in ['q', 'e']), end='')
