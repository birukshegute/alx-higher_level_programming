#!/usr/bin/python3
""" It sends a POST request to the passed URL with email parameter,
and finally displays the body of the response."""


import requests
from sys import argv

if __name__ == "__main__":
    email = {'email': argv[2]}
    print(requests.post(argv[1], email).text)
