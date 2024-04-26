#!/bin/bash
# This script takes in a URL, sends a POST request to the passed URL, and displays the body of the response
# curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

# send data and display body of response
curl -X POST --data '{"email": "test@gmail.com", "subject": "I will always be here for PLD"}' --header 'ContentType: application/json' $1

