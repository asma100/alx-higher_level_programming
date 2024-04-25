#!/bin/bash
#task101
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1" | jq -r '.'
