#!/usr/bin/python3
  fizzbuzz = __import__('12-fizzbuzz').fizzbuzz
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
             """Print the numbers from 1 to 100 separated by a space.
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')

# Test the function
fizzbuzz()
