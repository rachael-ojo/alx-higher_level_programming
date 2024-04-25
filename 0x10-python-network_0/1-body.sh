#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send a GET request to the URL and capture the response
curl_output=$(curl -s -w "%{http_code}" "$URL" -o response.txt)

# Extract the HTTP status code from the end of curl_output
http_status=$(tail -c 3 <<< "$curl_output")

# Check if the HTTP status code is empty or not a valid HTTP status code
if ! [[ "$http_status" =~ ^[0-9]{3}$ ]]; then
    echo "Request failed with unexpected HTTP status code: $http_status"
    exit 1
fi

# Check if the HTTP status code is 200 (OK)
if [ "$http_status" = "200" ]; then
    # Display the response body
    cat response.txt
else
    echo "Request failed with HTTP status code: $http_status"
    exit 1
fi

# Clean up: remove the temporary response file
rm -f response.txt
