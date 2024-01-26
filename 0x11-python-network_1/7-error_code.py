#!/usr/bin/python3
""" Fetches a given url with error handling"""


import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1]).txt
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)    
