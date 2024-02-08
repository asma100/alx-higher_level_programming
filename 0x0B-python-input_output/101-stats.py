#!/usr/bin/python3
"""module"""


import sys
"""module"""
tsize = 0
s_codes = {}
l_count = 0
try:
    for line in sys.stdin:
        l_count += 1
        try:
            _, _, _, _, _, s_code, file_size = line.split()
            file_size = int(file_size)
            tsize += file_size
            status_codes[s_code] = s_codes.get(s_code, 0) + 1
        except ValueError:
            pass
        if l_count % 10 == 0 or l_count == 1:
            print("File size:", tsize)
            for code in sorted(s_codes):
                print(code + ":", s_codes[code])
except KeyboardInterrupt:
    print("File size:", tsize)
    for code in sorted(s_codes):
        print(code + ":", s_codes[code])
