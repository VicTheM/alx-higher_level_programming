#!/bin/bash
# This script displays the size of a Http response from a server
# It receives an IP to curl as parameter, port could also be specified

#response=$(curl -s $1)
#echo "${#response}"

# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -o /dev/null -w "%{size_download}\n" "$1"
