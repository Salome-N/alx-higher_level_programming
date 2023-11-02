#!/usr/bin/python3
import sys

if __name__ == "__main__":
    c = len(sys.argv) - 1

    if c == 0:
        print("0 arguments.")
    elif c == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(c))
    for a in range(c):
        print("{}: {}".format(a + 1, sys.argv[a + 1]))
