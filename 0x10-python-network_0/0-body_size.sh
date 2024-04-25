#!/bin/bash                                                                                                                                                                               #task0
curl -sI "$1" | awk '/Content-Length/ {print $2}'
