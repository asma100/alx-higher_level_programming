#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
   html = response.read()
print(f"Body response:\n\t- type: {type(html)}\n\t- content: {html}\n\t- utf8 content: {html.decode('utf-8')}")

  
