#!/bin/bash
# This script takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
# send data and display body of response
# curl -X GET --data "X-School-User-Id=98" $1

