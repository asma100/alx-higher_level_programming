#!/bin/bash
#task0
url="$1"
curl -s -I -H "Content-Length" "$url"
