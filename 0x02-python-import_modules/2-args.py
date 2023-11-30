#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = sys.argv
    arg_num = len(a) - 1
    if arg_num == 0:
        print("0 arguments.")
    elif arg_num == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_num))
    for m in range(arg_num):
        print("{}: {}".format(m + 1, a[m + 1]))
