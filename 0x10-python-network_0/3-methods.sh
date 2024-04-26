#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept.
curl -s -X OPTIONS -I "$1" | grep -i "Allow:" | sed 's/Allow: //i'
