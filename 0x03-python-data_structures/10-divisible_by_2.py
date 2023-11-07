#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divisible = []
    for n in my_list:
        divisible.append(True if n % 2 == 0 else False)

    return divisible
