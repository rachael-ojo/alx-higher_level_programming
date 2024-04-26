#!/usr/bin/python3
"""
Module to send a request to a URL and display the value of the X-Request-Id header.
"""

import requests
import sys

if __name__ == "__main__":
    # Assuming the URL is provided as the first command-line argument
    url = sys.argv[1]

    try:
        response = requests.get(url)

        # Check if the X-Request-Id header is present in the response
        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id:
            print("X-Request-Id:", x_request_id)
        else:
            print("X-Request-Id header not found in the response.")

    except requests.exceptions.RequestException as e:
        print("Error accessing URL:", e)
        sys.exit(1)
