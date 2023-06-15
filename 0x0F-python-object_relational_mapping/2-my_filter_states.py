#!/usr/bin/python3
"""
SelectStates module
"""
import MySQLdb
import sys


def my_filter_state():
    """Filter states with the given name in database"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )
    cur = db.cursor()
    cur.execute("""SELECT *\
                FROM states\
                WHERE name LIKE BINARY '{}'\
                ORDER BY id ASC""".format(searched)
                )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    my_filter_state()
