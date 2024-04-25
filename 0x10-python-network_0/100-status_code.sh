#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Temporary file to store curl output
temp_file=$(mktemp)

# Send a request to the URL and store the output in the temporary file
curl -s -o "$temp_file" -w "%{http_code}" "$URL"

# Read and display only the status code from the temporary file
status_code=$(tail -n1 "$temp_file")

echo "Status code: $status_code"

# Clean up: remove the temporary file
rm "$temp_file"
