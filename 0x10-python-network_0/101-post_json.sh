#!/bin/bash
#task101
curl -s -o /dev/null -w "%{http_code}" "$1"
