#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL,
displays the value of the X-Request-Id variable found in the header"""


import sys
from urllib import request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as req:
        print(req.getheader("X-Request-Id"))
