#!/bin/bash
#task3
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
