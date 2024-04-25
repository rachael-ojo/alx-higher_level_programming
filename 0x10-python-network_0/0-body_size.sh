#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send a curl request to the URL and capture the size of the response body
response=$(curl -s -o /dev/null -w "%{size_download}" "$URL")

# Check if curl command was successful
if [ $? -ne 0 ]; then
    echo "Error: Curl request to $URL failed"
    exit 1
fi

# Display the size of the response body in bytes
echo "Size of the response body: $response bytes"
