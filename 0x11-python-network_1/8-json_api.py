#!/usr/bin/python3
""" a Python script that takes in a letter and
sends a POST request to url with letter as parameter"""


import requests
from sys import argv

if __name__ == "__main__":
    myVar = {"q": argv[1] if len(argv) > 1 else ""}
    req = requests.post("http://0.0.0.0:5000/search_user", data=myVar)
    try:
        json = request.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
