#!/bin/bash
#task3
curl -sI "$1"| grep -o "Allow" | cut -d':' -f2-
