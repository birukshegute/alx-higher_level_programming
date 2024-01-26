#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends a POST request
to the URL with the email as a parameter, displays the body of the response"""


import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = parse.urlencode({"Your email is:": sys.argv[2]}).encode("ascii")
    with request.urlopen(url, email) as req:
        print(req.read().decode('utf-8'))
