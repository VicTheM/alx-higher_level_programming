#!/bin/bash
# send data and display body of response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
