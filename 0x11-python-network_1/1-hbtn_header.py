#!/usr/bin/python3
"""task 1"""


import urllib.request
import sys
if __name__ == "__main__":
  url = sys.argv[1]
  with urllib.request.urlopen(url) as response:
    h = response.info() 
    request_id = h.get('X-Request-Id')
  
    if request_id:
      print(request_id)
