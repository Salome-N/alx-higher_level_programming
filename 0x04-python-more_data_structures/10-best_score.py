#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = None
    for num in a_dictionary.num():
        if best is None or num > best:
            best = num

    return best
