#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for value in my_list:
            if (count < x):
                print("{value}", end="")
                count += 1
        print()
        return count
    except IndexError:
        return count
