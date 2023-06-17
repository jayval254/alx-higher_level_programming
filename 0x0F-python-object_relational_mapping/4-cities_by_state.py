#!/usr/bin/python3
""" lists all cities from the database
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

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

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities, states WHERE states.id = state_id GROUP BY id")
    rows = cur.fetchall()
    for row in rows:
            print(row)

    cur.close()
    db.close()
