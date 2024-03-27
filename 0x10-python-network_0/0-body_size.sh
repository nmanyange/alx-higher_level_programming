#!/bin/bash
# script that takes in a URL, sends a request to that URL, 
#and displays the size of the body of the response

#!/bin/bash

# Check if URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send a request to the URL and store the response in a temporary file
response=$(mktemp)
curl -s -o "$response" "$URL"

# Get the size of the response body in bytes
size=$(wc -c < "$response")

# Display the size of the response body
echo "Response size: $size bytes"

# Clean up the temporary file
rm "$response"
