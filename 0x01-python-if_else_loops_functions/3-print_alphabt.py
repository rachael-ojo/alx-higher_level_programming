#!/usr/bin/python3
# Print the ASCII alphabet in lowercase no newline, 'q' and 'e'
print(''.join(["{}".format(chr(i)) for i in range(97, 123) if chr(i) not in ['q', 'e']]), end='')
