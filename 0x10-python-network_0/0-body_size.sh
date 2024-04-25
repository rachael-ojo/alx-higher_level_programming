#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send a curl request to the URL and capture the response
response=$(curl -s -o /dev/null -w "%{size_download}" "$URL")

# Display the size of the response body in bytes
echo "Size of the response body: $response bytes"
