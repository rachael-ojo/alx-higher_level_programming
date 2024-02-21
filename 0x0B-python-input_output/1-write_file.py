#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    try:
        # Open the file in write mode using UTF-8 encoding
        with open(filename, 'w', encoding='utf-8') as file:
            # Write the text to the file
            file.write(text)
            # Return the number of characters written
            return len(text)
    except Exception as e:
        # Print an error message if an unexpected error occurs
        print("An error occurred:", e)
        # Return 0 if an error occurs
        return 0
