#!/usr/bin/bash
# This script sends GET

# send data and display body of response
curl -X POST --data '{"email": "test@gmail.com", "subject": "I will always be here for PLD"}' --header 'ContentType: application/json' $1

