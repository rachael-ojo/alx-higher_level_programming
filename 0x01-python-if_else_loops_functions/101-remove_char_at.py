#!/usr/bin/python3
def remove_char_at(string, n):
    if n < 0 or n >= len(string):
        return string  # return original string if n is out of range

    new_string = ""
    for i in range(len(string)):
        if i != n:
            new_string += string[i]
    return new_string

# Test the function
original_string = "example"
position_to_remove = 2
print(remove_char_at(original_string, position_to_remove))  # Output: "exmple"
