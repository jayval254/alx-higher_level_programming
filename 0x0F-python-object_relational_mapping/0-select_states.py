#!/usr/bin/python3
"""
Lists all states
"""
import MySQLdb
import sys


if __name__ == "__main__":
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=USERNAME,
        passwd=PASSWORD,
        db=DATABASE,
        port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
