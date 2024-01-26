#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the URL,
displays the body of the response"""

from sys import argv
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as req:
            print(req.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
