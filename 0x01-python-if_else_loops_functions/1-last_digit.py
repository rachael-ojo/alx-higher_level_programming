#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Generate a random signed number
number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = abs(number) % 10

# Print the result based on the last digit
print("The string Last digit of")
print(number)
print("the string is")
if last_digit > 5:
    print(last_digit, "and is greater than 5")
elif last_digit == 0:
    print(last_digit, "and is 0")
else:
    print(last_digit, "and is less than 6 and not 0")
