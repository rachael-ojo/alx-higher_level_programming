#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send a DELETE request to the URL and capture the response
response=$(curl -s -X DELETE "$URL")

# Display the response body
echo "$response"
