#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = sys.argv
    result = 0
    for n in range(1, len(a)):
        result = result + int(a[n])
    print("{}".format(result))
