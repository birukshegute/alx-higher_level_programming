#!/usr/bin/python3
""" A script that takes your GitHub credentials to display an ID"""


import requests
from sys import argv

if __name__ == "__main__":
    passwd = (argv[1], argv[2])
    req = requests.get("https://api.github.com/user", auth=passwd)
    print(req.json().get("id"))
