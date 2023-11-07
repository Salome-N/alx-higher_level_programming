#!/usr/bin/python3

def max_integer(my_list=[]):
    size = len(my_list)
    if size <= 0:
        return None

    max_i = my_list[0]
    for i in my_list:
        if i > max_i:
            max_i = i

    return max_i
