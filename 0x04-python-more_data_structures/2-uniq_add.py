#!/usr/bin/python3

def uniq_add(my_list=[]):
    u_add = 0
    for n in (set(my_list)):
        u_add += n
    return u_add
