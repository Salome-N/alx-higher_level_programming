#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        if (count < x):
            print("{}".format(my_list[count]), end="")
            count += 1
        else:
            break
        print("")
        return count
    except IndexError:
        return count
