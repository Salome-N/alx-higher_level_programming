#!/usr/bin/python3
''' Displays the value of the X-Request-Id variable
found in the header of the response '''
from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
