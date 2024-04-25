#!/bin/bash
# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

# Define the URL from the first argument
url="$1"

# Use curl to get the response header size with silent mode (-s)
# and option to head only (-I) and only display headers relevant to size (-H)
size=$(curl -s -I -H "Content-Length" "$url")

# Extract the size value (assuming it's the only value in the header)
size_value=$(echo "$size" | grep -o '[0-9]*')

# Check if size was retrieved successfully
if [ -z "$size_value" ]; then
  echo "Error: Could not determine response size."
  exit 1
fi

# Display the size in bytes
echo "Response size: $size_value bytes"
