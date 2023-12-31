#!/usr/bin/python3
"""Defines save object to a file function"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj (str): object
        filename (str): name of file
    """
    with open(filenmae, mode="w", encoding="utf-8") as txt:
        json.dumps(my_obj, txt)
