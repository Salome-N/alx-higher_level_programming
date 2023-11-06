#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    l = len(my_list)
    copy = my_list.copy()
    if idx < 0 or idx > l:
        return copy

    copy[idx] = element
    return copy
