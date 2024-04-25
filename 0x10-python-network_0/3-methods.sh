#!/bin/bash
#task3
curl -sLX OPTIONS $1 | grep -o "Allow: .*" | cut -d':' -f2-
