#!/bin/bash
#task0
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
