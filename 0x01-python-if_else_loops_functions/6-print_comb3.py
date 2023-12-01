#!/usr/bin/python3
for n in range(10):
    for m in range(10):
        if n == 8 and m == 9:
            print("{}{}".format(n, m))
        elif n != m and m > n:
            print("{}{}, ".format(n, m), end="")
