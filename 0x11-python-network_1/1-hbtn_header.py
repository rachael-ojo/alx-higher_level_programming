#!/usr/bin/python3
"""
Module to send a request to a URL and display the value of the X-Request-Id header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    # Check if a URL argument is provided
    if len(sys.argv) < 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            # Get the value of the X-Request-Id header if present
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id:
                print("X-Request-Id:", x_request_id)
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        print("Error accessing URL:", e)
        sys.exit(1)
