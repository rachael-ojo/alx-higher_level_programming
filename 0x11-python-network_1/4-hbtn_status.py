#!/usr/bin/python3
"""
Module to fetch and display the body of a URL response using the requests package.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

        # Print the response body in the specified format
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))

    except requests.exceptions.RequestException as e:
        print("Error accessing URL:", e)
