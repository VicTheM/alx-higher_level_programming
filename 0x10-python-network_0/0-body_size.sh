#!/usr/bin/bash
# This script displays the size of a Http response from a server
# It receives an IP to curl as parameter, port could also be specified

response=$(curl -s $1)
echo "${#response}"
