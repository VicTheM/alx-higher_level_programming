#!/bin/bash
# This script sends GET

# send data and display body of response
curl -X POST --data @"$2" --header 'ContentType: application/json' $1

