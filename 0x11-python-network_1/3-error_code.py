#!/usr/bin/python3
''' displays the body of the response '''
from sys import argv
from urllib.error import HTTPError
import urllib.request


if __name__ == '__main__':
    url = argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error as e:
        print("Error code: {}".format(e.code))
