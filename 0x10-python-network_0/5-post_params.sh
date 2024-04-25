#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1
EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"

# Send a POST request with custom variables and capture the response body
response=$(curl -s -X POST "$URL" \
    -d "email=$EMAIL" \
    -d "subject=$SUBJECT")

# Display the response body
echo "$response"
