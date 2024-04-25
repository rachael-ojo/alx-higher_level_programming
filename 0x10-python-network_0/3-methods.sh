#!/bin/bash
# This script sends a request to a URL and displays all accepted HTTP methods

curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
