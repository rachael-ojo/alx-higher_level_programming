#!/bin/bash
# This script sends a request to 0.0.0.0:5000/catch_me to trigger a specific response from the server

curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me -H "Referer: 0.0.0.0:5000/catch_me"
