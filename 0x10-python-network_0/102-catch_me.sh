#!/bin/bash

# Send a POST request to the target URL with specific data that triggers the server response
curl -s -X PUT -L -d "user_id=98" 0.0.0.0:5000/catch_me
