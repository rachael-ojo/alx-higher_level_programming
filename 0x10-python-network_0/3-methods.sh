#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Array of HTTP methods to test
http_methods=("GET" "POST" "PUT" "DELETE" "HEAD" "OPTIONS")

# Iterate over each HTTP method and check server response
for method in "${http_methods[@]}"
do
    # Send an HTTP request with the current method to the URL
    response=$(curl -s -X "$method" -I "$URL")

    # Check if the response includes 'Allow' header indicating accepted methods
    allowed_methods=$(grep -i '^Allow:' <<< "$response" | sed 's/Allow: //i')

    # Display the allowed methods for the current HTTP method
    if [ -n "$allowed_methods" ]; then
        echo "HTTP $method - Allowed Methods: $allowed_methods"
    else
        echo "HTTP $method - No 'Allow' header found"
    fi
done
