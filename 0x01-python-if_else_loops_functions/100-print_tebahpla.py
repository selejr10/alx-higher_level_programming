#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    r = chr(c)
    if (ord('z') - c) % 2 == 1:
        r = r.upper()
    print("{}".format(r), end="")
