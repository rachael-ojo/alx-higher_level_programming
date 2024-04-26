#!/usr/bin/python3
"""
Module to use GitHub API with Basic Authentication to display user ID.
"""

import requests
import sys

if __name__ == "__main__":
    # Assuming the GitHub username and personal access token (PAT) are provided as command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # GitHub API endpoint for authenticated user information
    url = 'https://api.github.com/user'

    try:
        # Send GET request to GitHub API using Basic Authentication with username and PAT
        response = requests.get(url, auth=(username, password))

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data['id']
            print("User ID:", user_id)
        else:
            print("Failed to retrieve user information. Status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Error accessing GitHub API:", e)
        sys.exit(1)

