#!/usr/bin/bash
# This script sends GET request to a server and displays the body of a 200 response

# get header + body
curl -X GET -s -i $1 --output /tmp/tmp_curl
head --lines=1 /tmp/tmp_curl | grep --only-matching 200

# If the response is 200, output the body of response
# there is always a blank line before the message boddy
if [ $? -eq 0 ]; then
	grep -x -m 1 -A 10000 /tmp/tmp_curl | tail --lines=+2
fi
rm /tmp/tmp_curl
