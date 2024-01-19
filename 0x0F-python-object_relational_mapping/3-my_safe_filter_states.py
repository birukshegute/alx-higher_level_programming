#!/usr/bin/python3
"""
Lists all values in the states after taking arguements of database
Arg 4 safe from MySQL injections.
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name=%s ORDER BY states.id"
    rows = cur.execute(sql, (argv[4], ))
    for i in range(rows):
        print(cur.fetchone())
