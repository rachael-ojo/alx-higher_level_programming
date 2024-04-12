#!/usr/bin/python3
>>> import dis
>>> def magic_calculation(a, b, c):
...     return a + b * c
...
>>> dis.dis(magic_calculation)
  2           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 LOAD_FAST                2 (c)
              6 BINARY_MULTIPLY
              8 BINARY_ADD
             10 RETURN_VALUE
