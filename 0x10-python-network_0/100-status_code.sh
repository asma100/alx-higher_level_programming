#!/bin/bash
#task100
curl -s -o /dev/null -w "%{http_code}" "$1"
