#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends a POST request
to the URL with the email as a parameter, displays the body of the response"""


from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    url = argv[1]
    email = {"Your email is:": argv[2]}
    email = parse.urlencode(email).encode("ascii")
    with request.urlopen(url, email) as req:
        print(req.read().decode('utf-8'))
