#!/usr/bin/python3
for i in range(0, 8):
    for j in range(0, 10):
        if i >= j:
            continue

        
        d = str(i) + str(j)
        x = "{:02}, ".format(int(d))
        print(x, end='')
print("89")
