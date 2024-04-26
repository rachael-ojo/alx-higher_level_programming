#!/usr/bin/python3
"""
Module to fetch and display information about a GitHub repository.
"""

import requests
import sys

if __name__ == "__main__":
    # Assuming the repository name and owner name are provided as command-line arguments
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API endpoint for repository information
    url = f'https://api.github.com/repos/{owner_name}/{repository_name}'

    try:
        # Send GET request to GitHub API
        response = requests.get(url)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            repo_info = response.json()

            # Display repository information
            print("Repository Name:", repo_info['name'])
            print("Owner:", repo_info['owner']['login'])
            print("Description:", repo_info['description'])
            print("URL:", repo_info['html_url'])
            print("Stars:", repo_info['stargazers_count'])
            print("Watchers:", repo_info['subscribers_count'])
            print("Forks:", repo_info['forks_count'])
        else:
            print(f"Failed to retrieve repository information. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("Error accessing GitHub API:", e)
        sys.exit(1)

