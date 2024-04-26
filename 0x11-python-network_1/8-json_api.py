#!/usr/bin/python3
"""
Module to send a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    # Determine the letter (or set to empty string if no argument is provided)
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Define the URL for the POST request
    url = 'http://0.0.0.0:5000/search_user'

    # Prepare the data to be sent in the POST request
    data = {'q': q}

    try:
        # Send a POST request with the data
        response = requests.post(url, data=data)

        # Check if the response is properly JSON formatted and not empty
        if response.ok:
            try:
                json_data = response.json()
                if json_data:
                    print("[{}] {}".format(json_data['id'], json_data['name']))
                else:
                    print("No result")
            except ValueError:
                print("Not a valid JSON")
        else:
            print("No result")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)
