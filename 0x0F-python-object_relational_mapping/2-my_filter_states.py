#!/usr/bin/python3
"""
displays all values in the states table
"""
import MySQLdb
import sys


if __name__ == '__main__':
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE = sys.argv[3]
    ARG = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=USERNAME,
        passwd=PASSWORD,
        db=DATABASE,
        port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name='{}' COLLATE Latin1_General_CS ORDER BY id ASC".format(ARG))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
