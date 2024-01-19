#!/usr/bin/python3
""" lists all the states from hbtn_0e_0_usa database"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, 
                        user=argv[2], passwd=argv[3], db=argv[4])

    cur = db.cursor()
    
    rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    for i in rows:
        print(i)

    cur.close()
    db.close()
