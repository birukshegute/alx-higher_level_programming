#!/usr/bin/python3
""" lists all the states from hbtn_0e_0_usa database"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cute("SELECT * FROM states")

    rows = cur.fetchall()
    for i in rows:
        print(i)

    cur.close()
    db.close()
