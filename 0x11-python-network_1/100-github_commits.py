#!/usr/bin/python3
""" A script that lists 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”"""


import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10"\
          .format(argv[2], argv[1])

    req = requests.get(url)
    data = req.json()
    for i in data:
        print("{}: {}".format(i.get("sha"),
                              i.get("commit").get("author").get("name")))
