#!/usr/bin/python3
output = ""
for i in range(122, 96, -1):
    if i % 2 == 0:
        output += chr(i)
    else:
        output += chr(i-32)

format_string = "{0}"
print(format_string.format(output), end="")
