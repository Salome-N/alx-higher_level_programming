#!/usr/bin/python3
import sys

if __name__ == "__main__":
    c = len(sys.argv) - 1
    s = 0

    for a in range(c):
        s += int(sys.argv[a + 1])

    print(s)
