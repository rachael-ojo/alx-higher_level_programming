#!/usr/bin/python3
"""
Module to send a request to a URL and display the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    # Assuming the URL is provided as the first command-line argument
    url = sys.argv[1]

    try:
        response = requests.get(url)

        # Check the HTTP status code
        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            # Display the response body
            print(response.text)

    except requests.exceptions.RequestException as e:
        print("Error accessing URL:", e)
        sys.exit(1)
