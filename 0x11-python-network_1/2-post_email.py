#!/usr/bin/python3
"""
Module to send a POST request with an email parameter and display the response body.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Check if both URL and email arguments are provided
    if len(sys.argv) < 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare data to be sent in the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    try:
        # Send a POST request with the specified data
        with urllib.request.urlopen(url, data=data) as response:
            # Read and decode the response body
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.URLError as e:
        print("Error accessing URL:", e)
        sys.exit(1)
