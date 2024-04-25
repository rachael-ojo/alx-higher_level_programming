#!/bin/bash
# This script sends a POST request with parameters to a URL and displays the response body

curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1
