#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send a GET request to the URL with the specified header
response=$(curl -s -H "X-School-User-Id: 98" "$URL")

# Display the response body
echo "$response"
