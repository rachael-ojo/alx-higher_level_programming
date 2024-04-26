#!/usr/bin/python3
"""
Module to send a request to a URL and display the body of the response.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    # Check if a URL argument is provided
    if len(sys.argv) < 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
        sys.exit(1)
    except urllib.error.URLError as e:
        print("Error accessing URL:", e.reason)
        sys.exit(1)
