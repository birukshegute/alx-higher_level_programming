#!/usr/bin/python3
""" lists all the states from hbtn_0e_0_usa database"""
from sys import argv
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
                        user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    for i in range(rows):
        print(cur.fetchone())

    cur.close()
    db.close()
