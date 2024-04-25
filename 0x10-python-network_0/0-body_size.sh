#!/bin/bash
#task0
curl -sI $1 | grep "Content-Length" | cut -d " " -f2x
