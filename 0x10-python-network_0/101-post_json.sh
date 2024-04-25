#!/bin/bash

# Check if both URL and filename arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

URL=$1
FILENAME=$2

# Check if the specified file exists
if [ ! -f "$FILENAME" ]; then
    echo "Error: File '$FILENAME' not found"
    exit 1
fi

# Send a JSON POST request with file contents in the body and capture the response
response=$(curl -s -X POST -H "Content-Type: application/json" -d "@$FILENAME" "$URL")

# Display the response body
echo "$response"
