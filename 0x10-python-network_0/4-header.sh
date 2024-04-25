#!/bin/bash
# This script sends a GET request to a URL with custom headers and displays response headers

curl -sI -H "X-HolbertonSchool-User-Id: 98" -H "X-Request-Id: 123" "$1" | grep -i "^HTTP\|^X-"
