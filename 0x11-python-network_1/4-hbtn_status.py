#!/usr/bin/python3
""" a Python script that fetches a url"""


import requests

if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(req)))
    print("\t- content: {}".format(req))
