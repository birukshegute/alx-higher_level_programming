#!/usr/bin/python3
"""
Lists all cities from the database
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    sql = "SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    rows = cur.execute(sql)
    for i in range(rows):
        print(cur.fetchone())
    cur.close()
    db.close()
